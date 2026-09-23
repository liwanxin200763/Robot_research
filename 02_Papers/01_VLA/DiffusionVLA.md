# DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression

## Basic Information（基本信息）

- Title: DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression
- Authors: Junjie Wen; Yichen Zhu; Minjie Zhu; Zhibin Tang; Jinming Li; Zhongyi Zhou; Xiaoyu Liu; Chaomin Shen; Yaxin Peng; Feifei Feng
- Year: 2025
- Venue: ICML
- CCF Level: A
- Publication Status: Official Conference Paper
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Subcategory: VLA / Robot Foundation Models
- Keywords: VLA; Autoregressive Reasoning / Diffusion

## Classification

- Primary Category: VLA
- Categories: VLA; Robot Manipulation; Diffusion / Flow / IL / RL
- Subcategories: VLA / Robot Foundation Models
- Tags: VLA; Autoregressive Reasoning / Diffusion

## Paper Links（论文）

- Official Paper: https://proceedings.mlr.press/v267/wen25g.html
- DOI: Unknown
- arXiv: https://arxiv.org/abs/2412.03293
- Project Page: https://diffusion-vla.github.io/

## Code & Resources（代码与资源）

- Official GitHub: https://github.com/juruobenruo/DexVLA
- Code Status: Partial
- Hugging Face: Unknown
- ModelScope: Unknown
- Checkpoint / Weights: 公开ScaleDP权重不等于DiVLA论文完整权重；待核实（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: 作者提供DexVLA示例数据：https://huggingface.co/datasets/lesjie/dexvla_example_data；不是原论文全部实验数据
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

- Dataset: 作者提供DexVLA示例数据：https://huggingface.co/datasets/lesjie/dexvla_example_data；不是原论文全部实验数据
- Benchmark: Unknown
- Simulation Environment: Unknown
- Real-world Tasks: Unknown

## Research Summary（研究摘要）

- **Problem:** 研究主题为 `VLA / Robot Foundation Models`；本卡仅按官方摘要级证据整理，未替代全文审阅。
- **Main Contribution:**
  - DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and AutoregressionJunjie Wen, Yichen Zhu, Minjie Zhu, Zhibin Tang, Ji...
  - DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and AutoregressionJunjie Wen, Yichen Zhu, Minjie Zhu, Zhibin Tang, Ji...
- **Key Idea:** 以 `VLA; Autoregressive Reasoning / Diffusion` 为主要方法/能力线索；更细的结构和消融结论待正文核验。
- **Experiment / Validation:** Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。
- **Relevance to Our Project:** 可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

## Summary Evidence（摘要证据）

- Evidence Level: Abstract-level
- Sources: https://proceedings.mlr.press/v267/wen25g.html；官方摘要/论文集元数据
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

官网明确指向后续DexVLA仓库并称可训练DiVLA；实际存在train_divla.sh、UNet策略和评估。原论文模型/完整实验对应关系未核实；Partial可运行条件待复核，不准入核心。 Static checks only; no cloning/running or download.

## Citation Metrics

- Citation Count: Unknown
- Citation Source: OpenAlex (identity unmatched)
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: Unknown (no high-confidence match)
- OpenAlex Work: Unknown

## Standardized Research Fields

### Research Problem
研究主题为 `VLA / Robot Foundation Models`；本卡仅按官方摘要级证据整理，未替代全文审阅。

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
以 `VLA; Autoregressive Reasoning / Diffusion` 为主要方法/能力线索；更细的结构和消融结论待正文核验。

### Main Contributions
- DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and AutoregressionJunjie Wen, Yichen Zhu, Minjie Zhu, Zhibin Tang, Ji...

### Dataset & Benchmark
作者提供DexVLA示例数据：https://huggingface.co/datasets/lesjie/dexvla_example_data；不是原论文全部实验数据

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

## Full-paper Enrichment (Batch 02)

- Evidence Quality: A
- Evidence Status: Official full text was not reliably extractable in this batch; structured fields below preserve existing card evidence and mark unresolved details explicitly.

### Research Problem
研究主题为 `VLA / Robot Foundation Models`；本卡仅按官方摘要级证据整理，未替代全文审阅。

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
以 `VLA; Autoregressive Reasoning / Diffusion` 为主要方法/能力线索；更细的结构和消融结论待正文核验。

### Architecture / Key Components
Unknown / Needs Official Full-Text Verification

### Dataset & Benchmark
作者提供DexVLA示例数据：https://huggingface.co/datasets/lesjie/dexvla_example_data；不是原论文全部实验数据

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。

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
- Official GitHub: https://github.com/juruobenruo/DexVLA
- Code Status: Partial
- Checkpoint: Unknown
- Dataset: 作者提供DexVLA示例数据：https://huggingface.co/datasets/lesjie/dexvla_example_data；不是原论文全部实验数据

### Relevance to Our Project
** 可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://proceedings.mlr.press/v267/wen25g.html; https://diffusion-vla.github.io/; https://github.com/juruobenruo/DexVLA

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: A-Upgraded
- Supplement Status: Not Found
- Code Completeness: Partial
- Robot Platform Evidence: Unknown

## Deep Enrichment (Full Text Read: 2026-09-22)
- Evidence Quality: A
- Fulltext Checked: Yes — arXiv HTML 2412.03293v3 / ICML 2025 paper, Sections 2–4 and Supplementary Sections 6–7 inspected.
- Supplement Status: Available - Verified.
- Method: autoregressive VLM reasoning is injected into a diffusion policy through FiLM; total loss is Ldiff + αLntp with α=10 (Secs. 3.1–3.2).
- Backbone / Action: autoregressive reasoning module plus diffusion action model; DiVLA-2B/7B use DROID, while 72B uses OXE+DROID pretraining (Sec. 3.2).
- Dataset / Experiments: multi-task and visual-generalization tasks, factory sorting, zero-shot bin-picking, and bimanual table bussing; DROID/OXE pretraining and multiple real robots (Secs. 4, 6).
- Baselines: standard VLA/diffusion policy comparisons in multi-task, factory sorting and visual generalization settings (Sec. 4.2–4.5).
- Main Results: 63.7% accuracy on 102 previously unseen bin-picking objects; DiVLA-2B runs at 82 Hz on one A6000; scale is evaluated from 2B to 72B (abstract, Sec. 4.5).
- Ablation: loss weighting and reasoning injection are analyzed; supplementary tasks test distractors, background and colorful lighting (Secs. 3.2, Supplementary Figs. 10–11).
- Failure Cases: reasoning visualization is used for failure diagnosis; challenges include unseen object textures, varying heights and deformable objects (Supplementary Sec. 6).
- Limitations: Author-stated — dependence on auto-generated reasoning and limited task/embodiment coverage; Library Analysis — exact per-task failure counts are not fully tabulated in accessible HTML.
- Remaining Gap / Idea: evaluate whether reasoning injection remains useful when action space is dexterous or bimanual.
- Evidence Sources: https://arxiv.org/abs/2412.03293 ; https://diffusion-vla.github.io/ ; https://github.com/juruobenruo/DexVLA ; Sections 3–4 and Supplementary Sections 6–7.
- Evidence Upgrade Status: A-Upgraded