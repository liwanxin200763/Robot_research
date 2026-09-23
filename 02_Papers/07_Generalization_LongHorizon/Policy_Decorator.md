# Policy Decorator: Model-Agnostic Online Refinement for Large Policy Models

## Basic Information（基本信息）

- Title: Policy Decorator: Model-Agnostic Online Refinement for Large Policy Models
- Year: 2025
- Venue / Source: ICLR
- Publication Status: ICLR 2025 Conference
- CCF Level: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Type: Method Paper
- Category: Imitation Learning / Diffusion / Flow Matching / Robot Manipulation
- Subcategory: Robot Manipulation / IL / Diffusion
- Priority: P1

## Classification

- Primary Category: Generalization / Long-Horizon
- Categories: Robot Manipulation; Diffusion / Flow / IL / RL; Generalization / Long-Horizon
- Subcategories: Robot Manipulation / IL / Diffusion
- Tags: Unknown

## Links（链接）

- Official Paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/45c361d4117d598d4bb6568b407e9ac9-Abstract-Conference.html
- arXiv: 待补充
- Project Page: 待补充
- Official GitHub: 待补充

## Code（代码状态）

- Code Status: Unknown
- Checkpoint: 待补充
- Dataset Released: Unknown

## Embodiment（机器人形态）

- Single Arm / Bimanual / Dexterous Hand / Gripper: Bimanual / Dexterous benchmark tasks
- Real Robot: Unknown

## Why Collected（为什么被收录）

Uses ManiSkill and Adroit tasks; baselines include Behavior Transformer and Diffusion Policy.

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

## Full-paper Enrichment (Batch 05)

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
https://proceedings.iclr.cc/paper_files/paper/2025/hash/45c361d4117d598d4bb6568b407e9ac9-Abstract-Conference.html

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

- No verified in-library citation edge yet.

### Related Work

- No curated content relation yet.

## 快速摘要

### 研究问题

大型模仿策略在新环境中仍可能出现局部失误。

### 之前方法的问题

重新训练完整策略成本高，且难快速修复特定失败。

### 核心思路

Policy Decorator 在已有模仿策略外加模型无关的 residual policy，对执行动作进行局部修正。

### 输入

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 输出 / 动作

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 数据集 / Benchmark

ManiSkill 与 Adroit，共八项任务。

### 主要结果

作者报告在两项 benchmark 的八个任务上提升所比较策略；具体幅度需查论文表格。

### 为什么重要

提供不改动主策略的轻量失败修正路线。

### 和当前项目的关系

High：可作为双臂 VLA 或 ACT 的附加纠错层。

### 主要局限

残差动作要经过安全限幅，避免真机接触中的突然修正。

### 摘要证据

官方摘要/论文页; https://proceedings.iclr.cc/paper_files/paper/2025/hash/45c361d4117d598d4bb6568b407e9ac9-Abstract-Conference.html; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
