"""Fail-closed EXP05 access policy with a one-use onsite HOME diagnostic grant."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
import hashlib
import json
import secrets
from threading import Lock
import time
from typing import Callable

from dh116_dev.models import DeviceConfig


BLOCKER_ID = "EXP05_MULTI_HOME_UNRESOLVED_20261009"
LIVE_BLOCK_REASON = (
    f"{BLOCKER_ID}: 多电机 HOME 状态异常尚未完成真机验收；"
    "普通单轴/多轴 MOVE 和抓取仍被锁定。HOME-only 仅能经独立现场一次性批准入口执行。"
)


class AccessLevel(str, Enum):
    READ_ONLY = "READ_ONLY"
    HOME_ONLY_DIAGNOSTIC = "HOME_ONLY_DIAGNOSTIC"
    SINGLE_AXIS_MOVE = "SINGLE_AXIS_MOVE"
    MULTI_AXIS_MOVE = "MULTI_AXIS_MOVE"
    THREE_FINGER_GRASP = "THREE_FINGER_GRASP"


@dataclass(frozen=True, slots=True, eq=False)
class HomeOnlyApproval:
    level: AccessLevel
    run_id: str
    config_digest: str
    confirmed_utc: str
    expires_monotonic: float
    _token: str
    plan_digest: str | None = None

    @property
    def onsite_record(self) -> dict[str, str]:
        return {
            "level": self.level.value,
            "run_id": self.run_id,
            "confirmation_method": "SINGLE_YES",
            "confirmed_utc": self.confirmed_utc,
        }


_APPROVAL_TTL_SECONDS = 300.0
_issued: dict[str, HomeOnlyApproval] = {}
_issued_lock = Lock()


def _fingerprint(config: DeviceConfig) -> str:
    payload = json.dumps(config.as_dict(), sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _plan_fingerprint(plan: dict) -> str:
    payload = json.dumps(plan, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def collect_single_axis_approval(
    config: DeviceConfig, run_id: str, plan: dict, *,
    input_fn: Callable[[str], str] = input,
) -> HomeOnlyApproval:
    """One use, bound to the printed M3 plan; ordinary MOVE remains locked."""
    if not run_id or config.hand_model != "DH116" or plan.get("motor_id") != 3:
        raise RuntimeError("single-axis approval requires an M3 plan and run ID")
    try:
        prompt = ("即将执行 DH116 单轴实验：六轴广播 HOME、受监测地切回位置模式后只移动 M3，"
                  "目标及返回参数见上方计划；六轴 HOME 可能运动完整行程。"
                  "异常会尝试 stop_all、disable_all、close 并保存日志。\n"
                  "本次 run_id=" + run_id + "。输入 YES：")
        if input_fn(prompt) != "YES":
            raise RuntimeError("single-axis approval requires YES")
    except (EOFError, KeyboardInterrupt, StopIteration) as error:
        raise RuntimeError("single-axis approval input incomplete") from error
    approval = HomeOnlyApproval(
        AccessLevel.SINGLE_AXIS_MOVE, run_id, _fingerprint(config),
        datetime.now(timezone.utc).isoformat(),
        time.monotonic() + _APPROVAL_TTL_SECONDS,
        secrets.token_hex(16), _plan_fingerprint(plan),
    )
    with _issued_lock:
        _issued[approval._token] = approval
    return approval


def require_single_axis_approval(
    approval: HomeOnlyApproval | None, config: DeviceConfig,
    run_id: str, plan: dict,
) -> None:
    if approval is None:
        raise RuntimeError("single-axis approval required before adapter access")
    with _issued_lock:
        issued = _issued.pop(approval._token, None)
    if (issued is not approval or approval.level != AccessLevel.SINGLE_AXIS_MOVE or
            approval.run_id != run_id or approval.config_digest != _fingerprint(config) or
            approval.plan_digest != _plan_fingerprint(plan) or
            time.monotonic() > approval.expires_monotonic):
        raise RuntimeError("single-axis approval is invalid, expired, or already used")


def collect_motion_session_approval(
    config: DeviceConfig, run_id: str, plan: dict, *,
    input_fn: Callable[[str], str] = input,
) -> HomeOnlyApproval:
    """Grant one printed, immutable EXP05 session; legacy MOVE remains locked."""
    if not run_id or config.hand_model != "DH116" or not plan.get("stages"):
        raise RuntimeError("motion session requires a DH116 plan and run ID")
    try:
        answer = input_fn(
            f"EXP05 run_id={run_id}: six-axis HOME may traverse the full range; "
            "broadcast MOVE addresses all six motors, including held axes. "
            "Check the printed targets, travel space and independent power cut. "
            "Type YES once to authorize this exact session: "
        )
    except (EOFError, KeyboardInterrupt, StopIteration) as error:
        raise RuntimeError("motion session approval input incomplete") from error
    if answer != "YES":
        raise RuntimeError("motion session approval requires YES")
    approval = HomeOnlyApproval(
        AccessLevel.MULTI_AXIS_MOVE, run_id, _fingerprint(config),
        datetime.now(timezone.utc).isoformat(),
        time.monotonic() + _APPROVAL_TTL_SECONDS,
        secrets.token_hex(16), _plan_fingerprint(plan),
    )
    with _issued_lock:
        _issued[approval._token] = approval
    return approval


def require_motion_session_approval(
    approval: HomeOnlyApproval | None, config: DeviceConfig,
    run_id: str, plan: dict,
) -> None:
    if approval is None:
        raise RuntimeError("motion session approval required before adapter access")
    with _issued_lock:
        issued = _issued.pop(approval._token, None)
    if (issued is not approval or approval.level != AccessLevel.MULTI_AXIS_MOVE or
            approval.run_id != run_id or approval.config_digest != _fingerprint(config) or
            approval.plan_digest != _plan_fingerprint(plan) or
            time.monotonic() > approval.expires_monotonic):
        raise RuntimeError("motion session approval is invalid, expired, or already used")


def collect_home_only_approval(
    config: DeviceConfig, run_id: str, *, input_fn: Callable[[str], str] = input
) -> HomeOnlyApproval:
    """Collect a fresh, run-bound onsite approval before any adapter access."""
    if not run_id or config.hand_model != "DH116":
        raise RuntimeError("HOME-only approval requires DH116 configuration and a run ID")
    try:
        prompt = (
            "即将执行 DH116 HOME-only：\n"
            "- 不执行 MOVE\n"
            "- 使用 enable_all + home_all\n"
            "- 六轴可能运动\n"
            "- 异常会尝试停止并保存日志\n\n"
            "输入：\nYES\n> "
        )
        if input_fn(prompt) != "YES":
            raise RuntimeError("HOME-only approval requires YES")
    except (EOFError, KeyboardInterrupt, StopIteration) as error:
        raise RuntimeError("HOME-only approval input incomplete") from error
    approval = HomeOnlyApproval(
        AccessLevel.HOME_ONLY_DIAGNOSTIC, run_id, _fingerprint(config),
        datetime.now(timezone.utc).isoformat(),
        time.monotonic() + _APPROVAL_TTL_SECONDS, secrets.token_hex(16),
    )
    with _issued_lock:
        _issued[approval._token] = approval
    return approval


def require_access(
    level: AccessLevel, *, approval: HomeOnlyApproval | None = None,
    config: DeviceConfig | None = None, run_id: str | None = None,
) -> None:
    if level == AccessLevel.READ_ONLY:
        return
    if level == AccessLevel.HOME_ONLY_DIAGNOSTIC:
        if approval is None or config is None or run_id is None:
            raise RuntimeError("HOME-only approval is required before adapter access")
        with _issued_lock:
            issued = _issued.pop(approval._token, None)
        if (issued is not approval or approval.level != level or
                approval.run_id != run_id or approval.config_digest != _fingerprint(config) or
                time.monotonic() > approval.expires_monotonic):
            raise RuntimeError("HOME-only approval is invalid, expired, or already used")
        return
    raise RuntimeError(LIVE_BLOCK_REASON)


def require_live_authorized() -> None:
    """Legacy EXP05 control paths remain blocked, regardless of HOME approval."""
    require_access(AccessLevel.MULTI_AXIS_MOVE)
