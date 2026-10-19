"""Legacy reader and injectable vendor backend.

Importing this module never loads a DLL or opens USB. The formal exp01 command
uses MockFormalBackend by default; its explicit --live path is unverified on
hardware and requires an operator prompt before opening CANFD.
"""

from __future__ import annotations

import importlib
import json
import logging
import math
import os
import sys
import time
from collections import deque
from dataclasses import asdict
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from threading import Lock
from typing import Protocol

from .errors import DeviceError, check_sdk_result, translate_vendor_error
from .models import AdapterInfo, DeviceConfig, HandInfo, HandStatus, JointState
from .state import MotorState, POSITION_FRAME_TYPES, RawFeedback, utc_now
from .frame_provenance import classify_callback
from .motion import is_sdk_position_velocity










class VendorBackend:
    """Prepared wrapper around the official Python gsusb and LHandProLib APIs.

    No code here runs until a caller explicitly invokes scan/open/etc. The
    exp01 command instantiates this class only after --live and operator input.
    """

    def __init__(self, sample_dir: Path, dll_path: Path, *, capture_echo: bool = False):
        self.sample_dir = Path(sample_dir).resolve()
        self.dll_path = Path(dll_path).resolve()
        self.capture_echo = capture_echo
        self._gsusb = None
        self._sdk_type = None
        self._canfd_mode = None
        self._adapter = None
        self._bus = None
        self._sdk = None
        self._dll_directory = None
        self._callback_error: Exception | None = None
        self._failed_frame: RawFeedback | None = None
        self._phase = "STARTING"
        self._node_id: int | None = None
        self._raw_lock = Lock()
        self._raw_frames: deque[RawFeedback] = deque(maxlen=8192)
        self._transport_events: deque[dict] = deque(maxlen=8192)
        self.dropped_transport_events = 0
        self.dropped_raw_frames = 0
        self._frame_count = 0
        self._position_frame_count = 0
        self._decode_success_count = 0
        self._decode_error_count = 0
        self._first_valid_feedback_utc: str | None = None
        self._last_position_feedback_utc: str | None = None
        self._last_position_feedback_monotonic: float | None = None

    def _load_python(self) -> None:
        if self._gsusb is not None:
            return
        if not self.sample_dir.is_dir() or not self.dll_path.is_file():
            raise DeviceError("load", "official Python sample or SDK DLL is missing")
        gsusb_source = self.sample_dir / "gsusb_canfd"
        if not gsusb_source.is_dir():
            raise DeviceError("load", "official gsusb Python package is missing")
        sys.path.insert(0, str(self.sample_dir))
        self._gsusb = importlib.import_module("gsusb_canfd")
        wrapper = importlib.import_module("lhandprolib_python_sdk.lhandprolib_wrapper")
        if not Path(self._gsusb.__file__).resolve().is_relative_to(self.sample_dir):
            raise DeviceError("load", "gsusb module did not come from the official sample")
        if not Path(wrapper.__file__).resolve().is_relative_to(self.sample_dir):
            raise DeviceError("load", "SDK wrapper did not come from the official sample")
        self._sdk_type = wrapper.PyLHandProLib
        self._canfd_mode = wrapper.LCN_CANFD

    def scan(self, config: DeviceConfig) -> list[AdapterInfo]:
        self._load_python()
        try:
            adapters = list(self._gsusb.scan_adapters(config.adapter_vid,
                                                       config.adapter_pid))
            return [AdapterInfo(a.name(), a.vendor_id, a.product_id, a.serial)
                    for a in adapters]
        except Exception as error:
            raise translate_vendor_error("scan", error) from error

    def open(self, config: DeviceConfig, adapter: AdapterInfo) -> None:
        try:
            if os.name == "nt":
                from .cli import _lhandpro_running
                if _lhandpro_running():
                    raise DeviceError("open", "LHandPro.exe is running")
            self._load_python()
            candidates = [a for a in self._gsusb.scan_adapters(config.adapter_vid,
                                                                 config.adapter_pid)
                          if a.serial == config.adapter_serial
                          and a.name() == adapter.name]
            if len(candidates) != 1:
                raise DeviceError("open", "adapter identity changed since scan")
            self._adapter = candidates[0]
            self._bus = self._gsusb.CanFdBus()
            self._bus.open(self._adapter)
            self._bus.configure(self._gsusb.BusConfig(
                bitrate=config.nominal_bitrate, data_bitrate=config.data_bitrate,
                fd=True, sample_point=0.80, data_sample_point=0.75,
                drop_echo=not self.capture_echo))
            if hasattr(os, "add_dll_directory"):
                self._dll_directory = os.add_dll_directory(str(self.dll_path.parent))
            self._sdk = self._sdk_type(str(self.dll_path))
            self._sdk.set_send_canfd_callback(self._send_frame)
            self._node_id = config.node_id
            self._phase = "CAN_OPEN"
            self._bus.start(self._receive_frame)
        except Exception as error:
            self.close()
            raise translate_vendor_error("open", error) from error

    def _send_frame(self, msg_id: int, data: bytes, is_extended: int) -> bool:
        started = utc_now()
        try:
            frame = self._gsusb.CanFrame(id=msg_id, data=bytes(data).ljust(64, b"\0"),
                                          extended=bool(is_extended), fd=True, brs=True)
            self._bus.send(frame, echo=self.capture_echo)
            self._append_transport_event({"kind": "HOST_USB_WRITE_COMPLETED",
                                          "direction": "HOST_TO_ADAPTER",
                                          "started_utc": started, "finished_utc": utc_now(),
                                          "can_id": msg_id,
                                          "payload_hex": frame.data.hex().upper(),
                                          "callback_payload_hex": bytes(data).hex().upper(),
                                          "callback_payload_length": len(data),
                                          "device_accepted": "UNKNOWN"})
            return True
        except Exception as error:
            self._callback_error = error
            self._append_transport_event({"kind": "HOST_USB_WRITE_FAILED",
                                          "direction": "HOST_ATTEMPT_FAILED",
                                          "started_utc": started, "finished_utc": utc_now(),
                                          "can_id": msg_id,
                                          "callback_payload_hex": bytes(data).hex().upper(),
                                          "callback_payload_length": len(data),
                                          "error": str(error), "device_accepted": "UNKNOWN"})
            return False

    def _append_transport_event(self, event: dict) -> None:
        with self._raw_lock:
            if len(self._transport_events) == self._transport_events.maxlen:
                self.dropped_transport_events += 1
            self._transport_events.append(event)

    def drain_transport_events(self) -> list[dict]:
        with self._raw_lock:
            events = list(self._transport_events)
            self._transport_events.clear()
        return events

    def _receive_frame(self, frame: object) -> None:
        received_monotonic, received_utc = time.monotonic(), utc_now()
        payload = bytes(frame.data)
        frame_type = payload[0] if payload else None
        adapter_echo = getattr(frame, "echo", None)
        adapter_timestamp = getattr(frame, "timestamp", None)
        phase = self._phase
        result: int | None = None
        try:
            # CAN_OPEN startup traffic is captured but never passed to the DLL.
            # During INITIALIZING the DLL must decode handshake replies; only
            # READY frames enter normal experiment state processing.
            if adapter_echo is not True and phase in ("INITIALIZING", "READY"):
                result = self._sdk.set_canfd_data_decode(frame.id, payload)
                check_sdk_result(result, "CANFD decode")
        except Exception as error:
            self._callback_error = error
            result = getattr(error, "code", getattr(error, "error_code", result))
        raw = RawFeedback(received_utc, frame.id, frame_type, payload.hex().upper(),
                          len(payload), phase,
                          adapter_echo is not True and phase in ("INITIALIZING", "READY"),
                          result if isinstance(result, int) and result != 0 else None,
                          adapter_echo, adapter_timestamp,
                          classify_callback(frame.id, self._node_id, adapter_echo))
        with self._raw_lock:
            if len(self._raw_frames) == self._raw_frames.maxlen:
                self.dropped_raw_frames += 1
            self._raw_frames.append(raw)
            self._frame_count += 1
            if raw.decoded_by_sdk:
                if raw.sdk_error_code is None and result == 0:
                    self._decode_success_count += 1
                else:
                    self._decode_error_count += 1
            if (phase == "READY" and result == 0 and
                    frame.id == 0x480 + self._node_id and
                    frame_type in POSITION_FRAME_TYPES):
                self._position_frame_count += 1
                self._last_position_feedback_utc = received_utc
                self._last_position_feedback_monotonic = received_monotonic
                if self._first_valid_feedback_utc is None:
                    self._first_valid_feedback_utc = raw.timestamp_utc
            if raw.sdk_error_code is not None:
                self._failed_frame = raw

    def _check_callback(self) -> None:
        if self._callback_error is not None:
            error = translate_vendor_error("CANFD callback", self._callback_error)
            frame = self._failed_frame
            detail = (f" frame_type={frame.frame_type} payload={frame.payload_hex}"
                      if frame else "")
            raise DeviceError("CANFD callback", str(error) + detail,
                              getattr(error, "code", None))

    def initialize(self, config: DeviceConfig) -> None:
        if self._sdk is None or self._bus is None:
            raise DeviceError("initialize", "open must succeed first")
        try:
            self._node_id = config.node_id
            self._phase = "INITIALIZING"
            self._sdk.initial_ex(self._canfd_mode, config.node_id)
            self._check_callback()
        except Exception as error:
            raise translate_vendor_error("initial_ex", error) from error

    def mark_ready(self) -> None:
        if self._phase != "INITIALIZING":
            raise DeviceError("mark_ready", f"requires INITIALIZING, got {self._phase}")
        self._check_callback()
        self._phase = "READY"

    def read_motor_state(self, motor_id: int) -> MotorState:
        if self._phase != "READY":
            raise DeviceError("read_motor_state", "requires READY")
        self._check_callback()
        try:
            return MotorState(motor_id, self._sdk.get_now_position(motor_id),
                              self._sdk.get_now_angle(motor_id),
                              self._sdk.get_target_position(motor_id),
                              self._sdk.get_now_status(motor_id),
                              self._sdk.get_now_alarm(motor_id))
        except Exception as error:
            raise translate_vendor_error("read_motor_state", error) from error

    def drain_feedback(self) -> list[RawFeedback]:
        with self._raw_lock:
            frames = list(self._raw_frames)
            self._raw_frames.clear()
        return frames

    def feedback_counts(self) -> tuple[int, int, str | None]:
        self._check_callback()
        with self._raw_lock:
            return (self._frame_count, self._position_frame_count,
                    self._first_valid_feedback_utc)

    def feedback_snapshot(self) -> tuple:
        """Atomically pair the valid READY 0x50 count with its receipt clock."""
        self._check_callback()
        with self._raw_lock:
            return (self._frame_count, self._position_frame_count,
                    self._first_valid_feedback_utc, self._last_position_feedback_utc,
                    self._last_position_feedback_monotonic)

    def decode_counts(self) -> tuple[int, int]:
        with self._raw_lock:
            return self._decode_success_count, self._decode_error_count

    def read_hand_info(self, config: DeviceConfig) -> HandInfo:
        try:
            self._check_callback()
            hand_type = self._sdk.get_hand_type()
            firmware = self._sdk.get_firmware_version()
            total, active = self._sdk.get_dof()
            serial = self._sdk.get_serial_number()
            self._check_callback()
            if not 0 < active <= total <= 32:
                raise DeviceError("read_hand_info", "invalid DOF reported by SDK")
            return HandInfo(serial, str(firmware), total, config.hand_model,
                            active_dof=active, sdk_hand_type=hand_type)
        except Exception as error:
            raise translate_vendor_error("read_hand_info", error) from error

    def _motion_call(self, operation: str, method: str, *args,
                     ignore_callback_error: bool = False) -> None:
        if self._phase != "READY" or self._sdk is None:
            raise DeviceError(operation, "requires READY")
        if not ignore_callback_error:
            self._check_callback()
        try:
            getattr(self._sdk, method)(*args)
            if not ignore_callback_error:
                self._check_callback()
        except Exception as error:
            raise translate_vendor_error(operation, error) from error

    def enable(self, motor_id: int) -> None:
        self._motion_call("enable", "set_enable", motor_id, True)

    def home(self, motor_id: int) -> None:
        self._motion_call("home", "home_motors", motor_id)

    def disable(self, motor_id: int) -> None:
        # 反馈回调报错后仍需尝试断使能清理。
        self._motion_call("disable", "set_enable", motor_id, False,
                          ignore_callback_error=True)

    def stop(self, motor_id: int) -> None:
        self._motion_call("stop", "stop_motors", motor_id,
                          ignore_callback_error=True)

    def position_command(self, motor_id: int, target: int, velocity: int,
                         current_raw: int) -> str:
        # 按厂家顺序先设置三个运动值，再执行一次 move_motors。
        self._motion_call("set_target_position", "set_target_position", motor_id, target)
        self._motion_call("set_position_velocity", "set_position_velocity",
                          motor_id, velocity)
        self._motion_call("set_max_current", "set_max_current",
                          motor_id, current_raw)
        dispatch_utc = utc_now()
        self._motion_call("move_motors", "move_motors", motor_id)
        return dispatch_utc

    def set_position_mode_all(self) -> None:
        """Official SDK control-mode call; experiment monitors all six afterward."""
        self._motion_call("set_control_mode", "set_control_mode", 0, 0)

    def get_angle_limits(self, axes=(1,2,3,4,5,6)) -> dict[int, tuple[float,float]]:
        """Read the SDK's native limits, not a historical feedback envelope."""
        if self._phase!="READY" or self._sdk is None or not axes or not set(axes)<=set(range(1,7)):
            raise DeviceError("get_limit_target_angle","requires READY and console axes M1-M6")
        result={}
        try:
            for axis in axes:
                self._check_callback()
                low,high=self._sdk.get_limit_target_angle(axis)
                self._check_callback()
                if (not math.isfinite(low) or not math.isfinite(high) or not low<=0<high):
                    raise DeviceError("get_limit_target_angle",f"M{axis} invalid/unknown SDK limits: {low}, {high}")
                result[axis]=(float(low),float(high))
        except Exception as error:
            raise translate_vendor_error("get_limit_target_angle",error) from error
        return result

    def native_angles_command(self, angles: dict[int,float], held_targets: dict[int,int],
                              velocity: int,current_raw: int,tolerances: dict[int,float]) -> dict:
        """Use SDK limits and SDK conversion directly. No local angle/raw formula.

        Exactly one SDK motor ID is allowed. The vendor DLL may still serialize
        six-axis-field CANFD frames; this method does not promise wire isolation.
        SDK raw readback is limited only to the documented [0,10000] API domain;
        it is not treated as a calibrated mechanical limit or device receipt ACK.
        """
        if (len(angles)!=1 or not set(angles)<=set(range(1,7)) or
                set(held_targets)!=set(range(1,7)) or
                any(type(v) is not int or not 0<=v<=10000 for v in held_targets.values()) or
                any(not math.isfinite(v) or v<0 for v in angles.values()) or
                not set(angles)<=set(tolerances) or
                any(not math.isfinite(tolerances[axis]) or not 0<tolerances[axis]<=.1 for axis in angles) or
                not is_sdk_position_velocity(velocity) or current_raw!=1000):
            raise DeviceError("native_angles_command","invalid native angle/hold parameters")
        limits=self.get_angle_limits(tuple(angles))
        # Atomic range validation before any setter, including ALL.
        for axis,angle in angles.items():
            if not limits[axis][0]<=angle<=limits[axis][1]:
                raise DeviceError("set_target_angle",f"M{axis} requested={angle}; SDK limits={limits[axis]}; MOVE not sent")
        effective=dict(held_targets);sdk_angles={}
        for axis,angle in angles.items():
            self._motion_call("set_target_angle","set_target_angle",axis,angle)
            try:
                self._check_callback()
                raw=self._sdk.get_target_position(axis)
                accepted_angle=self._sdk.get_target_angle(axis)
                self._check_callback()
            except Exception as error:
                raise translate_vendor_error("native_angle_target_readback",error) from error
            if type(raw) is not int or not 0<=raw<=10000:
                raise DeviceError("set_target_angle",f"M{axis}: SDK raw readback {raw} outside documented API domain; MOVE not sent")
            if not math.isfinite(accepted_angle) or abs(accepted_angle-angle)>tolerances[axis]+1e-6:
                raise DeviceError("set_target_angle",f"M{axis}: SDK target angle readback {accepted_angle} differs from {angle}; MOVE not sent")
            effective[axis]=raw;sdk_angles[axis]=accepted_angle
        addressed=sorted(angles)
        speed_readback={}
        for axis in addressed:
            self._motion_call("set_position_velocity","set_position_velocity",axis,velocity)
            try:
                self._check_callback()
                speed_readback[axis]=self._sdk.get_position_velocity(axis)
                self._check_callback()
            except Exception as error:
                raise translate_vendor_error("get_position_velocity",error) from error
            if type(speed_readback[axis]) is not int or speed_readback[axis]!=velocity:
                raise DeviceError("set_position_velocity",
                    f"M{axis} requested={velocity}; SDK speed readback={speed_readback[axis]}; MOVE not sent")
            self._motion_call("set_max_current","set_max_current",axis,current_raw)
        stamp=utc_now()
        self._motion_call("move_motors","move_motors",addressed[0])
        return {"dispatch_utc":stamp,"effective_targets":effective,"sdk_limits":limits,
                "sdk_target_angles":sdk_angles,"sdk_accepted":True,"device_acknowledged":"UNKNOWN",
                "sdk_move_ids":addressed,"sdk_position_velocity":speed_readback,
                "speed_readback_source":"SDK_LOCAL_CACHE_NOT_DEVICE_SPEED_LIMIT_OR_ACK",
                "wire_axis_scope":"SDK_MANAGED_NOT_PROVEN_ISOLATED"}

    def angles_command(self, angles: dict[int, float], targets: dict[int, int],
                       velocity: int, current_raw: int,
                       raw_limits: dict[int, int]) -> dict:
        """Official angle setter; verify its local raw conversion BEFORE MOVE.

        Getter readback is a local SDK conversion check, not device acceptance.
        One requested motor uses move_motors(id); a group preloads six hold
        targets and uses the existing broadcast semantics.
        """
        if (not angles or not set(angles) <= {1,2,3,4} or
                set(targets) != set(range(1,7)) or set(raw_limits) != set(targets) or
                any(not math.isfinite(v) for v in angles.values()) or
                any(type(v) is not int or not 0 <= v <= raw_limits[axis] <= 2000
                    for axis,v in targets.items()) or
                (velocity,current_raw) != (500,1000)):
            raise DeviceError("angles_command", "invalid angle targets or scoped raw limits")
        addressed = sorted(angles) if len(angles)==1 else list(range(1,7))
        effective_targets=dict(targets)
        for axis in addressed:
            if axis in angles:
                self._motion_call("set_target_angle", "set_target_angle", axis, angles[axis])
                try:
                    self._check_callback()
                    converted = self._sdk.get_target_position(axis)
                    self._check_callback()
                except Exception as error:
                    raise translate_vendor_error("get_target_position_after_angle",error) from error
                if (not isinstance(converted,int) or not 0 <= converted <= raw_limits[axis] or
                        abs(converted-targets[axis]) > 1):
                    raise DeviceError("set_target_angle",
                        f"M{axis}: requested={angles[axis]} deg expected_raw={targets[axis]} "
                        f"sdk_converted_raw={converted} limit={raw_limits[axis]}; MOVE not sent")
                effective_targets[axis]=converted
            else:
                self._motion_call("set_target_position","set_target_position",axis,targets[axis])
            self._motion_call("set_position_velocity","set_position_velocity",axis,velocity)
            self._motion_call("set_max_current","set_max_current",axis,current_raw)
        dispatch_utc=utc_now()
        self._motion_call("move_motors","move_motors",addressed[0] if len(angles)==1 else 0)
        return {"dispatch_utc":dispatch_utc,"effective_targets":effective_targets}

    def read_control_mode(self, motor_id: int) -> int:
        if self._phase != "READY" or self._sdk is None or not 1 <= motor_id <= 6:
            raise DeviceError("get_control_mode", "requires READY and motor 1..6")
        self._check_callback()
        try:
            mode = self._sdk.get_control_mode(motor_id)
            self._check_callback()
            return mode
        except Exception as error:
            raise translate_vendor_error("get_control_mode", error) from error

    def positions_command(self, targets: dict[int, int], velocity: int,
                          current_raw: int) -> str:
        """Official per-axis setters followed by one SDK ID-0 broadcast MOVE."""
        if set(targets) != set(range(1, 7)):
            raise DeviceError("positions_command", "broadcast requires all six motor targets")
        for motor_id in range(1, 7):
            self._motion_call("set_target_position", "set_target_position",
                              motor_id, targets[motor_id])
            self._motion_call("set_position_velocity", "set_position_velocity",
                              motor_id, velocity)
            self._motion_call("set_max_current", "set_max_current",
                              motor_id, current_raw)
        dispatch_utc = utc_now()
        self._motion_call("move_motors", "move_motors", 0)
        return dispatch_utc

    def read_joint_states(self, active_dof: int) -> list[JointState]:
        try:
            joints = []
            for motor_id in range(1, active_dof + 1):
                self._check_callback()
                position = self._sdk.get_now_position(motor_id)
                status = self._sdk.get_now_status(motor_id)
                alarm = self._sdk.get_now_alarm(motor_id)
                joints.append(JointState(motor_id, position, status, alarm))
            self._check_callback()
            return joints
        except Exception as error:
            raise translate_vendor_error("read_joint_states", error) from error

    def close(self) -> None:
        self._phase = "CLOSING"
        errors = []
        if self._sdk is not None:
            try:
                self._sdk.close()
            except Exception as error:
                errors.append(str(error))
            self._sdk = None
        if self._bus is not None:
            worker = getattr(self._bus, "_worker", None)
            try:
                self._bus.close()
            except Exception as error:
                errors.append(str(error))
            if worker is not None and worker.is_alive():
                errors.append("RX worker still running after CANFD close")
            self._bus = None
        if self._dll_directory is not None:
            self._dll_directory.close()
            self._dll_directory = None
        if errors:
            raise DeviceError("close", "; ".join(errors))
        self._phase = "CLOSED"
