---
paper_id: P240
title: "Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild"
short_name: "JALA"
authors: ["Hao Luo", "Ye Wang", "Wanpeng Zhang", "Haoqi Yuan", "Yicheng Feng", "Haiweng Xu", "Sipeng Zheng", "Zongqing Lu"]
year: 2026
venue: "CVPR 2026:35047–35058"
arxiv: "2602.21736"
pdf: "01 论文文库/PDFs/08_数据与遥操作/JALA.pdf"
tags: ["Human_Video", "Latent_Action", "VLA", "Robot_Data"]
---

# JALA: Joint-Aligned Latent Action: Towards Scalable VLA Pretraining in the Wild

## A. 基本信息与研究问题

- 作者：Hao Luo、Ye Wang、Wanpeng Zhang、Haoqi Yuan、Yicheng Feng、Haiweng Xu、Sipeng Zheng、Zongqing Lu。
- 2026 年 2 月公开预印本；正式发表 [CVPR 2026，35047–35058 页](https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Joint-Aligned_Latent_Action_Towards_Scalable_VLA_Pretraining_in_the_Wild_CVPR_2026_paper.html)。[arXiv 2602.21736](https://arxiv.org/abs/2602.21736)；arXiv DOI：[10.48550/arXiv.2602.21736](https://doi.org/10.48550/arXiv.2602.21736)。正式会议独立 DOI 未核实。
- [正式 PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Luo_Joint-Aligned_Latent_Action_Towards_Scalable_VLA_Pretraining_in_the_Wild_CVPR_2026_paper.pdf) · [项目](https://research.beingbeyond.com/jala) · [官方代码](https://github.com/BeingBeyond/JALA) · [[01 论文文库/PDFs/08_数据与遥操作/JALA.pdf|本地 PDF]]。数据集 UniHand-Mix 的公开下载状态以项目页为准；不将论文中使用等同于已公开。
- 引用量：
- 引用量来源：

**问题。** 实验室里拍的人手视频有较准的三维动作，但数量与场景有限；互联网上的日常视频很多，手部轨迹却常不可靠。若每段视频都需要恢复精确手指关节，规模难上去。JALA 问能否学习“这两帧之间发生了什么动作变化”的 **latent action（隐式动作表示）**，同时用少量有动作标签的视频给它真实物理含义。

## B. 作者实际讨论的相关工作

- [[Being-H0 - Vision-Language-Action Pretraining from Large-Scale Human Videos|Being-H0]]（ICML 2026）：显式人手运动编码与预训练；JALA 在同一数据可用子集上检验更弱的动作标注需求（§2、表 3、5）。
- LAPA、UniVLA：由画面变化学习隐式动作，通常要根据该表示重建未来画面；本文认为画面细节重建会把背景噪声混入动作（§1–2）。
- GR00T N1.5：机器人数据预训练对照；对比范围依每张表的训练设置变化（§6）。

## C1. 核心贡献

1. **Joint-Aligned Latent Action。** 把从前后画面推得的隐式动作，与 VLA 根据当前画面和指令预测的运动表征对齐；有真实动作时再把该表征与动作对齐，无需强迫模型完整重建未来像素（§4、图 2）。
2. **UniHand-Mix。** 合并实验室和野外视频，约 **750 万段视频样本、超过 2000 小时**，既使用较精确的动作标签，也利用没有可靠动作标签的广泛场景（引言、§5）。样本数不是独立任务数。
3. **跨设置验证。** 在人手运动、LIBERO、RoboCasa、GR1 和三项真机任务分别测量收益；通过去除对齐、改变野外数据比例等消融检查原因（§6）。

## C2. 采用的方法

输入相邻视频画面及语言指令；**inverse dynamics model（逆动力学模型）**先由前后画面的变化提取紧凑向量，表示“可能发生的动作”。VLA 再从当前上下文预测这个向量，两个结果在同一空间对齐。如果数据本来有动作标签，还预测相应手部动作；没标签的视频仍可训练对齐目标。最后用少量机器人示范训练下游动作头，输出目标机器人的控制量。这样避开“先生成下一帧所有像素”的困难，但隐式向量仍需检验是否真代表动作而非相机移动（§4、图 1–2）。

## D. 实验与结果

- 两视角 LIBERO 的 JALA-dino 平均成功率 **96.9%**，Being-H0 为 90.3%、GR00T N1.5 为 93.9%（表 2）。表 3 的五随机种子消融里，完整 JALA 为 **96.9±0.3%**，去掉解耦更新仅 **56.6±2.0%**，说明稳定对齐训练不可少。
- RoboCasa 的合成示范设置 JALA **27.58%**、Being-H0 23.83%；GR1 桌面任务 **26.33%**、Being-H0 12.91%（表 5）。实验设置中的两种 RoboCasa 训练集不可混为一个结果。
- 真机用 Franka Research 3 + Inspire 灵巧手和 L515，相应三项多步骤任务每项 50 条示范、10 次测试。表 6 的指标是**平均子任务完成率**：JALA-dino 在见过／未见过桌布的 Put-Three-Obj 为 **60%／58%**，未见过笔色的 Wipe-Board 为 **80%**；不能改写成整任务成功率。
- 图 3 增加野外数据比例时下游效果持续改善；表 3 和图 3 的去模块消融支持“对齐＋稳定训练”的价值。有限硬件、少量测试和多项同时变更不足以证明任意网络视频都会带来收益。

## E. 不足与未来研究

**作者讨论的边界。** §7 指出野外视频缺少精确动作、跨本体映射仍是挑战；实验主要覆盖特定操作任务和设备，部分基准未报告误差条。隐式动作本身也不是可直接执行的机器人指令。

**本库分析。** 对 DH116 可采集 D435i 视频并建立少量准确腕部/手指动作锚点，比较“全量 3D 重建”和“隐式动作＋少量锚点”对下游抓取的帮助；需把相机位移、物体位移和人手动作区别开。NERO 双臂还要标记交接与相互作用，不可仅用单臂潜变量。下一步应按来源和质量分层，查看野外视频中无接触片段是否稀释有效动作。

**相关阅读。** [[Being-H0 - Vision-Language-Action Pretraining from Large-Scale Human Videos|Being-H0]] · [[VIPA-VLA - Spatial-Aware VLA Pretraining through Visual-Physical Alignment from Human Videos|VIPA-VLA]] · [[HuRo - Robotizing Human Videos for Scalable VLA Pretraining|HuRo]]。

## 核验范围

阅读 CVPR 正式 PDF 的引言、§2、§4–7、表 1–6、图 1–4 及附录；代码入口由作者官方仓库核实。引用量保持空白等待人工核验。
