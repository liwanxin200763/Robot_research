# Evaluating the Effect of State and Action Selection on In-Hand Manipulation Performance for Transferability

## Basic Information（基本信息）

- ID: R009
- Title: Evaluating the Effect of State and Action Selection on In-Hand Manipulation Performance for Transferability
- Authors: Nigel Swenson; Jeremiah Goddard; Xiaoli Z. Fern; Ravi Balasubramanian; Cindy Grimm
- Year: 2025
- Venue: RA-L
- Venue Type: Robotics Core Journal
- Publication Type: Journal Letter
- CCF Level: Unknown
- Research Category: Dexterous Manipulation / Sim2Real / Reinforcement Learning
- Subcategory: State/action-space transferability
- Tags: Dexterous; Sim2Real; Reinforcement Learning; Cross-Embodiment
- Priority: P2
- Special Attention: No
- Library Membership: Robotics Core

## Classification

- Primary Category: Dexterous
- Categories: Robot Manipulation; Dexterous; Sim2Real; Diffusion / Flow / IL / RL; Generalization / Long-Horizon
- Subcategories: State/action-space transferability
- Tags: Dexterous; Sim2Real; Reinforcement Learning; Cross-Embodiment

## Links（链接）

- Official Paper: https://ieeexplore.ieee.org/document/10955245/
- Project Page: Unknown
- Official GitHub: Unknown

## Code & Resources（代码与资源）

- Code Status: Unknown
- Checkpoint: Unknown
- Dataset: Two manipulation tasks; release status Unknown

## Robot / Embodiment（机器人与形态）

- Robot Platform: Multiple hand geometries
- Embodiment: Dexterous Hand
- Real Robot: Mixed

## Research Summary（研究摘要）

- **Problem:** State and action representations may not transfer across reality gaps or hand geometries.
- **Main Contribution:**
  - Studies representation choices across two in-hand tasks and two transfer settings.
  - Two exemplar tasks and sim-to-real/cross-hand transfer are reported.
- **Key Idea:** Reduce hand-specific state information to improve transfer robustness.
- **Experiment / Validation:** Two exemplar tasks and sim-to-real/cross-hand transfer are reported.
- **Relevance to Our Project:** Useful for later dexterous-hand extension and embodiment-agnostic action design.

## Requested Tags / Evidence Gaps（请求标签与证据差距）

- [ ] VLA: Unknown / not established by checked sources
- [x] Sim2Real: supported by official abstract/project page
- [ ] Robot Manipulation: Unknown / not established by checked sources
- [ ] Synthetic Data: Unknown / not established by checked sources
- [ ] Generalization: Unknown / not established by checked sources
- [ ] Bimanual: Unknown / not established by checked sources
- [x] Dexterous: supported by official abstract/project page
- [ ] Long-horizon: Unknown / not established by checked sources

## Summary Evidence（摘要证据）

- Evidence Level: Abstract-level
- Sources: IEEE Xplore abstract
- Verification Status: IEEE Xplore RA-L record verified
- Verified Date: 2026-09-19
- Notes: Follow-up dexterous extension; no conference-presentation relationship was identified in this pass.

## Citation Metrics

- Citation Count: Unknown
- Citation Source: OpenAlex (exact identity unresolved; API coverage may limit lookup)
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: Unknown (exact scholarly work unresolved)
- OpenAlex Work: Unknown

## Standardized Research Fields

### Research Problem
State and action representations may not transfer across reality gaps or hand geometries.

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
Reduce hand-specific state information to improve transfer robustness.

### Main Contributions
- Studies representation choices across two in-hand tasks and two transfer settings.

### Dataset & Benchmark
Two manipulation tasks; release status Unknown

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Two exemplar tasks and sim-to-real/cross-hand transfer are reported.

### Main Results
Unknown / Needs Full-Paper Verification

### Limitations
Unknown / Needs Full-Paper Verification

### What Remains Unsolved?
Library Analysis / Research Note: Unknown / Needs Full-Paper Verification

### Relevance to Our Project
Useful for later dexterous-hand extension and embodiment-agnostic action design.

## Full-paper Enrichment (Batch 08)

- Evidence Quality: B
- Evidence Status: Official full text was not reliably extractable in this batch; structured fields below preserve existing card evidence and mark unresolved details explicitly.

### Research Problem
State and action representations may not transfer across reality gaps or hand geometries.

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
Reduce hand-specific state information to improve transfer robustness.

### Architecture / Key Components
Unknown / Needs Official Full-Text Verification

### Dataset & Benchmark
Two manipulation tasks; release status Unknown

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Two exemplar tasks and sim-to-real/cross-hand transfer are reported.

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
- Dataset: Two manipulation tasks; release status Unknown

### Relevance to Our Project
** Useful for later dexterous-hand extension and embodiment-agnostic action design.

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://ieeexplore.ieee.org/document/10955245/

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Code-Unverified
- Supplement Status: Not Found
- Code Completeness: Unavailable
- Robot Platform Evidence: Multiple hand geometries

## Citation Relations

### References in Library

- No verified in-library citation edge yet.

### Cited By in Library

- No verified in-library citation edge yet.

### Related Work

- No curated content relation yet.

## 快速摘要

### 研究问题

灵巧手策略要跨仿真/现实和不同手型迁移。

### 之前方法的问题

域随机化等方法不能完全弥合观测与动作定义造成的差异。

### 核心思路

比较不同 State Space 与 Action Space 的选择，检验其对两类迁移的影响。

### 输入

官方摘要给出任务/数据类型；具体模型张量与接口需核对方法章节。

### 输出 / 动作

官方摘要未明确列出完整控制接口；需核对论文方法或代码。

### 数据集 / Benchmark

两项手内操作任务；具体机器人与设置见 RA-L 正文。

### 主要结果

IEEE RA-L 摘要报告：在两项示例操作任务中，去除手型特有信息的较小状态空间更利于迁移。

### 为什么重要

提醒本项目先确定哪些状态和动作维度可跨两只夹爪复用。

### 和当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

### 摘要证据

官方摘要/论文页：https://ieeexplore.ieee.org/document/10955245/；核验于 2026-09-23。仅为摘要级速读，原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
