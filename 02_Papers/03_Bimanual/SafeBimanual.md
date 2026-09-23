# SafeBimanual: Diffusion-based trajectory optimization for safe bimanual manipulation

## Basic Information（基本信息）

- Title: SafeBimanual: Diffusion-based trajectory optimization for safe bimanual manipulation
- Year: 2025
- Venue / Source: CoRL
- Publication Status: Formal PMLR v305 / CoRL 2025
- CCF Level: Not CCF A (robotics venue extension; CCF row not asserted)
- Type: Method Paper
- Category: Bimanual Manipulation / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation
- Subcategory: Bimanual
- Priority: P1

## Classification

- Primary Category: Bimanual
- Categories: Robot Manipulation; Bimanual; Diffusion / Flow / IL / RL
- Subcategories: Bimanual
- Tags: Unknown

## Links（链接）

- Official Paper: https://proceedings.mlr.press/v305/deng25c.html
- arXiv: 待补充
- Project Page: 待补充
- Official GitHub: 待补充

## Code（代码状态）

- Code Status: Unknown
- Checkpoint: 待补充
- Dataset Released: Unknown

## Embodiment（机器人形态）

- Single Arm / Bimanual / Dexterous Hand / Gripper: Bimanual
- Real Robot: Unknown

## Why Collected（为什么被收录）

待阅读后补充。

## Verification（待核验）

- [x] Venue 已确认
- [ ] CCF 等级已确认
- [x] Official Paper 已确认
- [ ] Official GitHub 已确认
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

## Full-paper Enrichment (Batch 03)

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
https://proceedings.mlr.press/v305/deng25c.html

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Fulltext-Unavailable
- Supplement Status: Not Found
- Code Completeness: Unknown
- Robot Platform Evidence: Unknown


## Deep Enrichment (Batch 04 Source Check: 2026-09-22)
- Evidence Quality: B
- Fulltext Checked: No — official proceedings/arXiv/project/repository search recorded for this batch; a legally accessible full text was not extracted in this pass.
- Supplement Status: Not Found.
- Evidence Boundary: no new numeric claims added without section/table verification.
- Required follow-up: extract Introduction, Method, Experiments, Results, Ablation, Failure Cases, Limitations and official code structure before Evidence A upgrade.
- Queue Status: Completed-B

## Citation Relations

### References in Library

- No verified in-library citation edge yet.

### Cited By in Library

- No verified in-library citation edge yet.

### Related Work

- No curated content relation yet.

## 快速摘要

### 研究问题

双臂扩散策略生成的动作可能违反安全和协调约束。

### 之前方法的问题

训练完成后的策略不一定知道新的障碍物或当前碰撞边界。

### 核心思路

SafeBimanual 在测试时对预训练扩散策略的轨迹进行优化，加入安全约束。

### 输入

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 输出 / 动作

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 数据集 / Benchmark

双臂扩散策略的测试时轨迹优化任务；具体 benchmark 见论文。

### 主要结果

已核验摘要未提供可安全复述的统一量化结果。

### 为什么重要

将安全约束放在策略与真机控制器之间，便于与现有策略组合。

### 和当前项目的关系

High：双臂普通夹爪真机部署需要碰撞与工作空间限制。

### 主要局限

优化耗时、约束保守程度和任务成功率之间的权衡需实测。

### 摘要证据

官方摘要/论文页; https://proceedings.mlr.press/v305/deng25c.html; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
