# AnyBimanual: Transferring Unimanual Policy for General Bimanual Manipulation

## Basic Information（基本信息）

- Title: AnyBimanual: Transferring Unimanual Policy for General Bimanual Manipulation
- Authors: Lu, Guanxing; Yu, Tengbo; Deng, Haoyuan; Chen, Season Si; Tang, Yansong; Wang, Ziwei
- Year: 2025
- Venue: ICCV
- CCF Level: A
- Publication Status: Official Conference Paper
- Type: Method Paper
- Category: Bimanual Manipulation; Imitation Learning
- Subcategory: Policy Transfer / Generalization
- Keywords: Unknown

## Classification

- Primary Category: Bimanual
- Categories: Robot Manipulation; Bimanual; Diffusion / Flow / IL / RL; Generalization / Long-Horizon
- Subcategories: Policy Transfer / Generalization
- Tags: Unknown

## Paper Links（论文）

- Official Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Lu_AnyBimanual_Transferring_Unimanual_Policy_for_General_Bimanual_Manipulation_ICCV_2025_paper.html
- DOI: Unknown
- arXiv: Unknown
- Project Page: Unknown

## Code & Resources（代码与资源）

- Official GitHub: Unknown
- Code Status: Unknown
- Hugging Face: Unknown
- ModelScope: Unknown
- Checkpoint / Weights: Unknown
- Dataset: Unknown
- Demo: Unknown
- Evaluation: Unknown
- Documentation: Unknown
- Other Official Resources: Unknown

## Robot / Embodiment（机器人与形态）

- Robot Platform: Unknown
- Embodiment: Bimanual / Parallel Gripper
- Single / Bimanual: Bimanual
- Gripper / Hand: Parallel Gripper
- Real Robot: Unknown
- Simulation: Unknown

## Experimental Metadata（实验基础信息）

- Dataset: Unknown
- Benchmark: Unknown
- Simulation Environment: Unknown
- Real-world Tasks: Unknown

## Research Summary（研究摘要）

- **Problem:** 研究主题为 `Policy Transfer / Generalization`；本卡仅按官方摘要级证据整理，未替代全文审阅。
- **Main Contribution:**
  - We propose a plug-and-play method named AnyBimanual, which transfers pretrained unimanual policy to general bimanual manipulation policy with few bimanual demonstrations.
  - Experiments on 9 real-world tasks further verify its practicality with an average success rate of 84.62%.
- **Key Idea:** 以 `Unknown` 为主要方法/能力线索；更细的结构和消融结论待正文核验。
- **Experiment / Validation:** Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。
- **Relevance to Our Project:** 与 NERO 双臂、普通夹爪、示范采集和双臂策略学习直接相关，优先评估动作表示与协同控制是否可迁移。

## Summary Evidence（摘要证据）

- Evidence Level: Abstract-level
- Sources: https://openaccess.thecvf.com/content/ICCV2025/html/Lu_AnyBimanual_Transferring_Unimanual_Policy_for_General_Bimanual_Manipulation_ICCV_2025_paper.html；官方摘要/论文集元数据
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping
- Verified Date: 2026-09-19
- Evidence Boundary: 未核实的机器人平台、数据集、代码可运行性和真机细节保持 Unknown。

## Verification（核验）

- [x] Venue confirmed
- [x] Full / Regular Paper confirmed
- [x] CCF A confirmed
- [x] Official Paper confirmed
- [ ] Project Page checked
- [ ] Official GitHub checked
- [ ] Code Status checked
- [ ] Checkpoint checked
- [ ] Dataset checked
- [ ] Robot Platform checked
- [ ] Real Robot checked

## Notes（备注）

Formal main-conference paper verified from official proceedings. Unchecked metadata remains Unknown.

## Citation Metrics

- Citation Count: 0
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4405254485
- OpenAlex Work: https://openalex.org/W4405254485

## Standardized Research Fields

### Research Problem
研究主题为 `Policy Transfer / Generalization`；本卡仅按官方摘要级证据整理，未替代全文审阅。

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
以 `Unknown` 为主要方法/能力线索；更细的结构和消融结论待正文核验。

### Main Contributions
- We propose a plug-and-play method named AnyBimanual, which transfers pretrained unimanual policy to general bimanual manipulation policy with few bimanual demonstrations.

### Dataset & Benchmark
Unknown

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。

### Main Results
Unknown / Needs Full-Paper Verification

### Limitations
Unknown / Needs Full-Paper Verification

### What Remains Unsolved?
Library Analysis / Research Note: Unknown / Needs Full-Paper Verification

### Relevance to Our Project
与 NERO 双臂、普通夹爪、示范采集和双臂策略学习直接相关，优先评估动作表示与协同控制是否可迁移。

## Full-paper Enrichment (Batch 01)

- Evidence Quality: A

### Research Problem
General language-conditioned bimanual manipulation requires expensive bimanual demonstrations and faces a high-dimensional action space.

### What Previous Problem Does This Paper Solve?
Author-stated: fixed cooperation patterns and hand-designed atomic movements do not generalize across diverse bimanual tasks; unimanual policies contain reusable manipulation knowledge but observe a different workspace.

### Model / Method
AnyBimanual is a model-agnostic plug-and-play transfer module. A skill manager schedules skill primitives with task-oriented compensation; a voxel/visual aligner creates spatial soft masks so each arm sees inputs aligned with unimanual pretraining.

### Architecture / Key Components
Pretrained unimanual policy; skill manager; skill primitives; task-oriented compensation; voxel visual aligner; bimanual policy wrapper.

### Dataset & Benchmark
Evaluation uses 12 simulated RLBench2 tasks and 9 real-world tasks. Training uses few bimanual demonstrations; exact count is not stated in the abstract evidence.

### Baseline / SOTA
Compared with prior bimanual manipulation methods on RLBench2 and real-world tasks; the abstract reports superiority over previous methods without naming every baseline.

### Experiment Setup
Simulation: 12 RLBench2 tasks. Real robot: 9 tasks. Bimanual manipulation with language-conditioned instructions; exact hardware and cameras require full paper details.

### Main Results
12 simulated tasks: 12.67% success-rate improvement over previous methods. 9 real-world tasks: average success rate 84.62%.

### Ablation Study
The accessible arXiv text describes the separate skill-manager and visual-aligner contributions; full ablation numbers were not re-extracted in this batch.

### Failure Cases
The paper identifies observation discrepancy between unimanual and bimanual systems as a transfer risk; detailed failure cases require appendix extraction.

### Limitations
Author-stated / evidence boundary: few-shot transfer still depends on bimanual demonstrations and the transfer assumes reusable unimanual policy representations.

### What Remains Unsolved?
Library Analysis: transfer under substantially different grippers, camera layouts and contact-rich coordination remains an open validation target.

### Open Source
Official project provides arXiv PDF, project website and GitHub link; code/checkpoint contents require repository-level follow-up.

### Relevance to Our Project
directly matches current bimanual project.

### Idea Clues
Idea Clue 1: use AnyBimanual as a baseline for ordinary-gripper dual-arm transfer with controlled demonstration budgets. Evidence: 12 RLBench2 + 9 real tasks and limited bimanual demonstrations. Why relevant: directly matches current bimanual project.

### Evidence Sources
Official ICCV 2025 record; author project page; arXiv full text; official GitHub link.

- Evidence Level: Full-paper sections checked where official full text was accessible; otherwise official abstract/project/PDF evidence only.
- Citation Source Identifier: OpenAlex Work: https://openalex.org/W4405254485
- Evidence Upgrade Status: A-Upgraded
- Supplement Status: Available - Verified
- Code Completeness: Unavailable
- Robot Platform Evidence: Unknown


## Deep Enrichment (Full Text Read: 2026-09-21)
- Evidence Quality: A
- Fulltext Checked: Yes — arXiv 2412.06779 and ICCV 2025 record inspected.
- Supplement Status: Available - Verified.
- Method / Architecture: skill manager decomposes tasks and a visual/voxel aligner transfers a unimanual policy to bimanual execution (paper Sec. 3–4).
- Dataset & Benchmark: 12 simulated RLBench2 tasks and 9 real-world tasks (abstract and experiments).
- Main Results: +12.67% success improvement over previous methods in simulation; 84.62% average success over the nine real-world tasks.
- Ablation / Failure Cases: component ablations isolate skill-manager and visual-aligner contributions; failures are associated with cross-arm alignment and visual correspondence under novel object/pose configurations.
- Limitations / Gap: transfer beyond the reported embodiments and broader long-horizon bimanual coverage remain open.
- Evidence Sources: https://arxiv.org/abs/2412.06779 ; https://github.com/Tengbo-Yu/AnyBimanual ; ICCV 2025 official record. PDF locations: abstract; Sec. 3–5; experiments/ablation tables.
- Evidence Upgrade Status: A-Upgraded

## Citation Relations

### References in Library

- [[02_Papers/01_VLA/Octo|Octo]] — [arXiv full-text bibliography item 51](https://arxiv.org/html/2412.06779#bib.bib51)
- [[02_Papers/01_VLA/OpenVLA|OpenVLA]] — [arXiv full-text bibliography item 41](https://arxiv.org/html/2412.06779#bib.bib41)
- [[02_Papers/03_Bimanual/RDT-1B|RDT-1B]] — [arXiv full-text bibliography item 46](https://arxiv.org/html/2412.06779#bib.bib46)
- [[02_Papers/03_Bimanual/VoxAct-B|VoxAct-B]] — [arXiv full-text bibliography item 45](https://arxiv.org/html/2412.06779#bib.bib45)
- [[02_Papers/06_Diffusion_Flow_IL_RL/3D_Diffuser_Actor|3D_Diffuser_Actor]] — [arXiv full-text bibliography item 39](https://arxiv.org/html/2412.06779#bib.bib39)
- [[02_Papers/08_Data_Teleoperation/DexCap|DexCap]] — [arXiv full-text bibliography item 56](https://arxiv.org/html/2412.06779#bib.bib56)
- [[02_Papers/10_Benchmark_Dataset/DROID|DROID]] — [arXiv full-text bibliography item 40](https://arxiv.org/html/2412.06779#bib.bib40)
- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open_X-Embodiment]] — [arXiv full-text bibliography item 17](https://arxiv.org/html/2412.06779#bib.bib17)

### Cited By in Library

- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]] — [arXiv full-text bibliography item 1270](https://arxiv.org/html/2510.10903#bib.bib1270)

### Related Work

- No curated content relation yet.

## Quick Summary

- Problem: General language-conditioned bimanual manipulation requires expensive bimanual demonstrations and faces a high-dimensional action space.
- Previous Gap: Author-stated: fixed cooperation patterns and hand-designed atomic movements do not generalize across diverse bimanual tasks; unimanual policies contain reusable manipulation knowledge but observe a different workspace.
- Core Idea: AnyBimanual is a model-agnostic plug-and-play transfer module. A skill manager schedules skill primitives with task-oriented compensation; a voxel/visual aligner creates spatial soft masks so each arm sees inputs aligned with unimanual pretraining.
- Input: Not specified in checked abstract/card.
- Output / Action: Not specified in checked abstract/card.
- Dataset / Benchmark: Evaluation uses 12 simulated RLBench2 tasks and 9 real-world tasks. Training uses few bimanual demonstrations; exact count is not stated in the abstract evidence.
- Main Result: 12 simulated tasks: 12.67% success-rate improvement over previous methods. 9 real-world tasks: average success rate 84.62%.
- Why It Matters: Provides a concrete method or benchmark for the documented gap: Author-stated: fixed cooperation patterns and hand-designed atomic movements do not generalize across diverse bimanual tasks…
- Project Relevance: High — directly informs dual-arm coordination, data or ordinary-gripper policy design.
- Key Limitation: Author-stated / evidence boundary: few-shot transfer still depends on bimanual demonstrations and the transfer assumes reusable unimanual policy representations.
- Summary Evidence: Official abstract / paper page; https://arxiv.org/html/2412.06779; checked 2026-09-23. Rapid summary only; existing Evidence Quality is unchanged.
- Quick Summary Status: Evidence-backed
