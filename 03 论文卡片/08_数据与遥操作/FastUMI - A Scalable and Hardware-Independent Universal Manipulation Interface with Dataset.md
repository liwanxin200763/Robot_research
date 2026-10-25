---
paper_id: "P222"
title: "FastUMI: A Scalable and Hardware-Independent Universal Manipulation Interface with Dataset"
aliases: ["FastUMI", "可扩展、硬件解耦的通用操作接口与数据集"]
authors: ["Zhaxizhuoma", "Liu, Kehui", "Guan, Chuyue", "Jia, Zhongjie", "Wu, Ziniu", "Liu, Xin", "Wang, Tianyu", "Liang, Shuai", "Chen, Pengan", "Zhang, Pingrui", "Song, Haoming", "Qu, Delin", "Wang, Dong", "Wang, Zhigang", "Cao, Nieqing", "Ding, Yan", "Zhao, Bin", "Li, Xuelong"]
year: 2024
venue: "CoRL 2025"
arxiv: "2409.19499"
version: "CoRL 2025 final"
pdf: "01 论文文库/PDFs/08_数据与遥操作/FastUMI.pdf"
document_type: "research_paper"
preprint_platform: "arXiv"
first_public_date: "2024-09-29"
first_public_month: "2024-09"
first_public_scope: "arXiv v1 UTC submission; cross-platform earliest release not established"
publication_status: "CoRL 2025"
affiliations: ["Shanghai Jiao Tong University", "Shanghai AI Lab", "University of Bristol", "Fudan University", "The University of Hong Kong", "Northwestern Polytechnical University", "Xi'an Jiaotong-Liverpool University", "Suzhou OneStar Robotics Co., Ltd.", "Institute of AI, China Telecom Corp Ltd."]
metadata_verified_on: "2026-10-25"
metadata_sources: ["https://arxiv.org/abs/2409.19499", "https://proceedings.mlr.press/v305/zhaxizhuoma25a.html", "https://raw.githubusercontent.com/mlresearch/v305/main/assets/zhaxizhuoma25a/zhaxizhuoma25a.pdf"]
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Human_Demonstration", "Retargeting"]
---

# FastUMI: A Scalable and Hardware-Independent Universal Manipulation Interface with Dataset

## 基本信息

- 稳定编号：P222
- 中文译名：可扩展、硬件解耦的通用操作接口与数据集
- 作者：Zhaxizhuoma；Liu, Kehui；Guan, Chuyue；Jia, Zhongjie；Wu, Ziniu；Liu, Xin；Wang, Tianyu；Liang, Shuai；Chen, Pengan；Zhang, Pingrui；Song, Haoming；Qu, Delin；Wang, Dong；Wang, Zhigang；Cao, Nieqing；Ding, Yan；Zhao, Bin；Li, Xuelong
- 研究机构：Shanghai Jiao Tong University；Shanghai AI Lab；University of Bristol；Fudan University；The University of Hong Kong；Northwestern Polytechnical University；Xi'an Jiaotong-Liverpool University；Suzhou OneStar Robotics Co., Ltd.；Institute of AI, China Telecom Corp Ltd.
- 年份：2024
- 首次公开：arXiv v1，2024-09-29（UTC；仅限定该平台，不声称全平台最早）
- 出处与版本：CoRL 2025；所读 CoRL 2025 final，25 页
- 研究主题：手持采集、数据质量检查、跨平台动作表示
- 引用量：待核验
- 引用量来源：Google Scholar
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/FastUMI.pdf|打开本地 PDF]]（已核对文件身份；仅本地保留，不承诺 GitHub 网页可访问）
- [官方论文页](https://arxiv.org/abs/2409.19499)｜[官方 PDF](https://raw.githubusercontent.com/mlresearch/v305/main/assets/zhaxizhuoma25a/zhaxizhuoma25a.pdf)｜[官方项目](https://fastumi.com/)
- [正式发表来源](https://proceedings.mlr.press/v305/zhaxizhuoma25a.html)
- 官方代码：[对应 GitHub 仓库](https://github.com/zxzm-zak/FastUMI_Data)
- 数据：未核实独立完整数据集入口；代码中的示例和项目展示不等于完整数据发布

- 项目主页访问状态（2026-10-25）：官方 fastumi.com 的 HTTPS 证书已过期，当前无法正常验证；不绕过浏览器安全检查。上方正式论文 PDF 和对应 GitHub 可访问，项目展示页待站点修复

## 论文简介

FastUMI 沿着 UMI 的方向继续降低机器人示范采集门槛：人拿着与机器人末端相似的装置演示，相机观察与位姿追踪同步记录，再把这些数据转换为策略训练所需的动作。它重点处理硬件绑定和软件复杂度：原有接口可能依赖指定夹爪、相机和视觉惯性估计流程，换平台就要重新改机械与标定。FastUMI 采用模块化机械接口、独立位姿追踪和统一数据格式，尝试把“如何采集”与“最后用哪台机器人执行”解耦

解耦并非没有条件。手持轨迹必须位于机器人的可达范围，追踪相机到夹爪中心的偏置必须正确，夹爪开合时工具中心还可能移动。论文不仅保存位姿，还讨论绝对与相对 TCP、关节动作、时间同步和轨迹质量检查。它还针对所采数据调整 ACT 与 Diffusion Policy：前者加入时序平滑与位姿表达，后者使用估计深度改善精细操作。因此数据接口、动作表示和学习器适配共同决定最终效果，不能只把更换传感器当作全部贡献

本卡以 CoRL 2025 正式版为实验口径。该版报告超过一万五千条、二十四项任务，而 arXiv v2 的较早数据规模不同，不能混写为同一批数据。真实执行使用十二项任务，每任务训练二百条并测试十五次。对我们的价值是可直接借鉴同步、动作转换与质量筛查；但 D435i 不是 T265 的位姿追踪替代品，DH116 也不是更换夹爪宽度字段就能得到的兼容末端

## A. 基本信息与研究问题

研究目标是降低手持示范装置与特定机械臂、夹爪的耦合，保留一致观察视角，并提供能供不同学习算法消费的数据。正式版来源是 PMLR 305，页码 3069–3093。论文机构以本地正式版首页署名为准，完整机构映射尚需逐作者复核，不凭作者当前主页补写

系统使用 GoPro 采集视觉、T265 提供位姿追踪，ArUco 标记辅助夹爪宽度估计。机器人主要评测平台是 xArm 6，另讨论 Flexiv Rizon、Z1 与 Robotiq 相关适配。该支持范围不等于每种机构完成同数量任务和相同成功率

## B. 相关工作

UMI 通过手持夹爪和一致腕部观察，将人类示范变成机器人可用数据，但指定夹爪和视觉惯性里程计配置增加部署负担。视觉惯性里程计结合图像和惯性传感器估计相机运动，在遮挡与纹理不足时仍可能退化

FastUMI 使用现成追踪设备减轻离线估计和调参负担，并通过模块化部件保持手持与机器人安装时的观察一致。主从臂采到的是直接执行的关节动作，手持装置则先得到末端运动，需要额外转换与可达性检查。这正是它可以脱离机器人采集，却不能自动保证所有示范都可执行的原因

ACT 预测绝对关节动作时容易绑定机器人与起始姿态，DP 使用相对 TCP 可以弱化这种绑定但也可能丢失绝对高度信息。本文的算法变体不是跨平台泛化问题的普适解，而是在同一数据系统中比较动作表达与观察补充的影响

## C. 核心贡献与方法

流程：模块化手持装置演示 → GoPro、追踪与夹爪信息同步 → 置信度及平滑性筛查 → 末端坐标转换 → 关节或 TCP 数据集 → 训练相应策略 → 校准到目标机器人执行

物理解耦通过标准接口适应不同机器人和夹爪，视觉一致性要求采集与部署的相机视角尽量匹配。传感器各自运行，ROS 节点记录，存储节点把同步流写入 HDF5。统一文件格式方便训练，并不能代替时间戳检查；双传感器漂移和延迟需要单独处理

坐标转换使用 T265 位姿、相机到夹爪中心的固定偏置，以及机器人基座下已知的夹爪初始位姿。根据这些关系得到绝对或相对 TCP，再结合机器人描述文件求关节动作。ArUco 标记的像素距离映射为夹爪实际开口，非平行夹爪关闭时的中心偏移还需要动态补偿

Smooth-ACT 用循环结构等时序处理改善不平顺预测，PoseACT 加入末端位姿表达；Depth-Enhanced DP 用 Depth Anything V2 估计深度并与 RGB 特征交叉注意力融合。估计深度不是经过标定的真实米制深度，不能把其改进直接归为新增深度传感器的贡献

数据质量检查关注追踪置信度和轨迹连续性。低置信、突变或明显不合理的记录应标记，而不是静默补成成功轨迹。机械臂不可达、奇异位形和关节突变仍应在部署前验证，尤其是从末端轨迹转换为绝对关节标签时

## D. 实验与结果

正式版 §5 报告超过一万五千条示范，二十四项任务、二十一类物体、十三类操作技能，每条约 120–400 帧。帧密集不能自动解释为独立信息或更长有效技能，动作覆盖仍需另外比较

§6.1 十二项真机任务每项随机取二百条示范，分四组，每组五十条；组内改变目标位置，组间改变机器人起始姿态和场景。测试使用训练中出现过的物体姿态、但新的场景上下文，每方法每任务十五次，不是完全未见动作组合

Table 1：Open Container 的 DP/ACT 为 93.33%/86.67%，Open Drawer 为 53.33%/80%，Pick Bear 为 80%/20%。这些比例的步长约为 1/15，说明表现明显依任务与动作表示变化，不能宣布一种方法始终更好

§6.2 的深度增强 DP 在 Pick Lid 上比原 DP 增加 26.67 个百分点，在 Open Ricecooker 上增加 73.33 个百分点；它们是相同任务协议下成功率的差，不是训练速度增益。ACT 的平滑与位姿变体另外比较，不能把多项改进效果相加

附录还检查追踪、镜头、数据量和跨平台设置。当前项目网站证书过期，因此不能写成网站已无障碍访问；代码仓库已迁移到当前链接，数据资源存在访问条款或登录门槛时，应按官方条件获取。采集者总人数、全部任务完整采集时长及不同硬件统一成本没有在本卡当作已知量

## E. 不足与未来

论文讨论双传感器同步、追踪漂移和不同控制表示的局限。相对动作降低部分起点依赖，但精细高度控制可能受损；绝对关节动作又可能超出目标机器人的工作范围

本库分析：T265 为追踪相机，D435i 为 RGB-D 相机，两者功能不能直接互换。硬件解耦不等于免标定，真实执行仍需要相机外参、工具偏置和机器人模型。对外发布的数据接口也不保证完整软硬件环境在当前版本可一键运行

我们的设想是先在普通夹爪上建立统一时间轴，保存原始位姿、置信度、夹爪宽度与转换后动作，再分别训练相对 TCP 和关节策略。若使用 DH116，需要独立的指关节与接触表示，夹爪一个宽度值无法表达多指运动。论文未建立独立任务失败恢复模块，采集质量筛查和轨迹平滑不能替代部署时的异常检测与回退

## 相关工作与阅读入口

- [[03 论文卡片/08_数据与遥操作/AirExo-2 - Scaling up Generalizable Robotic Imitation Learning with Low-Cost Exoskeletons|P220 · AirExo-2: Scaling up Generalizable Robotic Imitation Learning with Low-Cost Exoskeletons]]
- [[03 论文卡片/08_数据与遥操作/On Bringing Robots Home|P223 · On Bringing Robots Home]]
- [[03 论文卡片/08_数据与遥操作/Universal Manipulation Interface - In-The-Wild Robot Teaching Without In-The-Wild Robots|P193 · Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots]]

- 所属方向与专题导读：[[02 研究方向/数据与遥操作]]
- 遥操作路线：[[01 论文文库/专题阅读/机器人遥操作与动作重定向]]
- 数据质量路线：[[01 论文文库/专题阅读/机器人数据采集与数据质量]]

## 来源与核验边界

- 已阅读上述 25 页版本的正文、方法、实验与局限，含附录时一并核对；关键架构或实验表经页面渲染检查，数字位置见各节
- 日期依据官方 arXiv 提交历史，机构依据所读版本署名；正式出处与所读预印本版本分别标明，不用会议日程或演示获奖冒充正式出版
- 论文结果、作者限制和本库研究设想分开；未报告字段不补猜，未核实引用量不填 0
- 代码和数据链接用于核对公开资源，未运行第三方代码、未执行机器人动作；可访问与可完整复现分别评价
- PDF 再分发许可未统一确认，遵循现有忽略规则仅保存本地；代码许可不自动覆盖论文、数据及模型
