"""Readable meanings of the official LHandProLib C error codes."""

from __future__ import annotations


SDK_ERROR_TEXT = {
    0: "success",
    1: "invalid parameter",
    2: "required callback/function is not initialized",
    3: "failed to read configuration",
    4: "unexpected device data",
    5: "communication connection error",
    6: "communication send error",
    7: "communication receive error",
    8: "communication data format error",
    9: "invalid file path",
    10: "failed to save log file",
    11: "device has not homed",
    999: "unknown SDK error",
}

# LHandProLib.h C_LAM_* device alarm values; distinct from SDK return codes.
ALARM_TEXT = {
    0: "No alarm", 1: "Position error", 2: "Over speed",
    3: "Over current", 4: "Over load", 5: "Over voltage",
    6: "Under voltage", 7: "Encoder error", 8: "Stall",
    9: "Other alarm",
}


def alarm_text(code: int) -> str:
    return ALARM_TEXT.get(code, "Unknown device alarm")


def sdk_error_text(code: int) -> str:
    return SDK_ERROR_TEXT.get(code, "unrecognized SDK return code")


class DeviceError(RuntimeError):
    def __init__(self, operation: str, message: str, code: int | None = None):
        self.operation = operation
        self.code = code
        self.message = message
        suffix = f" (SDK code {code}: {sdk_error_text(code)})" if code is not None else ""
        super().__init__(f"{operation}: {message}{suffix}")


def check_sdk_result(code: int, operation: str) -> None:
    if code != 0:
        raise DeviceError(operation, "SDK call failed", code)


def translate_vendor_error(operation: str, error: Exception) -> DeviceError:
    if isinstance(error, DeviceError):
        return error
    code = getattr(error, "error_code", getattr(error, "code", None))
    return DeviceError(operation, str(error), code if isinstance(code, int) else None)
