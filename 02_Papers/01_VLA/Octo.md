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
- Citation Checked Date: 2026-09-21
- Citation Source Identifier: Unknown (no high-confidence match)
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