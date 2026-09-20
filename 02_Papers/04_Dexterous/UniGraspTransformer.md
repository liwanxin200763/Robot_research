# UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping

## Basic Information（基本信息）

- Title: UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping
- Authors: Wang, Wenbo; Wei, Fangyun; Zhou, Lei; Chen, Xi; Luo, Lin; Yi, Xiaohan; Zhang, Yizhong; Liang, Yaobo; Xu, Chang; Lu, Yan; Yang, Jiaolong; Guo, Baining
- Year: 2025
- Venue: CVPR
- CCF Level: A
- Publication Status: Official Conference Paper
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Subcategory: Robot Manipulation / IL / Diffusion; Dexterous Hand / Dexterous Manipulation
- Keywords: Dexterous Hand; Policy Distillation / Generalization

## Classification

- Primary Category: Dexterous
- Categories: Robot Manipulation; Dexterous; Diffusion / Flow / IL / RL; Generalization / Long-Horizon
- Subcategories: Robot Manipulation / IL / Diffusion; Dexterous Hand / Dexterous Manipulation
- Tags: Dexterous Hand; Policy Distillation / Generalization

## Paper Links（论文）

- Official Paper: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_UniGraspTransformer_Simplified_Policy_Distillation_for_Scalable_Dexterous_Robotic_Grasping_CVPR_2025_paper.html
- DOI: Unknown
- arXiv: 
- Project Page: https://dexhand.github.io/UniGraspTransformer/

## Code & Resources（代码与资源）

- Official GitHub: https://github.com/microsoft/UniGraspTransformer
- Code Status: Released
- Hugging Face: Unknown
- ModelScope: Unknown
- Checkpoint / Weights: IsaacGym3权重说明及IsaacGym4专用策略入口存在；IsaacGym4通用策略未发布（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: 提供资产/抓取初始化数据链接和生成轨迹步骤；未下载
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

- Dataset: 提供资产/抓取初始化数据链接和生成轨迹步骤；未下载
- Benchmark: Unknown
- Simulation Environment: Unknown
- Real-world Tasks: Unknown

## Research Summary（研究摘要）

- **Problem:** 研究主题为 `Robot Manipulation / IL / Diffusion; Dexterous Hand / Dexterous Manipulation`；本卡仅按官方摘要级证据整理，未替代正文精读。
- **Main Contribution:**
  - We introduce UniGraspTransformer, a universal Transformer-based network for dexterous robotic grasping that simplifies training while enhancing scalability and performance.
  - Experimental results demonstrate significant improvements over state-of-the-art, UniDexGrasp++, across various object categories, achieving success rate gains of 3.5%, 7.7%, and 10.1% on seen objects, unseen objects within seen categories, and completely unseen objects, respectively, in the vision-based setting.
- **Key Idea:** 以 `Dexterous Hand; Policy Distillation / Generalization` 为主要方法/能力线索；更细的结构和消融结论待正文核验。
- **Experiment / Validation:** Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。
- **Relevance to Our Project:** 对灵巧操作扩展有参考价值；当前普通夹爪主线需区分可迁移的学习方法与依赖多指硬件的部分。

## Summary Evidence（摘要证据）

- Reading Depth: Abstract-level / 未精读
- Sources: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_UniGraspTransformer_Simplified_Policy_Distillation_for_Scalable_Dexterous_Robotic_Grasping_CVPR_2025_paper.html；官方摘要/论文集元数据
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

已查在线RL和离线蒸馏实现及安装/训练/评估说明。代码Released；IsaacGym4通用策略权重仍Coming Soon，不代表代码也未发布。 Static checks only; no cloning/running or download.
