# OpenVLA: An Open-Source Vision-Language-Action Model

## Basic Information（基本信息）

- Title: OpenVLA: An Open-Source Vision-Language-Action Model
- Year: 2024
- Venue / Source: CoRL
- Publication Status: Formal CoRL 2024; PMLR volume 270 online 2025
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

- Official Paper: https://proceedings.mlr.press/v270/kim24e.html
- arXiv: https://arxiv.org/abs/2406.09246
- Project Page: https://openvla.github.io/
- Official GitHub: https://github.com/openvla/openvla

## Code（代码状态）

- Code Status: Released
- Checkpoint: Author checkpoint links; not downloaded
- Dataset Released: Partial (Open X-Embodiment sources; not downloaded)

## Embodiment（机器人形态）

- Single Arm / Bimanual / Dexterous Hand / Gripper: Single Arm / Parallel Gripper
- Real Robot: Yes

## Why Collected（为什么被收录）

Core public VLA baseline; platform and precise real-robot protocol require follow-up reading.

## Verification（待核验）

- [x] Venue 已确认
- [ ] CCF 等级已确认
- [x] Official Paper 已确认
- [x] Official GitHub 已确认
- [ ] Code 可运行性已确认
- [x] 是否真机已确认

## Citation Metrics

- Citation Count: 43
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4399695759
- OpenAlex Work: https://openalex.org/W4399695759

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
- Official GitHub: https://github.com/openvla/openvla
- Code Status: Released
- Checkpoint: Author checkpoint links; not downloaded
- Dataset: Unknown

### Relevance to Our Project
Unknown / Needs project-specific review

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://proceedings.mlr.press/v270/kim24e.html; https://openvla.github.io/; https://github.com/openvla/openvla

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: A-Upgraded
- Supplement Status: Not Found
- Code Completeness: Mostly Complete
- Robot Platform Evidence: Unknown

## Deep Enrichment (Full Text Read: 2026-09-22)
- Evidence Quality: A
- Fulltext Checked: Yes — arXiv HTML 2406.09246v3 / CoRL 2024 paper, Sections 3–6 and Appendices A–E inspected.
- Supplement Status: Available - Verified.
- Method: 7B Prismatic VLM with Llama 2, fused DINOv2+SigLIP encoders and an MLP projector; continuous actions are discretized into 256 tokenizer bins and trained with next-token cross-entropy (Secs. 3.1–3.2).
- Dataset: curated Open X-Embodiment mixture with 970k real-world trajectories, third-person views and single-arm end-effector control; DROID was removed from the final third of training after low action-token accuracy (Sec. 3.3, App. A).
- Baselines / Experiments: RT-2-X, Octo and Diffusion Policy across WidowX, Google Robot, Franka-Tabletop, Franka-DROID and LIBERO settings (Sec. 5, App. B–E).
- Main Results: +16.5 percentage points absolute success over 55B RT-2-X across 29 tasks/embodiments; +20.4% over Diffusion Policy in reported fine-tuning settings; 27 epochs, 64 A100s for 14 days, ~21,500 A100-hours; inference ~6 Hz on RTX 4090 with 15GB bfloat16 memory (Secs. 3.4–3.5, 5).
- Ablation: VLM backbone, resolution, vision-encoder finetuning, training epochs, learning rate, OpenX mixture, dual vs single encoder, quantization and LIBERO are detailed in Sec. 3.4 and Appendices D–E.
- Failure Cases: language grounding and novel-object distractors remain difficult; DROID diversity produced low action-token accuracy, motivating its removal (Secs. 3.3–3.4).
- Limitations: Author-stated — training data is restricted to single-arm/third-person configurations and the model still requires substantial compute; Library Analysis — bimanual/mobile transfer is not established.
- Remaining Gap / Idea: combine OpenVLA’s open training stack with explicit visual subgoal or gaze reconstruction for long-horizon tasks.
- Evidence Sources: https://arxiv.org/abs/2406.09246 ; https://openvla.github.io/ ; https://github.com/openvla/openvla ; Sections 3–6, Appendices A–E.
- Evidence Upgrade Status: A-Upgraded