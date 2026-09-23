# TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies

## Basic Information（基本信息）

- Title: TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies
- Year: 2025
- Venue / Source: ICLR
- Publication Status: 正式主会论文：官方论文集核实
- CCF Level: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Type: Method Paper
- Category: VLA / Robot Foundation Models / Robot Manipulation
- Subcategory: VLA / Robot Foundation Models
- Priority: P1

## Classification

- Primary Category: VLA
- Categories: VLA; Robot Manipulation
- Subcategories: VLA / Robot Foundation Models
- Tags: Unknown

## Links（链接）

- Official Paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/8667f264f88c7938a73a53ab01eb1327-Abstract-Conference.html
- arXiv: 待补充
- Project Page: https://tracevla.github.io/
- Official GitHub: https://github.com/umd-huang-lab/tracevla

## Code（代码状态）

- Code Status: Partial
- Checkpoint: 项目页Models入口与README基座链接须区分；论文权重待核实（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset Released: 视觉轨迹标注数据仍标Coming soon；基础数据另行获取

## Embodiment（机器人形态）

- Single Arm / Bimanual / Dexterous Hand / Gripper: Single Arm / Parallel Gripper
- Real Robot: Unknown

## Why Collected（为什么被收录）

已查TraceProcessor、推理与训练代码；README仍称轨迹标注数据Coming soon，未验证论文权重/数据完整链。保守标Partial，待可运行性复核。 Static checks only; no cloning/running or download.

## Verification（待核验）

- [x] Venue 已确认
- [ ] CCF 等级已确认
- [x] Official Paper 已确认
- [x] Official GitHub 已确认
- [ ] Code 可运行性已确认
- [ ] 是否真机已确认

## Citation Metrics

- Citation Count: Unknown
- Citation Source: OpenAlex (exact identity unresolved; API coverage may limit lookup)
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: Unknown (exact scholarly work unresolved)
- OpenAlex Work: Unknown

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

- Evidence Quality: B
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
- Official GitHub: https://github.com/umd-huang-lab/tracevla
- Code Status: Partial
- Checkpoint: 项目页Models入口与README基座链接须区分；论文权重待核实（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: Unknown

### Relevance to Our Project
Unknown / Needs project-specific review

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://proceedings.iclr.cc/paper_files/paper/2025/hash/8667f264f88c7938a73a53ab01eb1327-Abstract-Conference.html; https://tracevla.github.io/; https://github.com/umd-huang-lab/tracevla

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Fulltext-Unavailable
- Supplement Status: Not Found
- Code Completeness: Partial
- Robot Platform Evidence: Unknown

## Deep Enrichment (Full Text Read: 2026-09-22)
- Evidence Quality: A
- Fulltext Checked: Yes — arXiv HTML 2412.10345v3, Secs. 3–4 and Appendices A–F inspected.
- Supplement Status: Available - Verified.
- Method: visual trace prompting overlays multi-point state-action trajectories on images to expose spatial-temporal history to OpenVLA (Sec. 3).
- Dataset / Results: 150K collected robot manipulation trajectories; 137 SimplerEnv configurations and 4 physical WidowX tasks. TraceVLA outperforms OpenVLA by 10% in SimplerEnv and 3.5× on real-robot tasks (abstract, Sec. 4).
- Ablation: trace thickness/transparency/color and historical-observation steps are tested in App. C; additional LIBERO results in App. F.
- Failure Cases / Limitations: trace quality and history length can over/under-condition the policy; real-robot task coverage is limited.
- Remaining Gap / Idea: combine visual traces with explicit future-image reasoning.
- Evidence Sources: https://arxiv.org/html/2412.10345 ; ICLR 2025 official paper.
- Evidence Upgrade Status: A-Upgraded

## Citation Relations

### References in Library

- [[02_Papers/01_VLA/Octo|Octo]] — [arXiv full-text bibliography item 35](https://arxiv.org/html/2412.10345#bib.bib35)
- [[02_Papers/01_VLA/OpenVLA|OpenVLA]] — [arXiv full-text bibliography item 25](https://arxiv.org/html/2412.10345#bib.bib25)
- [[02_Papers/10_Benchmark_Dataset/DROID|DROID]] — [arXiv full-text bibliography item 24](https://arxiv.org/html/2412.10345#bib.bib24)
- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open_X-Embodiment]] — [arXiv full-text bibliography item 8](https://arxiv.org/html/2412.10345#bib.bib8)

### Cited By in Library

- [[02_Papers/01_VLA/SpatialVLA|SpatialVLA]] — [arXiv full-text bibliography item 71](https://arxiv.org/html/2501.15830#bib.bib71)
- [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI|A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]] — [arXiv full-text bibliography item 117](https://arxiv.org/html/2405.14093#bib.bib117)
- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]] — [arXiv full-text bibliography item 924](https://arxiv.org/html/2510.10903#bib.bib924)

### Related Work

- No curated content relation yet.

## 快速摘要

### 研究问题

大规模预训练 VLA 对交互中的时空动态仍可能理解不足。

### 之前方法的问题

只看当前帧，难表示动作轨迹和目标运动方向。

### 核心思路

TraceVLA 将状态—动作轨迹可视化为 trace prompt，辅助 VLA 做时空推理与动作预测。

### 输入

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 输出 / 动作

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 数据集 / Benchmark

SimplerEnv 137 种配置与 WidowX 真机四项任务。

### 主要结果

卡片记录相对 OpenVLA 在 SimplerEnv 高约 10%，真机任务表现约为 3.5 倍；指标定义见原卡。

### 为什么重要

为视觉轨迹提示如何改善 VLA 提供可测实例。

### 和当前项目的关系

High：双臂任务可以比较轨迹提示与显式状态估计。

### 主要局限

单臂 WidowX 结果不直接覆盖双臂真机。

### 摘要证据

官方摘要/论文页; https://arxiv.org/html/2412.10345; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
