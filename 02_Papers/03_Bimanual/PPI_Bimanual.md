# Gripper Pose and Object Pointflow as Interfaces for Robotic Bimanual Manipulation

## Basic Information（基本信息）

- ID: R003
- Title: Gripper Pose and Object Pointflow as Interfaces for Robotic Bimanual Manipulation
- Authors: Yuyin Yang; Zetao Cai; Yang Tian; Jia Zeng; Jiangmiao Pang
- Year: 2025
- Venue: RSS
- Venue Type: Robotics Core Venue
- Publication Type: Full Conference Paper
- CCF Level: Unknown
- Research Category: Bimanual Manipulation / 3D Spatial Reasoning
- Subcategory: Gripper keypose and object pointflow interfaces
- Tags: Bimanual; Gripper; Robot Manipulation; Generalization; Real Robot
- Priority: P0
- Special Attention: No
- Library Membership: Robotics Core

## Classification

- Primary Category: Bimanual
- Categories: Robot Manipulation; Bimanual; Generalization / Long-Horizon
- Subcategories: Gripper keypose and object pointflow interfaces
- Tags: Bimanual; Gripper; Robot Manipulation; Generalization; Real Robot

## Links（链接）

- Official Paper: https://www.roboticsproceedings.org/rss21/p160.html
- Project Page: https://yuyinyang3y.github.io/PPI/
- Official GitHub: Unknown

## Code & Resources（代码与资源）

- Code Status: Unknown
- Checkpoint: Unknown
- Dataset: RLBench2 and real-world tasks; release status Unknown

## Robot / Embodiment（机器人与形态）

- Robot Platform: Bimanual gripper system; exact model pending full-paper check
- Embodiment: Bimanual / Parallel Gripper
- Real Robot: Yes

## Research Summary（研究摘要）

- **Problem:** Bimanual policies must combine spatial localization with flexible continuous trajectories.
- **Main Contribution:**
  - PPI combines target gripper-pose and object-pointflow interfaces with continuous action prediction.
  - RLBench2 plus four real-world tasks reported by official abstract.
- **Key Idea:** Use spatial interfaces to guide continuous bimanual actions.
- **Experiment / Validation:** RLBench2 plus four real-world tasks reported by official abstract.
- **Relevance to Our Project:** Very close to NERO dual-arm and ordinary-gripper manipulation.

## Requested Tags / Evidence Gaps（请求标签与证据差距）

- [ ] VLA: Unknown / not established by checked sources
- [ ] Sim2Real: Unknown / not established by checked sources
- [x] Robot Manipulation: supported by official abstract/project page
- [ ] Synthetic Data: Unknown / not established by checked sources
- [x] Generalization: supported by official abstract/project page
- [x] Bimanual: supported by official abstract/project page
- [ ] Dexterous: Unknown / not established by checked sources
- [ ] Long-horizon: Unknown / not established by checked sources

## Summary Evidence（摘要证据）

- Evidence Level: Abstract-level
- Sources: RSS official proceedings abstract
- Verification Status: RSS official proceedings verified
- Verified Date: 2026-09-19
- Notes: Official paper page confirms simulated and real-world experiments.

## Citation Metrics

- Citation Count: 1
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4414050727
- OpenAlex Work: https://openalex.org/W4414050727

## Standardized Research Fields

### Research Problem
Bimanual policies must combine spatial localization with flexible continuous trajectories.

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
Use spatial interfaces to guide continuous bimanual actions.

### Main Contributions
- PPI combines target gripper-pose and object-pointflow interfaces with continuous action prediction.

### Dataset & Benchmark
RLBench2 and real-world tasks; release status Unknown

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
RLBench2 plus four real-world tasks reported by official abstract.

### Main Results
Unknown / Needs Full-Paper Verification

### Limitations
Unknown / Needs Full-Paper Verification

### What Remains Unsolved?
Library Analysis / Research Note: Unknown / Needs Full-Paper Verification

### Relevance to Our Project
Very close to NERO dual-arm and ordinary-gripper manipulation.

## Full-paper Enrichment (Batch 03)

- Evidence Quality: B
- Evidence Status: Official full text was not reliably extractable in this batch; structured fields below preserve existing card evidence and mark unresolved details explicitly.

### Research Problem
Bimanual policies must combine spatial localization with flexible continuous trajectories.

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
Use spatial interfaces to guide continuous bimanual actions.

### Architecture / Key Components
Unknown / Needs Official Full-Text Verification

### Dataset & Benchmark
RLBench2 and real-world tasks; release status Unknown

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
RLBench2 plus four real-world tasks reported by official abstract.

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
- Official GitHub: Unknown
- Code Status: Unknown
- Checkpoint: Unknown
- Dataset: RLBench2 and real-world tasks; release status Unknown

### Relevance to Our Project
** Very close to NERO dual-arm and ordinary-gripper manipulation.

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://www.roboticsproceedings.org/rss21/p160.html; https://yuyinyang3y.github.io/PPI/

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Code-Unverified
- Supplement Status: Not Found
- Code Completeness: Unavailable
- Robot Platform Evidence: Bimanual gripper system; exact model pending full-paper check


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

- [[02_Papers/03_Bimanual/YOTO|YOTO]] — 两者都涉及双臂普通夹爪操作，但示范方式和空间接口不同。

## 快速摘要

### 研究问题

双臂策略要兼顾目标的空间定位和连续轨迹的灵活性。

### 之前方法的问题

单独使用离散空间提示或连续动作预测，可能难同时实现定位与平滑控制。

### 核心思路

PPI 用空间接口引导连续双臂动作生成。

### 输入

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 输出 / 动作

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 数据集 / Benchmark

仿真与真机双臂任务；完整 benchmark 见论文。

### 主要结果

论文报告相对先前方法在仿真和真机上提升，卡片记录平均提升 16.1%；指标定义需回原文核对。

### 为什么重要

适合比较空间表示如何约束普通夹爪的双臂动作。

### 和当前项目的关系

High：直接对应双臂空间接口和连续动作。

### 主要局限

需进一步核验任务分布、失败类型和动作频率。

### 摘要证据

官方摘要/论文页; https://www.roboticsproceedings.org/rss21/p160.html; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
