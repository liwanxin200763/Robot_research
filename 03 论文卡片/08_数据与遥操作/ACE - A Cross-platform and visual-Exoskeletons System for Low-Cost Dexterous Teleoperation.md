---
paper_id: P195
title: "ACE: A Cross-platform and visual-Exoskeletons System for Low-Cost Dexterous Teleoperation"
authors: ["Yang, Shiqi", "Liu, Minghuan", "Qin, Yuzhe", "Ding, Runyu", "Li, Jialong", "Cheng, Xuxin", "Yang, Ruihan", "Yi, Sha", "Wang, Xiaolong"]
year: 2025
venue: "CoRL 2024; PMLR 270 (published 2025)"
arxiv: "2408.11805"
version: "v1"
arxiv_version: "v1"
pdf: "01 论文文库/PDFs/08_数据与遥操作/ACE.pdf"
verified_on: "2026-10-15"
citation_status: "待 Google Scholar 人工核验"
tags: ["Teleoperation", "Data_Collection", "Retargeting", "Imitation_Learning"]
document_type: "会议论文"
preprint_platform: "arXiv"
first_public_date: "2024-08-21"
first_public_month: "2024-08"
first_public_scope: "arXiv v1 submission history (UTC)"
latest_preprint_date: "2024-08-21"
latest_preprint_version: "v1"
publication_status: "已正式发表"
published_venue: "CoRL 2024；PMLR 270:4895–4911 (2025)"
affiliations: ["University of California San Diego"]
metadata_verified_on: "2026-10-17"
metadata_sources: ["https://arxiv.org/abs/2408.11805", "https://raw.githubusercontent.com/mlresearch/v270/main/assets/yang25d/yang25d.pdf", "https://proceedings.mlr.press/v270/yang25d.html", "https://ace-teleop.github.io/"]
publication_year: 2025
conference_month: "2024-11"
---

# ACE: A Cross-platform and visual-Exoskeletons System for Low-Cost Dexterous Teleoperation

## 出处与版本

- 文献类型：会议论文
- 预印本平台与编号：[arXiv 2408.11805](https://arxiv.org/abs/2408.11805)
- 首次公开日期：2024-08-21；首次公开月份：2024 年 8 月，依据 arXiv v1 提交历史（UTC）；本字段不宣称已穷尽项目网页或其他平台可能更早的公开记录
- 最近预印本版本：v1，日期 2024-08-21；当前未记录后续修订
- 当前发表状态：已正式发表
- 正式发表出处：[CoRL 2024；PMLR 270:4895–4911 (2025)](https://proceedings.mlr.press/v270/yang25d.html)
- 正式出版年份：2025；正式出版月份：待核验
- 会议月份：2024 年 11 月；不是录用通知日期
- 日期与状态说明：CoRL 2024 会议与 PMLR 2025 出版分开记录；正式出版月份待核验。预印本与正式版标题大小写和措辞略有差异，继续使用现有正式标题和稳定编号
- 作者所属机构：University of California San Diego
- 机构依据：正式版首页九位作者统一署名 UC San Diego；不由机器人品牌或合作视频推断其他作者单位；[对应版本 PDF 首页](https://raw.githubusercontent.com/mlresearch/v270/main/assets/yang25d/yang25d.pdf)
- 项目主页：[作者项目页](https://ace-teleop.github.io/)
- 官方代码：[作者链接的仓库](https://github.com/ACETeleop/ACETeleop)；入口存在不等于已核实完整实现、模型或许可，开源边界沿用下文说明
- 信息核验日期：2026-10-17；来源为官方版本历史、正文署名和上述正式条目；引用量沿用原 Google Scholar 人工核验规则

## 论文简介

同一套遥操作设备若每换一种机器人都重做，数据采集很难扩展。ACE 用外骨骼记录手腕位置，用面向手的相机估计手指姿态，再把两部分分别映射到目标机器人，兼顾精度、便携性和换平台的成本

输入是外骨骼关节读数和手部图像，输出是机器人手臂目标与手指动作。流程为“机械结构推算手腕位姿 → 图像恢复手形 → 按目标手重定向 → 平滑及限幅 → 执行与记录”。重定向是把人的动作改写成目标手能够做到的动作，不是逐指角度照抄。相较单纯视觉追踪腕部，外骨骼减少手腕漂移；相较同构主从系统，它把末端适配与通用采集装置分开（§3）

论文展示六种平台，并在若干真机任务上训练模仿策略。表 2 的六人仿真到达实验中，小工作区小目标成功率 97.1%，但这是遥操作到达测试，不是自主接触任务成绩。表 3 的 xArm 倒糖任务最终自主成功率仅 40%，每设置评估十回合；跨平台展示不等于每个平台都经过同样充分验证

对 DH116，更可迁移的是腕部与手指解耦、可达范围约束和连续平滑。D435i 可以成为另一路观察源，但不能默认替代面向手的相机视角；多指耦合和标定仍需实测。把这些模块接到现有机械臂并比较示范质量，是我们的实现方向，尚不是论文已经在本设备上证明的能力

## A. 基本信息与研究问题

- 作者：Shiqi Yang、Minghuan Liu、Yuzhe Qin、Runyu Ding、Jialong Li、Xuxin Cheng、Ruihan Yang、Sha Yi、Xiaolong Wang
- 正式发表：CoRL 2024；PMLR 270，4895–4911，出版年2025；首发arXiv为2024，最新v1为2024-08-21
- [官方论文集页](https://proceedings.mlr.press/v270/yang25d.html)｜[arXiv 2408.11805](https://arxiv.org/abs/2408.11805)｜[项目页](https://ace-teleop.github.io/)
- 正式页标题为本卡标题；arXiv标题为“ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation”，同一论文，非两篇
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/ACE.pdf|查看 PDF]]，正式论文集PDF17页；[官方代码](https://github.com/ACETeleop/ACETeleop)公开，仓库许可Apache-2.0；引用量待 Google Scholar 人工核验

ACE把“腕在哪里”和“手指怎么弯”交给不同传感器：低成本外骨骼用编码器与正向运动学测腕，始终面向手掌的相机估手形，再重定向到不同机器人。它希望兼顾同构主端的稳定性和视觉方案的跨平台能力。跨平台是采集／映射系统可适配多种本体，不代表一个权重在所有平台直接执行（图2、§3）

## B. 相关工作

ALOHA和GELLO按同构关节复制，几何清楚但每种目标臂要配对应主端；比例缩小后，手端小移动可能变成大臂位移。纯视觉AnyTeleop容易受到腕部尺度、世界位置与遮挡误差影响；DexCap用更丰富跟踪器提高动作观测，但设备价格和链路复杂度不同。ACE固定相机相对手的位置，外骨骼独立给腕位姿，减少这两类误差相互干扰（§2）

由腕位姿求目标臂IK，让设备不必复制目标臂拓扑；手形仍需依赖目标手模型做几何优化。此路线在“同构复制”与“只靠视觉”之间提供工程折中，但把难点转移到工作空间映射、IK及多指重定向，不能把600美元设备等同完整机器人系统（p2，表1）

## C. 核心贡献与方法

### 1. 双底座、机械腕追踪与掌前相机

双臂外骨骼每侧6自由度、七连杆，DYNAMIXEL XL330-M288-T提供12-bit角读数，经U2D2读取；相机架可二轴调整，使低成本RGB相机朝向掌面。桌面底座稳定且可托肘，移动底座可背负。磁连接便于独立穿戴和调整腕圈／连杆长度，作者报告桌面穿戴小于30秒（p4–5，图3）

编码器角经FK算腕，MediaPipe从相机图像得到腕坐标中的21手关键点。相机跟随手腕降低全局遮挡，但手指相互遮挡及模型误差仍可能存在；外骨骼本身测不到指尖接触力，也没有从机器人向人体的主动触觉反馈。表1约0.6k美元是采集接口报价，未包含被控臂、灵巧手和训练算力

### 2. 工作空间与动作尺度分别映射

先让操作者移动手臂测人工作空间中心ch，再指定机器人任务中心ct和比例γ，位置按xe=γ(xh−ch)+ct映射。附录算法从三轴活动范围求中心与半径，再限制映射点留在机器人工作球内；旋转按各轴范围缩放。这里的中心／比例需显式采集和配置，不能称无需标定（式1、p14–15）

Normal Mode按工作区比例直映；Mirror Mode用于面对面控制大机器人；Bimanual Mode调整两侧中心与比例，让相机架将接近碰撞时机器人双手恰好接触。后者改变了人手与机器人距离关系，是处理设备几何冲突的取舍，不是让穿戴设备真的能自由交叉（p6）

### 3. 臂、夹爪与手采用不同求解器

映射腕目标后，IK转换为目标臂关节；平台仍需各自PID、滤波与奇异点／运动限制。夹爪模式把拇指—食指距离线性映到0–1；灵巧手模式最小化人和机器人关键点向量差，加相邻关节变化惩罚，并约束ql≤q≤qu。α补偿手尺寸，β控制时间平滑，不能把关键点等同各机器人关节的角度真值（p16，式2）

当前手姿追踪约27 Hz；论文说换高频相机可进一步到100 Hz，应区分实测系统与可改进目标。全文没有清楚给每平台完整端到端延迟分布，不用27 Hz倒算延迟。该系统主要依赖现场观察；没有把沉浸式双目远程回传作为核心模块（§3.2）

### 4. 从采集到两类模仿策略

xArm＋Ability Hand使用3D Diffusion Policy，输入两相机视角独立采样的点云和本体状态，输出腕与手目标；H1＋Inspire使用ACT，输入头顶RGB。采集动作、图像／点云和状态需对齐，但正文未充分交代各流时间戳及存储频率，复现应单独核仓库，而不补猜。不同平台训练不同策略，跨设备演示不构成策略零样本迁移（§4.2）

## D. 实验与结果

### 精度与模拟到达实验

作者报告外骨骼FK平均约1 mm，拉卷尺20→40 cm的臂端综合平均误差约3 mm，后者含遥操作及从臂控制误差；这些不是所有姿态、全部手指的定位保证（p7，图5）

六名操作者在仿真xArm中用双末端到达目标球，对比GELLO；测试四组工作空间与目标尺寸。小工作区／小目标下ACE 4.69秒、97.1%成功，GELLO13.6秒、47.6%；中工作区／小目标4.54秒、91.4%，对照6.52秒、73.8%（p8，表2）

不能复述成所有设置全面更好：中工作区／中目标时GELLO3.65秒、93.8%，ACE4.05秒、87.5%，有效路径比也为75%对67.1%，是GELLO占优。表2主张“多数场景”更合理；这些结果是仿真到达效率，不是接触丰富真机任务成功率（附录C）

### 模仿学习与示范质量

| 平台／任务 | 采集成功／尝试 | 最后阶段策略成功率 |
|---|---:|---:|
| xArm Vacuum Keyboard | 30/38 | 50% |
| xArm Serve Candies | 45/53 | 40% |
| xArm Wipe Whiteboard | 30/37 | 70% |
| xArm Grasp Dolls | 120/123 | 80% |
| H1 Put in Tennis | 25/29 | 90% |
| H1 Grasp Dolls | 62/66 | 90% |

每项策略只评估10个episode；采集成功率高不能替换训练后成功率。长程任务吸尘从抓取100%到最终放回50%，倒糖从抓取90%到最终丢筒40%，反映下游误差累积仍明显。正文说“六个任务”含同名Grasp Dolls的两个平台，宜写六个任务—平台设置（p14，表3）

抓娃娃训练9种小娃娃、2种大娃娃，测试15种小、3种大，并变化机器人位置，提供一定物体泛化证据；没有与相同训练协议下其他遥操作数据做充分对照。多平台操作视频是能力展示，不能替代每平台重复试验（图4、6）

## E. 不足与未来

**作者指出：**相机架阻碍双手靠拢，并因额外力臂增加腕部旋转负担；缩放控制虽缓解功能限制，部分操作仍不直观（§5）

**我的理解：**对DH116可先复用“腕追踪和手形分开、受限向量优化、时间平滑”的离线模块。其6主动轴、11总自由度需正确耦合，先评估拇指／食指／中指指尖误差与捏合范围；当前多轴与臂手运动未验收，不把论文兼容性当本项目控制通过。D435i可提供训练点云，但掌前相机的视角和遮挡条件需要重做评估

最小方案是离线关键点、工作空间标定和日志质量检查；完整硬件还需两侧编码器外骨骼、底座、掌前相机、目标臂与手及训练设备。优先比较桌面固定与外部视觉腕追踪误差，再判断是否值得制作背负式完整装置

## 来源与核验边界

- [官方PDF](https://raw.githubusercontent.com/mlresearch/v270/main/assets/yang25d/yang25d.pdf)；已逐段核对方法、实验、失败与局限，并渲染架构图及主结果表核对行列
- 以上论文数值来自对应PDF页码；当前官方仓库状态与论文实验设置分开，未运行其代码或任何机器人动作
- arXiv预印本登记许可（不混作正式PDF许可）：http://creativecommons.org/licenses/by-nc-nd/4.0/；仓库代码许可不自动覆盖PDF、数据和第三方依赖
- [正式发表来源](https://proceedings.mlr.press/v270/yang25d.html)、[项目页](https://ace-teleop.github.io/)与官方仓库已核验；引用量仍待人工核验
- 关联专题：[[01 论文文库/专题阅读/机器人遥操作与动作重定向]]；[[01 论文文库/专题阅读/机器人数据采集与数据质量]]
