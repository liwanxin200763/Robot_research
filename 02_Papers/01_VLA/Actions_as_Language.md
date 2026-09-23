# Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting

## Basic Information（基本信息）

- Title: Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting
- Year: 2026
- Venue / Source: ICLR
- Publication Status: ICLR 2026 Conference
- CCF Level: A (CCF 7th edition; venue category not independently extracted from official PDF)
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

- Official Paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html
- arXiv: https://arxiv.org/abs/2509.22195
- Project Page: https://vlm2vla.github.io/
- Official GitHub: Not found after official project/repository search

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

- Citation Count: 0
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W7083676685
- OpenAlex Work: https://openalex.org/W7083676685

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

- Evidence Quality: A
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
- Official GitHub: Not found after official project/repository search
- Code Status: Unknown
- Checkpoint: 待补充
- Dataset: Unknown

### Relevance to Our Project
Unknown / Needs project-specific review

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://proceedings.iclr.cc/paper_files/paper/2026/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: A-Upgraded
- Supplement Status: Not Found
- Code Completeness: Unknown
- Robot Platform Evidence: Unknown

## Deep Enrichment (Full Text Read: 2026-09-22)
- Evidence Quality: A
- Fulltext Checked: Yes — arXiv HTML 2509.22195 / ICLR 2026 paper, Sections 3–5 and Appendices 6–9 inspected.
- Supplement Status: Available - Verified (Appendix sections and implementation details accessible in the official arXiv HTML).
- Method: VLM2VLA represents control hierarchically as high-level subtask language, mid-level directional motion plan, and low-level action-chunk text; Gemini 2.5 Pro/Flash creates the relabeling and a verifier closes the loop (Sec. 3.1).
- Backbone / Action: Gemma-3-12B-IT with LoRA; translational end-effector commands are represented as language, with variable-length action chunks (Sec. 3.1, 6.3).
- Dataset: human-teleoperated BridgeV2 trajectories are relabeled into hierarchical language; automatic labeling cost about $900, with manual spot checks (Appendix 6.1).
- Baselines: token-action ablation VLM2VLA-AT and standard VLA comparisons; tasks include in-distribution pick/place, multilingual instructions, and open-world “Ash Ketchum” semantic grounding (Sec. 4.2, App. 8).
- Main Results: in the “Item Above Ash Ketchum” task, VLM2VLA reaches 60% versus 30% for the token-action ablation; median action-generation cycle latency is 6.1 s (Sec. 4.2.2, 5.1).
- Ablation: action-as-language consistently beats token-action ablation; VLM2VLA-AT degrades on complex OOD tasks (Sec. 4.2.2).
- Failure Cases: verifier could not reliably perform subtask-completion verification; without action chunk post-processing, predicted motions were often negligible (Appendix 6.2).
- Limitations: Author-stated — 6.1 s latency, translational-only control, coarse motion plans, and single-embodiment training (Sec. 5.1). Library Analysis — dexterous rotation and cross-embodiment transfer remain unvalidated.
- Remaining Gap / Idea: richer language labels for rotational/dexterous actions and faster decoding, grounded in the stated limitations.
- Evidence Sources: https://arxiv.org/abs/2509.22195 ; https://openreview.net/pdf/cf9593931d94a949b766ab027d77762088dc056c.pdf ; PDF/HTML Sections 3–5, Appendix 6.1–6.3, 8.
- Evidence Upgrade Status: A-Upgraded

## Citation Relations

### References in Library

- [[02_Papers/01_VLA/3D-VLA|3D-VLA]] — [arXiv full-text bibliography item 20](https://arxiv.org/html/2509.22195#bib.bib20)
- [[02_Papers/01_VLA/CoT-VLA|CoT-VLA]] — [arXiv full-text bibliography item 32](https://arxiv.org/html/2509.22195#bib.bib32)
- [[02_Papers/01_VLA/Octo|Octo]] — [arXiv full-text bibliography item 25](https://arxiv.org/html/2509.22195#bib.bib25)
- [[02_Papers/01_VLA/OpenVLA|OpenVLA]] — [arXiv full-text bibliography item 4](https://arxiv.org/html/2509.22195#bib.bib4)
- [[02_Papers/01_VLA/SayCan|SayCan]] — [arXiv full-text bibliography item 33](https://arxiv.org/html/2509.22195#bib.bib33)
- [[02_Papers/07_Generalization_LongHorizon/HAMSTER|HAMSTER]] — [arXiv full-text bibliography item 41](https://arxiv.org/html/2509.22195#bib.bib41)
- [[02_Papers/10_Benchmark_Dataset/DROID|DROID]] — [arXiv full-text bibliography item 49](https://arxiv.org/html/2509.22195#bib.bib49)
- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open_X-Embodiment]] — [arXiv full-text bibliography item 10](https://arxiv.org/html/2509.22195#bib.bib10)

### Cited By in Library

- [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI|A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]] — [arXiv full-text bibliography item 776](https://arxiv.org/html/2405.14093#bib.bib776)

### Related Work

- No curated content relation yet.
