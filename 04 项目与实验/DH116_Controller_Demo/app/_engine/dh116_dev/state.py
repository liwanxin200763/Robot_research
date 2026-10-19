"""Transport-neutral feedback records. No SDK import or device access here."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import math
import time


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


@dataclass(frozen=True)
class RawFeedback:
    timestamp_utc: str
    can_id: int
    frame_type: int | None
    payload_hex: str
    payload_length: int
    phase: str
    decoded_by_sdk: bool
    sdk_error_code: int | None = None
    adapter_echo: bool | None = None
    adapter_timestamp: float | None = None
    provenance: str = "UNKNOWN_CAPTURE"

    @property
    def payload(self) -> bytes:
        return bytes.fromhex(self.payload_hex)

    @property
    def dlc(self) -> int:
        """Recover CAN FD DLC from the adapter's decoded payload length."""
        if self.payload_length <= 8:
            return self.payload_length
        for dlc, length in enumerate((12, 16, 20, 24, 32, 48, 64), start=9):
            if self.payload_length <= length:
                return dlc
        raise ValueError("CAN FD payload exceeds 64 bytes")

    def fields(self) -> dict:
        data = self.payload
        # The official protocol identifies 0x50 as position/velocity/current/
        # status but does not give a trustworthy byte layout for this frame.
        # Expose every byte/word without assigning unverified motor semantics.
        return {
            "frame_type": self.frame_type,
            "axis_count_or_length": data[1] if len(data) > 1 else None,
            "data_bytes_hex": [f"{value:02X}" for value in data[2:]],
            "data_words_u16_le": [int.from_bytes(data[i:i + 2], "little")
                                  for i in range(2, len(data) - 1, 2)],
            "layout": "unverified_0x50" if self.frame_type == 0x50 else "raw",
        }


@dataclass(frozen=True)
class MotorState:
    motor_id: int
    now_position: int
    now_angle_deg: float
    target_position: int
    status: int
    alarm: int


# One raw count is shared by all six active channels, not a travel limit.
# Stopped historical pairs: M1 200/199 (~0.006 deg), M2 199/200
# (~0.003 deg); EXP04 M3-M6 getters show at most 0.008 deg per raw count.
# Live ENABLE runs dcf087 (M4) and f3423b (M3/M4) corroborate one-count
# variation without a target/status/alarm change. c_float getter rounding
# is included explicitly; neither band grows at runtime.
FEEDBACK_POSITION_BAND_RAW = 1
FEEDBACK_ANGLE_BAND_DEG = 0.008002
RUNNING_TRANSITION_LIMIT_S = 0.35  # Existing bounded EXP05 status transition window.


def require_home_running_stable(before: MotorState, motor: MotorState,
                                running_since: dict[int, float]) -> None:
    """RUNNING is not motion proof; stationary transitions remain time bounded."""
    require_stationary_feedback(before, motor, "HOME_RUNNING")
    now = time.monotonic()
    started = running_since.setdefault(motor.motor_id, now)
    if now-started > RUNNING_TRANSITION_LIMIT_S:
        raise RuntimeError(f"M{motor.motor_id} HOME: RUNNING persisted duration_s={now-started:.3f}")


def feedback_measurement_policy() -> dict:
    return {
        "motor_ids": list(range(1, 7)), "position_raw": FEEDBACK_POSITION_BAND_RAW,
        "angle_degrees": FEEDBACK_ANGLE_BAND_DEG, "target_band": 0,
        "reference": "ANCHORED_UNTIL_AUTHORIZED_MOTION_NOT_SLIDING",
        "source_runs": ["20261014T140710547638Z-dcf087", "20261014T151203789719Z-f3423b"],
        "resolution_evidence": {
            "1": "experiments/exp04_remaining_motor_validation/results/20261009T072240369888Z-f9b863/samples.csv",
            "2": "experiments/exp04_remaining_motor_validation/results/20261009T070645126004Z-bd6c4d/samples.csv",
            "3": "experiments/exp05_multi_motor_control/results/20261014T151203789719Z-f3423b/samples.csv",
            "4": "experiments/exp04_remaining_motor_validation/results/20261008T141535326893Z-f8abdd/samples.csv",
            "5": "experiments/exp04_remaining_motor_validation/results/20261008T144256277901Z-4f3153/samples.csv",
            "6": "experiments/exp04_remaining_motor_validation/results/20261008T152159363177Z-94ca75/samples.csv",
        },
        "physical_stationarity_proven": False,
    }


def stationary_feedback_changes(before: MotorState, after: MotorState) -> dict:
    """Compare to an anchored phase reference, never to a sliding sample.

    Use the same bounded measurement rule on M1-M6. Evidence and limits
    are exposed by feedback_measurement_policy(), independent of motion
    target/arrival configuration. This does not establish a mechanical zero,
    physical stationarity, or a universal raw-to-angle conversion.
    Targets always compare exactly.
    """
    if before.motor_id != after.motor_id or after.motor_id not in range(1, 7):
        raise ValueError("stationary feedback requires the same valid motor ID")
    bands = {"now_position": FEEDBACK_POSITION_BAND_RAW,
             "now_angle_deg": FEEDBACK_ANGLE_BAND_DEG,
             "target_position": 0}
    return {field: {"before": getattr(before, field), "after": getattr(after, field),
                    "measurement_band": band}
            for field, band in bands.items()
            if not math.isfinite(getattr(before, field)) or
            not math.isfinite(getattr(after, field)) or
            abs(getattr(after, field) - getattr(before, field)) > band}


def require_stationary_feedback(before: MotorState, after: MotorState, phase: str) -> None:
    changes = stationary_feedback_changes(before, after)
    if changes:
        detail = "; ".join(f"{field} before={value['before']} after={value['after']} "
                           f"measurement_band={value['measurement_band']}"
                           for field, value in changes.items())
        raise RuntimeError(f"M{after.motor_id} {phase}: {detail}")


@dataclass(frozen=True)
class FeedbackSample:
    timestamp_utc: str
    motors: tuple[MotorState, ...]
    raw_frame_count: int
    position_frame_count: int
    first_valid_feedback_utc: str | None
    last_position_feedback_utc: str | None = None
    last_position_feedback_monotonic: float | None = None
    sampled_monotonic: float | None = None

    def as_dict(self) -> dict:
        return asdict(self)


# e6237a READY callback trace: median 1 ms, p99 5 ms, max 14 ms.
# Fixed 100 ms software deadline is >7x that observed maximum; it is not a
# manufacturer timing guarantee and never renews on getters/other CAN types.
POSITION_FEEDBACK_TIMEOUT_S = 0.100


class PositionFeedbackFreshness:
    """Transport 0x50 liveness only; not per-axis SDK cache freshness proof."""

    def __init__(self):
        self.last_count: int | None = None
        self.last_received: float | None = None
        self.age_seconds: float | None = None
        self.source = "UNKNOWN"

    def observe(self, sample: FeedbackSample) -> bool:
        now = sample.sampled_monotonic if sample.sampled_monotonic is not None else time.monotonic()
        if sample.position_frame_count <= 0:
            raise RuntimeError("no valid 0x50 feedback before six-axis state acceptance")
        if self.last_count is not None and sample.position_frame_count < self.last_count:
            raise RuntimeError("0x50 feedback counter regressed")
        advanced = self.last_count is None or sample.position_frame_count > self.last_count
        if advanced:
            if sample.last_position_feedback_monotonic is not None:
                self.last_received = sample.last_position_feedback_monotonic
                self.source = "VALID_READY_0x50_CALLBACK_RECEIPT"
            else:
                # Compatibility for historical CSV replay and older test
                # backends. Never label observation of a counter as RX time.
                self.last_received = now
                self.source = "COUNT_OBSERVATION_NOT_CALLBACK_TIME"
            self.last_count = sample.position_frame_count
        self.age_seconds = now - self.last_received
        if not math.isfinite(self.age_seconds) or self.age_seconds < 0:
            raise RuntimeError("invalid 0x50 receipt clock")
        if self.age_seconds >= POSITION_FEEDBACK_TIMEOUT_S:
            raise TimeoutError(f"0x50 feedback timeout: age_ms={self.age_seconds*1000:.3f} "
                               f"limit_ms={POSITION_FEEDBACK_TIMEOUT_S*1000:.0f} "
                               f"count={sample.position_frame_count} source={self.source}")
        return advanced


@dataclass(frozen=True)
class HandState:
    """One coherent read of the six active SDK motor getters."""

    timestamp_utc: str
    motors: tuple[MotorState, ...]
    raw_frame_count: int = 0
    position_frame_count: int = 0

    def __post_init__(self) -> None:
        if len(self.motors) != 6 or {motor.motor_id for motor in self.motors} != set(range(1, 7)):
            raise ValueError("HandState requires exactly Motor 1–6")
        if any(not math.isfinite(motor.now_angle_deg) for motor in self.motors):
            raise ValueError("HandState contains a non-finite SDK angle")

    @classmethod
    def from_feedback(cls, sample: FeedbackSample) -> "HandState":
        return cls(sample.timestamp_utc, tuple(sorted(sample.motors,
                    key=lambda motor: motor.motor_id)), sample.raw_frame_count,
                   sample.position_frame_count)

    @classmethod
    def from_dict(cls, data: dict) -> "HandState":
        return cls(str(data["timestamp_utc"]),
                   tuple(MotorState(**motor) for motor in data["motors"]),
                   int(data.get("raw_frame_count", 0)),
                   int(data.get("position_frame_count", 0)))

    def as_dict(self) -> dict:
        return asdict(self)


# The experiment is specifically about the 0x50 feedback path. Other
# feedback types can be logged, but must not inflate this counter.
POSITION_FRAME_TYPES = frozenset({0x50})
