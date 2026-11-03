---
paper_id: P244
title: "From Human Videos to Robot Manipulation: A Survey on Scalable Vision-Language-Action Learning with Human-Centric Data"
short_name: "Human-video VLA survey"
authors: ["Zhiyuan Feng", "Qixiu Li", "Huizhi Liang", "Rushuai Yang", "Yichao Shen", "Zhiying Du", "Zhaowei Zhang", "Yu Deng", "Li Zhao", "Hao Zhao", "Zongqing Lu", "Oier Mees", "Marc Pollefeys", "Jiaolong Yang", "Baining Guo"]
year: 2026
venue: "IJCAI 2026 Survey Track:7845–7854"
doi: "10.24963/ijcai.2026/871"
pdf: "01 论文文库/PDFs/08_数据与遥操作/Human-Video-Survey.pdf"
tags: ["Survey", "Human_Video", "VLA", "Robot_Data"]
---

# From Human Videos to Robot Manipulation: A Survey on Scalable Vision-Language-Action Learning with Human-Centric Data

## A. 基本信息与研究问题

- 作者：Zhiyuan Feng、Qixiu Li、Huizhi Liang、Rushuai Yang、Yichao Shen、Zhiying Du、Zhaowei Zhang、Yu Deng、Li Zhao、Hao Zhao、Zongqing Lu、Oier Mees、Marc Pollefeys、Jiaolong Yang、Baining Guo。
- 正式发表于 [IJCAI 2026 Survey Track，7845–7854 页](https://ijcai.org/proceedings/2026/871)，会议月份 2026 年 8 月；[DOI 10.24963/ijcai.2026/871](https://doi.org/10.24963/ijcai.2026/871)。本次未确认对应 arXiv 条目，保持未填。
- [会议 PDF](https://ijcai.org/proceedings/2026/0871.pdf) · [[01 论文文库/PDFs/08_数据与遥操作/Human-Video-Survey.pdf|本地 PDF]]。这是综述，没有本篇模型代码、数据集或权重；不把被综述论文的仓库写成其“官方代码”。
- 引用量：
- 引用量来源：

**研究问题。** 人类视频海量但缺少机器人可执行动作。不同论文看似都“用视频学机器人”，实际得到的可能只是画面变化、未来图像、二维轨迹或三维手/物位姿。本文按**从视频中提取什么动作相关信号**整理方法，帮助判断一项工作究竟打通了哪一步。

## B. 作者实际讨论的代表性相关工作

- LAPA、IGOR、UniVLA：从前后帧获得 latent action，适合缺少关节标签的视频，但动作含义未必明确（§3.1）。
- 视频预测/世界模型方向：用未来画面学习环境变化，再给策略提供先验；画面预测准确不等于执行动作准确（§3.2）。
- [[Being-H0 - Vision-Language-Action Pretraining from Large-Scale Human Videos|Being-H0]]、DexMV、DexVIP：使用三维人手结构或姿态，让动作与几何有更清楚的联系，也更依赖姿态估计质量（§3.4）。
- Ego4D、EPIC-KITCHENS 等：提供大规模 RGB 视频，但常缺少带尺度的三维动作标签（§4、表 2）。

## C1. 核心贡献

提出四条互补的“视频→动作监督”路线，并在表 1–2 比较中间表示与数据：① **隐式动作**，把前后画面变化压成向量；② **世界模型**，预测未来画面或状态；③ **显式二维线索**，跟踪图像上的手、物或点；④ **显式三维结构**，恢复手、腕、物体位姿。它还把瓶颈归纳为长视频切成可训练 episode、人机本体及视角差异，以及真实部署相关的评价设计（§3–5）。

## C2. 采用的方法

这是一篇文献比较，不提出新的机器人控制器。作者先从 VLA 的训练形式出发，解释策略需要画面、机器人状态、语言及未来动作；再逐类检查人类视频能提供什么监督。**Episode** 是有起止和任务指令的一段训练记录；原始长视频不能直接视作若干准确 episode。**二维轨迹**只说明图像坐标如何变，缺少深度；**三维姿态**含空间几何，但手部重建和相机标定容易出错；**隐式动作**可扩规模，却难解释和执行。最后按照有无三维标签及拍摄是否脚本化，对数据源分类（§2–4）。

## D. 证据与适用范围

本文是 Survey Track 综述，**没有新模型训练结果、消融或真机成功率**；表 1–2 汇总的是已有论文，不能写成作者复现的对比实验。它的证据价值是比较路线与数据可得性，而非证明某一种方法在全部平台上最优（§3–4）。

作者在§5建议未来报告固定机器人数据预算下的迁移效果、未见物体和场景拆分，以及视角和本体变化下的鲁棒性；只在 LIBERO 等固定仿真任务上取得提升，不能直接推断真机部署性能。

## E. 不足与未来研究

**作者指出的开放问题（§5–6）。** 野外长视频的动作分段与标签质量、跨视角和跨机械结构的映射，以及缺少真正反映部署的评价协议仍未解决。RGB 视频尤其缺少接触力、触觉与执行反馈。

**本库分析。** 对 DH116、NERO 与 AgileX，应先明确目标是学视觉先验、生成机器人轨迹，还是直接提升闭环成功率。D435i 帧和人手关键点只覆盖观察层；只有映射后的目标关节、实际反馈及时间戳齐全，才可能组成可执行示范。优先按本文四条路线建立数据来源与缺失信号表，再用真机固定示范预算验证增益。

**相关阅读。** [[Being-H0 - Vision-Language-Action Pretraining from Large-Scale Human Videos|Being-H0]] · [[JALA - Joint-Aligned Latent Action Towards Scalable VLA Pretraining in the Wild|JALA]] · [[VIPA-VLA - Spatial-Aware VLA Pretraining through Visual-Physical Alignment from Human Videos|VIPA-VLA]] · [[HuRo - Robotizing Human Videos for Scalable VLA Pretraining|HuRo]]。

## 核验范围

阅读 IJCAI 正式 PDF 全文的§1–6及表 1–2；正式作者和 DOI 以 IJCAI 论文页为准。引用量留空等待人工核验。
