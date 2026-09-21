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
- Citation Checked Date: 2026-09-21
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
