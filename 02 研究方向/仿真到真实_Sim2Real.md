# 仿真到真实
详细的问题地图、证据分层与十篇阅读顺序见 [[02 研究方向/Sim2Real 研究专题|Sim2Real 研究专题]]。下方保留原有分类索引结构。

## 新增核心研究

- [[03 论文卡片/05_仿真到真实_Sim2Real/Grounding Sim-to-Real Generalization in Robotic Manipulation - An Empirical Study with Vision-Language-Action Models|P179 · Grounding Sim-to-Real Generalization]] — 2026 arXiv；五任务、随机化与真机零样本实证。
- [[03 论文卡片/05_仿真到真实_Sim2Real/Robot Manipulation with GPT-6-Astra - Body Knowledge, Experience Reuse, Emergent Skills, and Sim2Real Transfer|P180 · GPT-6-Astra 机器人操作]] — 2026 arXiv；仿真知识和经验复用，真机仅以操作员确认接触判成功。
- [[03 论文卡片/05_仿真到真实_Sim2Real/Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors|P181 · World-Action Model 合成先验迁移]] — 2026 CVPR Embodied AI Workshop；四任务零样本真机初步结果。

本页依据论文主卡的分类、子类、标签、关键词和机器人形态等字段生成。论文实体按主分类保留在 `03 论文卡片` 中。

## 优先阅读与特别关注

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/Sim2Real-VLA - Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation|Sim2Real-VLA：将合成技能零样本泛化到真实操作]]

- 年份： 2026
- 会议 / 期刊： ICLR
- 代码状态：部分发布
- 优先级： P0


## CCF A 论文

### [[03 论文卡片/03_双臂协作/ManipTrans - Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning|ManipTrans：通过残差学习高效迁移双臂灵巧操作]]

- 年份： 2025
- 会议 / 期刊： CVPR
- 代码状态：已发布
- 优先级：未知

### [[03 论文卡片/05_仿真到真实_Sim2Real/Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training|面向仿真与真实策略联合训练的可泛化域适应]]

- 年份： 2025
- 会议 / 期刊： NeurIPS
- 代码状态：未知
- 优先级：未知


## 机器人核心论文

### [[03 论文卡片/04_灵巧操作/Evaluating the Effect of State and Action Selection on In-Hand Manipulation Performance for Transferability|评估状态与动作选择对手内操作迁移性能的影响]]

- 年份： 2025
- 会议 / 期刊： RA-L
- 代码状态：未知
- 优先级： P2


## 发现池与参考论文

### [[03 论文卡片/05_仿真到真实_Sim2Real/Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids|面向人形机器人的视觉灵巧操作 Sim2Real 强化学习]]

- 年份： 2025
- 会议 / 期刊： CoRL
- 代码状态：未知
- 优先级： P2


## 全身技能与具身执行关联阅读

比较制造商参数与低延迟工程、真实轨迹残差校正；仿真角色、跨仿真器与G1真机证据分开

- [[03 论文卡片/06_扩散模型_流匹配_IL_RL/BeyondMimic - From Motion Tracking to Versatile Humanoid Control via Guided Diffusion|P210 · BeyondMimic]]: 全身人形统一跟踪配方、潜在扩散与测试时引导；Science Robotics 2026-08-26；本地为已标明的 arXiv v4，不冒充出版定稿
- [[03 论文卡片/05_仿真到真实_Sim2Real/ASAP - Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills|P216 · ASAP]]: 用真实轨迹学习残差动作校正训练仿真；真机为G1踝部简化，不是23自由度残差全部验证

[[02 研究方向/全身运动技能与具身执行框架|统一专题]] · [[02 研究方向/SenseNova-RoboRSI 项目资料与开放边界|RoboRSI项目开放边界]]
