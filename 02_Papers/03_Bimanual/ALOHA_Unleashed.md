# ALOHA Unleashed: A Simple Recipe for Robot Dexterity

## Basic Information（基本信息）

- Title: ALOHA Unleashed: A Simple Recipe for Robot Dexterity
- Year: 2024
- Venue / Source: CoRL
- Publication Status: Formal CoRL 2024; PMLR v270 online 2025
- CCF Level: Not CCF A (robotics venue extension; CCF row not asserted)
- Type: Method Paper
- Category: Bimanual Manipulation / Dexterous Manipulation / Dexterous Hand / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation
- Subcategory: Bimanual; Dexterous Hand / Dexterous Manipulation
- Priority: P0

## Classification

- Primary Category: Bimanual
- Categories: Robot Manipulation; Bimanual; Dexterous; Diffusion / Flow / IL / RL
- Subcategories: Bimanual; Dexterous Hand / Dexterous Manipulation
- Tags: Unknown

## Links（链接）

- Official Paper: https://proceedings.mlr.press/v270/zhao25b.html
- arXiv: 待补充
- Project Page: 待补充
- Official GitHub: 待补充

## Code（代码状态）

- Code Status: Unknown
- Checkpoint: 待补充
- Dataset Released: Unknown

## Embodiment（机器人形态）

- Single Arm / Bimanual / Dexterous Hand / Gripper: Bimanual / Parallel Gripper
- Real Robot: Mixed

## Why Collected（为什么被收录）

Conference year is 2024; PMLR v270 published online in Jan 2025.

## Verification（待核验）

- [x] Venue 已确认
- [ ] CCF 等级已确认
- [x] Official Paper 已确认
- [ ] Official GitHub 已确认
- [ ] Code 可运行性已确认
- [x] 是否真机已确认

## Citation Metrics

- Citation Count: 2
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4403579180
- OpenAlex Work: https://openalex.org/W4403579180

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

## Full-paper Enrichment (Batch 07)

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
https://proceedings.mlr.press/v270/zhao25b.html

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Fulltext-Unavailable
- Supplement Status: Not Found
- Code Completeness: Unknown
- Robot Platform Evidence: Unknown

## Deep Enrichment (Full Text Read: 2026-09-22)
- Evidence Quality: A
- Fulltext Checked: Yes — arXiv HTML 2410.13126, Secs. 1–4 and Appendices A–C inspected.
- Supplement Status: Available - Verified.
- Method: ALOHA 2 bimanual parallel-jaw platform; ResNet50 multi-view encoder + 85M/55M Transformer encoder-decoder with diffusion loss, 50-step denoising and 50-action chunks (Sec. 3.1).
- Dataset / Setup: over 26K real demonstrations for 5 tasks and over 2K simulated demonstrations for 3 tasks; 4 RGB views, proprioception, 14-DoF action (Secs. 1, 3.2).
- Results: five real tasks and three simulation tasks; forward pass 0.043 s on RTX 4090 and target frequency above 50Hz (Sec. 3.1). Diffusion policy outperforms non-diffusion baselines on difficult deformable/contact-rich tasks (Sec. 4).
- Ablation: small/base model, data scale, architecture and OOD robustness are analyzed (Sec. 4.3, App. A).
- Failure Cases / Limitations: non-diffusion policies fail some tasks; long-horizon deformable manipulation remains sensitive to data coverage and distribution shift (Secs. 4–5).
- Remaining Gap / Idea: combine this ordinary-gripper bimanual recipe with VLA grounding and recovery signals.
- Evidence Sources: https://arxiv.org/html/2410.13126 ; https://aloha-unleashed.github.io/ ; https://github.com/tonyzhaozh/aloha.
- Evidence Upgrade Status: A-Upgraded

## Citation Relations

### References in Library

- [[02_Papers/08_Data_Teleoperation/DexCap|DexCap]] — [arXiv full-text bibliography item 44](https://arxiv.org/html/2410.13126#bib.bib44)
- [[02_Papers/10_Benchmark_Dataset/DROID|DROID]] — [arXiv full-text bibliography item 36](https://arxiv.org/html/2410.13126#bib.bib36)
- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open_X-Embodiment]] — [arXiv full-text bibliography item 45](https://arxiv.org/html/2410.13126#bib.bib45)

### Cited By in Library

- [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]] — [arXiv full-text bibliography item 68](https://arxiv.org/html/2412.03293#bib.bib68)
- [[02_Papers/03_Bimanual/COMBO-Grasp|COMBO-Grasp]] — [arXiv full-text bibliography item 45](https://arxiv.org/html/2502.08054#bib.bib45)

### Related Work

- No curated content relation yet.
