# 3D Diffuser Actor: Policy Diffusion with 3D Scene Representations

## Basic Information（基本信息）

- Title: 3D Diffuser Actor: Policy Diffusion with 3D Scene Representations
- Year: 2024
- Venue / Source: CoRL
- Publication Status: Formal CoRL 2024; PMLR v270 online 2025
- CCF Level: Not CCF A (robotics venue extension; CCF row not asserted)
- Type: Method Paper
- Category: Imitation Learning / Diffusion / Flow Matching / Robot Manipulation
- Subcategory: Robot Manipulation / IL / Diffusion
- Priority: P1

## Classification

- Primary Category: Diffusion / Flow / IL / RL
- Categories: Robot Manipulation; Diffusion / Flow / IL / RL
- Subcategories: Robot Manipulation / IL / Diffusion
- Tags: Unknown

## Links（链接）

- Official Paper: https://proceedings.mlr.press/v270/ke25a.html
- arXiv: 待补充
- Project Page: 待补充
- Official GitHub: 待补充

## Code（代码状态）

- Code Status: Unknown
- Checkpoint: 待补充
- Dataset Released: Unknown

## Embodiment（机器人形态）

- Single Arm / Bimanual / Dexterous Hand / Gripper: Single Arm / Parallel Gripper
- Real Robot: Unknown

## Why Collected（为什么被收录）

Conference year is 2024; PMLR v270 published online in Jan 2025.

## Verification（待核验）

- [x] Venue 已确认
- [ ] CCF 等级已确认
- [x] Official Paper 已确认
- [ ] Official GitHub 已确认
- [ ] Code 可运行性已确认
- [ ] 是否真机已确认

## Citation Metrics

- Citation Count: 4
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4391949089
- OpenAlex Work: https://openalex.org/W4391949089

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

## Full-paper Enrichment (Batch 08)

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
- Official GitHub: 待补充
- Code Status: Unknown
- Checkpoint: 待补充
- Dataset: Unknown

### Relevance to Our Project
Unknown / Needs project-specific review

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://proceedings.mlr.press/v270/ke25a.html

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Fulltext-Unavailable
- Supplement Status: Not Found
- Code Completeness: Unknown
- Robot Platform Evidence: Unknown

## Citation Relations

### References in Library

- No verified in-library citation edge yet.

### Cited By in Library

- [[02_Papers/01_VLA/BridgeVLA|BridgeVLA]] — [arXiv full-text bibliography item 11](https://arxiv.org/html/2506.07961#bib.bib11)
- [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]] — [arXiv full-text bibliography item 22](https://arxiv.org/html/2412.03293#bib.bib22)
- [[02_Papers/02_Robot_Manipulation/VidMan|VidMan]] — [arXiv full-text bibliography item 35](https://arxiv.org/html/2411.09153#bib.bib35)
- [[02_Papers/03_Bimanual/AnyBimanual|AnyBimanual]] — [arXiv full-text bibliography item 39](https://arxiv.org/html/2412.06779#bib.bib39)
- [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI|A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]] — [arXiv full-text bibliography item 111](https://arxiv.org/html/2405.14093#bib.bib111)
- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]] — [arXiv full-text bibliography item 881](https://arxiv.org/html/2510.10903#bib.bib881)

### Related Work

- [[02_Papers/06_Diffusion_Flow_IL_RL/Equivariant_Diffusion_Policy|Equivariant_Diffusion_Policy]] — 两者都以三维或等变结构改进操作动作生成。

## 快速摘要

### 研究问题

机器人动作有多种合理解，二维图像策略对三维几何理解不足。

### 之前方法的问题

直接回归动作或只用二维表示，可能难以表达多模态三维操作。

### 核心思路

3D Diffuser Actor 在三维场景表示上生成动作，并通过扩散模型刻画多种可行轨迹。

### 输入

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 输出 / 动作

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 数据集 / Benchmark

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 主要结果

论文报告与二维表示、回归及其他设计的消融比较，完整数字应以原论文表格为准。

### 为什么重要

是比较三维感知与生成式动作的基础方法。

### 和当前项目的关系

High：可为双普通夹爪的三维目标位姿生成提供基线。

### 主要局限

摘要不足以判断不同真机接触和双臂协调任务的完整覆盖。

### 摘要证据

官方摘要/论文页; https://proceedings.mlr.press/v270/ke25a.html; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
