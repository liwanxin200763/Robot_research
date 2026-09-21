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
- Citation Checked Date: 2026-09-21
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
