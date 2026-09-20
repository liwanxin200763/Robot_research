# 3D-VLA: A 3D Vision-Language-Action Generative World Model

## Basic Information（基本信息）

- Title: 3D-VLA: A 3D Vision-Language-Action Generative World Model
- Authors: Haoyu Zhen; Xiaowen Qiu; Peihao Chen; Jincheng Yang; Xin Yan; Yilun Du; Yining Hong; Chuang Gan
- Year: 2024
- Venue: ICML
- CCF Level: A
- Publication Status: Official Conference Paper
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Subcategory: VLA / Robot Foundation Models; Robot Manipulation / IL / Diffusion
- Keywords: VLA; World Model / 3D Generation

## Classification

- Primary Category: VLA
- Categories: VLA; Robot Manipulation; Diffusion / Flow / IL / RL
- Subcategories: VLA / Robot Foundation Models; Robot Manipulation / IL / Diffusion
- Tags: VLA; World Model / 3D Generation

## Paper Links（论文）

- Official Paper: https://proceedings.mlr.press/v235/zhen24a.html
- DOI: Unknown
- arXiv: 
- Project Page: https://vis-www.cs.umass.edu/3dvla/

## Code & Resources（代码与资源）

- Official GitHub: https://github.com/UMass-Embodied-AGI/3D-VLA
- Code Status: Partial
- Hugging Face: Unknown
- ModelScope: Unknown
- Checkpoint / Weights: https://huggingface.co/anyezhy/3dvla-diffusion ; https://huggingface.co/anyezhy/3dvla-diffusion-pointcloud（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: README及model card提供OpenX来源与数据说明；完整处理后数据待核实
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

- Dataset: README及model card提供OpenX来源与数据说明；完整处理后数据待核实
- Benchmark: Unknown
- Simulation Environment: Unknown
- Real-world Tasks: Unknown

## Research Summary（研究摘要）

- **Problem:** 研究主题为 `VLA / Robot Foundation Models; Robot Manipulation / IL / Diffusion`；本卡仅按官方摘要级证据整理，未替代正文精读。
- **Main Contribution:**
  - 3D-VLA: A 3D Vision-Language-Action Generative World ModelHaoyu Zhen, Xiaowen Qiu, Peihao Chen, Jincheng Yang, Xin Yan, Yilun Du,&nb...
  - 3D-VLA: A 3D Vision-Language-Action Generative World ModelHaoyu Zhen, Xiaowen Qiu, Peihao Chen, Jincheng Yang, Xin Yan, Yilun Du,&nb...
- **Key Idea:** 以 `VLA; World Model / 3D Generation` 为主要方法/能力线索；更细的结构和消融结论待正文核验。
- **Experiment / Validation:** Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。
- **Relevance to Our Project:** 可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

## Summary Evidence（摘要证据）

- Reading Depth: Abstract-level / 未精读
- Sources: https://proceedings.mlr.press/v235/zhen24a.html；官方摘要/论文集元数据
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

公开目标图像/点云扩散训练与推理、LLM训练实现；未确认完整机器人策略评测链，保守标Partial，端到端可运行性待复核。 Static checks only; no cloning/running or download.
