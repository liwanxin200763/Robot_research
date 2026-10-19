"""Dedicated EXP05 HOME-only candidate with one-use onsite authorization.

No position, velocity, torque, gesture, or mode-switch API is used here.
Offline tests inject a synthetic backend; no MOVE API is reachable here.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, replace
import json
from pathlib import Path
import sys
import time
from typing import Callable

from dh116_dev.device import FormalDevice
from dh116_dev.logging import RunRecorder
from dh116_dev.models import DeviceConfig
from dh116_dev.motion import MotionController
from dh116_dev.state import (FeedbackSample, MotorState, utc_now,
                            require_stationary_feedback,
                            PositionFeedbackFreshness, RUNNING_TRANSITION_LIMIT_S,
                            require_home_running_stable)
from controller import safety


PROJECT_ROOT = Path(__file__).resolve().parents[3]
AXES = frozenset(range(1, 7))




def _connect_with_adapter_warning(device: FormalDevice, config: DeviceConfig,
                                  recorder: RunRecorder) -> None:
    """Prefer configured SN, otherwise accept only one VID/PID candidate."""
    adapters = device.scan()
    compatible = [item for item in adapters if
                  (item.vid, item.pid) == (config.adapter_vid, config.adapter_pid)]
    exact = [item for item in compatible if item.serial == config.adapter_serial]
    if len(exact) == 1:
        selected = exact[0]
        selection = "EXACT_SERIAL"
    elif not exact and len(compatible) == 1:
        selected = compatible[0]
        selection = "UNIQUE_VID_PID"
        device.config = replace(config, adapter_serial=selected.serial)
        recorder.event("identity_warning", field="adapter_serial",
                       configured=config.adapter_serial, actual=selected.serial,
                       reason="unique VID/PID adapter selected")
        print(f"WARNING: adapter serial differs: configured={config.adapter_serial}, "
              f"selected={selected.serial}", flush=True)
    else:
        raise RuntimeError("CANFD adapter selection is absent or ambiguous")
    recorder.set_experiment_metadata(actual_adapter_serial=selected.serial,
                                     adapter_selection=selection)
    device.connect(adapters)




class HomeOnlyMonitor:
    """Candidate software checks; none prove physical HOME or wire mode."""

    def __init__(self, on_transition: Callable[..., None] | None = None) -> None:
        self.last_position_frame_count: int | None = None
        self.feedback_freshness = PositionFeedbackFreshness()
        self.pre_enable: dict[int, MotorState] | None = None
        self.post_enable: dict[int, MotorState] | None = None
        self.home_targets: dict[int, int] | None = None
        self.seen_homing: set[int] = set()
        self.stopped_streak: dict[int, int] = {axis: 0 for axis in AXES}
        self.first_stop: dict[int, MotorState] = {}
        self.home_running_reference: dict[int, MotorState] = {}
        self.post_stop_running_pending: set[int] = set()
        self.on_transition = on_transition
        self.completed: dict[int, MotorState] = {}
        self.post_home: dict[int, MotorState] | None = None
        self.running_since: dict[int, float] = {}

    def check_stationary_status(self, motor: MotorState, phase: str, *,
                                allow_transition: bool,
                                transition_timeout: float | None = RUNNING_TRANSITION_LIMIT_S) -> None:
        if motor.status == 0:
            if motor.motor_id in self.running_since:
                started = self.running_since.pop(motor.motor_id)
                if self.on_transition:
                    self.on_transition("stationary_running_cleared", phase=phase,
                                       motor_id=motor.motor_id,
                                       duration_s=time.monotonic() - started)
            return
        if motor.status != 1 or not allow_transition:
            raise RuntimeError(f"M{motor.motor_id} {phase}: status before=0 after={motor.status}")
        now = time.monotonic()
        if motor.motor_id not in self.running_since:
            self.running_since[motor.motor_id] = now
            if self.on_transition:
                self.on_transition("stationary_running_observed", phase=phase,
                                   motor_id=motor.motor_id, status=1,
                                   physical_motion="UNKNOWN")
        elif transition_timeout is not None and now - self.running_since[motor.motor_id] > transition_timeout:
            raise RuntimeError(f"M{motor.motor_id} {phase}: RUNNING persisted "
                               f"duration_s={now-self.running_since[motor.motor_id]:.3f}")

    def validate_feedback(self, sample: FeedbackSample, phase: str) -> bool:
        """Shared six-axis freshness/alarm checks, including acquisition."""
        if len(sample.motors) != 6 or {m.motor_id for m in sample.motors} != AXES:
            raise RuntimeError("incomplete six-axis getter sample")
        for m in sample.motors:
            if m.alarm:
                raise RuntimeError(f"M{m.motor_id} {phase}: alarm before=0 after={m.alarm}")
        advanced = self.feedback_freshness.observe(sample)
        self.last_position_frame_count = sample.position_frame_count
        if self.on_transition:
            self.on_transition("position_feedback_freshness", phase=phase,
                position_frame_count=sample.position_frame_count, new_position_frame=advanced,
                last_received_utc=sample.last_position_feedback_utc,
                age_ms=self.feedback_freshness.age_seconds*1000,
                timestamp_source=self.feedback_freshness.source,
                scope="TRANSPORT_0x50_NOT_PER_AXIS_GETTER")
        return advanced

    def check(self, sample: FeedbackSample, phase: str) -> bool:
        advanced = self.validate_feedback(sample, phase)
        motors = {m.motor_id: m for m in sample.motors}
        if phase == "PRE_ENABLE":
            for m in sample.motors:
                self.check_stationary_status(m, phase, allow_transition=False)
            self.pre_enable = motors
        elif phase == "ENABLE_SETTLE":
            if self.pre_enable is None:
                raise RuntimeError("ENABLE: missing pre-enable baseline")
            for m in sample.motors:
                require_stationary_feedback(self.pre_enable[m.motor_id], m, "ENABLE")
                self.check_stationary_status(m, "ENABLE", allow_transition=True)
        elif phase == "PRE_HOME":
            if self.pre_enable is None:
                raise RuntimeError("PRE_HOME: missing pre-enable baseline")
            for m in sample.motors:
                reference = self.post_enable if self.post_enable is not None else self.pre_enable
                require_stationary_feedback(reference[m.motor_id], m, phase)
                self.check_stationary_status(m, phase, allow_transition=False)
            # HOME's target reference comes from this phase, not PRE_ENABLE.
            self.home_targets = {m.motor_id: m.target_position for m in sample.motors}
        elif phase == "HOME":
            if self.home_targets is None:
                raise RuntimeError("missing pre-dispatch six-axis HOME target baseline")
            for m in sample.motors:
                axis = m.motor_id
                if m.target_position != self.home_targets[axis]:
                    raise RuntimeError(f"Motor {axis} target changed during HOME: "
                                       f"before={self.home_targets[axis]} after={m.target_position}")
                if m.status == 1:
                    reference = self.completed.get(axis, self.first_stop.get(axis,
                        self.home_running_reference.setdefault(axis,m)))
                    was_pending = axis in self.post_stop_running_pending
                    require_home_running_stable(reference,m,self.running_since)
                    self.post_stop_running_pending.add(axis)
                    self.completed.pop(axis,None)
                    self.stopped_streak[axis] = 0
                    if self.on_transition is not None and not was_pending:
                        self.on_transition("home_post_stop_running_observed", motor_id=axis,
                            status=1, now_position=m.now_position, now_angle_deg=m.now_angle_deg,
                            target_position=m.target_position, alarm=m.alarm,
                            sample_utc=sample.timestamp_utc, physical_motion="UNKNOWN")
                    continue
                if m.status in (0,7):
                    self.running_since.pop(axis,None)
                    self.home_running_reference.pop(axis,None)
                if not advanced:
                    # Cached reads can still expose an alarm/target/drift, but
                    # cannot add HOMING/STOPPED observations or repeat RUNNING.
                    if axis in self.completed:
                        if m.status != 0:
                            raise RuntimeError(f"Motor {axis} changed after HOME completion: status={m.status}")
                        require_stationary_feedback(self.completed[axis], m, "HOME_COMPLETED")
                    elif axis in self.first_stop:
                        require_stationary_feedback(self.first_stop[axis], m, "HOME_FIRST_STOP")
                    if m.status not in (0,1,7):
                        raise RuntimeError(f"Motor {axis} unexpected HOME status {m.status}")
                    continue
                if axis in self.completed:
                    if m.status != 0:
                        raise RuntimeError(f"Motor {axis} changed after HOME completion: "
                                           f"status before=0 after={m.status}")
                    require_stationary_feedback(self.completed[axis], m, "HOME_COMPLETED")
                    continue
                if m.status == 7:
                    self.seen_homing.add(axis)
                    self.stopped_streak[axis] = 0
                elif m.status == 0:
                    if axis in self.seen_homing:
                        if axis in self.first_stop:
                            require_stationary_feedback(self.first_stop[axis], m, "HOME_FIRST_STOP")
                        self.first_stop.setdefault(axis, m)
                        self.stopped_streak[axis] += 1
                        if axis in self.post_stop_running_pending:
                            self.post_stop_running_pending.remove(axis)
                            if self.on_transition is not None:
                                self.on_transition("home_post_stop_running_cleared",
                                                   motor_id=axis, sample_utc=sample.timestamp_utc)
                        if self.stopped_streak[axis] >= 2:
                            self.completed[axis] = self.first_stop[axis]
                else:
                    raise RuntimeError(f"Motor {axis} unexpected HOME status {m.status}")
        elif phase in ("HOME_BASELINE", "POST_HOME_STABILITY"):
            for m in sample.motors:
                self.check_stationary_status(m,phase,allow_transition=True)
            if phase == "HOME_BASELINE":
                if self.seen_homing != AXES or set(self.completed) != AXES:
                    raise RuntimeError("six-axis HOME history incomplete")
                for m in sample.motors:
                    require_stationary_feedback(self.completed[m.motor_id], m, phase)
                    require_stationary_feedback(
                        MotorState(m.motor_id, m.target_position, m.now_angle_deg,
                                   m.target_position, 0, 0), m, phase)
                self.post_home = dict(self.completed)
            elif self.post_home is None:
                raise RuntimeError("missing post-HOME baseline")
            else:
                for m in sample.motors:
                    require_stationary_feedback(self.post_home[m.motor_id], m, phase)
        return advanced

    @staticmethod
    def _values(motor: MotorState) -> tuple:
        return (motor.now_position, motor.now_angle_deg, motor.target_position)
