---
paper_id: "P218"
title: "Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning"
aliases: ["Bunny-VisionPro", "面向模仿学习的实时双臂灵巧遥操作"]
authors: ["Ding, Runyu", "Qin, Yuzhe", "Zhu, Jiyue", "Jia, Chengzhe", "Yang, Shiqi", "Yang, Ruihan", "Qi, Xiaojuan", "Wang, Xiaolong"]
year: 2024
venue: "IROS 2025"
arxiv: "2407.03162"
version: "v1"
pdf: "01 论文文库/PDFs/08_数据与遥操作/Bunny.pdf"
document_type: "research_paper"
preprint_platform: "arXiv"
first_public_date: "2024-07-03"
first_public_month: "2024-07"
first_public_scope: "arXiv v1 UTC submission; cross-platform earliest release not established"
publication_status: "IROS 2025"
affiliations: ["The University of Hong Kong", "University of California San Diego"]
metadata_verified_on: "2026-10-25"
metadata_sources: ["https://arxiv.org/abs/2407.03162", "https://dingry.github.io/projects/bunny_visionpro.html", "https://arxiv.org/pdf/2407.03162v1"]
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Human_Demonstration", "Retargeting"]
doi: "10.1109/IROS60139.2025.11247017"
---

# Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning

## 基本信息

- 稳定编号：P218
- 中文译名：面向模仿学习的实时双臂灵巧遥操作
- 作者：Ding, Runyu；Qin, Yuzhe；Zhu, Jiyue；Jia, Chengzhe；Yang, Shiqi；Yang, Ruihan；Qi, Xiaojuan；Wang, Xiaolong
- 研究机构：The University of Hong Kong；University of California San Diego
- 年份：2024
- 首次公开：arXiv v1，2024-07-03（UTC；仅限定该平台，不声称全平台最早）
- 出处与版本：IROS 2025；所读 v1，18 页
- 研究主题：双臂遥操作、运动学约束与振动反馈
- 引用量：待核验
- 引用量来源：Google Scholar
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/Bunny.pdf|打开本地 PDF]]（已核对文件身份；仅本地保留，不承诺 GitHub 网页可访问）
- [官方论文页](https://arxiv.org/abs/2407.03162)｜[官方 PDF](https://arxiv.org/pdf/2407.03162v1)｜[官方项目](https://dingry.github.io/projects/bunny_visionpro.html)
- DOI：[ 10.1109/IROS60139.2025.11247017 ](https://doi.org/10.1109/IROS60139.2025.11247017)
- 官方代码：[对应 GitHub 仓库](https://github.com/Dingry/BunnyVisionPro)
- 数据：未核实独立完整数据集入口；代码中的示例和项目展示不等于完整数据发布

## 论文简介

双臂灵巧遥操作不是把人的手腕位置直接发给机器人就能完成的工作。两条机械臂可能互相碰撞，手腕进入奇异姿态时关节速度会突然增大，而人手与机器人手的关节结构也不一样。Bunny-VisionPro 把这些问题放在一条实时控制链路里处理：Apple Vision Pro 追踪人的双手，手部优化器将手指动作转换为机器人可驱动关节，机械臂优化器同时考虑跟随、碰撞和奇异位形，机器人指尖的压力再转换成人手指套上的振动反馈。这里的振动表示接触强弱，不是能阻止人手运动的双向力反馈

这篇工作的价值在于将“容易采集”与“采到的数据是否适合训练”一起评价。作者不仅让人遥操作完成任务，还用所采示范训练 ACT、Diffusion Policy 和 DP3，检查机器人自主执行、位置变化和新物体条件下的表现。控制更平顺、双臂配合更自然的数据，确实可以改善后续学习，但收益依赖具体任务和策略，触觉作为策略输入也没有始终带来提升。尤其需要注意，主要遥操作与学习数据是在振动反馈系统完成前采集的，因此不能将所有性能提升归因于触觉反馈

对我们的参考点主要是可执行动作、安全约束和数据质量的关系。现有机械臂与 DH116 可以借鉴关节耦合建模和限速思路，但论文验证的是 xArm-7 与 Ability Hand，不是 DH116。论文中的长程整任务成功率还存在正文与表格不一致，阅读时应优先看每个任务的试次数和成功次数，不能只引用摘要式平均值

## A. 基本信息与研究问题

研究问题是如何稳定地采集双臂、多指手的高质量示范。单独准确追踪人手不够，机器人还必须满足自身关节限制和运动学关系。作者希望在普通计算机上维持实时优化，并减少突然跳变、机械臂碰撞和操作困难

输入是头显估计的双手关键点与手腕姿态，输出为双臂与灵巧手关节命令。实验平台是两台七自由度 xArm-7，每台配六自由度 Ability Hand，共二十四个可驱动自由度；每只手五个指尖分布三十个触觉传感器。观察数据来自前方和上方的两台 RealSense L515。自由度指能够独立控制的运动变量，并不等于图像中检测出的关键点数量

## B. 相关工作

视觉遥操作通常先检测人手关键点，再通过优化让机器人手的指尖或指骨向量尽量接近人的几何关系。AnyTeleop 属于这种思路，它降低了对专用手套的依赖，但仍要解决不同机械臂姿态之间的约束协调。主从臂则直接读取与机器人相似机构的关节角，标签直观，却需要额外机械设备，也不自然提供多指手反馈

ACT 将未来一段动作作为动作块预测，减少单步预测累计误差；Diffusion Policy 通过逐步去噪生成动作序列；DP3 进一步使用三维点云表达场景。这些都是从示范训练策略的方法，不是遥操作设备的替代品。本文保持这些学习器不变来比较不同采集系统的数据，才能讨论示范质量的影响

与仅提供视觉反馈的系统相比，本文增加振动指套；与只处理手腕逆运动学的系统相比，本文将碰撞、奇异位形和跟随误差联合优化。这些模块分别改善可操作性和执行约束，不能把传感器、优化器与学习器混为一个端到端模型

## C. 核心贡献与方法

流程是：双手追踪 → 手腕坐标对齐与手指重定向 → 双臂约束优化 → 机器人执行 → 记录图像、关节和触觉 → 训练模仿策略

第一步，手部重定向以机器人正向运动学为基础。正向运动学是从关节角计算指尖位置。人手与机器人手长度不同，因此匹配的是经过处理的指骨关系，而不是要求所有关节角相等。Ability Hand 的闭环连杆让部分关节只能随主动关节联动，本文把被动关节写成主动关节的函数，在前向计算中求出被动角，在反向求导时将其梯度贡献传回主动变量。这避免把不可独立控制的关节当作自由变量，减少优化维数

第二步，机械臂目标由跟随、奇异性和碰撞三项组成。跟随项惩罚末端与人腕的位置、旋转误差；奇异性项在最小奇异值过低时启用，用可操作度惩罚即将失去运动能力的姿态；碰撞项用球体近似机器人连杆，跳过同连杆及直接相邻连杆的无意义检查。球体距离计算快且便于求导，但约束优化不等于对任意障碍物给出形式化安全保证

第三步，FSR 压力电阻容易出现零点漂移。系统预先在不同关节位置记录基线，运行时插值扣除基线，再低通滤波，用 PWM 调制偏心转子马达的振动。指套告诉操作者“接触增强了”，不能反馈完整六维接触力，也不能凭它测出摩擦系数

第四步，示范按任务收集并分别训练 ACT、DP 和 DP3。触觉学习实验将压力或其时间差分作为向量或点集输入。这里论文使用 impulse 一词，但不能据此把差分信号直接解释为经过完整物理标定的冲量测量

## D. 实验与结果

Table 1 在 i7-12700KF 上报告：闭环关节作为约束求解需要 34.98 ms，使用主动变量化为 3.43 ms，约十点二倍加速；同时考虑碰撞和奇异性的机械臂优化为 15.93 ms。它们是模块计算耗时，不是整个头显网络链路的端到端延迟

Table 2 每项十次遥操作，双杯堆叠本文 9/10、AnyTeleop 7/10；剪刀抓取本文 7/10，低于 AnyTeleop 的 8/10。后者说明 Ability Hand 的结构限制不会因优化自动消失。该表的旧方法数值来自原论文，并非全部在同一硬件上重新实验

Table 3 的 Clean Pan 为收集五十条成功示范，本文尝试五十八次、AnyTeleop+ 尝试七十八次，耗时分别 30.4 与 74.6 分钟。这里五十是成功轨迹数，不能说两者都做了五十次测试。振动反馈用户研究另有五名未训练操作者，每人每任务五次，与上述主要数据采集分开

Table 4 每条件十次自主执行，Uncover & Pour 的 ACT 用本文数据时 8/10，对照 2/10；相同任务 DP3 为 7/10 对 5/10。SR-SG 测物体位置变化，SR-U 测未见物体，不能与原分布成功率平均后声称统一泛化率

Table 5 的 DP3 长程整任务为擦玻璃 7/10、扫地 4/10、准备咖啡 4/10，三项简单平均为 50%；正文 §5.1 却写整任务 38%。当前所读 arXiv v1 表文不一致，本卡保留逐任务结果，不把 38% 当已消除歧义的结论。Table 6 加触觉并非总有益，例如清锅视觉基线 8/10，压力向量 7/10。训练成本、所有采集者总人数和完整链路延迟没有统一报告

## E. 不足与未来

作者指出，头显在手指自遮挡时追踪不准，可能产生抖动；轻触时振动反馈也不够敏感，未来可考虑更敏感的执行器。这是作者明确提出的限制

本库分析：低成本指套不代表整个双臂系统便宜，真实设备成本仍包括头显、机械臂、灵巧手和相机。碰撞球近似需要与真实外形核对，接触任务中还需要速度、力与急停边界。论文展示受扰泛化和操作反馈，没有建立独立的失败检测、任务重规划和自主恢复闭环

对 DH116 的具体设想是先核实驱动关节、被动耦合与正向运动学，再比较指尖位置损失和指骨向量损失；对 D435i 可复用三维观察，但不能认为换成另一深度相机后遮挡和精度保持不变。建议用普通夹爪先建立采集成功率、轨迹跳变、关节速度和策略成功率四项基线，再逐步加入多指映射。以上是我们提出的实验路线，不是论文已经验证的 DH116 结果

## 相关工作与阅读入口

- [[03 论文卡片/08_数据与遥操作/AirExo - Low-Cost Exoskeletons for Learning Whole-Arm Manipulation in the Wild|P219 · AirExo: Low-Cost Exoskeletons for Learning Whole-Arm Manipulation in the Wild]]
- [[03 论文卡片/08_数据与遥操作/Open-TeleVision - Teleoperation with Immersive Active Visual Feedback|P194 · Open-TeleVision: Teleoperation with Immersive Active Visual Feedback]]
- [[03 论文卡片/08_数据与遥操作/DexCap - Scalable and Portable Mocap Data Collection System for Dexterous Manipulation|P009 · DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation]]

- 所属方向与专题导读：[[02 研究方向/数据与遥操作]]
- 遥操作路线：[[02 研究方向/机器人遥操作与动作重定向]]
- 数据质量路线：[[02 研究方向/机器人数据采集与数据质量]]

## 来源与核验边界

- 已阅读上述 18 页版本的正文、方法、实验与局限，含附录时一并核对；关键架构或实验表经页面渲染检查，数字位置见各节
- 日期依据官方 arXiv 提交历史，机构依据所读版本署名；正式出处与所读预印本版本分别标明，不用会议日程或演示获奖冒充正式出版
- 论文结果、作者限制和本库研究设想分开；未报告字段不补猜，未核实引用量不填 0
- 代码和数据链接用于核对公开资源，未运行第三方代码、未执行机器人动作；可访问与可完整复现分别评价
- PDF 再分发许可未统一确认，遵循现有忽略规则仅保存本地；代码许可不自动覆盖论文、数据及模型
