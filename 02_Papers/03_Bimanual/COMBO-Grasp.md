# COMBO-Grasp: Learning Constraint-Based Manipulation for Bimanual Occluded Grasping

## Basic Information（基本信息）

- Title: COMBO-Grasp: Learning Constraint-Based Manipulation for Bimanual Occluded Grasping
- Year: 2025
- Venue / Source: CoRL
- Publication Status: Formal PMLR v305 / CoRL 2025
- CCF Level: Not CCF A (robotics venue extension; CCF row not asserted)
- Type: Method Paper
- Category: Bimanual Manipulation / Robot Manipulation
- Subcategory: Bimanual
- Priority: P1

## Classification

- Primary Category: Bimanual
- Categories: Robot Manipulation; Bimanual
- Subcategories: Bimanual
- Tags: Unknown

## Links（链接）

- Official Paper: https://proceedings.mlr.press/v305/yamada25a.html
- arXiv: 待补充
- Project Page: 待补充
- Official GitHub: 待补充

## Code（代码状态）

- Code Status: Unknown
- Checkpoint: 待补充
- Dataset Released: Unknown

## Embodiment（机器人形态）

- Single Arm / Bimanual / Dexterous Hand / Gripper: Bimanual / Parallel Gripper
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
- Citation Source Identifier: https://openalex.org/W4407569722
- OpenAlex Work: https://openalex.org/W4407569722

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
https://proceedings.mlr.press/v305/yamada25a.html

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Fulltext-Unavailable
- Supplement Status: Not Found
- Code Completeness: Unknown
- Robot Platform Evidence: Unknown

## Deep Enrichment (Full Text Read: 2026-09-22)
- Evidence Quality: A
- Fulltext Checked: Yes — arXiv HTML 2502.08054 and OpenReview paper inspected.
- Supplement Status: Available - Verified.
- Method: coordinated constraint policy generates stabilizing poses; RL grasping policy reorients and grasps the occluded target, with value-function-guided coordination and teacher-student point-cloud distillation.
- Dataset / Benchmark: simulated and real bimanual occluded-grasping tasks, including unseen objects.
- Results: reported success improvements over competitive baselines and successful unseen-object generalization (abstract and Sec. 5).
- Ablation / Failure Cases: coordination/value-guidance and distillation are isolated; failures arise from kinematic infeasibility, occlusion and unstable support poses.
- Limitations: Author-stated — RL complexity and sim-to-real transfer; Library Analysis — broader long-horizon tasks remain open.
- Remaining Gap / Idea: combine constraint policy with VLA grounding for recovery from failed grasps.
- Evidence Sources: https://arxiv.org/html/2502.08054 ; https://openreview.net/pdf?id=xpEjjGC82v.
- Evidence Upgrade Status: A-Upgraded

## Citation Relations

### References in Library

- [[02_Papers/03_Bimanual/ALOHA_Unleashed|ALOHA_Unleashed]] — [arXiv full-text bibliography item 45](https://arxiv.org/html/2502.08054#bib.bib45)

### Cited By in Library

- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]] — [arXiv full-text bibliography item 244](https://arxiv.org/html/2510.10903#bib.bib244)

### Related Work

- No curated content relation yet.

## 快速摘要

### 研究问题

目标抓取位姿可能被障碍物遮挡，单臂难以直接到达。

### 之前方法的问题

只规划目标夹爪的直接抓取，缺少另一只手协助移动物体/障碍物。

### 核心思路

COMBO-Grasp 用两个协调策略处理遮挡抓取，让双臂先调整环境再完成目标抓取。

### 输入

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 输出 / 动作

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 数据集 / Benchmark

论文的遮挡抓取评测任务；具体平台和基线见实验章节。

### 主要结果

官方摘要报告成功率优于所比较基线，并对未见设置有一定泛化；未给统一数值。

### 为什么重要

展示双臂协作不只是同步抓取，也可以分工解除遮挡。

### 和当前项目的关系

High：适合普通夹爪双臂的支撑、移动与抓取任务。

### 主要局限

需进一步核验复杂杂乱场景与真机接触安全边界。

### 摘要证据

官方摘要/论文页; https://arxiv.org/html/2502.08054; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
