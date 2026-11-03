---
paper_id: P238
title: "Vision-Language-Action Pretraining from Large-Scale Human Videos"
short_name: "Being-H0"
authors: ["Hao Luo", "Yicheng Feng", "Wanpeng Zhang", "Sipeng Zheng", "Ye Wang", "Haoqi Yuan", "Jiazheng Liu", "Chaoyi Xu", "Haiweng Xu", "Qin Jin", "Zongqing Lu"]
year: 2026
venue: "ICML 2026; PMLR 306:82265–82293"
arxiv: "2507.15597"
pdf: "01 论文文库/PDFs/08_数据与遥操作/Being-H0.pdf"
tags: ["Robot_Data", "Human_Video", "VLA", "Dexterous_Manipulation"]
---

# Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos

## A. 基本信息与研究问题

- 正式标题：Vision-Language-Action Pretraining from Large-Scale Human Videos；常用名称 Being-H0。2025 年 7 月的 arXiv 版本在标题前有 “Being-H0:”，正式 ICML 版本去掉了此前缀。
- 作者：Hao Luo、Yicheng Feng、Wanpeng Zhang、Sipeng Zheng、Ye Wang、Haoqi Yuan、Jiazheng Liu、Chaoyi Xu、Haiweng Xu、Qin Jin、Zongqing Lu。作者名单以正式会议 PDF 首页为准，区别于早期预印本。
- 首次公开：2025 年 7 月；正式出处：[ICML 2026，PMLR 第 306 卷，82265–82293 页](https://proceedings.mlr.press/v306/luo26e.html)。[arXiv 2507.15597](https://arxiv.org/abs/2507.15597)；arXiv DOI：[10.48550/arXiv.2507.15597](https://doi.org/10.48550/arXiv.2507.15597)。未核实独立会议 DOI。
- [正式论文 PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/luo26e/luo26e.pdf) · [项目主页](https://research.beingbeyond.com/being-h0) · [官方代码](https://github.com/BeingBeyond/Being-H0) · [模型与数据入口](https://github.com/BeingBeyond/Being-H0#model-checkpoints) · [[01 论文文库/PDFs/08_数据与遥操作/Being-H0.pdf|本地 PDF]]。
- 引用量：
- 引用量来源：

**研究问题。** VLA（视觉—语言—动作模型）看图像和任务文字后输出机器人动作。常用机器人遥操作示范昂贵、场景有限；灵巧手还需要高维手指动作，因此数据更稀缺。人类日常操作视频很丰富，却只有“看见人怎么做”，没有机器人能直接执行的关节命令。本文问：能否先从大规模人手视频学到接触和运动规律，再用少量机器人示范适配具体机型？它值得关注的核心是**数据整理、动作表示、预训练与迁移的完整链条**，而非单一新模型。

## B. 作者实际讨论的相关工作

- Open X-Embodiment（2024）与 DROID（2024）：扩充真实机器人示范，仍依赖具体硬件采集；本文试图用人类视频扩大预训练来源（引言）。
- VITRA（文中引用的 Li 等，2026）：利用人类视频做 VLA 预训练；本文强调显式的手部运动监督，并在相同 LIBERO 适配协议下对比（§2、表 5）。
- UniVLA（Bu 等，2025）与 IGOR（Chen 等，2024）：从画面变化获得隐式动作表示；本文把腕部和手指运动编码成有结构的物理监督（§2）。
- GR00T N1.5（Bjorck 等，2025）：动作预测与迁移基线，表 2–4 中有具体对照。

## C1. 核心贡献

1. **UniHand 数据整理。** 将动作捕捉、VR 记录和带推断标签的 RGB 视频等 11 个来源统一为手部运动数据；完整底库有约 44 万条任务轨迹、1.3 亿帧、1100 多小时。从中平衡抽取 **250 万条指令样本**用于预训练，称 UniHand-2.5M；“250 万”是训练实例数，不是 250 万段独立视频（§4、图 3、附录 D）。
2. **Part-level Motion Tokenization（按手部部位编码动作）。** 把连续的腕部位置与姿态、手指关节运动分别压成离散代码。这样模型像学习文字序列一样学习运动，同时保留不同部位的物理含义（§3.1、图 2）。
3. **Physical Instruction Tuning（物理指令调优）。** 将画面、语言、人的手部运动作为成对训练任务，并在后续阶段把学到的表示接到目标机器人的动作输出。它并未把人手关节角直接当成通用机器人命令（§3）。
4. **视角对齐与数据规模实验。** 对不同相机的成像尺度和视角分布作对齐，并检查数据量、模型大小与下游任务效果（§3.2、§5、附录 F）。

## C2. 采用的方法

**输入。** 收集不同数据源的人手操作视频和可获得或推断的三维手部运动，把关节与腕部姿态统一到 MANO 参数。MANO 是描述人手姿态的参数模型；统一表示让来自不同设备的记录可以合并，但不会消除估计误差（§4）。

**处理。** 先调整不同相机的投影和图像尺度，让同一物理移动不因拍摄设置不同而对应完全不同的像素距离。随后用分组残差量化分别编码腕部与手指：可以理解为先用一个代码描述大致运动，再用后续代码补细节。训练包含“根据画面和指令生成手部运动”“根据前段运动预测后段”“把运动翻译成文字”三种任务（§3.1–3.2、图 2–3）。

**输出与适配。** 预训练模型学到视觉、文字与人手运动之间的关系。接入机器人时加入机器人的本体状态和可学习的动作查询，再用该机器人的示范训练动作头，一次输出连续的 action chunk（动作块，即未来几个控制步）。这一步才把人的运动先验变成目标机器人可执行的控制量；文中还测试了流匹配动作头变体 Being-H(FM)（§3.3、§5.1）。

## D. 实验与结果

- **数据与设置。** InternVL3 1B、8B、14B 主干在 UniHand-2.5M 上训练；手部任务按数据源留出 5% 测试。LIBERO 四组任务各任务 50 条机器人示范；RoboCasa 24 个原子任务各 50 条。真机包括单视角多指抓放、工具箱、杯盖、衣物、倒水与喷雾，以及移动双目视角下的双臂交接和插花；多数任务 50 条示范，玩具抓放 100 条，两个双臂任务分别 222 和 485 条（§5.1、附录 E）。
- **基线与数字。** LIBERO 平均成功率 Being-H 为 **90.3%**、Being-H(FM) 为 **94.5%**；GR00T N1.5 为 86.5%，VITRA 在同一适配设置下为 76.7%（表 3、表 5）。RoboCasa 为 **23.8%**，GR00T N1.5 为 21.0%、未做人手预训练的 InternVL3 为 18.2%（表 4）。这两套基准任务、视角和动作头不同，数字不能直接横比。
- **真机。** Spray–Plant 任务的二元成功率为 **35%**，Being-H(FM) 为 **40%**，GR00T N1.5 为 15%；移动双目双臂交接为 **50%／60%**（原版／FM），π0.5 为 35%（表 7–8）。不同硬件平台和少量试次不足以证明任意真实场景的可靠性。
- **消融。** 表 1–2 显示 1B→8B→14B 提高手部序列格式有效率和运动精度；图 6 显示增加至 250 万训练样本整体改善运动指标，但 PA-MPJPE 在最高数据量略有回落。附录 F 的部位编码消融验证分开表示腕部和手指的价值；图 5 显示少量机器人示范下仍可获得优势，但不是“零机器人数据即可部署”。

## E. 不足与未来研究

**作者明确的限制（§6）。** UniHand 中的伪标注 RGB 视频在深度敏感或接触密集场景可能有噪声；当前只使用视角平衡后的部分数据，而非全部数据；短时间片内视角相对稳定的假设可能不适用于突发的第一人称视角运动。真机任务虽涵盖灵巧与双臂操作，范围仍小于开放世界操作。

**本库分析。** 使用人手数据增加了动作多样性，但视频对接触力、物体滑动和执行反馈不总是可见；成功率提升不能单独归因于数据规模，模型和动作头也变化。对 DH116，可先用 D435i 采集带时间戳的视频，再区分“估计的人手动作”“映射到 DH116 的目标”“真实关节反馈”，逐项核对可达性与接触，不能直接把 MANO 的关节向量下发。NERO 双臂和 AgileX 两指夹爪应分别建立动作接口；两指夹爪无法照搬五指手势。拟议实验可以在固定示范预算下比较人手预训练与无预训练、再比较数量与质量筛选的独立增益。

**相关阅读。** [[Being-H0.5 - Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization|Being-H0.5]] → [[JALA - Joint-Aligned Latent Action Towards Scalable VLA Pretraining in the Wild|JALA]] / [[VIPA-VLA - Spatial-Aware VLA Pretraining through Visual-Physical Alignment from Human Videos|VIPA-VLA]] → [[HuRo - Robotizing Human Videos for Scalable VLA Pretraining|HuRo]]；数据质量对照 [[DataMIL - Selecting Data for Robot Imitation Learning with Datamodels|DataMIL]]、[[Quality over Quantity - Demonstration Curation via Influence Functions for Data-Centric Robot Learning|QoQ]]。

## 核验范围

基于 ICML 2026 正式 PDF 全文的引言、§2–6、表 1–8 和附录 D–F；代码及模型入口来自作者官方仓库。引用量留空，等待人工 Google Scholar 核验。PDF 只保留在本地，不进入公开 Git 仓库。
