# ReconVLA

## Basic Information（基本信息）

- Title: ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver
- Authors: Wenxuan Song; Ziyang Zhou; Han Zhao; Jiayi Chen; Pengxiang Ding; Haodong Yan; Yuxin Huang; Feilong Tang; Donglin Wang; Haoang Li
- Year: 2026
- Venue: AAAI
- CCF Level: A
- Publication Status: Official Conference Paper (AAAI-26 Technical Track on Intelligent Robotics)
- DOI: 10.1609/aaai.v40i22.38921

## Classification

- Primary Category: VLA
- Categories: VLA; Robot Manipulation; Generalization / Long-Horizon; Diffusion / Flow / IL / RL
- Subcategories: Visual Grounding / Robot Perception / Gaze-Region Reconstruction
- Tags: VLA; Robot Manipulation; Visual Grounding; Robot Perception; Implicit Grounding; Gaze-Region Reconstruction; Generalization; Diffusion Transformer
- Special Attention: Yes
- Priority: P1

## Paper Links（论文）

- Official Paper: https://ojs.aaai.org/index.php/AAAI/article/view/38921
- arXiv: https://arxiv.org/abs/2508.10333
- Project Page: https://zionchow.github.io/ReconVLA/

## Code & Resources（代码与资源）

- Official GitHub: https://github.com/OpenHelix-Team/ReconVLA
- Code Status: Released
- Checkpoint: Unknown — 本轮未在作者项目页或官方仓库中发现 ReconVLA checkpoint 的公开入口。
- Dataset: 官方仓库不附带原始数据；提供 BridgeData V2、LIBERO、CALVIN 的下载与预处理说明。论文所述 100k+ trajectories / 2M samples 汇编数据集的独立完整下载入口未核实。
- Demo: https://zionchow.github.io/ReconVLA/
- Evaluation: 官方仓库提供 CALVIN 评测脚本与说明；本轮未下载数据或运行代码。

## Robot / Embodiment（机器人与形态）

- Robot Platform: Franka Panda (CALVIN simulation); real-world platform not confirmed at abstract level
- Embodiment: Single Arm / Parallel Gripper
- Single / Bimanual: Single Arm
- Gripper / Hand: Parallel Gripper
- Real Robot: Yes
- Simulation: Yes (CALVIN)

## Research Summary（研究摘要）

- **Problem:** 现有 VLA 在执行操作时对任务目标区域的视觉注意力往往过于分散，可能关注错误对象，影响精确操作。
- **Main Contribution:** 提出 ReconVLA，以凝视区域重建作为辅助视觉监督，在不依赖额外 grounding 输入或显式边界框输出的情况下提升 VLA 的视觉 grounding；并构建包含 100k+ 轨迹和 2M 数据样本的机器人预训练数据集以增强视觉重建泛化。
- **Key Idea:** 模型从 VLA 的视觉输出生成重建条件，由轻量 diffusion transformer 从噪声重建对应目标操作对象的 gaze region，使视觉表示隐式对齐到正确目标区域，同时保留动作预测目标。
- **Experiment / Validation:** 官方论文报告在 CALVIN 仿真和真实机器人任务上进行实验，并比较 implicit grounding、explicit grounding 与 chain-of-thought grounding；结果支持其精确操作、长时序任务和未见目标泛化能力。
- **Relevance to Our Project:** 适合用于研究 VLA 感知瓶颈、目标区域 grounding 与操作策略联合训练；其辅助重建目标可作为提升复杂场景目标选择和泛化能力的参考。

## Summary Evidence（摘要证据）

- Evidence Level: Abstract-level
- Sources: https://ojs.aaai.org/index.php/AAAI/article/view/38921；https://arxiv.org/abs/2508.10333；https://zionchow.github.io/ReconVLA/；https://github.com/OpenHelix-Team/ReconVLA
- Verification Status: Official AAAI proceedings, author project page, arXiv, and official code repository verified; CCF A verified on the current official CCF Artificial Intelligence list
- Verified Date: 2026-09-20
- Evidence Boundary: 内容以 AAAI 官方摘要、作者项目页和官方仓库静态核验为主；未完成全文全文证据核验、代码运行、权重下载或复现实验。

## Verification（核验）

- [x] Title and authors confirmed
- [x] Venue and publication status confirmed
- [x] DOI confirmed
- [x] CCF A confirmed from official CCF source
- [x] Official Paper confirmed
- [x] arXiv and Project Page confirmed
- [x] Official GitHub checked
- [x] Code Status checked
- [x] Dataset instructions checked
- [ ] Checkpoint release confirmed
- [ ] Local reproduction completed

## Notes（备注）

Code Status `Released` 表示官方仓库已公开训练、评测和数据预处理实现；不表示 checkpoint、汇编后的完整预训练数据或本地复现已完成。

## Citation Metrics

- Citation Count: 3
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W7137985120
- OpenAlex Work: https://openalex.org/W7137985120

## Standardized Research Fields

### Research Problem
现有 VLA 在执行操作时对任务目标区域的视觉注意力往往过于分散，可能关注错误对象，影响精确操作。

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
模型从 VLA 的视觉输出生成重建条件，由轻量 diffusion transformer 从噪声重建对应目标操作对象的 gaze region，使视觉表示隐式对齐到正确目标区域，同时保留动作预测目标。

### Main Contributions
提出 ReconVLA，以凝视区域重建作为辅助视觉监督，在不依赖额外 grounding 输入或显式边界框输出的情况下提升 VLA 的视觉 grounding；并构建包含 100k+ 轨迹和 2M 数据样本的机器人预训练数据集以增强视觉重建泛化。

### Dataset & Benchmark
官方仓库不附带原始数据；提供 BridgeData V2、LIBERO、CALVIN 的下载与预处理说明。论文所述 100k+ trajectories / 2M samples 汇编数据集的独立完整下载入口未核实。

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
官方论文报告在 CALVIN 仿真和真实机器人任务上进行实验，并比较 implicit grounding、explicit grounding 与 chain-of-thought grounding；结果支持其精确操作、长时序任务和未见目标泛化能力。

### Main Results
Unknown / Needs Full-Paper Verification

### Limitations
Unknown / Needs Full-Paper Verification

### What Remains Unsolved?
Library Analysis / Research Note: Unknown / Needs Full-Paper Verification

### Relevance to Our Project
适合用于研究 VLA 感知瓶颈、目标区域 grounding 与操作策略联合训练；其辅助重建目标可作为提升复杂场景目标选择和泛化能力的参考。

## Full-paper Enrichment (Batch 01)

- Evidence Quality: A

### Research Problem
Current VLAs may spread visual attention across irrelevant regions instead of the task target, weakening precise manipulation and generalization.

### What Previous Problem Does This Paper Solve?
Author-stated: existing VLAs struggle to allocate visual attention to target regions; ReconVLA addresses this with implicit grounding rather than requiring explicit grounding inputs.

### Model / Method
A diffusion transformer reconstructs the gaze region of the manipulated object conditioned on the VLA visual outputs, jointly encouraging task-specific visual representations while preserving action prediction.

### Architecture / Key Components
VLA backbone; visual output conditioning; diffusion transformer reconstruction head; implicit gaze-region grounding.

### Dataset & Benchmark
Curated pretraining data from open-source robotics datasets: over 100k trajectories and 2 million samples. Evaluation includes CALVIN simulation and real-world manipulation.

### Baseline / SOTA
Official abstract confirms comparison of implicit grounding against alternative grounding paradigms; exact named baselines and metric table require full PDF extraction.

### Experiment Setup
Simulation and real-world manipulation; CALVIN is explicitly named. Exact robot hardware and episode protocol are not stated in the accessible abstract-level evidence.

### Main Results
Official AAAI abstract reports improved precise manipulation and generalization, but no numeric result is entered without table-level extraction.

### Ablation Study
Not Reported in the official abstract/project evidence rechecked for this batch.

### Failure Cases
Not Explicitly Reported in the accessible official abstract/project evidence.

### Limitations
Evidence boundary: exact ablations, failure cases, checkpoint release and full benchmark numbers still require paper-table extraction.

### What Remains Unsolved?
Library Analysis: calibration of reconstructed attention under occlusion, clutter and multi-object bimanual scenes remains open.

### Open Source
Official GitHub is released for training/evaluation and preprocessing; checkpoint and complete assembled pretraining data release were not confirmed.

### Relevance to Our Project
maps directly to current VLA perception bottleneck.

### Idea Clues
Idea Clue 1: test implicit gaze reconstruction on dual-arm ordinary-gripper tasks with distractor objects. Evidence: official target-region grounding motivation. Why relevant: maps directly to current VLA perception bottleneck.

### Evidence Sources
Official AAAI paper page and DOI; official arXiv; author project page; official GitHub.

- Evidence Level: Full-paper sections checked where official full text was accessible; otherwise official abstract/project/PDF evidence only.
- Citation Source Identifier: OpenAlex Work: https://openalex.org/W7137985120
- Evidence Upgrade Status: A-Upgraded
- Supplement Status: Available - Verified
- Code Completeness: Mostly Complete
- Robot Platform Evidence: Franka Panda (CALVIN simulation); real-world platform not confirmed at abstract level


## Deep Enrichment (Full Text Read: 2026-09-21)

- Evidence Quality: A
- Fulltext Checked: Yes — arXiv PDF `2508.10333`, text extracted and sections/tables inspected.
- Supplement Status: Available - Verified (AAAI supplementary material link checked from official paper page; no separate numeric claims added beyond the paper text reviewed).

### Method (field-level evidence)
- Input / Observation: RGB image history plus language instruction; the model uses a reconstructed gaze region as an intermediate visual target (Sec. 3, Fig. 2).
- Backbone: Qwen2.5-VL-3B-Instruct and SigLIP-so400m visual encoder are specified in the architecture description (Sec. 3.2).
- Core Architecture: autoregressive action head coupled with a diffusion transformer that reconstructs the target/gaze region (Sec. 3.2–3.3).
- Key Modules: implicit visual grounding, gaze-region reconstruction, and action prediction; the reconstruction signal is trained jointly with action supervision (Sec. 3, Fig. 2).
- Intermediate Representation: reconstructed image crop / gaze region and its visual tokens (Sec. 3.3).
- Action Representation: executable robot action tokens predicted autoregressively (Sec. 3.2).
- Training / Loss: large-scale pretraining on BridgeData V2, LIBERO, and CALVIN-derived data; language/action and visual reconstruction objectives are combined (Sec. 3.4).
- Inference: reconstruct the task-relevant region and use the resulting representation to condition action generation; the paper argues this improves sub-goal switching in long-horizon tasks (Sec. 3.3).

### Dataset & Benchmark
- Training Dataset: BridgeData V2, LIBERO, and CALVIN-derived open robotic data (Sec. 3.4); the constructed pretraining corpus contains over 100k trajectories and 2M samples (abstract and Sec. 3.4).
- Evaluation Dataset / Benchmark: CALVIN ABC→D and ABCD→D, plus real-world manipulation tasks (Sec. 4, Tables 1–4).
- Real-world Dataset / Data Collection: real-world experiments are described in Sec. 4.6; the paper reports qualitative and task-success comparisons but does not provide a reusable public dataset.

### Baselines / Main Results
- Table 1 compares the baseline and explicit/implicit grounding variants; the extracted text reports baseline average success 57.0 and the EG variant 62.2 on the shown CALVIN setting, with corresponding average length 3.36 and 3.61.
- Table 2 is an ablation of reconstructive part, gaze region, and pretraining; numeric rows were inspected in the PDF. The paper attributes the gain to implicit grounding and target-region reconstruction rather than adding a separate detector at inference.
- Tables 3–4 compare manipulation models on CALVIN ABC→D and ABCD→D; exact per-task values are retained in the official PDF and were not transcribed here beyond the verified rows above.

### Failure Cases
- The discussion around Fig. 4 notes failures when the target is not grounded precisely or when preprocessing/detector localization is inaccurate; these are evidence-backed qualitative failure modes (Sec. 4.6).

### Limitations
- Author-stated: performance depends on reconstructing the correct target region and the reported evaluation is concentrated on CALVIN plus a limited real-world suite (Sec. 4.6 and conclusion).
- Library Analysis: broader embodiment and unseen-camera robustness remain unverified from the reported experiments.

### Remaining Unsolved Problem / Idea Clues
- Evidence: ablations isolate reconstruction and gaze-region supervision as the main contributors (Table 2).
- Research question: test whether the same implicit grounding signal improves bimanual and dexterous policies under occlusion and long-horizon sub-goal switches.

### Evidence Sources
- https://ojs.aaai.org/index.php/AAAI/article/view/38921
- https://arxiv.org/abs/2508.10333
- https://github.com/OpenHelix-Team/ReconVLA
- PDF locations: Abstract; Sec. 3.2–3.4; Sec. 4; Tables 1–4; Fig. 4.

- Evidence Upgrade Status: A-Upgraded
- Code Completeness: Partial — repository includes training/evaluation/preprocessing entry points; checkpoint and complete assembled pretraining data were not confirmed.

## Citation Relations

### References in Library

- [[02_Papers/01_VLA/3D-VLA|3D-VLA]] — [arXiv full-text bibliography item 58](https://arxiv.org/html/2508.10333#bib.bib58)
- [[02_Papers/01_VLA/Octo|Octo]] — [arXiv full-text bibliography item 32](https://arxiv.org/html/2508.10333#bib.bib32)
- [[02_Papers/01_VLA/OpenVLA|OpenVLA]] — [arXiv full-text bibliography item 21](https://arxiv.org/html/2508.10333#bib.bib21)
- [[02_Papers/01_VLA/RoboGround|RoboGround]] — [arXiv full-text bibliography item 18](https://arxiv.org/html/2508.10333#bib.bib18)
- [[02_Papers/02_Robot_Manipulation/VidMan|VidMan]] — [arXiv full-text bibliography item 49](https://arxiv.org/html/2508.10333#bib.bib49)
- [[02_Papers/07_Generalization_LongHorizon/Closed-Loop_Visuomotor_Control_with_Generative_Expectation_for_Robotic_Manipulation|Closed-Loop_Visuomotor_Control_with_Generative_Expectation_for_Robotic_Manipulation]] — [arXiv full-text bibliography item 6](https://arxiv.org/html/2508.10333#bib.bib6)
- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open_X-Embodiment]] — [arXiv full-text bibliography item 33](https://arxiv.org/html/2508.10333#bib.bib33)

### Cited By in Library

- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]] — [arXiv full-text bibliography item 926](https://arxiv.org/html/2510.10903#bib.bib926)

### Related Work

- [[02_Papers/01_VLA/RoboGround|RoboGround]] — Both target visual grounding in VLA-style manipulation, with different perception mechanisms.

## Quick Summary

- Problem: Current VLAs may spread visual attention across irrelevant regions instead of the task target, weakening precise manipulation and generalization.
- Previous Gap: Author-stated: existing VLAs struggle to allocate visual attention to target regions; ReconVLA addresses this with implicit grounding rather than requiring explicit grounding inputs.
- Core Idea: A diffusion transformer reconstructs the gaze region of the manipulated object conditioned on the VLA visual outputs, jointly encouraging task-specific visual representations while preserving action prediction.
- Input: RGB image history plus language instruction; the model uses a reconstructed gaze region as an intermediate visual target (Sec. 3, Fig. 2).
- Output / Action: Not specified in checked abstract/card.
- Dataset / Benchmark: Training Dataset: BridgeData V2, LIBERO, and CALVIN-derived open robotic data (Sec. 3.4); the constructed pretraining corpus contains over 100k trajectories and 2M samples…
- Main Result: Official AAAI abstract reports improved precise manipulation and generalization, but no numeric result is entered without table-level extraction.
- Why It Matters: Provides a concrete method or benchmark for the documented gap: Author-stated: existing VLAs struggle to allocate visual attention to target regions; ReconVLA addresses this with implicit…
- Project Relevance: High — informs language-conditioned manipulation and VLA design.
- Key Limitation: Author-stated: performance depends on reconstructing the correct target region and the reported evaluation is concentrated on CALVIN plus a limited real-world suite (Sec. 4.6 and conclusion). - Library Analysis: broader…
- Summary Evidence: Official abstract / paper page; https://arxiv.org/html/2508.10333; checked 2026-09-23. Rapid summary only; existing Evidence Quality is unchanged.
- Quick Summary Status: Evidence-backed
