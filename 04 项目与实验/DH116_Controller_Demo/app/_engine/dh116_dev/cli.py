"""Existing Windows process conflict checks; no motion entry point."""
import json, os, subprocess, sys
from typing import Callable
from .errors import DeviceError

def _query_lhandpro_processes() -> list[dict]:
    """Read Windows process thread counts; never infer liveness from tasklist names."""
    script = (
        "$ErrorActionPreference='Stop'; "
        "$items=@(Get-CimInstance Win32_Process -Filter \"Name='LHandPro.exe'\" | "
        "Select-Object ProcessId,ThreadCount); "
        "ConvertTo-Json -InputObject $items -Compress"
    )
    output = subprocess.check_output(
        ["powershell.exe", "-NoProfile", "-NonInteractive", "-Command", script],
        text=True, timeout=5, stderr=subprocess.STDOUT)
    records = json.loads(output)
    if not isinstance(records, list):
        raise ValueError("unexpected LHandPro process query result")
    return records

def _lhandpro_running(*, on_stale: Callable[[dict], None] | None = None) -> bool:
    if os.name != "nt":
        return False
    try:
        records = _query_lhandpro_processes()
        if not isinstance(records, list):
            raise ValueError("process query did not return a list")
        for record in records:
            if not isinstance(record, dict) or type(record.get("ProcessId")) is not int or \
                    type(record.get("ThreadCount")) is not int or \
                    record["ProcessId"] <= 0 or record["ThreadCount"] < 0:
                raise ValueError("missing or invalid PID/ThreadCount")
    except Exception as error:
        raise DeviceError("preflight", "cannot verify LHandPro process state") from error
    for record in records:
        if record["ThreadCount"] == 0:
            message = (f"LHandPro preflight: PID {record['ProcessId']} "
                       "ThreadCount=0; terminated process record ignored; "
                       "CANFD availability remains subject to open result")
            print(message, file=sys.stderr, flush=True)
            if on_stale is not None:
                on_stale({"pid": record["ProcessId"], "thread_count": 0,
                          "diagnostic": message})
    return any(record["ThreadCount"] > 0 for record in records)
