# RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins

## Basic Information（基本信息）

- Title: RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins
- Authors: Mu, Yao; Chen, Tianxing; Chen, Zanxin; Peng, Shijia; Lan, Zhiqian; Gao, Zeyu; Liang, Zhixuan; Yu, Qiaojun; Zou, Yude; Xu, Mingkun; Lin, Lunkai; Xie, Zhiqiang; Ding, Mingyu; Luo, Ping
- Year: 2025
- Venue: CVPR
- CCF Level: A
- Publication Status: Official Conference Paper
- Type: Dataset / Benchmark
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Subcategory: Bimanual; Dataset / Benchmark
- Keywords: Bimanual; Benchmark / Synthetic Demonstrations

## Classification

- Primary Category: Benchmark / Dataset
- Categories: Robot Manipulation; Bimanual; Data / Teleoperation; Benchmark / Dataset
- Subcategories: Bimanual; Dataset / Benchmark
- Tags: Bimanual; Benchmark / Synthetic Demonstrations

## Paper Links（论文）

- Official Paper: https://openaccess.thecvf.com/content/CVPR2025/html/Mu_RoboTwin_Dual-Arm_Robot_Benchmark_with_Generative_Digital_Twins_CVPR_2025_paper.html
- DOI: Unknown
- arXiv: 
- Project Page: https://robotwin-platform.github.io/

## Code & Resources（代码与资源）

- Official GitHub: https://github.com/RoboTwin-Platform/RoboTwin/tree/RoboTwin-1.0
- Code Status: Released
- Hugging Face: Unknown
- ModelScope: Unknown
- Checkpoint / Weights: 
- Dataset: 作者提供资源下载与示范采集脚本；本轮未下载或核验数据完整性
- Demo: Unknown
- Evaluation: Unknown
- Documentation: Unknown
- Other Official Resources: Unknown

## Robot / Embodiment（机器人与形态）

- Robot Platform: Unknown
- Embodiment: Bimanual / Parallel Gripper
- Single / Bimanual: Bimanual
- Gripper / Hand: Parallel Gripper
- Real Robot: Unknown
- Simulation: Unknown

## Experimental Metadata（实验基础信息）

- Dataset: 作者提供资源下载与示范采集脚本；本轮未下载或核验数据完整性
- Benchmark: Unknown
- Simulation Environment: Unknown
- Real-world Tasks: Unknown

## Research Summary（研究摘要）

- **Problem:** 研究主题为 `Bimanual; Dataset / Benchmark`；本卡仅按官方摘要级证据整理，未替代正文精读。
- **Main Contribution:**
  - To address this, we introduce RoboTwin, a generative digital twin framework that uses 3D generative foundation models and large language models to produce diverse expert datasets and provide a real-world-aligned evaluation platform for dual-arm robotic tasks.
  - However, the scarcity of diverse, high-quality demonstration data and real-world-aligned evaluation benchmarks severely limits such development.
- **Key Idea:** 以 `Bimanual; Benchmark / Synthetic Demonstrations` 为主要方法/能力线索；更细的结构和消融结论待正文核验。
- **Experiment / Validation:** Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。
- **Relevance to Our Project:** 与 NERO 双臂、普通夹爪、示范采集和双臂策略学习直接相关，优先评估动作表示与协同控制是否可迁移。

## Summary Evidence（摘要证据）

- Reading Depth: Abstract-level / 未精读
- Sources: https://openaccess.thecvf.com/content/CVPR2025/html/Mu_RoboTwin_Dual-Arm_Robot_Benchmark_with_Generative_Digital_Twins_CVPR_2025_paper.html；官方摘要/论文集元数据
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
- [ ] Checkpoint checked
- [x] Dataset checked
- [ ] Robot Platform checked
- [ ] Real Robot checked

## Reading Status（阅读状态）

Discovery / 未读

## Notes（备注）

采用RoboTwin-1.0分支；已查任务环境、交接动作及评估。与早期ECCV Workshop版本、CVPR Workshop竞赛报告、2.0版本区别记录。 Static checks only; no cloning/running or download.
