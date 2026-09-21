# DexVLG: Dexterous Vision-Language-Grasp Model at Scale

## Basic Information（基本信息）

- Title: DexVLG: Dexterous Vision-Language-Grasp Model at Scale
- Authors: He, Jiawei; Li, Danshi; Yu, Xinqiang; Qi, Zekun; Zhang, Wenyao; Chen, Jiayi; Zhang, Zhaoxiang; Zhang, Zhizheng; Yi, Li; Wang, He
- Year: 2025
- Venue: ICCV
- CCF Level: A
- Publication Status: Official Conference Paper
- Type: Method Paper
- Category: VLA; Dexterous Manipulation
- Subcategory: Vision-Language-Grasp / Flow Matching
- Keywords: Unknown

## Classification

- Primary Category: Dexterous
- Categories: VLA; Robot Manipulation; Dexterous; Diffusion / Flow / IL / RL
- Subcategories: Vision-Language-Grasp / Flow Matching
- Tags: Unknown

## Paper Links（论文）

- Official Paper: https://openaccess.thecvf.com/content/ICCV2025/html/He_DexVLG_Dexterous_Vision-Language-Grasp_Model_at_Scale_ICCV_2025_paper.html
- DOI: Unknown
- arXiv: Unknown
- Project Page: Unknown

## Code & Resources（代码与资源）

- Official GitHub: https://github.com/jiaweihe1996/DexVLG
- Code Status: Coming Soon
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
- Embodiment: Dexterous Hand
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

- **Problem:** 研究主题为 `Vision-Language-Grasp / Flow Matching`；本卡仅按官方摘要级证据整理，未替代全文审阅。
- **Main Contribution:**
  - In this paper, we introduce DexVLG, a large Vision-Language-Grasp model for Dexterous grasp pose prediction aligned with language instructions using single-view RGBD input.
  - To evaluate DexVLG's performance, we create benchmarks in simulations and conduct real-world experiments.
- **Key Idea:** 以 `Unknown` 为主要方法/能力线索；更细的结构和消融结论待正文核验。
- **Experiment / Validation:** Real Robot 字段为 `Yes`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。
- **Relevance to Our Project:** 可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

## Summary Evidence（摘要证据）

- Evidence Level: Abstract-level
- Sources: https://openaccess.thecvf.com/content/ICCV2025/html/He_DexVLG_Dexterous_Vision-Language-Grasp_Model_at_Scale_ICCV_2025_paper.html；官方摘要/论文集元数据
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping
- Verified Date: 2026-09-19
- Evidence Boundary: 未核实的机器人平台、数据集、代码可运行性和真机细节保持 Unknown。

## Verification（核验）

- [x] Venue confirmed
- [x] Full / Regular Paper confirmed
- [x] CCF A confirmed
- [x] Official Paper confirmed
- [ ] Project Page checked
- [x] Official GitHub checked
- [x] Code Status checked
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
- OpenAlex Work: https://openalex.org/W4417183400

## Standardized Research Fields

### Research Problem
研究主题为 `Vision-Language-Grasp / Flow Matching`；本卡仅按官方摘要级证据整理，未替代全文审阅。

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
以 `Unknown` 为主要方法/能力线索；更细的结构和消融结论待正文核验。

### Main Contributions
- In this paper, we introduce DexVLG, a large Vision-Language-Grasp model for Dexterous grasp pose prediction aligned with language instructions using single-view RGBD input.

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
可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

## Full-paper Enrichment (Batch 01)

- Evidence Quality: B

### Research Problem
Large vision-language models have rarely been scaled for language-aligned dexterous grasping because high-quality dexterous pose data is difficult to collect.

### What Previous Problem Does This Paper Solve?
Author-stated: prior large-model robotic work focuses mainly on simple grippers, leaving functional grasping with human-like dexterous hands underexplored.

### Model / Method
DexVLG uses single-view RGB-D, a point-cloud encoder and Florence-2 language model with a flow-matching pose head. The head predicts hand-base translation/rotation and finger joint angles conditioned on language and 3D features.

### Architecture / Key Components
Florence-2 (232M/771M); point-cloud encoder; CLIP-aligned 3D features; MLP projector; flow-matching pose denoiser; pose decoder.

### Dataset & Benchmark
DexGraspNet 3.0: 170 million dexterous grasp poses over 174,000 simulated objects, paired with part-level captions. Benchmarks include LVIS-Seen, Unseen and SamPart3D, plus physical-object tests.

### Baseline / SOTA
Compared against DexGraspNet2.0 retrained on DexGraspNet3.0 (DGN2.0*) and DGN2.0* + CLIP. Metrics are simulation success (Suc), part-touch accuracy (PTA) and part-grasp accuracy (PGA).

### Experiment Setup
Simulation benchmarks with 10,000-point clouds and language instructions; real-world physical-object experiments; training uses 230 epochs on 64 RTX 4090 GPUs.

### Main Results
On LVIS-Seen, Unseen and SamPart3D, the reported Suc values are 87.7/79.1/76.3%; PGA values are 62.1/36.3/52.0%. The project reports over 76% zero-shot execution success and successful part-aligned real grasps.

### Ablation Study
The paper compares language-enabled DGN2.0* + CLIP against the full VLM/flow model; exact component ablations require supplementary extraction.

### Failure Cases
The reported setting focuses on tabletop part-aligned grasps; broader clutter, occlusion and multi-step manipulation are not established by the cited results.

### Limitations
Evidence boundary: full failure taxonomy, checkpoint/data license and long-horizon manipulation beyond grasp execution require follow-up.

### What Remains Unsolved?
Library Analysis: language-aligned dexterous grasp generation still needs validation for bimanual coordination and ordinary-gripper transfer.

### Open Source
Official GitHub is listed in the card; checkpoint and dataset release status require repository-level verification.

### Relevance to Our Project
supports target-region and action alignment.

### Idea Clues
Idea Clue 1: use part-level language affordances as a perception front-end for bimanual grasp sequencing. Evidence: part-touch/part-grasp metrics and flow pose head. Why relevant: supports target-region and action alignment.

### Evidence Sources
Official ICCV 2025 paper/PDF; arXiv; official GitHub.

- Evidence Level: Full-paper sections checked where official full text was accessible; otherwise official abstract/project/PDF evidence only.
- Citation Source Identifier: OpenAlex Work: https://openalex.org/W4417183400
