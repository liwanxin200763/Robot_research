---
paper_id: P217
title: 'Diffuse-CLoC: Guided Diffusion for Physics-based Character Look-ahead Control'
authors:
- Xiaoyu Huang
- Takara Truong
- Yunbo Zhang
- Fangzhou Yu
- Jean Pierre Sleiman
- Jessica Hodgins
- Koushil Sreenath
- Farbod Farshidian
year: 2025
venue: ACM Transactions on Graphics 44(4), SIGGRAPH 2025
arxiv: '2503.11801'
arxiv_version: v3
pdf: 01 论文文库/PDFs/06_扩散模型_流匹配_IL_RL/Diffuse-CLoC.pdf
verified_on: '2026-10-24'
citation_status: 待 Google Scholar 人工核验
citation_source: Google Scholar
tags:
- Diffusion
- Humanoid_Control
- Physics_Based_Animation
- Guided_Control
document_type: 期刊论文
preprint_platform: arXiv
first_public_date: '2025-03-14'
first_public_month: 2025-03
first_public_scope: arXiv v1 submission history (UTC)
latest_preprint_date: '2025-08-05'
latest_preprint_version: v3
publication_status: 已正式发表
published_venue: ACM Transactions on Graphics 44(4)
publication_year: 2025
publication_month: 2025-07
published_online_date: '2025-07-27'
print_issue_month: 2025-08
conference_month: 2025-08
doi: 10.1145/3731206
affiliations:
- University of California, Berkeley
- Stanford University
- RAI Institute
metadata_verified_on: '2026-10-24'
metadata_sources:
- https://arxiv.org/abs/2503.11801
- https://arxiv.org/pdf/2503.11801v3
- https://doi.org/10.1145/3731206
- https://api.crossref.org/works/10.1145/3731206
- https://rai-inst.com/resources/papers/diffuse-cloc-guided-diffusion-for-physics-based-character-look-ahead-control/
- https://s2025.conference-schedule.org/presentation/?id=papers_1047&sess=sess156
---

# Diffuse-CLoC: Guided Diffusion for Physics-based Character Look-ahead Control

## 出处与版本

- 年份：2025
- 稳定编号：P217；作者：Xiaoyu Huang、Takara Truong、Yunbo Zhang、Fangzhou Yu、Jean Pierre Sleiman、Jessica Hodgins、Koushil Sreenath、Farbod Farshidian；前两位为共同第一作者，Takara Truong 为通讯作者，依 v3 首页
- 对应版本机构：Xiaoyu Huang、Koushil Sreenath 为 University of California, Berkeley 与 RAI Institute；Takara Truong 为 Stanford University 与 RAI Institute；其余五位为 RAI Institute。不能因 Jessica Hodgins 的其他任职把本篇机构补成 CMU
- 预印本：[arXiv 2503.11801](https://arxiv.org/abs/2503.11801)；首发 2025-03-14 UTC，首发月份 2025-03；只限定 arXiv v1 提交历史，不排除其他平台更早公开
- 最近修订：v3，2025-08-05；v2 为 2025-07-01；本卡读 12 页 v3，含附录 A 的 Table 3，并视觉核对方法图与两张核心实验表
- 正式出版：[ACM Transactions on Graphics 44(4)](https://doi.org/10.1145/3731206)，DOI 10.1145/3731206；[出版者提交的 Crossref 元数据](https://api.crossref.org/works/10.1145/3731206)给出线上出版 2025-07-27，印刷卷期 2025-08；本地 PDF 页脚也写 August 2025，不与 arXiv 修订日期混用
- [SIGGRAPH 2025 官方报告日程](https://s2025.conference-schedule.org/presentation/?id=papers_1047&sess=sess156)：2025-08-13；此为报告日期，不是首次公开或线上出版日期
- [RAI 官方论文条目](https://rai-inst.com/resources/papers/diffuse-cloc-guided-diffusion-for-physics-based-character-look-ahead-control/)｜[固定 v3 PDF](https://arxiv.org/pdf/2503.11801v3)；官方条目指向的[项目页](https://diffusecloc.github.io/website/)本轮返回 404，保留入口并注明状态，不据此断言论文撤回
- 本地 PDF：[[01 论文文库/PDFs/06_扩散模型_流匹配_IL_RL/Diffuse-CLoC.pdf|阅读 Diffuse-CLoC 全文]]；官方合法全文留本地，沿库中 PDF 忽略规则管理
- 引用量：待核验
- 引用量来源：Google Scholar
- 核验日期：2026-10-24

## 论文简介

让一个模拟人形角色避开障碍并跳过箱子，既要知道未来身体往哪里走，也要产生符合动力学的关节动作。只生成身体姿态的扩散模型容易出现漂浮、穿透等现象，再接一个跟踪器也未必能执行；只生成动作的策略虽然可驱动角色，却难以直接按空间目标引导。Diffuse-CLoC 将未来状态和动作放进同一个扩散模型，使避障、到达目标和关键帧要求能在状态空间表达，并共同影响动作生成

训练数据来自 AMASS 的五十四条行走、跑步、爬行和跳跃动作。作者用 PHC+ 跟踪器在仿真中采集状态—动作轨迹，并加入扰动收集纠偏行为。推理时读取短段历史，预测约一秒的未来状态与更短的动作序列，通过可微代价引导去噪或补全已知关键帧，再只执行当前动作。滚动缓冲区保留前次计划，减少频繁重新采样造成的摇摆，因此一个模型能处理训练时未专门训练的下游任务

Table 1 的模拟森林穿越成功率为 96%，越障为 71%，行走受扰跌倒率为 16%；这些是模拟角色的任务统计，不是真实机器人的成功率。论文未明确列出这些百分比对应的完整试次数分母，不能把训练动作数五十四当分母。结果也不是每项都胜过基线，较慢重规划的分层基线在运动分布距离上更低

本文的重要性在于把规划目标与可执行动作连接到同一个生成过程，并让新目标可在推理时加入。它也是理解 BeyondMimic 状态引导路线的重要相关论文，但没有验证硬件迁移或灵巧手抓取。对机械臂、DH116 与 D435i，可研究将未来物体和指尖状态与动作共同建模；接触表示、感知不确定性、数据覆盖和控制时延都要重新设计，不能把模拟角色的成功直接当作当前设备的能力

## A. 基本问题与快速摘要

本文研究 physics-based character control（由物理仿真驱动的角色控制），不是仅在屏幕上播放人体骨架，也不是已部署在人形硬件上的机器人控制器。状态为 165 维，动作是 23 个球关节对应的 69 维 PD 目标；这种 SMPL 模拟身体的关节拓扑、执行器假设与真实 G1 或 DH116 均不同（§5.1）

关键矛盾是任务通常用未来状态描述，例如“身体不要碰柱子”“未来一秒到达某处”，而关节动作空间不方便直接计算这些目标。若规划器生成姿态，再让低层跟踪器执行，会受到 planner–controller mismatch（规划器与控制器不匹配）影响；若只学状态到动作，又没有可以直接引导的未来身体轨迹。联合建模 p(s,a) 让状态上的约束可以通过去噪模型传到动作上，是论文的主要设计选择（Fig. 2、§1–3）

输入为过去四步左右状态—动作历史、当前状态与推理时给定的任务代价或关键帧；输出包含未来身体状态及关节动作，真正交给模拟器的是当前一步动作。未来状态预测不是传感器真值，也不是经形式验证的动力学模型。模型不读取 RGB、深度图或自然语言；障碍和目标已转成可计算的几何或任务空间量

## B. 相关工作、贡献定位与 BeyondMimic 关系

MDM、Guided-MDM 等运动学扩散能按文字、路径或关键帧生成姿态，但不直接产生可执行控制。Diffusion Policy、PDP、DiffuseLoco 等动作生成路线能学习控制分布，却不自然支持在未来状态上施加新约束。Diffuser 已联合生成状态与动作，因此本文不是“首次把状态动作放进扩散模型”，贡献在复杂角色任务上的架构、注意力、滚动推理与实验验证（§2、Fig. 2）

Kin+PHC 是作者构造的代表性分层对照：训练类似 Guided-MDM 的运动学模型，并用 PHC+ 跟踪预测动作，改变重规划间隔来比较响应与平滑度。不能把这一对照称为直接跑了所有既有分层论文的官方完整实现，也不能把 PHC+ 训练所用的数据采集角色误认为部署时仍保留的低层跟踪器

与 [[03 论文卡片/06_扩散模型_流匹配_IL_RL/BeyondMimic - From Motion Tracking to Versatile Humanoid Control via Guided Diffusion|BeyondMimic]] 的关系有直接引文证据：BeyondMimic v4 参考文献 #45 收录本篇，第 4 页讨论规划—控制不匹配时引用 #44/#45，第 49 页在 emphasis projection（突出根部轨迹特征的投影表示）处引用 #45/#84，并在数据扰动讨论中比较 #45/#85 的逐步独立高斯噪声，改用时间相关的 OU 噪声

这些具体引用足以支持方法联系，但不表示 BeyondMimic 原样复用本篇网络和训练代码。BeyondMimic 加入自己的跟踪、潜空间策略与真机验证，本篇扩散的是原始角色关节动作；二者需要区分状态—动作联合生成这一思想、具体 latent action（潜动作）接口及硬件部署证据。与 [[03 论文卡片/05_仿真到真实_Sim2Real/ASAP - Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills|ASAP]] 的联系属于本库的对照阅读：前者校正迁移动力学，本篇解决推理目标的可引导性，未核实两者构成直接继承链

## C. 方法：输入 → 步骤 → 输出

### C1. 模拟轨迹与表示

先选 AMASS 54 条动作，用 PHC+ 跟踪器平均每动作采 40 条 rollout（执行轨迹），论文括注数据约 3.5 小时。采集时注入动作噪声，记录被扰动状态及对应纠偏动作，让模型不只看完美轨迹。训练动作库不是五十四个全新下游任务，动作数也不等于成功率试验分母（§5.1）

165 维状态含根部位置、线速度、旋转，以及 23 关节的局部三维位置与速度、手和踝的旋转。根部量在当前角色坐标系中表示，局部关节量在各时刻角色坐标系中表示，降低全局平移与朝向变化的影响。69 维动作表示关节 PD 目标位置，不能写为 69 个独立电机或直接力矩。噪声虽影响执行力矩与轨迹，但策略输出接口仍是关节目标位置

### C2. 联合扩散和注意力

去噪序列交错包含状态 token（一个时间步的特征单元）和动作 token，每类 token 单独编码并带噪声等级。decoder-only Transformer（仅解码器结构的注意力网络）预测清洁轨迹，以均方误差训练；状态与动作各时刻的噪声等级独立采样。模型不是先预测全部动作再外接一个精确动力学求解器，而是从离线数据学习联合序列分布（§3.1、Fig. 3）

注意力不是简单“全连接更强”：状态可读取过去和未来状态，但不读取动作 token；动作只读取当前/过去的状态与历史动作，避免直接依赖噪声较大的远期状态。未来任务信息通过状态间传播，再间接改变当前动作。这里的 causal（因果）指注意力访问时间顺序的限制，不是关于真实系统因果机制的识别证明

状态预测时域为 32 步、约一秒，动作损失只保留前 16 步，减轻长时动作不确定性。emphasis projection 强调全局根部状态，同时拼接原始局部状态，避免只突出全局移动却丢失局部姿态。其目的是兼顾导航与精细身体结构，不等于引入视觉注意力或物体接触特征

### C3. 在状态空间加入目标

classifier guidance（利用目标代价梯度引导扩散采样）把任务目标写成可微成本。静态障碍使用 SDF（有符号距离函数）惩罚身体与障碍接近或穿透；对需要跳上去的平台，只惩罚内部穿透而不必排斥所有接近。waypoint（路径点）代价引导根部接近目标，任务空间代价约束某个身体部位的位置、速度或朝向；动态避障使用不同角色预测位置之间的距离（§4、式 3–5）

motion in-betweening（在稀疏关键帧之间补动作）则在指定未来时刻直接固定已知状态，并把该处噪声等级置零，通过 inpainting（保留已知部分、生成未知部分）补全中间序列。关键帧不必来自连续轨迹，但过于冲突或超出训练覆盖的要求仍可能失败。zero-shot（无需针对新下游任务再训练）只指在已有身体、动作分布与任务表达范围内切换引导，并非任意目标都可成功

### C4. 滚动推理与执行

每个模拟时间步只执行当前动作，随后读入新状态再规划。FIFO（先进先出）缓冲区保留前次预测，近端噪声小、远端噪声大；推出当前已清洁状态—动作对，在远端加新噪声，复用中间去噪结果。这样可减少相邻计划反复切换，同时保留远期多种解法，不是固定开环执行整段动作（§3.2、Fig. 3）

但“保留计划”也会形成惯性，过强一致性可能让角色坚持错误路线。作者因此在较高状态噪声等级 14 保留引导作用，动作滚动等级为 4；这仍依赖具体权重选择。滚动预测中的未来状态是规划变量，最终是否成功要看真实模拟执行，不应只看去噪轨迹图

## D. 实验、基线、消融与分母

### D1. 训练与任务协议

模型六层、八头、512 维嵌入，约 19.95M 参数；训练用单张 A100、1000 epochs，约 24 小时；20 个训练去噪步，推理内存约 1 GB。速度在 RTX 4060 加 TensorRT 的条件下测量，不能转述为普通 CPU、D435i 主机或真机板载平台的实测延迟（§5.2）

Walk-Perturb 在 30 秒行走中每秒施加一次从 0–3000 N 采样的瞬时推扰；不是持续施加 3000 N。Forest 在 8×9 m 区域随机摆 15 根柱，测抵达对面目标的成功率与耗时。Jump 将高 0.3–0.5 m 的箱体放在身前 1–2 m，要求越过且不跌倒。补帧任务拼接三条训练动作、每条按一秒间隔取三个关键帧，评估完成情况与关键帧误差；头高低于 0.2 m 统一判跌倒（§5.2.1）

正文和 Table 1/2 未明确提供各任务百分比所对应的完整 rollout 总数、种子数与置信区间；下表只记录原表百分比，不补造“96/100”之类分母。耗时与位置误差表头也未逐项清楚标单位，故保留原表数值并标作原表尺度，不自行补充所有列的物理单位。训练数据 54 条动作、平均 40 条 rollout，均不能作这些任务结果的评估分母

### D2. 核心对照结果

| Table 1 指标，均为物理仿真 | Kin+PHC：每 1 步重规划 | Kin+PHC：每 16 步重规划 | Diffuse-CLoC：每 1 步重规划 |
| --- | --- | --- | --- |
| Walk-Perturb 跌倒率，越低越好 | 30% | 30% | 16% |
| Walk-Perturb FID，越低越好 | 0.185 | 0.073 | 0.074 |
| Forest 成功率 | 69% | 68% | 96% |
| Forest 耗时，原表尺度 | 39.72 | 16.87 | 13.23 |
| Jump 成功率 | 0% | 22% | 71% |
| 补帧跌倒率 | 66% | 55% | 31% |
| 补帧 MJPE / MRPE，原表尺度 | 0.200 / 0.985 | 0.140 / 0.388 | 0.116 / 0.322 |

FID（Fréchet 分布距离）衡量动作分布差异，不是任务成功率。Kin+PHC 每 32 步重规划时 FID 达 0.038，比本篇 0.074 更低，但跌倒率升到 44%；因此可以说任务稳健性与响应改善，不能说运动质量每项都最好。Forest 中 Kin+PHC 的最佳成功率是 8 步重规划的 83%，若取“最佳基线”比较就应使用 83%，不能只选一行 69% 放大提升。MJPE 为关键帧关节位置误差，MRPE 为根部误差，不宜混作全身连续轨迹误差（§5.3）

Fig. 1 展示 16 个角色静态/动态避障；Fig. 4 展示右手到达目标、路径跟踪、越障与平台跳跃；Fig. 8 展示同一长序列串联任务。这些图支持示范能力，但没有为每种场景给出独立成功率或严格碰撞率分母，不能将 16 个角色写成 16 种机器人本体或真机重复试验

### D3. 架构与滚动消融

Table 2 中固定动作 16 步，状态 16 / 32 / 64 步时 Forest 成功率为 0% / 96% / 19%，Jump 为 0% / 71% / 6%；一秒左右的视野比半秒更能预见障碍，但两秒也可能因不确定性和错误承诺而更差。固定状态 32 步时，动作 4 步的 Jump 成功率为 77%，高于最终 16 步模型的 71%，后者在 Forest 达到 96%，说明最终选择考虑跨任务平衡，不能称所有任务单独最优

完整注意力的 Forest / Jump 为 58% / 53%，Diffuser 局部注意力为 0% / 0%，本文专用注意力为 96% / 71%。这些结果支持在所测任务中避免动作直接依赖嘈杂远期状态，但不是所有联合扩散问题都应使用相同掩码的普遍证明（§5.5、Fig. 7）

双滚动方案为 77.41 Hz，对照非双滚动行为 58.06 Hz；速度依该 GPU 与加速设置。去掉状态滚动会明显损害 Jump，一致性有助于保留起跳动量；Forest 又可能因过度坚持旧计划增加耗时。§5.6 的“25% acceleration”是作者用语，按表频率直接计算相对增加约三分之一，按单次时间折算约减少四分之一；本卡优先保留两个实测频率与条件，避免混用提升分母

附录 Table 3 给出任务代价权重，例如 Jump 的静态障碍项 1、路径点项 0.06，而 Forest 路径点项 0.175。模型无需重训不代表免调任务成本；任务、权重和几何接口仍须人为定义，不能把这些结果写成自动理解未知任务指令

## E. 局限、开源与本项目研究设想

### E1. 作者承认的局限

§6 明确指出引导强度难调，过强约束会产生不自然动作或劣化质量；某些跳跃与爬行任务为保证通过又必须增强障碍约束。训练数据覆盖不足时，角色可能用原地跳跃响应头顶目标，因为训练含跳跃却缺少对应的上举到达动作。增强数据中的动作噪声可能带来足部抖动，而去掉扰动又会产生闭环误差积累，平滑性与鲁棒性仍有矛盾

依赖历史还可能限制动作过渡和引导响应速度。作者明确把 human-object interaction（人与物体交互）、physical manipulation（物理操作）与 contact-rich behaviors（多接触行为）列为开放问题，因此右手碰目标的可视化不能充当多指抓取、物体稳定夹持或手内重定位的验证

### E2. 本库分析

全部定量实验在模拟角色上，未给真实执行器迟滞、关节限位误差、感知遮挡或硬件算力部署结果。动态避障读取其他角色预测轨迹，也不等于解决从 D435i 图像跟踪未知行人的完整感知预测问题。状态和动作的联合分布能提高可执行性，但本文没有给出不可碰撞的形式保证、分布外安全保证或强扰动后的普遍自恢复机制

带噪 rollout 的“纠偏”针对身体控制误差，Walk-Perturb 测身体受推后的稳定性；二者不能升级为高层任务失败恢复。若抓取滑落、目标识别错误或障碍检测丢失，需要额外状态判定、重试与停止策略，论文没有展示这些模块。即使同一模型连续处理多个目标，也不能据此宣称解决任意长时操作任务

### E3. 开源、材料与许可

截至 2026-10-24，可访问官方 arXiv 全文、RAI 论文条目及 SIGGRAPH 日程；RAI 条目中的项目页链接返回 404。本轮未从官方来源核实可下载的训练代码、检查点、数据集或部署脚本，故开源状态记为“未核实官方实现”，不写成“已完整开源”，也不将第三方仿写仓库算作作者发布。项目页不可访问不能单独证明永远闭源

arXiv 条目链接 CC BY-NC-ND 4.0；PDF 首页另有 ACM 权利声明，二者都不是软件代码许可。AMASS、SMPL 与 PHC+ 的使用还需分别查看各自条款，不能从可读论文推导可任意分发数据或模型。本轮进行全文与元数据核验，没有训练模型或复现表格；实际复现仍受未核实的官方实现、数据生成配置及计算环境影响

### E4. 面向 DH116、机械臂与 D435i 的设想

可以先选择机械臂的低速避障到达，让状态包括末端、关节与目标物体位姿，动作使用现有控制器可接受的增量接口，比较“状态规划＋独立跟踪”“动作扩散”“状态—动作联合扩散”三组。以新障碍位置测试引导泛化，同时报告实际执行碰撞、目标误差、动作平滑度和超时率；不要只比较生成轨迹是否好看

若进一步用 DH116，必须加入可观测的指尖、接触与物体状态，并重新处理欠驱动耦合和动作维度，不能直接使用本文的 69 维球关节目标。D435i 提供的几何需要时间戳对齐、手眼标定和遮挡处理；当深度不可靠时，状态成本的梯度可能把策略引向错误目标。可研究在联合生成中保留感知不确定性并降低不可信约束权重，但这属于本库提出的实验方向，本文没有验证

建议先用固定物体与简单碰触检查建模，再做抓取接触；将“动作偏离后纠偏”与“物体滑落后重抓”分别建协议，单独统计触发条件、恢复次数和总回合成功率。这样才能判断状态引导对操作任务是否有用，而不是把模拟人的越障结果换一个名称当作灵巧手成果

## 来源与阅读证据

- [arXiv 版本页](https://arxiv.org/abs/2503.11801)与[固定 v3 全文](https://arxiv.org/pdf/2503.11801v3)：首页作者机构、§1–6、Fig. 1–8、Table 1–3、附录 A；本轮视觉核对 Fig. 3 与 Table 1/2
- [ACM DOI](https://doi.org/10.1145/3731206)与[出版者 Crossref 元数据](https://api.crossref.org/works/10.1145/3731206)：期刊、卷期、线上与印刷时间；本轮 ACM 页面直接访问受限，未据其空白页补造信息
- [RAI 官方条目](https://rai-inst.com/resources/papers/diffuse-cloc-guided-diffusion-for-physics-based-character-look-ahead-control/)和[SIGGRAPH 日程](https://s2025.conference-schedule.org/presentation/?id=papers_1047&sess=sess156)：作者、项目入口及报告日期
- [BeyondMimic v4](https://arxiv.org/abs/2508.08241)：第 4、36、49 页与参考文献 #45；采用实际引文说明关系，未宣称复用未经核实的代码

## 研究关联入口

[[02 研究方向/全身运动技能与具身执行框架|全身运动技能与具身执行框架]] · [[01 论文文库/论文编号索引|稳定编号索引]]
