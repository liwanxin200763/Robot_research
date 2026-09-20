# VideoVLA: Video Generators Can Be Generalizable Robot Manipulators

## Basic Information（基本信息）

- Title: VideoVLA: Video Generators Can Be Generalizable Robot Manipulators
- Authors: Shen, Yichao; Wei, Fangyun; Du, Zhiying; Liang, Yaobo; Lu, Yan; Yang, Jiaolong; Zheng, Nanning; Guo, Baining
- Year: 2025
- Venue: NeurIPS
- CCF Level: A
- Publication Status: Official Conference Paper
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Subcategory: VLA / Robot Foundation Models
- Keywords: VLA; Video-Action Model / Generalization

## Classification

- Primary Category: VLA
- Categories: VLA; Robot Manipulation; Generalization / Long-Horizon
- Subcategories: VLA / Robot Foundation Models
- Tags: VLA; Video-Action Model / Generalization

## Paper Links（论文）

- Official Paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/89a3b655a8b68ae1c76b768152c9c19d-Abstract-Conference.html
- DOI: 10.52202/085713-3197
- arXiv: 
- Project Page: https://videovla-nips2025.github.io/

## Code & Resources（代码与资源）

- Official GitHub: https://github.com/VideoVLA-Project/VideoVLA
- Code Status: Partial
- Hugging Face: Unknown
- ModelScope: Unknown
- Checkpoint / Weights: 项目页提供VideoVLA模型链接；README还要求CogVideo的T5与VAE；未下载（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: README未提供完整论文训练数据准备流程
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

- Dataset: README未提供完整论文训练数据准备流程
- Benchmark: Unknown
- Simulation Environment: Unknown
- Real-world Tasks: Unknown

## Research Summary（研究摘要）

- **Problem:** 研究主题为 `VLA / Robot Foundation Models`；本卡仅按官方摘要级证据整理，未替代正文精读。
- **Main Contribution:**
  - In this work, we present VideoVLA, a simple approach that explores the potential of transforming large video generation models into robotic VLA manipulators.
  - Our experiments show that high-quality imagined futures correlate with reliable action predictions and task success, highlighting the importance of visual imagination in manipulation.
- **Key Idea:** 以 `VLA; Video-Action Model / Generalization` 为主要方法/能力线索；更细的结构和消融结论待正文核验。
- **Experiment / Validation:** Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。
- **Relevance to Our Project:** 可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

## Summary Evidence（摘要证据）

- Reading Depth: Abstract-level / 未精读
- Sources: https://proceedings.neurips.cc/paper_files/paper/2025/hash/89a3b655a8b68ae1c76b768152c9c19d-Abstract-Conference.html；官方摘要/论文集元数据
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

已查动作DiT、扩散引擎、sample_video_action.py。旧Coming soon文字在HTML注释中，不能当作当前状态；训练/机器人benchmark完整流水线本轮未确认，标Partial待运行条件复核。 Static checks only; no cloning/running or download.
