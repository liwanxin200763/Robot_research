"""Legacy read-only facade plus the formal staged device lifecycle.

Importing this module never opens CANFD or calls the vendor SDK.
"""

from __future__ import annotations

from pathlib import Path
import time
from typing import Any, Callable, Protocol

from .errors import DeviceError
from .models import AdapterInfo, DeviceConfig, HandInfo
from .state import FeedbackSample, HandState, MotorState, RawFeedback, utc_now








class FormalBackend(Protocol):
    def scan(self, config: DeviceConfig) -> list[AdapterInfo]: ...
    def open(self, config: DeviceConfig, adapter: AdapterInfo) -> None: ...
    def initialize(self, config: DeviceConfig) -> None: ...
    def mark_ready(self) -> None: ...
    def read_hand_info(self, config: DeviceConfig) -> HandInfo: ...
    def read_motor_state(self, motor_id: int) -> MotorState: ...
    def drain_feedback(self) -> list[RawFeedback]: ...
    def feedback_counts(self) -> tuple[int, int, str | None]: ...
    def close(self) -> None: ...


class FormalDevice:
    """Single adapter lifecycle. Importing this class has no hardware effect."""

    STATES = ("STARTING", "CAN_OPEN", "INITIALIZING", "READY", "CLOSING", "CLOSED")

    def __init__(self, config: DeviceConfig, backend: FormalBackend,
                 event: Callable[..., None]):
        self.config, self.backend, self.event = config, backend, event
        self.state = "STARTING"
        self.hand_info: HandInfo | None = None
        self.homed_this_session = False
        self.homed_motor_id: int | None = None
        self.homed_motor_ids: set[int] = set()
        self.home_command_motor_id: int | None = None
        self.event("state_transition", state=self.state, timestamp_utc=utc_now())

    def _transition(self, new_state: str) -> None:
        allowed = {
            "STARTING": {"CAN_OPEN", "CLOSING"},
            "CAN_OPEN": {"INITIALIZING", "CLOSING"},
            "INITIALIZING": {"READY", "CLOSING"},
            "READY": {"CLOSING"},
            "CLOSING": {"CLOSED"},
            "CLOSED": set(),
        }
        if new_state not in allowed[self.state]:
            raise DeviceError("state", f"invalid {self.state} -> {new_state}")
        self.state = new_state
        self.event("state_transition", state=new_state, timestamp_utc=utc_now())

    def scan(self) -> list[AdapterInfo]:
        if self.state != "STARTING":
            raise DeviceError("scan", f"requires STARTING, got {self.state}")
        adapters = self.backend.scan(self.config)
        self.event("scan", adapters=[vars(item) for item in adapters])
        return adapters

    def connect(self, adapters: list[AdapterInfo]) -> None:
        if self.state != "STARTING":
            raise DeviceError("connect", f"requires STARTING, got {self.state}")
        self.homed_this_session = False
        self.homed_motor_id = None
        self.homed_motor_ids.clear()
        self.home_command_motor_id = None
        matches = [item for item in adapters if
                   (item.vid, item.pid, item.serial) ==
                   (self.config.adapter_vid, self.config.adapter_pid,
                    self.config.adapter_serial)]
        if len(matches) != 1:
            raise DeviceError("connect", f"expected one exact adapter, found {len(matches)}")
        self.backend.open(self.config, matches[0])
        self._transition("CAN_OPEN")

    def initialize(self) -> HandInfo:
        if self.state != "CAN_OPEN":
            raise DeviceError("initialize", f"requires CAN_OPEN, got {self.state}")
        self._transition("INITIALIZING")
        self.event("initial_ex_started", timestamp_utc=utc_now())
        self.backend.initialize(self.config)
        self.homed_this_session = False
        self.homed_motor_id = None
        self.homed_motor_ids.clear()
        self.home_command_motor_id = None
        # The vendor Python wrapper checks the native return code and returns
        # None on success. Therefore reaching here means native result 0.
        self.event("initial_ex_finished", result=0, timestamp_utc=utc_now())
        self.hand_info = self.backend.read_hand_info(self.config)
        if self.hand_info.active_dof != 6 or self.hand_info.dof != 11:
            raise DeviceError("initialize", "DH116 identity/DOF mismatch")
        self._transition("READY")
        self.backend.mark_ready()
        return self.hand_info

    def connect_and_initialize(self) -> HandInfo:
        """Shared EXP02/EXP03 startup: scan, exact adapter open, initial_ex."""
        self.connect(self.scan())
        return self.initialize()

    def read_raw_feedback(self) -> list[RawFeedback]:
        if self.state != "READY":
            raise DeviceError("read_raw_feedback", "requires READY")
        return self.backend.drain_feedback()

    def drain_pending_feedback(self) -> list[RawFeedback]:
        """Flush frames already captured by the callback during shutdown.

        This never reads CANFD or calls the SDK; it empties the local queue.
        """
        return self.backend.drain_feedback()

    def drain_pending_transport_events(self) -> list[dict]:
        """Read local SDK-send/USB-submission evidence without touching CANFD."""
        drain = getattr(self.backend, "drain_transport_events", None)
        return drain() if drain is not None else []

    def read_hand_info(self) -> HandInfo:
        if self.state != "READY" or self.hand_info is None:
            raise DeviceError("read_hand_info", "requires READY")
        return self.hand_info

    def read_joint_states(self) -> FeedbackSample:
        if self.state != "READY":
            raise DeviceError("read_joint_states", "requires READY")
        motors = []
        for motor_id in range(1, 7):
            started = utc_now()
            try:
                motor = self.backend.read_motor_state(motor_id)
            except BaseException as error:
                self.event("sdk_getter_read", motor_id=motor_id,
                           started_utc=started, finished_utc=utc_now(),
                           source="SDK_GETTER_NONATOMIC", error=str(error),
                           field_receive_timestamp="UNKNOWN")
                raise
            self.event("sdk_getter_read", motor_id=motor_id,
                       started_utc=started, finished_utc=utc_now(),
                       source="SDK_GETTER_NONATOMIC", error=None,
                       field_receive_timestamp="UNKNOWN")
            motors.append(motor)
        snapshot = getattr(self.backend, "feedback_snapshot", None)
        if snapshot is not None:
            total, position, first, received_utc, received_monotonic = snapshot()
        else:
            total, position, first = self.backend.feedback_counts()
            received_utc = received_monotonic = None
        return FeedbackSample(utc_now(), tuple(motors), total, position, first,
                              received_utc, received_monotonic, time.monotonic())

    def get_state(self) -> HandState:
        return HandState.from_feedback(self.read_joint_states())

    def close(self) -> None:
        if self.state in ("CLOSING", "CLOSED"):
            return
        self._transition("CLOSING")
        try:
            self.backend.close()
        finally:
            self.homed_this_session = False
            self.homed_motor_id = None
            self.homed_motor_ids.clear()
            self.home_command_motor_id = None
            self._transition("CLOSED")
