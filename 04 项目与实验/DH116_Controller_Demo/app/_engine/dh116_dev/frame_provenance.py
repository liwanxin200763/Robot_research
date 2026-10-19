"""Conservative labels for adapter callbacks, independent of SDK decoding."""


def classify_callback(can_id: int, node_id: int | None, adapter_echo: bool | None) -> str:
    if adapter_echo is True:
        return "ADAPTER_TAGGED_LOCAL_ECHO"
    if node_id is None:
        return "ADAPTER_CALLBACK_SOURCE_UNKNOWN"
    if can_id == 0x480 + node_id:
        return "RX_CALLBACK_RETURN_ID_NOT_DEVICE_ACK"
    if can_id == 0x580 + node_id:
        return "RX_CALLBACK_SDO_RETURN_ID_NOT_MOTION_ACK"
    if can_id in (0x500 + node_id, 0x600 + node_id):
        return "COMMAND_FORMAT_CAPTURE_SOURCE_UNKNOWN"
    return "ADAPTER_CALLBACK_SOURCE_UNKNOWN"


def callback_direction(provenance: str) -> str:
    """Adapter callback direction, never a claim of hand-side acceptance."""
    if provenance == "ADAPTER_TAGGED_LOCAL_ECHO":
        return "LOCAL_ECHO"
    if provenance in ("RX_CALLBACK_RETURN_ID_NOT_DEVICE_ACK",
                      "RX_CALLBACK_SDO_RETURN_ID_NOT_MOTION_ACK"):
        return "ADAPTER_RX_CALLBACK"
    return "UNKNOWN"
