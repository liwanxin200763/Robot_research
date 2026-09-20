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

- **Problem:** 研究主题为 `VLA / Robot Foundation Models`；本卡仅按官方摘要级证据整理，未替代正文精读。
- **Main Contribution:**
  - In this paper, we introduce a new paradigm for constructing 3D VLAs.
  - Extensive experiments show that the resulting model, BridgeVLA, can learn 3D manipulation both efficiently and effectively.
- **Key Idea:** 以 `VLA; 3D Manipulation / Data Efficiency` 为主要方法/能力线索；更细的结构和消融结论待正文核验。
- **Experiment / Validation:** Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。
- **Relevance to Our Project:** 可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

## Summary Evidence（摘要证据）

- Reading Depth: Abstract-level / 未精读
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

## Reading Status（阅读状态）

Discovery / 未读

## Notes（备注）

原论文代码在bridgevla分支；main已是BridgeVLA++，不可混用。已查agent、训练、评估；PaliGemma基础权重需申请访问。 Static checks only; no cloning/running or download.
