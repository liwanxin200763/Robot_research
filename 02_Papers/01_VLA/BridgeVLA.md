# BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models

## Basic Information（基本信息）

- Title: BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models
- Authors: Li, Peiyan; Chen, Yixiang; Wu, Hongtao; Ma, Xiao; Wu, Xiangnan; Huang, Yan; Wang, Liang; Kong, Tao; Tan, Tieniu
- Year: 2025
- Venue: NeurIPS
- CCF Level: A
- Publication Status: Official Conference Paper
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Subcategory: VLA / Robot Foundation Models
- Keywords: VLA; 3D Manipulation / Data Efficiency

## Classification

- Primary Category: VLA
- Categories: VLA; Robot Manipulation
- Subcategories: VLA / Robot Foundation Models
- Tags: VLA; 3D Manipulation / Data Efficiency

## Paper Links（论文）

- Official Paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/5c1a8aa04c1a2cf5013f28831870dafa-Abstract-Conference.html
- DOI: 10.52202/085713-2137
- arXiv: 
- Project Page: https://bridgevla.github.io/

## Code & Resources（代码与资源）

- Official GitHub: https://github.com/BridgeVLA/BridgeVLA/tree/bridgevla
- Code Status: Released
- Hugging Face: Unknown
- ModelScope: Unknown
- Checkpoint / Weights: https://huggingface.co/datasets/LPY/BridgeVLA/tree/main/checkpoints/bridgevla（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: README提供预训练数据及RLBench/COLOSSEUM/GemBench说明；入口存在，未下载
- Demo: Unknown
- Evaluation: Unknown
- Documentation: Unknown
- Other Official Resources: Unknown

## Robot / Embodiment（机器人与形态）

- Robot Platform: Unknown
- Embodiment: Single Arm / Parallel Gripper
- Single / Bimanual: Single Arm
- Gripper / Hand: Parallel Gripper
- Real Robot: Unknown
- Simulation: Unknown

## Experimental Metadata（实验基础信息）

- Dataset: README提供预训练数据及RLBench/COLOSSEUM/GemBench说明；入口存在，未下载
- Benchmark: Unknown
- Simulation Environment: Unknown
- Real-world Tasks: Unknown

## Research Summary（研究摘要）

- **Problem:** 研究主题为 `VLA / Robot Foundation Models`；本卡仅按官方摘要级证据整理，未替代全文审阅。
- **Main Contribution:**
  - In this paper, we introduce a new paradigm for constructing 3D VLAs.
  - Extensive experiments show that the resulting model, BridgeVLA, can learn 3D manipulation both efficiently and effectively.
- **Key Idea:** 以 `VLA; 3D Manipulation / Data Efficiency` 为主要方法/能力线索；更细的结构和消融结论待正文核验。
- **Experiment / Validation:** Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。
- **Relevance to Our Project:** 可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

## Summary Evidence（摘要证据）

- Evidence Level: Abstract-level
- Sources: https://proceedings.neurips.cc/paper_files/paper/2025/hash/5c1a8aa04c1a2cf5013f28831870dafa-Abstract-Conference.html；官方摘要/论文集元数据
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping
- Verified Date: 2026-09-19
- Evidence Boundary: 未核实的机器人平台、数据集、代码可运行性和真机细节保持 Unknown。

## Verification（核验）

- [x] Venue confirmed
- [x] Full / Regular Paper confirmed
- [x] CCF A confirmed
- [x] Official Paper confirmed
- [x] Project Page checked
- [x] Official GitHub checked
- [x] Code Status checked
- [x] Checkpoint checked
- [x] Dataset checked
- [ ] Robot Platform checked
- [ ] Real Robot checked

## Notes（备注）

原论文代码在bridgevla分支；main已是BridgeVLA++，不可混用。已查agent、训练、评估；PaliGemma基础权重需申请访问。 Static checks only; no cloning/running or download.

## Citation Metrics

- Citation Count: 0
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4415272059
- OpenAlex Work: https://openalex.org/W4415272059

## Standardized Research Fields

### Research Problem
研究主题为 `VLA / Robot Foundation Models`；本卡仅按官方摘要级证据整理，未替代全文审阅。

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
以 `VLA; 3D Manipulation / Data Efficiency` 为主要方法/能力线索；更细的结构和消融结论待正文核验。

### Main Contributions
- In this paper, we introduce a new paradigm for constructing 3D VLAs.

### Dataset & Benchmark
README提供预训练数据及RLBench/COLOSSEUM/GemBench说明；入口存在，未下载

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。

### Main Results
Unknown / Needs Full-Paper Verification

### Limitations
Unknown / Needs Full-Paper Verification

### What Remains Unsolved?
Library Analysis / Research Note: Unknown / Needs Full-Paper Verification

### Relevance to Our Project
可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

## Full-paper Enrichment (Batch 02)

- Evidence Quality: A
- Evidence Status: Official full text was not reliably extractable in this batch; structured fields below preserve existing card evidence and mark unresolved details explicitly.

### Research Problem
研究主题为 `VLA / Robot Foundation Models`；本卡仅按官方摘要级证据整理，未替代全文审阅。

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
以 `VLA; 3D Manipulation / Data Efficiency` 为主要方法/能力线索；更细的结构和消融结论待正文核验。

### Architecture / Key Components
Unknown / Needs Official Full-Text Verification

### Dataset & Benchmark
README提供预训练数据及RLBench/COLOSSEUM/GemBench说明；入口存在，未下载

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。

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
- Official GitHub: https://github.com/BridgeVLA/BridgeVLA/tree/bridgevla
- Code Status: Released
- Checkpoint: Unknown
- Dataset: README提供预训练数据及RLBench/COLOSSEUM/GemBench说明；入口存在，未下载

### Relevance to Our Project
** 可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://proceedings.neurips.cc/paper_files/paper/2025/hash/5c1a8aa04c1a2cf5013f28831870dafa-Abstract-Conference.html; https://bridgevla.github.io/; https://github.com/BridgeVLA/BridgeVLA/tree/bridgevla

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: A-Upgraded
- Supplement Status: Not Found
- Code Completeness: Mostly Complete
- Robot Platform Evidence: Unknown

## Deep Enrichment (Full Text Read: 2026-09-22)
- Evidence Quality: A
- Fulltext Checked: Yes — arXiv HTML 2506.07961 / NeurIPS 2025 paper, Sections 3–8 and Tables 1–3 inspected.
- Supplement Status: Available - Verified (official arXiv supplementary sections 6–8 inspected).
- Method: pretrain a VLM to map multi-view projected point clouds to 2D heatmaps, then fine-tune the VLA while preserving input-output alignment; heatmaps precede action generation (Sec. 3).
- Architecture: 2D VLM backbone, multi-view point-cloud projection, 2D heatmap prediction, and action head; real setup uses colored point clouds (Sec. 3, 8.1).
- Dataset / Benchmark: RLBench, COLOSSEUM, GemBench simulation; real Franka Research 3 with parallel-jaw gripper and ZED 2i camera, 13 tasks with 10 expert trajectories/task (Sec. 7–8).
- Baselines: Image-BC CNN/ViT, C2F-ARM-BC, PerAct, HiveFormer, PolarNet, Act3D, 3D Diffuser Actor, RVT, RVT-2, SpatialVLA, π0, and ACT (Sec. 4.1, 8.2).
- Main Results: RLBench average success 88.2% vs 81.4%; COLOSSEUM 64.0% vs 56.7%; GemBench average 50.0%; real-world average improvement 32%; 95.4% success on 10+ tasks with 3 trajectories/task (abstract, Tables 1–3, Sec. 8).
- Ablation: experiments test point-cloud projection, heatmap pretraining, and alignment choices (Sec. 4, ablation sections 4.1–4.3).
- Failure Cases: precision-heavy peg insertion and sorting tasks are sensitive to alignment; generalization settings include distractors, lighting, background, height and novel object-skill combinations (Sec. 8.2–8.5).
- Limitations: Author-stated/future work — broader 3D input-output alignment and more efficient training remain open (Sec. 5). Library Analysis — only the reported Franka setup was validated.
- Remaining Gap / Idea: test the 2D heatmap bridge with bimanual or dexterous action spaces.
- Evidence Sources: https://arxiv.org/abs/2506.07961 ; https://bridgevla.github.io/ ; https://github.com/BridgeVLA/BridgeVLA ; Sections 3–8, Tables 1–3.
- Evidence Upgrade Status: A-Upgraded

## Citation Relations

### References in Library

- [[02_Papers/01_VLA/3D-VLA|3D-VLA]] — [arXiv full-text bibliography item 15](https://arxiv.org/html/2506.07961#bib.bib15)
- [[02_Papers/01_VLA/OpenVLA|OpenVLA]] — [arXiv full-text bibliography item 5](https://arxiv.org/html/2506.07961#bib.bib5)
- [[02_Papers/06_Diffusion_Flow_IL_RL/3D_Diffuser_Actor|3D_Diffuser_Actor]] — [arXiv full-text bibliography item 11](https://arxiv.org/html/2506.07961#bib.bib11)
- [[02_Papers/10_Benchmark_Dataset/THE_COLOSSEUM|THE_COLOSSEUM]] — [arXiv full-text bibliography item 18](https://arxiv.org/html/2506.07961#bib.bib18)

### Cited By in Library

- [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI|A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]] — [arXiv full-text bibliography item 506](https://arxiv.org/html/2405.14093#bib.bib506)
- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]] — [arXiv full-text bibliography item 958](https://arxiv.org/html/2510.10903#bib.bib958)

### Related Work

- No curated content relation yet.

## Quick Summary

- Problem: Recently, leveraging pre-trained vision-language models (VLMs) for building vision-language-action (VLA) models has emerged as a promising approach to effective robot manipulation learning.
- Previous Gap: However, only few methods incorporate 3D signals into VLMs for action prediction, and they do not fully leverage the spatial structure inherent in 3D data, leading to low data efficiency.
- Core Idea: In this paper, we introduce a new paradigm for constructing 3D VLAs.
- Input: Not specified in checked abstract/card.
- Output / Action: Not specified in checked abstract/card.
- Dataset / Benchmark: README提供预训练数据及RLBench/COLOSSEUM/GemBench说明；入口存在，未下载
- Main Result: RLBench average success 88.2% vs 81.4%; COLOSSEUM 64.0% vs 56.7%; GemBench average 50.0%; real-world average improvement 32%; 95.4% success on 10+ tasks with 3 trajectories/task (abstract, Tables 1–3, Sec. 8).
- Why It Matters: Provides a concrete method or benchmark for the documented gap: However, only few methods incorporate 3D signals into VLMs for action prediction, and they do not fully leverage the spatial…
- Project Relevance: High — informs language-conditioned manipulation and VLA design.
- Key Limitation: Author-stated/future work — broader 3D input-output alignment and more efficient training remain open (Sec. 5). Library Analysis — only the reported Franka setup was validated.
- Summary Evidence: Official abstract / paper page; https://arxiv.org/html/2506.07961; checked 2026-09-23. Rapid summary only; existing Evidence Quality is unchanged.
- Quick Summary Status: Evidence-backed
