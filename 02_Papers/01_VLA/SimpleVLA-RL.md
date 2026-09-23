# SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning

## Basic Information（基本信息）

- Title: SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning
- Year: 2026
- Venue / Source: ICLR
- Publication Status: ICLR 2026 Conference
- CCF Level: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Type: Method Paper
- Category: VLA / Robot Foundation Models / Robot Manipulation
- Subcategory: VLA / Robot Foundation Models
- Priority: P1

## Classification

- Primary Category: VLA
- Categories: VLA; Robot Manipulation; Diffusion / Flow / IL / RL
- Subcategories: VLA / Robot Foundation Models
- Tags: Unknown

## Links（链接）

- Official Paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html
- arXiv: 待补充
- Project Page: 待补充
- Official GitHub: 待补充

## Code（代码状态）

- Code Status: Unknown
- Checkpoint: 待补充
- Dataset Released: Unknown

## Embodiment（机器人形态）

- Single Arm / Bimanual / Dexterous Hand / Gripper: Unknown
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

- Citation Count: Unknown
- Citation Source: OpenAlex (identity unmatched)
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: Unknown (no high-confidence match)
- OpenAlex Work: Unknown

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

## Full-paper Enrichment (Batch 02)

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
https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Fulltext-Unavailable
- Supplement Status: Not Found
- Code Completeness: Unknown
- Robot Platform Evidence: Unknown

## Deep Enrichment (Full Text Read: 2026-09-22)
- Evidence Quality: A
- Fulltext Checked: Yes — arXiv HTML 2509.09674, Secs. 2–6 inspected.
- Supplement Status: Available - Verified.
- Method: VLA-specific interactive rollouts, outcome reward modeling, exploration enhancements and GRPO-style RL are integrated into veRL (Secs. 2–3).
- Dataset / Benchmark: OpenVLA-OFT on LIBERO, RoboTwin 1.0/2.0 and real-world tasks; the paper emphasizes reducing dependence on demonstrations.
- Main Results: achieves state-of-the-art LIBERO performance, surpasses π0 on RoboTwin with exploration enhancements, and outperforms SFT on real-world tasks (abstract, Sec. 4).
- Ablation / Failure Cases: exploration, reward and rollout choices are analyzed; Sec. 6.2 explicitly discusses RL failure modes and unstable exploration.
- Limitations: Author-stated — RL rollout cost and reward sparsity; Library Analysis — transfer beyond evaluated embodiments remains open.
- Remaining Gap / Idea: combine verifier-based rewards with low-cost real-world safety constraints.
- Evidence Sources: https://arxiv.org/html/2509.09674 ; https://github.com/thegovind/simplevla-rl ; https://openreview.net/pdf?id=TQhSodCM4r.
- Evidence Upgrade Status: A-Upgraded

## Citation Relations

### References in Library

- [[02_Papers/01_VLA/Octo|Octo]] — [arXiv full-text bibliography item 46](https://arxiv.org/html/2509.09674#bib.bib46)
- [[02_Papers/01_VLA/OpenVLA|OpenVLA]] — [arXiv full-text bibliography item 2](https://arxiv.org/html/2509.09674#bib.bib2)
- [[02_Papers/03_Bimanual/RDT-1B|RDT-1B]] — [arXiv full-text bibliography item 23](https://arxiv.org/html/2509.09674#bib.bib23)
- [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective|A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective]] — [arXiv full-text bibliography item 3](https://arxiv.org/html/2509.09674#bib.bib3)
- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open_X-Embodiment]] — [arXiv full-text bibliography item 5](https://arxiv.org/html/2509.09674#bib.bib5)
- [[02_Papers/10_Benchmark_Dataset/RoboTwin|RoboTwin]] — [arXiv full-text bibliography item 40](https://arxiv.org/html/2509.09674#bib.bib40)

### Cited By in Library

- [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI|A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]] — [arXiv full-text bibliography item 718](https://arxiv.org/html/2405.14093#bib.bib718)
- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]] — [arXiv full-text bibliography item 919](https://arxiv.org/html/2510.10903#bib.bib919)

### Related Work

- No curated content relation yet.
