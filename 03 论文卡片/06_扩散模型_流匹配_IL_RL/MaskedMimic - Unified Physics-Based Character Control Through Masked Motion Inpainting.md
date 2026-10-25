---
paper_id: P215
title: "MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting"
year: 2024
authors:
  - Chen Tessler
  - Yunrong Guo
  - Ofir Nabati
  - Gal Chechik
  - Xue Bin Peng
venue: "ACM Transactions on Graphics 43(6), Article 209 (Proc. SIGGRAPH Asia 2024)"
document_type: journal_article
preprint_platform: arXiv
arxiv: "2409.14393"
first_public_date: "2024-09-22"
first_public_month: "2024-09"
first_public_scope: "arXiv v1 submission date in UTC; earlier cross-platform disclosure not exhaustively checked"
latest_preprint_date: "2024-09-22"
latest_preprint_version: v1
preprint_revision_note: "Only v1 listed on arXiv as verified on 2026-10-24"
publication_status: published
published_venue: "ACM Transactions on Graphics 43(6), Article 209"
publication_year: 2024
publication_month: "2024-12"
published_online_date: "2024-11-19"
published_print_date: "2024-12-19"
doi: "10.1145/3687951"
affiliations:
  - "NVIDIA, Israel"
  - "NVIDIA, Canada"
  - "Bar-Ilan University, Israel"
  - "Simon Fraser University, Canada"
affiliation_scope: "arXiv v1 first-page author affiliations; publisher record uses different institution details"
pdf: "01 论文文库/PDFs/06_扩散模型_流匹配_IL_RL/MaskedMimic.pdf"
code: "https://github.com/NVlabs/ProtoMotions"
citation_count: null
citation_source: "Google Scholar"
citation_status: "待人工核验"
verified_on: "2026-10-24"
metadata_verified_on: "2026-10-24"
metadata_sources:
  - "https://arxiv.org/abs/2409.14393"
  - "https://arxiv.org/pdf/2409.14393v1"
  - "https://research.nvidia.com/labs/par/projects/maskedmimic/"
  - "https://api.crossref.org/works/10.1145/3687951"
  - "https://github.com/NVlabs/ProtoMotions"
---

# MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting

## 基本信息

- 年份：2024
- 稳定编号：P215；研究方向：物理角色控制、模仿学习、部分约束动作补全；模型采用条件变分自编码器，不是扩散模型
- 作者与对应机构按 arXiv v1 首页：Chen Tessler、Ofir Nabati 为 NVIDIA, Israel；Yunrong Guo 为 NVIDIA, Canada；Gal Chechik 为 NVIDIA, Israel 与 Bar-Ilan University；Xue Bin Peng 为 NVIDIA, Canada 与 Simon Fraser University
- 正式出版：ACM Transactions on Graphics 43(6)，Article 209，21 页，Proc. SIGGRAPH Asia 2024；DOI：[10.1145/3687951](https://doi.org/10.1145/3687951)
- 时间边界：arXiv 首发 2024-09-22 UTC，核验时仅列 v1；期刊卷期月份为 2024-12，Crossref 单独记录在线日 2024-11-19、印刷日 2024-12-19，不用会议时间代替首发日期
- 机构版本边界：出版数据库的署名机构记录与 arXiv 首页有细节差异，本卡采用明确标注版本的首页署名，不按作者当前任职补猜
- [arXiv](https://arxiv.org/abs/2409.14393) · [官方项目页](https://research.nvidia.com/labs/par/projects/maskedmimic/) · [项目页当前代码入口](https://github.com/NVlabs/ProtoMotions)
- 本地全文：[[01 论文文库/PDFs/06_扩散模型_流匹配_IL_RL/MaskedMimic.pdf|MaskedMimic.pdf]]，arXiv v1，21 页含 Appendix A–B 与 Listing 1
- 引用量：待核验
- 引用量来源：Google Scholar
- 核验日期：2026-10-24

## 论文简介

MaskedMimic 希望用一个物理仿真人体控制器支持不同控制方式，例如跟随完整动作、仅跟随头手传感器、向目标伸手、沿路径行走、根据文字改变风格和坐到椅子上 先前方法往往为每种任务训练高层控制器或设计奖励，本工作把这些需求统一成“已知部分目标，补全其余动作”的问题 输入是当前身体状态、地形及可选的未来关节目标、文字和物体信息，输出是驱动仿真关节的目标旋转；它并非只生成一段不经过物理执行的骨架动画

方法先用强化学习训练完整动作跟踪教师，再通过在线行为克隆把教师蒸馏成部分约束学生 学生使用条件变分自编码器表示同一目标下的多种动作，训练时随机遮住关节、未来帧、文字或物体，推理时由只观察部分信息的先验采样技能 结构化掩码会在时间上连续保持缺失，使模型真正学会处理长期缺少某些约束的情况，而不是从相邻帧拼回完整答案

在 AMASS 稀疏 VR 测试中，Table 2 报告成功率 98.1%、全身平均关节位置误差 58.1 mm，观测到的头手关节误差另为 45.8 mm，三者不能混用 物体交互在 Table 6 达到 96.9% 成功率，移除结构化掩码后为 0%，但这些结果是仿真评测，不是真机坐下或抓取实验 对 DH116 和机械臂加 D435i，更有价值的是用“末端在何时到哪里”等部分约束组织控制接口；深度感知、接触稳定与机器人动力学仍要单独解决 本简介依据全文、六张结果表及附录，复杂文字时序、精确动作复制和动态物体操作仍受限制

## 快速摘要

- 研究问题：同一策略如何根据不同密度、不同模态的目标控制物理角色
- 先前不足：抽象技能潜变量不够直观；新任务常要训练专用高层；纯运动学补全缺少接触和物理约束
- 核心思路：把任务写成部分运动约束，通过结构化随机掩码、完整跟踪教师与条件变分模型训练统一学生
- 输入输出：状态、地形、历史姿态及部分目标进入模型；输出关节 PD 目标旋转；没有直接从 RGB-D 图像到抓取动作的模块
- 数据与评测：AMASS、HumanML3D、SAMP；全身/VR/稀疏关节跟踪、地形泛化、路径/转向/伸手和物体交互，全为仿真
- 主要结果：VR 测试 98.1% / 58.1 mm，物体交互 96.9%；必须分别读成功定义、误差关节集合及评测分母
- 为什么重要：减少为新目标重新训练策略的成本，用显式约束直接组织控制
- 项目关系：可参考关节目标掩码和目标切换机制，不能直接复用其人体权重或将仿真分数当机械臂结果
- 局限：长期语言任务与地形规划弱，动作仍抖动，静态家具交互不等于动态操作
- 摘要证据：全文 Sections 1–10、Tables 1–6、Appendix A–B、Listing 1；关键表格已渲染核对

## A. 基本问题与研究定位

### A1. 把控制任务转为部分约束

同一条完整人体轨迹可以提供全身关节目标，也可以只保留头和双手的位置，或只提供未来某一时刻的一个目标 模型不把未提供信息当零动作，而是根据目标、身体状态和场景补出可行全身运动 Motion Inpainting（运动补全）在这里是通过物理控制动作实现的，不只是补一组关节坐标 [Sections 1、4]

Any-Joint-Any-Time（任意关节、任意未来时刻约束）是接口思想，但训练实际选择了左踝、右踝、骨盆、头、左手和右手六类身体部位，不能把名称扩写成已经验证任意人体细节或灵巧手接触 此外，目标约束可来自人类动作数据，也可来自用户手工规则，不代表模型自行从长篇任务描述生成全部计划 [Section 7]

### A2. 单策略与任务逻辑的边界

论文在各评测中使用统一模型，不针对每个任务微调，但目标的构造和切换仍要人工设计 Goal-Engineering（目标编排）通常借助有限状态机实现，例如先靠近椅子，再切换到物体条件 省去了任务专用策略训练，仍需要任务表示和逻辑，不等于完全自主的通用规划系统 [Sections 7.3、8.2]

## B. 相关工作与证据关系

ASE、CALM 等方法用潜变量组织自然动作技能，再训练高层把这些抽象技能映射到新任务 MaskedMimic 把用户可理解的部分目标作为条件，希望直接控制同一个策略，不再逐任务训练高层 它明确在 Section 2 讨论 ASE，并在 Table 2 使用先前工作报告的 ASE、CALM 与 PULSE 结果；这些对比必须说明来源与任务适配方式

纯运动学文字生成与动作补全能提供动作，却可能出现穿透、悬空等物理问题 本文通过物理仿真闭环执行关节动作，并把地形和家具信息输入策略 与专门的 VR 跟踪不同，它训练不同掩码和模态组合，因此能承受更灵活的条件变化，但这不意味着所有训练外约束都能稳定完成 [Section 2]

本库将 [[03 论文卡片/06_扩散模型_流匹配_IL_RL/ASE - Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters|ASE]]、本篇与 [[03 论文卡片/06_扩散模型_流匹配_IL_RL/BeyondMimic - From Motion Tracking to Versatile Humanoid Control via Guided Diffusion|BeyondMimic]] 并列阅读，分别比较抽象技能控制、部分约束补全与引导生成控制 本篇是本库按研究问题组织的补充阅读；未核实 BeyondMimic 直接引用 MaskedMimic，不据此声称模型直接继承 本篇虽然与生成控制相关，其生成模型是 C-VAE（Conditional Variational Autoencoder，条件变分自编码器），不能因所在分类含扩散模型就改称扩散方法

## C. 方法流程、输入输出与掩码

### C1. 第一阶段：完整跟踪教师

教师 πFC 输入当前身体姿态和速度、未来完整目标帧，以及局部地形高度图 采用 Transformer 处理序列，强化学习奖励组合关节位置、旋转、根部高度、速度和能耗 训练环境包括平地、不规则地形和只在平地布置的物体交互区，对难动作提高采样概率，并以跟踪偏差过大作为提前终止条件 [Sections 5.1–5.5、Figure 4]

SMPL 中性形体角色有 69 个自由度，状态表示为 358 维，动作为 69 维关节目标旋转，由 PD（Proportional-Derivative，比例微分）控制器执行 控制每秒 30 次，物理仿真每秒 120 步；没有添加残差外力或残差控制来帮助角色完成动作 [Section 5.1、Appendix A]

### C2. 第二阶段：教师向学生蒸馏

学生 πPC 在自身访问到的状态上执行动作，教师读取相同状态与完整未来参考，为学生标注正确动作 这种 DAgger（Dataset Aggregation，数据集聚合）式在线蒸馏减轻行为克隆偏离训练状态的问题 教师的访问状态仍有限，因此学生也采用提前终止，避免要求教师在陌生失控状态给出可靠指导 [Sections 3.2、6.3]

C-VAE 包括完整信息编码器、部分信息先验和动作解码器 训练时编码器能看到未掩码参考，输出相对先验均值的残差；动作重建损失教学生模仿教师，KL（Kullback–Leibler，分布差异）项让后验靠近先验 推理时丢弃完整信息编码器，仅由部分信息先验产生 64 维潜变量，再由解码器结合当前状态和地形输出动作 [Equations 6–8、Figure 5、Appendix B]

同一部分约束允许多种合理全身动作，潜变量负责表示这种歧义 每回合固定重参数化噪声，而不是每帧重抽，以减少不连贯；KL 系数从 0.0001 逐渐增加到 0.01 历史姿态从过去 40 步中每隔 8 步取一个，共五个历史观测；文字使用 512 维 XCLIP 编码；局部高度图为 16×16、采样间距 10 cm [Sections 6.3–6.5、Appendix B]

### C3. 结构化掩码的具体规则

附录使用 11 个未来姿态，前十个表示紧邻未来帧，第十一个表示随机远期姿态 近未来掩码以 98% 概率延续原模式，2% 概率重抽可观察关节及位置/旋转条件，以免模型从连续变化的可见关节拼回完整轨迹 [Appendix B.2、Listing 1]

另以 1% 概率插入长度 1–9 帧的全掩码时间段；有文字、物体或远期姿态约束时，时间段乘四，让模型学习只依靠高层条件运动 回合中物体信息有 20% 概率隐藏、文字有 80% 概率隐藏、远期姿态以 20% 概率提供 因此“随机遮挡”不是各维各时刻完全独立采样，这一细节对复现尤其关键 [Appendix B.2]

### C4. 数据与推理接口

AMASS 提供核心关节运动，按 PHC 方法过滤异常片段并做左右镜像；HumanML3D 提供动作文字，镜像时同步改左右词；SAMP 提供物体交互和家具形状 目标物体编码使用包围盒角点、朝向和类别，不能等同真实深度相机已经提供了这些可靠语义量 [Section 7.1、Appendix B]

推理可以填头部路径、手部目标或物体条件，缺失目标通过掩码排除目标 token 地形和当前身体状态始终提供 定量评测取先验均值以提高稳定性；随机采样虽然更丰富，但可能降低原始跟踪分数 因此不能把确定性评测结果直接理解为每次随机生成也有相同表现 [Section 7.2]

## D. 实验数字、分母与消融

### D1. 训练规模与指标定义

Section 7 报告 16,384 个并行环境分布在四张 A100，训练约两周，教师/学生阶段约采集 300 亿/100 亿步 附录也记录四卡、14 天设置，但没有充分拆出每项配置的完整计算成本，不能换算成真机训练时长

MPJPE（Mean Per Joint Position Error，平均每关节位置误差）评估全身关节；MPOJPE（Mean Per Observed Joint Position Error，观测关节平均位置误差）只评估被给定目标的关节，单位均为 mm 跟踪评测使用 AMASS 训练/测试划分；本文未在结果表直接列出对应试验总条数，分母应写“该划分中的运动试验”，不补造整数样本量 Table 5/6 任务评测的 Section 8.2 则明确每项统计来自 5000 个随机回合，不能将此分母搬给跟踪表

### D2. 平地跟踪与 VR

| 表与任务 | 方法 | 测试成功率 | 测试误差 |
| --- | --- | --- | --- |
| Table 1，全身 | FC 教师 | 99.9% | MPJPE 31.3 mm |
| Table 1，全身 | PHC+ | 99.2% | MPJPE 36.1 mm |
| Table 1，全身 | MaskedMimic | 99.2% | MPJPE 35.1 mm |
| Table 1，全身 | PULSE | 97.1% | MPJPE 54.1 mm |
| Table 2，VR | MaskedMimic | 98.1% | MPJPE 58.1 mm |
| Table 2，VR | PULSE | 93.4% | MPJPE 88.6 mm |
| Table 2，VR | ASE | 37.6% | MPJPE 120.5 mm |
| Table 2，VR | CALM | 10.1% | MPJPE 122.4 mm |

全身跟踪失败指某一帧的平均关节偏差超过 0.5 m；VR 仅给头部位置与旋转、双手位置，成功评价针对观测到的头手约束，而表中另给全身 MPJPE MaskedMimic 的 VR 观测关节误差为测试 45.8 mm，不能将全身 58.1 mm 写成传感器跟踪误差 [Sections 7.2、8.1]

论文正文声称 FC 相对 PHC+ 降低 62.5% 失败率，但 Table 1 的已显示数值为 99.9% 与 99.2%，直接计算不对应这一比例 本卡保留可核对表值，不依据舍入后表值重复该降幅，也不自行修正作者未公开的原始数 [Table 1、Section 8.1]

### D3. 稀疏性、地形与任务

Table 3 测试时只给骨盆约束可达 98.4%、MPOJPE 33.4 mm；只给脚为 91.8%、94.3 mm，说明不同部位约束难度不同 Table 3 全身成功率写 99.1%，与 Table 1 的 99.2% 略有不一致，本卡按各自表格保留，不能拼成无差异的一个精确结果

不规则地形的 Table 4 中，学生全身跟踪测试为 95.4%、MPJPE 62.9 mm；VR 为 93.6%、MPOJPE 69.4 mm 它不是“地形变化完全不降性能”，而是在新地形上仍能维持较高成功率，跟踪精度有所下降

Table 5 平地/地形的路径跟随为 96.3%/96.3%，位置误差 11.2/12.5 cm；转向为 97.8%/93.8%，速度误差均为 8.4 cm/s；伸手为 88.7%/87.3%，保持阶段距离误差 20.3/21.7 cm 三种误差的单位和测量阶段不同，不能取平均当统一控制精度 路径超过目标 2 m 记失败；转向偏差超过 45° 记失败；伸手在目标时刻偏差超过 0.5 m 记失败 [Sections 8.2、Table 5]

### D4. 物体交互与消融

物体交互从距未见家具 2–10 m 处开始，远处先用移动与文字条件靠近，进入 2 m 后改用物体条件 骨盆进入有效座位 20 cm 内视为坐下成功；误差是回合中到有效座位的最小距离平均值，不是稳态坐姿误差或物理接触成功率 [Sections 7.3、8.3]

| Table 6 变体 | 成功率 | 误差 cm |
| --- | --- | --- |
| 完整 MaskedMimic | 96.9% | 10.5 |
| 无历史 | 94.9% | 12.7 |
| 无 VAE | 93.2% | 12.2 |
| 无残差先验 | 21.1% | 57.4 |
| 无结构化掩码 | 0% | 274.4 |

该表支持残差先验与时间结构化掩码对这一组合任务至关重要，而非证明所有任务都下降同样幅度 无历史和无 VAE 也影响结果，但这里幅度较小 Figure 8e 展示在不规则地面上的未见沙发交互，是组合泛化例子；没有提供单独的大规模跨地形家具成功率表，不能把 96.9% 专门归于该画面

## E. 局限、迁移与未来问题

### E1. 作者承认的限制

Section 9 指出动作仍有抖动，后空翻与霹雳舞等难动作无法完整复现；不规则地形上常沿用平地步态，没有充分规划落脚点；大规模角色和复杂场景中的目标编排仍可能费时；动态场景、移动物体、工具使用和多角色交互留作未来工作 Section 8.4 还指出带多步计数和先后关系的文字容易失败，作者推测有限历史限制了长期推理，因此不能把文字演示提升为长任务规划证据

### E2. 本库对 DH116 与机械臂加 D435i 的判断

可以借鉴的是明确区分“已知约束”和“自由生成维度”，例如只约束末端到达目标时刻，让冗余关节自行寻找自然运动；也可以训练末端目标缺失、时间间隔缺失和部分观测缺失，以检验策略对控制模式切换的承受能力

不能直接迁移的是 SMPL 人体、69 维关节动作、全状态与精确高度图假设 机械臂抓取需要物体六维位姿、夹持器开合与接触反馈，家具坐下的骨盆距离指标不能替代抓取成功、滑移或插接力指标 DH116 的关节、负载、碰撞模型与控制接口也需单独匹配；论文没有对应真机数据

D435i 可以为几何目标提供深度观测，但这需要相机标定、分割、位姿估计和遮挡处理，本文输入的包围盒/高度图没有验证上述视觉误差 本库的研究设想是先让少量可信末端约束驱动仿真策略，再比较完整轨迹条件与随机掩码条件在遮挡下的任务结果；不将该设想表述为作者已完成机器人迁移

### E3. 开源范围与版本边界

官方项目页的 Code 当前指向 NVlabs/ProtoMotions，当前主页为 ProtoMotions3，源码 LICENSE.md 为 Apache-2.0；当前 README 另将 NVIDIA 提供模型列为 NVIDIA Open Model License，并说明第三方资产单独归属 这些是核验日仓库状态，不能反推所有历史 MaskedMimic 代码和数据都采用同一许可

项目页与公开框架支持进一步复现，但本次没有运行训练、核实历史版本与论文每张表的完全一致性，也没有核验完整原始 AMASS/HumanML3D/SAMP 数据已随仓库直接再分发 数据和 SMPL 等资产仍须检查其独立许可 当前框架新增的机器人部署能力不属于本篇 2024 仿真人体论文的实验贡献

## 来源与阅读证据

- [arXiv 版本页](https://arxiv.org/abs/2409.14393)：首发日期、仅 v1、正式题名和作者
- [arXiv v1 全文](https://arxiv.org/pdf/2409.14393v1)：已读 Sections 1–10、Tables 1–6、Appendix A–B、Listing 1；关键表格已渲染核对
- [官方项目页](https://research.nvidia.com/labs/par/projects/maskedmimic/)：TOG/SIGGRAPH Asia 出处、任务演示和当前代码入口
- [Crossref 正式出版记录](https://api.crossref.org/works/10.1145/3687951)：DOI、43(6)、页数与 online/print 日期
- [当前官方框架](https://github.com/NVlabs/ProtoMotions) · [当前源码许可](https://github.com/NVlabs/ProtoMotions/blob/main/LICENSE.md)：公开实现入口及核验日许可边界；不冒充论文原始提交版

## 研究关联入口

[[01 论文文库/专题阅读/全身运动技能与具身执行框架|全身运动技能与具身执行框架]] · [[01 论文文库/论文编号索引|稳定编号索引]]
