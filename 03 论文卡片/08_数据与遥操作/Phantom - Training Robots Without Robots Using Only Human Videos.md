---
paper_id: P246
title: "Phantom: Training Robots Without Robots Using Only Human Videos"
short_name: "Phantom"
authors: ["Marion Lepert", "Jiaying Fang", "Jeannette Bohg"]
year: 2025
venue: "CoRL 2025; PMLR 305:4545–4565"
arxiv: "2503.00779"
pdf: "01 论文文库/PDFs/08_数据与遥操作/Phantom.pdf"
tags: ["Human_Video", "Robotization", "Data_Generation", "Imitation_Learning"]
---

# Phantom: Training Robots Without Robots Using Only Human Videos

## A. 基本信息与研究问题

- 作者：Marion Lepert、Jiaying Fang、Jeannette Bohg。2025 年 3 月首次公开；正式出处：[CoRL 2025，PMLR 305:4545–4565](https://proceedings.mlr.press/v305/lepert25a.html)，会议于 2025 年 9 月举行。[arXiv 2503.00779](https://arxiv.org/abs/2503.00779)，[arXiv DOI](https://doi.org/10.48550/arXiv.2503.00779)；正式 DOI 未核实。
- [正式 PDF](https://raw.githubusercontent.com/mlresearch/v305/main/assets/lepert25a/lepert25a.pdf) · [项目视频](https://phantom-human-videos.github.io/) · [作者数据处理代码](https://github.com/MarionLepert/phantom) · [[01 论文文库/PDFs/08_数据与遥操作/Phantom.pdf|本地 PDF]]。代码仓库说明其公开人类视频处理流程；不据此宣称完整策略、权重或全部训练数据已开放。
- 引用量：
- 引用量来源：

**问题。** 人类操作视频没有机器人动作标签，且画面中的人手与部署时的机械臂外观不同。Phantom 试图只从人类视频生成“看起来像机器人观察、配有机器人动作”的训练记录，并在同一类型机器人上直接测试，不用该任务的机器人训练示范。这里的“without robots”指**训练数据采集不需要机器人示范**，真机评价仍然需要机器人。

## B. 作者实际讨论的相关工作

- Rovi-Aug、SHADOW：在机器人与机器人之间通过图像编辑减小外观差异，Phantom 将编辑迁移到人手→机器人，难度还包括动作估计（§2）。
- EgoMimic、AR2-D2：有类似视觉编辑，但依赖机器人数据联合训练；作者将其编辑样式或需求作为对照（§2、§4）。
- Diffusion Policy：本文用作训练策略的现有学习器，而非 Phantom 自己提出的动作生成网络（§4）。

## C1. 核心贡献

1. **RGB-D 人类视频→机器人观察和动作对。** 从深度辅助的人手姿态估计得到末端位置、方向、夹爪开合，再用图像修补和虚拟机器人覆盖替换人手（§3、图 1–3）。
2. **零机器人示范的闭环部署。** 将编辑后的数据训练模仿学习策略，在 Franka、Kinova 相关任务上实际闭环运行；“zero-shot”限定为未使用该任务的机器人示范微调（§4）。
3. **视觉编辑消融。** 比较完整修补、手部掩码、红线和未编辑图像，分离“有机器人外观”与“修补质量”对迁移的作用（表 1–3）。

## C2. 采用的方法

采集第三人称 RGB-D 视频，示范者用拇指和食指做捏取。HaMeR 从 RGB 估手部 21 点和网格；SAM2 分出人手，深度图给部分点云；ICP 对齐估计网格与点云，改善绝对三维位置。拇指与食指的指尖中点作为目标夹爪位置，两指形成的平面确定方向，指尖间距给出开合宽度。再用相机外参变换到机器人坐标系（§3.1–3.2）。

图像侧把人手擦去并补背景，按上述姿态渲染目标机器人，利用深度处理遮挡；部署时也用渲染覆盖真实机器人外观，使训练和测试画面更一致。最后训练 Diffusion Policy 并闭环测试。此处输出的是面向**两指夹爪的末端位姿＋夹爪宽度**，不是完整人手五指关节轨迹，不能直接套到 DH116（§3.3–4）。

## D. 实验与结果

- 五种同场景任务每项采集 250–350 条人类视频，每项测试 25 次。完整编辑的抓书放盒、叠杯、系绳、转盒成功率分别为 **92%、72%、64%、72%**；扫垃圾任务按扫入数量分级，不应只报单一成功率。红线/未编辑对照在表 1 中这些任务为 0（§4.2、表 1）。
- 跨新场景扫垃圾使用 950 条人类示范，在室外草地和室内休息区测试。新地面材质下表现下降，作者指出采集仅有四类表面（§4.3、表 2）。
- 图像修补消融：室内新场景扫垃圾，视频修补 **84%**，简单 OpenCV 修补 **76%**，只遮罩不修补 **60%**，各 25 次测试（表 3）。这些结果支持视觉域对齐，但并未证明真实几何轨迹总正确。

## E. 不足与未来研究

**作者明确限制（§6）。** 人手姿态估计在遮挡时会失败；训练相机与部署相机需要相近视角且部署外参已知；方法基于 RGB-D 和捏取动作。视觉修补/渲染也可能留下域差。

**本库分析。** 这条路线较适合 AgileX 两指夹爪：可先核对 D435i 深度与外参，再从人手拇指/食指估夹爪目标。对于 DH116 灵巧手，它丢失其他手指接触；应另建多指映射并检查关节限位。NERO 双臂若要复现，还需两手相互遮挡、协作和同步控制，不能把单臂实验直接外推。可先把转换动作在仿真中逐条执行，记录碰撞和失败，再与真实示范训练比较。

**相关阅读。** [[HuRo - Robotizing Human Videos for Scalable VLA Pretraining|HuRo]]（扩展到异构来源和双侧机器人化） · [[CUPID - Curating Data your Robot Loves with Influence Functions|CUPID]]（生成后按实测价值筛选）。

## 核验范围

阅读 PMLR 正式 PDF 的引言、§2–6、表 1–3 和附录数据描述；代码范围核对作者 GitHub。引用量未自动获取。
