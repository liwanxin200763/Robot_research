---
paper_id: P242
title: "HuRo: Robotizing Human Videos for Scalable VLA Pretraining"
short_name: "HuRo"
authors: ["Jinho Jeong", "Se June Joo", "Jaehyun Kang", "Dongyun Kim", "Yena Kim", "Hanjung Kim", "Seon Joo Kim"]
year: 2026
venue: "CoRL 2026（作者官方代码库标注；正式 proceedings 待核）"
arxiv: "2609.10706"
pdf: "01 论文文库/PDFs/08_数据与遥操作/HuRo.pdf"
tags: ["Human_Video", "Robotization", "Data_Generation", "VLA"]
---

# HuRo: Robotizing Human Videos for Scalable VLA Pretraining

## A. 基本信息与研究问题

- 作者：Jinho Jeong、Se June Joo、Jaehyun Kang、Dongyun Kim、Yena Kim、Hanjung Kim、Seon Joo Kim。
- 2026 年 9 月公开；[arXiv 2609.10706](https://arxiv.org/abs/2609.10706)，[arXiv DOI](https://doi.org/10.48550/arXiv.2609.10706)。[官方仓库](https://github.com/3587jjh/HuRo)标注 CoRL 2026，正式出版页码和 DOI 待核。
- [论文 PDF](https://arxiv.org/pdf/2609.10706) · [作者项目](https://3587jjh.github.io/HuRo/) · [官方代码](https://github.com/3587jjh/HuRo) · [数据和输出格式入口](https://github.com/3587jjh/HuRo/tree/main/examples) · [[01 论文文库/PDFs/08_数据与遥操作/HuRo.pdf|本地 PDF]]。代码库实际公开数据处理流水线，本文未在本库运行其硬件依赖。
- 引用量：
- 引用量来源：

**问题。** 人类视频显示人手，不显示目标机器人的形状；人手轨迹也不是机器人的关节命令。HuRo 研究能否同时转换**观察画面**和**动作轨迹**，把异构的人类视频变成在形式上接近机器人训练集的数据。这里的 **robotization（机器人化）**是数据转换，不是说机器人真实执行了这些片段。

## B. 作者实际讨论的相关工作

- H2R、Masquerade：在人类视频中替换可见的手或预测机器人端点，主要改善视觉或部分监督；HuRo 同时生成机器人画面和目标动作（§2）。
- VITRA、EgoScale：从人手视频获取动作监督，但仍主要保留人的观察画面；HuRo 检查双侧对齐是否带来收益（§2、附录 B）。
- 论文也讨论视频生成式视觉转换；它们生成像机器人操作的画面，与可执行关节轨迹不是同一种输出（§2）。

## C1. 核心贡献

1. **完整 robotization 流水线。** 从原始长视频估相机、人手与操作片段，补足来源缺失的标注，再将人手映射到目标机器人，同时去掉人手并在图像中叠加机器人外观（§3、图 2）。
2. **HuRo 数据集。** 来自 EgoDex、EgoVerse、Ego4D、Ego10K、EPIC-Kitchens 五个来源，约 **63 万条机器人化 episode、1.42 亿处理帧**。episode 指有明确起止和语言任务的一段训练记录，不等于原始视频数（摘要、附录表 5）。
3. **真实机器人规模验证。** 不是只看转换视频是否逼真，还在四类操作任务中检查预训练数据增多后真机表现，以及只改视觉和同时改动作的区别（§4）。

## C2. 采用的方法

原始视频先估相机内外参和三维手部姿态，分出操作片段并生成语言任务。**Retargeting（动作重定向）**根据目标机器人的运动学把人手和手腕运动转为机器人关节与末端目标；缺少标注的片段先由估计模型补齐。视觉侧识别人手区域，修补背景，再渲染目标机器人覆盖到相应位置。最后把图像、语言、机器人状态和动作打包成 LeRobot 格式的 episode（§3、官方 README）。它输出“机器人对齐的训练数据”，并不保证每条轨迹满足接触力学或能在真机安全完成。

## D. 实验与结果

- 目标策略基于 GR00T-N1.6-3B，预测 40 步动作块。四项 ALLEX 真机任务分别为苹果抓放（43 条后训练示范）、叠杯（40）、杯面交接（16）、微波炉装载（20）；OOD 条件含物体位置及视觉变化。苹果为二元成功，其余按阶段完成度打分（§3–4、附录 A）。
- 随着 HuRo 预训练比例增加，四任务总体完成度从无预训练的 **51.5%** 升到完整数据的 **80.3%**；OOD 从 **34.9%** 升到 **72.2%**（摘要、图 3）。这两个分数聚合了二元和阶段指标，不宜称为“所有任务成功率”。
- 视觉机器人化在 OOD 下有帮助：10% 叠加版优于 100% 不叠加版；带重定向动作的端到端预训练比仅视觉迁移有效（§4、图 4–5）。附录表 3 的 Masquerade 风格比较在另一任务上给出 ID **86.1**、OOD **63.9**，与主实验总分分母不同。
- 作者明确列出数据处理质量诊断与保留率（附录表 8–10），提醒大规模视频转换会丢失或污染部分样本。没有直接证明每条合成数据都可被机器人安全执行。

## E. 不足与未来研究

**作者明确局限（§6）。** 机器人叠加未显式处理机器人与场景的遮挡，图像修补会留下伪影；数据没有力/触觉监督；运动学重定向未建模自身碰撞及物理接触。因此真实可行性仍需下游验证。

**本库分析。** 与 Being-H0 的“学习人手运动先验”不同，HuRo 明确输出机器人外观和机器人动作标签，适合测试“视频能否代替部分遥操作采集”。对 DH116，先建立可靠 URDF/关节限位和手指耦合映射，再用离线重定向数据做仿真可行性筛查；在 D435i 图像上检查渲染遮挡，不能直接用叠加画面宣称真机数据。NERO 双臂还需双臂碰撞与同步。建议对每条转换轨迹记录来源、估计置信度、碰撞/接触测试和真实执行反馈，再与 [[DataMIL - Selecting Data for Robot Imitation Learning with Datamodels|DataMIL]] 一类质量选择方法结合。

**相关阅读。** [[Being-H0 - Vision-Language-Action Pretraining from Large-Scale Human Videos|Being-H0]] · [[JALA - Joint-Aligned Latent Action Towards Scalable VLA Pretraining in the Wild|JALA]] · [[Scalable Vision-Language-Action Model Pretraining for Robotic Manipulation with Real-Life Human Activity Videos|VITRA]]。

## 核验范围

阅读 arXiv 全文的引言、方法、§4 实验、附录数据诊断及§6 局限；代码公开状态依据作者 GitHub README。正式 CoRL 出版条目待核；引用量留给人工核验。
