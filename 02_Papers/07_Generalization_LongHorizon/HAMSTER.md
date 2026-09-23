# HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation

## Basic Information（基本信息）

- Title: HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation
- Year: 2025
- Venue / Source: ICLR
- Publication Status: ICLR 2025 Conference
- CCF Level: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Type: Method Paper
- Category: VLA / Robot Foundation Models / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation
- Subcategory: VLA / Robot Foundation Models; Robot Manipulation / IL / Diffusion
- Priority: P0

## Classification

- Primary Category: Generalization / Long-Horizon
- Categories: VLA; Robot Manipulation; Diffusion / Flow / IL / RL; Generalization / Long-Horizon
- Subcategories: VLA / Robot Foundation Models; Robot Manipulation / IL / Diffusion
- Tags: Unknown

## Links（链接）

- Official Paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/3bfee3bc6639c36e6e7b058db909f760-Abstract-Conference.html
- arXiv: 待补充
- Project Page: https://hamster-robot.github.io/
- Official GitHub: 待补充

## Code（代码状态）

- Code Status: Unknown
- Checkpoint: 待补充
- Dataset Released: Unknown

## Embodiment（机器人形态）

- Single Arm / Bimanual / Dexterous Hand / Gripper: Single Arm / Parallel Gripper
- Real Robot: Yes

## Why Collected（为什么被收录）

Abstract reports real robot experiments and multiple axes of generalization.

## Verification（待核验）

- [x] Venue 已确认
- [ ] CCF 等级已确认
- [x] Official Paper 已确认
- [ ] Official GitHub 已确认
- [ ] Code 可运行性已确认
- [x] 是否真机已确认

## Citation Metrics

- Citation Count: 1
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4407384835
- OpenAlex Work: https://openalex.org/W4407384835

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
https://proceedings.iclr.cc/paper_files/paper/2025/hash/3bfee3bc6639c36e6e7b058db909f760-Abstract-Conference.html; https://hamster-robot.github.io/

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

- [[02_Papers/01_VLA/Actions_as_Language|Actions_as_Language]] — [arXiv full-text bibliography item 41](https://arxiv.org/html/2509.22195#bib.bib41)
- [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective|A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective]] — [arXiv full-text bibliography item 190](https://arxiv.org/html/2507.01925#bib.bib190)
- [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI|A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]] — [arXiv full-text bibliography item 589](https://arxiv.org/html/2405.14093#bib.bib589)
- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]] — [arXiv full-text bibliography item 827](https://arxiv.org/html/2510.10903#bib.bib827)

### Related Work

- [[02_Papers/01_VLA/SayCan|SayCan]] — 两者都用高层动作结构处理长任务，可比较显式可执行性判断与子目标表示。

## 快速摘要

### 研究问题

开放世界操作需要利用基础模型知识，但机器人动作数据昂贵。

### 之前方法的问题

高层 VLM 不适合直接生成精细控制，低层策略又缺少广泛语义知识。

### 核心思路

HAMSTER 将高层任务理解与低层动作控制分工，降低双方负担。

### 输入

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 输出 / 动作

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 数据集 / Benchmark

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 主要结果

论文摘要报告该分层设计改善任务执行；统一数字需查实验表。

### 为什么重要

是比较分层规划和端到端 VLA 的阅读入口。

### 和当前项目的关系

High：双臂普通夹爪可能需要高层分工和低层安全控制。

### 主要局限

高低层接口不一致会造成目标误解或执行失败。

### 摘要证据

官方摘要/论文页; https://proceedings.iclr.cc/paper_files/paper/2025/hash/3bfee3bc6639c36e6e7b058db909f760-Abstract-Conference.html; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
