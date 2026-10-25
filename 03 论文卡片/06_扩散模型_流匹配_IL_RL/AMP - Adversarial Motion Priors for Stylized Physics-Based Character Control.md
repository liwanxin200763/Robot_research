---
paper_id: P213
title: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control'
authors:
- Xue Bin Peng
- Ze Ma
- Pieter Abbeel
- Sergey Levine
- Angjoo Kanazawa
year: 2021
venue: ACM Transactions on Graphics 40(4), Article 144; Proc. SIGGRAPH 2021
arxiv: '2104.02180'
version: v2
arxiv_version: v2
pdf: 01 论文文库/PDFs/06_扩散模型_流匹配_IL_RL/AMP.pdf
verified_on: '2026-10-24'
citation_status: 待 Google Scholar 人工核验
tags:
- Motion_Control
- Imitation_Learning
- Reinforcement_Learning
- Physics_Based_Animation
document_type: 期刊论文（SIGGRAPH会议成果）
preprint_platform: arXiv
first_public_date: '2021-04-05'
first_public_month: 2021-04
first_public_scope: arXiv v1 submission history (UTC); other earlier platforms not exhausted
latest_preprint_date: '2022-05-12'
latest_preprint_version: v2
publication_status: 已正式发表
published_venue: ACM Transactions on Graphics 40(4), Article 144; Proc. SIGGRAPH 2021
publication_year: 2021
doi: 10.1145/3450626.3459670
affiliations:
- University of California, Berkeley
- Shanghai Jiao Tong University
metadata_verified_on: '2026-10-24'
metadata_sources:
- https://arxiv.org/abs/2104.02180
- https://xbpeng.github.io/projects/AMP/index.html
- https://xbpeng.github.io/projects/AMP/AMP_2021.pdf
- https://doi.org/10.1145/3450626.3459670
pdf_version: Author-hosted PDF; 20 pages including supplements; arXiv byte identity not checked
---

# AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control

## 基本信息

- 稳定编号：P213；作者：Xue Bin Peng、Ze Ma、Pieter Abbeel、Sergey Levine、Angjoo Kanazawa；前两位为共同第一作者
- 年份：2021
- 正式发表：ACM Transactions on Graphics 40(4), Article 144，Proc. SIGGRAPH 2021；DOI：[10.1145/3450626.3459670](https://doi.org/10.1145/3450626.3459670)
- 作者机构：Ze Ma署名Shanghai Jiao Tong University，其余四位署名University of California, Berkeley，依据官方PDF首页
- arXiv：[2104.02180](https://arxiv.org/abs/2104.02180)；首次提交2021-04-05，首次公开月份2021-04；限定为arXiv v1提交历史UTC，未穷尽其他更早公开渠道
- 最新预印本：v2，2022-05-12；正式发表年份仍为2021，不把预印本修订误记为出版年份
- 项目：[作者主页](https://xbpeng.github.io/projects/AMP/index.html)；原始代码：[xbpeng/DeepMimic](https://github.com/xbpeng/DeepMimic)，该仓库同时承载DeepMimic和AMP
- 本地 PDF：[[01 论文文库/PDFs/06_扩散模型_流匹配_IL_RL/AMP.pdf|AMP 官方全文]]，作者托管版20页，含Appendix A–D与学习曲线
- 引用量：待核验
- 引用量来源：Google Scholar
- 核验日期：2026-10-24

## 论文简介

如果希望仿真角色走到目标旁再出拳，传统参考跟踪通常先规定跟哪个片段、何时换片段，再让控制器逐帧追踪。动作库越大，挑选、同步和编排越复杂。AMP把问题改为学习“这段运动是否像示范中的风格”：判别器比较示范与策略生成的相邻身体状态，给出风格奖励；策略同时获得任务奖励，于是能够围绕目标自行组合动作，而不必事先选择固定参考轨迹

训练输入是无任务标注的参考姿态序列、仿真角色状态和任务目标，输出仍是关节比例微分控制器的目标位置。判别器只用与动作相关的局部姿态、速度和手脚位置，不读取具体任务目标；策略也没有参考相位输入。最小二乘判别损失、梯度惩罚和历史样本回放共同稳定对抗训练。这里的运动先验是一种学习得到的奖励模型，并非扩散轨迹生成器，也不需要示范者施加的控制力矩

实验在Humanoid、T-Rex和Dog的物理仿真中进行。最大Locomotion数据集为56片段、8位演员、434.1秒。Table 1中Target Heading回报为0.90±0.01，按3个训练种子、每种子32回合评价；这不是90%任务成功率。单片段对照显示AMP多数动作误差高于同步跟踪，换来的是免相位同步和较自然的技能组合。作者承认模式坍塌、跨任务重用不足及部分前空翻局部最优；附录D还做了边走边挥手的有限空间组合实验。对BeyondMimic，它提供可对照的风格约束路线；对机械臂、DH116和D435i，则主要启发如何从示范学习接触动作偏好，尚未证明视觉抓取或真机迁移。其价值在于让同一任务通过更换示范集合呈现不同运动风格，并明确展示数据覆盖范围会改变策略能学到的动作

## 快速摘要

- 研究问题：从多种未按任务分段、编排的动作片段学习风格约束，使物理角色为目标自主组合技能
- 先前不足与核心思路：相位跟踪依赖参考选择与手工相似度；用判别器学习状态转移的风格奖励，再与目标奖励合成训练
- 输入与输出：局部身体状态、目标、可选高度场／球状态 → PD关节目标；判别器训练读取示范和策略相邻帧，不需要人的力矩标签
- 数据与Benchmark：动捕库、自录动作和关键帧，Humanoid、T-Rex、Dog仿真；方向、位置、带球、击打、障碍、单片段模仿与有限空间组合
- 主要结果与意义：Table 1/2与Figure 4显示多样示范支持不同速度的步态切换；Table 3显示单片段精确度的代价；可把完成任务与符合动作风格分别优化和评价
- 本项目关系与局限：为BeyondMimic提供对读背景；对本地操作设备提供奖励学习思路，未验证真实抓取，模式覆盖与任务依赖仍待解决
- 摘要证据：已读20页官方全文和Appendix A–D，复核Table 1/2/3/6与Figure 4/8；数字注明归一化回报、米制姿态误差和各自评估分母

## A. 基本研究问题

运动风格与任务目标是不同层次的要求：目标规定“去哪里、打哪个目标”，动作数据规定“以什么姿态和节奏完成”。把所有要求都写成人工奖励容易漏掉自然动作特征；强制跟踪一个片段又限制角色偏离轨迹以适应新情境。论文研究如何直接从不带任务标注的姿态序列提取通用风格信号，并允许策略自行选择何时走、跑、滚动或击打（§1、§3）

“无结构数据”指无需逐段技能标签、任务标签或预先编排，并不意味着无需骨架对应、物理本体建模或数据处理。数据是姿态与由其计算的运动特征，训练仍在可交互物理模拟器中进行；它不是仅凭互联网上任意视频直接训练真实机器人

## B. 相关工作与阅读关系

GAIL（生成对抗模仿学习）把模仿变为让策略生成的数据难以被判别器与示范区分。原始形式常读取状态与动作，但动作捕捉没有人的控制指令，AMP改用相邻状态转移来判别。DeepMimic类跟踪方法显式设计姿态误差并同步参考进度；潜变量控制方法将动作压入低维编码，但高层策略可能利用预训练时未覆盖的编码产生异常行为（§2、§4–5、§8.3）

- [[03 论文卡片/06_扩散模型_流匹配_IL_RL/DeepMimic - Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills|DeepMimic]] 是论文直接讨论和实验对比的跟踪方法来源，帮助理解取消相位同步的收益和代价
- [[03 论文卡片/06_扩散模型_流匹配_IL_RL/BeyondMimic - From Motion Tracking to Versatile Humanoid Control via Guided Diffusion|BeyondMimic]] 是本库核心对读入口，可比较对抗风格奖励与引导扩散如何约束可行动作；知识组织上的并列不等于已核实的模型直接继承关系

## C. 方法：数据、奖励与控制循环

### 1. 分开策略输入与判别器输入

策略π(a|s,g)读取角色身体状态s和目标g。状态包括身体段相对根部的位置、姿态、线速度和角速度，坐标系以骨盆为原点、身体朝向为局部前向，旋转用6维法向／切向编码。任务再追加目标方向和速度、目标位置、足球状态或地形高度场。策略不接收参考片段ID、相位或未来参考姿态（§6.1）

判别器D读取两个相邻时刻经特征映射Φ处理后的身体信息：根部速度、关节局部旋转与速度、手脚等末端位置。它不读取目标或地形任务标签，也不看人的动作指令。相邻帧提供变化信息，显式速度还能帮助识别“真的在滚动”与“静止保持某个滚动姿态”（§5.1、§5.3、§8.5）

### 2. 学习风格奖励

最小二乘判别器把真实示范转移的分数推向+1，策略转移推向−1，而非用会饱和的sigmoid分类损失。风格奖励为 rS=max[0,1−0.25(D−1)²]，范围[0,1]；它给出动作风格相似度，不保证特定片段逐帧重现。总奖励为r=wG·rG+wS·rS，附加任务实验权重各0.5，单片段模仿只优化风格项（§5.2、§8.2、§8.4）

梯度惩罚约束判别器在示范特征上的梯度，系数10，缓解对抗训练振荡；判别器还从历史策略回放缓冲区抽样，防止只记住最近一批策略的缺点。判别器、策略和价值函数共同迭代，并非先训练一个固定奖励模型后永不更新（§5.4、§6.3、Algorithm 1）

### 3. 用物理仿真生成可执行动作

策略输出高斯分布的均值，固定对角协方差提供探索。网络隐藏层1024、512单元；价值和判别网络结构相近。动作是各关节PD（比例微分）控制目标：球关节用3维指数映射，即向量方向指定旋转轴、模长指定角度；单自由度关节用一个角度。低层PD再产生驱动刚体仿真的关节力矩，策略查询30Hz、物理仿真1.2kHz（§6.1–6.2、§8.1）

参考状态初始化从数据中随机抽起点；大多数任务在脚以外身体段碰地时提前终止，滚动和起身等任务需取消该规则。策略与价值函数用PPO更新，判别器从示范与历史策略样本更新。Appendix B每轮4096样本、批量256、回放容量10万；单片段γ=0.95、任务γ=0.99，以便在任务中考虑更长回报

### 4. 任务奖励仍需明确设计

Target Heading奖励目标速度与指定方向质心速度的接近程度；Target Location兼顾目标距离和朝目标移动；Strike分为远处接近、近处出拳、已命中三个阶段；障碍任务使用向前运动奖励与高度场。风格奖励减少了手工设计动作细节的负担，并没有取消目标定义、分段任务逻辑或安全约束设计（Appendix A）

障碍高度场是前方10米内100个均匀高度采样点，论文未实现从D435i RGB-D流估计它的完整感知模块。带球任务利用已知球位置、姿态与速度，属于仿真足球控制，不能泛称为已经解决机械臂三维物体操作

## D. 实验、基线与消融

### 1. 数据量、训练预算与硬件边界

正文用34自由度Humanoid、59自由度T-Rex、64自由度Dog，全部为Bullet仿真。参考动作来自公开动捕、自录片段和手工关键帧。Table 2最大Locomotion数据集434.1秒、56片段、8位演员；Walk+Punch为247.8秒、15片段、9位演员；Run+Leap+Roll为22.1秒、10片段、7位演员。秒数是示范时长，不是策略采样预算或运行时间

每策略约1亿至3亿仿真样本，在16核CPU约30–140小时。该预算来自原论文设置，不能与使用GPU并行仿真或新版MimicKit的速度混用（§8.1）

### 2. 多片段任务看任务回报，不能直接改写为成功率

Table 1每配置3个随机种子，每模型32回合，报告平均归一化任务回报，0与1对应理论最小、最大回报，数值含±但表注未将其定义为置信区间

| Humanoid任务与示范 | Task Return |
|---|---:|
| Target Heading，Locomotion | 0.90 ± 0.01 |
| Target Heading，仅Walk | 0.46 ± 0.01 |
| Target Heading，仅Run | 0.63 ± 0.01 |
| Obstacles，Run+Leap+Roll | 0.27 ± 0.10 |
| Dribble，Locomotion | 0.78 ± 0.05 |
| Strike，Walk+Punch | 0.73 ± 0.02 |

Figure 4显示混合步态数据更能覆盖约1–5m/s目标速度；只有Walk数据时难以产生快跑，只有Run数据时低速跟随较差。Zombie和Stealthy的目标速度固定1m/s，不宜拿其0.94、0.89与Locomotion跨条件比较。Figure 3展示行走到目标后出拳、跨障碍与滚动组合，这种组合并不要求数据中已有完整任务片段（§8.2）

### 3. 与潜变量控制及无示范基线比较

Figure 5对比AMP、Latent Space和No Data。潜变量基线先用同一批动作跟踪预训练低层，再固定低层，为下游任务训练输出16维潜变量的高层策略；Appendix C给出编码器与目标姿态输入。其低层预训练已用3亿样本，阅读下游学习速度时需要计算这个前置成本。作者定性观察AMP动作更自然、任务回报相近，但论文没有给出覆盖所有任务的统一“自然度提升百分比”（§8.3）

### 4. 单片段精确模仿有明确代价

Table 3将AMP与Peng et al. 2018的Motion Tracking比较，采用DTW（动态时间规整，将节奏不同的两段动作进行时间对齐）后的平均关节位置误差，单位米，关节位置均相对根部。3个种子、各32回合、每回合最多20秒；误差不是抓取位置误差，也不是全局路径误差

| Humanoid动作 | Motion Tracking | AMP |
|---|---:|---:|
| Back-Flip | 0.076 ± 0.021 m | 0.150 ± 0.028 m |
| Cartwheel | 0.039 ± 0.011 m | 0.067 ± 0.014 m |
| Front-Flip | 0.278 ± 0.040 m | 0.425 ± 0.010 m |
| Spin | 0.063 ± 0.022 m | 0.047 ± 0.002 m |
| Side-Flip | 0.191 ± 0.043 m | 0.124 ± 0.012 m |

同步跟踪通常更快、更准，AMP只在部分动作更低误差。前空翻可能退化为向前挪步以免跌倒；免同步也使按参考姿态偏差提前终止的技巧难直接套用（§8.4）

### 5. 消融与附录空间组合

Figure 8移除Gradient Penalty后训练振荡和最终误差显著增加；移除速度输入后，滚动策略可能静止躺地。图中的横轴是训练样本、纵轴是姿态误差，不能将曲线高度解释成成功率，也不从图像估读未列出的精确倍数（§8.5）

Appendix D并非完全没有空间组合证据：以独立Walk和Wave示范训练边走边挥手，数据不含同时做两件事的片段。Table 6每模型100回合，Wave+Walk的Heading Return为0.885±0.184、Waving Return为0.891±0.202；仅Walk为0.945/0.306，仅Wave为0.683/0.949。挥手任务奖励衡量手高度，不能升级解读为复杂交互手势或双臂接触操作；作者仍观察到高举手时动作不自然

## E. 局限、剩余问题与本项目启发

### 作者明确指出的局限

AMP存在mode collapse（模式坍塌，只模仿数据中少量行为）风险，可能忽略更合适的技能。每个策略的先验仍从头训练，虽然判别输入不含任务目标，负样本来自特定任务策略，仍可能带入任务依赖，限制先验复用。正文实验主要关注时间组合；附录空间组合有一定效果，但作者仍将更灵活的同时组合列为后续方向。单片段存在前空翻等局部最优问题（§8.4、§9、Appendix D）

### 本库分析与可检验的研究问题

局部相邻状态的风格匹配并不自动保证长时序任务完成、接触力安全或罕见动作覆盖；正文的高质量动作主要由视觉和姿态误差评价支撑。要面向机器人，应分别评价任务成功、技能覆盖、动作质量和物理安全，并独立验证仿真到真实的状态误差与执行限制。这些是本库分析，论文没有提供真实机器人部署结果

对“机械臂+DH116+D435i”，可以设想从本设备的遥操作示范学习接近、接触、闭合、抬升的状态转移偏好，再与抓取成功奖励结合。输入需要加入对象相对位姿、手指状态、可用接触信息，判别器是否只用两帧需重新验证；D435i负责提供几何观测，不能从AMP已有成果推断其完成了物体识别或遮挡估计。一个具体实验是比较手工动作奖励与学习先验在相同示范和预算下的抓取成功率、失败接触与技能覆盖，属于本库未来实验设计

## 来源与开源边界

- [作者官方PDF](https://xbpeng.github.io/projects/AMP/AMP_2021.pdf)：20页，正文与Appendix A–D；已查关键表图与空间组合附录
- [arXiv版本历史](https://arxiv.org/abs/2104.02180)：v1/v2日期；版本字段描述预印本历史，作者托管PDF未与v2逐字比对
- [官方项目页](https://xbpeng.github.io/projects/AMP/index.html)与[正式DOI](https://doi.org/10.1145/3450626.3459670)：题名、机构、TOG/SIGGRAPH与Article 144
- [官方仓库](https://github.com/xbpeng/DeepMimic)README明确同时对应两篇论文，代码[MIT许可](https://github.com/xbpeng/DeepMimic/blob/master/LICENSE)；当前README标为旧框架并推荐MimicKit，本卡保留原论文预算
- 作者托管PDF首页保留ACM版权／复制条件；arXiv条目指向[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，两种文件的声明分别记录。数据、动作片段和第三方组件不能由代码MIT许可一概覆盖，PDF仅本地保存且不纳入Git发布

## 研究关联入口

[[01 论文文库/专题阅读/全身运动技能与具身执行框架|全身运动技能与具身执行框架]] · [[01 论文文库/论文编号索引|稳定编号索引]]
