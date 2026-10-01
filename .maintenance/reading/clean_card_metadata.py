"""Move workflow metadata out of canonical paper cards without changing citations or notes."""

from __future__ import annotations

import csv
import io
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CARDS = ROOT / "02_论文"
TEMPLATE = ROOT / "99_模板" / "论文阅读模板.md"
READING = ROOT / ".maintenance" / "reading"
CITATION = ROOT / ".maintenance" / "citation"

READING_FIELDS = {
    "核验日期", "阅读状态", "摘要依据", "全文核验状态", "阅读核验状态",
    "阅读优先级", "最后阅读日期", "最后更新时间", "核验状态", "核验时间",
}
CITATION_FIELDS = {
    "引用量来源链接", "引用量查询日期", "引用量状态", "引用量查询状态",
}
FIELD = re.compile(r"^- ([^：\r\n]+)：([^\r\n]*)$", re.M)


def write_csv(path: Path, header: list[str], rows: list[list[str]]) -> None:
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(rows)
    path.write_text(output.getvalue(), encoding="utf-8-sig", newline="\n")


def main() -> None:
    cards = sorted(CARDS.glob("*/*.md"))
    reading_rows: list[list[str]] = []
    citation_rows: list[list[str]] = []
    count_before: dict[str, str] = {}
    year_before: dict[str, str] = {}
    notes_before: dict[str, str] = {}
    stats: dict[str, int] = {}

    for path in [*cards, TEMPLATE]:
        data = path.read_bytes()
        bom = b"\xef\xbb\xbf" if data.startswith(b"\xef\xbb\xbf") else b""
        body = data.decode("utf-8-sig")
        relative = path.relative_to(ROOT).as_posix()
        fields = dict(FIELD.findall(body))
        count_before[relative] = fields.get("引用量", "")
        year_before[relative] = fields.get("年份", "")
        notes_before[relative] = body.split("## 我的阅读笔记", 1)[-1] if "## 我的阅读笔记" in body else ""
        kept: list[str] = []
        for line in body.splitlines(keepends=True):
            match = FIELD.match(line.rstrip("\r\n"))
            key = match.group(1) if match else ""
            if key in READING_FIELDS | CITATION_FIELDS:
                value = match.group(2).strip()
                (reading_rows if key in READING_FIELDS else citation_rows).append([relative, key, value])
                stats[key] = stats.get(key, 0) + 1
                continue
            if key == "引用量来源" and match.group(2).strip() != "Google Scholar":
                citation_rows.append([relative, "原引用量来源", match.group(2).strip()])
                line = "- 引用量来源：Google Scholar" + ("\r\n" if line.endswith("\r\n") else "\n")
            if path == TEMPLATE and key == "引用量":
                line = "- 引用量：" + ("\r\n" if line.endswith("\r\n") else "\n")
            kept.append(line)
        result = "".join(kept)
        updated = dict(FIELD.findall(result))
        if updated.get("引用量", "") != ("" if path == TEMPLATE else count_before[relative]):
            raise ValueError(f"citation count changed: {relative}")
        if updated.get("年份", "") != year_before[relative]:
            raise ValueError(f"paper year changed: {relative}")
        if notes_before[relative] and not result.endswith(notes_before[relative]):
            raise ValueError(f"manual note section changed: {relative}")
        if result != body:
            path.write_bytes(bom + result.encode("utf-8"))

    READING.mkdir(parents=True, exist_ok=True)
    write_csv(READING / "card_metadata_archive.csv", ["canonical_file", "field", "value"], reading_rows)
    write_csv(CITATION / "card_metadata_archive.csv", ["canonical_file", "field", "value"], citation_rows)
    print(f"cards={len(cards)} removed={stats} reading_archive={len(reading_rows)} citation_archive={len(citation_rows)}")


if __name__ == "__main__":
    main()
