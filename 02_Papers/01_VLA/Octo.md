# Octo: An Open-Source Generalist Robot Policy

## Basic Information（基本信息）

- Title: Octo: An Open-Source Generalist Robot Policy
- Year: 2024
- Venue / Source: RSS
- Publication Status: Formal RSS 2024 proceedings
- CCF Level: Not CCF A (robotics venue extension)
- Type: Method Paper
- Category: VLA / Robot Foundation Models / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation
- Subcategory: VLA / Robot Foundation Models; Robot Manipulation / IL / Diffusion
- Priority: P0

## Classification

- Primary Category: VLA
- Categories: VLA; Robot Manipulation; Diffusion / Flow / IL / RL
- Subcategories: VLA / Robot Foundation Models; Robot Manipulation / IL / Diffusion
- Tags: Unknown

## Links（链接）

- Official Paper: https://roboticsproceedings.org/rss20/p090.html
- arXiv: https://arxiv.org/abs/2405.12213
- Project Page: https://octo-models.github.io/
- Official GitHub: https://github.com/octo-models/octo

## Code（代码状态）

- Code Status: Released
- Checkpoint: Author checkpoints; not downloaded
- Dataset Released: Partial (trained on OXE; not downloaded)

## Embodiment（机器人形态）

- Single Arm / Bimanual / Dexterous Hand / Gripper: Multi-Embodiment / Parallel Gripper
- Real Robot: Mixed

## Why Collected（为什么被收录）

Official RSS paper reports training over 800K trajectories and evaluation across nine robot platforms.

## Verification（待核验）

- [x] Venue 已确认
- [ ] CCF 等级已确认
- [x] Official Paper 已确认
- [x] Official GitHub 已确认
- [ ] Code 可运行性已确认
- [x] 是否真机已确认

## Citation Metrics

- Citation Count: 102
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4402353985
- OpenAlex Work: https://openalex.org/W4402353985

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

- Evidence Quality: A
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
- Official GitHub: https://github.com/octo-models/octo
- Code Status: Released
- Checkpoint: Author checkpoints; not downloaded
- Dataset: Unknown

### Relevance to Our Project
Unknown / Needs project-specific review

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://roboticsproceedings.org/rss20/p090.html; https://octo-models.github.io/; https://github.com/octo-models/octo

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: A-Upgraded
- Supplement Status: Not Found
- Code Completeness: Mostly Complete
- Robot Platform Evidence: Unknown

## Deep Enrichment (Full Text Read: 2026-09-22)
- Evidence Quality: A
- Fulltext Checked: Yes — arXiv HTML 2405.12213v2 / RSS 2024 paper, Sections III–V and Appendices B–F inspected.
- Supplement Status: Available - Verified (official appendices and code repository checked).
- Method: tokenizers encode language, goal images and observation histories; a transformer produces readout embeddings and a diffusion action head outputs chunks of consecutive actions (Sec. III).
- Backbone / Action: t5-base (111M) language encoder, convolutional image tokenizer, transformer backbone, diffusion action head; supports language, goal-image, wrist/third-person and proprioceptive inputs (Sec. III).
- Dataset / Benchmark: Open X-Embodiment contains ~1.5M episodes; Octo curates 800k. Zero-shot and finetuning evaluations cover WidowX BridgeV2, UR5, RT-1 and six downstream tasks (Secs. II–IV, App. F).
- Baselines / Results: design ablations compare diffusion, MSE and discretized action heads; model scale compares Octo-Tiny 10M, Small 27M and Base 93M. The paper reports strongest robustness and performance for Base (Sec. IV-C).
- Ablation: architecture, training data, training objective and model scale are explicitly ablated; diffusion head improves multimodal action distributions while retaining continuous precision (Sec. IV-C, App. F-B).
- Failure Cases: wrist-camera processing is weak; finetuning can be stronger with only third-person views (Sec. V).
- Limitations: Author-stated — only 27% of data includes wrist cameras, 56% includes language, training uses optimal demonstrations, and evaluation is limited to single/dual-arm manipulators (Sec. V).
- Remaining Gap / Idea: add language/wrist coverage and online suboptimal data, then test mobile manipulation.
- Evidence Sources: https://arxiv.org/abs/2405.12213 ; https://roboticsproceedings.org/rss20/p090.html ; https://octo-models.github.io/ ; https://github.com/octo-models/octo ; Sections III–V, Appendices B–F.
- Evidence Upgrade Status: A-Upgraded

## Citation Relations

### References in Library

- [[02_Papers/01_VLA/SayCan|SayCan]] — [arXiv full-text bibliography item 11](https://arxiv.org/html/2405.12213#bib.bib11)
- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open_X-Embodiment]] — [arXiv full-text bibliography item 67](https://arxiv.org/html/2405.12213#bib.bib67)

### Cited By in Library

- [[02_Papers/01_VLA/Actions_as_Language|Actions_as_Language]] — [arXiv full-text bibliography item 25](https://arxiv.org/html/2509.22195#bib.bib25)
- [[02_Papers/01_VLA/CoT-VLA|CoT-VLA]] — [arXiv full-text bibliography item 59](https://arxiv.org/html/2503.22020#bib.bib59)
- [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]] — [arXiv full-text bibliography item 35](https://arxiv.org/html/2412.03293#bib.bib35)
- [[02_Papers/01_VLA/OpenVLA|OpenVLA]] — [arXiv full-text bibliography item 5](https://arxiv.org/html/2406.09246#bib.bib5)
- [[02_Papers/01_VLA/ReconVLA|ReconVLA]] — [arXiv full-text bibliography item 32](https://arxiv.org/html/2508.10333#bib.bib32)
- [[02_Papers/01_VLA/RoboMonkey|RoboMonkey]] — [arXiv full-text bibliography item 34](https://arxiv.org/html/2506.17811#bib.bib34)
- [[02_Papers/01_VLA/SP-VLA|SP-VLA]] — [arXiv full-text bibliography item 36](https://arxiv.org/html/2506.12723#bib.bib36)
- [[02_Papers/01_VLA/SimpleVLA-RL|SimpleVLA-RL]] — [arXiv full-text bibliography item 46](https://arxiv.org/html/2509.09674#bib.bib46)
- [[02_Papers/01_VLA/SpatialVLA|SpatialVLA]] — [arXiv full-text bibliography item 48](https://arxiv.org/html/2501.15830#bib.bib48)
- [[02_Papers/01_VLA/TraceVLA|TraceVLA]] — [arXiv full-text bibliography item 35](https://arxiv.org/html/2412.10345#bib.bib35)
- [[02_Papers/01_VLA/VLA-Cache|VLA-Cache]] — [arXiv full-text bibliography item 9](https://arxiv.org/html/2502.02175#bib.bib9)
- [[02_Papers/01_VLA/VideoVLA|VideoVLA]] — [arXiv full-text bibliography item 1](https://arxiv.org/html/2512.06963#bib.bib1)
- [[02_Papers/02_Robot_Manipulation/VidMan|VidMan]] — [arXiv full-text bibliography item 7](https://arxiv.org/html/2411.09153#bib.bib7)
- [[02_Papers/03_Bimanual/AnyBimanual|AnyBimanual]] — [arXiv full-text bibliography item 51](https://arxiv.org/html/2412.06779#bib.bib51)
- [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective|A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective]] — [arXiv full-text bibliography item 248](https://arxiv.org/html/2507.01925#bib.bib248)
- [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI|A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]] — [arXiv full-text bibliography item 110](https://arxiv.org/html/2405.14093#bib.bib110)
- [[02_Papers/09_Survey_Review/Learning_by_Watching|Learning_by_Watching]] — [arXiv full-text bibliography item 97](https://arxiv.org/html/2402.07127#bib.bib97)
- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]] — [arXiv full-text bibliography item 886](https://arxiv.org/html/2510.10903#bib.bib886)

### Related Work

- [[02_Papers/01_VLA/OpenVLA|OpenVLA]] — Two generalist robot-policy approaches with different architectures and training mixtures.

## Quick Summary

- Problem: Large policies pretrained on diverse robot datasets have the potential to transform robotic learning: instead of training new policies from scratch, such generalist robot policies may be finetuned with only a little in-domain data, yet generalize broadly.
- Previous Gap: However, to be widely applicable across a range of robotic learning scenarios, environments, and tasks, such policies need to handle diverse sensors and action spaces, accommodate a variety of commonly used robotic platforms, and finetune readily and…
- Core Idea: As a first step, we introduce Octo, a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset to date.
- Input: Not specified in checked abstract/card.
- Output / Action: Not specified in checked abstract/card.
- Dataset / Benchmark: Open X-Embodiment contains ~1.5M episodes; Octo curates 800k. Zero-shot and finetuning evaluations cover WidowX BridgeV2, UR5, RT-1 and six downstream tasks (Secs. II–IV, App. F).
- Main Result: In experiments across 9 robotic platforms, we demonstrate that Octo serves as a versatile policy initialization that can be effectively finetuned to new observation and action spaces.
- Why It Matters: Provides a concrete method or benchmark for the documented gap: However, to be widely applicable across a range of robotic learning scenarios, environments, and tasks, such policies need to…
- Project Relevance: High — informs language-conditioned manipulation and VLA design.
- Key Limitation: Author-stated — only 27% of data includes wrist cameras, 56% includes language, training uses optimal demonstrations, and evaluation is limited to single/dual-arm manipulators (Sec. V).
- Summary Evidence: Official abstract / paper page; https://arxiv.org/html/2405.12213; checked 2026-09-23. Rapid summary only; existing Evidence Quality is unchanged.
- Quick Summary Status: Evidence-backed
