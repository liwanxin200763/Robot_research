---
paper_id: P216
title: 'ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills'
authors:
- Tairan He
- Jiawei Gao
- Wenli Xiao
- Yuanhang Zhang
- Zi Wang
- Jiashun Wang
- Zhengyi Luo
- Guanqi He
- Nikhil Sobanbabu
- Chaoyi Pan
- Zeji Yi
- Guannan Qu
- Kris Kitani
- Jessica Hodgins
- Linxi "Jim" Fan
- Yuke Zhu
- Changliu Liu
- Guanya Shi
year: 2025
venue: 'Robotics: Science and Systems (RSS) 2025'
arxiv: '2502.01143'
arxiv_version: v3
pdf: 01 论文文库/PDFs/05_仿真到真实_Sim2Real/ASAP.pdf
verified_on: '2026-10-24'
citation_status: 待 Google Scholar 人工核验
citation_source: Google Scholar
tags:
- Sim2Real
- Humanoid_Control
- Motion_Tracking
- Residual_Learning
document_type: 会议论文
preprint_platform: arXiv
first_public_date: '2025-02-03'
first_public_month: 2025-02
first_public_scope: arXiv v1 submission history (UTC)
latest_preprint_date: '2025-04-26'
latest_preprint_version: v3
publication_status: 已正式发表
published_venue: 'Proceedings of Robotics: Science and Systems XXI'
publication_year: 2025
publication_month: 2025-06
doi: 10.15607/RSS.2025.XXI.066
affiliations:
- Carnegie Mellon University
- NVIDIA
metadata_verified_on: '2026-10-24'
metadata_sources:
- https://arxiv.org/abs/2502.01143
- https://arxiv.org/pdf/2502.01143v3
- https://roboticsproceedings.org/rss21/p066.html
- https://agile.human2humanoid.com/
- https://github.com/LeCAR-Lab/ASAP
---

# ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills

## 出处与版本

- 年份：2025
- 稳定编号：P216；作者依本地 v3 首页列出的 18 人，前四位为共同贡献；完整名单见 YAML
- 作者机构：Carnegie Mellon University（CMU，卡内基梅隆大学）与 NVIDIA；Tairan He、Wenli Xiao、Zhengyi Luo 为双机构，Linxi “Jim” Fan 与 Yuke Zhu 为 NVIDIA，其余为 CMU，不据当前任职改写署名
- 预印本：[arXiv 2502.01143](https://arxiv.org/abs/2502.01143)；首发 2025-02-03 UTC，首发月份 2025-02；仅指 arXiv v1 提交历史，不声称排除其他平台更早公开
- 最新预印本：v3，2025-04-26；v2 为 2025-02-08；本卡按 18 页 v3 正文与附录核验
- 正式发表：[RSS XXI 官方论文页](https://roboticsproceedings.org/rss21/p066.html)，2025 年 6 月；DOI：[10.15607/RSS.2025.XXI.066](https://doi.org/10.15607/RSS.2025.XXI.066)；arXiv DOI 不是会议 DOI
- 姓名版本差异：arXiv 摘要页把 Nikhil 的姓显示为 Sobanbab，本地 v3 首页和 RSS 正式条目均为 Sobanbabu，本卡采用后者；正式条目的 Jessica K. Hodgins / Linxi Fan 与 v3 的 Jessica Hodgins / Linxi “Jim” Fan 属署名格式差异
- [官方项目页](https://agile.human2humanoid.com/)｜[官方仓库](https://github.com/LeCAR-Lab/ASAP)｜[固定版本 PDF](https://arxiv.org/pdf/2502.01143v3)
- 本地 PDF：[[01 论文文库/PDFs/05_仿真到真实_Sim2Real/ASAP.pdf|阅读 ASAP 全文]]；官方合法全文留本地，沿库中 PDF 忽略规则管理
- 引用量：待核验
- 引用量来源：Google Scholar
- 核验日期：2026-10-24

## 论文简介

人形机器人在仿真里能跳起来，到了真机却可能因电机、传动与接触模型不准而失稳。ASAP 研究的是敏捷全身动作的仿真到真实迁移，目标是降低真实机器人与训练仿真器之间的动力学差异，而非增加语言理解或抓取规划。直接调物理参数只能修正预先选定的误差，扩大域随机化又可能让策略过于保守，作者因此用真实动作轨迹学习一个残差动作模型

流程先把人类视频重建成身体动作，经物理模拟清洗和动作重定向后，用强化学习训练单动作跟踪策略。机器人执行这些策略，记录本体状态、动捕位置与动作。随后在仿真中回放真实动作，加上学到的补偿，使模拟轨迹接近真实轨迹；冻结补偿模型，再在这个校正后的仿真器里微调跟踪策略。最终部署的是微调后的策略，残差模型只用于训练仿真器，不在真机执行时叠加到动作上

论文在两个跨仿真器设置与 Unitree G1 真机上验证。Table V 中，踢腿的全局位置误差由 61.2 降到 50.2 mm，未参与残差数据训练的 LeBron 动作为 159 降到 112 mm；这些是动作跟踪误差，不是抓取成功率。真机受数据和硬件损耗限制，只学习踝部四自由度残差，不能把仿真的二十三自由度校正写成已完成的真机结果

它对机械臂、DH116 与 D435i 项目的启发，是先定位传动与接触误差，再以小范围真实轨迹校正仿真，而非直接移植人形动作策略。动捕依赖、数据覆盖不足和高动态采集损伤都限制扩展；相机能否替代动捕、残差能否描述多指接触，还需要独立实验。这些属于本库设想，并非论文已经验证的能力

## A. 基本问题与快速摘要

研究对象为固定手腕的 Unitree G1，全身控制策略输出 23 维关节目标位置，由 PD controller（比例微分关节控制器）驱动。它处理身体平衡、跳跃、踢腿和动作风格，不涉及灵巧手的指尖接触、物体抓取或手内操作；Fig. 1 的篮球姿态也不等于完成真实投篮任务

核心问题可以写成：已知仿真策略和少量真实执行轨迹，怎样使训练时的状态转移接近真实转移，又不必准确识别所有物理参数？ASAP 选择修改“送入仿真器的动作”，让模拟器保留接触与动力学求解，而非直接把神经网络预测的位置增量写进模拟状态。后者可能破坏物理一致性，且随时间累积误差（§I、§III、Fig. 4）

输入分两层：训练管线需要参考身体动作和真实状态—动作轨迹；最终单动作策略只需要五步本体历史及 phase（参考动作进度，0 到 1）。输出为关节目标位置，不是任务级路径，也不是摄像头到动作的视觉策略。成功跟踪需要预先给定动作与相位安排，不能将这种模仿能力等同于自主决定下一项任务

## B. 相关工作、差异与 BeyondMimic 关系

SysID（系统辨识）搜索质量、质心、控制增益等可解释参数，优势是物理含义明确，但误差未必落在所选参数空间。Domain Randomization（域随机化）让策略覆盖参数变化，可增加鲁棒性，但可能牺牲敏捷性。Delta Dynamics（残差动力学）用网络预测模拟状态与真实状态之差，本文的对照实现把残差加到下一状态；ASAP 则把残差加到动作再交由模拟器推进，两者不能统称为同一个“残差策略”（§VI、附录 C）

动作来源也不是全新生成模型：TRAM 从视频恢复 SMPL（参数化人体模型）动作；MaskedMimic 做物理跟踪清洗；形状与运动两阶段重定向提供机器人参考；DeepMimic 启发 phase、RSI 与模仿奖励。ASAP 的新增重点是真实轨迹到训练仿真的校正闭环。其相关工作明确讨论 RGAT 的残差动作校正思想，不能将全部组件都归为 ASAP 首创（§II、§VI-C）

与 [[03 论文卡片/06_扩散模型_流匹配_IL_RL/BeyondMimic - From Motion Tracking to Versatile Humanoid Control via Guided Diffusion|BeyondMimic]] 的关系已核：BeyondMimic v4 参考文献 #33 正式引用 ASAP，在第 4 页把它作为敏捷单动作模仿的代表，第 7 页比较庆祝跳转连续执行，第 48 页 Fig. S2 比较其 PD 增益。BeyondMimic 自身报告的连续五次与前作单次属于该后作的比较叙述，不是 ASAP 的统计失败率，也不证明两篇在完全相同条件下重跑了全部实验

因此，ASAP 是 BeyondMimic 的相关前作和控制设计对照，不宜写成 BeyondMimic 必经的残差校正模块。BeyondMimic 的低阻抗设计、统一跟踪和引导扩散不能由 ASAP 自动推出；与 [[03 论文卡片/06_扩散模型_流匹配_IL_RL/Diffuse-CLoC - Guided Diffusion for Physics-based Character Look-ahead Control|Diffuse-CLoC]] 更合适的并读方式，是分别观察动力学迁移与推理时任务引导这两个瓶颈

## C. 方法：输入 → 处理步骤 → 输出

### C1. 从视频到机器人可跟踪参考

人类视频先经 TRAM 得到全局平移、朝向、身体姿态与形状参数。重建含噪声，作者用 MaskedMimic 在 IsaacGym 中跟踪并保存通过物理模拟验证的动作，再按人体与机器人之间 12 个身体链接的对应关系拟合形状和轨迹，输出清洗后的机器人参考动作。这个过程改善物理可执行性，但没有证明所有视频动作都能保留或适用于任意机器人（§II-A、Fig. 3）

### C2. 单动作预训练

Actor（动作策略）读取五步关节位置、速度、基座角速度、重力方向和历史动作，再加相位；Critic（价值评估器）在仿真训练时可读取参考全局位置、基座线速度等特权信息。PPO（近端策略优化）以身体位置、朝向、速度和关节跟踪为目标，同时限制力矩、动作变化和足部滑动。最终 actor 不依赖全局位置观测，因此运行跟踪策略本身不需要里程计；这不表示后续真实数据采集无需动捕（§II-B、Table I）

两项训练机制需要区分用途：termination curriculum（终止阈值课程）把允许的位置偏离从 1.5 m 收紧至 0.3 m，帮助策略先学会保持与落地，再学精确跟踪；RSI（参考状态初始化）随机选参考动作中间时刻设置初态，让不同动作阶段并行学习。它们是训练中的采样与失效处理，不是部署时检测高层任务失败、重新规划或从跌倒后恢复的系统

### C3. 用真实轨迹训练残差动作

执行预训练策略后，动捕和机载传感器记录基座位置、速度、姿态、角速度、关节位置与速度，以及已下发的动作。仿真以这些轨迹为目标，网络根据当前模拟状态和记录动作输出 Δa，使模拟器执行 a_real＋Δa 后的轨迹接近记录的真实轨迹。PPO 优化跟踪奖励，并惩罚过大补偿与动作变化；并非直接监督回归一个已知的正确 Δa 标签（§III-A/B、Table II）

残差方向容易混淆：假如仿真电机过强、现实无法起跳，残差在模拟器中应削弱有效动作，重现真实限制。它的用途是“让训练环境像真实机器人”，不是给真机额外加力。正文给出 f_ASAP(s,a)=f_sim(s,a＋πΔ(s,a))，这条关系说明残差是训练动力学校正层，不能在部署时机械加回而重复补偿

### C4. 冻结残差、微调并部署

固定 πΔ，在校正后的仿真器内用原跟踪奖励微调原策略；部署时移除 πΔ，把微调策略直接用于真实 G1。跨动作的数据可训练共用残差，但每条单动作跟踪策略仍围绕自己的相位参考。真实机器人之间不能像仿真那样复位，因此另训 locomotion（行走）策略，在动作结束后接管平衡，直到下一个跟踪动作开始；这是动作间站立与行走衔接，没有展示通用语义任务规划或跌倒后的自主再起（§III-C/D、§IV-C）

## D. 实验、基线、消融与证据边界

### D1. 设置与指标

仿真选择 43 条动作，按 Easy、Medium、Hard 分组；IsaacGym 为训练环境，IsaacSim 和 Genesis 为目标环境，二者是跨仿真器验证，不能计作真机试验。对照包括同环境训练测试的 Oracle、直接迁移的 Vanilla、SysID、DeltaDynamics；基础预训练含 Table VI 的摩擦、P 增益、20–40 ms 延迟及推扰随机化，因此“Vanilla”并非完全不使用 DR 的策略（§IV、附录 A/B）

Eg-mpjpe 是全局身体位置误差，Empjpe 是相对根节点的平均关节位置误差，单位 mm；Eacc 为 mm/frame²，Evel 为 mm/frame，不能改成 m/s² 或 m/s。成功定义为整个模仿过程中，平均身体距离误差未超过 0.5 m。43 是动作库规模，不能直接充当 Table IV 每组或每项真机百分比的分母，论文未完整列出每组有效试次与种子明细

### D2. 跨仿真器结果

| 证据与设置 | Vanilla / OpenLoop | ASAP | 可支持的结论 |
| --- | --- | --- | --- |
| Table III，IsaacSim，回放 1.0 s，Eg-mpjpe | 80.8 mm | 37.9 mm | 更准确回放目标环境轨迹 |
| Table III，Genesis，回放 1.0 s，Eg-mpjpe | 82.5 mm | 36.9 mm | 长时动力学匹配改善 |
| Table IV，IsaacSim Hard，Eg-mpjpe | 148 mm | 129 mm | 微调后全局跟踪改善 |
| Table IV，IsaacSim Hard，Empjpe | 51.6 mm | 56.5 mm | 局部姿态误差反而上升 |
| Table IV，Genesis Hard，成功率 | 82.9%±5.70% | 100%±0.000% | 指定跨仿真器模仿任务的结果 |

Table III 的 0.25 s IsaacSim Eg-mpjpe 为 OpenLoop 19.5、ASAP 19.9 mm，说明文中“所有长度始终更好”的文字概括不能替代表格逐项判断。Table IV 中 ASAP 也并非每项误差都最低，特别是局部误差与全局误差会出现权衡。上表保留这一反例，而不把“最好”泛化成全指标统治

### D3. 真机证据

由于全身 23-DoF 残差需大量数据，真机改为 4-DoF 踝部校正。作者记录 100 条动作片段，覆盖 kick、jump forward、step forward/back、single foot balance、single foot jump；另采 10 分钟行走数据。正文另写每个任务执行 30 次，但 Table V 没有把各列有效试次数、重复种子和误差条逐一列出，不能把 100 条训练片段直接作表格评估分母（§IV-C）

| Table V 真机动作 | Eg-mpjpe，Vanilla → ASAP | Empjpe，Vanilla → ASAP | Eacc / Evel，Vanilla → ASAP |
| --- | --- | --- | --- |
| Kick，分布内 | 61.2 → 50.2 mm | 43.5 → 40.1 mm | 2.96 / 2.91 → 2.46 / 2.70 |
| LeBron，残差模型数据分布外 | 159 → 112 mm | 55.3 → 47.5 mm | 3.43 / 6.43 → 2.84 / 5.94 |

由表值计算，全局误差分别降低约 18.0% 与 29.6%；这是本库按原数值计算的相对变化。LeBron 的 OOD（分布外）指其动作不在残差训练集内，但该跟踪策略仍经过校正仿真微调，不是从未训练的任务直接零样本执行。结论处“up to 52.7%”不能直接用 Table V 复核，因此不作为本卡主要真机结论。Fig. 1 的 1.5 m 前跳与 1.3 m 侧跳是动作展示，未给完整重复成功分母

### D4. 消融与不一致记录

Fig. 10 在跨仿真器环境研究数据量、训练时域和残差范数权重：数据增加改善未见轨迹匹配，但从 4300 到 43000 样本时闭环提升趋于饱和；开环偏好更长时域，不意味着微调闭环也持续改善，作者报告闭环最佳时域为 1.0 s。Fig. 11 与附录 D 比较不微调的一步固定点迭代、梯度搜索和 RL 微调，后者更好，支持多步反馈优化的必要性，不是保证任意分布下的收敛证明

Fig. 12 比较随机动作噪声与结构化残差；正文把最佳随机噪声 MPJPE 写为 150，而图注写 173，数值不一致，本卡仅记录定性优劣，不选择其中一个作为确定事实。Fig. 13 的不同关节残差幅值只说明该数据设置中误差有结构；不能把踝部重要性当所有机器人通用规律

## E. 局限、开源范围与本项目设想

### E1. 作者明确承认的局限

§VIII 明确列出硬件过热和损伤、动捕依赖及全身残差训练数据需求。两台 G1 在采集时不同程度损坏，意味着当前高动态数据采集成本并非可以忽略。四自由度简化提升样本效率，却限制了对上肢与全身传动误差的校正覆盖；论文提出损伤感知策略、免动捕校正和更少样本适配作为后续方向，不能写成已实现模块

### E2. 本库分析

数据来自可运行的预训练策略，其覆盖范围与真实硬件状态绑定；更换负载、地面、控制延迟或温度后，残差未必仍可靠。作者没有给出跨任意机器人泛化、感知闭环导航或多指物体交互证据。训练中的终止、RSI 与动作后行走接管只能分别说明训练稳定性与有限策略衔接，尚不足以构成部署失败检测、重试、重新抓取或任务级恢复架构

### E3. 开源与部署边界

截至 2026-10-24，官方仓库 README 已提供 phase 跟踪、残差训练、残差辅助微调、动作重定向、MuJoCo Sim2Sim 与 UnitreeSDK Sim2Real 操作入口，TODO 对应条目已勾选；实际可读取 train_agent.py 和 listener_deltaa.py。README 说明提供原始 SMPL 与 G1 重定向动作、部分模型检查点，并有真实数据采集示例；这证明模块入口与材料已发布，本轮未运行代码，未逐文件审计全部权重、采集数据完整性或复现论文结果

仓库 LICENSE 为 MIT；SMPL、AMASS、IsaacGym、Unitree SDK 等第三方资产和运行时须分别依其许可，MIT 不自动授予这些资产的再分发权。论文 arXiv 条目使用其非独占分发许可，与代码 MIT 分开记录。运行环境包含特定 NVIDIA 仿真器、Linux 和匹配机器人配置；真实部署需要 G1 关节顺序、增益、SDK、安全停机与设备状态适配，不能把演示命令视为适合 DH116 的即插即用控制器

### E4. 面向 DH116、机械臂与 D435i 的研究设想

可先在机械臂低速自由空间与 DH116 简单开合中收集关节命令和实际位置，比较“只调延迟/增益”“域随机化”“小维度残差动作”三组，在新轨迹上同时看跟踪误差、动作平滑度与异常接触。通过后再加入固定物体的受限抓持，把自由空间误差与接触误差分开，避免残差掩盖错误的接触模型。这是可控的小规模研究设计，不是沿用 G1 踝部结论直接证明手部有效

D435i 可用于观察物体位姿与可见末端轨迹，但其可见性、时间对齐、深度噪声与手指遮挡需要实测；它不是天然等价的全身 MoCap 替代品。建议保留独立测量链评估几何误差，以未参与校正的物体位置、负载和抓取姿态测试泛化，同时单独设计滑落检测与停止逻辑。物体失败恢复应作为新增高层模块验证，不能从 ASAP 的动作终止机制推导出来

## 来源与阅读证据

- [arXiv 版本历史](https://arxiv.org/abs/2502.01143)与[固定 v3 全文](https://arxiv.org/pdf/2502.01143v3)：首页署名，§II–VIII，Table I–VII，Fig. 1–13，附录 A–D；本轮读正文与必要附录，并视觉核对 Table IV/V 与方法图
- [RSS 正式条目](https://roboticsproceedings.org/rss21/p066.html)：正式题名、作者、会议月份和 DOI；正文证据仍采用注明版本的 arXiv PDF，不混称为同一个文件
- [官方 README](https://github.com/LeCAR-Lab/ASAP/blob/main/README.md)与[LICENSE](https://github.com/LeCAR-Lab/ASAP/blob/main/LICENSE)：开源模块、第三方资产要求和 MIT；入口存在不等于本库已复现
- [BeyondMimic v4](https://arxiv.org/abs/2508.08241)：参考文献 #33，第 4、7、48 页；关系按实际引文定位，不根据方法相似猜测继承链

## 研究关联入口

[[01 论文文库/专题阅读/全身运动技能与具身执行框架|全身运动技能与具身执行框架]] · [[01 论文文库/论文编号索引|稳定编号索引]]
