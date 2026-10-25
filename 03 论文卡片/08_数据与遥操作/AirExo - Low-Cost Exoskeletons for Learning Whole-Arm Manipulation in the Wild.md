---
paper_id: "P219"
title: "AirExo: Low-Cost Exoskeletons for Learning Whole-Arm Manipulation in the Wild"
aliases: ["AirExo", "用于野外全臂操作学习的低成本外骨骼"]
authors: ["Fang, Hongjie", "Fang, Hao-Shu", "Wang, Yiming", "Ren, Jieji", "Chen, Jingjing", "Zhang, Ruo", "Wang, Weiming", "Lu, Cewu"]
year: 2023
venue: "ICRA 2024"
arxiv: "2309.14975"
version: "v2"
pdf: "01 论文文库/PDFs/08_数据与遥操作/AirExo.pdf"
document_type: "research_paper"
preprint_platform: "arXiv"
first_public_date: "2023-09-26"
first_public_month: "2023-09"
first_public_scope: "arXiv v1 UTC submission; cross-platform earliest release not established"
publication_status: "ICRA 2024"
affiliations: ["Shanghai Jiao Tong University", "Shanghai Artificial Intelligence Laboratory"]
metadata_verified_on: "2026-10-25"
metadata_sources: ["https://arxiv.org/abs/2309.14975", "https://airexo.github.io/", "https://arxiv.org/pdf/2309.14975v2"]
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Human_Demonstration", "Retargeting"]
doi: "10.1109/ICRA57147.2024.10610799"
---

# AirExo: Low-Cost Exoskeletons for Learning Whole-Arm Manipulation in the Wild

## 基本信息

- 稳定编号：P219
- 中文译名：用于野外全臂操作学习的低成本外骨骼
- 作者：Fang, Hongjie；Fang, Hao-Shu；Wang, Yiming；Ren, Jieji；Chen, Jingjing；Zhang, Ruo；Wang, Weiming；Lu, Cewu
- 研究机构：Shanghai Jiao Tong University；Shanghai Artificial Intelligence Laboratory
- 年份：2023
- 首次公开：arXiv v1，2023-09-26（UTC；仅限定该平台，不声称全平台最早）
- 出处与版本：ICRA 2024；所读 v2，12 页
- 研究主题：同构外骨骼、双臂全臂示范、预训练与微调
- 引用量：待核验
- 引用量来源：Google Scholar
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/AirExo.pdf|打开本地 PDF]]（已核对文件身份；仅本地保留，不承诺 GitHub 网页可访问）
- [官方论文页](https://arxiv.org/abs/2309.14975)｜[官方 PDF](https://arxiv.org/pdf/2309.14975v2)｜[官方项目](https://airexo.github.io/)
- DOI：[ 10.1109/ICRA57147.2024.10610799 ](https://doi.org/10.1109/ICRA57147.2024.10610799)
- 官方代码：[对应 GitHub 仓库](https://github.com/AirExo/collector)
- 数据：[官方数据入口](https://drive.google.com/drive/folders/1f_bmrFPep90aUSBj28TdXRiNvHo7PpxR)（下载内容、许可与访问权限以页面说明为准）

## 论文简介

机器人不仅能用夹爪，还可能用前臂挡住物体、把一堆球拢到中间，或者用一条手臂撑开帘子，让另一条手臂伸进去抓取。对于这些全臂操作，只告诉机器人末端去哪里通常不够，因为不同肘部姿态会与环境产生完全不同的接触。AirExo 因而选择记录与机器人机构对应的关节角，而不是只追踪人手位置。它是一套可穿戴、以三维打印零件为主的双臂外骨骼，每个编码器关节对应机器人关节，末端机构还记录夹爪开合

它有两种用途：一是在机器人旁边直接遥操作，得到真正执行过的示范；二是在没有机器人的地方穿戴外骨骼演示，得到便宜、可扩展的关节动作和观察。第二类数据虽然不占用机器人，但画面中出现的是人和外骨骼，不能与机器人数据当作完全同分布。论文采取先用野外数据预训练、再用少量遥操作数据微调的方式，让策略先学会动作的大致结构，再适应真实机器人画面与执行差异

实验重点不是证明所有任务都能不依赖机器人数据，而是证明少量机器人示范可以被便宜的人类示范补充。Gather Balls 和隔帘抓取都使用双臂配合，且明确区分任务完成比例、阈值成功率与碰撞率。对我们而言，这篇论文适合用来理解为什么关节级标签对全臂操作重要，也提醒我们：外骨骼成本、机器人总成本和数据采集总成本是三个不同概念。DH116 的手指映射不在该平台验证范围内

## A. 基本信息与研究问题

研究背景是末端控制忽略了机器人手臂形状，而纯遥操作采集又受机器数量、场地和操作时间限制。作者提出价格约六百美元的双臂外骨骼，目标包括便宜、可适配、便携、耐用和易维护。这个价格是外骨骼材料与编码器成本，不包括两台机械臂、相机或工作站

实验使用两台 Flexiv Rizon 和 Robotiq 2F-85 夹爪。每条外骨骼有七个手臂关节和一个末端开合自由度，与机器人关节结构对应。UR5、Franka、Kuka 的模型说明可通过改连杆适配，不能据此说论文在所有平台上都完成了同规模学习实验

## B. 相关工作

主从机械臂利用结构对应关系读取关节角，控制清晰，但专用主臂不易带到真实环境。视觉追踪手腕或手套捕捉人手可以减少机械设备，却需要求逆运动学；当末端位置相同、肘部姿态不同，单纯末端目标不能描述全臂接触

VINN 将图像映射到视觉特征空间，再查找示范中的邻近状态并使用其动作，数据少时容易受覆盖范围限制。ACT 则学习未来动作块，能表达多关节协调，但只用少量真实示范时仍可能对一侧手臂学得更好。AirExo 的主要变化是提供额外的同构动作来源，让 ACT 先接触更广泛的协调过程，再用机器人数据纠正观察域差异

这也解释了与 AirExo-2 的关系：本作通过微调跨越外骨骼与机器人的视觉差异，后续工作再尝试主动改造图像与深度，让野外示范更接近机器人观察。不能把后作零机器人示范的设定倒写成本作结论

## C. 核心贡献与方法

完整流程：穿戴并校准同构外骨骼 → 编码器读取关节角和夹爪开合 → 同步采集相机图像 → 野外示范预训练 → 少量机器人遥操作微调 → 机器人闭环执行

机械设计将关节分成固定在前一连杆的 pre-joint 和连接后一连杆的 post-joint，通过阻尼转轴连接，编码器不直接承受主要弯矩。限位盘和钢球限制活动范围，降低误操作损坏概率。外骨骼按机器人约八成尺寸制作，安装在背心底座上，以减轻上肢负担；缩小几何尺寸仍保留关节对应，不代表末端绝对坐标可以直接按一比一使用

校准时让机器人和外骨骼处于对应姿态，记录机器人角 q_c 和编码器值 p_c。运行时用 q=q_c+k(p-p_c) 再裁剪到机器人关节上下限，k 表示方向和比例。这里主要是几何对应与编码器偏置校准，没有训练一个复杂的人体姿态到机器人动作网络。夹爪将编码器角度范围映射为开口范围

野外采集时机器人不在场，但操作者仍穿戴同构机构，记录的不是任意互联网视频。先用这些数据训练策略，可以学习双臂在不同阶段的协调；再用机器人实际执行数据微调，使视觉编码和动作预测适应部署时的画面。文中分析发现，纯机器人少样本训练可能偏重左臂，补充野外数据后双侧更均衡，这是特定任务的观察，不是普遍因果定理

关节限幅仅排除角度越界，不能独立保证与桌面、另一手臂或物体无碰撞。采集数据还需要相机与关节的时间对齐、准确的初始校准，以及操作者不超出真实机器工作空间

## D. 实验与结果

Gather Balls 评价将球拢进中心三角区域。完成率是区域内球的比例，在线上的球按半个计算；成功率还要指定完成率阈值，论文比较 40%、60%、80% 三种阈值。每种方法五十次测试、每次六十秒，控制约五赫兹。因此“完成率 75%”和“成功率 75%”是不同指标，不能互换

隔帘抓取分为伸入、撑开帘子、接近、抓取和丢入桶五阶段，每种方法二十五次、每次一百二十秒。Table II 比较五十条遥操作、十条遥操作，以及十条遥操作加野外数据的设置。论文指出约三分钟的十条遥操作结合野外数据，可以超过仅用超过二十分钟的五十条遥操作训练的部分结果。这不等于总采集时间只有三分钟，因为还需要野外示范

Table III 的鲁棒性测试每项八次，例如视觉干扰条件原策略 4/8，结合野外学习为 8/8。它们是固定小样本扰动实验，不是覆盖任意新环境的保证。论文同时比较 VINN、ConvMLP、BeT 和 ACT，Table I 的碰撞率提醒我们：任务进度高也可能伴随不安全接触

外骨骼采用十六个约三十美元的编码器，其他打印、机械和线材约一百二十美元，合计约六百美元。编码器标称分辨率 0.08° 是传感器分辨能力，不能视为整机末端定位误差。论文没有给出统一的全任务采集者人数、全年运行可靠性或与 DH116 集成耗时，不能自行补齐

## E. 不足与未来

作者明确把野外画面与机器人画面的差异列为后续方向，希望进一步减少机器人微调数据。本文没有证明完全靠野外数据即可在所有真实任务上部署

本库分析：关节同构是优势也是限制。换机器人时需要重新设计尺寸、关节对应、限位和校准，便携不等于任意人体动作都可执行。外骨骼可记录手臂动作，但普通夹爪的单自由度开合不能提供多指接触和独立指关节标签。碰撞统计也说明采集流程需要明确安全边界

对我们的启发是先比较末端位姿数据与完整关节数据在撑物、挡物等任务上的差别。如果只有普通夹爪，可先复制双阶段预训练加少量真机微调的思想；若加入 DH116，需要单独解决手指运动学与接触标签。D435i 可作为观察设备，但其标定、深度空洞和时间同步需要独立检查。实际部署失败恢复未形成专门系统，受扰后的表现不能替代明确的失败检测、回退与重试机制

## 相关工作与阅读入口

- [[03 论文卡片/08_数据与遥操作/AirExo-2 - Scaling up Generalizable Robotic Imitation Learning with Low-Cost Exoskeletons|P220 · AirExo-2: Scaling up Generalizable Robotic Imitation Learning with Low-Cost Exoskeletons]]
- [[03 论文卡片/08_数据与遥操作/GELLO - A General, Low-Cost, and Intuitive Teleoperation Framework for Robot Manipulators|P192 · GELLO: A General, Low-Cost, and Intuitive Teleoperation Framework for Robot Manipulators]]
- [[03 论文卡片/08_数据与遥操作/Universal Manipulation Interface - In-The-Wild Robot Teaching Without In-The-Wild Robots|P193 · Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots]]

- 所属方向：[[02 研究方向/数据与遥操作]]
- 专题导读：[[02 研究方向/数据与遥操作_从采集到可执行示范]]
- 遥操作路线：[[02 研究方向/机器人遥操作与动作重定向]]
- 数据质量路线：[[02 研究方向/机器人数据采集与数据质量]]

## 来源与核验边界

- 已阅读上述 12 页版本的正文、方法、实验与局限，含附录时一并核对；关键架构或实验表经页面渲染检查，数字位置见各节
- 日期依据官方 arXiv 提交历史，机构依据所读版本署名；正式出处与所读预印本版本分别标明，不用会议日程或演示获奖冒充正式出版
- 论文结果、作者限制和本库研究设想分开；未报告字段不补猜，未核实引用量不填 0
- 代码和数据链接用于核对公开资源，未运行第三方代码、未执行机器人动作；可访问与可完整复现分别评价
- PDF 再分发许可未统一确认，遵循现有忽略规则仅保存本地；代码许可不自动覆盖论文、数据及模型
