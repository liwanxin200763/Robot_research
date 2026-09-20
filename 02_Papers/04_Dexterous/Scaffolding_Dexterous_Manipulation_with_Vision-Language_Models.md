# Scaffolding Dexterous Manipulation with Vision-Language Models

## Basic Information（基本信息）

- Title: Scaffolding Dexterous Manipulation with Vision-Language Models
- Authors: de Bakker, Vincent; Hejna, Joey; Lum, Tyler; Celik, Onur; Taranovic, Aleksandar; Blessing, Denis; Neumann, Gerhard; Bohg, Jeannette; Sadigh, Dorsa
- Year: 2025
- Venue: NeurIPS
- CCF Level: A
- Publication Status: Official Conference Paper
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Subcategory: Dexterous Hand / Dexterous Manipulation
- Keywords: Dexterous Hand; Residual RL / VLM Planning

## Classification

- Primary Category: Dexterous
- Categories: Robot Manipulation; Dexterous
- Subcategories: Dexterous Hand / Dexterous Manipulation
- Tags: Dexterous Hand; Residual RL / VLM Planning

## Paper Links（论文）

- Official Paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/862644b156e51c35dea5a7446d640b14-Abstract-Conference.html
- DOI: 10.52202/085713-3121
- arXiv: 
- Project Page: https://sites.google.com/view/dexterous-vlm-scaffolding

## Code & Resources（代码与资源）

- Official GitHub: https://github.com/vdebakker/vlm-scaffolding
- Code Status: Released
- Hugging Face: Unknown
- ModelScope: Unknown
- Checkpoint / Weights: 本轮未发现完整预训练策略包公开链接（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: 公开数据生成实现与任务资产；不等于所有论文轨迹均已提供
- Demo: Unknown
- Evaluation: Unknown
- Documentation: Unknown
- Other Official Resources: Unknown

## Robot / Embodiment（机器人与形态）

- Robot Platform: Unknown
- Embodiment: Dexterous Hand
- Single / Bimanual: Unknown
- Gripper / Hand: Dexterous Hand
- Real Robot: Unknown
- Simulation: Unknown

## Experimental Metadata（实验基础信息）

- Dataset: 公开数据生成实现与任务资产；不等于所有论文轨迹均已提供
- Benchmark: Unknown
- Simulation Environment: Unknown
- Real-world Tasks: Unknown

## Research Summary（研究摘要）

- **Problem:** 研究主题为 `Dexterous Hand / Dexterous Manipulation`；本卡仅按官方摘要级证据整理，未替代正文精读。
- **Main Contribution:**
  - Dexterous robotic hands are essential for performing complex manipulation tasks, yet remain difficult to train due to the challenges of demonstration collection and high-dimensional control.
  - Across a number of simulated tasks involving articulated objects and semantic understanding, we demonstrate that our method is able to learn robust dexterous manipulation policies.
- **Key Idea:** 以 `Dexterous Hand; Residual RL / VLM Planning` 为主要方法/能力线索；更细的结构和消融结论待正文核验。
- **Experiment / Validation:** Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。
- **Relevance to Our Project:** 可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

## Summary Evidence（摘要证据）

- Reading Depth: Abstract-level / 未精读
- Sources: https://proceedings.neurips.cc/paper_files/paper/2025/hash/862644b156e51c35dea5a7446d640b14-Abstract-Conference.html；官方摘要/论文集元数据
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

已查轨迹生成、RL训练和评估；README提供真机ROS部署说明。依赖外部Gemini服务、仿真器及机器人环境，未运行。 Static checks only; no cloning/running or download.
