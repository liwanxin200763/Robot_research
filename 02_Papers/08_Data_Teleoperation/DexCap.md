# DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation

## Basic Information（基本信息）

- ID: R004
- Title: DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation
- Authors: Chen Wang; Haochen Shi; Weizhuo Wang; Ruohan Zhang; Li Fei-Fei; Karen Liu
- Year: 2024
- Venue: RSS
- Venue Type: Robotics Core Venue
- Publication Type: Full Conference Paper
- CCF Level: Unknown
- Research Category: Dexterous Manipulation / Teleoperation
- Subcategory: Portable hand motion capture and imitation learning
- Tags: Dexterous; Human Demonstration; Teleoperation; Imitation Learning
- Priority: P1
- Special Attention: No
- Library Membership: Robotics Core

## Classification

- Primary Category: Data / Teleoperation
- Categories: Robot Manipulation; Dexterous; Diffusion / Flow / IL / RL; Data / Teleoperation
- Subcategories: Portable hand motion capture and imitation learning
- Tags: Dexterous; Human Demonstration; Teleoperation; Imitation Learning

## Links（链接）

- Official Paper: https://roboticsproceedings.org/rss20/p043.html
- Project Page: Unknown
- Official GitHub: Unknown

## Code & Resources（代码与资源）

- Code Status: Unknown
- Checkpoint: Unknown
- Dataset: Human hand mocap data; release status Unknown

## Robot / Embodiment（机器人与形态）

- Robot Platform: Dexterous robotic hand
- Embodiment: Dexterous Hand
- Real Robot: Yes

## Research Summary（研究摘要）

- **Problem:** Collecting detailed, portable human-hand demonstrations for dexterous robot learning.
- **Main Contribution:**
  - A wearable mocap system and a retargeting/imitation pipeline for dexterous policies.
  - Official paper describes robot-policy learning from collected mocap.
- **Key Idea:** Capture wrist and finger motion with environment-grounded 3D observations.
- **Experiment / Validation:** Official paper describes robot-policy learning from collected mocap.
- **Relevance to Our Project:** Useful for teleoperation/data-collection design; hardware differs from the current gripper setup.

## Requested Tags / Evidence Gaps（请求标签与证据差距）

- [ ] VLA: Unknown / not established by checked sources
- [ ] Sim2Real: Unknown / not established by checked sources
- [ ] Robot Manipulation: Unknown / not established by checked sources
- [ ] Synthetic Data: Unknown / not established by checked sources
- [ ] Generalization: Unknown / not established by checked sources
- [ ] Bimanual: Unknown / not established by checked sources
- [x] Dexterous: supported by official abstract/project page
- [ ] Long-horizon: Unknown / not established by checked sources

## Summary Evidence（摘要证据）

- Evidence Level: Abstract-level
- Sources: RSS official proceedings
- Verification Status: RSS official proceedings PDF and volume listing verified
- Verified Date: 2026-09-19
- Notes: Follow-up expansion topic; not the current ordinary-gripper main line.

## Citation Metrics

- Citation Count: Unknown
- Citation Source: OpenAlex (exact identity unresolved; API coverage may limit lookup)
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: Unknown (exact scholarly work unresolved)
- OpenAlex Work: Unknown

## Standardized Research Fields

### Research Problem
Collecting detailed, portable human-hand demonstrations for dexterous robot learning.

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
Capture wrist and finger motion with environment-grounded 3D observations.

### Main Contributions
- A wearable mocap system and a retargeting/imitation pipeline for dexterous policies.

### Dataset & Benchmark
Human hand mocap data; release status Unknown

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Official paper describes robot-policy learning from collected mocap.

### Main Results
Unknown / Needs Full-Paper Verification

### Limitations
Unknown / Needs Full-Paper Verification

### What Remains Unsolved?
Library Analysis / Research Note: Unknown / Needs Full-Paper Verification

### Relevance to Our Project
Useful for teleoperation/data-collection design; hardware differs from the current gripper setup.

## Full-paper Enrichment (Batch 05)

- Evidence Quality: B
- Evidence Status: Official full text was not reliably extractable in this batch; structured fields below preserve existing card evidence and mark unresolved details explicitly.

### Research Problem
Collecting detailed, portable human-hand demonstrations for dexterous robot learning.

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
Capture wrist and finger motion with environment-grounded 3D observations.

### Architecture / Key Components
Unknown / Needs Official Full-Text Verification

### Dataset & Benchmark
Human hand mocap data; release status Unknown

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Official paper describes robot-policy learning from collected mocap.

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
- Dataset: Human hand mocap data; release status Unknown

### Relevance to Our Project
** Useful for teleoperation/data-collection design; hardware differs from the current gripper setup.

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://roboticsproceedings.org/rss20/p043.html

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Code-Unverified
- Supplement Status: Not Found
- Code Completeness: Unavailable
- Robot Platform Evidence: Dexterous robotic hand

## Citation Relations

### References in Library

- No verified in-library citation edge yet.

### Cited By in Library

- [[02_Papers/03_Bimanual/ALOHA_Unleashed|ALOHA_Unleashed]] — [arXiv full-text bibliography item 44](https://arxiv.org/html/2410.13126#bib.bib44)
- [[02_Papers/03_Bimanual/AnyBimanual|AnyBimanual]] — [arXiv full-text bibliography item 56](https://arxiv.org/html/2412.06779#bib.bib56)
- [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective|A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective]] — [arXiv full-text bibliography item 320](https://arxiv.org/html/2507.01925#bib.bib320)
- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]] — [arXiv full-text bibliography item 1118](https://arxiv.org/html/2510.10903#bib.bib1118)

### Related Work

- No curated content relation yet.

## 快速摘要

### 研究问题

灵巧机器人学习缺少可携带、细节完整的人手示范。

### 之前方法的问题

只记录视频，难准确捕捉手腕、手指和环境的三维关系。

### 核心思路

DexCap 同步采集手腕与手指运动以及环境三维观测，形成可迁移的人手操作数据。

### 输入

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 输出 / 动作

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 数据集 / Benchmark

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 主要结果

作者报告在六项灵巧操作任务上验证采集与学习价值；具体数值需查正文。

### 为什么重要

提醒示范采集装置决定后续策略能学到什么。

### 和当前项目的关系

Medium：普通夹爪不需手指细节，但腕部和环境标定有用。

### 主要局限

人手示范迁移到普通夹爪仍需动作重定向。

### 摘要证据

官方摘要/论文页; https://roboticsproceedings.org/rss20/p043.html; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
