---
paper_id: P241
title: "Spatial-Aware VLA Pretraining through Visual-Physical Alignment from Human Videos"
short_name: "VIPA-VLA"
authors: ["Yicheng Feng", "Wanpeng Zhang", "Ye Wang", "Hao Luo", "Haoqi Yuan", "Sipeng Zheng", "Zongqing Lu"]
year: 2026
venue: "CVPR 2026:712–723"
arxiv: "2512.13080"
pdf: "01 论文文库/PDFs/08_数据与遥操作/VIPA-VLA-CVPR.pdf"
tags: ["Human_Video", "VLA", "Visual_Physical_Alignment", "Robot_Data"]
---

# VIPA-VLA: Spatial-Aware VLA Pretraining through Visual-Physical Alignment from Human Videos

## A. 基本信息与研究问题

- 作者：Yicheng Feng、Wanpeng Zhang、Ye Wang、Hao Luo、Haoqi Yuan、Sipeng Zheng、Zongqing Lu。
- 2025 年 12 月首次发布预印本；正式发表于 [CVPR 2026，712–723 页](https://openaccess.thecvf.com/content/CVPR2026/html/Feng_Spatial-Aware_VLA_Pretraining_through_Visual-Physical_Alignment_from_Human_Videos_CVPR_2026_paper.html)。[arXiv 2512.13080](https://arxiv.org/abs/2512.13080)；[arXiv DOI](https://doi.org/10.48550/arXiv.2512.13080)；未核实独立会议 DOI。
- [正式 PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_Spatial-Aware_VLA_Pretraining_through_Visual-Physical_Alignment_from_Human_Videos_CVPR_2026_paper.pdf) · [作者项目页](https://research.beingbeyond.com/vipa-vla) · [官方代码](https://github.com/BeingBeyond/VIPA-VLA) · [[01 论文文库/PDFs/08_数据与遥操作/VIPA-VLA-CVPR.pdf|本地 PDF]]。Hand3D 在论文中构建；公开下载入口需按官方仓库另行确认，不将“使用过”写作“已开放”。
- 引用量：
- 引用量来源：

**问题。** 普通 VLA 看到的是二维像素，但动作要在三维空间完成。物体在画面里靠近，不一定在真实空间里靠近。本文想用人类操作视频教模型把画面位置、三维结构和人手轨迹联系起来，再迁移到机器人动作。

## B. 作者实际讨论的相关工作

- [[Being-H0 - Vision-Language-Action Pretraining from Large-Scale Human Videos|Being-H0]]（ICML 2026）：从人手运动中学习物理先验；VIPA-VLA 更突出二维视觉与三维几何对齐，并用它做真机基线（§2、表 5）。
- SpatialVLA、TraceVLA、MolmoAct：在空间表征上增强机器人策略，文中作为 LIBERO 对照；训练信息源与方式各异（§2、表 3）。
- GR00T N1.5、π0.5：已用机器人数据预训练的强基线，不应把所有差异归因于视觉编码器（§4）。

## C1. 核心贡献

1. **Hand3D 数据集。** 从多样人类操作视频提取三维视觉标注与人手运动标注，使“画面中的点”和“物理空间中的运动”能成对训练（§3、图 1）。
2. **Visual-Physical Alignment（视觉—物理对齐）。** 分阶段先学习二维画面到三维结构，再学习三维人手动作，不用等机器人数据出现后才学习空间感（§3）。
3. **双视觉编码器。** 一路识别物体语义，一路处理三维空间线索，融合后给动作头；这与只从二维图像直接预测控制量不同（图 2–4）。

## C2. 采用的方法

第一阶段从人类视频生成相机、手物关系等三维视觉标注，让视觉主干同时看到原始画面和可核对的空间位置。第二阶段把三维腕部轨迹离散成动作 token，训练它预测接下来的人手运动。第三阶段使用机器人示范进行 post-training（后训练），把获得的空间理解转成目标机器人动作。动作头用 flow matching（流匹配：从噪声逐步形成连续动作）输出控制序列；这并非把人手关节角直接下发给机器人（§3、作者项目页）。

## D. 实验与结果

- 在 LIBERO 四任务组、RoboCasa 24 任务和 Franka Research 3 + Inspire 手真机测试。RoboCasa 每任务 50 条人类示范、每任务 50 次评估；论文还比较单视角与双视角（§4、表 3–4）。
- RoboCasa 总平均成功率 **45.8%**，π0.5 为 41.4%，GR00T N1 为 36.0%；Doors/Drawers 类为 **67.7%**，π0.5 为 57.8%（表 4）。
- 真机 Wipe-Board 的**子任务／整任务**完成率为 **83%／60%**，Being-H0 为 40%／10%；Water-Plant 为 57%／50%。Put-Three-Obj 为 52%／10%，其中整任务成功率**低于** GR00T N1.5 的 40%，不能概括为全部真机任务都最好（表 5）。每项仅 10 次试验。
- LIBERO 表 7：完整模型平均 **92.4%**，去掉空间预训练为 91.2%，去掉双编码器为 90.4%。论文图 7 显示其失败更多发生于小物体精细抓取的偏移，空间对齐不能代替接触控制。

## E. 不足与未来研究

**作者讨论的边界。** 结论提出未来结合机器人数据预训练；图 7 显示细小物体抓取仍会因控制偏差失败。Hand3D 的三维标注由估计流程产生，并非所有片段都是真值测量。

**本库分析。** D435i 可提供深度线索，但深度与 RGB 配准、遮挡和手指接触误差需要实测；若要映射到 DH116，先构建目标指尖位置及关节限制。NERO 双臂还需共享物体坐标和双臂碰撞检查。可按固定示范预算比较 RGB-only、RGB-D 和三维标注预训练的效果，并把抓错物体、对准误差与接触失稳分开记录。

**相关阅读。** [[Being-H0 - Vision-Language-Action Pretraining from Large-Scale Human Videos|Being-H0]] · [[JALA - Joint-Aligned Latent Action Towards Scalable VLA Pretraining in the Wild|JALA]] · [[HuRo - Robotizing Human Videos for Scalable VLA Pretraining|HuRo]]。

## 核验范围

阅读 CVPR 正式 PDF 的引言、方法、实验、消融、失败例与结论；核对作者项目页和官方仓库。引用量未自动填入。
