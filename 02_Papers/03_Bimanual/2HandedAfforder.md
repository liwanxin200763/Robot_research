# 2HandedAfforder: Learning Precise Actionable Bimanual Affordances from Human Videos

## Basic Information（基本信息）

- Title: 2HandedAfforder: Learning Precise Actionable Bimanual Affordances from Human Videos
- Authors: Heidinger, Marvin; Jauhri, Snehal; Prasad, Vignesh; Chalvatzaki, Georgia
- Year: 2025
- Venue: ICCV
- CCF Level: A
- Publication Status: Official Conference Paper
- Type: Method Paper
- Category: Bimanual Manipulation; Robot Manipulation
- Subcategory: Human Video / Affordance
- Keywords: Unknown

## Classification

- Primary Category: Bimanual
- Categories: Robot Manipulation; Bimanual; Data / Teleoperation
- Subcategories: Human Video / Affordance
- Tags: Unknown

## Paper Links（论文）

- Official Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Heidinger_2HandedAfforder_Learning_Precise_Actionable_Bimanual_Affordances_from_Human_Videos_ICCV_2025_paper.html
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
- Real Robot: Yes
- Simulation: Unknown

## Experimental Metadata（实验基础信息）

- Dataset: Unknown
- Benchmark: Unknown
- Simulation Environment: Unknown
- Real-world Tasks: Unknown

## Research Summary（研究摘要）

- **Problem:** 研究主题为 `Human Video / Affordance`；本卡仅按官方摘要级证据整理，未替代全文审阅。
- **Main Contribution:**
  - In this work, we propose a framework for extracting affordance data from human activity video datasets.
  - Finally, we show that our predicted affordance regions are actionable, i.e., can be used by an agent performing a task, through demonstration in robotic manipulation scenarios.
- **Key Idea:** 以 `Unknown` 为主要方法/能力线索；更细的结构和消融结论待正文核验。
- **Experiment / Validation:** Real Robot 字段为 `Yes`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。
- **Relevance to Our Project:** 与 NERO 双臂、普通夹爪、示范采集和双臂策略学习直接相关，优先评估动作表示与协同控制是否可迁移。

## Summary Evidence（摘要证据）

- Evidence Level: Abstract-level
- Sources: https://openaccess.thecvf.com/content/ICCV2025/html/Heidinger_2HandedAfforder_Learning_Precise_Actionable_Bimanual_Affordances_from_Human_Videos_ICCV_2025_paper.html；官方摘要/论文集元数据
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
- Citation Checked Date: 2026-09-21
- OpenAlex Work: https://openalex.org/W4416031407

## Standardized Research Fields

### Research Problem
研究主题为 `Human Video / Affordance`；本卡仅按官方摘要级证据整理，未替代全文审阅。

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
以 `Unknown` 为主要方法/能力线索；更细的结构和消融结论待正文核验。

### Main Contributions
- In this work, we propose a framework for extracting affordance data from human activity video datasets.

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
与 NERO 双臂、普通夹爪、示范采集和双臂策略学习直接相关，优先评估动作表示与协同控制是否可迁移。

## Full-paper Enrichment (Batch 01)

- Evidence Quality: B

### Research Problem
Human videos contain rich bimanual interactions but generic affordance labels often lack precise, actionable regions for left/right/both-hand interaction.

### What Previous Problem Does This Paper Solve?
Author-stated: object-part labels do not necessarily identify the precise interaction region, and affordance prediction is multi-modal.

### Model / Method
A VLM emits a [SEG] token consumed by left/right SAM-based mask decoders and a hand-taxonomy classifier; LoRA adapts a LLaVA-13B while freezing the image encoder and most VLM parameters. A CLIP-based alternative is also trained.

### Architecture / Key Components
LLaVA-13B; [SEG] token; SAM mask decoders; taxonomy classifier; LoRA; dice + focal losses and cross-entropy.

### Dataset & Benchmark
2HANDS human-video data; ActAffordance benchmark has 400 activities from EPIC-KITCHENS and Ego4D with unimanual and bimanual masks; 10 human annotators label possible interaction regions.

### Baseline / SOTA
VLM-based model compared with 2HandedAfforder-CLIP; exact additional baselines and table values require full PDF extraction.

### Experiment Setup
In-the-wild human video images; cropped and uncropped ActAffordance evaluation; actionability is tested for downstream robotic manipulation.

### Main Results
The accessible official PDF evidence confirms ActAffordance and actionable-affordance evaluation; exact numerical scores were not re-extracted.

### Ablation Study
VLM-based versus CLIP-based affordance predictor is reported; exact ablation numbers require table extraction.

### Failure Cases
The paper notes ambiguity/multi-modality of valid interaction regions; exact failure examples require figure-level review.

### Limitations
Evidence boundary: real-robot transfer results and exact metrics require full PDF and supplementary extraction.

### What Remains Unsolved?
Library Analysis: converting human-video affordance masks into robust closed-loop dual-arm gripper actions remains open.

### Open Source
Official paper and supplementary are available through ICCV; repository/checkpoint status not confirmed.

### Relevance to Our Project
actionable perception before VLA action generation.

### Idea Clues
Idea Clue 1: evaluate predicted left/right/both affordances as a front-end for dual-arm task planning. Evidence: explicit hand-taxonomy decoder. Why relevant: actionable perception before VLA action generation.

### Evidence Sources
Official ICCV 2025 PDF and paper record.

- Evidence Level: Full-paper sections checked where official full text was accessible; otherwise official abstract/project/PDF evidence only.
- Citation Source Identifier: OpenAlex Work: Unknown
