# Literature Field Completeness Report

日期：2026-09-21
范围：133 张 active canonical cards。

## Evidence Upgrade

| 状态 | 数量 |
|---|---:|
| Evidence Quality A / A-Upgraded | 2 |
| Evidence B — Fulltext unavailable or not reliably extractable | 86 |
| Evidence B — Supplement missing / not checked | 0 |
| Evidence B — Experiment not extracted | 2 |
| Evidence B — Code unverified | 43 |
| Evidence B — Metadata-only source | 0 |
| Manual review needed | 0 |

Evidence B 的原因已逐卡写入 `Evidence Upgrade Status`；B 不再是一个无解释的笼统标签。`A-Upgraded` 只保留给 AnyBimanual 和 ManipLLM，其他论文没有因为摘要内容而升级为 A。

## Other coverage

- Citation Count verified: 60 / 133；Unknown: 73
- DOI explicitly present: 27 / 133
- arXiv URL explicitly present: 6 / 133
- Full-paper enrichment marker: 133 / 133
- Main Results with numeric evidence in the current enriched cards: 7（保守文本扫描，仍需逐表复核）
- Ablation entries with explicit evidence or an explicit Not Reported status: 133；其中有数据的核心卡集中在 Batch 01
- Failure Cases: all 133 have an explicit evidence status; most remain Unknown / Not Explicitly Reported
- Limitations: all 133 have an explicit author-stated or library-analysis status; many still need primary-text extraction
- Remaining Unsolved Problem: all 133 have an explicit status; evidence-backed detail remains concentrated in Batch 01
- Idea Clues: all 133 have an explicit status; many later-batch cards remain evidence-pending

## Code and hardware

- Code Completeness: Mostly Complete 24; Partial 8; Unavailable 44; Unknown 57
- Robot Platform Evidence: field synchronized for all 133 cards; exact hardware confirmation still requires paper-level extraction for most B cards
- Supplement Status: currently recorded as Not Checked unless a future batch verifies the supplement directly

Citation source remains OpenAlex where a high-confidence identifier exists. No fuzzy citation value was inserted.
