# RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models

## Basic Information（基本信息）

- Title: RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models
- Year: 2025
- Venue / Source: CoRL
- Publication Status: Formal PMLR v305 / CoRL 2025
- CCF Level: Not CCF A (robotics venue extension; CCF row not asserted)
- Type: Method Paper
- Category: VLA / Robot Foundation Models / Robot Manipulation
- Subcategory: VLA / Robot Foundation Models
- Priority: P1

## Classification

- Primary Category: VLA
- Categories: VLA; Robot Manipulation
- Subcategories: VLA / Robot Foundation Models
- Tags: Unknown

## Links（链接）

- Official Paper: https://proceedings.mlr.press/v305/kwok25a.html
- arXiv: 待补充
- Project Page: 待补充
- Official GitHub: 待补充

## Code（代码状态）

- Code Status: Unknown
- Checkpoint: 待补充
- Dataset Released: Unknown

## Embodiment（机器人形态）

- Single Arm / Bimanual / Dexterous Hand / Gripper: Unknown
- Real Robot: Unknown

## Why Collected（为什么被收录）

待阅读后补充。

## Verification（待核验）

- [x] Venue 已确认
- [ ] CCF 等级已确认
- [x] Official Paper 已确认
- [ ] Official GitHub 已确认
- [ ] Code 可运行性已确认
- [ ] 是否真机已确认

## Citation Metrics

- Citation Count: Unknown
- Citation Source: OpenAlex (exact identity unresolved; API coverage may limit lookup)
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: Unknown (exact scholarly work unresolved)
- OpenAlex Work: Unknown

## Standardized Research Fields

### Research Problem
Unknown / Needs Full-Paper Verification

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
Unknown / Needs Full-Paper Verification

### Main Contributions
Unknown / Needs Full-Paper Verification

### Dataset & Benchmark
Unknown / Needs Full-Paper Verification

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Unknown / Needs Full-Paper Verification

### Main Results
Unknown / Needs Full-Paper Verification

### Limitations
Unknown / Needs Full-Paper Verification

### What Remains Unsolved?
Library Analysis / Research Note: Unknown / Needs Full-Paper Verification

### Relevance to Our Project
Unknown / Needs Project-Specific Review

## Full-paper Enrichment (Batch 02)

- Evidence Quality: B
- Evidence Status: Official full text was not reliably extractable in this batch; structured fields below preserve existing card evidence and mark unresolved details explicitly.

### Research Problem
Unknown / Needs Full-Paper Verification

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
Unknown / Needs Full-Paper Verification

### Architecture / Key Components
Unknown / Needs Official Full-Text Verification

### Dataset & Benchmark
Unknown / Needs Full-Paper Verification

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Unknown / Needs Full-Paper Verification

### Main Results
Unknown / Needs Full-Paper Verification

### Ablation Study
Unknown / Not Explicitly Reported in the currently accessible sources.

### Failure Cases
Unknown / Not Explicitly Reported in the currently accessible sources.

### Limitations
Unknown / Needs Full-Paper Verification

### What Remains Unsolved?
Library Analysis / Research Note: Unknown / Needs Full-Paper Verification

### Open Source
- Official GitHub: 待补充
- Code Status: Unknown
- Checkpoint: 待补充
- Dataset: Unknown

### Relevance to Our Project
Unknown / Needs project-specific review

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://proceedings.mlr.press/v305/kwok25a.html

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Fulltext-Unavailable
- Supplement Status: Not Found
- Code Completeness: Unknown
- Robot Platform Evidence: Unknown

## Deep Enrichment (Full Text Read: 2026-09-22)
- Evidence Quality: A
- Fulltext Checked: Yes — arXiv HTML 2506.17811v2, Secs. 3–6 and Appendices C–H inspected.
- Supplement Status: Available - Verified.
- Method: sample multiple VLA actions, apply Gaussian perturbation/majority voting, then select with a VLM action verifier trained from synthetic preference data (Secs. 3–4).
- Baselines / Results: existing VLAs gain 25% absolute on OOD tasks, 9% on ID tasks, and 7% when verifier and policy are jointly fine-tuned for new setups (abstract, Sec. 5).
- Ablation: action-selection rules, sample count, generalist policy, reward margin and preference learning are isolated in Appendices C–F.
- Failure Cases / Limitations: computational overhead, synthetic-data scaling and evaluation scope are explicit limitations (Sec. 6); verifier mistakes remain a deployment risk.
- Remaining Gap / Idea: adaptive sample budgets tied to uncertainty for real-time manipulation.
- Evidence Sources: https://arxiv.org/html/2506.17811 ; https://robomonkey-vla.github.io/.
- Evidence Upgrade Status: A-Upgraded

## Citation Relations

### References in Library

- [[02_Papers/01_VLA/CoT-VLA|CoT-VLA]] — [arXiv full-text bibliography item 18](https://arxiv.org/html/2506.17811#bib.bib18)
- [[02_Papers/01_VLA/Octo|Octo]] — [arXiv full-text bibliography item 34](https://arxiv.org/html/2506.17811#bib.bib34)
- [[02_Papers/01_VLA/OpenVLA|OpenVLA]] — [arXiv full-text bibliography item 2](https://arxiv.org/html/2506.17811#bib.bib2)
- [[02_Papers/10_Benchmark_Dataset/DROID|DROID]] — [arXiv full-text bibliography item 6](https://arxiv.org/html/2506.17811#bib.bib6)
- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open_X-Embodiment]] — [arXiv full-text bibliography item 7](https://arxiv.org/html/2506.17811#bib.bib7)

### Cited By in Library

- [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI|A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]] — [arXiv full-text bibliography item 81](https://arxiv.org/html/2405.14093#bib.bib81)
- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]] — [arXiv full-text bibliography item 915](https://arxiv.org/html/2510.10903#bib.bib915)

### Related Work

- No curated content relation yet.

## Quick Summary

- Problem: Vision-Language-Action (VLA) models have demonstrated remarkable capabilities in visuomotor control, yet ensuring their robustness in unstructured real-world environments remains a persistent challenge.
- Previous Gap: Not established in checked summary source.
- Core Idea: Building on these insights, we introduce RoboMonkey, a test-time scaling framework for VLAs.
- Input: Not specified in checked abstract/card.
- Output / Action: Not specified in checked abstract/card.
- Dataset / Benchmark: Not specified in checked abstract/card.
- Main Result: Additionally, when adapting to new robot setups, we show that fine-tuning both VLAs and action verifiers yields a 7% performance increase compared to fine-tuning VLAs alone.
- Why It Matters: High — informs language-conditioned manipulation and VLA design.
- Project Relevance: High — informs language-conditioned manipulation and VLA design.
- Key Limitation: Not established by the checked summary source; consult the full paper.
- Summary Evidence: Official abstract / paper page; https://arxiv.org/html/2506.17811; checked 2026-09-23. Rapid summary only; existing Evidence Quality is unchanged.
- Quick Summary Status: Evidence-backed
