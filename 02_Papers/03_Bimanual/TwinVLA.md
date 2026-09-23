# TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models

## Basic Information（基本信息）

- Title: TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models
- Year: 2026
- Venue / Source: ICLR
- Publication Status: 正式主会论文：官方论文集核实
- CCF Level: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Type: Method Paper
- Category: VLA / Robot Foundation Models / Bimanual Manipulation / Robot Manipulation
- Subcategory: VLA / Robot Foundation Models; Bimanual
- Priority: P0

## Classification

- Primary Category: Bimanual
- Categories: VLA; Robot Manipulation; Bimanual
- Subcategories: VLA / Robot Foundation Models; Bimanual
- Tags: Unknown

## Links（链接）

- Official Paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/65475a59e2a2cb707c9462e8a308e980-Abstract-Conference.html
- arXiv: 待补充
- Project Page: https://jellyho.github.io/TwinVLA/
- Official GitHub: https://github.com/jellyho/TwinVLA

## Code（代码状态）

- Code Status: Released
- Checkpoint: https://huggingface.co/collections/jellyho/twinvla（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset Released: 作者提供数据集合：https://huggingface.co/collections/jellyho/twinvla-datasets；未下载

## Embodiment（机器人形态）

- Single Arm / Bimanual / Dexterous Hand / Gripper: Bimanual / Parallel Gripper
- Real Robot: Unknown

## Why Collected（为什么被收录）

官方2026论文集确认；已查模型、训练、RoboTwin部署。论文集年份优先于2025预印本。 Static checks only; no cloning/running or download.

## Verification（待核验）

- [x] Venue 已确认
- [ ] CCF 等级已确认
- [x] Official Paper 已确认
- [x] Official GitHub 已确认
- [ ] Code 可运行性已确认
- [ ] 是否真机已确认

## Citation Metrics

- Citation Count: 0
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W7104816971
- OpenAlex Work: https://openalex.org/W7104816971

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

## Full-paper Enrichment (Batch 03)

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
- Official GitHub: https://github.com/jellyho/TwinVLA
- Code Status: Released
- Checkpoint: https://huggingface.co/collections/jellyho/twinvla（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: Unknown

### Relevance to Our Project
Unknown / Needs project-specific review

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://proceedings.iclr.cc/paper_files/paper/2026/hash/65475a59e2a2cb707c9462e8a308e980-Abstract-Conference.html; https://jellyho.github.io/TwinVLA/; https://github.com/jellyho/TwinVLA

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Fulltext-Unavailable
- Supplement Status: Not Found
- Code Completeness: Mostly Complete
- Robot Platform Evidence: Unknown


## Deep Enrichment (Batch 04 Source Check: 2026-09-22)
- Evidence Quality: B
- Fulltext Checked: No — official proceedings/arXiv/project/repository search recorded for this batch; a legally accessible full text was not extracted in this pass.
- Supplement Status: Not Found.
- Evidence Boundary: no new numeric claims added without section/table verification.
- Required follow-up: extract Introduction, Method, Experiments, Results, Ablation, Failure Cases, Limitations and official code structure before Evidence A upgrade.
- Queue Status: Completed-B

## Citation Relations

### References in Library

- No verified in-library citation edge yet.

### Cited By in Library

- No verified in-library citation edge yet.

### Related Work

- [[02_Papers/03_Bimanual/RDT-1B|RDT-1B]] — Both target bimanual VLA control; compare joint modeling with twin single-arm adaptation.

## Quick Summary

- Problem: Vision-language-action models (VLAs) trained on large-scale robotic datasets have demonstrated strong performance on manipulation tasks, including bimanual tasks.
- Previous Gap: However, because most public datasets focus on single-arm demonstrations, adapting VLAs for bimanual tasks typically requires substantial additional bimanual data and fine-tuning.
- Core Idea: To address this challenge, we introduce TwinVLA, a modular framework that composes two copies of a pretrained single-arm VLA into a coordinated bimanual VLA.
- Input: Not specified in checked abstract/card.
- Output / Action: Not specified in checked abstract/card.
- Dataset / Benchmark: Not specified in checked abstract/card.
- Main Result: Across diverse bimanual tasks in real-world and simulation settings, TwinVLA outperforms a comparably-sized monolithic RDT-1B model without requiring *any* bimanual pretraining.
- Why It Matters: Provides a concrete method or benchmark for the documented gap: However, because most public datasets focus on single-arm demonstrations, adapting VLAs for bimanual tasks typically requires…
- Project Relevance: High — directly informs dual-arm coordination, data or ordinary-gripper policy design.
- Key Limitation: Not established by the checked summary source; consult the full paper.
- Summary Evidence: Official abstract / paper page; https://proceedings.iclr.cc/paper_files/paper/2026/hash/65475a59e2a2cb707c9462e8a308e980-Abstract-Conference.html; checked 2026-09-23. Rapid summary only; existing Evidence Quality is unchanged.
- Quick Summary Status: Evidence-backed
