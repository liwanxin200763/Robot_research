---
paper_id: P247
title: "Curating Demonstrations using Online Experience"
short_name: "Demo-SCORE"
authors: ["Annie S. Chen", "Alec M. Lessing", "Yuejiang Liu", "Chelsea Finn"]
year: 2025
venue: "Robotics: Science and Systems (RSS) 2025"
arxiv: "2503.03707"
doi: "10.15607/RSS.2025.XXI.071"
pdf: "01 论文文库/PDFs/08_数据与遥操作/Demo-SCORE.pdf"
tags: ["Data_Curation", "Demonstration_Selection", "Failure_Recovery"]
---

# Demo-SCORE: Curating Demonstrations using Online Experience

## A. 基本信息与研究问题

- 正式论文标题：Curating Demonstrations using Online Experience；方法简称 Demo-SCORE。作者：Annie S. Chen、Alec M. Lessing、Yuejiang Liu、Chelsea Finn。
- 2025 年 3 月首次公开；正式发表于 [RSS 2025](https://www.roboticsproceedings.org/rss21/p071.html)，[正式 DOI 10.15607/RSS.2025.XXI.071](https://doi.org/10.15607/RSS.2025.XXI.071)。[arXiv 2503.03707](https://arxiv.org/abs/2503.03707)。
- [官方论文页](https://www.roboticsproceedings.org/rss21/p071.html) · [官方项目与视频](https://anniesch.github.io/demo-score/) · [官方代码](https://github.com/alessing/demo-score) · [[01 论文文库/PDFs/08_数据与遥操作/Demo-SCORE.pdf|本地 arXiv 全文]]。代码含多个下游策略仓库的修改版，未在本机运行；无权重开放结论。
- 引用量：
- 引用量来源：

**问题。** 人工示范里即使都成功，也可能包含机器人难复现的抓法。整库模仿学习可能把这些脆弱策略一起学走。Demo-SCORE 让机器人先尝试任务，再用实际成功/失败判断哪些旧示范可靠。它并不从人类视频生成新机器人动作，而是为已有示范做**数据质量选择**。

## B. 作者实际讨论的相关工作

- Diffusion Policy、ACT：作为下游策略训练方法；Demo-SCORE 是能套在两者前面的数据筛选过程（§2、§5）。
- Autonomous Imitation Learning：把成功自采轨迹补入训练；Demo-SCORE 还反过来筛原有示范，所以不只是扩大数据量（§3–5）。
- Return-conditioned policies、训练损失筛选：作为文中对照；损失小或来自成功人类示范，不必然代表真机容易复现（§5）。

## C1. 核心贡献

1. 使用实际机器人 rollout（一次策略执行记录）的成功/失败，训练示范质量分类器；再给历史示范打分并过滤，不需要人工逐条判断抓法（§4、图 2）。
2. 在不同训练 checkpoint 的 rollout 之间做交叉验证，避免分类器只记住单一版本策略的行为；可按完整 episode 或动作片段选择（§4、表 II）。
3. 在仿真及 ALOHA 双臂真机验证“策略跑过以后再筛数据”比只加数据更有用；同时讨论初始策略全失败时的边界（§5–6）。

## C2. 采用的方法

先用混合质量示范训练初始策略，让它在目标任务运行并记录成功和失败。分类器学会分辨哪些状态—动作序列像成功策略，哪些像失败策略。不同训练阶段的策略给出略有不同的行为分布，利用一部分阶段训练、一部分验证，以减少过拟合。然后用分类器过滤原示范，重新训练最终策略并独立评估。**Action chunk（动作片段）**是连续若干步，可以只删坏片段；**episode（完整回合）**则整条保留或删除。分类器不是安全证明，仍需测试分布内真实执行（§4）。

## D. 实验与结果

- Robosuite 方孔插入和仿真 ALOHA 双手插销，用 Diffusion Policy/ACT，比全部示范、训练损失过滤、Auto-IL 和回报条件策略。筛后方孔平均成功率超过 **94%**，插销超过 **90%**；Auto-IL 对应为 88.2% 和 79.9%（§5、图 4）。
- 真机 ALOHA 的草莓、勺子、巧克力、马克笔及 Jellybeans 任务包含不同抓取策略。论文图 6 报多数真机任务比全数据基线增加约 **15–40 个百分点**；Jellybeans 初始策略不能完成整任务，因此改用五阶段得分训练分类器，不能与单步成功率混为一谈（§5、表 I）。
- 消融：不同 checkpoint 交叉验证很重要；少至每 checkpoint 10 次 rollout，方孔任务平均成功率仍约 **92%**，但这仍需真实执行与标注。按动作块和按整条示范筛选在文中仿真设置均有效（表 II–III）。

## E. 不足与未来研究

**作者明确限制（§6）。** 如果初始策略覆盖不了某种优秀示范，rollout 分类器看不到它，可能错删；若所有示范太差，初始策略完全不成功，方法会缺少正例；筛选也可能缩窄状态覆盖，因此作者建议主要用于后训练而非保留广覆盖的预训练。

**本库分析。** 对 NERO 双臂可先用安全仿真任务收集不同交接抓法，比较整回合与阶段筛选；DH116 真机如尚无法安全稳定执行，不能仅为获取分类器训练数据强行上机。D435i 视频要与关节、命令、失败原因和时间戳同步，才能追溯“示范不好”是视觉误判还是执行误差。与 [[CUPID - Curating Data your Robot Loves with Influence Functions|CUPID]] 不同，Demo-SCORE 训练判别器来识别成功策略的模式；CUPID 估计单条数据对期望回报的影响。可在同预算下比较两种筛选方案。

**相关阅读。** [[CUPID - Curating Data your Robot Loves with Influence Functions|CUPID]] · [[Quality over Quantity - Demonstration Curation via Influence Functions for Data-Centric Robot Learning|QoQ]] · [[DataMIL - Selecting Data for Robot Imitation Learning with Datamodels|DataMIL]]。

## 核验范围

阅读官方 arXiv 全文的引言、§2–6、图 2–6、表 I–III 与局限；RSS 正式出处和 DOI 由会议页核实，代码由作者项目页链接核实。引用量未自动填入。
