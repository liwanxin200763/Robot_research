# Real-Time Coordination of Multiple Robotic Arms With Reactive Trajectory Modulation

## Basic Information（基本信息）

- ID: R008
- Title: Real-Time Coordination of Multiple Robotic Arms With Reactive Trajectory Modulation
- Authors: Unknown
- Year: 2024
- Venue: T-RO
- Venue Type: Robotics Core Journal
- Publication Type: Journal Article
- CCF Level: Unknown
- Research Category: Bimanual / Multi-arm Coordination
- Subcategory: Reactive trajectory modulation from demonstrations
- Tags: Bimanual; Multi-arm; Demonstration; Collision Avoidance; Real Robot
- Priority: P1
- Special Attention: No
- Library Membership: Robotics Core

## Classification

- Primary Category: Bimanual
- Categories: Robot Manipulation; Bimanual
- Subcategories: Reactive trajectory modulation from demonstrations
- Tags: Bimanual; Multi-arm; Demonstration; Collision Avoidance; Real Robot

## Links（链接）

- Official Paper: https://ieeexplore.ieee.org/document/10758213/
- Project Page: Unknown
- Official GitHub: Unknown

## Code & Resources（代码与资源）

- Code Status: Unknown
- Checkpoint: Unknown
- Dataset: Single-demonstration trajectories; release status Unknown

## Robot / Embodiment（机器人与形态）

- Robot Platform: Multiple robotic arms
- Embodiment: Multi-arm / Gripper
- Real Robot: Yes

## Research Summary（研究摘要）

- **Problem:** Multiple arms need online trajectory adaptation and collision avoidance in shared workspaces.
- **Main Contribution:**
  - Combines learned movement primitives with reactive multi-arm coordination.
  - Experiments with multiple arms in a shared workspace are reported.
- **Key Idea:** Modulate demonstrated trajectories online while coordinating shared-space motion.
- **Experiment / Validation:** Experiments with multiple arms in a shared workspace are reported.
- **Relevance to Our Project:** Directly relevant to NERO dual-arm coordination and collision-aware trajectory execution.

## Requested Tags / Evidence Gaps（请求标签与证据差距）

- [ ] VLA: Unknown / not established by checked sources
- [ ] Sim2Real: Unknown / not established by checked sources
- [ ] Robot Manipulation: Unknown / not established by checked sources
- [ ] Synthetic Data: Unknown / not established by checked sources
- [ ] Generalization: Unknown / not established by checked sources
- [x] Bimanual: supported by official abstract/project page
- [ ] Dexterous: Unknown / not established by checked sources
- [ ] Long-horizon: Unknown / not established by checked sources

## Summary Evidence（摘要证据）

- Evidence Level: Abstract-level
- Sources: IEEE Xplore abstract
- Verification Status: IEEE Xplore T-RO record verified; authors pending
- Verified Date: 2026-09-19
- Notes: Published online in 2024, assigned to T-RO volume 41.

## Citation Metrics

- Citation Count: 10
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4404520558
- OpenAlex Work: https://openalex.org/W4404520558

## Standardized Research Fields

### Research Problem
Multiple arms need online trajectory adaptation and collision avoidance in shared workspaces.

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
Modulate demonstrated trajectories online while coordinating shared-space motion.

### Main Contributions
- Combines learned movement primitives with reactive multi-arm coordination.

### Dataset & Benchmark
Single-demonstration trajectories; release status Unknown

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Experiments with multiple arms in a shared workspace are reported.

### Main Results
Unknown / Needs Full-Paper Verification

### Limitations
Unknown / Needs Full-Paper Verification

### What Remains Unsolved?
Library Analysis / Research Note: Unknown / Needs Full-Paper Verification

### Relevance to Our Project
Directly relevant to NERO dual-arm coordination and collision-aware trajectory execution.

## Full-paper Enrichment (Batch 03)

- Evidence Quality: B
- Evidence Status: Official full text was not reliably extractable in this batch; structured fields below preserve existing card evidence and mark unresolved details explicitly.

### Research Problem
Multiple arms need online trajectory adaptation and collision avoidance in shared workspaces.

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
Modulate demonstrated trajectories online while coordinating shared-space motion.

### Architecture / Key Components
Unknown / Needs Official Full-Text Verification

### Dataset & Benchmark
Single-demonstration trajectories; release status Unknown

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Experiments with multiple arms in a shared workspace are reported.

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
- Dataset: Single-demonstration trajectories; release status Unknown

### Relevance to Our Project
** Directly relevant to NERO dual-arm coordination and collision-aware trajectory execution.

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://ieeexplore.ieee.org/document/10758213/

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Code-Unverified
- Supplement Status: Not Found
- Code Completeness: Unavailable
- Robot Platform Evidence: Multiple robotic arms


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

多只机械臂共享工作空间时，需要在线修改轨迹并避免碰撞。

### 之前方法的问题

离线示范轨迹不能保证在动态变化下仍安全可行。

### 核心思路

对示范轨迹做在线调制，并在共享空间中协调多臂运动。

### 输入

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 输出 / 动作

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 数据集 / Benchmark

多臂协调场景；具体任务和平台需查正文。

### 主要结果

已核验摘要未给可安全复述的统一量化结果。

### 为什么重要

为双臂策略外部增加安全协调层提供参照。

### 和当前项目的关系

High：普通夹爪双臂真机必须处理共享空间碰撞。

### 主要局限

需验证在线修正是否破坏原策略的任务意图。

### 摘要证据

OpenAlex 索引摘要; https://api.openalex.org/works/W4404520558; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
