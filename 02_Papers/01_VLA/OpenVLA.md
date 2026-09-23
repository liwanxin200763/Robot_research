# OpenVLA: An Open-Source Vision-Language-Action Model

## Basic Information（基本信息）

- Title: OpenVLA: An Open-Source Vision-Language-Action Model
- Year: 2024
- Venue / Source: CoRL
- Publication Status: Formal CoRL 2024; PMLR volume 270 online 2025
- CCF Level: Not CCF A (robotics venue extension)
- Type: Method Paper
- Category: VLA / Robot Foundation Models / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation
- Subcategory: VLA / Robot Foundation Models; Robot Manipulation / IL / Diffusion
- Priority: P0

## Classification

- Primary Category: VLA
- Categories: VLA; Robot Manipulation; Diffusion / Flow / IL / RL
- Subcategories: VLA / Robot Foundation Models; Robot Manipulation / IL / Diffusion
- Tags: Unknown

## Links（链接）

- Official Paper: https://proceedings.mlr.press/v270/kim24e.html
- arXiv: https://arxiv.org/abs/2406.09246
- Project Page: https://openvla.github.io/
- Official GitHub: https://github.com/openvla/openvla

## Code（代码状态）

- Code Status: Released
- Checkpoint: Author checkpoint links; not downloaded
- Dataset Released: Partial (Open X-Embodiment sources; not downloaded)

## Embodiment（机器人形态）

- Single Arm / Bimanual / Dexterous Hand / Gripper: Single Arm / Parallel Gripper
- Real Robot: Yes

## Why Collected（为什么被收录）

Core public VLA baseline; platform and precise real-robot protocol require follow-up reading.

## Verification（待核验）

- [x] Venue 已确认
- [ ] CCF 等级已确认
- [x] Official Paper 已确认
- [x] Official GitHub 已确认
- [ ] Code 可运行性已确认
- [x] 是否真机已确认

## Citation Metrics

- Citation Count: 43
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4399695759
- OpenAlex Work: https://openalex.org/W4399695759

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
- Official GitHub: https://github.com/openvla/openvla
- Code Status: Released
- Checkpoint: Author checkpoint links; not downloaded
- Dataset: Unknown

### Relevance to Our Project
Unknown / Needs project-specific review

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://proceedings.mlr.press/v270/kim24e.html; https://openvla.github.io/; https://github.com/openvla/openvla

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: A-Upgraded
- Supplement Status: Not Found
- Code Completeness: Mostly Complete
- Robot Platform Evidence: Unknown

## Deep Enrichment (Full Text Read: 2026-09-22)
- Evidence Quality: A
- Fulltext Checked: Yes — arXiv HTML 2406.09246v3 / CoRL 2024 paper, Sections 3–6 and Appendices A–E inspected.
- Supplement Status: Available - Verified.
- Method: 7B Prismatic VLM with Llama 2, fused DINOv2+SigLIP encoders and an MLP projector; continuous actions are discretized into 256 tokenizer bins and trained with next-token cross-entropy (Secs. 3.1–3.2).
- Dataset: curated Open X-Embodiment mixture with 970k real-world trajectories, third-person views and single-arm end-effector control; DROID was removed from the final third of training after low action-token accuracy (Sec. 3.3, App. A).
- Baselines / Experiments: RT-2-X, Octo and Diffusion Policy across WidowX, Google Robot, Franka-Tabletop, Franka-DROID and LIBERO settings (Sec. 5, App. B–E).
- Main Results: +16.5 percentage points absolute success over 55B RT-2-X across 29 tasks/embodiments; +20.4% over Diffusion Policy in reported fine-tuning settings; 27 epochs, 64 A100s for 14 days, ~21,500 A100-hours; inference ~6 Hz on RTX 4090 with 15GB bfloat16 memory (Secs. 3.4–3.5, 5).
- Ablation: VLM backbone, resolution, vision-encoder finetuning, training epochs, learning rate, OpenX mixture, dual vs single encoder, quantization and LIBERO are detailed in Sec. 3.4 and Appendices D–E.
- Failure Cases: language grounding and novel-object distractors remain difficult; DROID diversity produced low action-token accuracy, motivating its removal (Secs. 3.3–3.4).
- Limitations: Author-stated — training data is restricted to single-arm/third-person configurations and the model still requires substantial compute; Library Analysis — bimanual/mobile transfer is not established.
- Remaining Gap / Idea: combine OpenVLA’s open training stack with explicit visual subgoal or gaze reconstruction for long-horizon tasks.
- Evidence Sources: https://arxiv.org/abs/2406.09246 ; https://openvla.github.io/ ; https://github.com/openvla/openvla ; Sections 3–6, Appendices A–E.
- Evidence Upgrade Status: A-Upgraded

## Citation Relations

### References in Library

- [[02_Papers/01_VLA/Octo|Octo]] — [arXiv full-text bibliography item 5](https://arxiv.org/html/2406.09246#bib.bib5)
- [[02_Papers/10_Benchmark_Dataset/DROID|DROID]] — [arXiv full-text bibliography item 11](https://arxiv.org/html/2406.09246#bib.bib11)
- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open_X-Embodiment]] — [arXiv full-text bibliography item 1](https://arxiv.org/html/2406.09246#bib.bib1)

### Cited By in Library

- [[02_Papers/01_VLA/Actions_as_Language|Actions_as_Language]] — [arXiv full-text bibliography item 4](https://arxiv.org/html/2509.22195#bib.bib4)
- [[02_Papers/01_VLA/BridgeVLA|BridgeVLA]] — [arXiv full-text bibliography item 5](https://arxiv.org/html/2506.07961#bib.bib5)
- [[02_Papers/01_VLA/CoT-VLA|CoT-VLA]] — [arXiv full-text bibliography item 29](https://arxiv.org/html/2503.22020#bib.bib29)
- [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]] — [arXiv full-text bibliography item 24](https://arxiv.org/html/2412.03293#bib.bib24)
- [[02_Papers/01_VLA/ReconVLA|ReconVLA]] — [arXiv full-text bibliography item 21](https://arxiv.org/html/2508.10333#bib.bib21)
- [[02_Papers/01_VLA/RoboGround|RoboGround]] — [arXiv full-text bibliography item 19](https://arxiv.org/html/2504.21530#bib.bib19)
- [[02_Papers/01_VLA/RoboMamba|RoboMamba]] — [arXiv full-text bibliography item 29](https://arxiv.org/html/2406.04339#bib.bib29)
- [[02_Papers/01_VLA/RoboMonkey|RoboMonkey]] — [arXiv full-text bibliography item 2](https://arxiv.org/html/2506.17811#bib.bib2)
- [[02_Papers/01_VLA/SP-VLA|SP-VLA]] — [arXiv full-text bibliography item 10](https://arxiv.org/html/2506.12723#bib.bib10)
- [[02_Papers/01_VLA/SimpleVLA-RL|SimpleVLA-RL]] — [arXiv full-text bibliography item 2](https://arxiv.org/html/2509.09674#bib.bib2)
- [[02_Papers/01_VLA/SpatialVLA|SpatialVLA]] — [arXiv full-text bibliography item 30](https://arxiv.org/html/2501.15830#bib.bib30)
- [[02_Papers/01_VLA/TraceVLA|TraceVLA]] — [arXiv full-text bibliography item 25](https://arxiv.org/html/2412.10345#bib.bib25)
- [[02_Papers/01_VLA/VLA-Cache|VLA-Cache]] — [arXiv full-text bibliography item 11](https://arxiv.org/html/2502.02175#bib.bib11)
- [[02_Papers/01_VLA/VideoVLA|VideoVLA]] — [arXiv full-text bibliography item 3](https://arxiv.org/html/2512.06963#bib.bib3)
- [[02_Papers/03_Bimanual/AnyBimanual|AnyBimanual]] — [arXiv full-text bibliography item 41](https://arxiv.org/html/2412.06779#bib.bib41)
- [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective|A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective]] — [arXiv full-text bibliography item 21](https://arxiv.org/html/2507.01925#bib.bib21)
- [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI|A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]] — [arXiv full-text bibliography item 35](https://arxiv.org/html/2405.14093#bib.bib35)
- [[02_Papers/09_Survey_Review/Learning_by_Watching|Learning_by_Watching]] — [arXiv full-text bibliography item 96](https://arxiv.org/html/2402.07127#bib.bib96)
- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]] — [arXiv full-text bibliography item 13](https://arxiv.org/html/2510.10903#bib.bib13)

### Related Work

- [[02_Papers/01_VLA/SayCan|SayCan]] — 比较“显式技能可执行性规划”与“视觉语言直接预测动作”。
- [[02_Papers/01_VLA/Octo|Octo]] — 两种通用机器人策略，架构和训练数据组合不同。
- [[02_Papers/03_Bimanual/RDT-1B|RDT-1B]] — 比较通用 VLA 与双臂扩散式动作生成，重点看动作表示。
- [[02_Papers/05_Sim2Real/Sim2Real-VLA|Sim2Real-VLA]] — 比较合成数据到真机的 VLA 迁移与开放通用 VLA 基线。

## 快速摘要

### 研究问题

现有 VLA 多为闭源，且针对新任务高效微调的方法仍不充分。

### 之前方法的问题

既有 VLA 多为闭源，新任务的高效微调方法也缺少系统评估。

### 核心思路

OpenVLA 是开放的 7B VLA，在约 97 万条真实机器人轨迹上训练，支持通过微调适配新任务。

### 输入

机器人相机图像和语言任务指令；具体预处理见论文方法及官方代码。

### 输出 / 动作

预测机器人控制动作；动作编码与本体适配以官方代码和论文方法为准。

### 数据集 / Benchmark

训练使用整理后的 Open X-Embodiment 混合数据，约 97 万条真机轨迹；DROID 在后期训练数据中被剔除，详见原卡。

### 主要结果

卡片记录在 29 项任务/本体评测中相对 55B RT-2-X 的成功率高 16.5 个百分点；微调设置下相对 Diffusion Policy 高 20.4 个百分点。推理约 6 Hz（RTX 4090）；比较条件详见原卡。

### 为什么重要

提供可复用的 VLA 基线，同时明确了数据、算力和推理速度代价。

### 和当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

### 主要局限

作者指出训练数据偏单臂、第三人称视角且算力成本高；双臂/移动平台迁移仍需单独验证。

### 摘要证据

官方摘要/论文页; https://arxiv.org/html/2406.09246; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
