# Ego4WAM：第一视角人类数据如何帮助机器人学习

## 基本信息

- 英文标题：Ego4WAM: What Matters When Scaling Egocentric Human Data for Robot Learning?
- 作者：Zhihao Sun、Liu Liu、Xinjiang Wang、Haoyi Jiang、Wei Feng、Huiqiang Zhang、Xiaosong Jia、Zhizhong Su、Zuxuan Wu
- 年份：2026
- 发表 venue：arXiv 预印本
- 论文类型：数据与训练策略研究；World-Action Model
- 研究方向：数据与遥操作；VLA；跨执行体泛化
- 关键词：Egocentric Human Data；Human-Robot Alignment；World-Action Model；Video-Only Pretraining；RoboDojo
- 论文链接：[arXiv 论文](https://arxiv.org/abs/2609.40341)
- DOI：[10.48550/arXiv.2609.40341](https://doi.org/10.48550/arXiv.2609.40341)
- arXiv：[2609.40341](https://arxiv.org/abs/2609.40341)
- 项目主页：[作者项目页](https://sunzhihao18.github.io/Ego4WAM/)
- 代码：[作者链接的 GitHub](https://github.com/HorizonRobotics/Ego4WAM)（当前仓库仅有 README，训练代码未公开）
- 本地 PDF：—
- 引用量：
- 引用量来源：Google Scholar

## 领域地图级总结

**问题与缺口。**大规模第一视角人类数据是否有用，不能只看时长；人机动作对齐、任务多样性、标签有无与数据进入训练的阶段可能决定效果。本文固定 World-Action Model 骨干，比较这些数据因素，主要位于“数据 → 跨执行体训练 → 泛化”。

**方法与数据。**作者组织机器人对齐的视频—动作数据、跨任务视频—动作数据与仅视频数据，在共享骨干中同时学习未来视觉与动作。项目页给出约 4 小时机器人对齐数据、12,000 小时多任务视频—动作数据、120,000 小时仅视频数据的分层规模；这些是不同监督层级，不能相加称为同一种机器人示范。具体采集、过滤与增强需在精读时核对。

**观测与动作。**项目页描述共享动作空间容纳机器人关节、夹爪、末端监督及人类第一视角可恢复的动作信号；准确输入通道、坐标系和输出维度待查方法章节。仅视频预训练不需要人类动作标签，最终机器人控制仍需要动作监督。

**评测与结果。**作者在 RoboDojo 和真实机器人上闭环评测。项目页给出真实“放入篮子”任务中，使用对齐人类数据后物体 OOD 成功率 **10%→60%**、场景 OOD **0%→20%**；RoboDojo 仅视频预训练使平均分 **6.39→14.13**、成功率 **3.15%→9.45%**。这些是各自特定设置的比较，不与其他论文直接横比。作者还报告长尾任务过多可能产生负迁移。

**局限与研究价值。**项目页指出 Memory 和 Open 类别较弱；作者尚未证明只增加人类视频小时数就稳定提升所有任务。它与 [[02_论文/01_VLA/ACE-Ego-0：统一第一视角人类与机器人数据用于VLA预训练|ACE-Ego-0]] 的伪动作对齐路线可形成数据配方对照：普通夹爪双臂任务先比较对齐程度、任务覆盖与无动作视频各自的增益。此处是研究设计建议，非论文已经验证的双臂结论。
