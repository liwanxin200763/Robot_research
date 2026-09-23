# Dreamitate: Real-World Visuomotor Policy Learning via Video Generation

## Basic Information（基本信息）

- Title: Dreamitate: Real-World Visuomotor Policy Learning via Video Generation
- Year: 2024
- Venue / Source: CoRL
- Publication Status: Formal CoRL 2024; PMLR v270 online 2025
- CCF Level: Not CCF A (robotics venue extension; CCF row not asserted)
- Type: Method Paper
- Category: VLA / Robot Foundation Models / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation
- Subcategory: VLA / Robot Foundation Models; Robot Manipulation / IL / Diffusion
- Priority: P1

## Classification

- Primary Category: Robot Manipulation
- Categories: VLA; Robot Manipulation; Diffusion / Flow / IL / RL
- Subcategories: VLA / Robot Foundation Models; Robot Manipulation / IL / Diffusion
- Tags: Unknown

## Links（链接）

- Official Paper: https://proceedings.mlr.press/v270/liang24a.html
- arXiv: 待补充
- Project Page: 待补充
- Official GitHub: 待补充

## Code（代码状态）

- Code Status: Unknown
- Checkpoint: 待补充
- Dataset Released: Unknown

## Embodiment（机器人形态）

- Single Arm / Bimanual / Dexterous Hand / Gripper: Single Arm / Parallel Gripper
- Real Robot: Yes

## Why Collected（为什么被收录）

Conference year is 2024; PMLR v270 published online in Jan 2025.

## Verification（待核验）

- [x] Venue 已确认
- [ ] CCF 等级已确认
- [x] Official Paper 已确认
- [ ] Official GitHub 已确认
- [ ] Code 可运行性已确认
- [x] 是否真机已确认

## Citation Metrics

- Citation Count: 0
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4400024954
- OpenAlex Work: https://openalex.org/W4400024954

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

## Full-paper Enrichment (Batch 07)

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
https://proceedings.mlr.press/v270/liang24a.html

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Fulltext-Unavailable
- Supplement Status: Not Found
- Code Completeness: Unknown
- Robot Platform Evidence: Unknown

## Deep Enrichment (Source Checked: 2026-09-22; Full Text Pending)
- Evidence Quality: B
- Fulltext Checked: No — official project page and arXiv PDF identified; extraction not completed in this batch.
- Supplement Status: Not Found.
- Evidence Boundary: abstract-level facts only; no detailed results added.
- Evidence Sources: https://arxiv.org/abs/2406.16862 ; https://dreamitate.cs.columbia.edu/ ; https://dreamitate.cs.columbia.edu/assets/dreamitate_arxiv_v3.pdf.
- Evidence Upgrade Status: B-Experiment-Not-Extracted.

## Citation Relations

### References in Library

- [[02_Papers/10_Benchmark_Dataset/DROID|DROID]] — [arXiv full-text bibliography item 1](https://arxiv.org/html/2406.16862#bib.bib1)

### Cited By in Library

- [[02_Papers/01_VLA/CoT-VLA|CoT-VLA]] — [arXiv full-text bibliography item 35](https://arxiv.org/html/2503.22020#bib.bib35)

### Related Work

- No curated content relation yet.

## 快速摘要

### 研究问题

机器人模仿学习策略在新视觉环境中往往难以保持稳定表现。

### 之前方法的问题

少量机器人示范不足以覆盖环境外观变化；直接行为克隆的泛化有限。

### 核心思路

Dreamitate 用人类任务示范微调视频扩散模型，再利用生成的视频辅助学习视觉运动策略。

### 输入

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 输出 / 动作

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 数据集 / Benchmark

论文评估四项复杂度递增的操作任务；具体任务设置见 CoRL 论文。

### 主要结果

官方摘要报告比现有行为克隆方法具有更强的视觉环境泛化；摘要未给出统一成功率数字。

### 为什么重要

探索大规模视频生成模型如何补充少量机器人示范。

### 和当前项目的关系

Medium：可借鉴视频到动作的数据利用方式，但双臂普通夹爪需单独验证。

### 主要局限

已核验摘要未明确列出全部失败情形；需读实验和局限章节。

### 摘要证据

官方摘要/论文页; https://arxiv.org/html/2406.16862; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
