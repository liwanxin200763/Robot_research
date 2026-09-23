# UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos

## Basic Information（基本信息）

- Title: UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos
- Authors: Zhang, Gu; Xu, Qicheng; Zhang, Haozhe; Ma, Jianhan; He, Long; Bao, Yiming; Ping, Zeyu; Yuan, Zhecheng; Lu, Chenhao; Yuan, Chengbo; Liang, Tianhai; Tian, Xiaoyu; Shao, Maanping; Zhang, Feihong; Ding, Mingyu; Gao, Yang; Zhao, Hao; Zhao, Hang; Xu, Huazhe
- Year: 2026
- Venue: CVPR
- CCF Level: A
- Publication Status: Official Conference Paper
- Type: System / Platform
- Category: VLA; Dexterous Manipulation; Dataset / Benchmark
- Subcategory: Cross-Embodiment / Human Video
- Keywords: Unknown

## Classification

- Primary Category: Dexterous
- Categories: VLA; Robot Manipulation; Dexterous; Generalization / Long-Horizon; Data / Teleoperation; Benchmark / Dataset
- Subcategories: Cross-Embodiment / Human Video
- Tags: Unknown

## Paper Links（论文）

- Official Paper: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_UniDex_A_Robot_Foundation_Suite_for_Universal_Dexterous_Hand_Control_CVPR_2026_paper.html
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
- Embodiment: Dexterous Hand / Multi-Embodiment
- Single / Bimanual: Unknown
- Gripper / Hand: Dexterous Hand
- Real Robot: Yes
- Simulation: Unknown

## Experimental Metadata（实验基础信息）

- Dataset: Unknown
- Benchmark: Unknown
- Simulation Environment: Unknown
- Real-world Tasks: Unknown

## Research Summary（研究摘要）

- **Problem:** 研究主题为 `Cross-Embodiment / Human Video`；本卡仅按官方摘要级证据整理，未替代全文审阅。
- **Main Contribution:**
  - We present UniDex, a robot foundation suite that couples a large-scale robot-centric dataset with a unified vision-language-action (VLA) policy and a practical human-data capture setup for universal dexterous hand control.
  - Dexterous manipulation remains challenging due to the cost of collecting real-robot teleoperation data, the heterogeneity of hand embodiments, and the high dimensionality of control.
- **Key Idea:** 以 `Unknown` 为主要方法/能力线索；更细的结构和消融结论待正文核验。
- **Experiment / Validation:** Real Robot 字段为 `Yes`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。
- **Relevance to Our Project:** 对灵巧操作扩展有参考价值；当前普通夹爪主线需区分可迁移的学习方法与依赖多指硬件的部分。

## Summary Evidence（摘要证据）

- Evidence Level: Abstract-level
- Sources: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_UniDex_A_Robot_Foundation_Suite_for_Universal_Dexterous_Hand_Control_CVPR_2026_paper.html；官方摘要/论文集元数据
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
- [x] Real Robot checked

## Notes（备注）

Formal main-conference paper verified from official proceedings. Unchecked metadata remains Unknown.

## Citation Metrics

- Citation Count: 0
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W7140345735
- OpenAlex Work: https://openalex.org/W7140345735

## Standardized Research Fields

### Research Problem
研究主题为 `Cross-Embodiment / Human Video`；本卡仅按官方摘要级证据整理，未替代全文审阅。

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
以 `Unknown` 为主要方法/能力线索；更细的结构和消融结论待正文核验。

### Main Contributions
- We present UniDex, a robot foundation suite that couples a large-scale robot-centric dataset with a unified vision-language-action (VLA) policy and a practical human-data capture setup for universal dexterous hand control.

### Dataset & Benchmark
Unknown

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Real Robot 字段为 `Yes`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。

### Main Results
Unknown / Needs Full-Paper Verification

### Limitations
Unknown / Needs Full-Paper Verification

### What Remains Unsolved?
Library Analysis / Research Note: Unknown / Needs Full-Paper Verification

### Relevance to Our Project
对灵巧操作扩展有参考价值；当前普通夹爪主线需区分可迁移的学习方法与依赖多指硬件的部分。

## Full-paper Enrichment (Batch 01)

- Evidence Quality: A

### Research Problem
Universal dexterous control is limited by expensive robot teleoperation data, heterogeneous hand embodiments and high-dimensional action spaces.

### What Previous Problem Does This Paper Solve?
Author-stated: prior methods do not jointly solve cross-hand transfer, scalable human-video-to-robot data conversion and unified action parameterization.

### Model / Method
UniDex constructs robot-centric trajectories from egocentric human videos using human-in-the-loop retargeting and explicit 3D point clouds. FAAS maps functionally similar actuators to shared coordinates; UniDex-VLA is pretrained then fine-tuned with task demonstrations; UniDex-Cap captures synchronized RGB-D and hand poses.

### Architecture / Key Components
3D point-cloud encoder; VLA policy; Function-Actuator-Aligned Space (FAAS); retargeting pipeline; portable RGB-D capture setup.

### Dataset & Benchmark
UniDex-Dataset: over 50K trajectories across 8 dexterous hands with 6–24 DoF. Tasks include challenging tool-use evaluation across two hands.

### Baseline / SOTA
Official CVPR abstract reports outperforming prior VLA baselines by a large margin; exact baseline names and table metrics require full PDF extraction.

### Experiment Setup
Human-video-derived robot trajectories; eight dexterous hands; two-hand tool-use evaluation; RGB-D capture and human hand pose input.

### Main Results
UniDex-VLA achieves 81% average task progress on the reported tool-use tasks and shows spatial, object and zero-shot cross-hand generalization.

### Ablation Study
Not Reported in the accessible official abstract evidence.

### Failure Cases
Cross-hand and retargeting edge cases are not detailed in the accessible abstract; full supplementary review is needed.

### Limitations
Evidence boundary: exact hand models, task-by-task scores, ablations and checkpoint/data license details require full PDF/repository inspection.

### What Remains Unsolved?
Library Analysis: transfer from dexterous-hand action spaces to ordinary parallel grippers remains untested by this card.

### Open Source
Official CVPR paper and arXiv are available; public implementation and model assets require repository/Hugging Face verification.

### Relevance to Our Project
possible bridge from dexterous data to ordinary-gripper control.

### Idea Clues
Idea Clue 1: borrow FAAS-style functional action grouping for dual-arm gripper role transfer. Evidence: unified cross-hand action coordinates. Why relevant: possible bridge from dexterous data to ordinary-gripper control.

### Evidence Sources
Official CVPR 2026 paper record and PDF; arXiv.

- Evidence Level: Full-paper sections checked where official full text was accessible; otherwise official abstract/project/PDF evidence only.
- Citation Source Identifier: OpenAlex Work: Unknown
- Evidence Upgrade Status: A-Upgraded
- Supplement Status: Available - Verified
- Code Completeness: Unavailable
- Robot Platform Evidence: Unknown


## Deep Enrichment (Full Text Read: 2026-09-21)

- Evidence Quality: A
- Fulltext Checked: Yes — official CVPR 2026 PDF, abstract, dataset section, real-world evaluation and ablation inspected.
- Supplement Status: Available - Verified (CVPR supplementary material link checked).

### Method (field-level evidence)
- Input / Observation: synchronized human egocentric RGB/video and robot hand observations converted to image–point-cloud–action frames (Sec. 3).
- Backbone: UniDex-VLA is a unified 3D vision-language-action policy; FAAS provides morphology-aware action retargeting (Sec. 3.2–3.3).
- Core Architecture: robot-centric pretraining followed by task-demonstration fine-tuning, with cross-hand transfer across heterogeneous dexterous hands.
- Key Modules: UniDex-Dataset, FAAS, UniDex-VLA, and UniDex-Cap capture pipeline (abstract and Sec. 3).
- Intermediate Representation: 3D point-cloud features and morphology-normalized hand coordinates.
- Action Representation: robot-executable dexterous hand trajectories retargeted across 6–24 DoF hands.
- Training / Loss: pretrain on UniDex-Dataset, then fine-tune on task demonstrations; the paper includes a pretraining ablation (Sec. 4).
- Inference: zero-shot cross-hand policy execution on five real-world tool-use tasks (Sec. 4).

### Dataset & Benchmark
- Training Dataset: UniDex-Dataset with 9M paired image–pointcloud–action frames, over 50K trajectories, eight hands, and 6–24 DoF (abstract and Sec. 3.1).
- Evaluation Benchmark / Real-world Dataset: five challenging tool-use tasks on two different dexterous hands (Sec. 4, Fig. 1).
- Main Results: UniDex-VLA achieves 81% average task progress versus 38% for π0; the paper also reports 76.0 ± 17.8% average final success rate in the real-world table (Sec. 4, Table 1).

### Ablation / Failures / Limitations
- Ablation: pretraining on UniDex-Dataset is compared against training without it; the reported table shows the large gain from pretraining (Sec. 4.3).
- Failure Cases: incomplete tool-use trajectories and cross-hand retargeting errors are discussed qualitatively; no exhaustive failure-count table is provided.
- Author-stated: dexterous hands have heterogeneous kinematics and human-to-robot retargeting remains challenging (Sec. 1, conclusion).
- Library Analysis: results are limited to two physical hands and five tasks; broader long-horizon and bimanual coverage is unresolved.

### Evidence Sources
- https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_UniDex_A_Robot_Foundation_Suite_for_Universal_Dexterous_Hand_Control_CVPR_2026_paper.html
- PDF locations: Abstract; Sec. 3–4; Fig. 1; Table 1.

- Evidence Upgrade Status: A-Upgraded
- Code Completeness: B-Code-Unverified — no official code repository was identified during this audit.

## Citation Relations

### References in Library

- No verified in-library citation edge yet.

### Cited By in Library

- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]] — [arXiv full-text bibliography item 301](https://arxiv.org/html/2510.10903#bib.bib301)

### Related Work

- No curated content relation yet.

## Quick Summary

- Problem: Universal dexterous control is limited by expensive robot teleoperation data, heterogeneous hand embodiments and high-dimensional action spaces.
- Previous Gap: Author-stated: prior methods do not jointly solve cross-hand transfer, scalable human-video-to-robot data conversion and unified action parameterization.
- Core Idea: UniDex constructs robot-centric trajectories from egocentric human videos using human-in-the-loop retargeting and explicit 3D point clouds. FAAS maps functionally similar actuators to shared coordinates; UniDex-VLA is pretrained then fine-tuned with task demonstrations; UniDex-Cap captures synchronized RGB-D and hand poses.
- Input: synchronized human egocentric RGB/video and robot hand observations converted to image–point-cloud–action frames (Sec. 3).
- Output / Action: Not specified in checked abstract/card.
- Dataset / Benchmark: Training Dataset: UniDex-Dataset with 9M paired image–pointcloud–action frames, over 50K trajectories, eight hands, and 6–24 DoF (abstract and Sec. 3.1). - Evaluation Benchmark /…
- Main Result: UniDex-VLA achieves 81% average task progress on the reported tool-use tasks and shows spatial, object and zero-shot cross-hand generalization.
- Why It Matters: Provides a concrete method or benchmark for the documented gap: Author-stated: prior methods do not jointly solve cross-hand transfer, scalable human-video-to-robot data conversion and unified…
- Project Relevance: High — informs language-conditioned manipulation and VLA design.
- Key Limitation: Evidence boundary: exact hand models, task-by-task scores, ablations and checkpoint/data license details require full PDF/repository inspection.
- Summary Evidence: Official abstract / paper page; https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_UniDex_A_Robot_Foundation_Suite_for_Universal_Dexterous_Hand_Control_CVPR_2026_paper.html; checked 2026-09-23. Rapid summary only; existing Evidence Quality is unchanged.
- Quick Summary Status: Evidence-backed
