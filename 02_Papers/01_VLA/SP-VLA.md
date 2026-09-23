# SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration

## Basic Information（基本信息）

- Title: SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration
- Year: 2026
- Venue / Source: ICLR
- Publication Status: ICLR 2026 Conference
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

- Official Paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/4072543747a14bbed76284cf2c04b9e9-Abstract-Conference.html
- arXiv: 待补充
- Project Page: 待补充
- Official GitHub: 待补充

## Code（代码状态）

- Code Status: Unknown
- Checkpoint: 待补充
- Dataset Released: Unknown

## Embodiment（机器人形态）

- Single Arm / Bimanual / Dexterous Hand / Gripper: Unknown
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

- Citation Count: 0
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4417536563
- OpenAlex Work: https://openalex.org/W4417536563

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
- Official GitHub: 待补充
- Code Status: Unknown
- Checkpoint: 待补充
- Dataset: Unknown

### Relevance to Our Project
Unknown / Needs project-specific review

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://proceedings.iclr.cc/paper_files/paper/2026/hash/4072543747a14bbed76284cf2c04b9e9-Abstract-Conference.html

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Fulltext-Unavailable
- Supplement Status: Not Found
- Code Completeness: Unknown
- Robot Platform Evidence: Unknown

## Deep Enrichment (Full Text Read: 2026-09-22)
- Evidence Quality: A
- Fulltext Checked: Yes — arXiv HTML 2506.12723v3, Secs. 3–5 and Appendix A inspected.
- Supplement Status: Available - Verified.
- Method: action-aware model scheduling switches between a full VLA and lightweight generator; spatial-semantic dual-aware token pruning removes redundant tokens (Sec. 3).
- Results: 1.5× lossless acceleration on LIBERO, 2.4× on SimplerEnv, with up to 6% average performance gain (abstract, Sec. 4).
- Ablation: individual scheduling/pruning modules, latency/frequency, sensitivity and acceleration ratios are reported in Sec. 4 and App. A.2–A.5.
- Failure Cases / Limitations: action-type misclassification and over-pruning can hurt accuracy; Appendix A.6 records limitations.
- Remaining Gap / Idea: hardware-aware scheduling for high-frequency bimanual control.
- Evidence Sources: https://arxiv.org/html/2506.12723.
- Evidence Upgrade Status: A-Upgraded

## Citation Relations

### References in Library

- [[02_Papers/01_VLA/Octo|Octo]] — [arXiv full-text bibliography item 36](https://arxiv.org/html/2506.12723#bib.bib36)
- [[02_Papers/01_VLA/OpenVLA|OpenVLA]] — [arXiv full-text bibliography item 10](https://arxiv.org/html/2506.12723#bib.bib10)
- [[02_Papers/03_Bimanual/RDT-1B|RDT-1B]] — [arXiv full-text bibliography item 20](https://arxiv.org/html/2506.12723#bib.bib20)
- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open_X-Embodiment]] — [arXiv full-text bibliography item 25](https://arxiv.org/html/2506.12723#bib.bib25)

### Cited By in Library

- No verified in-library citation edge yet.

### Related Work

- No curated content relation yet.

## 快速摘要

### 研究问题

VLA 推理开销大，在线控制频率受限。

### 之前方法的问题

固定模型规模与统一 token 处理会浪费简单状态的计算。

### 核心思路

SP-VLA 联合进行模型调度与 token 剪枝，在不同状态分配不同推理计算量。

### 输入

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 输出 / 动作

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 数据集 / Benchmark

LIBERO、SimplerEnv 与论文列出的真机任务。

### 主要结果

论文报告 LIBERO 无损加速约 1.5 倍、SimplerEnv 约 2.4 倍；平均成功率变化需按论文设置理解。

### 为什么重要

为双臂 VLA 真机控制提供延迟优化方向。

### 和当前项目的关系

High：控制频率会影响双臂同步和失败恢复。

### 主要局限

剪枝造成的少数困难状态失误，需用真实任务失败案例检验。

### 摘要证据

官方摘要/论文页; https://arxiv.org/html/2506.12723; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
