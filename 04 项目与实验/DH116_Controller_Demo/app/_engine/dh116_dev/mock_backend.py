"""Formal 6-motor/11-DOF test backend. Never imports vendor code."""

from __future__ import annotations
import time

from .models import AdapterInfo, DeviceConfig, HandInfo
from .state import MotorState, RawFeedback, utc_now


class MockFormalBackend:
    def __init__(self):
        self.phase = "STARTING"
        self.frames: list[RawFeedback] = []
        self.count = 0
        self.position_count = 0
        self.first_valid: str | None = None
        self.last_position_feedback_utc: str | None = None
        self.last_position_feedback_monotonic: float | None = None

    def scan(self, config: DeviceConfig) -> list[AdapterInfo]:
        return [AdapterInfo("Com Equipment CANFD Analyser", config.adapter_vid,
                            config.adapter_pid, config.adapter_serial)]

    def open(self, config: DeviceConfig, adapter: AdapterInfo) -> None:
        self.phase = "CAN_OPEN"
        self.frames.append(RawFeedback(utc_now(), 0x481, 0x50, "5006",
                                       2, self.phase, False))

    def initialize(self, config: DeviceConfig) -> None:
        self.phase = "INITIALIZING"

    def mark_ready(self) -> None:
        self.phase = "READY"

    def read_hand_info(self, config: DeviceConfig) -> HandInfo:
        return HandInfo("MOCK-NO-DEVICE", "mock-0.0", 11, config.hand_model,
                        active_dof=6, sdk_hand_type=0)

    def _frame(self) -> None:
        # Synthetic words are intentionally not interpreted as real 0x50 axes.
        data = bytes.fromhex("5006") + bytes(range(48))
        frame = RawFeedback(utc_now(), 0x481, 0x50, data.hex().upper(),
                            len(data), self.phase, True)
        self.frames.append(frame)
        self.count += 1
        self.position_count += 1
        self.first_valid = self.first_valid or frame.timestamp_utc
        self.last_position_feedback_utc = frame.timestamp_utc
        self.last_position_feedback_monotonic = time.monotonic()

    def read_motor_state(self, motor_id: int) -> MotorState:
        if motor_id == 1:
            self._frame()
        return MotorState(motor_id, motor_id * 100, motor_id * 1.25,
                          0, 0, 0)

    def drain_feedback(self) -> list[RawFeedback]:
        frames, self.frames = self.frames, []
        return frames

    def feedback_counts(self) -> tuple[int, int, str | None]:
        return self.count, self.position_count, self.first_valid

    def feedback_snapshot(self) -> tuple:
        return (*self.feedback_counts(), self.last_position_feedback_utc,
                self.last_position_feedback_monotonic)

    def decode_counts(self) -> tuple[int, int]:
        return 0, 0

    def close(self) -> None:
        self.phase = "CLOSED"
