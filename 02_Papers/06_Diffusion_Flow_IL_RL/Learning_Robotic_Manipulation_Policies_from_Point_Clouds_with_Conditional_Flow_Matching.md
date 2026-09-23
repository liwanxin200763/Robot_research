# Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching

## Basic Information（基本信息）

- Title: Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching
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

- Official Paper: https://proceedings.mlr.press/v270/chisari25a.html
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

- Citation Count: 1
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4403622102
- OpenAlex Work: https://openalex.org/W4403622102

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

## Full-paper Enrichment (Batch 09)

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
https://proceedings.mlr.press/v270/chisari25a.html

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

- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]] — [arXiv full-text bibliography item 1084](https://arxiv.org/html/2510.10903#bib.bib1084)

### Related Work

- No curated content relation yet.

## 快速摘要

### 研究问题

少量示范条件下，策略输入和动作生成目标的选择影响操作表现。

### 之前方法的问题

二维图像可能丢失三维几何；迭代生成动作又增加延迟。

### 核心思路

PointFlowMatch 从点云观测学习条件 Flow Matching 策略，生成机器人操作动作。

### 输入

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 输出 / 动作

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 数据集 / Benchmark

RLBench。

### 主要结果

作者报告在 RLBench 上达到有竞争力的结果；完整数值需看论文表格。

### 为什么重要

为点云输入加流式动作生成提供基线。

### 和当前项目的关系

Medium：双夹爪三维定位可借鉴，但真机点云质量需检查。

### 主要局限

仿真点云与真机深度噪声之间可能存在差距。

### 摘要证据

官方摘要/论文页; https://proceedings.mlr.press/v270/chisari25a.html; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
