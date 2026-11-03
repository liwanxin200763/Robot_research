---
paper_id: P245
title: "CUPID: Curating Data your Robot Loves with Influence Functions"
short_name: "CUPID"
authors: ["Christopher Agia", "Rohan Sinha", "Jingyun Yang", "Rika Antonova", "Marco Pavone", "Haruki Nishimura", "Masha Itkina", "Jeannette Bohg"]
year: 2025
venue: "CoRL 2025; PMLR 305:2907–2932"
pdf: "01 论文文库/PDFs/08_数据与遥操作/CUPID.pdf"
tags: ["Data_Curation", "Demonstration_Selection", "Imitation_Learning"]
---

# CUPID: Curating Data your Robot Loves with Influence Functions

## A. 基本信息与研究问题

- 作者：Christopher Agia、Rohan Sinha、Jingyun Yang、Rika Antonova、Marco Pavone、Haruki Nishimura、Masha Itkina、Jeannette Bohg。
- 正式出处：[CoRL 2025，PMLR 305:2907–2932](https://proceedings.mlr.press/v305/agia25a.html)，会议于 2025 年 9 月 27–30 日举行；正式 DOI 和 arXiv ID 本次未核实，保持空白。
- [正式 PDF](https://raw.githubusercontent.com/mlresearch/v305/main/assets/agia25a/agia25a.pdf) · [官方代码](https://github.com/agiachris/cupid) · [[01 论文文库/PDFs/08_数据与遥操作/CUPID.pdf|本地 PDF]]。代码仓库含筛选流程与 PushT/RoboMimic 配置；未在本机运行，数据集与权重不能据论文默认视作公开。
- 引用量：
- 引用量来源：

**问题。** 机器人示范里既有明显失败，也有“看起来很好却会让策略学到脆弱习惯”的轨迹。只凭人工看视频或数据量，难判断哪条示范真正帮助闭环执行。CUPID 用机器人自己测试后的成功、失败和回报，估计每条训练示范对策略表现的影响。**Data curation（数据筛选）**在此不是生成更多示范，而是选出更有用的已有示范。

## B. 作者实际讨论的相关工作

- DemInf：用状态多样性和动作可预测性评价数据；CUPID 将评价直接联系到目标策略的闭环表现（§2、§6）。
- Demo-SCORE：依据在线经验评估示范质量；CUPID 特别讨论“全失败”“策略偏好与分布转移”时简单筛选的局限（§6）。
- Diffusion Policy、π0：作为下游策略，检验筛选后重新训练是否有益，而非 CUPID 自己发明的策略架构（§5–6）。

## C1. 核心贡献

1. 用 **influence function（影响函数）**思路估计“提高一条训练示范权重后，策略测试回报会怎样变化”；避免对每条示范都完整重训一次（§3–4）。
2. 同时解决两类选择：删除可能伤害性能的原有示范，以及从新采集的轨迹中挑选最有价值的加入训练（§4）。
3. 用 RoboMimic 仿真和 Franka FR3 真机验证数据价值随任务、策略和测试分布变化，而非设一个通用的“好看”分数（§5–6）。

## C2. 采用的方法

先在全部示范上训练初始策略，并让策略在目标任务里运行，记录测试回合（rollout，即一次实际尝试）的动作和结果。影响函数近似计算：某条训练轨迹对模型参数的作用方向，是否会让这些测试回合的期望回报更高。按估计分数给完整示范排序，选择保留或补充的子集，再**重新训练并独立评估**。输出是筛后的数据和新策略，不是机器人动作重定向器。若只看原始示范是否成功，就无法识别环境改变后哪种策略更稳（§3–4）。

## D. 实验与结果

- RoboMimic 评估 Lift、Square、Transport 等混合质量示范，以及真机 Figure-8 系绳、TuckBox、Bookshelf。仿真对比随机选择、DemInf、Demo-SCORE 等，真机还检验 π0 的后训练（§5–6、图 2、图 4）。
- Transport MH 中，用原有 **300 条示范的不到 33%**，能训练到与强扩散策略相当的表现；这只针对该数据配置，不可概括成所有任务数据都可以删掉 2/3（§6.1、图 2）。
- Figure-8 真机中，CUPID 筛选后的扩散策略较原策略提高约 **38%**（按论文对过滤与新增选择的平均表述）；用筛选数据对 π0 后训练提升约 **54%**（§6.1、图 4）。百分数口径需读图注，不应转述为绝对百分点。
- 消融与反例同样重要：Lift MH 高度冗余，约 15% 数据可维持表现；Square MH 去掉很多示范反会变差。TuckBox 在测试分布改变后，常见的滑动策略失效；依赖单纯“训练时看着成功”的筛选会错选（§6、图 2、4）。这说明**数据价值依目标分布而变**。

## E. 不足与未来研究

**作者明确限制（§7）。** 预先指定筛选数量 k，如何确定合适预算仍未解决；数据是否冗余、是否含有害轨迹决定方法收益；影响估计尚不能直接解释示范的具体错误原因。需要初始策略和测试 rollout，计算与真实执行成本都不为零。

**本库分析。** 对 DH116，可先固定少量安全、可信的真实评估回合，将接触失败、抓空、滑落和成功分开；筛选目标应是对目标物体的成功，而非视频视觉相似度。D435i 图像不足以解释力控失败，应同步目标动作、实际关节状态与时间戳。NERO 双臂可能有协作失败，需整回合与阶段指标并用。与 [[DataMIL - Selecting Data for Robot Imitation Learning with Datamodels|DataMIL]]、[[Quality over Quantity - Demonstration Curation via Influence Functions for Data-Centric Robot Learning|QoQ]] 对比时固定策略、评估集与筛选预算，避免“更少数据胜出”来自实验条件变化。

**相关阅读。** [[HuRo - Robotizing Human Videos for Scalable VLA Pretraining|HuRo]]（增加候选数据） → CUPID（按真实执行筛选） → [[Quality over Quantity - Demonstration Curation via Influence Functions for Data-Centric Robot Learning|QoQ]]。

## 核验范围

阅读 CoRL/PMLR 正式 PDF 的引言、方法、仿真及真机实验、图 2/4 与局限；作者官方仓库核对公开代码。引用量留空，由人工核验。
