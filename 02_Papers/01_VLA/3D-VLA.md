# 3D-VLA: A 3D Vision-Language-Action Generative World Model

## Basic Information（基本信息）

- Title: 3D-VLA: A 3D Vision-Language-Action Generative World Model
- Authors: Haoyu Zhen; Xiaowen Qiu; Peihao Chen; Jincheng Yang; Xin Yan; Yilun Du; Yining Hong; Chuang Gan
- Year: 2024
- Venue: ICML
- CCF Level: A
- Publication Status: Official Conference Paper
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Subcategory: VLA / Robot Foundation Models; Robot Manipulation / IL / Diffusion
- Keywords: VLA; World Model / 3D Generation

## Classification

- Primary Category: VLA
- Categories: VLA; Robot Manipulation; Diffusion / Flow / IL / RL
- Subcategories: VLA / Robot Foundation Models; Robot Manipulation / IL / Diffusion
- Tags: VLA; World Model / 3D Generation

## Paper Links（论文）

- Official Paper: https://proceedings.mlr.press/v235/zhen24a.html
- DOI: Unknown
- arXiv: 
- Project Page: https://vis-www.cs.umass.edu/3dvla/

## Code & Resources（代码与资源）

- Official GitHub: https://github.com/UMass-Embodied-AGI/3D-VLA
- Code Status: Partial
- Hugging Face: Unknown
- ModelScope: Unknown
- Checkpoint / Weights: https://huggingface.co/anyezhy/3dvla-diffusion ; https://huggingface.co/anyezhy/3dvla-diffusion-pointcloud（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: README及model card提供OpenX来源与数据说明；完整处理后数据待核实
- Demo: Unknown
- Evaluation: Unknown
- Documentation: Unknown
- Other Official Resources: Unknown

## Robot / Embodiment（机器人与形态）

- Robot Platform: Unknown
- Embodiment: Single Arm / Parallel Gripper
- Single / Bimanual: Single Arm
- Gripper / Hand: Parallel Gripper
- Real Robot: Unknown
- Simulation: Unknown

## Experimental Metadata（实验基础信息）

- Dataset: README及model card提供OpenX来源与数据说明；完整处理后数据待核实
- Benchmark: Unknown
- Simulation Environment: Unknown
- Real-world Tasks: Unknown

## Research Summary（研究摘要）

- **Problem:** 研究主题为 `VLA / Robot Foundation Models; Robot Manipulation / IL / Diffusion`；本卡仅按官方摘要级证据整理，未替代全文审阅。
- **Main Contribution:**
  - 3D-VLA: A 3D Vision-Language-Action Generative World ModelHaoyu Zhen, Xiaowen Qiu, Peihao Chen, Jincheng Yang, Xin Yan, Yilun Du,&nb...
  - 3D-VLA: A 3D Vision-Language-Action Generative World ModelHaoyu Zhen, Xiaowen Qiu, Peihao Chen, Jincheng Yang, Xin Yan, Yilun Du,&nb...
- **Key Idea:** 以 `VLA; World Model / 3D Generation` 为主要方法/能力线索；更细的结构和消融结论待正文核验。
- **Experiment / Validation:** Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。
- **Relevance to Our Project:** 可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

## Summary Evidence（摘要证据）

- Evidence Level: Abstract-level
- Sources: https://proceedings.mlr.press/v235/zhen24a.html；官方摘要/论文集元数据
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping
- Verified Date: 2026-09-19
- Evidence Boundary: 未核实的机器人平台、数据集、代码可运行性和真机细节保持 Unknown。

## Verification（核验）

- [x] Venue confirmed
- [x] Full / Regular Paper confirmed
- [x] CCF A confirmed
- [x] Official Paper confirmed
- [x] Project Page checked
- [x] Official GitHub checked
- [x] Code Status checked
- [x] Checkpoint checked
- [x] Dataset checked
- [ ] Robot Platform checked
- [ ] Real Robot checked

## Notes（备注）

公开目标图像/点云扩散训练与推理、LLM训练实现；未确认完整机器人策略评测链，保守标Partial，端到端可运行性待复核。 Static checks only; no cloning/running or download.

## Citation Metrics

- Citation Count: 14
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-21
- OpenAlex Work: https://openalex.org/W4392886475

## Standardized Research Fields

### Research Problem
研究主题为 `VLA / Robot Foundation Models; Robot Manipulation / IL / Diffusion`；本卡仅按官方摘要级证据整理，未替代全文审阅。

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
以 `VLA; World Model / 3D Generation` 为主要方法/能力线索；更细的结构和消融结论待正文核验。

### Main Contributions
- 3D-VLA: A 3D Vision-Language-Action Generative World ModelHaoyu Zhen, Xiaowen Qiu, Peihao Chen, Jincheng Yang, Xin Yan, Yilun Du,&nb...

### Dataset & Benchmark
README及model card提供OpenX来源与数据说明；完整处理后数据待核实

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
可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

## Full-paper Enrichment (Batch 01)

- Evidence Quality: B

### Research Problem
2D VLA policies lack explicit 3D physical-world structure and often map perception directly to actions without modeling future dynamics.

### What Previous Problem Does This Paper Solve?
Author-stated: existing VLA models underuse 3D relations and world dynamics for planning.

### Model / Method
3D-VLA builds on a 3D-based LLM, introduces action tokens, and aligns embodied diffusion models that predict goal images and point clouds with the language model for planning.

### Architecture / Key Components
3D LLM; action-token interface; embodied diffusion models; goal-image and point-cloud generation; 3D embodied instruction dataset.

### Dataset & Benchmark
Large-scale 3D embodied instruction dataset assembled from existing robotics datasets; evaluation is reported on held-in datasets. Exact dataset names and sizes require full paper tables.

### Baseline / SOTA
Official PMLR abstract only states held-in dataset improvement; named baselines and metrics require PDF extraction.

### Experiment Setup
Embodied environments with 3D perception, reasoning, generation and action planning; real-world application is discussed but the accessible proceedings page does not provide hardware details.

### Main Results
PMLR reports improved reasoning, multimodality generation and planning on held-in datasets; no numeric values are added from the abstract page alone.

### Ablation Study
Not Reported in the accessible proceedings page.

### Failure Cases
Not Explicitly Reported in the accessible proceedings page.

### Limitations
Evidence boundary: exact benchmark tables, real-robot coverage and failure cases require full PDF extraction.

### What Remains Unsolved?
Library Analysis: closed-loop robustness and real dual-arm execution of generated 3D plans remain open.

### Open Source
Official GitHub is linked from the card; checkpoint and reproducibility status require repository inspection.

### Relevance to Our Project
direct test of 3D planning value.

### Idea Clues
Idea Clue 1: compare explicit 3D goal prediction against image-only VLA on dual-arm ordinary-gripper tasks. Evidence: paper motivation and 3D goal image/point-cloud generation. Why relevant: direct test of 3D planning value.

### Evidence Sources
Official PMLR proceedings page and linked PDF; official project page; official GitHub.

- Evidence Level: Full-paper sections checked where official full text was accessible; otherwise official abstract/project/PDF evidence only.
- Citation Source Identifier: OpenAlex Work: https://openalex.org/W4392886475
