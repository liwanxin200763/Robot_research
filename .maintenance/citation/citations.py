"""Local-only citation field cleanup, ranking, and validation.

Citation numbers are maintained by the user in the paper cards. This tool never
looks up citations or copies numbers from a cache, audit, or ranking file.
"""

from __future__ import annotations

import argparse
import csv
import io
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CARDS = ROOT / "02_论文"
RANKING = ROOT / "01_检索与审计" / "按引用量排序.md"
MANUAL = ROOT / "01_检索与审计" / "引用量待人工核验.md"
RANKING_CSV = ROOT / ".maintenance" / "citation" / "CITATION_RANKING.csv"
TEMPLATE = ROOT / "99_模板" / "论文阅读模板.md"

COUNT = "引用量"
SOURCE = "引用量来源"
SOURCE_VALUE = "Google Scholar"
VERIFIED_API_SOURCES = {"OpenAlex", "Semantic Scholar"}
SOURCE_EVIDENCE = {"引用量来源链接", "引用量查询日期", "引用量状态"}
REMOVE = {
    "引用量来源链接",
    "引用量查询日期",
    "引用量状态",
    "引用量查询状态",
    "OpenAlex Work ID",
    "排序引用量",
    "排序引用量来源",
    "citation_status",
    "citation_checked",
    "citation_source_url",
    "openalex_id",
    "openalex_work_id",
    "scholar_status",
    "citation audit status",
}
FIELD = re.compile(r"^- ([^：\r\n]+)：([^\r\n]*)", re.M)


def fields(body: str) -> list[tuple[str, str]]:
    return [(key, value.strip()) for key, value in FIELD.findall(body)]


def value(body: str, name: str) -> str:
    matches = [item for key, item in fields(body) if key == name]
    if len(matches) != 1:
        raise ValueError(f"expected one {name} field, found {len(matches)}")
    return matches[0]


def citation_number(raw: str) -> int | None:
    return int(raw.replace(",", "")) if re.fullmatch(r"[\d,]+", raw) else None


def card_paths() -> list[Path]:
    return sorted(CARDS.glob("*/*.md"))


def read_body(path: Path) -> tuple[str, bool]:
    data = path.read_bytes()
    return data.decode("utf-8-sig"), data.startswith(b"\xef\xbb\xbf")


def write_body(path: Path, body: str, bom: bool) -> None:
    path.write_bytes((b"\xef\xbb\xbf" if bom else b"") + body.encode("utf-8"))


def clean_text(body: str) -> tuple[str, int, bool]:
    before = value(body, COUNT)
    original_source = value(body, SOURCE)
    verified_api = original_source in VERIFIED_API_SOURCES
    kept = []
    removed = 0
    source_changed = False
    for line in body.splitlines(keepends=True):
        match = FIELD.match(line)
        key = match.group(1) if match else None
        if key in REMOVE and not (verified_api and key in SOURCE_EVIDENCE):
            removed += 1
            continue
        if key == SOURCE and not verified_api:
            ending = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
            replacement = f"- {SOURCE}：{SOURCE_VALUE}{ending}"
            source_changed = replacement != line
            kept.append(replacement)
        else:
            kept.append(line)
    result = "".join(kept)
    if value(result, COUNT) != before:
        raise ValueError("citation count changed during cleanup")
    return result, removed, source_changed


def clean(*, apply: bool = False) -> None:
    paths = card_paths()
    if not paths:
        raise ValueError("no paper cards found")
    changed = removed = sources = 0
    for path in [*paths, TEMPLATE]:
        body, bom = read_body(path)
        result, count, source_changed = clean_text(body)
        if result != body:
            changed += 1
            if apply:
                write_body(path, result, bom)
        removed += count
        sources += source_changed
    print(f"[CLEAN] cards={len(paths)} changed_files={changed} removed_fields={removed} source_changes={sources} applied={apply}")


@dataclass(frozen=True)
class Card:
    path: Path
    relative: str
    title: str
    year: str
    count_text: str
    count: int | None
    english_title: str = ""
    source: str = "Google Scholar"


def cards() -> list[Card]:
    output = []
    for path in card_paths():
        body, _ = read_body(path)
        count_text = value(body, COUNT)
        output.append(Card(path, path.relative_to(ROOT).as_posix(), path.stem,
                           value(body, "年份"), count_text, citation_number(count_text),
                           value(body, "英文标题"), value(body, SOURCE)))
    return output


def wikilink(card: Card) -> str:
    return f"[[{card.relative[:-3]}|{card.title}]]"


def ordered_cards(all_cards: list[Card]) -> tuple[list[Card], list[Card]]:
    numeric = sorted((card for card in all_cards if card.count is not None),
                     key=lambda card: (-card.count, card.title.casefold(), card.relative))
    missing = sorted((card for card in all_cards if card.count is None),
                     key=lambda card: (card.title.casefold(), card.relative))
    return numeric, missing


def ranking_text(all_cards: list[Card], today: str) -> str:
    numeric, missing = ordered_cards(all_cards)
    lines = ["# 按引用量排序", "", f"仅按当前论文卡的“引用量”字段排序；生成日期：{today}。生成过程不调用外部数据。", "", "## 数字引用量排序", ""]
    lines.extend(f"{index}. {wikilink(card)} — 引用量：{card.count_text}；年份：{card.year or '—'}"
                 for index, card in enumerate(numeric, 1))
    lines.extend(["", "## 待补充引用量", ""])
    lines.extend(f"- {wikilink(card)} — 引用量：{card.count_text or '空'}；年份：{card.year or '—'}"
                 for card in missing)
    return "\n".join(lines) + "\n"


def ranking_csv_text(all_cards: list[Card]) -> str:
    numeric, missing = ordered_cards(all_cards)
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(["canonical_file", "chinese_title", "english_title", "year", "category", "citation_count", "citation_source"])
    for card in [*numeric, *missing]:
        writer.writerow([card.relative, card.title, card.english_title, card.year,
                         card.path.parent.name, card.count_text, card.source])
    return output.getvalue()


def manual_text(all_cards: list[Card]) -> str:
    missing = [card for card in all_cards if card.count is None]
    zeros = [card for card in all_cards if card.count == 0 and card.source == SOURCE_VALUE]
    lines = ["# 引用量待人工核验", "", "仅提示需要人工查看的论文，不会修改论文卡的引用量。历史自动查询记录不作为当前数字依据。", "", "## 尚未填写数字", ""]
    lines.extend(f"- {wikilink(card)} — 当前引用量：{card.count_text or '空'}" for card in missing)
    lines.extend(["", "## 当前为 0，待人工确认", ""])
    lines.extend(f"- {wikilink(card)}" for card in zeros)
    return "\n".join(lines) + "\n"


def render(*, dry_run: bool = False) -> None:
    all_cards = cards()
    ranking = ranking_text(all_cards, date.today().isoformat())
    ranking_csv = ranking_csv_text(all_cards)
    manual = manual_text(all_cards)
    if not dry_run:
        RANKING.write_text(ranking, encoding="utf-8", newline="\n")
        RANKING_CSV.write_text(ranking_csv, encoding="utf-8-sig", newline="\n")
        MANUAL.write_text(manual, encoding="utf-8", newline="\n")
    print(f"[RENDER] ranked={len(all_cards)} missing={sum(c.count is None for c in all_cards)} zero={sum(c.count == 0 for c in all_cards)} dry_run={dry_run}")


def validate() -> None:
    all_paths = [*card_paths(), TEMPLATE]
    errors = []
    for path in all_paths:
        body, _ = read_body(path)
        items = fields(body)
        names = [name for name, _ in items]
        if names.count(COUNT) != 1 or names.count(SOURCE) != 1:
            errors.append(f"missing or duplicate citation field: {path}")
        source = [item for key, item in items if key == SOURCE]
        if len(source) != 1 or source[0] not in {SOURCE_VALUE, *VERIFIED_API_SOURCES}:
            errors.append(f"unexpected citation source: {path}")
        for name in names:
            allowed_evidence = source and source[0] in VERIFIED_API_SOURCES and name in SOURCE_EVIDENCE
            if (name in REMOVE or ("引用量" in name and name not in {COUNT, SOURCE})) and not allowed_evidence:
                errors.append(f"legacy citation field {name}: {path}")
    if errors:
        raise ValueError("\n".join(errors))
    print(f"[VALID] cards={len(all_paths) - 1} template=1 legacy_fields=0")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    cleanup = sub.add_parser("clean", help="preview cleanup; use --apply to write only field structure/source")
    cleanup.add_argument("--apply", action="store_true")
    rendering = sub.add_parser("render", help="render local ranking and manual review pages")
    rendering.add_argument("--dry-run", action="store_true")
    sub.add_parser("validate", help="validate citation fields without network access")
    for name in ("bootstrap", "update"):
        sub.add_parser(name, help="disabled: automatic citation lookup/writeback was retired")
    args = parser.parse_args()
    if args.command == "clean":
        clean(apply=args.apply)
    elif args.command == "render":
        render(dry_run=args.dry_run)
    elif args.command == "validate":
        validate()
    else:
        parser.error("automatic citation lookup/writeback is disabled; edit paper-card counts manually")


if __name__ == "__main__":
    main()
