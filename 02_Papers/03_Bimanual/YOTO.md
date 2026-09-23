# You Only Teach Once: Learn One-Shot Bimanual Robotic Manipulation from Video Demonstrations

## Basic Information（基本信息）

- ID: R002
- Title: You Only Teach Once: Learn One-Shot Bimanual Robotic Manipulation from Video Demonstrations
- Authors: Huayi Zhou; Ruixiang Wang; Yunxin Tai; Yueci Deng; Guiliang Liu; Kui Jia
- Year: 2025
- Venue: RSS
- Venue Type: Robotics Core Venue
- Publication Type: Full Conference Paper
- CCF Level: Unknown
- Research Category: Bimanual Manipulation / Imitation Learning
- Subcategory: Video demonstration / bimanual diffusion policy
- Tags: Bimanual; Human Video; Imitation Learning; Diffusion Policy; Generalization; Long-horizon
- Priority: P0
- Special Attention: No
- Library Membership: Robotics Core

## Classification

- Primary Category: Bimanual
- Categories: Robot Manipulation; Bimanual; Diffusion / Flow / IL / RL; Generalization / Long-Horizon; Data / Teleoperation
- Subcategories: Video demonstration / bimanual diffusion policy
- Tags: Bimanual; Human Video; Imitation Learning; Diffusion Policy; Generalization; Long-horizon

## Links（链接）

- Official Paper: https://www.roboticsproceedings.org/rss21/p149.html
- Project Page: https://hnuzhy.github.io/projects/YOTO
- Official GitHub: Unknown

## Code & Resources（代码与资源）

- Code Status: Unknown
- Checkpoint: Unknown
- Dataset: Generated demonstrations; release status Unknown

## Robot / Embodiment（机器人与形态）

- Robot Platform: Dual robot arms; exact platform pending full-paper check
- Embodiment: Bimanual / Gripper
- Real Robot: Yes

## Research Summary（研究摘要）

- **Problem:** Learning coordinated bimanual skills with low demonstration cost.
- **Main Contribution:**
  - Extracts bimanual action patterns from a binocular human video and generates varied demonstrations for a bimanual diffusion policy.
  - Official abstract reports five long-horizon bimanual tasks.
- **Key Idea:** One-shot human video becomes structured keyframe trajectories and scalable robot demonstrations.
- **Experiment / Validation:** Official abstract reports five long-horizon bimanual tasks.
- **Relevance to Our Project:** Direct match to bimanual manipulation, human demonstration and diffusion-policy training.

## Requested Tags / Evidence Gaps（请求标签与证据差距）

- [ ] VLA: Unknown / not established by checked sources
- [ ] Sim2Real: Unknown / not established by checked sources
- [ ] Robot Manipulation: Unknown / not established by checked sources
- [ ] Synthetic Data: Unknown / not established by checked sources
- [x] Generalization: supported by official abstract/project page
- [x] Bimanual: supported by official abstract/project page
- [ ] Dexterous: Unknown / not established by checked sources
- [x] Long-horizon: supported by official abstract/project page

## Summary Evidence（摘要证据）

- Evidence Level: Abstract-level
- Sources: RSS official proceedings abstract
- Verification Status: RSS official proceedings verified
- Verified Date: 2026-09-19
- Notes: Five long-horizon tasks are reported in the official abstract.

## Citation Metrics

- Citation Count: 7
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4414050937
- OpenAlex Work: https://openalex.org/W4414050937

## Standardized Research Fields

### Research Problem
Learning coordinated bimanual skills with low demonstration cost.

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
One-shot human video becomes structured keyframe trajectories and scalable robot demonstrations.

### Main Contributions
- Extracts bimanual action patterns from a binocular human video and generates varied demonstrations for a bimanual diffusion policy.

### Dataset & Benchmark
Generated demonstrations; release status Unknown

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Official abstract reports five long-horizon bimanual tasks.

### Main Results
Unknown / Needs Full-Paper Verification

### Limitations
Unknown / Needs Full-Paper Verification

### What Remains Unsolved?
Library Analysis / Research Note: Unknown / Needs Full-Paper Verification

### Relevance to Our Project
Direct match to bimanual manipulation, human demonstration and diffusion-policy training.

## Full-paper Enrichment (Batch 03)

- Evidence Quality: B
- Evidence Status: Official full text was not reliably extractable in this batch; structured fields below preserve existing card evidence and mark unresolved details explicitly.

### Research Problem
Learning coordinated bimanual skills with low demonstration cost.

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
One-shot human video becomes structured keyframe trajectories and scalable robot demonstrations.

### Architecture / Key Components
Unknown / Needs Official Full-Text Verification

### Dataset & Benchmark
Generated demonstrations; release status Unknown

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Official abstract reports five long-horizon bimanual tasks.

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
- Dataset: Generated demonstrations; release status Unknown

### Relevance to Our Project
** Direct match to bimanual manipulation, human demonstration and diffusion-policy training.

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://www.roboticsproceedings.org/rss21/p149.html; https://hnuzhy.github.io/projects/YOTO

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Code-Unverified
- Supplement Status: Not Found
- Code Completeness: Unavailable
- Robot Platform Evidence: Dual robot arms; exact platform pending full-paper check


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

- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]] — [arXiv full-text bibliography item 1073](https://arxiv.org/html/2510.10903#bib.bib1073)

### Related Work

- [[02_Papers/03_Bimanual/PPI_Bimanual|PPI_Bimanual]] — 两者都涉及双臂普通夹爪操作，但示范方式和空间接口不同。

## 快速摘要

### 研究问题

低成本示范条件下，如何学会协调的双臂技能。

### 之前方法的问题

一段人类视频不能直接提供机器人两臂的连续可执行动作。

### 核心思路

把单段人类视频转换为结构化关键帧轨迹，并扩展成机器人示范。

### 输入

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 输出 / 动作

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 数据集 / Benchmark

论文评估五项复杂的长时序双臂任务。

### 主要结果

作者报告可模仿五项双臂任务，并对视觉和空间变化有一定泛化；具体数值需看原文。

### 为什么重要

可帮助研究 Human Video → Robot Action 的数据成本。

### 和当前项目的关系

High：与双臂普通夹爪和低示范预算直接相关。

### 主要局限

人类视频关键帧到真机连续控制仍需验证可达性与接触安全。

### 摘要证据

官方摘要/论文页; https://www.roboticsproceedings.org/rss21/p149.html; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
