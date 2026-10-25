---
paper_id: P214
title: "ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters"
year: 2022
authors:
  - Xue Bin Peng
  - Yunrong Guo
  - Lina Halper
  - Sergey Levine
  - Sanja Fidler
venue: "ACM Transactions on Graphics 41(4), Article 94 (Proc. SIGGRAPH 2022)"
document_type: journal_article
preprint_platform: arXiv
arxiv: "2205.01906"
first_public_date: "2022-05-04"
first_public_month: "2022-05"
first_public_scope: "arXiv v1 submission date in UTC; earlier cross-platform disclosure not exhaustively checked"
latest_preprint_date: "2022-05-05"
latest_preprint_version: v2
publication_status: published
published_venue: "ACM Transactions on Graphics 41(4), Article 94"
publication_year: 2022
publication_month: "2022-07"
published_online_date: "2022-07-22"
doi: "10.1145/3528223.3530110"
affiliations:
  - "University of California, Berkeley, USA"
  - "NVIDIA, Canada"
  - "University of Toronto, Canada"
affiliation_scope: "arXiv v2 first-page author affiliations"
pdf: "01 论文文库/PDFs/06_扩散模型_流匹配_IL_RL/ASE.pdf"
code: "https://github.com/nv-tlabs/ASE"
citation_count: null
citation_source: "Google Scholar"
citation_status: "待人工核验"
verified_on: "2026-10-24"
metadata_verified_on: "2026-10-24"
metadata_sources:
  - "https://arxiv.org/abs/2205.01906"
  - "https://arxiv.org/pdf/2205.01906v2"
  - "https://xbpeng.github.io/projects/ASE/index.html"
  - "https://api.crossref.org/works/10.1145/3528223.3530110"
  - "https://github.com/nv-tlabs/ASE"
---

# ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters

## 基本信息

- 年份：2022
- 稳定编号：P214；研究方向：模仿学习、强化学习、可复用运动先验；归档分类不表示本方法使用扩散模型
- 作者与对应机构按 arXiv v2 首页：Xue Bin Peng 为 University of California, Berkeley 与 NVIDIA；Yunrong Guo、Lina Halper 为 NVIDIA；Sergey Levine 为 University of California, Berkeley；Sanja Fidler 为 University of Toronto 与 NVIDIA
- 出处：ACM Transactions on Graphics 41(4)，Article 94，Proc. SIGGRAPH 2022；DOI：[10.1145/3528223.3530110](https://doi.org/10.1145/3528223.3530110)
- 时间边界：arXiv v1 为 2022-05-04 UTC，v2 为 2022-05-05 UTC；期刊卷期月份为 2022-07，Crossref 另记录在线出版日 2022-07-22；不将预印本、卷期与会议时间混写
- [arXiv](https://arxiv.org/abs/2205.01906) · [作者项目页](https://xbpeng.github.io/projects/ASE/index.html) · [官方代码](https://github.com/nv-tlabs/ASE)
- 本地全文：[[01 论文文库/PDFs/06_扩散模型_流匹配_IL_RL/ASE.pdf|ASE.pdf]]，保存 arXiv v2，18 页含 Appendix A
- 引用量：待核验
- 引用量来源：Google Scholar
- 核验日期：2026-10-24

## 论文简介

ASE 研究如何把人体动作数据变成能够反复使用的运动能力，而不是为每个新任务重新学一次站立、行走和挥剑等基础动作 论文的对象是带剑盾的物理仿真人体角色，输入包括当前身体状态和连续技能向量，输出是各关节比例微分控制器的目标旋转 它先用无任务标注的动作片段训练底层策略，再固定底层，为不同任务学习负责选择技能的高层策略 核心区别在于不逐帧追踪某条指定动作，而是通过对抗模仿匹配动作转移分布，同时用互信息和多样性目标让不同技能向量产生可区分、可切换的行为

实验使用 Reallusion 的 187 条动作、约 30 分钟参考数据，底层在 4096 个并行环境中采集超过 100 亿条仿真样本 下游包含 Reach、Speed、Steering、Location、Strike 五项任务 Table 1 的 ASE 回报依次为 0.75、0.93、0.90、0.45、0.82，这些是每个模型评估 4096 回合、跨三个模型汇总的归一化回报，并不是成功率 从头训练在其中四项的回报更高，但作者观察到不自然动作，因此论文的价值主要是可复用技能、动作风格与学习效率的结合，而不是所有分数都最高

对 DH116 或机械臂加 D435i，可借鉴“固定底层技能、由高层选择技能”的分层接口，以及把任务达成和动作质量分开评价的做法 但论文没有真机、视觉观测、手指抓取或柔性物体证据，人体状态和剑盾技能也不能直接迁移为机械臂控制 本简介依据全文 Sections 4–11、Table 1、Figures 9–14 与 Appendix A，作者仍承认模式坍塌、训练耗样本和部分动作不自然

## 快速摘要

- 研究问题：从非结构化动作数据中学习可供新任务复用的底层运动能力
- 先前不足：逐任务学习重复消耗样本；直接动作跟踪约束行为接近特定参考；单纯对抗模仿容易只覆盖少数动作
- 核心思路：对抗模仿保证风格，互信息促进可区分技能，连续球面潜变量提供高层动作空间
- 输入与输出：预训练读参考状态转移与当前身体状态；推理读当前状态和技能向量，输出关节目标；高层另读任务目标
- 数据与评测：187 段 Reallusion 动作、Isaac Gym 仿真、五类下游任务与恢复测试；没有机器人实测
- 主要结果：Table 1 必须同时读 Scratch 与消融；不能把归一化回报当成功比例
- 为什么重要：把动作先验从单任务奖励塑形推进为可组合的策略接口
- 当前项目关系：适合作为分层控制和先验评测的概念基线，不能直接作为 DH116 权重或 D435i 感知模块
- 主要局限：训练成本高、技能覆盖不完整、仍有抖动和过强恢复动作
- 摘要证据：arXiv v2 全文、关键表图与附录，已核对表格版面

## A. 基本问题与研究定位

### A1. 要复用的是控制能力

论文把运动技能建模为底层策略 π(a|s,z)，其中 s 是人体状态，z 是技能潜变量，a 是仿真关节控制指令 高层策略 ω(z|s,g) 根据任务目标 g 选择 z，从而组合底层已学能力 同一个底层服务所有下游任务，但每个任务仍训练单独高层，不能称为无需额外训练的通用任务执行器 [Section 4、Section 10.3]

预训练使用动作数据的状态转移，不需要给每个片段加“跑步”“挥剑”等技能标签，也不要求先分割成离散技能 类别语义是学习后的行为解释，不是训练时监督标签 这种无标签技能接口降低数据整理需求，但也意味着用户不能直接用自然语言精确指定某个技能 [Sections 5–6]

### A2. 技术路线边界

ASE 属于对抗模仿与无监督技能发现的结合，既不是扩散动作生成器，也不是在真实机器人上验证的运动基础模型 它主要讨论自然动作风格、技能多样性和高层控制之间如何协调，而不是视觉定位、机械臂逆运动学或夹爪接触稳定性

## B. 相关工作与差异

DeepMimic 等动作跟踪方法通过显式参考轨迹教角色完成特定动作，能够忠实模仿，但为了完成新任务常需规划器挑选参考轨迹 AMP（Adversarial Motion Priors，对抗运动先验）用判别器奖励鼓励自然动作，能在任务中组合数据里的行为，但通常仍为任务重新训练策略 ASE 延续分布匹配思想，把一个带潜变量的底层策略预训练为可重用控制接口 [Section 2]

纯无监督技能发现可以增加探索多样性，却不保证得到类似人的行为 ASE 同时要求生成转移像参考数据，又能从转移反推出潜变量，避免技能向量变化却动作始终相同 论文没有声称完全解决技能模式坍塌，其讨论章节明确认为动作覆盖仍不足

与 [[03 论文卡片/06_扩散模型_流匹配_IL_RL/MaskedMimic - Unified Physics-Based Character Control Through Masked Motion Inpainting|MaskedMimic]] 的区别是：ASE 让新任务训练高层来选抽象技能，MaskedMimic 让用户用部分运动约束直接控制一个模型 后者在相关工作中明确讨论 ASE，且在其 VR 表中纳入 ASE 基线；这不等于所有实验共享同一训练配置

与 [[03 论文卡片/06_扩散模型_流匹配_IL_RL/BeyondMimic - From Motion Tracking to Versatile Humanoid Control via Guided Diffusion|BeyondMimic]] 的联系属于本库按研究问题组织的补充阅读；未核实 BeyondMimic 直接引用 ASE，不据此声称直接继承 可比较“高层选技能”与“生成参考运动后交由控制器执行”两种接口

## C. 方法流程、训练与技能表征

### C1. 输入、动作与网络

仿真人体有 37 个自由度，佩戴剑和盾 状态是 120 维，包含根部高度与方向、局部速度、关节旋转以及手脚、盾和剑尖位置 动作是 31 维目标旋转，交给 PD（Proportional-Derivative，比例微分）控制器执行；角色总自由度不等于可控动作维数 [Section 8]

底层策略和价值网络采用全连接网络；编码器与判别器共享主体、输出头分开 高层输出未经归一化的技能向量，再投影到单位球面 底层每秒决策 30 次，高层每秒 6 次，物理模拟每秒 120 步，因此高层输出会在五个底层步中保持 [Sections 8、10.1、Appendix A]

### C2. 对抗模仿与互信息

判别器 D(s,s′) 区分参考动作与策略生成的状态转移，底层获得 −log(1−D) 风格奖励 这匹配的是边缘转移分布，不要求任何一条生成轨迹逐帧对齐原片段 另一个编码器 q(z|s,s′) 从动作转移预测技能，其对数似然构成互信息的变分下界，鼓励潜变量和行为建立稳定关联 [Equations 2–10]

潜变量是 64 维单位球面上的连续向量，由标准高斯向量归一化采样 编码器使用 von Mises–Fisher 分布，即定义在球面上的方向分布 球面有界可减少高层挑选远离预训练分布的技能，同时便于连续插值 这是一种设计上的约束，不构成真实机器人安全保证 [Section 6.1–6.2、Table 2]

### C3. 响应性与训练顺序

预训练中，同一条轨迹会切换 z，每个技能保持 1–150 步，使策略不能只在回合开始读一次潜变量 多样性目标比较两个技能引出的动作分布差异和潜变量距离，推动不同技能产生不同控制响应，同时避免所有潜变量坍塌到同一个动作 [Equation 15、Appendix A]

每回合有 10% 概率从随机跌倒姿态开始，鼓励底层同时掌握恢复能力 每轮先采样仿真轨迹、更新编码器、用参考与生成转移更新判别器，再用 PPO（Proximal Policy Optimization，近端策略优化）更新策略和价值函数 [Algorithm 1、Section 6.5]

迁移阶段固定底层和判别器，高层用任务奖励加风格奖励训练，权重为 0.9 和 0.1 仍保留风格约束，是因为高层快速切换技能也可能形成抖动 新任务不再读取动作数据，不等于不再训练策略 [Equation 16、Section 10.6、Table 3]

## D. 实验、真实数字与消融

### D1. 规模与指标口径

Section 10.1 使用单张 NVIDIA V100、4096 个并行环境，187 段约 30 分钟动作 底层超过 100 亿样本约对应十年仿真时间，训练约十天 这些是并行仿真经验与墙钟成本，既不是十年人类数据，也不是十天真机训练

Table 1 将回报归一化到理论每回合最小值 0 和最大值 1；三个模型使用不同预训练底层，每个模型评估 4096 回合 下表保留原表的 ± 项，原表未在表注中明确其统计类型，不补称置信区间或标准误

| 任务 | Scratch | No SD + No Div. | No SD | No Div. | ASE |
| --- | --- | --- | --- | --- | --- |
| Reach | 0.56 ± 0.11 | 0.18 ± 0.05 | 0.33 ± 0.05 | 0.72 ± 0.02 | 0.75 ± 0.01 |
| Speed | 0.95 ± 0.01 | 0.87 ± 0.01 | 0.87 ± 0.01 | 0.93 ± 0.01 | 0.93 ± 0.01 |
| Steering | 0.94 ± 0.01 | 0.72 ± 0.01 | 0.74 ± 0.02 | 0.90 ± 0.01 | 0.90 ± 0.01 |
| Location | 0.67 ± 0.01 | 0.22 ± 0.04 | 0.25 ± 0.06 | 0.47 ± 0.01 | 0.45 ± 0.01 |
| Strike | 0.87 ± 0.01 | 0.21 ± 0.13 | 0.50 ± 0.07 | 0.80 ± 0.02 | 0.82 ± 0.01 |

Scratch 是从头训练；SD 是技能发现目标，Div. 是多样性目标 去掉 SD 后 Reach 和 Strike 明显下降，但去掉 Div. 对这五项回报的影响较小 不能把不同机制一概写成“都有巨大分数提升” Scratch 四项回报最高，作者用 Figure 8 与视频指出其中存在不自然行为，因此动作风格和任务回报必须分别评价

### D2. 精度、覆盖与恢复

Reach 的剑尖平均误差为 0.088 ± 0.046 m [Section 10.3]，对应此仿真目标设置，不能解释为机械臂毫米级定位 Figure 10 从 1000 条轨迹匹配参考片段，观察动作分布覆盖；Figure 9 则统计约 1000 条切换技能轨迹中出现的有向动作对，ASE 约覆盖全部可能转移的 10% 这里分母是动作对的可能组合，不是任务次数，也不是数据里已含转移的比例 [Section 10.4]

随机扰动力为 500–1000 N，施加于根部 0.5 s；500 次试验均恢复，平均 0.31 s、最慢 4.1 s 判定跌倒为脚以外身体接触地面；判定恢复为根部高于 0.5 m 且头部高于 1 m [Section 10.7、Figure 14] 这只是该角色和扰动分布内的结果，不能推广成任何跌倒都能恢复，更不能当真机抗冲击能力

## E. 局限、项目迁移与未来问题

### E1. 作者明确指出

Section 11 承认对抗训练仍会模式坍塌，技能发现目标不能完整覆盖大动作库；下游任务相对简单，复杂环境和更长技能组合尚需研究；训练样本很多；恢复可能出现过强旋转、翻滚，常规动作也可能抖动 作者提出探索其他分布匹配近似，包括流模型和扩散模型，以及加入自然恢复数据和能量效率目标 这些是未来方向，不能回写为本文已实现功能

### E2. 本库对 DH116、机械臂和 D435i 的判断

可迁移的是控制架构：把伸手、保持、退回等可重复能力作为底层接口，高层选择技能，并同时报告任务完成与动作平滑性 还可借鉴“去掉技能区分后是否退化成单一动作”的消融，避免训练出的技能库表面多样、实际无效

不可直接迁移的是人体球面技能权重、剑盾动作数据和全状态观测 DH116 的具体关节限制、执行延迟、碰撞接触与此仿真人体不同；机械臂还涉及末端位姿、夹持力、物体滑移和工作空间边界 D435i 给的是图像与深度，需要另做目标估计和坐标标定，本文没有提供从深度图到技能选择的视觉系统

本库建议把 ASE 当“先验是否改善探索与动作质量”的研究对照，而不是优先复现完整十天预训练 可先在小仿真环境比较关节动作空间与技能动作空间，再考虑真实平台接口；这是本库设想，论文未验证

### E3. 开源范围与复现边界

官方 ASE 仓库提供训练与任务配置、动作数据、底层及任务预训练模型和重定向示例，README 已标记旧代码不再维护，并推荐 MimicKit 原仓库 LICENSE.txt 为 NVIDIA License，Section 3.3 限研究或评估等非商业用途；Reallusion 动作也明确仅非商业使用 不能标为 MIT 或声称数据任意商用；论文、代码、数据许可应分开判断

## 来源与阅读证据

- [arXiv 版本页](https://arxiv.org/abs/2205.01906)：v1/v2 日期、正式题名、作者与关联 DOI
- [arXiv v2 全文](https://arxiv.org/pdf/2205.01906v2)：已读 Sections 1–11 与 Appendix A，重点核对 Table 1–3、Figures 9–14；表格页面已渲染核对
- [作者项目页](https://xbpeng.github.io/projects/ASE/index.html)：机构对应与 TOG/SIGGRAPH 出处
- [Crossref 出版记录](https://api.crossref.org/works/10.1145/3528223.3530110)：卷期、出版月份与在线日期；题名在记录中分成 title 与 subtitle
- [官方代码与 README](https://github.com/nv-tlabs/ASE) · [原仓库许可](https://github.com/nv-tlabs/ASE/blob/main/LICENSE.txt)：公开材料范围、旧仓库状态与非商业限制

## 研究关联入口

[[01 论文文库/专题阅读/全身运动技能与具身执行框架|全身运动技能与具身执行框架]] · [[01 论文文库/论文编号索引|稳定编号索引]]
