---
paper_id: P202
title: "MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations"
authors: ["Mandlekar, Ajay", "Nasiriany, Soroush", "Wen, Bowen", "Akinola, Iretiayo", "Narang, Yashraj", "Fan, Linxi", "Zhu, Yuke", "Fox, Dieter"]
year: 2023
venue: "CoRL 2023"
arxiv: "2310.17596"
arxiv_version: "v1"
pdf: "01 论文文库/PDFs/08_数据与遥操作/MimicGen.pdf"
verified_on: "2026-10-15"
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Data_Quality"]
---

# MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations

## A. 基本信息与研究问题

- 作者：Mandlekar, Ajay; Nasiriany, Soroush; Wen, Bowen; Akinola, Iretiayo; Narang, Yashraj; Fan, Linxi; Zhu, Yuke; Fox, Dieter
- 年份与 Venue：2023；CoRL 2023
- arXiv：[最新核验版本 2310.17596v1](https://arxiv.org/abs/2310.17596)；核验日期 2026-10-15
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/MimicGen.pdf|查看全文]]；[官方 PDF](https://arxiv.org/pdf/2310.17596v1)
- [项目主页](https://mimicgen.github.io/)；[官方仓库](https://github.com/NVlabs/mimicgen)
- 开源边界：代码 NVIDIA Source Code License（研究/评估用途限制）；数据 CC BY 4.0；本轮核验发布文件，未运行作者代码或复现实验
- 引用量：待 Google Scholar 人工核验，不填写估计数量
- 关联专题：[[02 研究方向/机器人数据采集与数据质量]]；[[02 研究方向/机器人遥操作与动作重定向]]


### 研究方向与快速摘要

MimicGen 问的是：示范中有多少是独特技能，又有多少只是同一技能随物体位置变化重复采集？核心思路是把少量机器人遥操作示范拆成相对物体的片段，在新场景变换、拼接并实际执行，只保留成功轨迹，再用行为克隆训练。输入不是任意人类裸手视频，而是已有机器人状态—动作轨迹、子任务结构及生成时的物体位姿；输出新机器人演示数据和单独训练的视觉策略（§3–5）

论文用约两百条源示范生成超过五万条、覆盖十八任务，支持场景、同类物体及机械臂变化。价值在减少重复示教，但仍需采样执行和成功判定；不是离线复制文件就获得独立新数据，也不是跨臂共享一个策略或直接验证 Sim2Real

## B. 相关工作与先前不足

人工遥操作可采复杂技能，却要为各种物体位置反复操作；脚本和强化学习自动采集又常需任务专用设计。图像增强只改变视觉输入，未补新状态—动作覆盖。已有 replay imitation 把轨迹回放直接当部署策略，依赖初始对齐和局部伺服；MimicGen 把回放当数据采集器，允许许多尝试失败，最终用成功数据训练闭环策略，因此生成成功率与策略成功率可以差很大（§2、§6.3、附录 E/P）

与 robomimic 的关系是复用离线训练和数据接口；新贡献集中在对象坐标下的片段改写与在线执行，不是新的大模型。它与视频生成机器人画面的路线也不同：数据是机器人实际在仿真或真机环境中交互产生，含对应动作，而非仅合成 RGB

## C. 核心贡献与方法

### 1. 三个关键前提与源数据

动作必须能转换为末端 delta pose 加夹爪开闭；任务有已知且固定顺序的 object-centric subtasks（每阶段相对一个参考物体）；每阶段开始时可取得该物体位姿。部署策略不一定需要物体位姿，生成器需要。用子任务完成判据切分源示范，保留每段控制器目标和夹爪动作。一般每任务十条源示范，Mobile Kitchen 用二十五条，Square 直接取 robomimic PH 十条（§3–5、图 2）

### 2. 在对象坐标中变换并拼接

新场景先选同阶段的参考段，可随机或依据物体位置选择。保持末端目标相对源物体的关系，再换到新物体坐标，得到新的世界系末端轨迹。这里操作的是统一控制帧，不能直接搬运原机械臂关节角。新段起点通常不在当前末端处，故在段前加入线性插值，并按源示范配对夹爪动作。每个阶段重新观察对象、选择参考、变换和执行，最终检查全任务成功；失败整段丢弃（§4、附录 M/N）

**少量源轨迹 → 子任务切段 → 新物体位姿 → 参考段对象相对变换 → 插值衔接 → 执行并记录 → 成功筛选 → BC-RNN 训练。** 跨 Panda、Sawyer、IIWA、UR5e 要共同末端坐标约定及各自控制器，新物体要有同类规范坐标。共享的是生成机制和源片段，而不是无需适配的网络权重

### 3. 感知、记录与训练

主要仿真任务在 robosuite/MuJoCo，装配任务在 Factory/Isaac Gym。附录 L.1 说明 robosuite 控制 20 Hz，不将此频率泛化为所有模块采样率。真机使用标定外部 D415：深度变点云，RANSAC 去桌面、DBSCAN 分割，以颜色或尺寸区分物体，再初始化姿态并 ICP 精化；视觉策略输入另有腕部 D435。真机训练图像 120×160，通常仿真 84×84。端到端采集延迟未报告（附录 H/O）

每变体通常生成一千条成功轨迹；必须同时记录尝试次数和来源示范，因为生成成功会偏向某几条源数据。BC-RNN 学 RGB 到动作，模拟评测三种子，按训练中最高成功率汇总；并不与最终检查点等价。计算设置含 V100，真机实验机器 RTX 3090，不能据此假定普通 CPU 可低成本跑完整流程（附录 O）

## D. 实验与结果

十八任务包括堆叠、螺母插入、穿线、多件装配、咖啡、厨房、移动操作及真机。D0 是源数据初始分布，D1/D2 扩大或移动物体初始区域，不是训练/验证数据划分。图 4 给 RGB BC-RNN 三种子结果：

| 任务 | 十条源数据 | 一千条生成数据 D0 | 生成数据 D1 |
|---|---:|---:|---:|
| Square | 11.3% | 90.7% | 73.3% |
| Threading | 19.3% | 98.0% | 60.7% |
| Three Piece Assembly | 1.3% | 82.0% | 62.7% |

它证明这些任务的覆盖扩增能支持特定策略，不证明所有生成样本在任何算法下都更优。等量二百条生成与二百条人工数据在若干任务上接近；一千扩至五千存在收益递减；源数据十条增加到五十、两百也不总有明显提升。跨机械臂数据生成率差异较大，训练后的策略结果却接近，进一步说明生成率不能代替数据学习价值（§6.1–6.3）

真机每任务十条源示范，正文明确 Stack 生成二百条/二百四十三次尝试，Coffee 一百条/一百九十二次尝试，生成率为 82.3%/52.1%。图 5 图注与附录对 Stack 条数有简写不一致，本卡采用正文及尝试数可复核的二百条。BC-RNN 各评五十次，成功率 Stack 36%、Coffee 14%；这与生成率是不同分母。附录 H 将 Stack 换 Diffusion Policy 为 76%，是同一真机数据下不同策略结果（§6.4）

真实数据为安全使用更长插值段；模拟对应消融中 Stack D1 从 99.3%降到 68.7%，Pick Place 从 50.7%降到 11.3%，提示“轨迹可执行”与“观察下可学”不是一回事。姿态噪声与数据来源选择也有专门分析（附录 H/I/U）

## E. 不足、当前平台复用与未来

**作者明确指出：**需要固定子任务序列及阶段物体位姿；每阶段只相对一个对象；成功过滤仍带偏差；线性插值无避碰保证；主要是刚体、近静态、相似类别与尺度。移动案例不同时移动底盘与机械臂，未解决完整通用移动操作（§7、附录 D）

**我的推论与复用：**先在仿真中建立源段、目标段、碰撞检查及来源追溯，适合当前 D435i＋DH116 的离线数据工程。D435i 点云可研究物体定位，但要校准和标注失败，不能直接宣称达到论文姿态精度。DH116 是六主动轴/十一总自由度，多指接触不是夹爪开闭；需先做三指运动学和受限映射，再研究“末端＋手形”片段，不能直接套七维动作

当前整手/多轴运动仍锁定、原因未知，应只做离线日志与仿真；未来机械臂、腕部视觉、双臂及控制器都是新增成本。论文没有把其仿真策略直接迁到真机，Sim2Real 在文中是未来方向。下一步可把成功过滤加上碰撞、停顿、来源占比和阶段可预测性，检查扩增是否只复制容易成功的窄模式

## 来源与核验边界

- 官方 arXiv v1 全文 45 页；实看图 2（p.3）、图 4（p.6）、真机评测（p.8），阅读附录 D/H/N/O/P/U
- [官方代码许可](https://github.com/NVlabs/mimicgen/blob/main/LICENSE)与 README 已核验。当前公开数据约 48,000 条/12 任务是发布子集，不与论文全部十八任务混同

## 延伸阅读：数据采集与可执行示范

- [[03 论文卡片/08_数据与遥操作/DemoGen - Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning|P230 · DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning]]：少示范扩增、物体中心轨迹变换、点云编辑
- [[03 论文卡片/08_数据与遥操作/GenSim2 - Scaling Robot Data Generation with Multi-modal and Reasoning LLMs|P234 · GenSim2: Scaling Robot Data Generation with Multi-modal and Reasoning LLMs]]：自动任务编程、关键点约束求解、点云策略与Sim2Real
