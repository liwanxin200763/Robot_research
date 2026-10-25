---
paper_id: "P228"
title: "DexVIP: Learning Dexterous Grasping with Human Hand Pose Priors from Video"
aliases: ["DexVIP", "利用视频人手姿态先验学习灵巧抓取"]
authors: ["Mandikal, Priyanka", "Grauman, Kristen"]
year: 2022
venue: "CoRL 2021；PMLR 164 出版年 2022"
arxiv: "2202.00164"
version: "v1"
pdf: "01 论文文库/PDFs/08_数据与遥操作/DexVIP.pdf"
document_type: "research_paper"
preprint_platform: "arXiv"
first_public_date: "2022-02-01"
first_public_month: "2022-02"
first_public_scope: "arXiv v1 UTC submission; cross-platform earliest release not established"
publication_status: "CoRL 2021；PMLR 164 出版年 2022"
affiliations: ["The University of Texas at Austin", "Facebook AI Research"]
metadata_verified_on: "2026-10-25"
metadata_sources: ["https://arxiv.org/abs/2202.00164", "https://proceedings.mlr.press/v164/mandikal22a.html", "https://arxiv.org/pdf/2202.00164v1"]
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Human_Demonstration", "Retargeting"]
---

# DexVIP: Learning Dexterous Grasping with Human Hand Pose Priors from Video

## 基本信息

- 稳定编号：P228
- 中文译名：利用视频人手姿态先验学习灵巧抓取
- 作者：Mandikal, Priyanka；Grauman, Kristen
- 研究机构：The University of Texas at Austin；Facebook AI Research
- 年份：2022
- 首次公开：arXiv v1，2022-02-01（UTC；仅限定该平台，不声称全平台最早）
- 出处与版本：CoRL 2021；PMLR 164 出版年 2022；所读 v1，18 页
- 研究主题：视频抓姿筛选、功能区域、强化学习先验
- 引用量：待核验
- 引用量来源：Google Scholar
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/DexVIP.pdf|打开本地 PDF]]（已核对文件身份；仅本地保留，不承诺 GitHub 网页可访问）
- [官方论文页](https://arxiv.org/abs/2202.00164)｜[官方 PDF](https://arxiv.org/pdf/2202.00164v1)｜[官方项目](https://vision.cs.utexas.edu/projects/dexvip-dexterous-grasp-pose-prior/)
- [正式发表来源](https://proceedings.mlr.press/v164/mandikal22a.html)
- 官方代码：未核实独立官方代码仓库，不用机构主页代替
- 数据：未核实独立完整数据集入口；代码中的示例和项目展示不等于完整数据发布

## 论文简介

DexVIP 不要求一段视频精确给出每一步机器人动作，而是问：人们经常怎样握住某类物体，这种姿态能否帮助机器人更快学会抓取。作者从公开视频挑出手持物体的图像，估计人手三维姿态，按物体类别聚类选出代表握姿，再映射到机器人手。训练时，这个握姿成为强化学习的辅助奖励，与抓取成功、接触功能区域和探索奖励一起指导策略

这个监督比完整遥操作轨迹弱得多。视频只告诉机器人“可以考虑这样的手型”，并不提供可直接执行的力矩、接近路径或完整接触过程。机器人仍要在仿真里大量试错，学会如何靠近、接触和抬起物体。方法还使用物体功能区域信息，例如杯把或工具握柄，使机器人不仅抓得住，也倾向于抓在有使用意义的位置。姿态先验只在足够接触时启用，避免机器人在远处就盲目摆出固定握姿

实验全部在 MuJoCo 仿真，作者明确说没有真实灵巧手可用。因此它是人类视频提供低成本先验的基础证据，不是互联网视频直接训练真机操作的完成系统。论文还区分抓取成功、扰动力下稳定性、功能性和姿态相似度，不能把某一评分提升当成所有能力同时解决。对 DH116 的启发是利用常见抓姿缩小搜索空间，但人手与机器手的关节差异、接触几何和真实传感噪声仍要重新验证

## A. 基本信息与研究问题

研究问题是在三十维动作空间中怎样利用免费或低成本人类观察帮助探索，同时避免采集大量实验室遥操作示范。输入为筛选后的物体抓持图像、对应类别与仿真场景，输出为仿真抓取策略

正式来源为第五届 CoRL，即 CoRL 2021，PMLR 164 在 2022 年出版。首次 arXiv 公开是 2022-02，不能据此说整个工作首次出现于 2022-02；本卡首次公开字段明确限定 arXiv 平台，会议与跨平台更早公开分开记录

## B. 相关工作

只奖励物体离桌会让机器人在巨大关节空间中缓慢探索。GRAFF 用物体可操作区域引导在哪里抓，DAPG 则依赖专家的运动捕捉轨迹指导如何抓。前者缺少手型指导，后者需要专门设备与演示

DexVIP 将两者之间的低成本信息利用起来：公开视频提供手型，功能区域提供位置，强化学习负责真正完成动作。与轨迹重定向不同，它不复制一段人手运动；与直接姿态监督不同，策略可以在任务奖励下调整自己的动作，姿态只是辅助偏好

因此公开视频质量、类别选择和代表姿态是否合理十分重要。一个类别常见的握姿不一定适合不同尺寸、不同摩擦的每个实例，不能把“人常这样握”直接解释为物理最优

## C. 核心贡献与方法

流程：筛选公开视频抓持帧 → FrankMocap 人手姿态 → 每类别聚类选代表 → 映射机器人握姿 → 视觉与本体感觉策略 → PPO 抓取训练 → 多指标仿真评价

作者从 HowTo100M 中按物体与任务类别筛帧，共七百一十五张、二十七种物体，平均每物体约二十六张。只保留右手，使用相对规范直立物体图像。不是无人工筛选地吸收整套公开视频，也没有使用完整视频的逐时刻接触力

FrankMocap 估计三维手姿态，然后用 k-medoid 聚类选最大簇的代表姿态，避免直接平均不同握法得到不可用的中间姿态。该姿态经关节重定向成为目标机器人手型。只选最大簇也可能忽略少见但有用的握法

策略视觉流包含 RGB、深度与功能区域图，本体流包含关节状态、速度和手物距离；手上还有二十一个触觉传感点。输出为三十维关节目标，使用 PPO 学习。奖励中手型项在约三成触觉点激活后才生效，避免接近阶段过度受固定姿态限制；手臂方位等与视频视角相关的分量在姿态误差中被忽略

成功奖励、功能区域距离和姿态奖励一起权衡。距离是几何代理，不等于真实压力或摩擦锥约束。策略的可执行性只在给定 MuJoCo 模型与控制设定下得到验证

## D. 实验与结果

机器人是二十四自由度多指手加六自由度手臂的 Adroit 模型，共三十自由度。所有实验均为仿真。策略在二十七种物体上训练一亿五千万个交互步，每回合二百步，四个随机种子；评价每物体一百回合、初始方向变化零到一百八十度

成功定义为最后五十个时间步持续把物体抬离桌面；稳定性是在回合后沿六个正交方向施加一牛顿扰动，仍抓住才满足；功能性只针对成功抓取，检查与真实功能区域的接近；姿态指标衡量与目标握姿距离并归一化。这四个数不能直接作为同一成功率相互比较

附录 Table C：仅功能区域成功评分 60、稳定性 41；加入触觉为 63、45；完整姿态先验为 68、51。功能性由 63 到 64 变化很小，说明主要增益不在所有维度均匀出现。姿态评分则从 48 提高到 62

在额外十一种非 ContactDB 类别物体上，论文报告 DexVIP 从 68% 到 65%，下降三个百分点，约 4% 相对下降；DAPG 从 59% 到 50%，下降九个百分点，约 15% 相对下降。必须区分百分点与相对降幅。没有真机、采集吞吐、真实相机部署或 DH116 结果，也没有给出完整真实复现系统

## E. 不足与未来

论文明确仅有仿真验证，双手抓取留给未来。公开视频姿态筛选与类别对应也有人工和分布限制，不能称为完全自动通用系统

本库分析：单个代表姿态可能压制类别内多样握法，功能区域假设和三维对象追踪也增加部署依赖。加噪声仿真能检查一定鲁棒性，但不能替代真实接触材料、传感漂移和控制延迟。页面未提供已核实的本文独立代码仓库，模板引用的其他 GitHub 项目不能冒充代码链接

对 DH116 可把常见握姿作为候选初始化或软奖励，先确认关节可达与接触可行，再看是否减少探索；不能强行匹配人手全部关节。D435i 可提供物体深度，但功能区域和手物状态仍需估计。恢复能力没有作为独立系统验证，稳定性扰动测试也不等于会自主检测失败和重新抓取

## 相关工作与阅读入口

- [[03 论文卡片/08_数据与遥操作/DexMV - Imitation Learning for Dexterous Manipulation from Human Videos|P227 · DexMV: Imitation Learning for Dexterous Manipulation from Human Videos]]
- [[03 论文卡片/08_数据与遥操作/Hand-Object Interaction Pretraining from Videos|P237 · Hand-Object Interaction Pretraining from Videos]]
- [[03 论文卡片/04_灵巧操作/Human2Dex - Dexterous Robot Learning from Wrist-Centric Human Demonstrations|P185 · Human2Dex: Dexterous Robot Learning from Wrist-Centric Human Demonstrations]]

- 所属方向：[[02 研究方向/数据与遥操作]]
- 专题导读：[[02 研究方向/数据与遥操作_从采集到可执行示范]]
- 遥操作路线：[[02 研究方向/机器人遥操作与动作重定向]]
- 数据质量路线：[[02 研究方向/机器人数据采集与数据质量]]

## 来源与核验边界

- 已阅读上述 18 页版本的正文、方法、实验与局限，含附录时一并核对；关键架构或实验表经页面渲染检查，数字位置见各节
- 日期依据官方 arXiv 提交历史，机构依据所读版本署名；正式出处与所读预印本版本分别标明，不用会议日程或演示获奖冒充正式出版
- 论文结果、作者限制和本库研究设想分开；未报告字段不补猜，未核实引用量不填 0
- 代码和数据链接用于核对公开资源，未运行第三方代码、未执行机器人动作；可访问与可完整复现分别评价
- PDF 再分发许可未统一确认，遵循现有忽略规则仅保存本地；代码许可不自动覆盖论文、数据及模型
