# Real-Time Robot Execution with Masked Action Chunking

## Basic Information（基本信息）

- Title: Real-Time Robot Execution with Masked Action Chunking
- Year: 2026
- Venue / Source: ICLR
- Publication Status: ICLR 2026 Conference
- CCF Level: A (CCF 7th edition; venue category not independently extracted from official PDF)
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

- Official Paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/c35834443b7881e782e52b3519fe27c7-Abstract-Conference.html
- arXiv: 待补充
- Project Page: 待补充
- Official GitHub: 待补充

## Code（代码状态）

- Code Status: Unknown
- Checkpoint: 待补充
- Dataset Released: Unknown

## Embodiment（机器人形态）

- Single Arm / Bimanual / Dexterous Hand / Gripper: Parallel Gripper
- Real Robot: Mixed

## Why Collected（为什么被收录）

Abstract reports simulation and real-world evaluations.

## Verification（待核验）

- [x] Venue 已确认
- [ ] CCF 等级已确认
- [x] Official Paper 已确认
- [ ] Official GitHub 已确认
- [ ] Code 可运行性已确认
- [x] 是否真机已确认

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
https://proceedings.iclr.cc/paper_files/paper/2026/hash/c35834443b7881e782e52b3519fe27c7-Abstract-Conference.html

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

机器人必须实时响应，但动作块策略可能错过中途变化。

### 之前方法的问题

固定动作块执行快，却不容易及时修正已预测动作。

### 核心思路

REMAC 用 masked action chunking 学习对预训练策略动作的修正。

### 输入

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 输出 / 动作

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 数据集 / Benchmark

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 主要结果

作者报告仿真与真机中执行更快，并保持任务表现；具体延迟和成功率需查论文。

### 为什么重要

直接对应普通夹爪真机的实时执行与修正。

### 和当前项目的关系

High：可比较动作块长度、控制频率和失败恢复。

### 主要局限

在线修正是否产生不安全突变需在控制器层验证。

### 摘要证据

官方摘要/论文页; https://proceedings.iclr.cc/paper_files/paper/2026/hash/c35834443b7881e782e52b3519fe27c7-Abstract-Conference.html; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
