# 仿真到真实
详细的问题地图、证据分层与十篇阅读顺序见 [[01 论文文库/专题阅读/Sim2Real 研究专题|Sim2Real 研究专题]]。下方保留原有分类索引结构。

## 迁移问题、证据层级与实验设计

仿真与现实差距应分成视觉、几何、动作接口和接触动力学四类。相机角度或桌高导致的失效，不能只靠增加摩擦随机化解决；关节零位与延迟问题也不能归因于图像域差异。域随机化增加训练变化，系统辨识用真实反馈估计参数，两条路线互补

零样本迁移指不使用目标任务真机示范更新策略，并不免除相机安装、关节校准与动作限幅。使用少量真实数据共同训练、仿真引导微调和真实反馈筛选，应单独归类，不与零样本结果排成同一榜单

1. **视觉域差异**：材质、背景、灯光与相机外参。[[03 论文卡片/05_仿真到真实_Sim2Real/Grounding Sim-to-Real Generalization in Robotic Manipulation - An Empirical Study with Vision-Language-Action Models|Grounding Sim-to-Real Generalization]]直接比较不同随机化因子。
2. **几何与物理差异**：桌高、相机位置、重力、摩擦、接触。先测哪些因素真实掉点最多，再决定仿真预算。
3. **本体与动作空间差异**：关节映射、坐标系、相机几何。[[03 论文卡片/05_仿真到真实_Sim2Real/Robot Manipulation with GPT-6-Astra - Body Knowledge, Experience Reuse, Emergent Skills, and Sim2Real Transfer|GPT-6-Astra 机器人操作]]在统一 API 和校准前提下复用仿真机械资产。
4. **仿真与真实数据混合**：[[03 论文卡片/05_仿真到真实_Sim2Real/Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training|Sim-and-Real Policy Co-Training]]讨论少量真机数据与仿真共同训练；[[03 论文卡片/05_仿真到真实_Sim2Real/Rapidly Adapting Policies to the Real-World via Simulation-Guided Fine-Tuning|Simulation-Guided Fine-Tuning]]讨论快速真机适配。二者不属于零样本路线。
5. **合成数据规模和可执行性**：[[03 论文卡片/10_基准测试与数据集/RoboTwin 2.0 - A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation|RoboTwin 2.0]]、[[03 论文卡片/08_数据与遥操作/DexMimicGen - Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning|DexMimicGen]]、[[03 论文卡片/08_数据与遥操作/RDGen - Demonstration Generation for High-Quality Robot Learning via Reinforcement Learning|RDGen]]。数据更多不等于真机自动更稳，必须看部署测试。
6. **强化学习与策略更新**：Grounding 的同组实验比较 SFT、SFT+RL、SFT+RL+DR；[[03 论文卡片/05_仿真到真实_Sim2Real/Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids|视觉灵巧操作 Sim2Real RL]]提供接触任务路线。
7. **零样本真实部署**：[[03 论文卡片/06_扩散模型_流匹配_IL_RL/Sim2Real-VLA - Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation|Sim2Real-VLA]]和[[03 论文卡片/05_仿真到真实_Sim2Real/Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors|World-Action Model 合成先验迁移]]分别测试 VLA 与视频—动作联合模型；二者的任务、数据和指标不同，不直接横向比较。
8. **真实评测**：分别记录仿真成功率、真机接触/阶段成功率、整任务成功率、完成时间和操作者介入，避免把不同指标汇成一个“成功”。

### 真机证据如何比较

P179 的五任务平均 SFT 5.6% 与 SFT+RL+DR 42.8% 来自同组实验，但 RL 组动作头也改变；P180 的真实电梯厅实验以操作员确认接触为终点，不能改写成稳定按下按钮；P181 四任务各十次、平均35%，属于早期小规模证据。P145 的90%只覆盖指定真机任务，P172的50个仿真任务不能当50个真机任务。原文的任务、平台、数据预算、评价终点和表号必须一起阅读

1. **先做域差异矩阵**：分别变相机外参、桌高、光照、背景、物体摆位，再组合；每组记录仿真、真机的任务成功率及其差值。不要只报告单一平均数。（P179 表 1–3）
2. **把接触模型单独校准**：记录 DH116 指尖材料、关节零位/回差、摩擦与力阈值；视觉逼真度和接触真实性分别做消融。P179 的物理对照是极端参数，并不等于已给出适用于 DH116 的参数。
3. **低成本数据闭环**：先用少量真实示范校准数字孪生，再用 DexMimicGen/RoboTwin 2.0 生成可执行轨迹，保留失败日志；同量真实数据、纯合成、混合数据都要分别测试。（P145、P172）
4. **独立评估部署反馈**：同步保存三视角或腕部图像、动作、状态与接触信号；可复用成功姿态或局部视觉技能，但必须设安全限幅和自动接触判定。Astra 论文的人工确认只能作为可行性线索。（P180）
5. **明确数据预算与终点**：用每任务固定的真机试次数比较成功率，分别报告首次接触、稳定抓取与整任务完成；World-Action 早期研究的 4×10 设计可作最低起点，但 DH116 需要更多重复。（P181）

逐篇证据、量化与定性迁移区分、旧卡待补字段和候选原始来源见 [[01 论文文库/专题阅读/Sim2Real 研究专题|完整迁移证据与阅读表]]

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

[[01 论文文库/专题阅读/全身运动技能与具身执行框架|统一专题]] · [[04 项目与实验/SenseNova-RoboRSI 项目资料与开放边界|RoboRSI项目开放边界]]
