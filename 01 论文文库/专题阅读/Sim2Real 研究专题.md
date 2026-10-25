# Sim2Real 研究专题

本专题把“仿真训练或生成数据 → 真机测试”的**实际证据**放在一起。每篇仍只有一张 `03 论文卡片` 主卡；主分类不因专题关联而移动。原有 10 篇名单保留；2026-10-15 新增 Video2Sim2Real、LUCID 与 DemoBot 三项有量化真机结果的研究，共 **13 篇**；本轮另新增有量化真机评估的 TUCO，量化名单现为 **14 篇**。这里的“收录”不表示这些方法可以直接迁移到 DH116

## 2026-10-15 近期视频示教增补

| 唯一主卡 | 仿真到真实的证据 | 真机平台与条件 | 关键边界 |
|---|---|---|---|
| [P189 Video2Sim2Real](../../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/05_%E4%BB%BF%E7%9C%9F%E5%88%B0%E7%9C%9F%E5%AE%9E_Sim2Real/Video2Sim2Real%20-%20Full-Stack%20Autonomous%20Dexterous%20Skill%20Acquisition%20from%20a%20Single%20Human%20Video.md) | 数字孪生、点云 IL、手指残差 RL 后真机测试 | Kinova＋LEAP，七任务各十次，67/70 成功；表 2 | RGB-D、参考场景和标定；点云位姿仅在初始查询，残差逐步执行 |
| [P188 LUCID](../../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/04_%E7%81%B5%E5%B7%A7%E6%93%8D%E4%BD%9C/LUCID%20-%20Learning%20Embodiment-Agnostic%20Intent%20Models%20from%20Unstructured%20Human%20Videos%20for%20Scalable%20Dexterous%20Robot%20Skill%20Acquisition.md) | Isaac Lab 控制教师／感知学生迁移，实时意图重查询 | UR5e＋LEAP，三网络任务各三场景各十次；另有夹爪两任务各十五次 | 高层意图共享，控制器按本体训练；还需要系统辨识和腕部深度 |
| [P190 DemoBot](../../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/03_%E5%8F%8C%E8%87%82%E5%8D%8F%E4%BD%9C/DemoBot%20-%20Efficient%20Learning%20of%20Bimanual%20Manipulation%20with%20Dexterous%20Hands%20From%20Third-Person%20Human%20Videos.md) | 仿真残差 RL 与执行器随机化后的真机概念验证 | 单 UR3e＋xHand，单步装配 18/20、多步 12/20 | 双臂只在仿真中验证；真实单臂任务经过改造，不能说同策略直接跨本体 |

另见 [[01 论文文库/专题阅读/从人类视频学习灵巧操作_近期论文对比|八条视频示教路线对比]]：Do as I Do 有仿真轨迹到真机回放展示，但没有统一重复试验成功率，暂不并入上述量化名单；V2P-Manip 当前证据为仿真；Human2Dex 与 Hand2Robot 有真机策略实验，但本轮未据此认定为仿真训练迁移

## 研究问题：为什么仿真成功不等于真机成功

**Reality Gap（仿真与现实的差距）**包括相机视角和材质外观、物体与工作台几何、关节零位、摩擦和接触力等不一致。策略可能在单一仿真布置中学会视觉捷径，或在理想碰撞模型里学会真实手指无法执行的动作。**Zero-shot Sim2Real（零样本仿真到真实迁移）**只表示不拿目标真机示范更新策略；相机安装、关节校准、安全限幅仍然需要做。

**Domain Randomization（域随机化）**在训练时改变环境参数；**System Identification（系统辨识）**则用真实运动和反馈估计参数，使仿真模型更接近硬件。两者可以互补，但不是同一件事。

## 八条研究线索

1. **视觉域差异**：材质、背景、灯光与相机外参。[[03 论文卡片/05_仿真到真实_Sim2Real/Grounding Sim-to-Real Generalization in Robotic Manipulation - An Empirical Study with Vision-Language-Action Models|Grounding Sim-to-Real Generalization]]直接比较不同随机化因子。
2. **几何与物理差异**：桌高、相机位置、重力、摩擦、接触。先测哪些因素真实掉点最多，再决定仿真预算。
3. **本体与动作空间差异**：关节映射、坐标系、相机几何。[[03 论文卡片/05_仿真到真实_Sim2Real/Robot Manipulation with GPT-6-Astra - Body Knowledge, Experience Reuse, Emergent Skills, and Sim2Real Transfer|GPT-6-Astra 机器人操作]]在统一 API 和校准前提下复用仿真机械资产。
4. **仿真与真实数据混合**：[[03 论文卡片/05_仿真到真实_Sim2Real/Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training|Sim-and-Real Policy Co-Training]]讨论少量真机数据与仿真共同训练；[[03 论文卡片/05_仿真到真实_Sim2Real/Rapidly Adapting Policies to the Real-World via Simulation-Guided Fine-Tuning|Simulation-Guided Fine-Tuning]]讨论快速真机适配。二者不属于零样本路线。
5. **合成数据规模和可执行性**：[[03 论文卡片/10_基准测试与数据集/RoboTwin 2.0 - A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation|RoboTwin 2.0]]、[[03 论文卡片/08_数据与遥操作/DexMimicGen - Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning|DexMimicGen]]、[[03 论文卡片/08_数据与遥操作/RDGen - Demonstration Generation for High-Quality Robot Learning via Reinforcement Learning|RDGen]]。数据更多不等于真机自动更稳，必须看部署测试。
6. **强化学习与策略更新**：Grounding 的同组实验比较 SFT、SFT+RL、SFT+RL+DR；[[03 论文卡片/05_仿真到真实_Sim2Real/Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids|视觉灵巧操作 Sim2Real RL]]提供接触任务路线。
7. **零样本真实部署**：[[03 论文卡片/06_扩散模型_流匹配_IL_RL/Sim2Real-VLA - Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation|Sim2Real-VLA]]和[[03 论文卡片/05_仿真到真实_Sim2Real/Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors|World-Action Model 合成先验迁移]]分别测试 VLA 与视频—动作联合模型；二者的任务、数据和指标不同，不直接横向比较。
8. **真实评测**：分别记录仿真成功率、真机接触/阶段成功率、整任务成功率、完成时间和操作者介入，避免把不同指标汇成一个“成功”。

## 代表论文与证据层级

| 论文 | 归类 | 真机与直接迁移证据 | 真实数据微调 | 关键结论与边界 |
| --- | --- | --- | --- | --- |
| [P179 · Grounding Sim-to-Real Generalization](../../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/05_%E4%BB%BF%E7%9C%9F%E5%88%B0%E7%9C%9F%E5%AE%9E_Sim2Real/Grounding%20Sim-to-Real%20Generalization%20in%20Robotic%20Manipulation%20-%20An%20Empirical%20Study%20with%20Vision-Language-Action%20Models.md) | 核心 | Piper；五任务零样本真机评测 | 否 | 相机/桌高随机化作用大；五任务平均 SFT 5.6%、SFT+RL+DR 42.8%，表 3。RL 组动作头也改变。 |
| [P180 · GPT-6-Astra 机器人操作](../../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/05_%E4%BB%BF%E7%9C%9F%E5%88%B0%E7%9C%9F%E5%AE%9E_Sim2Real/Robot%20Manipulation%20with%20GPT-6-Astra%20-%20Body%20Knowledge%2C%20Experience%20Reuse%2C%20Emergent%20Skills%2C%20and%20Sim2Real%20Transfer.md) | 核心 | XLeRobot；12 次真实电梯厅实验 | 模型权重不更新；需实机校准 | 仿真资产/经验让同起点到目标接触的平均时间少 53.0%/49.9%；**成功标准是操作员确认接触**，不是可靠按下按钮。 |
| [P181 · World-Action Model 合成先验迁移](../../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/05_%E4%BB%BF%E7%9C%9F%E5%88%B0%E7%9C%9F%E5%AE%9E_Sim2Real/Efficient%20Sim-to-Real%20Transfer%20of%20World-Action%20Models%20from%20Synthetic%20Priors.md) | 核心 | Franka；四任务×10 次零样本真机测试 | 否 | 35% 平均任务成功率；3 页早期结果，缺模块消融。 |
| [P001 · Sim2Real-VLA](../../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/06_%E6%89%A9%E6%95%A3%E6%A8%A1%E5%9E%8B_%E6%B5%81%E5%8C%B9%E9%85%8D_IL_RL/Sim2Real-VLA%20-%20Zero-Shot%20Generalization%20of%20Synthesized%20Skills%20to%20Realistic%20Manipulation.md) | 核心 | 项目页称有真机零样本任务 | 否 | 现有主卡仍是摘要级，具体数值、硬件需复查本地全文。 |
| [P094 · Sim-and-Real Policy Co-Training](../../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/05_%E4%BB%BF%E7%9C%9F%E5%88%B0%E7%9C%9F%E5%AE%9E_Sim2Real/Generalizable%20Domain%20Adaptation%20for%20Sim-and-Real%20Policy%20Co-Training.md) | 核心 | 真机操控实验 | 是，仿真与少量真实数据联合 | 主卡现为摘要级，具体 baseline 与数值待复查全文。 |
| [P095 · Simulation-Guided Fine-Tuning](../../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/05_%E4%BB%BF%E7%9C%9F%E5%88%B0%E7%9C%9F%E5%AE%9E_Sim2Real/Rapidly%20Adapting%20Policies%20to%20the%20Real-World%20via%20Simulation-Guided%20Fine-Tuning.md) | 核心 | 真机少样本适配 | 是 | 主卡现为摘要级，任务与对照数值待复查全文。 |
| [P096 · 视觉灵巧操作 Sim2Real RL](../../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/05_%E4%BB%BF%E7%9C%9F%E5%88%B0%E7%9C%9F%E5%AE%9E_Sim2Real/Sim-to-Real%20Reinforcement%20Learning%20for%20Vision-Based%20Dexterous%20Manipulation%20on%20Humanoids.md) | 核心 | 人形灵巧操作真机 | 以主卡摘要为准，待核全文 | 当前笔记未给统一真机成功率，不推断 DH116 收益。 |
| [P172 · RoboTwin 2.0](../../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/10_%E5%9F%BA%E5%87%86%E6%B5%8B%E8%AF%95%E4%B8%8E%E6%95%B0%E6%8D%AE%E9%9B%86/RoboTwin%202.0%20-%20A%20Scalable%20Data%20Generator%20and%20Benchmark%20with%20Strong%20Domain%20Randomization%20for%20Robust%20Bimanual%20Robotic%20Manipulation.md) | 实质实验 | COBOT-Magic 双臂四任务；真实数据加合成轨迹 | 是，对照含 10 条真机示范 | 50 任务仿真基准与四项真机实验；不是“所有任务零样本”。 |
| [P145 · DexMimicGen](../../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/08_%E6%95%B0%E6%8D%AE%E4%B8%8E%E9%81%A5%E6%93%8D%E4%BD%9C/DexMimicGen%20-%20Automated%20Data%20Generation%20for%20Bimanual%20Dexterous%20Manipulation%20via%20Imitation%20Learning.md) | 实质实验 | GR-1 双灵巧手 Can Sorting | 4 条真实源示范构建数字孪生 | 40 条生成示范训练策略的真机测试为 90%；只覆盖一个真机任务。 |
| [P152 · RDGen](../../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/08_%E6%95%B0%E6%8D%AE%E4%B8%8E%E9%81%A5%E6%93%8D%E4%BD%9C/RDGen%20-%20Demonstration%20Generation%20for%20High-Quality%20Robot%20Learning%20via%20Reinforcement%20Learning.md) | 实质实验 | Marvin M6CCS + RY-H2 手；仿真 SAC 技能真机执行 | 仿真技能迁移后收真机数据 | 两项下游 π0 测试各仅 10 次；方块成功率 60%→80%，罐 70%→100%。 |

前 3 篇由本轮官方全文核对；P145/P152/P172 的原主卡记录了全文章节和真机表格；P001/P094/P095/P096 的旧主卡尚有实验细节缺口。专题只将已有证据够具体的结果写成数字。[[03 论文卡片/01_VLA/π0.5 - a Vision-Language-Action Model with Open-World Generalization|π0.5]]有未见真实家庭评测，但现有全文卡没有证明“仿真训练→真机直接迁移”，因此暂不计入本专题十篇。

## 对机械臂 + DH116 灵巧手的具体启发

1. **先做域差异矩阵**：分别变相机外参、桌高、光照、背景、物体摆位，再组合；每组记录仿真、真机的任务成功率及其差值。不要只报告单一平均数。（P179 表 1–3）
2. **把接触模型单独校准**：记录 DH116 指尖材料、关节零位/回差、摩擦与力阈值；视觉逼真度和接触真实性分别做消融。P179 的物理对照是极端参数，并不等于已给出适用于 DH116 的参数。
3. **低成本数据闭环**：先用少量真实示范校准数字孪生，再用 DexMimicGen/RoboTwin 2.0 生成可执行轨迹，保留失败日志；同量真实数据、纯合成、混合数据都要分别测试。（P145、P172）
4. **独立评估部署反馈**：同步保存三视角或腕部图像、动作、状态与接触信号；可复用成功姿态或局部视觉技能，但必须设安全限幅和自动接触判定。Astra 论文的人工确认只能作为可行性线索。（P180）
5. **明确数据预算与终点**：用每任务固定的真机试次数比较成功率，分别报告首次接触、稳定抓取与整任务完成；World-Action 早期研究的 4×10 设计可作最低起点，但 DH116 需要更多重复。（P181）

## 建议先读的十篇

1. [[03 论文卡片/10_基准测试与数据集/RoboTwin 2.0 - A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation|RoboTwin 2.0]] — 建立双臂仿真和数据基准。
2. [[03 论文卡片/05_仿真到真实_Sim2Real/Grounding Sim-to-Real Generalization in Robotic Manipulation - An Empirical Study with Vision-Language-Action Models|Grounding Sim-to-Real Generalization]] — 找出先该校准哪些差异。
3. [[03 论文卡片/06_扩散模型_流匹配_IL_RL/Sim2Real-VLA - Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation|Sim2Real-VLA]] — 理解合成 VLA 零样本路线；主卡数值待补。
4. [[03 论文卡片/05_仿真到真实_Sim2Real/Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors|World-Action Model 合成先验迁移]] — 比较另一种模型族的零样本可行性。
5. [[03 论文卡片/08_数据与遥操作/DexMimicGen - Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning|DexMimicGen]] — 双臂灵巧手数字孪生数据生成。
6. [[03 论文卡片/08_数据与遥操作/RDGen - Demonstration Generation for High-Quality Robot Learning via Reinforcement Learning|RDGen]] — 仿真 RL 技能迁移后生成真机示范。
7. [[03 论文卡片/05_仿真到真实_Sim2Real/Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training|Sim-and-Real Policy Co-Training]] — 真/仿混训，需补读实验细节。
8. [[03 论文卡片/05_仿真到真实_Sim2Real/Rapidly Adapting Policies to the Real-World via Simulation-Guided Fine-Tuning|Simulation-Guided Fine-Tuning]] — 真机快速适配，需补读实验细节。
9. [[03 论文卡片/05_仿真到真实_Sim2Real/Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids|视觉灵巧操作 Sim2Real RL]] — 接触密集任务的 RL 迁移。
10. [[03 论文卡片/05_仿真到真实_Sim2Real/Robot Manipulation with GPT-6-Astra - Body Knowledge, Experience Reuse, Emergent Skills, and Sim2Real Transfer|GPT-6-Astra 机器人操作]] — 执行时复用知识、经验与局部反馈；注意接触判定边界。

## 待跟进候选与边界

- [Zero-Shot Sim-to-Real Robot Learning: A Dexterous Manipulation Study on Reactive Catching](https://roboticsproceedings.org/rss22/p148.html)：RSS 2026 正式论文，研究多实例域随机化和零样本动态接触；本轮正式页面可见，但 PDF 入口未取得有效文件，**未全文核验，暂不建主卡**。
- [Crossing the Human-Robot Embodiment Gap with Sim-to-Real RL using One Human Demonstration](https://proceedings.mlr.press/v305/lum25a.html)：CoRL 2025 正式论文，单人类 RGB-D 示范到仿真 RL 再到真机；待阅读全文后决定是否增加主卡。
- [[03 论文卡片/10_基准测试与数据集/RoboTwin - Dual-Arm Robot Benchmark with Generative Digital Twins|RoboTwin 1.0]]：数字孪生与真实数据并列，但旧主卡没有足够清楚的直接策略迁移对照，暂不计入十篇。
- [[03 论文卡片/01_VLA/π0.5 - a Vision-Language-Action Model with Open-World Generalization|π0.5]]：属于真实环境泛化研究；不能因为真机部署就自动改称 Sim2Real。

## 2026-10-15 仿真数据筛选与物理重定向

- [[03 论文卡片/08_数据与遥操作/TUCO - Curating Simulation Demonstrations for Sim-to-Real Robot Policy Co-Training|P207 · TUCO]]：10 次真实成功执行/任务用于筛选与联合训练；从1200条仿真候选选600条；FR3三任务各40次独立测试，宏平均85.8%。这是有真实反馈的联合训练，不是零真机数据迁移
- [[03 论文卡片/08_数据与遥操作/SPIDER - Scalable Physics-Informed Dexterous Retargeting|P209 · SPIDER]]：v3物理轨迹鲁棒化后在Panda＋Allegro开环回放；没有统一重复真机成功率，单列定性迁移证据，不加入上方量化计数
- [[03 论文卡片/08_数据与遥操作/DexMan - Learning Bimanual Dexterous Manipulation from Human and Generated Videos|P204 · DexMan]] 的当前证据为仿真；[[03 论文卡片/08_数据与遥操作/MimicGen - A Data Generation System for Scalable Robot Learning using Human Demonstrations|P202 · MimicGen]] 的真机源示范、实际生成和学习实验与纯仿真训练迁移不同，不能一概统称零样本Sim2Real

完整边界见 [[01 论文文库/专题阅读/机器人数据与遥操作技术路线对比]]


## 全身技能与具身执行关联阅读

新增全身运动迁移对照，不改变既有灵巧操作专题的含义

- [[03 论文卡片/06_扩散模型_流匹配_IL_RL/BeyondMimic - From Motion Tracking to Versatile Humanoid Control via Guided Diffusion|P210 · BeyondMimic]]: 全身人形统一跟踪配方、潜在扩散与测试时引导；Science Robotics 2026-08-26；本地为已标明的 arXiv v4，不冒充出版定稿
- [[03 论文卡片/05_仿真到真实_Sim2Real/ASAP - Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills|P216 · ASAP]]: 用真实轨迹学习残差动作校正训练仿真；真机为G1踝部简化，不是23自由度残差全部验证

[[01 论文文库/专题阅读/全身运动技能与具身执行框架|统一专题]] · [[04 项目与实验/SenseNova-RoboRSI 项目资料与开放边界|RoboRSI项目开放边界]]
