"""Rebuild the strict CCF A Obsidian index from current canonical paper cards.

Run with ``python .maintenance/scripts/rebuild_ccf_a_library.py --write``.
The venue list is from the CCF 2026 seventh-edition AI conference A section.
An A venue alone is insufficient: the card must also link to official proceedings,
or be an explicitly verified exception below. Unverified candidates are reported.
"""

from __future__ import annotations

import argparse
import collections
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CARDS = ROOT / "02_论文"
OUTPUT = ROOT / "00_论文池" / "CCF A 论文库.md"
CCF_CATALOGUE = "https://www.ccf.org.cn/Academic_Evaluation/By_category/"
CCF_PDF_MIRROR = (
    "https://kyc.lsu.edu.cn/_upload/article/files/20/77/"
    "2cbaa3754eb9aff9ed74cafed8ff/23a8de02-594c-445f-b084-69b0193c05b3.pdf"
)
A_VENUES = ("AAAI", "NeurIPS", "ACL", "CVPR", "ICCV", "ICML", "ICLR")
PROCEEDINGS_HOSTS = (
    "ojs.aaai.org", "proceedings.neurips.cc", "proceedings.nips.cc",
    "openaccess.thecvf.com", "proceedings.mlr.press",
    "proceedings.iclr.cc", "aclanthology.org",
)

# These cards currently link an arXiv/OpenReview PDF instead of the final record.
# The listed identities and formal status were separately checked on 2026-10-06.
VERIFIED_EXCEPTIONS = {
    "HAMLET: Switch your Vision-Language-Action Model into a History-Aware Policy":
        "https://openreview.net/forum?id=KcJ9U0x6kO",
    "MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation":
        "https://proceedings.iclr.cc/papers/search?q=MemoryVLA",
    "RoboPARA: Dual-Arm Robot Planning with Parallel Allocation and Recomposition Across Tasks":
        "https://proceedings.iclr.cc/paper/2026/hash/e8aa3f5e8b5f24b830f31fd828e2a2a3-Abstract-Conference.html",
    "Sim2Real-VLA: Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation":
        "https://proceedings.iclr.cc/papers/search?q=Sim2Real%20VLA",
}


def field(text: str, key: str) -> str:
    match = re.search(r"^- " + re.escape(key) + r"：\s*(.*?)\s*$", text, re.M)
    return match.group(1).strip() if match else ""


def title_for_display(title: str) -> str:
    return re.sub(r"（AAAI 正式题名；.*?）$", "", title).strip()


def collect() -> tuple[list[dict[str, str | int]], list[str]]:
    records = []
    pending = []
    for card in sorted(CARDS.rglob("*.md")):
        data = card.read_text(encoding="utf-8-sig")
        venue_raw = field(data, "发表 venue")
        venue = next((v for v in A_VENUES if re.match(r"^" + v + r"\b", venue_raw, re.I)), "")
        if not venue:
            continue
        heading = re.search(r"^# ([^\r\n]+)", data, re.M)
        title = title_for_display(field(data, "英文标题") or (heading.group(1) if heading else ""))
        year_match = re.search(r"20\d{2}", field(data, "年份"))
        if not title or not year_match:
            pending.append(f"{card.relative_to(ROOT)}：缺英文一级标题或年份")
            continue
        paper_line = field(data, "论文链接")
        urls = re.findall(r"https?://[^\s)\]>]+", paper_line)
        official = next((u for u in urls if any(host in u.lower() for host in PROCEEDINGS_HOSTS)), "")
        if not official:
            official = VERIFIED_EXCEPTIONS.get(title, "")
        if not official:
            pending.append(f"{card.relative_to(ROOT)}：A 类 venue 但正式论文入口待核验")
            continue
        records.append({
            "title": title,
            "year": int(year_match.group()),
            "venue": venue,
            "category": card.parent.name,
            "path": card.relative_to(ROOT).with_suffix("").as_posix(),
            "official": official,
        })
    return records, pending


def render(records: list[dict[str, str | int]], pending: list[str]) -> str:
    year_count = collections.Counter(int(r["year"]) for r in records)
    venue_count = collections.Counter(str(r["venue"]) for r in records)
    category_count = collections.Counter(str(r["category"]) for r in records)
    lines = [
        "# CCF A 论文库", "",
        "依据 [CCF 第七版正式目录](" + CCF_CATALOGUE + ")的人工智能会议 A 类清单核验；"
        "[正式 PDF 校核副本](" + CCF_PDF_MIRROR + ")第 57 页列出 AAAI、NeurIPS、ACL、CVPR、ICCV、ICML、ICLR。"
        "只收录当前文献库中有正式论文身份及可核对入口的唯一主卡；CoRL、ICRA、ECCV、预印本不因研究价值高而计入。"
        "论文标题和链接取自当前 `02_论文`，阅读笔记及引用量不参与本索引。核验日期：2026-10-06。",
        "", "## 统计", "", f"- 总数：{len(records)}", "",
    ]
    for year in sorted(year_count):
        lines.append(f"- {year}：{year_count[year]}")
    lines.extend(["", "### 会议与期刊", ""])
    for venue in A_VENUES:
        lines.append(f"- {venue}：{venue_count[venue]}")
    lines.extend(["", "### 主分类（互斥）", ""])
    for category in sorted(category_count):
        lines.append(f"- {category}：{category_count[category]}")
    lines.extend(["", "## 论文索引", ""])
    for category in sorted(category_count):
        lines.extend([f"### {category}", ""])
        subset = [r for r in records if r["category"] == category]
        subset.sort(key=lambda r: (-int(r["year"]), str(r["title"]).casefold()))
        for r in subset:
            lines.append(
                f"- [[{r['path']}|{r['title']}]] · {r['year']} · {r['venue']} · "
                f"[正式论文]({r['official']})"
            )
        lines.append("")
    lines.extend([
        "## 更新规则", "",
        "新建论文主卡后，先核验 CCF 正式目录中的 venue 等级和该论文的正式发表身份，"
        "再运行 `python .maintenance/scripts/rebuild_ccf_a_library.py --write`。"
        "脚本会列出证据不足的 A 类 venue 候选，不会仅凭 venue 自动收录。",
        "",
    ])
    if pending:
        lines.extend(["## 待核验候选（未计入）", ""])
        lines.extend(f"- {item}" for item in pending)
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    records, pending = collect()
    result = render(records, pending)
    if args.write:
        OUTPUT.write_text(result, encoding="utf-8")
    print(f"CCF A cards: {len(records)}; pending: {len(pending)}; wrote: {args.write}")
    for item in pending:
        print("PENDING", item)


if __name__ == "__main__":
    main()
