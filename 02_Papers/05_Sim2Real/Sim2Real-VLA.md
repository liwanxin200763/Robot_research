# Sim2Real-VLA: Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation

## Basic Information（基本信息）

- ID: R001
- Title: Sim2Real-VLA: Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation
- Authors: Runyi Zhao; Sheng Xu; Ruixing Jin; Yueci Deng; Yunxin Tai; Kui Jia; Guiliang Liu
- Year: 2026
- Venue: ICLR
- Venue Type: Important AI/ML Venue
- Publication Type: Official Conference Paper
- CCF Level: Unknown (current official CCF directory checked; no authoritative ICLR A row located in accessible current listing)
- Research Category: VLA / Robot Manipulation / Sim2Real
- Subcategory: Synthetic-data VLA / zero-shot real-world transfer
- Tags: VLA; Sim2Real; Robot Manipulation; Synthetic Data; Generalization; Bimanual; Dexterous; Long-horizon
- Priority: P0
- Special Attention: Yes
- Library Membership: Robotics Core / Important Papers

## Classification

- Primary Category: VLA
- Categories: VLA; Robot Manipulation; Bimanual; Dexterous; Sim2Real; Generalization / Long-Horizon; Data / Teleoperation
- Subcategories: Synthetic Data; Zero-Shot; Long-horizon
- Tags: VLA; Sim2Real; Robot Manipulation; Synthetic Data; Generalization; Bimanual; Dexterous; Long-horizon

## Links（链接）

- Official Paper: https://openreview.net/pdf/a4174c2964dc0df03c26c311b73e0a2e43de2929.pdf
- ICLR Proceedings: https://proceedings.iclr.cc/papers/search?q=Manipulating
- Project Page: https://edem-ai.github.io/sim2realvla.github.io/
- Official GitHub: https://github.com/DexForce/EmbodiChain

## Code & Resources（代码与资源）

- Code Status: Partial (official project links the paper implementation as an integration into EmbodiChain; no standalone paper repository)
- Checkpoint: Unknown
- Dataset: Automated synthetic manipulation-skill data; complete public release not confirmed

## Robot / Embodiment（机器人与形态）

- Robot Platform: Multiple real-world setups are shown; exact hardware inventory not extracted at abstract/project level
- Embodiment: Single Arm / Bimanual / Dexterous Hand
- Real Robot: Yes

## Research Summary（研究摘要）

- **Problem:** Synthetic-only VLA training usually transfers unreliably to real manipulation.
- **Main Contribution:**
  - A reconstructive VLA trained exclusively on synthetic data for zero-shot real-world transfer.
  - A dual-system design: a high-level planner infers chains of affordances, while a low-level actor executes and validates actions in a tokenized action space.
  - Automated synthetic manipulation-skill generation without manual real-world fine-tuning.
- **Key Idea:** Reconstruct gaze-region / affordance-relevant visual structure so the policy filters manipulation-irrelevant variation and retains motion-critical dynamics for transfer.
- **Model / Method:** High-level chain-of-affordances planning plus low-level tokenized action execution and validation.
- **Experiment / Validation:** The official project reports six robot manipulation tasks spanning single-arm, dual-arm, hand-over, pouring, basket pick-and-place and pan opening/placement settings, with domain-gap conditions.
- **Main Results:** The project reports the best success-rate and step-count performance across its six-task comparison; exact full-paper tables remain unextracted.
- **Limitations / Open Questions:** This record is abstract-level. Exact hardware inventory, baselines, ablations, checkpoint release and complete dataset release require full-paper and code-level follow-up.
- **Relevance to Our Project:** Directly relevant to VLA, synthetic data, generalization, dual-arm manipulation and real-world deployment.

## Requested Tags / Evidence Gaps（请求标签与证据差距）

- [x] VLA: supported by official abstract/project page
- [x] Sim2Real: supported by official abstract/project page
- [x] Robot Manipulation: supported by official abstract/project page
- [x] Synthetic Data: supported by official abstract/project page
- [x] Generalization: supported by official abstract/project page
- [x] Bimanual: supported by official abstract/project page
- [x] Dexterous: supported by official abstract/project page
- [x] Long-horizon: supported by the official project’s stated long-horizon tasks and six-task evaluation

## Summary Evidence（摘要证据）

- Evidence Level: Abstract-level
- Sources: Official ICLR Downloads/Proceedings; accepted OpenReview PDF; official project page; official EmbodiChain repository; author publication list; current official CCF directory
- Verification Status: ICLR 2026 publication confirmed through official ICLR Downloads/Proceedings and accepted OpenReview PDF; project and author pages cross-checked; code remains Partial integration; CCF remains Unknown
- Verified Date: 2026-09-21
- Notes: Current official CCF directory was checked; no authoritative ICLR A row was located in the accessible current listing, so this paper remains in Robotics Core / Important Papers and is not copied into strict CCF_A_Library.

## Citation Metrics

- Citation Count: Unknown
- Citation Source: OpenAlex (no high-confidence title match)
- Citation Checked Date: 2026-09-21
- OpenAlex Work: Unknown

## Standardized Research Fields

### Research Problem
Synthetic-only VLA training usually transfers unreliably to real manipulation.

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
Reconstruct gaze-region / affordance-relevant visual structure so the policy filters manipulation-irrelevant variation and retains motion-critical dynamics for transfer.

### Main Contributions
- A reconstructive VLA trained exclusively on synthetic data for zero-shot real-world transfer.

### Dataset & Benchmark
Automated synthetic manipulation-skill data; complete public release not confirmed

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
The official project reports six robot manipulation tasks spanning single-arm, dual-arm, hand-over, pouring, basket pick-and-place and pan opening/placement settings, with domain-gap conditions.

### Main Results
The project reports the best success-rate and step-count performance across its six-task comparison; exact full-paper tables remain unextracted.

### Limitations
Unknown / Needs Full-Paper Verification

### What Remains Unsolved?
Library Analysis / Research Note: Unknown / Needs Full-Paper Verification

### Relevance to Our Project
Directly relevant to VLA, synthetic data, generalization, dual-arm manipulation and real-world deployment.

## Full-paper Enrichment (Batch 01)

- Evidence Quality: B

### Research Problem
合成数据训练的 VLA 在真实机器人上受到 Sim2Real 外观、物体和桌面变化影响，且长时序操作的 affordance 结构容易丢失。

### What Previous Problem Does This Paper Solve?
Author-stated: synthetic-only VLA training has a persistent simulation-to-real gap; the paper targets zero-shot transfer without manual real-world fine-tuning.

### Model / Method
The paper uses a dual-system design: a high-level planner infers chains of affordances and a low-level actor executes and validates tokenized actions. Automatic skill acquisition generates simulator trajectories from atomic tasks, affordance supervision, inverse kinematics and rendered observations.

### Architecture / Key Components
High-level VLA planner; affordance chain; tokenized low-level action actor; automatic skill acquisition; simulator rendering and generalized IK.

### Dataset & Benchmark
Synthetic manipulation-skill trajectories generated by the project pipeline; evaluation covers six tasks: table rearrangement, single-arm pouring, dual-arm pouring, basket pick-and-place, hand-over/place and pan open/place. Complete dataset release is not confirmed.

### Baseline / SOTA
Official project comparison reports success rate and step count across six tasks; exact baseline names and full table values require full-paper table extraction.

### Experiment Setup
Simulation and real-world manipulation; single-arm and dual-arm settings; six tasks with domain-gap conditions for background, object and table variation. Exact camera, hardware and episode protocol require full-paper extraction.

### Main Results
Official project page reports the best success-rate and step-count performance across all six tasks and metrics. No unverified numeric values are added here.

### Ablation Study
Not Reported in the sources rechecked for this batch.

### Failure Cases
Domain-gap evaluation explicitly tests background, object, table and combined shifts; exact failure cases require full-paper appendix extraction.

### Limitations
Author-stated / evidence boundary: exact hardware inventory, complete benchmark table, checkpoint release and complete dataset release were not confirmed from the accessible official sources.

### What Remains Unsolved?
Library Analysis: robustness under broader embodiment, contact dynamics and unseen long-horizon compositions remains open.

### Open Source
Official project links implementation integration to EmbodiChain; no standalone paper repository or checkpoint confirmed.

### Relevance to Our Project
directly matches bimanual + sim2real direction.

### Idea Clues
Idea Clue 1: use affordance-conditioned dual-arm skill transfer as a controlled baseline for real gripper experiments. Evidence: official six-task and domain-gap evaluation. Why relevant: directly matches bimanual + sim2real direction.

### Evidence Sources
Official accepted OpenReview PDF; official project page; official EmbodiChain repository; ICLR 2026 proceedings.

- Evidence Level: Full-paper sections checked where official full text was accessible; otherwise official abstract/project/PDF evidence only.
- Citation Source Identifier: OpenAlex Work: https://openalex.org/W? title match was not high-confidence for this title; Citation Count remains Unknown.
