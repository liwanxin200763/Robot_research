---
paper_id: P191
title: "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware"
authors: ["Zhao, Tony Z.", "Kumar, Vikash", "Levine, Sergey", "Finn, Chelsea"]
year: 2023
venue: "Robotics: Science and Systems (RSS) 2023"
arxiv: "2304.13705"
version: "v1"
arxiv_version: "v1"
pdf: "01 论文文库/PDFs/08_数据与遥操作/ALOHA.pdf"
verified_on: "2026-10-15"
citation_status: "待 Google Scholar 人工核验"
tags: ["Teleoperation", "Data_Collection", "Retargeting", "Imitation_Learning"]
document_type: "会议论文"
preprint_platform: "arXiv"
first_public_date: "2023-04-23"
first_public_month: "2023-04"
first_public_scope: "arXiv v1 submission history (UTC)"
latest_preprint_date: "2023-04-23"
latest_preprint_version: "v1"
publication_status: "已正式发表"
published_venue: "Robotics: Science and Systems (RSS) 2023"
affiliations: ["Stanford University", "University of California Berkeley", "Meta"]
metadata_verified_on: "2026-10-17"
metadata_sources: ["https://arxiv.org/abs/2304.13705", "https://arxiv.org/pdf/2304.13705v1", "https://www.roboticsproceedings.org/rss19/p016.html", "https://tonyzhaozh.github.io/aloha/"]
publication_year: 2023
publication_month: "2023-07"
---

# Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware

## 出处与版本

- 文献类型：会议论文
- 预印本平台与编号：[arXiv 2304.13705](https://arxiv.org/abs/2304.13705)
- 首次公开日期：2023-04-23；首次公开月份：2023 年 4 月，依据 arXiv v1 提交历史（UTC）；本字段不宣称已穷尽项目网页或其他平台可能更早的公开记录
- 最近预印本版本：v1，日期 2023-04-23；当前未记录后续修订
- 当前发表状态：已正式发表
- 正式发表出处：[Robotics: Science and Systems (RSS) 2023](https://www.roboticsproceedings.org/rss19/p016.html)
- 正式出版年份：2023；正式出版月份：2023 年 7 月
- 日期与状态说明：RSS XIX 官方 BibTeX：2023 年 7 月；DOI：10.15607/RSS.2023.XIX.016；硬件与采集代码另见 https://github.com/tonyzhaozh/aloha
- 作者所属机构：Stanford University；University of California Berkeley；Meta
- 机构依据：Tony Z. Zhao、Chelsea Finn：Stanford；Sergey Levine：UC Berkeley；Vikash Kumar：Meta，均以正文首页署名为准；[对应版本 PDF 首页](https://arxiv.org/pdf/2304.13705v1)
- 项目主页：[作者项目页](https://tonyzhaozh.github.io/aloha/)
- 官方代码：[作者链接的仓库](https://github.com/tonyzhaozh/act)；入口存在不等于已核实完整实现、模型或许可，开源边界沿用下文说明
- 信息核验日期：2026-10-17；来源为官方版本历史、正文署名和上述正式条目；引用量沿用原 Google Scholar 人工核验规则

## 论文简介

便宜机械臂在开杯盖、装电池这类小尺度接触任务里，误差会逐步积累；人类示范又经常忽快忽慢，逐帧预测下一步不容易学好。这篇工作把低成本双臂遥操作硬件 ALOHA 和 ACT（用注意力序列模型预测一段动作的模仿学习方法）配成完整系统

操作者拖动主机械臂，从机械臂镜像执行，记录多路图像与关节动作。训练时 ACT 同时预测未来一段动作，即“动作块”，降低每步小误差滚动累积的机会；部署时把不同预测块对同一时刻的动作做时间加权，平衡平滑与反应。它还用条件变分自编码器描述示范中的多种合理动作，区别于只能给出单一下一步命令的做法（§III–IV）

作者在两项仿真和六项真机任务上比较。装电池最终成功率为 96%，但穿魔术贴只有 20%；真机每配置一个训练种子、25 次评估，不能把代表任务的 80%–90% 推广到全部任务。“约十分钟示范”指有效动作数据，不包括重置和失误的全部采集时间（表 I–II、§V-B）

对我们最值得借鉴的是相机、动作和时间戳统一记录，以及从简单行为克隆建立基线。DH116 的欠驱动手指并不等同于 ALOHA 平行夹爪；增加 D435i 或改变动作频率也需要重新验证观察和控制接口。多指接触策略、跨任务泛化与失败后的恢复属于后续研究设想，本文没有替我们解决

## A. 基本信息与研究问题

- 作者：Tony Z. Zhao、Vikash Kumar、Sergey Levine、Chelsea Finn
- 正式发表：Robotics: Science and Systems（RSS）2023；arXiv 2304.13705 最新为 v1，2023-04-23
- [官方会议页](https://www.roboticsproceedings.org/rss19/p016.html)｜[arXiv](https://arxiv.org/abs/2304.13705)｜[项目页](https://tonyzhaozh.github.io/aloha/)
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/ALOHA.pdf|查看 PDF]]；本卡据官方 arXiv v1 全文 18 页
- 代码：[ALOHA 硬件与采集](https://github.com/tonyzhaozh/aloha)、[ACT 算法与仿真](https://github.com/tonyzhaozh/act)；引用量待 Google Scholar 人工核验

本篇要让低成本、绝对定位不够准确的双臂，通过人类示范学会开小杯盖、装电池等毫米级接触任务。答案由两部分构成：ALOHA 提供容易操控的主从示教硬件，ACT 用视觉、关节状态预测连续动作块，减少单步模仿的误差累积。论文中的遥操作能力展示与自主学习结果必须分别理解：能被人遥控完成穿扎带，并不意味着策略也学会该技能（§III–V）

## B. 相关工作

普通 Behavior Cloning 每步独立预测，细小偏差会把状态推离示范分布；DAgger 用在线专家纠正补数据，但精细操作中反复纠正、注入噪声都不方便。ACT 改变预测单位，用一段动作表达短时协调关系，也容纳人类暂停等非单步 Markov 行为（§II、IV）

相对 VR 的末端位姿加 IK，ALOHA 让操作者拖动与从臂近似同构的小臂，直接映射关节；这一取舍降低奇异点附近求解困难，却绑定特定硬件。后续 GELLO 把主臂变成廉价编码器模型，UMI 则让示教脱离机器人；这些改进针对采集接口，不能替代 ACT 的时序学习贡献

## C. 核心贡献与方法

### 1. 主从同构与连续夹爪

两台 WidowX 为主臂，两台 ViperX 6-DoF 为从臂，每臂另含一维夹爪。主臂关节读数直接成为从臂目标，操作者看到真实工作区并闭环纠正。手柄和剪刀机构降低反拖负担，橡皮筋部分补偿重力，主臂质量及电机阻力也提供被动阻尼。该阻力不代表从端接触力被传回操作者（p3，图3）

透明结构的定制指爪改善可见性，表面抓握带增加摩擦。系统用四台 Logitech C922x RGB 相机，两个腕视角、一个前视角、一个俯视角，各 480×640；遥操作和记录为50 Hz。完整双臂系统预算低于20000美元，包含四台臂等设备，不能与仅控制器的报价直接比较。文中未给可复用的端到端毫秒延迟实测（§III）

### 2. 必须保存“想让机器人怎么动”

观察是从臂当前14维关节状态与四路图像，动作监督是主臂14维目标关节位置。两者不能混用：主从位置差经低层 PID 形成实际作用，因此只保存从臂已达到的位置，会抹去操作者有意施加的指令偏差。新平台仍需核对关节符号、零位、限位和夹爪行程，同构结构并不自动消除装配误差（p4，§IV）

### 3. ACT 与时间集成

每次输出未来 k 步绝对关节目标，而非下一步增量。四路图像经 ResNet18，和关节、潜变量一起送入 Transformer encoder；decoder 的位置查询生成 k×14 动作。训练用 CVAE：另一 encoder 从真实动作块与关节状态编码示范风格 z，部署删除该 encoder 并令 z=0。正文实现采用 L1 重建损失与 KL 正则；伪代码写MSE，复现应注意这处表述差异（p4–6，图4、算法1）

Action Chunk（动作块）降低有效决策长度；为避免每k步才更新造成突变，策略每步重算，并对“同一未来时刻”被多个历史动作块预测的值加权平均。它平均的是同一时刻的多个预测，不是把相邻时刻动作直接平滑。算法2和图5给出时间集成流程，附录表III默认k=100（p5、18）

每任务单独训练，约8000万参数，作者报告单张11GB RTX2080Ti约5小时、推理约0.01秒。这是指定实现的计算耗时，不等于包含相机、通信、电机执行的总延迟（p6）

## D. 实验与结果

### 数据、任务与主结果

两项 MuJoCo 任务为交接方块和双臂插接，分别用脚本与人类示范；六项真实任务为拉开密封袋、装电池、开杯盖、穿魔术贴、准备胶带、穿鞋。真实任务多数各50条示范，穿魔术贴100条；有效动作约10–20分钟，连同重置及失误的采集墙钟时间约30–60分钟。不能把“10分钟示范”写成整项实验只需10分钟（§V-B）

| 真实任务最终成功率 | ACT | 主要对照 |
|---|---:|---:|
| Slide Ziploc | 88% | 四种基线最终均0% |
| Slot Battery | 96% | 四种基线最终均0% |
| Open Cup | 84% | BeT 0% |
| Thread Velcro | 20% | BeT 0% |
| Prep Tape | 64% | BeT 0% |
| Put On Shoe | 92% | BeT 0% |

真实结果每配置1个训练种子、25次评估；仿真为3种子、各50次。低至20%的穿魔术贴结果应和摘要80–90%的代表任务一起保留，避免把所有任务写成同一成功区间（p8，表I–II）

### 消融与失败证据

四种仿真设置的动作块消融中，关闭时间集成时，k从1到100，聚合成功率约1%→44%；继续增大至接近整回合会损失反应能力。时间集成给ACT约3.3个百分点收益，VINN却下降，说明它不是所有策略均有效的通用滤波器。人类示范上去掉CVAE使仿真聚合成功率35.3%→2%，脚本数据几乎不变（p9–10，图8）

六人用户实验比较50 Hz与5 Hz，低频完成时间平均慢62%。这支持本文精细示教需要高频反馈，不能推导所有平台都必须以50 Hz训练。穿魔术贴失败来自提前闭爪及插接偏差，细暗目标在图像中占比很小，视觉难度与动作误差耦合（§V-C、VI-C）

## E. 不足与未来

**作者指出：**硬件负载、速度和夹爪形态限制能力；更复杂的拆糖纸、空中展开塑料袋尝试未学成，感知及数据不足是可能原因；本文没有解决任意物体、任意场景泛化（附录F）

**我的理解：**同构关节映射和时间集成值得先复用，但没有触觉时，视觉成功不等于接触力安全可控。当前DH116应先离线建立6主动轴、11总自由度的耦合模型与日志字段，重点检查拇指、食指、中指的映射；多轴运动尚未验收，不能直接输出ACT命令。D435i可作为外部RGB-D观测来源，但相机布局和训练分布改变后需重新实验

最小研究模块可先做同步数据结构、目标／实测状态区分和离线动作块回放；完整ALOHA需要四臂、夹爪、四相机、支架及计算设备，已有一只手不等于已经具备双臂系统。未来可比较动作块长度与接触阶段的关系，并为失败恢复收集明确示范

## 来源与核验边界

- [官方PDF](https://arxiv.org/pdf/2304.13705v1)；已逐段核对方法、实验、失败与局限，并渲染架构图及主结果表核对行列
- 以上论文数值来自对应PDF页码；当前官方仓库状态与论文实验设置分开，未运行其代码或任何机器人动作
- PDF许可：http://arxiv.org/licenses/nonexclusive-distrib/1.0/；仓库代码许可不自动覆盖PDF、数据和第三方依赖
- [正式发表来源](https://www.roboticsproceedings.org/rss19/p016.html)、[项目页](https://tonyzhaozh.github.io/aloha/)与官方仓库已核验；引用量仍待人工核验
- 关联专题：[[02 研究方向/机器人遥操作与动作重定向]]；[[02 研究方向/机器人数据采集与数据质量]]
