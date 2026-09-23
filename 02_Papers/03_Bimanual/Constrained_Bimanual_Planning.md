# Constrained Bimanual Planning with Analytic Inverse Kinematics

## Basic Information（基本信息）

- ID: R006
- Title: Constrained Bimanual Planning with Analytic Inverse Kinematics
- Authors: Thomas Cohn; Seiji Shaw; Max Simchowitz; Russ Tedrake
- Year: 2024
- Venue: ICRA
- Venue Type: Robotics Core Venue
- Publication Type: Full Conference Paper
- CCF Level: Unknown
- Research Category: Bimanual Manipulation / Motion Planning
- Subcategory: Analytic IK parameterization
- Tags: Bimanual; Motion Planning; Collision Avoidance; Real Robot
- Priority: P1
- Special Attention: No
- Library Membership: Robotics Core

## Classification

- Primary Category: Bimanual
- Categories: Robot Manipulation; Bimanual
- Subcategories: Analytic IK parameterization
- Tags: Bimanual; Motion Planning; Collision Avoidance; Real Robot

## Links（链接）

- Official Paper: https://ieeexplore.ieee.org/document/10610675/
- Project Page: https://tommycohn.com/Bimanual-Web/index.html
- Official GitHub: https://github.com/cohnt/constrained-bimanual-planning-example

## Code & Resources（代码与资源）

- Code Status: Released
- Checkpoint: Not applicable
- Dataset: Not applicable

## Robot / Embodiment（机器人与形态）

- Robot Platform: Dual robot arms; exact model pending full-paper check
- Embodiment: Bimanual / Gripper
- Real Robot: Yes

## Research Summary（研究摘要）

- **Problem:** Planning while maintaining a fixed transform between two end effectors creates difficult equality constraints.
- **Main Contribution:**
  - Uses analytic inverse kinematics to parameterize a lower-dimensional feasible space compatible with existing planners.
  - Official paper/project materials include bimanual hardware planning examples.
- **Key Idea:** Make the constrained bimanual manifold directly searchable.
- **Experiment / Validation:** Official paper/project materials include bimanual hardware planning examples.
- **Relevance to Our Project:** Useful for safe dual-arm constraints and planner-policy integration.

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
- Sources: IEEE Xplore abstract; official project page
- Verification Status: IEEE Xplore ICRA record verified
- Verified Date: 2026-09-19
- Notes: Planning-focused rather than end-to-end policy learning.

## Citation Metrics

- Citation Count: 11
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4401415458
- OpenAlex Work: https://openalex.org/W4401415458

## Standardized Research Fields

### Research Problem
Planning while maintaining a fixed transform between two end effectors creates difficult equality constraints.

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
Make the constrained bimanual manifold directly searchable.

### Main Contributions
- Uses analytic inverse kinematics to parameterize a lower-dimensional feasible space compatible with existing planners.

### Dataset & Benchmark
Not applicable

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Official paper/project materials include bimanual hardware planning examples.

### Main Results
Unknown / Needs Full-Paper Verification

### Limitations
Unknown / Needs Full-Paper Verification

### What Remains Unsolved?
Library Analysis / Research Note: Unknown / Needs Full-Paper Verification

### Relevance to Our Project
Useful for safe dual-arm constraints and planner-policy integration.

## Full-paper Enrichment (Batch 07)

- Evidence Quality: B
- Evidence Status: Official full text was not reliably extractable in this batch; structured fields below preserve existing card evidence and mark unresolved details explicitly.

### Research Problem
Planning while maintaining a fixed transform between two end effectors creates difficult equality constraints.

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
Make the constrained bimanual manifold directly searchable.

### Architecture / Key Components
Unknown / Needs Official Full-Text Verification

### Dataset & Benchmark
Not applicable

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Official paper/project materials include bimanual hardware planning examples.

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
- Official GitHub: https://github.com/cohnt/constrained-bimanual-planning-example
- Code Status: Released
- Checkpoint: Not applicable
- Dataset: Not applicable

### Relevance to Our Project
** Useful for safe dual-arm constraints and planner-policy integration.

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://ieeexplore.ieee.org/document/10610675/; https://tommycohn.com/Bimanual-Web/index.html; https://github.com/cohnt/constrained-bimanual-planning-example

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Fulltext-Unavailable
- Supplement Status: Not Found
- Code Completeness: Mostly Complete
- Robot Platform Evidence: Dual robot arms; exact model pending full-paper check

## Deep Enrichment (Full Text Read: 2026-09-22)
- Evidence Quality: A
- Fulltext Checked: Yes — arXiv HTML 2309.08770 and MIT Robotics Center PDF inspected.
- Supplement Status: Not Applicable.
- Method: analytic inverse-kinematics parameterizes the fixed relative transform between end effectors, reducing constrained planning to a lower-dimensional positive-measure manifold.
- Experiments / Baselines: sampling-based planners, trajectory optimizers and convex inner-approximation planners are evaluated under the analytic parameterization.
- Results / Failure Cases: valid bimanual plans are produced while avoiding measure-zero sampling; failures remain tied to collision constraints and robot-specific IK assumptions.
- Limitations: Author-stated — analytic solutions depend on arm kinematic classes; Library Analysis — learned perception and uncertain contact are outside scope.
- Remaining Gap / Idea: pair analytic constraint manifolds with learned VLA action proposals.
- Evidence Sources: https://arxiv.org/html/2309.08770 ; https://groups.csail.mit.edu/robotics-center/public_papers/Cohn23a.pdf ; https://github.com/cohnt/constrained-bimanual-planning-example.
- Evidence Upgrade Status: A-Upgraded

## Citation Relations

### References in Library

- No verified in-library citation edge yet.

### Cited By in Library

- No verified in-library citation edge yet.

### Related Work

- No curated content relation yet.

## 快速摘要

### 研究问题

双臂共同操作时，两只末端之间常需保持固定相对位姿。

### 之前方法的问题

这种等式约束使普通规划器难以高效搜索可行动作。

### 核心思路

直接在满足双臂相对位姿约束的运动流形上搜索轨迹。

### 输入

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 输出 / 动作

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 数据集 / Benchmark

约束双臂规划场景；具体 benchmark 需核对正文。

### 主要结果

已核验摘要未提供可安全复述的统一量化结果。

### 为什么重要

为普通夹爪共同搬运物体提供几何约束基线。

### 和当前项目的关系

High：双臂同步和共同约束是本项目基础问题。

### 主要局限

需评估模型化固定相对位姿与真实滑动、形变之间的差异。

### 摘要证据

官方摘要/论文页; https://arxiv.org/html/2309.08770; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
