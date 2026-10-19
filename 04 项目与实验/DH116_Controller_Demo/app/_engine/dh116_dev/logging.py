"""One immutable-on-disk directory per experiment run."""

from __future__ import annotations

import csv
import hashlib
import json
import secrets
import subprocess
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from .models import DeviceConfig, HandInfo
from .state import RawFeedback
from .frame_provenance import callback_direction


def _sha256(path: Path) -> str | None:
    if not path.is_file():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _git_hash(project_root: Path) -> str | None:
    try:
        return subprocess.check_output(
            ["git", "-C", str(project_root), "rev-parse", "HEAD"],
            stderr=subprocess.DEVNULL, text=True, timeout=3).strip()
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return None


class RunRecorder:
    COLUMNS = (
        "run_id", "timestamp_utc", "motor_id", "now_position", "now_angle_deg",
        "target_position", "status", "alarm", "raw_frame_count",
        "position_frame_count", "first_valid_feedback_utc", "experiment_phase",
        "last_position_feedback_utc", "position_feedback_age_ms", "feedback_freshness_scope",
    )

    def __init__(self, project_root: Path, experiment: str,
                 config: DeviceConfig, dll_path: Path,
                 output_root: Path | None = None):
        self.project_root = Path(project_root).resolve()
        self.experiment = experiment
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        self.run_id = f"{stamp}-{secrets.token_hex(3)}"
        self.directory = ((Path(output_root).resolve() if output_root is not None else
                           self.project_root / "experiments" / experiment / "results") /
                          self.run_id)
        self.directory.mkdir(parents=True, exist_ok=False)
        self.jsonl_path = self.directory / "events.jsonl"
        self.raw_path = self.directory / "raw_frames.jsonl"
        self.csv_path = self.directory / "samples.csv"
        self.summary_path = self.directory / "summary.md"
        self._events = self.jsonl_path.open("w", encoding="utf-8", newline="\n")
        self._raw = self.raw_path.open("w", encoding="utf-8", newline="\n")
        self._samples = self.csv_path.open("w", encoding="utf-8", newline="")
        self._writer = csv.DictWriter(self._samples, fieldnames=self.COLUMNS)
        self._writer.writeheader()
        snapshot = {
            "run_id": self.run_id,
            "created_utc": datetime.now(timezone.utc).isoformat(),
            "experiment": experiment,
            "device": config.as_dict(),
            "git_commit": _git_hash(self.project_root),
            "sdk_dll_path": str(dll_path.resolve()),
            "sdk_dll_sha256": _sha256(dll_path),
            "firmware_version": None,
            "hand_serial_number": None,
            "adapter_serial_number": config.adapter_serial,
        }
        self.snapshot_path = self.directory / "config.json"
        self._snapshot = snapshot
        self._write_snapshot()
        self.event("run_created")

    def _write_snapshot(self) -> None:
        self.snapshot_path.write_text(json.dumps(self._snapshot, ensure_ascii=False,
                                                 indent=2) + "\n", encoding="utf-8")

    def set_hand_info(self, info: HandInfo) -> None:
        self._snapshot["firmware_version"] = info.firmware_version
        self._snapshot["hand_serial_number"] = info.serial_number
        self._write_snapshot()
        self.event("hand_info", **asdict(info))

    def set_experiment_metadata(self, **fields: Any) -> None:
        self._snapshot.update(fields)
        self._write_snapshot()
        self.event("experiment_metadata", **fields)

    def event(self, name: str, **fields: Any) -> None:
        row = {"run_id": self.run_id, "timestamp_utc": datetime.now(timezone.utc).isoformat(
            timespec="milliseconds"), "event": name, **fields}
        self._events.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")
        self._events.flush()

    def raw_frame(self, frame: RawFeedback, *, dlc: int | None,
                  experiment_phase: str | None = None, flush: bool = True) -> None:
        row = {
            "run_id": self.run_id,
            "timestamp_utc": frame.timestamp_utc,
            "can_id": frame.can_id,
            "frame_type": frame.frame_type,
            "dlc": dlc,
            "payload_length": frame.payload_length,
            "payload_hex": frame.payload_hex,
            "is_0x50": frame.frame_type == 0x50,
            "phase": frame.phase,
            "experiment_phase": experiment_phase,
            "decoded_by_sdk": frame.decoded_by_sdk,
            "sdk_error_code": frame.sdk_error_code,
            "adapter_echo": frame.adapter_echo,
            "adapter_timestamp": frame.adapter_timestamp,
            "provenance": frame.provenance,
            "direction": callback_direction(frame.provenance),
            "raw_payload_fields": frame.fields(),
        }
        self._raw.write(json.dumps(row, ensure_ascii=False) + "\n")
        if flush:
            self._raw.flush()

    def raw_frames(self, frames: Iterable[RawFeedback], *,
                   experiment_phase: str | None = None) -> None:
        """Write each drained bounded batch immediately; flush once per batch."""
        for frame in frames:
            self.raw_frame(frame, dlc=frame.dlc, experiment_phase=experiment_phase,
                           flush=False)
        self._raw.flush()

    def sample(self, sample: Any, *, experiment_phase: str | None = None) -> None:
        for motor in sample.motors:
            self._writer.writerow({
                "run_id": self.run_id, "timestamp_utc": sample.timestamp_utc,
                "motor_id": motor.motor_id, "now_position": motor.now_position,
                "now_angle_deg": motor.now_angle_deg,
                "target_position": motor.target_position, "status": motor.status,
                "alarm": motor.alarm, "raw_frame_count": sample.raw_frame_count,
                "position_frame_count": sample.position_frame_count,
                "first_valid_feedback_utc": sample.first_valid_feedback_utc,
                "experiment_phase": experiment_phase,
                "last_position_feedback_utc": getattr(sample, "last_position_feedback_utc", None),
                "position_feedback_age_ms": (
                    (sample.sampled_monotonic-sample.last_position_feedback_monotonic)*1000
                    if getattr(sample, "sampled_monotonic", None) is not None and
                    getattr(sample, "last_position_feedback_monotonic", None) is not None else None),
                "feedback_freshness_scope": "TRANSPORT_0x50_NOT_PER_AXIS_GETTER",
            })
        self._samples.flush()

    def finish(self, result: str, notes: list[str]) -> None:
        try:
            self._finish_report(result, notes)
        finally:
            # A failed report write must not leave files/Windows handles open.
            close_errors = []
            for stream in (self._events, self._raw, self._samples):
                try:
                    stream.close()
                except Exception as error:
                    close_errors.append(str(error))
            if close_errors:
                raise OSError("log stream close failed: " + "; ".join(close_errors))

    def _finish_report(self, result: str, notes: list[str]) -> None:
        self.event("run_finished", result=result)
        description = {
            "SEQUENCE_COMPLETE": "已完成本次计划的命令与清理流程；各阶段反馈需结合下方分析判读。",
            "HOME_ONLY_SEQUENCE_COMPLETE": "HOME-only 命令、六轴监测和清理流程已完成；物理回零仍须结合现场观察确认。",
            "SINGLE_AXIS_SEQUENCE_COMPLETE": "单轴命令、返回及清理流程已完成；机械方向仍须结合现场观察确认。",
            "SESSION_COMPLETE_SDK_FEEDBACK_ONLY": "本次动作序列及清理流程完成；SDK反馈不等于物理夹持或同步到达证明。",
            "MOCK_ONLY": "仅生成合成数据，未连接真机。",
            "DRY_RUN_ONLY": "仅检查计划，未连接真机。",
            "READ_ONLY_SUCCESS": "只读采样流程完成。",
            "MOCK_SUCCESS": "模拟采样流程完成，未连接真机。",
        }.get(result, "流程未完整完成，请结合事件记录和备注检查。")
        title = self.experiment.split("_", 1)[0].upper()
        lines = [f"# {title} 实验结果摘要", "", f"run_id：`{self.run_id}`", "",
                 "## 实验结果", "", f"实验状态：`{result}`", "", description, "",
                 "## 记录文件", "", f"采样：`{self.csv_path.name}`",
                 f"事件：`{self.jsonl_path.name}`",
                 f"配置：`{self.snapshot_path.name}`", "", "## 备注", ""]
        lines.extend(f"- {note}" for note in notes)
        self.summary_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
