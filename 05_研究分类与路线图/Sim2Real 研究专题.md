# Sim2Real 研究专题

本专题把“仿真训练或生成数据 → 真机测试”的**实际证据**放在一起。每篇仍只有一张 `02_论文` 主卡；主分类不因专题关联而移动。当前收录 **10 篇**：核心 Sim2Real 研究 7 篇，含实质迁移实验的关联研究 3 篇。这里的“收录”不表示这些方法可以直接迁移到 DH116。

## 研究问题：为什么仿真成功不等于真机成功

**Reality Gap（仿真与现实的差距）**包括相机视角和材质外观、物体与工作台几何、关节零位、摩擦和接触力等不一致。策略可能在单一仿真布置中学会视觉捷径，或在理想碰撞模型里学会真实手指无法执行的动作。**Zero-shot Sim2Real（零样本仿真到真实迁移）**只表示不拿目标真机示范更新策略；相机安装、关节校准、安全限幅仍然需要做。

**Domain Randomization（域随机化）**在训练时改变环境参数；**System Identification（系统辨识）**则用真实运动和反馈估计参数，使仿真模型更接近硬件。两者可以互补，但不是同一件事。

## 八条研究线索

1. **视觉域差异**：材质、背景、灯光与相机外参。[[02_论文/05_仿真到真实_Sim2Real/Grounding Sim-to-Real Generalization in Robotic Manipulation - An Empirical Study with Vision-Language-Action Models|Grounding Sim-to-Real Generalization]]直接比较不同随机化因子。
2. **几何与物理差异**：桌高、相机位置、重力、摩擦、接触。先测哪些因素真实掉点最多，再决定仿真预算。
3. **本体与动作空间差异**：关节映射、坐标系、相机几何。[[02_论文/05_仿真到真实_Sim2Real/Robot Manipulation with GPT-6-Astra - Body Knowledge, Experience Reuse, Emergent Skills, and Sim2Real Transfer|GPT-6-Astra 机器人操作]]在统一 API 和校准前提下复用仿真机械资产。
4. **仿真与真实数据混合**：[[02_论文/05_仿真到真实_Sim2Real/Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training|Sim-and-Real Policy Co-Training]]讨论少量真机数据与仿真共同训练；[[02_论文/05_仿真到真实_Sim2Real/Rapidly Adapting Policies to the Real-World via Simulation-Guided Fine-Tuning|Simulation-Guided Fine-Tuning]]讨论快速真机适配。二者不属于零样本路线。
5. **合成数据规模和可执行性**：[[02_论文/10_基准测试与数据集/RoboTwin 2.0 - A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation|RoboTwin 2.0]]、[[02_论文/08_数据与遥操作/DexMimicGen - Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning|DexMimicGen]]、[[02_论文/08_数据与遥操作/RDGen - Demonstration Generation for High-Quality Robot Learning via Reinforcement Learning|RDGen]]。数据更多不等于真机自动更稳，必须看部署测试。
6. **强化学习与策略更新**：Grounding 的同组实验比较 SFT、SFT+RL、SFT+RL+DR；[[02_论文/05_仿真到真实_Sim2Real/Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids|视觉灵巧操作 Sim2Real RL]]提供接触任务路线。
7. **零样本真实部署**：[[02_论文/06_扩散模型_流匹配_IL_RL/Sim2Real-VLA - Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation|Sim2Real-VLA]]和[[02_论文/05_仿真到真实_Sim2Real/Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors|World-Action Model 合成先验迁移]]分别测试 VLA 与视频—动作联合模型；二者的任务、数据和指标不同，不直接横向比较。
8. **真实评测**：分别记录仿真成功率、真机接触/阶段成功率、整任务成功率、完成时间和操作者介入，避免把不同指标汇成一个“成功”。

## 代表论文与证据层级

| 论文 | 归类 | 真机与直接迁移证据 | 真实数据微调 | 关键结论与边界 |
| --- | --- | --- | --- | --- |
| [[02_论文/05_仿真到真实_Sim2Real/Grounding Sim-to-Real Generalization in Robotic Manipulation - An Empirical Study with Vision-Language-Action Models|P179 · Grounding Sim-to-Real Generalization]] | 核心 | Piper；五任务零样本真机评测 | 否 | 相机/桌高随机化作用大；五任务平均 SFT 5.6%、SFT+RL+DR 42.8%，表 3。RL 组动作头也改变。 |
| [[02_论文/05_仿真到真实_Sim2Real/Robot Manipulation with GPT-6-Astra - Body Knowledge, Experience Reuse, Emergent Skills, and Sim2Real Transfer|P180 · GPT-6-Astra 机器人操作]] | 核心 | XLeRobot；12 次真实电梯厅实验 | 模型权重不更新；需实机校准 | 仿真资产/经验让同起点到目标接触的平均时间少 53.0%/49.9%；**成功标准是操作员确认接触**，不是可靠按下按钮。 |
| [[02_论文/05_仿真到真实_Sim2Real/Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors|P181 · World-Action Model 合成先验迁移]] | 核心 | Franka；四任务×10 次零样本真机测试 | 否 | 35% 平均任务成功率；3 页早期结果，缺模块消融。 |
| [[02_论文/06_扩散模型_流匹配_IL_RL/Sim2Real-VLA - Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation|P001 · Sim2Real-VLA]] | 核心 | 项目页称有真机零样本任务 | 否 | 现有主卡仍是摘要级，具体数值、硬件需复查本地全文。 |
| [[02_论文/05_仿真到真实_Sim2Real/Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training|P094 · Sim-and-Real Policy Co-Training]] | 核心 | 真机操控实验 | 是，仿真与少量真实数据联合 | 主卡现为摘要级，具体 baseline 与数值待复查全文。 |
| [[02_论文/05_仿真到真实_Sim2Real/Rapidly Adapting Policies to the Real-World via Simulation-Guided Fine-Tuning|P095 · Simulation-Guided Fine-Tuning]] | 核心 | 真机少样本适配 | 是 | 主卡现为摘要级，任务与对照数值待复查全文。 |
| [[02_论文/05_仿真到真实_Sim2Real/Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids|P096 · 视觉灵巧操作 Sim2Real RL]] | 核心 | 人形灵巧操作真机 | 以主卡摘要为准，待核全文 | 当前笔记未给统一真机成功率，不推断 DH116 收益。 |
| [[02_论文/10_基准测试与数据集/RoboTwin 2.0 - A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation|P172 · RoboTwin 2.0]] | 实质实验 | COBOT-Magic 双臂四任务；真实数据加合成轨迹 | 是，对照含 10 条真机示范 | 50 任务仿真基准与四项真机实验；不是“所有任务零样本”。 |
| [[02_论文/08_数据与遥操作/DexMimicGen - Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning|P145 · DexMimicGen]] | 实质实验 | GR-1 双灵巧手 Can Sorting | 4 条真实源示范构建数字孪生 | 40 条生成示范训练策略的真机测试为 90%；只覆盖一个真机任务。 |
| [[02_论文/08_数据与遥操作/RDGen - Demonstration Generation for High-Quality Robot Learning via Reinforcement Learning|P152 · RDGen]] | 实质实验 | Marvin M6CCS + RY-H2 手；仿真 SAC 技能真机执行 | 仿真技能迁移后收真机数据 | 两项下游 π0 测试各仅 10 次；方块成功率 60%→80%，罐 70%→100%。 |

前 3 篇由本轮官方全文核对；P145/P152/P172 的原主卡记录了全文章节和真机表格；P001/P094/P095/P096 的旧主卡尚有实验细节缺口。专题只将已有证据够具体的结果写成数字。[[02_论文/01_VLA/π0.5 - a Vision-Language-Action Model with Open-World Generalization|π0.5]]有未见真实家庭评测，但现有全文卡没有证明“仿真训练→真机直接迁移”，因此暂不计入本专题十篇。

## 对机械臂 + DH116 灵巧手的具体启发

1. **先做域差异矩阵**：分别变相机外参、桌高、光照、背景、物体摆位，再组合；每组记录仿真、真机的任务成功率及其差值。不要只报告单一平均数。（P179 表 1–3）
2. **把接触模型单独校准**：记录 DH116 指尖材料、关节零位/回差、摩擦与力阈值；视觉逼真度和接触真实性分别做消融。P179 的物理对照是极端参数，并不等于已给出适用于 DH116 的参数。
3. **低成本数据闭环**：先用少量真实示范校准数字孪生，再用 DexMimicGen/RoboTwin 2.0 生成可执行轨迹，保留失败日志；同量真实数据、纯合成、混合数据都要分别测试。（P145、P172）
4. **独立评估部署反馈**：同步保存三视角或腕部图像、动作、状态与接触信号；可复用成功姿态或局部视觉技能，但必须设安全限幅和自动接触判定。Astra 论文的人工确认只能作为可行性线索。（P180）
5. **明确数据预算与终点**：用每任务固定的真机试次数比较成功率，分别报告首次接触、稳定抓取与整任务完成；World-Action 早期研究的 4×10 设计可作最低起点，但 DH116 需要更多重复。（P181）

## 建议先读的十篇

1. [[02_论文/10_基准测试与数据集/RoboTwin 2.0 - A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation|RoboTwin 2.0]] — 建立双臂仿真和数据基准。
2. [[02_论文/05_仿真到真实_Sim2Real/Grounding Sim-to-Real Generalization in Robotic Manipulation - An Empirical Study with Vision-Language-Action Models|Grounding Sim-to-Real Generalization]] — 找出先该校准哪些差异。
3. [[02_论文/06_扩散模型_流匹配_IL_RL/Sim2Real-VLA - Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation|Sim2Real-VLA]] — 理解合成 VLA 零样本路线；主卡数值待补。
4. [[02_论文/05_仿真到真实_Sim2Real/Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors|World-Action Model 合成先验迁移]] — 比较另一种模型族的零样本可行性。
5. [[02_论文/08_数据与遥操作/DexMimicGen - Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning|DexMimicGen]] — 双臂灵巧手数字孪生数据生成。
6. [[02_论文/08_数据与遥操作/RDGen - Demonstration Generation for High-Quality Robot Learning via Reinforcement Learning|RDGen]] — 仿真 RL 技能迁移后生成真机示范。
7. [[02_论文/05_仿真到真实_Sim2Real/Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training|Sim-and-Real Policy Co-Training]] — 真/仿混训，需补读实验细节。
8. [[02_论文/05_仿真到真实_Sim2Real/Rapidly Adapting Policies to the Real-World via Simulation-Guided Fine-Tuning|Simulation-Guided Fine-Tuning]] — 真机快速适配，需补读实验细节。
9. [[02_论文/05_仿真到真实_Sim2Real/Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids|视觉灵巧操作 Sim2Real RL]] — 接触密集任务的 RL 迁移。
10. [[02_论文/05_仿真到真实_Sim2Real/Robot Manipulation with GPT-6-Astra - Body Knowledge, Experience Reuse, Emergent Skills, and Sim2Real Transfer|GPT-6-Astra 机器人操作]] — 执行时复用知识、经验与局部反馈；注意接触判定边界。

## 待跟进候选与边界

- [Zero-Shot Sim-to-Real Robot Learning: A Dexterous Manipulation Study on Reactive Catching](https://roboticsproceedings.org/rss22/p148.html)：RSS 2026 正式论文，研究多实例域随机化和零样本动态接触；本轮正式页面可见，但 PDF 入口未取得有效文件，**未全文核验，暂不建主卡**。
- [Crossing the Human-Robot Embodiment Gap with Sim-to-Real RL using One Human Demonstration](https://proceedings.mlr.press/v305/lum25a.html)：CoRL 2025 正式论文，单人类 RGB-D 示范到仿真 RL 再到真机；待阅读全文后决定是否增加主卡。
- [[02_论文/10_基准测试与数据集/RoboTwin - Dual-Arm Robot Benchmark with Generative Digital Twins|RoboTwin 1.0]]：数字孪生与真实数据并列，但旧主卡没有足够清楚的直接策略迁移对照，暂不计入十篇。
- [[02_论文/01_VLA/π0.5 - a Vision-Language-Action Model with Open-World Generalization|π0.5]]：属于真实环境泛化研究；不能因为真机部署就自动改称 Sim2Real。
