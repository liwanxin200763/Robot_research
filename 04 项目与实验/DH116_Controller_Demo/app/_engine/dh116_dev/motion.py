"""Single-motor motion facade. Experiments never call a DLL directly."""

from __future__ import annotations

import time
import math
from ctypes import c_int, sizeof
from dataclasses import dataclass
from typing import Callable

from .device import FormalDevice
from .errors import DeviceError
from .state import (FeedbackSample, MotorState, utc_now,
                    stationary_feedback_changes, require_stationary_feedback,
                    PositionFeedbackFreshness, require_home_running_stable)


HOME_STOPPED = 0
HOME_RUNNING = 7

# Header: set_position_velocity(..., int velocity), encoder counts/second.
# CANFD protocol section "发送所有轴速度": a two-byte field per motor.
# These are representation guards, NOT a certified SDK/firmware speed limit;
# SDK-to-wire scaling and the actual device maximum are not documented locally.
SDK_POSITION_VELOCITY_UNIT = "SDK位置计数/秒（当量/秒；非度/秒）"
SDK_POSITION_VELOCITY_C_INT_MAX = (1 << (sizeof(c_int)*8-1))-1
SDK_POSITION_VELOCITY_REPRESENTATION_MAX = min(SDK_POSITION_VELOCITY_C_INT_MAX,0xffff)


def is_sdk_position_velocity(value) -> bool:
    """Positive SDK integer, bounded by C int and CANFD field capacity only."""
    return type(value) is int and 1 <= value <= SDK_POSITION_VELOCITY_REPRESENTATION_MAX


@dataclass(frozen=True)
class PositionPlan:
    motor_id: int
    target_position: int
    position_velocity: int
    current_raw: int
    home_before_move: bool
    control_mode: str
    motion_duration_ms: int
    physical_initial_pose: str

    @classmethod
    def from_fields(cls, fields: dict[str, str]) -> "PositionPlan":
        required = ("motor_id", "target_position", "position_velocity", "current_raw",
                    "home_before_move", "control_mode", "motion_duration_ms",
                    "physical_initial_pose")
        missing = [name for name in required if fields.get(name, "UNSET") in
                   ("UNSET", "NEEDS_ONSITE_CONFIRMATION", "")]
        if missing:
            raise ValueError("UNSET: " + ", ".join(missing))
        if fields["control_mode"] != "position":
            raise ValueError("control_mode must be explicitly position")
        if fields["home_before_move"] != "1":
            raise ValueError("normal SDK home is required before movement")
        if fields["physical_initial_pose"] != "zero_reference_pose":
            raise ValueError("physical_initial_pose must record zero_reference_pose")
        motor, target, velocity, current = (int(fields[name]) for name in required[:4])
        duration = int(fields["motion_duration_ms"])
        if not 1 <= motor <= 6 or not 0 <= target <= 10000 or velocity <= 0 or current <= 0 or duration <= 0:
            raise ValueError("invalid single-motor plan values")
        return cls(motor, target, velocity, current, True, "position", duration,
                   fields["physical_initial_pose"])


@dataclass(frozen=True)
class HomeCompletion:
    completion_timestamp_utc: str
    status_after: int
    observed_statuses: tuple[int, ...]


def wait_home_complete(motor_id: int, read_sample: Callable[[], FeedbackSample], *,
                       minimum_wait: float = 5.0, timeout: float = 15.0,
                       poll_seconds: float = 0.1) -> HomeCompletion:
    """等待厂家状态从 HOMING(7) 转为稳定 STOPPED(0)。"""
    if not 1 <= motor_id <= 6 or minimum_wait < 0 or timeout <= minimum_wait or poll_seconds < 0:
        raise ValueError("invalid home wait parameters")
    started = time.monotonic()
    deadline = started + timeout
    statuses: list[int] = []
    saw_homing = False
    stopped_samples = 0
    while True:
        if time.monotonic() >= deadline:
            raise TimeoutError("home completion timeout; move_motors skipped")
        sample = read_sample()
        target = next(m for m in sample.motors if m.motor_id == motor_id)
        statuses.append(target.status)
        if any(m.alarm != 0 for m in sample.motors):
            raise RuntimeError("alarm during home; move_motors skipped")
        if target.status == HOME_RUNNING:
            saw_homing = True
            stopped_samples = 0
        elif target.status == HOME_STOPPED:
            stopped_samples = stopped_samples + 1 if saw_homing else 0
        else:
            raise RuntimeError(f"invalid home status {target.status}; move_motors skipped")
        if time.monotonic() >= deadline:
            raise TimeoutError("home completion timeout; move_motors skipped")
        if (saw_homing and stopped_samples >= 2 and
                time.monotonic() - started >= minimum_wait):
            return HomeCompletion(utc_now(), target.status, tuple(statuses))
        remaining = deadline - time.monotonic()
        if remaining > 0 and poll_seconds > 0:
            time.sleep(min(poll_seconds, remaining))


class MotionController:
    def __init__(self, device: FormalDevice):
        self.device = device

    def _backend(self, operation: str):
        if self.device.state != "READY":
            raise DeviceError(operation, "device must be READY")
        backend = self.device.backend
        if not hasattr(backend, operation):
            raise DeviceError(operation, "backend does not implement motion API")
        return backend

    @staticmethod
    def _motor(motor_id: int) -> None:
        if not 1 <= motor_id <= 6:
            raise DeviceError("motion", "motor_id must be 1..6; broadcast disabled")

    def enable(self, motor_id: int) -> None:
        self._motor(motor_id)
        backend = self._backend("enable")
        sample = self.device.read_joint_states()
        if any(m.status != 0 or m.alarm != 0 for m in sample.motors):
            raise DeviceError("enable", "status/alarm precheck failed")
        backend.enable(motor_id)

    def enable_all(self) -> None:
        backend = self._backend("enable")
        sample = self.device.read_joint_states()
        if len(sample.motors) != 6 or any(m.status != 0 or m.alarm != 0 for m in sample.motors):
            raise DeviceError("enable_all", "six-motor status/alarm precheck failed")
        backend.enable(0)  # Official SDK ID 0 broadcasts to the six motors.

    def disable(self, motor_id: int) -> None:
        self._motor(motor_id)
        self._backend("disable").disable(motor_id)

    def disable_all(self) -> None:
        self._backend("disable").disable(0)

    def home(self, motor_id: int) -> None:
        self._motor(motor_id)
        backend = self._backend("home")
        homed = getattr(self.device, "homed_motor_ids", None)
        if homed is not None:
            homed.discard(motor_id)
            self.device.homed_this_session = bool(homed)
            self.device.homed_motor_id = next(iter(homed), None)
        else:
            self.device.homed_this_session = False
            self.device.homed_motor_id = None
        self.device.home_command_motor_id = None
        sample = self.device.read_joint_states()
        target = next(m for m in sample.motors if m.motor_id == motor_id)
        if target.status != HOME_STOPPED or any(m.alarm != 0 for m in sample.motors):
            raise DeviceError("home", "status/alarm precheck failed")
        backend.home(motor_id)
        self.device.home_command_motor_id = motor_id

    def home_all(self, *, read_sample: Callable[[], FeedbackSample] | None = None,
                 minimum_wait: float = 5.0, timeout: float = 15.0,
                 poll_seconds: float = 0.1,
                 on_dispatched: Callable[[], None] | None = None) -> dict[int, HomeCompletion]:
        backend = self._backend("home")
        sample = self.device.read_joint_states()
        if len(sample.motors) != 6 or any(m.status != HOME_STOPPED or m.alarm != 0
                                          for m in sample.motors):
            raise DeviceError("home_all", "six-motor status/alarm precheck failed")
        self.device.homed_this_session = False
        self.device.homed_motor_id = None
        self.device.home_command_motor_id = None
        self.device.homed_motor_ids.clear()
        backend.home(0)
        if on_dispatched is not None:
            on_dispatched()
        try:
            results = wait_home_complete_all(read_sample or self.device.read_joint_states,
                                             minimum_wait=minimum_wait, timeout=timeout,
                                             poll_seconds=poll_seconds)
        except BaseException:
            self.device.homed_motor_ids.clear()
            raise
        self.device.homed_motor_ids.update(range(1, 7))
        self.device.homed_this_session = True
        return results

    def wait_home_complete(self, motor_id: int, *,
                           read_sample: Callable[[], FeedbackSample] | None = None,
                           minimum_wait: float = 5.0, timeout: float = 15.0,
                           poll_seconds: float = 0.1) -> HomeCompletion:
        self._motor(motor_id)
        self._backend("home")
        if self.device.home_command_motor_id != motor_id:
            raise DeviceError("wait_home_complete", "HOME command not issued for this motor")
        try:
            completion = wait_home_complete(motor_id, read_sample or self.device.read_joint_states,
                                            minimum_wait=minimum_wait, timeout=timeout,
                                            poll_seconds=poll_seconds)
        except BaseException:
            self.device.homed_this_session = False
            self.device.homed_motor_id = None
            self.device.home_command_motor_id = None
            raise
        self.device.homed_this_session = True
        self.device.homed_motor_id = motor_id
        if hasattr(self.device, "homed_motor_ids"):
            self.device.homed_motor_ids.add(motor_id)
        self.device.home_command_motor_id = None
        return completion

    def stop(self, motor_id: int) -> None:
        self._motor(motor_id)
        self._backend("stop").stop(motor_id)

    def stop_all(self) -> None:
        self._backend("stop").stop(0)

    def set_position_mode_all(self) -> None:
        """Use only after monitored six-axis HOME in a scoped experiment."""
        self._backend("set_position_mode_all").set_position_mode_all()

    def move_position(self, motor_id: int, target: int, velocity: int,
                      current_raw: int) -> str:
        self._motor(motor_id)
        if not 0 <= target <= 10000 or velocity <= 0 or current_raw <= 0:
            raise DeviceError("move_position", "invalid plan values")
        homed = getattr(self.device, "homed_motor_ids", None)
        if (motor_id not in homed if homed is not None else
            not getattr(self.device, "homed_this_session", False) or
            getattr(self.device, "homed_motor_id", None) != motor_id):
            raise DeviceError("move_position", "verified HOME required for this motor in this session")
        backend = self._backend("position_command")
        sample = self.device.read_joint_states()
        if any(m.alarm != 0 for m in sample.motors):
            raise DeviceError("move_position", "alarm precheck failed")
        return backend.position_command(motor_id, target, velocity, current_raw)

    def move_positions(self, targets: dict[int, int], *, velocity: int,
                       current_raw: int,
                       on_dispatched: Callable[[dict[int, int], str], None] | None = None) -> str:
        """Dispatch a group; optional observer records and checks each completed SDK command."""
        if (not isinstance(targets, dict) or not targets or
                any(type(motor) is not int or not 1 <= motor <= 6 or
                    type(target) is not int or not 0 <= target <= 10000
                    for motor, target in targets.items()) or
                type(velocity) is not int or velocity <= 0 or
                type(current_raw) is not int or current_raw <= 0):
            raise DeviceError("move_positions", "invalid motor targets or raw controls")
        backend = self._backend("position_command")
        homed = getattr(self.device, "homed_motor_ids", set())
        if any(motor not in homed for motor in targets):
            raise DeviceError("move_positions", "verified HOME required for every target motor")
        sample = self.device.read_joint_states()
        if (len(sample.motors) != 6 or {m.motor_id for m in sample.motors} != set(range(1, 7)) or
                any(m.status != HOME_STOPPED or m.alarm != 0 for m in sample.motors)):
            raise DeviceError("move_positions", "six-motor status/alarm precheck failed")
        idle_reference = {m.motor_id: (m.now_position, m.now_angle_deg, m.target_position)
                          for m in sample.motors}
        if set(targets) == set(range(1, 7)) and hasattr(backend, "positions_command"):
            dispatched = backend.positions_command(targets, velocity, current_raw)
            if on_dispatched is not None:
                on_dispatched(dict(targets), dispatched)
            return dispatched
        dispatched = ""
        dispatched_motors: set[int] = set()
        for motor in sorted(targets):
            dispatched = backend.position_command(motor, targets[motor], velocity, current_raw)
            dispatched_motors.add(motor)
            if on_dispatched is not None:
                on_dispatched({motor: targets[motor]}, dispatched)
            # Enforce the same six-axis invariant even when no experiment observer is supplied.
            feedback = self.device.read_joint_states()
            if len(feedback.motors) != 6 or {m.motor_id for m in feedback.motors} != set(range(1, 7)):
                raise DeviceError("move_positions", "six-motor dispatch feedback incomplete")
            for axis in feedback.motors:
                if axis.alarm or axis.status not in ((HOME_STOPPED, 1) if axis.motor_id in dispatched_motors
                                                    else (HOME_STOPPED,)):
                    raise DeviceError("move_positions", f"Motor {axis.motor_id} unexpected dispatch status/alarm")
                if axis.motor_id not in dispatched_motors and (
                    axis.now_position, axis.now_angle_deg, axis.target_position
                ) != idle_reference[axis.motor_id]:
                    raise DeviceError("move_positions", f"Motor {axis.motor_id} idle feedback changed during dispatch")
        return dispatched

    def read_angle_limits(self,axes=(1,2,3,4,5,6)) -> dict[int,tuple[float,float]]:
        """READY-only SDK query; no enable, HOME or MOVE is issued here."""
        return self._backend("get_angle_limits").get_angle_limits(axes)

    def move_sdk_angles(self, angles: dict[int,float], held_targets: dict[int,int], *,
                        velocity: int,current_raw: int,tolerances: dict[int,float]) -> dict:
        """Native-angle console path; preserve existing raw-motion entry limits."""
        if (len(angles)!=1 or not set(angles)<=set(range(1,7)) or
                set(held_targets)!=set(range(1,7)) or
                any(type(v) is not int or not 0<=v<=10000 for v in held_targets.values()) or
                any(not math.isfinite(v) or v<0 for v in angles.values()) or
                not is_sdk_position_velocity(velocity) or current_raw!=1000):
            raise DeviceError("move_sdk_angles","invalid native angle session command")
        if not set(held_targets)<=getattr(self.device,"homed_motor_ids",set()):
            raise DeviceError("move_sdk_angles","six-axis HOME required in this session")
        backend=self._backend("native_angles_command")
        sample=self.device.read_joint_states()
        if (len(sample.motors)!=6 or {m.motor_id for m in sample.motors}!=set(held_targets) or
                any(m.status!=0 or m.alarm for m in sample.motors)):
            raise DeviceError("move_sdk_angles","six-axis status/alarm precheck failed")
        return backend.native_angles_command(angles,held_targets,velocity,current_raw,tolerances)

    def move_angles(self, angles: dict[int, float], targets: dict[int, int], *,
                    velocity: int, current_raw: int, raw_limits: dict[int, int]) -> dict:
        """Scoped SDK-angle command; existing raw MOVE methods are unchanged."""
        if (not angles or not set(angles) <= {1,2,3,4} or
                set(targets) != set(range(1,7)) or set(raw_limits) != set(targets) or
                any(not math.isfinite(v) for v in angles.values()) or
                any(type(v) is not int or not 0 <= v <= raw_limits[axis] <= 2000
                    for axis,v in targets.items()) or
                any(targets[axis] for axis in (5,6)) or
                (velocity,current_raw) != (500,1000)):
            raise DeviceError("move_angles","invalid mapped angle plan")
        if not set(targets) <= getattr(self.device,"homed_motor_ids",set()):
            raise DeviceError("move_angles","six-axis HOME required in this session")
        backend=self._backend("angles_command")
        sample=self.device.read_joint_states()
        if (len(sample.motors)!=6 or {m.motor_id for m in sample.motors}!=set(targets) or
                any(m.status!=0 or m.alarm for m in sample.motors)):
            raise DeviceError("move_angles","six-axis status/alarm precheck failed")
        return backend.angles_command(angles,targets,velocity,current_raw,raw_limits)

    def position_command(self, motor_id: int, target: int, velocity: int,
                         current_raw: int) -> str:
        """兼容 EXP02 旧名称；新调用使用 move_position。"""
        return self.move_position(motor_id, target, velocity, current_raw)


def wait_home_complete_all(read_sample: Callable[[], FeedbackSample], *,
                           minimum_wait: float = 5.0, timeout: float = 15.0,
                           poll_seconds: float = 0.1) -> dict[int, HomeCompletion]:
    """Verify HOMING(7) then two STOPPED(0) observations for every motor."""
    if minimum_wait < 0 or timeout <= minimum_wait or poll_seconds < 0:
        raise ValueError("invalid six-motor HOME wait parameters")
    started = time.monotonic()
    history: dict[int, list[int]] = {motor: [] for motor in range(1, 7)}
    homing: set[int] = set()
    stopped: dict[int, int] = {motor: 0 for motor in range(1, 7)}
    first_stop: dict[int, MotorState] = {}
    running_since: dict[int, float] = {}
    running_reference: dict[int, MotorState] = {}
    completed_state: dict[int, MotorState] = {}
    freshness = PositionFeedbackFreshness()
    while time.monotonic() - started < timeout:
        sample = read_sample()
        if len(sample.motors) != 6 or {m.motor_id for m in sample.motors} != set(range(1, 7)):
            raise RuntimeError("six-motor HOME feedback incomplete")
        if any(m.alarm != 0 for m in sample.motors):
            raise RuntimeError("alarm during six-motor HOME")
        # Legacy unit fixtures have no transport counter. Actual EXP05 reads
        # carry a positive READY counter and callback receipt time.
        advanced = freshness.observe(sample) if sample.position_frame_count > 0 else True
        for motor in sample.motors:
            if advanced:
                history[motor.motor_id].append(motor.status)
            if motor.status == 1:
                reference = completed_state.get(motor.motor_id,
                    first_stop.get(motor.motor_id, running_reference.setdefault(motor.motor_id,motor)))
                require_home_running_stable(reference,motor,running_since)
                completed_state.pop(motor.motor_id,None)
                stopped[motor.motor_id] = 0
                continue
            if motor.status in (HOME_STOPPED,HOME_RUNNING):
                running_since.pop(motor.motor_id,None)
                running_reference.pop(motor.motor_id,None)
            if motor.motor_id in completed_state:
                expected = completed_state[motor.motor_id]
                if motor.status != HOME_STOPPED or stationary_feedback_changes(expected, motor):
                    require_stationary_feedback(expected, motor, "HOME_COMPLETED")
                    raise RuntimeError(f"Motor {motor.motor_id} changed after verified HOME: "
                                       f"status before=0 after={motor.status}")
                continue
            if not advanced:
                if motor.motor_id in first_stop:
                    require_stationary_feedback(first_stop[motor.motor_id], motor, "HOME_FIRST_STOP")
                if motor.status not in (HOME_RUNNING, HOME_STOPPED, 1):
                    raise RuntimeError(f"invalid HOME status {motor.status} on Motor {motor.motor_id}")
                continue
            if motor.status == HOME_RUNNING:
                homing.add(motor.motor_id)
                stopped[motor.motor_id] = 0
            elif motor.status == HOME_STOPPED:
                if motor.motor_id in homing:
                    if motor.motor_id in first_stop:
                        require_stationary_feedback(first_stop[motor.motor_id], motor, "HOME_FIRST_STOP")
                    first_stop.setdefault(motor.motor_id, motor)
                    stopped[motor.motor_id] += 1
                else:
                    stopped[motor.motor_id] = 0
                if stopped[motor.motor_id] >= 2:
                    completed_state[motor.motor_id] = first_stop[motor.motor_id]
            else:
                raise RuntimeError(f"invalid HOME status {motor.status} on Motor {motor.motor_id}")
        if (len(completed_state) == 6 and
                time.monotonic() - started >= minimum_wait):
            completed = utc_now()
            return {motor: HomeCompletion(completed, HOME_STOPPED, tuple(history[motor]))
                    for motor in range(1, 7)}
        if poll_seconds:
            time.sleep(min(poll_seconds, max(0, started + timeout - time.monotonic())))
    raise TimeoutError("six-motor HOME completion timeout; MOVE skipped")
