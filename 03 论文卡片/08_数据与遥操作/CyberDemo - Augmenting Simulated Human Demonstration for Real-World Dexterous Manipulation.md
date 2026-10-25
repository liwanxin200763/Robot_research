---
paper_id: "P231"
title: "CyberDemo: Augmenting Simulated Human Demonstration for Real-World Dexterous Manipulation"
aliases: ["CyberDemo", "用仿真示范扩增学习真实灵巧操作"]
authors: ["Wang, Jun", "Qin, Yuzhe", "Kuang, Kaiming", "Korkmaz, Yigit", "Gurumoorthy, Akhilan", "Su, Hao", "Wang, Xiaolong"]
year: 2024
venue: "CVPR 2024"
arxiv: "2402.14795"
version: "v2"
pdf: "01 论文文库/PDFs/08_数据与遥操作/CyberDemo.pdf"
document_type: "research_paper"
preprint_platform: "arXiv"
first_public_date: "2024-02-22"
first_public_month: "2024-02"
first_public_scope: "arXiv v1 UTC submission; cross-platform earliest release not established"
publication_status: "CVPR 2024"
affiliations: ["University of California San Diego", "University of Southern California"]
metadata_verified_on: "2026-10-25"
metadata_sources: ["https://arxiv.org/abs/2402.14795", "https://cyber-demo.github.io/", "https://arxiv.org/pdf/2402.14795v2"]
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Human_Demonstration", "Retargeting", "Synthetic_Data"]
---

# CyberDemo: Augmenting Simulated Human Demonstration for Real-World Dexterous Manipulation

## 基本信息

- 稳定编号：P231
- 中文译名：用仿真示范扩增学习真实灵巧操作
- 作者：Wang, Jun；Qin, Yuzhe；Kuang, Kaiming；Korkmaz, Yigit；Gurumoorthy, Akhilan；Su, Hao；Wang, Xiaolong
- 研究机构：University of California San Diego；University of Southern California
- 年份：2024
- 首次公开：arXiv v1，2024-02-22（UTC；仅限定该平台，不声称全平台最早）
- 出处与版本：CVPR 2024；所读 v2，17 页
- 研究主题：灵敏度感知轨迹扩增、自动课程、Sim2Real
- 引用量：待核验
- 引用量来源：Google Scholar
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/CyberDemo.pdf|打开本地 PDF]]（已核对文件身份；仅本地保留，不承诺 GitHub 网页可访问）
- [官方论文页](https://arxiv.org/abs/2402.14795)｜[官方 PDF](https://arxiv.org/pdf/2402.14795v2)｜[官方项目](https://cyber-demo.github.io/)
- 官方代码：[对应 GitHub 仓库](https://github.com/wang59695487/hand_teleop_real_sim_mix_adr)
- 数据：未核实独立完整数据集入口；代码中的示例和项目展示不等于完整数据发布

## 论文简介

CyberDemo 研究如何把少量仿真遥操作示范扩展成能帮助真实灵巧手学习的数据。灵巧手有许多关节、接触复杂，反复在真机上收集高质量演示很贵；仿真可以改变物体、相机和光照，但随意给动作加噪声往往会破坏抓取。论文的关键是根据一段动作对扰动有多敏感，决定把需要的位移变化安排在哪些时段，并逐步增加训练难度

系统先在 SAPIEN 场景里通过视觉遥操作采集种子轨迹，再对场景外观、物体几何和初始位置进行扩增。物体位置改变时，接触关键阶段不能和自由移动阶段承受同样的噪声，因此生成器估计轨迹片段的鲁棒性，把更多变化分配给不敏感片段。生成的新数据用来训练动作块策略，并根据策略当前表现调整扩增课程。最后还要用少量真实数据微调，不是完全不接触真机就能解决所有任务

实验包括取放、阀门旋转和倒方块，使用 xArm 与 Allegro 灵巧手。主要结果的每个任务每个条件只有二十次真机试验，所以表中相差一次就是五个百分点，不宜过度解读小差异。论文还存在正文与表注对条件编号不一致的地方，本卡采用明确的表头定义。对我们的价值主要是扩增时保护关键接触，以及用闭环策略表现评价数据，而不是把仿真数量当作质量证明；迁移到 DH116 仍需重新设计手模型、重定向和控制接口

## A. 基本信息与研究问题

研究目标是在尽量减少真实遥操作时间的条件下，得到对位置与视觉变化较稳健的灵巧操作策略。输入是少量仿真种子轨迹及可编辑场景，输出为扩增数据与预训练策略，随后用真实数据适配

动作包含机械臂末端的六维增量与十六个手关节目标，不能直接等同于 DH116 六个主动轴。真实部署的动作含义、控制频率和关节限制必须与训练定义对应。论文的实际价值在于如何生成有效数据并安排学习过程，而不是提出一种无需硬件适配的万能遥操作器

## B. 相关工作

纯真实示范准确反映接触，却采集慢、难覆盖光照和新物体。纯仿真强化学习需要奖励设计和大量交互，接触误差可能阻碍迁移。传统域随机化改变相机、纹理和动力学参数，提升训练变化，但不自动解决示范动作随物体位置变化的问题

MimicGen 一类工作以物体中心重组动作；CyberDemo 强调不同时间片段对扰动的敏感性。若抓取闭合时突然偏移，即使手腕轨迹平滑也会失败；自由移动时同样偏移可能没有影响。因此扩增不应只统一设置噪声标准差

R3M、PVR、MVP 等视觉预训练模型主要提供感知表征。CyberDemo 的仿真预训练同时提供动作监督与环境变化，两类方法的训练资源和信息不同，表格胜出不能简单推导“视觉预训练无用”。ACT 用 Transformer 预测连续动作块，负责学习生成数据，而不是数据扩增算法本身

## C. 核心贡献与方法

流程：搭建任务仿真 → 人手视觉遥操作采集 → 外观与几何扩增 → 估计动作片段灵敏度 → 生成位置变化轨迹 → 自动课程训练 → 少量真机微调

仿真不是完全自动从任意视频重建，任务场景需要人工配置。人手视觉输入经运动学映射控制虚拟机械臂与 Allegro，记录 RGB、机器人本体状态及动作，实验数据记录三十赫兹。外观变化可在同一状态重新渲染，而物体几何变化需要检查原轨迹能否仍执行成功，必要时扰动动作寻找可行示范

灵敏度感知扩增把源轨迹切段，通过逐步施加噪声观察哪些部分容易失败，建立局部鲁棒性估计。然后把物体位移需要的动作变化更多放到鲁棒片段，尽量少改精密接触片段。这里不是简单给每个手指关节随机抖动，也不是训练一个能理解所有失败语义的网络

自动课程根据当前策略任务成功情况提高随机化难度，遇到不足时使用限制与回退。生成器能产生某个难例，不代表策略已经学会，所以反馈信号是策略执行，而不只是生成数据的成功数

策略使用动作分块训练，并对小运动等情况处理动作聚合。预训练后用每任务约三分钟真实示范微调，机器人执行仍依赖低层控制和场景观测。对象发生不可逆滑落或手型不适配时，本文没有一个独立安全恢复器来保证重新完成任务

## D. 实验与结果

Table 1 的每任务每条件真机评估为二十次，条件依表注为分布内、新位置、随机光照、两者同时变化。瓶子取放依次成功 7/20、6/20、8/20、5/20；罐子为 14/20、11/20、13/20、13/20；倒块为 9/20、4/20、10/20、7/20；阀门旋转为 15/20、10/20、17/20、13/20

阀门成功要求旋转 720 度，倒块要求四个方块全部倒出，不能把碰到物体就算成功。正文 §5.1 对第二、三条件编号与表注有交换，本卡按表头解释，不改写论文原数据

Table 2 扩增从 100 到 810 条的比较同时涉及难度变化，不能仅凭性能变化分离出纯数据量效应。Table 3 比较自动课程，在真机复合变化条件下，策略驱动课程为 35%，数据生成驱动为 20%，无课程为 5%；真机每条件二十次，仿真二百次

Table 4 的总五十条源数据混合实验也有条件差异：十五条仿真加三十五条真实，分布内表现 50%、新位置 15%；三十五条仿真加十五条真实，分别 25%、35%。因此不能提出一个在所有测试条件下最优的固定混合比例

平台为 xArm6 加 Allegro，论文包含仿真与真机结果，但没有统一给出采集人数、所有任务总人时、所有生成过滤率或整套部署硬件价格。真实微调数据、手模型和人工场景配置都是复现成本的一部分

## E. 不足与未来

作者方法仍受仿真—现实接触差异与任务模型限制。几何、纹理和位置增强不能完全覆盖摩擦变化、柔性材料和多指接触顺序改变。本文不是纯视频直接生成真机可执行动作，也没有证明完全零真机数据迁移

我的理解是最有价值的可迁移原则是“让自由空间吸收变化，保护接触片段”，但应以实际扰动实验判断片段，而非只手工指定。碰撞与接触成功过滤也是训练数据质量控制，不等同于部署阶段失败恢复

我们的普通夹爪可先做取放位置扩增，D435i 提供同步 RGB-D 检查遮挡与位姿变化。DH116 则要建立主动关节—指尖映射、耦合约束和接触模型，再测试同样思想是否成立，不能复制 Allegro 十六维动作。后续可记录失败轨迹与触觉信息，比较不同接触阶段允许的变化范围，并保留人工接管与终止机制

## 相关工作与阅读入口

- [[03 论文卡片/08_数据与遥操作/DemoGen - Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning|P230 · DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning]]
- [[03 论文卡片/08_数据与遥操作/DexTransfer - Real World Multi-fingered Dexterous Grasping with Minimal Human Demonstrations|P229 · DexTransfer: Real World Multi-fingered Dexterous Grasping with Minimal Human Demonstrations]]
- [[03 论文卡片/08_数据与遥操作/DexMimicGen - Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning|P145 · DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning]]

- 所属方向与专题导读：[[02 研究方向/数据与遥操作]]
- 遥操作路线：[[02 研究方向/机器人遥操作与动作重定向]]
- 数据质量路线：[[02 研究方向/机器人数据采集与数据质量]]

## 来源与核验边界

- 已阅读上述 17 页版本的正文、方法、实验与局限，含附录时一并核对；关键架构或实验表经页面渲染检查，数字位置见各节
- 日期依据官方 arXiv 提交历史，机构依据所读版本署名；正式出处与所读预印本版本分别标明，不用会议日程或演示获奖冒充正式出版
- 论文结果、作者限制和本库研究设想分开；未报告字段不补猜，未核实引用量不填 0
- 代码和数据链接用于核对公开资源，未运行第三方代码、未执行机器人动作；可访问与可完整复现分别评价
- PDF 再分发许可未统一确认，遵循现有忽略规则仅保存本地；代码许可不自动覆盖论文、数据及模型
