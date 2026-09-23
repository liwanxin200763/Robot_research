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