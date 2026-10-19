"""Transport-independent DH116 data and future ROS 2 message boundaries."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Callable


@dataclass(frozen=True)
class DeviceConfig:
    hand_model: str = "DH116"
    hand_side: str = "Right"
    node_id: int = 1
    adapter_vid: int = 0xA8FA
    adapter_pid: int = 0x8598
    adapter_serial: str = "SET_YOUR_ADAPTER_SERIAL"
    nominal_bitrate: int = 1_000_000
    data_bitrate: int = 5_000_000

    def __post_init__(self) -> None:
        if self.hand_model != "DH116" or self.hand_side != "Right":
            raise ValueError("Only the confirmed DH116 Right configuration is prepared")
        if not 1 <= self.node_id <= 255:
            raise ValueError("node_id must be in 1..255")
        if not 0 <= self.adapter_vid <= 0xFFFF or not 0 <= self.adapter_pid <= 0xFFFF:
            raise ValueError("adapter VID/PID must be 16-bit values")
        if not self.adapter_serial:
            raise ValueError("adapter_serial is required for exact selection")
        if self.nominal_bitrate <= 0 or self.data_bitrate <= 0:
            raise ValueError("CANFD bitrates must be positive")

    def as_dict(self) -> dict:
        data = asdict(self)
        data["adapter_vid"] = f"{self.adapter_vid:04X}"
        data["adapter_pid"] = f"{self.adapter_pid:04X}"
        return data


@dataclass(frozen=True)
class AdapterInfo:
    name: str
    vid: int
    pid: int
    serial: str


@dataclass(frozen=True)
class HandInfo:
    serial_number: str
    firmware_version: str
    dof: int
    model: str
    active_dof: int
    sdk_hand_type: int | None = None


@dataclass(frozen=True)
class JointState:
    joint_id: int
    position: int  # SDK position equivalent; physical angle/encoder mapping is unverified.
    status: int
    alarm: int


@dataclass(frozen=True)
class HandStatus:
    connected: bool
    stamp_utc: str
    hand_info: HandInfo
    joints: tuple[JointState, ...]

    @classmethod
    def capture(cls, info: HandInfo, joints: list[JointState]) -> "HandStatus":
        return cls(True, datetime.now(timezone.utc).isoformat(), info, tuple(joints))

    def as_dict(self) -> dict:
        return asdict(self)


def to_ros_joint_states(
    status: HandStatus, counts_to_radians: Callable[[int, int], float]
) -> dict:
    """Prepare /joint_states data; caller must supply a calibrated conversion.

    SDK positions are position equivalents, not calibrated joint radians. The mock may use a synthetic converter,
    but live publication must wait for verified direction, zero and scale.
    """
    if counts_to_radians is None:
        raise ValueError("A calibrated counts_to_radians converter is required")
    return {
        "topic": "/joint_states",
        "header": {"stamp_utc": status.stamp_utc},
        "name": [f"joint_{joint.joint_id}" for joint in status.joints],
        "position": [counts_to_radians(joint.joint_id, joint.position)
                     for joint in status.joints],
        "velocity": [],
        "effort": [],
    }
