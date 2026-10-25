---
paper_id: "P237"
title: "Hand-Object Interaction Pretraining from Videos"
aliases: ["HOP", "从视频进行手物交互预训练"]
authors: ["Singh, Himanshu Gaurav", "Loquercio, Antonio", "Sferrazza, Carmelo", "Wu, Jane", "Qi, Haozhi", "Abbeel, Pieter", "Malik, Jitendra"]
year: 2024
venue: "ICRA 2025"
arxiv: "2409.08273"
version: "v1"
pdf: "01 论文文库/PDFs/08_数据与遥操作/HOP.pdf"
document_type: "research_paper"
preprint_platform: "arXiv"
first_public_date: "2024-09-12"
first_public_month: "2024-09"
first_public_scope: "arXiv v1 UTC submission; cross-platform earliest release not established"
publication_status: "ICRA 2025"
affiliations: ["University of California Berkeley"]
metadata_verified_on: "2026-10-25"
metadata_sources: ["https://arxiv.org/abs/2409.08273", "https://himanshusingh.ai/hop/", "https://arxiv.org/pdf/2409.08273v1"]
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Human_Demonstration", "Retargeting", "Data_Quality"]
doi: "10.1109/ICRA55743.2025.11127811"
---

# Hand-Object Interaction Pretraining from Videos

## 基本信息

- 稳定编号：P237
- 中文译名：从视频进行手物交互预训练
- 作者：Singh, Himanshu Gaurav；Loquercio, Antonio；Sferrazza, Carmelo；Wu, Jane；Qi, Haozhi；Abbeel, Pieter；Malik, Jitendra
- 研究机构：University of California Berkeley
- 年份：2024
- 首次公开：arXiv v1，2024-09-12（UTC；仅限定该平台，不声称全平台最早）
- 出处与版本：ICRA 2025；所读 v1，17 页
- 研究主题：视频重建、运动学重定向、交互先验与下游微调
- 引用量：待核验
- 引用量来源：Google Scholar
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/HOP.pdf|打开本地 PDF]]（已核对文件身份；仅本地保留，不承诺 GitHub 网页可访问）
- [官方论文页](https://arxiv.org/abs/2409.08273)｜[官方 PDF](https://arxiv.org/pdf/2409.08273v1)｜[官方项目](https://himanshusingh.ai/hop/)
- DOI：[ 10.1109/ICRA55743.2025.11127811 ](https://doi.org/10.1109/ICRA55743.2025.11127811)
- 官方代码：[对应 GitHub 仓库](https://github.com/hgaurav2k/hop)
- 数据：[官方数据入口](https://drive.google.com/file/d/12-xghxt0rf_0xDo5SMdrRBnNr7LWJ02Y/view)（下载内容、许可与访问权限以页面说明为准）

## 论文简介

HOP 研究普通人类视频能为灵巧手提供什么动作知识。只用网络图片预训练视觉，模型可能看得懂物体，却不知道手应该怎样接近和调整；直接用强化学习探索高维手关节，又需要许多交互。作者先从视频恢复手和物体，再把人的运动映射到仿真机器人，生成带机器人观察和动作的数据，用来预训练一个时序策略，之后再做具体任务的模仿或强化学习微调

这条流程的重要边界是物体怎么动。预训练中物体每一步被强制放到视频估计的姿态，忽略了真实物体动力学，所以得到的是对交互几何和运动的先验，不能当成已经通过物理验证的接触示范。机器人自身仍在仿真中执行，并通过碰撞和跟踪误差筛选轨迹。下游任务再用真实机器人示范或仿真奖励把这些先验调整成可执行策略

真实实验使用 xArm 与 Allegro，在落物、对准倾倒姿态和抬物上测试。它并非每个任务都优于扩散策略；有些指标表头虽写百分数，内容实际是零到一的比例，本卡按真实取值说明。对我们的意义是把大规模人类视频用于预训练，而非直接当 DH116 控制标签。应把视觉重建误差、重定向误差、接触可行性和下游学习效果分开评估，避免“视频变成机器人动画”就等于已经得到可执行数据

## A. 基本信息与研究问题

研究问题是能否从无机器人动作标签的人类交互视频，得到对下游多指操作有帮助的预训练。视频输入需要恢复三维手与物体，输出先是仿真观察—动作序列，再训练动作预测模型，不直接输出最终真机通用策略

所读为 arXiv v1 共十七页，包含详细附录。官方项目另提供较短论文版本；本卡实验数字明确来自所读版本，不将不同长度文件当成完全相同出版排版。真实平台为七自由度 xArm、十六自由度 Allegro 和 Zed2 相机，不是 D435i 或 DH116

## B. 相关工作

图像预训练 R3M、VIP、MVP 主要学习视觉表征，不直接学习“给定观察应该怎样动作”。DexMV 等方法恢复视频手物轨迹后指导仿真学习，但对每项具体任务的重建、奖励和训练仍有成本

HOP 将多种视频转换为统一机器人交互序列，先训练一个动作预测先验，再通过行为克隆或强化学习微调。它试图共享手物运动经验，而不要求预训练每条视频都与下游任务完全相同

物理约束方法要求机器人通过真实接触使物体跟随目标，通常更难求解。HOP 选择强制物体姿态来提高数据生成可行性，得到更多交互先验，却不能保证抓取力闭合、质量和摩擦一致。理解这个取舍比把它归类为“物理仿真数据”更重要

## C. 核心贡献与方法

流程：交互视频筛选 → 手与物体三维重建 → 机器人运动学重定向 → 仿真执行与筛选 → 因果时序动作预训练 → 任务行为克隆或强化学习微调

HaMeR 估计三维手，MCC-HO 重建手物关系与物体点云。100DOH 中从有手物框的稀疏帧取约十秒片段，再传播检测；加入 DexYCB 的带真值片段。单相机需静止，遮挡和物体位姿噪声会影响后续轨迹

重定向优化把人手关键点 x_h 与机器人正运动学 f(a) 对齐，同时惩罚与上一时刻实际关节 φ 的偏差，可写作 0.5||x_h-f(a)||²+λ||a-φ||²，并受关节上下界限制。第一项匹配几何，第二项减少动作跳变；不是只按人手关节角逐一复制

PD 控制器执行机器人目标，物体却每步设到观察姿态，不受机器人实际施力决定。对每视频运行约七百次优化并筛掉手臂撞桌、撞地和手跟踪误差超过三厘米的轨迹，最终约七万条；不能用视频数乘七百当最终数据量

预训练模型为四层、四头、隐藏 192 的因果 Transformer，历史窗口十六。深度图用卷积编码，另一实验使用物体点云与 PointNet2，两者是分开的输入配置。以 L1 下一步动作损失训练，不把只预测未来图像的模型当作同一种预训练

下游行为克隆使用真实示范；PPO 强化学习微调时限制噪声、对编码器停止 critic 梯度并先冻结 actor 两百步热身。真实推理二十赫兹，机械臂位置控制一百二十赫兹，二者不可混用。新任务仍需动作监督或奖励，不是视频预训练后完全零样本部署

## D. 实验与结果

预训练使用二百个人类视频，其中约六成来自已有标注，其余补充视频，另加二百五十条 DexYCB 片段，共四百五十个视频来源，筛选后约七万轨迹。它们是生成后的序列，不等于七万条独立真实人类演示

真实实验每任务每方法二十次，限时三十秒。Drop 与 Pour 各十五条机器人示范，Lift 四类物体共五十条；采集由两人使用 GELLO 控臂、OPENTEACH 控手。物体与位置在训练测试间相同，再施加关节初始扰动，不能泛称所有结果都是新物体泛化

Table 1，HOP 与 Diffusion Policy 的 Drop 为 0.80/0.90，Pour 为 1.00/0.20，Lift 为 0.65/0.30。尽管表注带百分号，数据取值是比例，即 80%/90% 等，不能读成 0.8%。HOP 没有在 Drop 上胜出

Pour 的成功含义是把容器转到规定倾倒姿态，不是测量真实液体流量；Lift 要抬高约十五厘米。ImageNet 零样本或微调、R3M、VIP、MVP 等基线的输入模态与预训练资源不同，因此结果不构成单一变量下对所有视觉预训练的全面否定

仿真采用二百五十六环境、三个种子，部分任务学习速度约二到五倍，属于样本效率曲线，不是真机成功率同倍增加。新物体鲁棒性图注与正文有“超过两倍/三倍”措辞差异，本卡保留定性结论，不拼接成精确比值

真实行为克隆约九千梯度步、batch 128、AdamW 1e-4，扩散策略六万步；训练步数不同不能直接比较墙钟时间。数据与权重链接在官方仓库 README 中，具体下载权限需按链接确认，不承诺全部无门槛

## E. 不足与未来

作者指出单物体、静止相机和重建误差等限制。物体动力学被忽略，使预训练不能学习准确质量、摩擦或接触力，真实多物体拥挤、遮挡与柔性任务仍有挑战

我的理解是“轨迹能在仿真播放”与“机器人通过接触实现物体运动”必须分别验收。DH116 主动轴与耦合方式不同，重新配置运动学并检查指尖关系后才能讨论迁移；不可把 Allegro 十六维输出直接裁剪成六维

我们的 D435i 可记录 RGB-D 和固定视角，但不能未经比较就替代 Zed2 的几何质量。可以先从普通夹爪验证视频重建与对象轨迹，再用少量 DH116 真实示范锚定接触。后续研究可加入力与接触约束、双臂物体关系、失败检测和恢复微调，并明确分别报告数据生成成功、策略任务成功和失败恢复成功

## 相关工作与阅读入口

- [[03 论文卡片/08_数据与遥操作/DexMV - Imitation Learning for Dexterous Manipulation from Human Videos|P227 · DexMV: Imitation Learning for Dexterous Manipulation from Human Videos]]
- [[03 论文卡片/08_数据与遥操作/DexVIP - Learning Dexterous Grasping with Human Hand Pose Priors from Video|P228 · DexVIP: Learning Dexterous Grasping with Human Hand Pose Priors from Video]]
- [[03 论文卡片/04_灵巧操作/Hand2Robot - Object-Centric 4D Hand Reconstruction from Human Demonstrations for Robotics|P184 · Hand2Robot: Object-Centric 4D Hand Reconstruction from Human Demonstrations for Robotics]]

- 所属方向：[[02 研究方向/数据与遥操作]]
- 专题导读：[[02 研究方向/数据与遥操作_从采集到可执行示范]]
- 遥操作路线：[[02 研究方向/机器人遥操作与动作重定向]]
- 数据质量路线：[[02 研究方向/机器人数据采集与数据质量]]

## 来源与核验边界

- 已阅读上述 17 页版本的正文、方法、实验与局限，含附录时一并核对；关键架构或实验表经页面渲染检查，数字位置见各节
- 日期依据官方 arXiv 提交历史，机构依据所读版本署名；正式出处与所读预印本版本分别标明，不用会议日程或演示获奖冒充正式出版
- 论文结果、作者限制和本库研究设想分开；未报告字段不补猜，未核实引用量不填 0
- 代码和数据链接用于核对公开资源，未运行第三方代码、未执行机器人动作；可访问与可完整复现分别评价
- PDF 再分发许可未统一确认，遵循现有忽略规则仅保存本地；代码许可不自动覆盖论文、数据及模型
