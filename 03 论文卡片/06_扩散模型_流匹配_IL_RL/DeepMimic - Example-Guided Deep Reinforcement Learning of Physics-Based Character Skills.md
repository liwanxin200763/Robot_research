---
paper_id: P212
title: 'DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills'
authors:
- Xue Bin Peng
- Pieter Abbeel
- Sergey Levine
- Michiel van de Panne
year: 2018
venue: ACM Transactions on Graphics 37(4), Article 143; Proc. SIGGRAPH 2018
arxiv: '1804.02717'
version: v3
arxiv_version: v3
pdf: 01 论文文库/PDFs/06_扩散模型_流匹配_IL_RL/DeepMimic.pdf
verified_on: '2026-10-24'
citation_status: 待 Google Scholar 人工核验
tags:
- Motion_Control
- Imitation_Learning
- Reinforcement_Learning
- Physics_Based_Animation
document_type: 期刊论文（SIGGRAPH会议成果）
preprint_platform: arXiv
first_public_date: '2018-04-08'
first_public_month: 2018-04
first_public_scope: arXiv v1 submission history (UTC); other earlier platforms not exhausted
latest_preprint_date: '2018-07-27'
latest_preprint_version: v3
publication_status: 已正式发表
published_venue: ACM Transactions on Graphics 37(4), Article 143; Proc. SIGGRAPH 2018
publication_year: 2018
doi: 10.1145/3197517.3201311
affiliations:
- University of California, Berkeley
- University of British Columbia
metadata_verified_on: '2026-10-24'
metadata_sources:
- https://arxiv.org/abs/1804.02717
- https://xbpeng.github.io/projects/DeepMimic/index.html
- https://xbpeng.github.io/projects/DeepMimic/DeepMimic_2018.pdf
- https://doi.org/10.1145/3197517.3201311
pdf_version: Author-hosted PDF; 18 pages including supplements; arXiv byte identity not checked
---

# DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills

## 基本信息

- 稳定编号：P212；作者：Xue Bin Peng、Pieter Abbeel、Sergey Levine、Michiel van de Panne
- 年份：2018
- 正式发表：ACM Transactions on Graphics 37(4), Article 143，Proc. SIGGRAPH 2018；DOI：[10.1145/3197517.3201311](https://doi.org/10.1145/3197517.3201311)
- 作者机构：前三位署名 University of California, Berkeley；Michiel van de Panne 署名 University of British Columbia，依据所读官方 PDF 首页
- arXiv：[1804.02717](https://arxiv.org/abs/1804.02717)；首次提交 2018-04-08，首次公开月份 2018-04；限定为 arXiv v1 提交历史 UTC，未穷尽其他平台更早记录
- 最新预印本：v3，2018-07-27；另有 v2，2018-06-16；正式出版状态与预印本修订时间分别记录
- 项目：[作者主页](https://xbpeng.github.io/projects/DeepMimic/index.html)；代码：[xbpeng/DeepMimic](https://github.com/xbpeng/DeepMimic)
- 本地 PDF：[[01 论文文库/PDFs/06_扩散模型_流匹配_IL_RL/DeepMimic.pdf|DeepMimic 官方全文]]，作者托管版共18页，含第15–18页补充材料；不将此页数与出版页数混用
- 引用量：待核验
- 引用量来源：Google Scholar
- 核验日期：2026-10-24

## 论文简介

让仿真角色向前移动并不难，难的是让它以像人一样的姿态完成后空翻、旋踢、起身，并能在受到扰动或目标改变后继续行动。单纯奖励“到达目标”容易产生奇怪但有效的动作，逐帧播放运动捕捉又无法处理真实物理接触。DeepMimic 把运动捕捉或手工关键帧当作动作示范，将“接近参考动作”和“完成指定任务”同时写入奖励，再用强化学习训练能够闭环反馈的控制策略

输入包括角色当前身体状态、参考片段的相位以及可选的目标方向、目标位置或地形高度；输出是各关节比例微分控制器的目标角度，控制器再产生关节力矩。方法并不需要示范者真实施加的力矩。两个训练设计尤其关键：从参考动作的不同时间点初始化，让策略尽早见到翻转和落地；在出现不允许的地面接触后结束回合，避免学成倒在地上模仿四肢运动。它还探索了多片段奖励、技能选择输入和依据价值函数组合已有策略

实验涵盖 Humanoid、仿真 Atlas、T-Rex 和 Dragon。Table 4 中，模仿与任务奖励共同训练的旋踢击中率为99%、投球为75%，每种策略评估100次；这些是特定仿真任务成绩，不能解释成通用机器人成功率。Table 2 的步行0.985则是归一化回报，不是98.5%成功率。作者承认相位同步限制动作节奏、多片段扩展和训练成本仍有困难，也未完成真实机器人部署。对本库，它是理解“先跟踪示范、再适应任务”的基础；对机械臂、DH116和D435i，只能提取奖励设计与训练分布的启发，抓取和视觉闭环能力仍需另行验证。它的重要性在于把动作质量转化为能够与目标共同优化的学习约束，并用消融揭示回合设计会改变最终技能

## 快速摘要

- 研究问题：用少量参考动作训练既自然又能适应任务和物理扰动的仿真控制策略
- 先前不足与核心思路：任务奖励容易被取巧，运动学播放缺少物理反馈；把模仿奖励与任务奖励结合，并改善回合起点和失败终止规则
- 输入与输出：身体状态、相位、可选目标与高度图 → 关节 PD 目标角度 → 力矩；不输入 RGB-D、不输出抓取位姿
- 数据与评测：CMU、SFU 动捕和艺术家关键帧，四种仿真本体，多技能模仿、击打、投球和地形穿越；主要比较归一化回报、任务成功率与推力耐受值
- 主要结果与意义：Table 4 说明“做成任务”和“动作符合示范”应分别评价；RSI与ET使高动态技能更容易训练
- 项目关系与局限：是 BeyondMimic 跟踪控制背景；对本地操作平台提供方法参考，跨本体策略仍需重训，真机与视觉抓取未经本论文验证
- 摘要证据：已读作者官方18页全文与补充材料，重点复核 §5–7、§9–11、Table 2/4/5/6、Figure 8/11；表中数字按各自条件解释

## A. 基本研究问题

物理角色控制需要同时回答两个问题：当前动作是否好看、是否完成目标。若只跟踪一个参考片段，目标不在参考轨迹上时角色无法灵活适应；若只追任务回报，策略可能找到与预期技能无关的捷径。论文因此研究如何从短片段提取动作风格，又允许策略为击打位置、行进方向和地形变化调整动作（§1、§3）

这里的“模仿”不是行为克隆，即直接监督拟合示范状态到示范动作的映射。数据主要是姿态序列，没有人的控制力矩；策略通过物理仿真中的试错，寻找能够实现相似运动的关节控制。学习目标同时含动作相似度和任务回报，最终控制器按当前状态反馈修正，区别于开环播放动画

## B. 相关工作与阅读关系

论文将运动学合成、手工或模型驱动控制、深度强化学习、参考运动跟踪区分讨论。DeepLoco 已使用模仿奖励，但此前展示主要限于运动方向与步点控制，固定初态也妨碍高动态动作学习。SAMCON 能复现丰富技能，但算法结构较复杂；本工作的定位是用较统一的无模型学习框架覆盖高维本体、技能与目标，而非证明其在全部指标上击败所有模型控制方法（§2）

- [[03 论文卡片/06_扩散模型_流匹配_IL_RL/AMP - Adversarial Motion Priors for Stylized Physics-Based Character Control|AMP]] 在正文中直接讨论并比较 DeepMimic 式相位同步跟踪，适合对照“手工相似度奖励”和“学习得到的风格奖励”
- [[03 论文卡片/06_扩散模型_流匹配_IL_RL/BeyondMimic - From Motion Tracking to Versatile Humanoid Control via Guided Diffusion|BeyondMimic]] 是本库核心对读入口，比较参考运动跟踪与更灵活任务控制之间的关系；阅读关联本身不构成代码或模型直接继承的证据

## C. 方法：输入、控制与训练步骤

### 1. 准备本体与参考运动

角色建模为关节连接的刚体系统，参考片段由目标姿态序列构成。训练前人工处理片段并重定向到对应本体；人形和Atlas有不同质量、驱动力与限制。Table 1 的 Humanoid 为34自由度、197维状态、36维动作，Dragon为79自由度、418维状态、94维动作；动作参数数目受旋转编码影响，不等于可驱动关节自由度

### 2. 构造策略输入和输出

状态记录各身体段相对骨盆的位置、四元数姿态、线速度和角速度，使用角色局部坐标系，并加相位 φ∈[0,1]标记参考动作进度。带任务时追加目标；地形任务还输入高度图。策略每秒查询30次，输出各关节 PD（比例微分控制，用位置误差与速度误差生成驱动力矩）的目标姿态，球关节使用轴角编码、转动关节使用单角度（§5.1）

策略和价值函数分别采用两层全连接网络，隐藏层1024、512单元，策略输出高斯分布的均值、协方差固定。地形版本用卷积网络处理高度图后与身体和目标特征拼接。本文的“视觉”地形信息是模拟器提供的高度场，未建立从D435i深度图到该输入的完整估计管线（§5.2、§9）

### 3. 设计两层奖励

总奖励为 r=ωI·rI+ωG·rG。模仿项 rI 又分为关节姿态、关节速度、手脚末端位置和质心位置四项，权重分别0.65、0.10、0.15、0.10；各项对参考误差做指数衰减。附加任务实验使用ωI=0.7、ωG=0.3（§5.3、§10）

任务项依目标改变：朝指定方向走、让指定肢体接近并击中目标、让球命中目标，或通过障碍向前走。投球场景起始时球通过球关节连在手上，到固定时刻释放，不包含手指抓住球或学习释放时机，因此不能直接解释为灵巧抓取或抓抛一体策略（§9）

### 4. 用回合结构帮助探索

RSI（参考状态初始化）从参考片段均匀抽取姿态与速度作为起点，使策略在还不会起跳时也能练习翻转后半段与落地。ET（提前终止）在头、躯干等不允许的接触发生后终止并停止后续奖励，减少“倒地挣扎”样本和取巧解。具体接触规则必须配合技能定义，不能将所有接触一律作为失败（§6）

PPO（近端策略优化）根据仿真采样更新策略，价值函数预测后续回报，GAE估计当前动作的优势。补充材料D设置每次更新4096样本、小批256、γ=0.95、λ=0.95、PPO裁剪0.2。典型单技能约6000万样本，在8核CPU上约2天；这是原论文环境下的训练成本，不能当作当前机器速度（补充材料D）

### 5. 扩展到多个技能

多片段奖励取各片段模仿分的最大值；技能选择器额外接收one-hot（独热）片段ID，并训练技能之间的转换；组合策略则分别训练技能，再依据各价值函数通过Boltzmann分布选下一项。三者是不同方案，不能混写成一个通用的动作库规划器。差异过大的片段会使最大值方案只覆盖少数技能，作者因此建议更分散技能使用组合策略（§7、§10.2）

## D. 实验、基线与消融

### 1. 实验范围与指标

所有实验在Bullet内完成，物理频率1.2kHz、策略30Hz。Humanoid、Atlas、T-Rex、Dragon都是仿真角色，Atlas模型还将部分串联单自由度关节合并成球关节以便重定向。它不是未经改造的实体Atlas，也没有本地机械臂、DH116或D435i实验（§8、§10.3）

Table 2 的 NR 是每种策略32回合平均回报，按理论最小与最大值归一化，循环技能上限20秒，非循环技能按片段周期评价。Humanoid Walk为0.985、Backflip为0.729、Frontflip为0.485，对应训练样本6100万、7200万、8100万。不同技能难度与回报不同，不宜将NR跨技能解释成统一成功概率

### 2. 模仿与任务目标互补，但并非任务分总会升高

Table 4 每配置100次评估，使用相同任务定义比较三种奖励

| 仿真任务 | 模仿+任务 | 仅模仿 | 仅任务 |
|---|---:|---:|---:|
| 旋踢击中目标 | 99% | 19% | 55% |
| Baseball Pitch投球目标 | 75% | 5% | 93% |

投球仅任务策略会持球跑向目标，Figure 8直接展示这种捷径。因而75%相对93%的下降并不否定风格约束的作用，而是揭示只看命中指标无法保证“以投球方式完成”。作者并未提供机械臂抓取成功率，本卡也不将其借用为操作基准

### 3. RSI、ET与不同评估协议

Table 5 的后空翻 NR：RSI+ET为0.791、仅ET为0.730、仅RSI为0.379；步行为0.980、0.981、0.974。Figure 11表明ET对动态技能更关键；缺少RSI的后空翻可能只学到后跳，尽管回报接近完整方法。说明必须观察是否完成完整旋转，不能只看单个标量

这一组在评估时使用固定初态并关闭ET，而Table 2评估使用RSI和ET，所以0.791与0.729不是同一协议下的矛盾。多数技能只训练一个种子，补充Figure 12仅为后空翻和跑步额外报告3次训练，统计稳定性证据有限（§10.4、补充材料）

### 4. 迁移与抗扰动边界

重新训练的Atlas Run和Backflip回报为0.846和0.630，直接把Humanoid策略用于Atlas则仅0.013和0.014，说明迁移的是参考运动与训练流程，跨本体网络权重并非即插即用（§10.3）

Table 6向Humanoid骨盆施加持续0.2秒的推力，逐次增加10N到跌倒，Run最大前向720N、侧向300N；这是指定相位和方向的阈值实验，不是任意时刻、持续冲击或真实机器人安全保证。作者称与SAMCON文献报告相当或更好，未提供统一训练预算下重跑SAMCON的完整对照（§10.5）

## E. 局限、剩余问题与本项目启发

### 作者明确指出的局限

相位线性推进限制动作时序调整；多片段方法仅展示较小动作集合，尚未证明能扩展至大型库；各本体PD增益仍需人工设定；每个技能单独训练且耗时数天；模仿奖励依赖手工状态相似度与权重。真实机器人部署被列为未来方向，不能用论文中的Atlas渲染画面替代真机证据（§11）

### 本库分析与可检验的研究问题

参考状态随机初始化为仿真提供了训练捷径，但真实机器人不能任意瞬移到翻转中途；从仿真迁移时，初态分布与重置成本应独立核查。Task Return与动作质量应分开报告，必要时加完整技能判定、接触正确性和能耗；这些是本库提出的评测建议

对“机械臂+DH116+D435i”，可借鉴的是将任务完成与动作先验拆成奖励，以及在仿真中覆盖关键接触阶段。落地实施需要重新定义机械臂状态、手部动作、接触与对象位姿，标定D435i到机器人坐标系，并提供适合夹爪或灵巧手的示范。可以先对比“仅任务、仅模仿、混合奖励”在同一抓取任务上的成功率与动作稳定性；这是研究设想，尚无本论文的本设备结果

## 来源与开源边界

- [作者官方PDF](https://xbpeng.github.io/projects/DeepMimic/DeepMimic_2018.pdf)：全文18页及补充材料，实验与局限依据，已核对关键表图
- [arXiv版本历史](https://arxiv.org/abs/1804.02717)：首次提交与最新版本；最新arXiv版本号不等于已证明作者托管PDF与其逐字一致
- [作者项目页](https://xbpeng.github.io/projects/DeepMimic/index.html)与[正式DOI](https://doi.org/10.1145/3197517.3201311)：题名、作者、venue与出版信息
- [官方仓库README](https://github.com/xbpeng/DeepMimic)同时列出DeepMimic与AMP，现已提示旧代码弃用并链接MimicKit；本卡按原论文解释方法，不将后续框架速度写回2018实验
- [代码MIT许可](https://github.com/xbpeng/DeepMimic/blob/master/LICENSE)与论文版权分开；作者PDF首页保留ACM出版许可和个人／课堂复制条款，arXiv为非独占分发许可。动捕数据各自权利未穷尽核查，PDF只作本地阅读保存，不纳入Git发布

## 研究关联入口

[[01 论文文库/专题阅读/全身运动技能与具身执行框架|全身运动技能与具身执行框架]] · [[01 论文文库/论文编号索引|稳定编号索引]]
