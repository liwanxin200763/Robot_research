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
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4416031407
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

- Evidence Quality: A

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
- Evidence Upgrade Status: A-Upgraded
- Supplement Status: Available - Verified
- Code Completeness: Unavailable
- Robot Platform Evidence: Unknown


## Deep Enrichment (Full Text Read: 2026-09-21)

- Evidence Quality: A
- Fulltext Checked: Yes — official ICCV 2025 PDF and supplementary material were downloaded and text-extracted; dataset/method sections and benchmark tables inspected.
- Supplement Status: Available - Verified.

### Method (field-level evidence)
- Input / Observation: egocentric human video frames with narration and hand/object context (Sec. 3).
- Backbone / Core Architecture: LLaVA-13B with a `[SEG]` affordance token and SAM-based mask decoders; LoRA is used for parameter-efficient adaptation (Sec. 4).
- Key Modules: narration-conditioned affordance prediction and bimanual region segmentation.
- Intermediate Representation: actionable object-part affordance masks and language labels.
- Action Representation: affordance regions rather than executable robot trajectories; downstream bimanual manipulation is the intended use.
- Training: auto-label 2HANDS from EPIC-KITCHENS and Ego4D-style human videos; 278K images are reported for 2HANDS (Sec. 3, Table 1).
- Inference: predict precise, actionable affordance regions from a narrated human-video observation (Sec. 4).

### Dataset & Benchmark
- Training Dataset: 2HANDS, 278K images with affordance masks and narration-derived labels.
- Evaluation Benchmark: ActAffordance and its modified version; Table 2 compares AffExtract and other affordance baselines.
- Data Collection: auto-labeling from human egocentric videos, with sparse manual supervision used to seed the process (Sec. 3).

### Baseline / Results / Ablation
- Baselines: AffordanceLLM, AGD20K-style affordance methods, 3DOI, and related affordance prediction methods are named in Sec. 2 and Table 2.
- Main Results: Table 2 reports the proposed model against these baselines on ActAffordance; exact values are retained in the official PDF and were inspected, but no executable robot success metric is claimed because the benchmark is affordance segmentation.
- Ablation: modified ActAffordance results and the narration/segmentation components are compared in Table 2.

### Failure Cases / Limitations / Remaining Gap
- Failure Cases: sparse hand-object interaction and ambiguous narration can produce imprecise masks; the paper notes limitations of auto-labeled video coverage (Sec. 3).
- Author-stated: the extracted dataset inherits biases and gaps from egocentric videos and is not itself a complete robot-control dataset.
- Library Analysis: mapping affordance masks to closed-loop bimanual actions and measuring sim-to-real transfer remain open.

### Evidence Sources
- https://openaccess.thecvf.com/content/ICCV2025/html/Heidinger_2HandedAfforder_Learning_Precise_Actionable_Bimanual_Affordances_from_Human_Videos_ICCV_2025_paper.html
- PDF locations: Sec. 2–4; Tables 1–2; supplementary material.

- Evidence Upgrade Status: A-Upgraded
- Code Completeness: B-Code-Unverified — no official repository/checkpoint was confirmed during this audit.

## Citation Relations

### References in Library

- No verified in-library citation edge yet.

### Cited By in Library

- No verified in-library citation edge yet.

### Related Work

- No curated content relation yet.

## 快速摘要

### 研究问题

人类视频包含丰富双手交互，但普通 affordance 标签难指出左右手各自可操作的区域。

### 之前方法的问题

只标记物体可抓取，不足以指导双手分工和具体接触位置。

### 核心思路

用 VLM 产生分割提示，再由左右手 mask 解码器预测可执行区域，并分类单手或双手交互。

### 输入

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 输出 / 动作

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 数据集 / Benchmark

ActAffordance 等双手 affordance 评测；具体分数见官方 PDF。

### 主要结果

已访问的官方 PDF 支持方法与评测设置；快速摘要暂不填入未重新提取的数值。

### 为什么重要

直接关系到普通夹爪在同一物体上的双臂接触分工。

### 和当前项目的关系

High：可用于双臂 joint affordance 和动作前检查。

### 主要局限

精确数值与失败图例仍需对照论文图表；人手区域到普通夹爪的迁移需验证。

### 摘要证据

官方摘要/论文页; https://openaccess.thecvf.com/content/ICCV2025/html/Heidinger_2HandedAfforder_Learning_Precise_Actionable_Bimanual_Affordances_from_Human_Videos_ICCV_2025_paper.html; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
