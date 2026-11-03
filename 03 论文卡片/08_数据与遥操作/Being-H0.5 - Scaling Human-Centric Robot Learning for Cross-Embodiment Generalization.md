---
paper_id: P239
title: "Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization"
short_name: "Being-H0.5"
authors: ["Hao Luo", "Ye Wang", "Wanpeng Zhang", "Sipeng Zheng", "Ziheng Xi", "Chaoyi Xu", "Haiweng Xu", "Haoqi Yuan", "Chi Zhang", "Yiqing Wang", "Yicheng Feng", "Zongqing Lu"]
year: 2026
venue: "CoRL 2026（作者代码库宣布录用；正式论文条目待核）"
arxiv: "2601.12993"
pdf: "01 论文文库/PDFs/08_数据与遥操作/Being-H0.5.pdf"
tags: ["Robot_Data", "Human_Video", "VLA", "Cross_Embodiment"]
---

# Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization

## A. 基本信息与研究问题

- 作者：Hao Luo、Ye Wang、Wanpeng Zhang、Sipeng Zheng、Ziheng Xi、Chaoyi Xu、Haiweng Xu、Haoqi Yuan、Chi Zhang、Yiqing Wang、Yicheng Feng、Zongqing Lu。
- 首次公开：2026 年 1 月；[arXiv 2601.12993](https://arxiv.org/abs/2601.12993)，[arXiv DOI](https://doi.org/10.48550/arXiv.2601.12993)。作者[官方代码库](https://github.com/BeingBeyond/Being-H)记录 CoRL 2026 录用；尚未据此编造 proceedings 页码或正式 DOI。
- [论文 PDF](https://arxiv.org/pdf/2601.12993) · [项目主页](https://research.beingbeyond.com/being-h05) · [官方代码、训练文档](https://github.com/BeingBeyond/Being-H/tree/main/Being-H05) · [官方数据入口](https://github.com/BeingBeyond/Being-H) · [[01 论文文库/PDFs/08_数据与遥操作/Being-H0.5.pdf|本地 PDF]]。模型权重入口由官方仓库导航；本库未实际运行。
- 引用量：
- 引用量来源：

**研究问题。** 不同机器人的关节数、末端形态和控制频率不同，直接把一个机器人采集的动作向量给另一个机器人通常不可执行，这就是 **cross-embodiment（跨本体）**困难。Being-H0 已说明人手视频可提供运动先验；本篇进一步问：人、双臂灵巧手、单臂夹爪等数据能否放入同一训练体系，让少数据平台也受益？

## B. 作者实际讨论的相关工作

- [[Being-H0 - Vision-Language-Action Pretraining from Large-Scale Human Videos|Being-H0]]（ICML 2026）：由人手视频预训练再适配机器人；本篇扩大数据与本体范围，改进统一动作接口（引言）。
- Open X-Embodiment（2024）、DROID（2024）、BridgeData（2022/2023）：扩大机器人数据来源，但各自的关节与控制表示异构（§2、§3）。
- π0.5、GR00T-N1 等 VLA：仿真及真机对照；不能从不同预训练数据量的比较单独推出架构优劣（§7）。

## C1. 核心贡献

1. **UniHand-2.0 数据配方。** 论文统计约 **400M 样本、超过 35,000 小时**，包括约 16,000 小时人类数据与 14,000 小时机器人交互数据，并覆盖 30 个满足统计门槛的机器人本体；余量还有视觉文字数据，故两种小时数不能相加当成总量（§3、图 2–4）。
2. **Unified Action Space（统一动作空间）。** 将不同平台的动作拆成有共同语义的槽位，同时保留机型专属信息，减少“向量第 7 维在每台机器人含义不同”的冲突（§4）。
3. **MoF 与统一训练。** Mixture-of-Flow（流模型专家混合）让共享运动规律和具体本体的控制差异分工学习；Manifold-Preserving Gating 和 Universal Async Chunking 分别处理感知变化与不同控制延迟（§4–5）。

## C2. 采用的方法

先整理人手运动、机器人轨迹和一般视觉语言任务，统一视觉、文字与运动的样本结构。动作不是强行补齐为完全相同的关节角，而是按意义映射到共享槽位并标记哪个平台提供哪些通道。模型对不同样本学习“看见什么、任务是什么、下一段动作该如何变化”；动作专家按本体差异生成连续动作块。最后对目标机器人用该平台的示范后训练，并用真实控制延迟的异步执行策略部署。这里的 **embodiment（本体）**指机械结构、传感器及动作接口的组合；共享抽象不等于免去标定或安全检查（§3–6）。

相较 Being-H0，本篇不只把人手先验转成单一机器人的动作头，而是把多本体数据本身作为联合训练对象；统一动作空间是核心桥梁，数据增加与结构改变同时发生。

## D. 实验与结果

- 真机部署在 PND Adam-U、Franka+Inspire、Unitree G1、BeingBeyond D1 和 LeRobot SO-101 五种平台；图 9–10 含不同任务的专门模型与联合模型。机器人平台的成功率不能照搬到 DH116 或 NERO。
- LIBERO 四套任务专门模型平均 **98.9%**，其中 Long 为 97.4%；跨 LIBERO 与 RoboCasa 联合训练的模型平均 **97.6%**。专门模型使用 224×224 RGB、2B 主干；表 4 的 π0.5 为 96.9%，但训练资料和设定不同（§7.2、表 4）。
- RoboCasa 24 个任务，专门模型平均 **53.9%**、联合模型 **53.3%**，π0.5 对照 41.4%。每任务 50 次评估，仍需检查训练示范及硬件差异（表 5）。
- 表 6–7 的 5-shot（每任务仅五条示范）适配对比和图 11–13 的动作专家、门控及异步动作消融支持各模块的实际作用；这些消融不证明所有机器人均可零样本迁移。论文报告部分未见本体任务可零样本完成，但成功率仍低，不能写成稳定部署（§7、附录）。

## E. 不足与未来研究

**论文实验呈现的边界。** §7 报告未见本体的零样本成功率低于训练分布内表现，动作精度也较不可靠；消融分析指出缺少稳定机制时，长时序任务会出现误差累积，双臂协调会在观测噪声或视角变化下变得脆弱。§8 结论未单列作者声明的局限；数据与计算成本属于本库的复现分析，不能当作作者原话。

**本库分析。** 数据来自多种来源，采样比例、动作噪声与平台不平衡可能同时影响结果，单看总小时数无法衡量对目标平台的贡献。对 DH116，应先明确有效自由度、耦合关系和动作槽位，再映射人手运动；对 NERO 与 AgileX 应分别记录两臂、夹爪命令和执行反馈。以 D435i 采集的视频仍缺少触觉与实时力反馈，需另建对应标签。建议固定平台和数据预算，对比“只加数量”“加统一表示”“加质量筛选”的独立作用。

**相关阅读。** [[Being-H0 - Vision-Language-Action Pretraining from Large-Scale Human Videos|Being-H0]] · [[HuRo - Robotizing Human Videos for Scalable VLA Pretraining|HuRo]] · [[Quality over Quantity - Demonstration Curation via Influence Functions for Data-Centric Robot Learning|QoQ]]。

## 核验范围

阅读官方 arXiv PDF 的引言、数据、方法、§7 实验、消融及附录；官方 GitHub 核对代码和录用公告。正式 CoRL 出版记录与独立 DOI 待核，引用量只由人工填写。
