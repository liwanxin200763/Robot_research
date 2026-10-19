"""One EXP05 session for single-axis, coordinated curl/open, or fixed-hand grasp.

Import and dry-run never construct a vendor backend. The ordinary EXP05 MOVE
gate stays locked; live access consumes a plan-bound one-use approval here.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass, replace
import json
import math
from pathlib import Path
import sys
import time
from typing import Callable, Iterable
from queue import Queue, Empty
from threading import Thread

from dh116_dev.device import FormalDevice
from dh116_dev.errors import DeviceError
from dh116_dev.logging import RunRecorder
from dh116_dev.models import DeviceConfig
from dh116_dev.motion import MotionController, is_sdk_position_velocity
from dh116_dev.state import (FeedbackSample, MotorState, utc_now,
                            require_stationary_feedback, feedback_measurement_policy,
                            FEEDBACK_POSITION_BAND_RAW,
                            stationary_feedback_changes, PositionFeedbackFreshness,
                            POSITION_FEEDBACK_TIMEOUT_S)
from controller import safety
from controller.home_monitor import (
    AXES, HomeOnlyMonitor, PROJECT_ROOT, _connect_with_adapter_warning,
    RUNNING_TRANSITION_LIMIT_S,
)


BOUNDS_PATH = PROJECT_ROOT / "config" / "exp05_motion_bounds.json"
IDLE_BROADCAST_RUNNING_GRACE_S = RUNNING_TRANSITION_LIMIT_S
ENABLE_ACQUISITION_TIMEOUT_S = 1.0  # Existing HOME-only enable observation window.
ENABLE_STABLE_SPAN_S = 0.2  # Three fresh samples at the existing 10 Hz polling.
NATIVE_IDLE_CONFIRM_SAMPLES = 3
NATIVE_IDLE_CONFIRM_SPAN_S = ENABLE_STABLE_SPAN_S
NATIVE_IDLE_MAX_OBSERVATION_S = RUNNING_TRANSITION_LIMIT_S
ENABLE_ACQUISITION_POLICY = {
    "all_axes": "TIME_BOUNDED_CONVERGENCE_NOT_STARTUP_DISPLACEMENT_LIMIT",
    "timeout_seconds": ENABLE_ACQUISITION_TIMEOUT_S,
    "stable_span_seconds": ENABLE_STABLE_SPAN_S,
    "minimum_fresh_samples": 3,
    "evidence": "b1c1c4 early getters cannot distinguish startup cache from adjustment",
    "mechanical_cause": "UNKNOWN_ENABLE_ADJUSTMENT_OR_CACHE_REFRESH",
    "manufacturer_safe_excursion_verified": False,
}




@dataclass(frozen=True)
class Stage:
    name: str
    targets: dict[int, int]
    active: tuple[int, ...]
    hold_seconds: float = 0.0
    angle_targets: dict[int, float] | None = None


@dataclass(frozen=True)
class SessionPlan:
    profile: str
    stages: tuple[Stage, ...]
    velocity: int
    current_raw: int
    global_max_raw: int = 2000
    requires_step_advance: bool = True
    amplitude_context: dict | None = None

    def as_dict(self) -> dict:
        return asdict(self)








def validate_session_plan(plan: SessionPlan) -> None:
    """Structural and global limits only; historical evidence is not a gate."""
    native_angle=(plan.profile=="angle" and
                  (plan.amplitude_context or {}).get("native_sdk_angle_control") is True)
    allowed = {"single": {1,2,3,4}, "three": {1,2,3,4}, "grasp": {1,2,3,4},
               "five": AXES, "return": AXES, "angle": AXES if native_angle else {1,2,3,4}}
    if (plan.profile not in allowed or not 1 <= len(plan.stages) <= 8 or
            type(plan.global_max_raw) is not int or not 0 < plan.global_max_raw <= (10000 if native_angle else 2000) or
            plan.current_raw != 1000 or
            (not is_sdk_position_velocity(plan.velocity) if native_angle else plan.velocity != 500)):
        raise ValueError("invalid profile, global maximum, velocity/current or stage count")
    if plan.stages[-1].name != "CONTROLLED_OPEN_RETURN" or any(plan.stages[-1].targets.values()):
        raise ValueError("session must finish with a zero-reference return")
    if plan.profile == "return" and len(plan.stages) != 1:
        raise ValueError("return profile permits only one zero-target stage")
    if plan.profile == "angle" and (len(plan.stages)!=2 or
            plan.stages[0].name!="ANGLE_SESSION_LIMITS" or plan.requires_step_advance):
        raise ValueError("angle sessions require a limits envelope and interactive input")
    expected = allowed[plan.profile]
    for stage in plan.stages:
        if (set(stage.targets) != AXES or not stage.active or
                stage.angle_targets is not None or
                len(set(stage.active)) != len(stage.active) or
                not set(stage.active) <= expected or
                (plan.profile == "single" and len(stage.active) != 1) or
                (plan.profile != "single" and set(stage.active) != expected) or
                any(type(v) is not int or not 0 <= v <= plan.global_max_raw for v in stage.targets.values()) or
                any(stage.targets[axis] != 0 for axis in AXES-set(stage.active)) or
                not math.isfinite(stage.hold_seconds) or not 0 <= stage.hold_seconds <= 30):
            raise ValueError("stage has invalid motor mapping, target, global maximum or hold time")




@dataclass(frozen=True)
class SessionResult:
    result: str
    directory: Path
    error: str | None
    cleanup: dict[str, str]


class CoordinatedStateMonitor(HomeOnlyMonitor):
    """One six-axis observer with command-scoped, anchored phase references."""

    def begin_acquisition(self, phase: str, reference: FeedbackSample) -> None:
        if phase not in ("PRE_ENABLE_ACQUIRE", "ENABLE"):
            raise ValueError("acquisition is limited to startup and ENABLE")
        self.acquisition_phase = phase
        starting = {m.motor_id: m for m in reference.motors}
        self.acquisition_reference = starting
        self.acquisition_candidate = starting
        self.acquisition_started = self.acquisition_stable_since = time.monotonic()
        self.acquisition_samples = 0  # Reference predates the command; count new reads only.
        self.acquisition_ready = False
        if self.on_transition:
            self.on_transition("feedback_acquisition_started", phase=phase,
                               policy=ENABLE_ACQUISITION_POLICY,
                               reference={axis:vars(m) for axis,m in self.acquisition_reference.items()})

    def check_acquisition(self, sample: FeedbackSample) -> bool:
        phase = self.acquisition_phase
        advanced = self.validate_feedback(sample, phase)
        now = time.monotonic()
        if now - self.acquisition_started >= ENABLE_ACQUISITION_TIMEOUT_S:
            raise TimeoutError(f"{phase}: no stable fresh six-axis feedback within 1 second")
        motors = {m.motor_id:m for m in sample.motors}
        for axis,m in motors.items():
            before = self.acquisition_reference[axis]
            if (not math.isfinite(m.now_position) or not math.isfinite(m.now_angle_deg)):
                raise RuntimeError(f"M{axis} {phase}: nonfinite position/angle")
            if m.target_position != before.target_position:
                raise RuntimeError(f"M{axis} {phase}: target_position before={before.target_position} after={m.target_position}")
            if m.status not in (0,1):
                raise RuntimeError(f"M{axis} {phase}: unexpected status={m.status}")
            # RUNNING and changed getters are provisional during acquisition,
            # not proof of safe motion. A fixed deadline (never renewed by
            # movement) and stationary fresh samples are required to proceed.
        if not advanced:
            return False  # Re-reading the same callback cannot certify settling.
        if any(stationary_feedback_changes(self.acquisition_candidate[axis],m)
               for axis,m in motors.items()) or any(m.status != 0 for m in motors.values()):
            if self.on_transition:
                self.on_transition("feedback_acquisition_candidate_changed", phase=phase,
                    elapsed_seconds=now-self.acquisition_started,
                    changes={axis:stationary_feedback_changes(self.acquisition_candidate[axis],m)
                             for axis,m in motors.items()},
                    physical_motion="UNKNOWN", acquisition_deadline_not_reset=True)
            self.acquisition_candidate = motors
            self.acquisition_stable_since = now
            self.acquisition_samples = 1
        else:
            self.acquisition_samples += 1
        self.acquisition_ready = (self.acquisition_samples >= 3 and
            now - self.acquisition_stable_since >= ENABLE_STABLE_SPAN_S and
            all(m.status == 0 for m in motors.values()))
        if self.acquisition_ready:
            if phase == "ENABLE":
                self.post_enable = dict(self.acquisition_candidate)
            else:
                self.pre_enable = dict(self.acquisition_candidate)
            if self.on_transition:
                self.on_transition("feedback_acquisition_stable", phase=phase,
                    fresh_samples=self.acquisition_samples,
                    elapsed_seconds=now-self.acquisition_started,
                    reference={axis:vars(m) for axis,m in self.acquisition_candidate.items()},
                    physical_zero_verified=False, mechanical_cause="UNKNOWN")
        return self.acquisition_ready

    def start_phase(self, phase: str, reference: FeedbackSample, *,
                    targets: dict[int, int], active: set[int],
                    broadcast: bool = False) -> None:
        if self.running_since:
            raise RuntimeError(f"{phase}: previous RUNNING transition has not cleared")
        prior_phase = getattr(self, "session_phase", None)
        prior_active = getattr(self, "active", set())
        anchors = getattr(self, "reference", {})
        # Re-anchor only channels with an authorized command, once on entering
        # that command and once after it completes. HOLD/NEXT and idle channels
        # retain their reference across phase boundaries, so +1,+2 cannot hide.
        self.reference = {m.motor_id: m if (
            m.motor_id not in anchors or
            phase in ("MOVE", "RETURN") and m.motor_id in active or
            phase == "HOLD" and prior_phase in ("MOVE", "RETURN") and m.motor_id in prior_active
        ) else anchors[m.motor_id] for m in reference.motors}
        self.session_phase = phase
        self.expected_targets = dict(targets)
        self.active = set(active)
        self.broadcast = broadcast
        if self.on_transition:
            self.on_transition("control_phase_entered", phase=phase,
                               baseline_utc=reference.timestamp_utc,
                               anchored_motor_reference={axis: vars(m) for axis, m in self.reference.items()},
                               targets=self.expected_targets, active=sorted(active))

    def check_native_idle(self,motor: MotorState,sample: FeedbackSample,*,advanced: bool) -> None:
        """Observe one deviation; confirm persistence against the FIXED anchor.

        This is limited to native-angle non-target axes after initialization.
        It does not classify the real 629a76 M6 sample as noise or safe motion.
        """
        axis=motor.motor_id;phase=self.session_phase
        if not math.isfinite(motor.now_position) or not -FEEDBACK_POSITION_BAND_RAW<=motor.now_position<=10000+FEEDBACK_POSITION_BAND_RAW:
            raise RuntimeError(f'M{axis} {phase}: invalid non-target raw feedback {motor.now_position}')
        self.check_stationary_status(motor,phase,allow_transition=True)
        changes=stationary_feedback_changes(self.reference[axis],motor)
        pending=self.native_idle_pending
        now=time.monotonic()
        if not changes:
            if axis in pending:
                first=pending.pop(axis)
                if self.on_transition:
                    self.on_transition('native_idle_variation_cleared',phase=phase,motor_id=axis,
                        duration_s=now-first['started'],reference=vars(self.reference[axis]),
                        sample_utc=sample.timestamp_utc,physical_stationarity_verified=False)
            return
        if axis not in pending:
            pending[axis]={'started':now,'fresh_samples':0,'first_sample_utc':sample.timestamp_utc}
            if self.on_transition:
                self.on_transition('native_idle_variation_observed',phase=phase,motor_id=axis,
                    reference=vars(self.reference[axis]),changes=changes,status=motor.status,
                    sample_utc=sample.timestamp_utc,physical_motion='UNKNOWN',
                    confirmation_samples=NATIVE_IDLE_CONFIRM_SAMPLES,
                    confirmation_span_s=NATIVE_IDLE_CONFIRM_SPAN_S,
                    maximum_observation_s=NATIVE_IDLE_MAX_OBSERVATION_S)
        first=pending[axis]
        if advanced:first['fresh_samples']+=1
        elapsed=now-first['started']
        if ((first['fresh_samples']>=NATIVE_IDLE_CONFIRM_SAMPLES and elapsed>=NATIVE_IDLE_CONFIRM_SPAN_S-1e-9) or
                elapsed>=NATIVE_IDLE_MAX_OBSERVATION_S):
            if self.on_transition:
                self.on_transition('native_idle_persistent_change',phase=phase,motor_id=axis,
                    reference=vars(self.reference[axis]),changes=changes,elapsed_seconds=elapsed,
                    fresh_samples=first['fresh_samples'],first_sample_utc=first['first_sample_utc'])
            raise RuntimeError(f'M{axis} {phase}: persistent non-target change; '
                               f'fixed_reference={vars(self.reference[axis])}; changes={changes}; '
                               f'fresh_samples={first["fresh_samples"]} duration_s={elapsed:.3f}')

    def check_phase(self, sample: FeedbackSample) -> None:
        phase = self.session_phase
        advanced=self.validate_feedback(sample, phase)
        for motor in sample.motors:
            axis = motor.motor_id
            if motor.alarm:
                raise RuntimeError(f"M{axis} {phase}: alarm before=0 after={motor.alarm}")
            if not math.isfinite(motor.now_angle_deg):
                raise RuntimeError(f"M{axis} {phase}: now_angle_deg={motor.now_angle_deg}")
            if motor.target_position != self.expected_targets[axis]:
                raise RuntimeError(f"M{axis} {phase}: target_position "
                                   f"before={self.expected_targets[axis]} after={motor.target_position}")
            if (getattr(self,'native_idle_observation',False) and
                    phase in ('MOVE','RETURN','HOLD') and axis not in self.active):
                self.check_native_idle(motor,sample,advanced=advanced)
                continue
            if phase == "POSITION_MODE" or axis not in self.active:
                require_stationary_feedback(self.reference[axis], motor, phase)
                self.check_stationary_status(motor, phase,
                    allow_transition=(phase == "POSITION_MODE" or self.broadcast),
                    # A broadcast addresses even held M5/M6. Stationary status
                    # 1 is observed until the command deadline; it is neither
                    # motion proof nor completion. Drift/target/alarm fail now.
                    transition_timeout=(None if self.broadcast and phase in ("MOVE","RETURN")
                                        else RUNNING_TRANSITION_LIMIT_S))
            elif phase == "HOLD":
                require_stationary_feedback(self.reference[axis], motor, phase)
                if abs(motor.now_position - self.expected_targets[axis]) > 5:
                    raise RuntimeError(f"M{axis} HOLD: now_position "
                                       f"before={self.expected_targets[axis]} after={motor.now_position} "
                                       "completion_band=5")
                self.check_stationary_status(motor, phase, allow_transition=True)
            elif motor.status not in (0, 1):
                raise RuntimeError(f"M{axis} {phase}: status allowed=[0,1] after={motor.status}")


def run_session(config: DeviceConfig, backend_factory: Callable,
                recorder: RunRecorder, plan: SessionPlan, *,
                approval: safety.HomeOnlyApproval | None,
                step_input: Callable[[str], str] = input,
                minimum_wait: float = 5.0, home_timeout: float = 15.0,
                move_timeout: float = 15.0, poll_seconds: float = 0.1,
                stage_source: Callable[[Callable[[], FeedbackSample], FeedbackSample], Iterable[Stage]] | None = None,
                on_initialized: Callable[[MotionController],None] | None = None,
                session_velocity_source: Callable[[],int] | None = None) -> SessionResult:
    """Broadcast HOME once, then execute reviewed stages in one open session."""
    validate_session_plan(plan)
    if (plan.profile == "angle") != (stage_source is not None):
        raise ValueError("interactive stage source is restricted to the angle session envelope")
    native_angle=(plan.profile=="angle" and
                  (plan.amplitude_context or {}).get("native_sdk_angle_control") is True)
    if native_angle and on_initialized is None:
        raise ValueError("native angle sessions require SDK limits query before enable/HOME")
    if session_velocity_source is not None and (not native_angle or not (plan.amplitude_context or {}).get("interactive_speed_updates")):
        raise ValueError("speed updates require the approved native angle session policy")
    safety.require_motion_session_approval(approval, config, recorder.run_id, plan.as_dict())
    recorder.set_experiment_metadata(motion_plan=plan.as_dict(),
                                     dispatch="PER_AXIS_SDK_MOVE_IDS_ONLY" if native_angle else "SINGLE_MOTOR_OR_SIX_AXIS_BROADCAST",
                                     native_idle_observer={
                                         "enabled":native_angle,"fixed_reference":True,
                                         "detector_raw_band":FEEDBACK_POSITION_BAND_RAW,
                                         "confirmation_samples":NATIVE_IDLE_CONFIRM_SAMPLES,
                                         "confirmation_span_s":NATIVE_IDLE_CONFIRM_SPAN_S,
                                         "maximum_observation_s":NATIVE_IDLE_MAX_OBSERVATION_S,
                                         "physical_cause":"UNKNOWN_SINGLE_SAMPLE_NOT_CLASSIFIED_AS_NOISE",
                                         "source_run":"20261018T085459976804Z-629a76"},
                                     control_phases=["CONNECT", "ENABLE", "HOME", "POSITION_MODE",
                                                     "MOVE", "HOLD", "RETURN", "CLEANUP"],
                                     capture_policy="BOUNDED_QUEUE_CONTINUOUS_DRAIN_WITH_BATCH_DISK_FLUSH",
                                     next_wait_six_axis_monitoring=True,
                                     normal_return_requires_next=False,
                                     cleanup_control_before_log_io=True,
                                     feedback_measurement_band=feedback_measurement_policy(),
                                     enable_acquisition=ENABLE_ACQUISITION_POLICY,
                                     position_feedback_timeout_seconds=POSITION_FEEDBACK_TIMEOUT_S,
                                     position_feedback_timeout_evidence="e6237a READY median=1ms p99=5ms max=14ms",
                                     position_feedback_scope="0x50 TRANSPORT NOT PER_AXIS_CACHE_PROOF; 5A1F DOES_NOT_RENEW",
                                     physical_motion_verified=False)
    recorder.event("onsite_approval_consumed", run_id=recorder.run_id,
                   plan=plan.as_dict())
    device = None
    motion = None
    enabled = False
    phase = "STARTING"
    cleanup: dict[str, str] = {}
    error = None
    result = "FAILED"
    capture_errors: list[str] = []
    cleanup_events: list[tuple[str, dict]] = []
    home_monitor = CoordinatedStateMonitor(on_transition=recorder.event)
    home_monitor.native_idle_observation=native_angle
    home_monitor.native_idle_pending={}
    capture_freshness = PositionFeedbackFreshness()
    mode_submission_seen = False

    def soft_event(name: str, **fields) -> None:
        """Cleanup diagnostics cannot prevent the actual stop/disable/close."""
        try:
            recorder.event(name, **fields)
        except Exception as caught:
            detail = f"{name}: {type(caught).__name__}: {caught}"
            if detail not in capture_errors:
                capture_errors.append(detail)
            try:
                print(f"LOG_WRITE_FAILED {detail}", file=sys.stderr, flush=True)
            except Exception as output_error:
                capture_errors.append(f"stderr diagnostic failed: {output_error}")

    def device_event(name: str, **fields) -> None:
        if phase == "CLEANUP":
            defer_cleanup_event(name, **fields)
        else:
            recorder.event(name, **fields)

    def defer_cleanup_event(name: str, **fields) -> None:
        # Emergency control has priority over disk I/O. This small queue is
        # bounded independently of the receive log and flushed after close.
        if len(cleanup_events) < 256:
            cleanup_events.append((name, {"timestamp_utc": utc_now(), **fields}))
        elif "cleanup diagnostic queue full" not in capture_errors:
            capture_errors.append("cleanup diagnostic queue full")

    def drain(*, enforce_capture: bool = True) -> None:
        nonlocal mode_submission_seen
        if device is None:
            return
        for row in device.drain_pending_transport_events():
            recorder.event("transport_event", experiment_phase=phase, **row)
            if (row.get("kind") == "HOST_USB_WRITE_COMPLETED" and
                    row.get("can_id") == 0x500 + config.node_id):
                try:
                    payload = bytes.fromhex(row.get("callback_payload_hex", ""))
                except ValueError:
                    payload = b""
                if (native_angle and phase in ('MOVE','RETURN') and len(payload)>=2 and
                        payload[0] in (0x01,0x02,0x03,0x04,0x81,0x82,0x83,0x84) and payload[1]==6):
                    recorder.event('sdk_multi_axis_field_frame',phase=phase,
                        sdk_requested_motors=sorted(home_monitor.active),
                        frame_type=payload[0],wire_axis_fields=6,payload_hex=payload.hex().upper(),
                        direction='HOST_TO_ADAPTER',device_acknowledged='UNKNOWN',
                        wire_axis_scope='SDK_MANAGED_NOT_PROVEN_ISOLATED',
                        note='Six-axis fields do not establish a call to move_motors(0) or physical motion')
                if len(payload) >= 14 and payload[0] in (0x01, 0x81) and payload[1] == 6:
                    modes = payload[2:14:2]
                    controls = payload[3:14:2]
                    recorder.event("mode_control_host_submission", phase=phase,
                                   modes=list(modes), controls=list(controls),
                                   device_accepted="UNKNOWN")
                    if phase == "HOME" and any(mode != 0x25 for mode in modes):
                        raise RuntimeError("unexpected mode submission during HOME")
                    if phase == "POSITION_MODE" and all(mode == 0x20 for mode in modes):
                        mode_submission_seen = True
        try:
            recorder.raw_frames(device.drain_pending_feedback(), experiment_phase=phase)
        except Exception as caught:
            capture_errors.append(f"raw_log_writer: {type(caught).__name__}: {caught}")
            raise
        raw_drops = getattr(device.backend, "dropped_raw_frames", 0)
        tx_drops = getattr(device.backend, "dropped_transport_events", 0)
        if raw_drops or tx_drops:
            fault_event = recorder.event if enforce_capture else soft_event
            fault_event("capture_fault", phase=phase,
                           source="PYTHON_LOG_CAPTURE_QUEUES_NOT_CANFD_RECEIVE_BUFFER",
                           dropped_raw_frames=raw_drops, dropped_transport_events=tx_drops,
                           raw_log_queue_capacity=getattr(
                               getattr(device.backend, "_raw_frames", None), "maxlen", None),
                           transport_log_queue_capacity=getattr(
                               getattr(device.backend, "_transport_events", None), "maxlen", None),
                           device_communication_health="NOT_DETERMINED_BY_LOG_LOSS")
            detail = (f"transport capture overflow: raw_log_queue dropped={raw_drops}; "
                      f"transport_log_queue dropped={tx_drops}")
            if enforce_capture:
                raise RuntimeError(detail)
            if detail not in capture_errors:
                capture_errors.append(detail)

    def capture(home_phase: str | None = None) -> FeedbackSample:
        while True:
            drain()
            started = utc_now()
            try:
                sample = device.read_joint_states()
            finally:
                recorder.event("getter_window", phase=phase, started_utc=started,
                               finished_utc=utc_now(), source="SDK_GETTER_NONATOMIC")
                drain()
            recorder.sample(sample, experiment_phase=phase)
            # Keep all phase safety checks active even on a cached read. Only
            # return a new receipt to loops that count completion/stability.
            if home_phase:
                home_monitor.check(sample, home_phase)
            elif phase in ("PRE_ENABLE_ACQUIRE", "ENABLE"):
                home_monitor.check_acquisition(sample)
            elif phase in ("POSITION_MODE", "MOVE", "HOLD", "RETURN"):
                home_monitor.check_phase(sample)
                modes = {axis: device.backend.read_control_mode(axis) for axis in AXES}
                recorder.event("six_axis_control_modes", phase=phase, modes=modes,
                               source="SDK_GETTER_NOT_WIRE_MODE_PROOF")
                for axis, mode in modes.items():
                    if mode != 0:
                        raise RuntimeError(f"M{axis} {phase}: control_mode before=0 after={mode}")
            if capture_freshness.observe(sample):
                return sample
            recorder.event("waiting_for_position_feedback", phase=phase,
                           age_ms=capture_freshness.age_seconds*1000,
                           position_frame_count=sample.position_frame_count,
                           counted_as_new_feedback=False)
            time.sleep(min(poll_seconds, .005))

    def command(name: str, function: Callable, *args):
        recorder.event("sdk_command_started", command=name, phase=phase,
                       args=list(args), device_accepted="UNKNOWN")
        try:
            returned = function(*args)
        except BaseException as caught:
            recorder.event("sdk_command_failed", command=name, phase=phase,
                           error=str(caught), sdk_code=getattr(caught, "code", None))
            raise
        recorder.event("sdk_command_completed", command=name, phase=phase,
                       timestamp_utc=utc_now(), sdk_result=returned,
                       device_accepted="UNKNOWN")
        drain()
        return returned

    def wait_stationary_clear(sample: FeedbackSample) -> FeedbackSample:
        started = time.monotonic()
        while (home_monitor.running_since or home_monitor.native_idle_pending or
               any(m.status != 0 for m in sample.motors)):
            if time.monotonic() - started >= move_timeout:
                raise TimeoutError(f"{phase}: stationary transition not cleared")
            time.sleep(poll_seconds)
            sample = capture()
        return sample

    def wait_next(stage_name: str, targets: dict[int,int], *, place_object: bool = False) -> str:
        # Only keyboard input runs in this daemon thread. All SDK reads, state
        # checks, bounded-queue drains and disk writes stay on the control thread.
        answers: Queue = Queue(maxsize=1)
        def read_answer() -> None:
            try:
                answers.put((True, step_input(
                    f"{stage_name}: " + ("PLACE_OBJECT: place light cube only while open; " if place_object else "") +
                    f"next raw targets={targets}. Observe thumb lateral/flexion, index and middle. "
                    "Type NEXT to allow this step, RETURN to open now, STOP to stop: ")))
            except BaseException as caught:
                answers.put((False, caught))
        Thread(target=read_answer, name="exp05-next-input", daemon=True).start()
        recorder.event("stage_advance_wait_started", stage=stage_name,
                       six_axis_monitoring="ACTIVE", capture="CONTINUOUS_BOUNDED_DRAIN")
        while True:
            # Also recheck on the iteration receiving NEXT: input is not a
            # substitute for a fresh six-axis pre-command safety snapshot.
            wait_stationary_clear(capture())
            try:
                ok, answer = answers.get_nowait()
            except Empty:
                time.sleep(poll_seconds)
                continue
            if not ok:
                raise answer
            recorder.event("stage_advance_answer", stage=stage_name, answer=answer)
            return answer

    try:
        for startup_attempt in (1,2):
            device = FormalDevice(config, backend_factory(), device_event)
            phase = "CONNECT"
            _connect_with_adapter_warning(device, config, recorder)
            phase = "INITIALIZE"
            try:
                info = device.initialize()
                break
            except DeviceError as caught:
                # Only initial_ex receive failure, before enable/HOME/MOVE.
                # Recreate the entire SDK/adapter session, never re-use a
                # failed handle or retry a motion command.
                if startup_attempt != 1 or caught.code != 7 or device.state != "INITIALIZING":
                    raise
                recorder.event("startup_receive_error",attempt=startup_attempt,error=str(caught))
                phase = "STARTUP_RETRY_CLOSE"
                try:
                    device.close()
                except BaseException as close_error:
                    cleanup["startup_attempt_1_close"] = f"FAILED: {close_error}"
                    recorder.event("startup_retry_close_failed",error=str(close_error),retry=False)
                    raise
                cleanup["startup_attempt_1_close"] = "COMPLETED"
                drain(enforce_capture=False)
                recorder.event("startup_retry_close_completed",retry=True)
                print("initial_ex Error 7: closed failed session; retrying startup once (no motion).",flush=True)
                device = None
                time.sleep(.2)
        recorder.set_hand_info(info)
        # FormalDevice.initialize already checks 11/6 DOF. Keep the actual SDK
        # hand-type guard; no repeated serial/version/side authentication.
        if info.sdk_hand_type != 0:
            raise RuntimeError("SDK hand type is not DH116")
        motion = MotionController(device)
        if on_initialized is not None:
            phase="SDK_ANGLE_LIMITS"
            on_initialized(motion)
        phase = "PRE_ENABLE"
        sample = capture("PRE_ENABLE")
        # The first READY getter can still be a cold-cache zero (b1c1c4
        # had only one READY 0x50). Acquire a bounded stable reference first.
        phase = "PRE_ENABLE_ACQUIRE"
        home_monitor.begin_acquisition(phase, sample)
        while True:
            time.sleep(poll_seconds)
            sample = capture()
            if home_monitor.acquisition_ready:
                break
        enabled = True
        phase = "ENABLE"
        # Start the deadline before the actual SDK call, not after it.
        home_monitor.begin_acquisition(phase, sample)
        command("enable_all", motion.enable_all)
        while True:
            sample = capture()
            if home_monitor.acquisition_ready:
                break
            time.sleep(poll_seconds)
        phase = "PRE_HOME"
        capture("PRE_HOME")
        phase = "HOME"
        recorder.event("video_sync_marker", marker="HOME_START")
        command("home_all", lambda: motion.home_all(
            read_sample=lambda: capture("HOME"), minimum_wait=minimum_wait,
            timeout=home_timeout, poll_seconds=poll_seconds))
        phase = "HOME_BASELINE"
        sample = capture("HOME_BASELINE")
        while home_monitor.running_since:
            time.sleep(poll_seconds)
            sample = capture("HOME_BASELINE")
        phase = "POSITION_MODE"
        home_monitor.start_phase(phase, replace(sample, motors=tuple(home_monitor.post_home.values())), targets={m.motor_id: m.target_position
                                                       for m in sample.motors}, active=set())
        command("set_position_mode_all", motion.set_position_mode_all)
        mode_wait_started = time.monotonic()
        while not mode_submission_seen and time.monotonic() - mode_wait_started < 0.5:
            time.sleep(poll_seconds)
            drain()
        if not mode_submission_seen:
            raise RuntimeError("position-mode host submission was not captured")
        mode_started = time.monotonic()
        stopped_samples = 0
        while time.monotonic() - mode_started < home_timeout:
            sample = capture()
            stopped_samples = stopped_samples + 1 if all(m.status == 0 for m in sample.motors) else 0
            if stopped_samples >= 2:
                break
            time.sleep(poll_seconds)
        else:
            raise TimeoutError("POSITION_MODE: stopped six-axis feedback not established")
        # HOME already verified position against its target. Preserve that
        # measured reference, including angle offset; do not require a second
        # independently fabricated all-zero angle/position snapshot here.
        baseline = capture()
        previous = baseline
        last_dispatch_broadcast = False
        if stage_source is not None:
            phase="HOLD"
            home_monitor.start_phase(phase,baseline,
                targets={m.motor_id:m.target_position for m in baseline.motors},active=set())
        stages=stage_source(capture,baseline) if stage_source is not None else plan.stages
        for stage_index, stage in enumerate(stages, 1):
            stage_velocity = session_velocity_source() if session_velocity_source is not None else plan.velocity
            if not is_sdk_position_velocity(stage_velocity):
                raise ValueError("invalid session position velocity")
            recorder.event("session_speed_applied", velocity=stage_velocity, stage=stage.name)
            if stage_source is not None:
                # The approved plan is a bounds envelope, NEVER a set of
                # automatic curl targets. Validate every keyboard-produced step.
                limits=plan.stages[0].targets
                is_return=stage.name=="CONTROLLED_OPEN_RETURN"
                requested=stage.angle_targets or {}
                previous_targets={m.motor_id:m.target_position for m in previous.motors}
                if (set(stage.targets)!=AXES or stage.hold_seconds!=0 or
                        any(type(v) is not int or not 0<=v<=limits[axis]
                            for axis,v in stage.targets.items()) or
                        is_return and (any(stage.targets.values()) or requested or set(stage.active)!=AXES) or
                        not is_return and (not requested or not set(requested)<=(AXES if native_angle else {1,2,3,4}) or
                            set(stage.active)!=set(requested) or
                            any(not math.isfinite(v) for v in requested.values()) or
                            any(stage.targets[axis]!=previous_targets[axis] for axis in AXES-set(requested)))):
                    raise ValueError("interactive command exceeds approved angle-session envelope")
            if native_angle:
                # Resolve an observed non-target transient before crossing a
                # phase boundary or issuing another command; do not re-anchor it.
                wait_stationary_clear(capture())
            phase = "HOLD"
            home_monitor.start_phase(phase, previous,
                targets={m.motor_id: m.target_position for m in previous.motors},
                active=set(stage.active), broadcast=last_dispatch_broadcast)
            if (stage_source is None and stage_index > 1 and plan.requires_step_advance and
                    stage.name != "CONTROLLED_OPEN_RETURN"):
                place_object = plan.profile == "grasp" and stage_index == 2
                answer = wait_next(stage.name,stage.targets,place_object=place_object)
                if place_object:
                    recorder.event("object_placement_answer",answer=answer,
                                   physical_contact_verified=False, physical_grasp_verified=False)
                if answer == "RETURN":
                    recorder.event("operator_requested_controlled_return",skipped_stage=stage.name)
                    stage = plan.stages[-1]
                elif answer != "NEXT":
                    raise RuntimeError("operator stopped staged motion")
            before = wait_stationary_clear(capture())
            active = {axis for axis in stage.active if stage.targets[axis] !=
                      home_monitor.expected_targets[axis]}
            if native_angle and stage.angle_targets is not None:
                # Raw targets are unknown until the SDK itself processes the
                # angle setter. No local historical ratio is extrapolated.
                active=set(stage.angle_targets)
            zero_only_return = plan.profile == "return" or (stage_source is not None and stage.name=="CONTROLLED_OPEN_RETURN")
            if zero_only_return:
                # HOME may already have established zero. This command still
                # dispatches a real six-axis zero target, rather than aliasing HOME.
                active = set(AXES)
            if not active:
                recorder.event("stage_no_motion", stage=stage.name)
                if stage.name == "CONTROLLED_OPEN_RETURN" and stage_source is None:
                    break
                continue
            idle = {m.motor_id: m for m in before.motors}
            phase = "RETURN" if stage.name == "CONTROLLED_OPEN_RETURN" or (native_angle and stage.name=='ANGLE_RETURN') else "MOVE"
            single_dispatch=(plan.profile=="single" or
                             stage.angle_targets is not None and len(stage.angle_targets)==1)
            home_monitor.start_phase(phase, before, targets=stage.targets, active=active,
                                     broadcast=not single_dispatch)
            recorder.event("video_sync_marker", marker=f"{stage.name}_MOVE_START",
                           targets=stage.targets)
            display_stage = "RETURN" if phase == "RETURN" else stage.name
            if native_angle and stage.angle_targets is not None:
                print(f"{display_stage}: DISPATCH SDK_angles={stage.angle_targets} "
                      f"SDK_move_id={next(iter(stage.angle_targets))}; six-axis snapshot is monitoring only",flush=True)
            else:
                print(f"{display_stage}: DISPATCH targets={stage.targets}", flush=True)
            if stage.angle_targets is not None:
                dispatch="SINGLE_AXIS" if single_dispatch else "SIX_AXIS_BROADCAST_WITH_IDLE_HOLD"
                if native_angle:
                    tolerances=(plan.amplitude_context or {})["angle_tolerances_deg"]
                    native=command("move_sdk_angles",lambda:motion.move_sdk_angles(
                        stage.angle_targets,stage.targets,velocity=stage_velocity,
                        current_raw=plan.current_raw,tolerances=tolerances))
                else:
                    native=command("move_angles",lambda:motion.move_angles(
                        stage.angle_targets,stage.targets,velocity=stage_velocity,
                        current_raw=plan.current_raw,raw_limits=plan.stages[0].targets))
                effective=native["effective_targets"]
                if (set(effective)!=AXES or any(type(v) is not int or
                        not 0<=v<=plan.stages[0].targets[axis] or
                        (not native_angle and abs(v-stage.targets[axis])>1)
                        for axis,v in effective.items())):
                    raise RuntimeError("invalid native angle conversion readback")
                recorder.event("angle_native_conversion",requested_angles=stage.angle_targets,
                               predicted_targets=None if native_angle else stage.targets,
                               sdk_limits=native.get("sdk_limits"),sdk_accepted=native.get("sdk_accepted"),
                               requested_position_velocity=stage_velocity,
                               sdk_position_velocity=native.get("sdk_position_velocity"),
                               speed_readback_source=native.get("speed_readback_source"),
                               effective_targets=effective,
                               source="SDK_LOCAL_CACHE_NOT_DEVICE_ACK")
                stage=replace(stage,targets=dict(effective))
                home_monitor.expected_targets=dict(effective)
                if native_angle:
                    print(f"SDK_ACCEPTED=YES target_sdk_angles={stage.angle_targets} "
                          f"sdk_command_raw_targets={ {axis:effective[axis] for axis in stage.angle_targets} } "
                          f"TARGET_REACHED=UNCONFIRMED DEVICE_ACK=UNKNOWN",flush=True)
            elif len(active) == 1 and plan.profile == "single":
                axis = next(iter(active))
                dispatch = "SINGLE_AXIS"
                command("move_position", motion.move_position, axis,
                        stage.targets[axis], stage_velocity, plan.current_raw)
            else:
                # Vendor SDK sample preloads all six and issues move_motors(0).
                # M5/M6 may receive hold commands in the three-finger profile.
                if not hasattr(device.backend, "positions_command"):
                    raise RuntimeError("backend lacks one-dispatch broadcast MOVE")
                dispatch = "SIX_AXIS_BROADCAST_WITH_IDLE_HOLD"
                command("move_positions_broadcast", lambda: motion.move_positions(
                    stage.targets, velocity=stage_velocity,
                    current_raw=plan.current_raw))
            recorder.event("move_dispatched", stage=stage.name, dispatch=dispatch,
                           targets=({axis:stage.targets[axis] for axis in stage.angle_targets}
                                    if native_angle and stage.angle_targets is not None else stage.targets),
                           six_axis_target_snapshot=stage.targets,
                           sdk_move_ids=sorted(stage.angle_targets) if native_angle and stage.angle_targets is not None else None,
                           wire_axis_scope="SDK_MANAGED_NOT_PROVEN_ISOLATED" if native_angle else "NOT_ASSESSED",
                           active=sorted(active),
                           displacement_required=not zero_only_return,
                           timestamp_utc=utc_now(), physical_motion_verified=False)
            last_dispatch_broadcast = dispatch == "SIX_AXIS_BROADCAST_WITH_IDLE_HOLD"
            started = time.monotonic()
            # Native angles may legitimately exceed the historical 2000-raw
            # points. Use SDK-returned distance and the unchanged raw/s speed,
            # not an extrapolated angle/raw ratio, to bound travel time.
            stage_timeout=(max(move_timeout,max(
                abs(stage.targets[axis]-idle[axis].now_position) for axis in active
            )/stage_velocity+5.0) if native_angle else move_timeout)
            if native_angle:
                recorder.event("native_angle_motion_deadline",timeout_seconds=stage_timeout,
                               source="SDK_RAW_DISTANCE_OVER_CONFIGURED_RAW_SPEED_PLUS_5S")
            stable = 0
            seen_motion: set[int] = set()
            # Tiny angle commands may quantize to the same/adjacent raw count.
            # Still require three fresh stopped target-feedback samples below.
            response_required=({axis for axis in active if
                abs(stage.targets[axis]-idle[axis].now_position)>FEEDBACK_POSITION_BAND_RAW}
                if stage.angle_targets is not None else active)
            settled: set[int] = set()
            settled_streak = {axis: 0 for axis in active}
            first_angle_sample=True
            while time.monotonic() - started < stage_timeout:
                sample = capture()
                states = {m.motor_id: m for m in sample.motors}
                if native_angle and stage.angle_targets is not None and first_angle_sample:
                    print("SDK_FEEDBACK "+", ".join(
                        f"M{axis} actual_sdk_angle={states[axis].now_angle_deg:g} status={states[axis].status}"
                        for axis in stage.angle_targets)+" TARGET_REACHED=UNCONFIRMED (monitoring)",flush=True)
                    first_angle_sample=False
                for axis in active:
                    motor = states[axis]
                    if axis in settled:
                        if abs(motor.now_position - stage.targets[axis]) > 5:
                            raise RuntimeError(f"M{axis} {phase}: now_position "
                                               f"before={stage.targets[axis]} after={motor.now_position} "
                                               "left settled target")
                        home_monitor.check_stationary_status(motor, phase, allow_transition=True,
                                                             transition_timeout=None)
                    # Status 1 or SDK acceptance alone is not movement evidence.
                    if abs(motor.now_position - idle[axis].now_position) > FEEDBACK_POSITION_BAND_RAW:
                        seen_motion.add(axis)
                    settled_streak[axis] = (settled_streak[axis] + 1 if
                        (zero_only_return or axis not in response_required or axis in seen_motion) and motor.status == 0 and
                        abs(motor.now_position - stage.targets[axis]) <= 5 else 0)
                    if settled_streak[axis] >= 2:
                        settled.add(axis)
                ready = all(states[axis].status == 0 and
                            abs(states[axis].now_position - stage.targets[axis]) <= 5
                            and (zero_only_return or axis not in response_required or axis in seen_motion) for axis in active) and not home_monitor.running_since
                stable = stable + 1 if ready else 0
                if stable >= 3:
                    recorder.event("stage_stable", stage=stage.name,
                                   stable_samples=stable, tolerance_raw=5,
                                   displacement_observed=sorted(seen_motion),
                                   tolerance_source="M3_EXP03_ONLY_OTHER_AXES_PROVISIONAL")
                    print(f"{display_stage}: FEEDBACK_COMPLETE "
                          + ", ".join(f"M{m.motor_id}={m.now_position} angle_deg={m.now_angle_deg:.4f} target={m.target_position}"
                                      for m in sample.motors), flush=True)
                    break
                time.sleep(poll_seconds)
            else:
                raise TimeoutError(f"{stage.name} position/status timeout")
            previous = sample
            phase = "HOLD"
            home_monitor.start_phase(phase, previous, targets=stage.targets,
                                     active=set(stage.active), broadcast=last_dispatch_broadcast)
            hold_started = time.monotonic()
            held = sample
            while time.monotonic() - hold_started < stage.hold_seconds:
                time.sleep(poll_seconds)
                held = capture()
            # A phase boundary must not turn one bounded transition into an
            # immediate failure or dispatch the next command while it persists.
            wait_stationary_clear(held)
            if stage.name == "CONTROLLED_OPEN_RETURN" and stage_source is None:
                break
        result = "SESSION_COMPLETE_SDK_FEEDBACK_ONLY"
    except BaseException as caught:
        error = f"{type(caught).__name__}: {caught}"
    finally:
        if error:
            defer_cleanup_event("session_failure", phase=phase, error=error)
        if device is not None:
            failed_phase = phase
            phase = "CLEANUP"
            defer_cleanup_event("cleanup_started", failed_phase=failed_phase,
                       controlled_return_on_error="NOT_DISPATCHED_STOP_HAS_PRIORITY")
            if enabled and motion is not None and device.state == "READY":
                for name, action in (("stop_all", motion.stop_all),
                                     ("disable_all", motion.disable_all)):
                    try:
                        # Call the SDK even if the recorder/capture guard is
                        # broken. API completion and feedback confirmation are
                        # reported separately; neither means physical release.
                        defer_cleanup_event("sdk_command_started", command=name, phase=phase,
                                   device_accepted="UNKNOWN")
                        action()
                        cleanup[name] = "COMPLETED"
                        defer_cleanup_event("sdk_command_completed", command=name, phase=phase,
                                   sdk_result=0, device_accepted="UNKNOWN")
                    except BaseException as caught:
                        cleanup[name] = f"FAILED: {caught}"
                        defer_cleanup_event("sdk_command_failed", command=name, phase=phase,
                                            error=str(caught))
                # Verify new SDK feedback after stop/disable when available.
                # A failed callback/communication read cannot be certified safe.
                cleanup["stop_confirmation"] = "UNCONFIRMED: no fresh stopped feedback"
                try:
                    previous_count = device.backend.feedback_counts()[1]
                    deadline = time.monotonic() + min(move_timeout, 1.0)
                    stopped = None
                    while time.monotonic() < deadline:
                        stopped = device.read_joint_states()
                        if (len(stopped.motors) == 6 and
                                {m.motor_id for m in stopped.motors} == AXES and
                                stopped.position_frame_count > previous_count and
                                all(m.status == 0 and m.alarm == 0 for m in stopped.motors)):
                            cleanup["stop_confirmation"] = "SDK_FEEDBACK_STOPPED_PHYSICAL_STOP_NOT_CONFIRMED"
                            break
                        time.sleep(poll_seconds)
                    defer_cleanup_event("cleanup_feedback", result=cleanup["stop_confirmation"],
                               sample_utc=stopped.timestamp_utc if stopped else None,
                               position_frame_count=stopped.position_frame_count if stopped else None,
                               motors=[vars(m) for m in stopped.motors] if stopped else [])
                except BaseException as caught:
                    cleanup["stop_confirmation"] = f"UNCONFIRMED: {caught}"
                    defer_cleanup_event("cleanup_feedback", result=cleanup["stop_confirmation"])
            try:
                device.close()
                cleanup["close"] = "COMPLETED"
            except BaseException as caught:
                cleanup["close"] = f"FAILED: {caught}"
            try:
                drain(enforce_capture=False)
            except BaseException as caught:
                cleanup["drain"] = f"FAILED: {caught}"
        for name, fields in cleanup_events:
            soft_event(name, **fields)
        if capture_errors:
            cleanup["capture"] = "FAILED: " + "; ".join(capture_errors)
        if error or any(value.startswith(("FAILED", "UNCONFIRMED")) for value in cleanup.values()):
            result = "FAILED"
        try:
            recorder.finish(result, [f"error: {error or 'none'}", f"cleanup: {cleanup}",
                                     "SDK feedback is not proof of visible grasp or synchronized arrival."])
        except BaseException as caught:
            result = "FAILED"
            cleanup["report"] = f"FAILED: {caught}"
            print(f"REPORT_WRITE_FAILED error={error} cleanup={cleanup}", file=sys.stderr, flush=True)
    return SessionResult(result, recorder.directory, error, cleanup)
