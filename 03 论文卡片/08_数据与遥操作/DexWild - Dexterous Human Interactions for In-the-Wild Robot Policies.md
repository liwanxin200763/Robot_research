---
paper_id: "P224"
title: "DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies"
aliases: ["DexWild", "利用野外人类灵巧交互训练机器人策略"]
authors: ["Tao, Tony", "Srirama, Mohan Kumar", "Liu, Jason Jingzhou", "Shaw, Kenneth", "Pathak, Deepak"]
year: 2025
venue: "RSS 2025"
arxiv: "2505.07813"
version: "v2"
pdf: "01 论文文库/PDFs/08_数据与遥操作/DexWild.pdf"
document_type: "research_paper"
preprint_platform: "arXiv"
first_public_date: "2025-05-12"
first_public_month: "2025-05"
first_public_scope: "arXiv v1 UTC submission; cross-platform earliest release not established"
publication_status: "RSS 2025"
affiliations: ["Carnegie Mellon University"]
metadata_verified_on: "2026-10-25"
metadata_sources: ["https://arxiv.org/abs/2505.07813", "https://roboticsconference.org/2025/program/papers/75/", "https://arxiv.org/pdf/2505.07813v2"]
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Human_Demonstration", "Retargeting"]
---

# DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies

## 基本信息

- 稳定编号：P224
- 中文译名：利用野外人类灵巧交互训练机器人策略
- 作者：Tao, Tony；Srirama, Mohan Kumar；Liu, Jason Jingzhou；Shaw, Kenneth；Pathak, Deepak
- 研究机构：Carnegie Mellon University
- 年份：2025
- 首次公开：arXiv v1，2025-05-12（UTC；仅限定该平台，不声称全平台最早）
- 出处与版本：RSS 2025；所读 v2，15 页
- 研究主题：自然人手采集、跨具身共同训练、数据筛选
- 引用量：待核验
- 引用量来源：Google Scholar
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/DexWild.pdf|打开本地 PDF]]（已核对文件身份；仅本地保留，不承诺 GitHub 网页可访问）
- [官方论文页](https://arxiv.org/abs/2505.07813)｜[官方 PDF](https://arxiv.org/pdf/2505.07813v2)｜[官方项目](https://dexwild.github.io/)
- [正式发表来源](https://roboticsconference.org/2025/program/papers/75/)
- 官方代码：[对应 GitHub 仓库](https://github.com/dexwild/dexwild)
- 数据：[官方数据入口](https://huggingface.co/datasets/boardd/dexwild-dataset)（下载内容、许可与访问权限以页面说明为准）

## 论文简介

DexWild 关心的不是让机器人在一个训练桌面上再提高一点，而是如何把不同房间、物体、光照和操作者的经验变成可用的灵巧操作数据。直接遥操作能得到真实机器人动作，但采集受硬件和场地限制；只看人类视频又缺少准确的手指与手腕状态。作者让人戴着动作捕捉手套，在手掌安装相机，用自己的手自然操作物体，再将这些数据与少量机器人遥操作共同训练

系统刻意对齐两种数据的观察与动作。人的手掌相机和机器人手相机采用相似位置，尽量看物体而不是手的外形；手指动作通过运动学重定向转成机器人关节目标，手腕使用相对运动表达，减少依赖全局坐标。共同训练时，人类数据带来场景多样性，机器人数据提供真实执行约束，二者缺一都会影响效果。论文还对轨迹做启发式筛选，并分别归一化人类与机器人的动作，说明扩大数据量不能省略质量与分布处理

作者用十名未经训练的采集者记录九千多条自然示范，并在单臂和双臂任务上测试。值得注意的是，论文正文用“成功率”描述部分结果，但附录按任务阶段给分，不能把所有表中小数都解释为整任务成功比例。当前所读 v2 的极端新环境平均分与摘要数字也不完全一致，本卡保留表格口径。对我们的启发是用少量可信机器人数据锚定大量人类数据，并明确衡量覆盖、多样性与动作可执行性；它不等于任何手套数据都能无校准地用于 DH116

## A. 基本信息与研究问题

研究问题是如何同时获得低门槛、多样性和可用于机器人训练的动作标签。DexWild 分为可携带采集系统与共同训练框架。视觉、手指和手腕都要记录，仅有自然视频不能完成本文流程

采集端包含手套、掌部同步相机、跟踪相机与小型计算机。机器人实验包括 xArm、Franka，以及 LEAP Hand 和 LEAP Hand V2 Advanced。论文的 embodiment-agnostic 意为数据与表示尽量不绑定单一机器人，并不表示无需给新机械手配置运动学和控制接口

## B. 相关工作

主从与视觉遥操作让机器人实际执行动作，标签可信但吞吐受机器人限制。自然人手采集更快，却必须解决人与机器人的动作和视觉差异。DexCap 等工作表明可利用穿戴设备获得更可靠的人手轨迹，UMI 则通过类似夹爪的工具和一致视角缩小差异

DexWild 保留自然人手的灵活性，用掌部视角和机器人手运动学重定向搭桥，再用机器人示范共同训练。与只用人类视频预训练视觉表征不同，这里的手指与手腕信息直接进入动作训练目标。与只混合数据不处理分布的做法不同，本文分别归一化动作、筛除无效轨迹，并实验比较混合比例

扩散策略能表达多个操作者采用的不同动作方式，但不能保证多样性越大越好。若把不准确的人类标签大量加入，模型仍可能远离机器人可执行动作，机器人示范的锚定作用因此重要

## C. 核心贡献与方法

流程：自然人手示范 → 手套与手腕跟踪 → 同步掌部观察 → 机器人手重定向和质量过滤 → 分域动作归一化 → 人机共同训练 → 真机闭环执行

手套记录指端几何，外部相机追踪手套上的 ArUco 标记。掌部双相机尽量观察环境并减小手本体进入画面的比例，机器人也复制相机安装方式。相对位姿表达避免每个新场景都依赖固定全局坐标，但固定安装几何、相机内参和机器人运动学仍然存在，不能把 calibration free 扩大解释为没有任何几何前提

手指重定向通过机器人正向运动学优化匹配指尖位置，手腕动作由相邻时刻的相对位姿得到。单手动作示例为二十六维：九维末端位姿表示加十七维手部目标。双手时复制两侧观察与动作，并增加双手相对位姿，帮助跨手配合。这里旋转的六维表示是连续编码，不是六个独立旋转自由度

启发式过滤移除明显无效轨迹；人和机器人动作分别归一化，避免天然尺度差异让一种数据支配学习。训练批次按固定权重同时采两种数据，用预训练视觉 Transformer 编码图像，再用扩散 U-Net 预测动作块。论文没有采用“先把人数据全部变成机器人真实执行成功轨迹”这一前提，所以剩余域差异由数据配比和机器人示范共同缓解

部署时视觉策略预测的末端与关节目标还要通过机器人控制器执行。跟踪质量、关节限位、相机遮挡和动作跳变仍需检查，不能把损失下降等同于安全接触

## D. 实验与结果

§IV 的人类数据共 9,290 条：喷瓶 3,000、玩具整理 3,000、倾倒 621、插花 1,545、折衣 1,124，来自十名采集者和多种环境。机器人数据 1,395 条用于具身锚定。Figure 5 列出训练与测试物体，不能把人类数据出现过的环境都算完全未见

Table IV 比较 Robot:Human 的 1:1、1:2、1:5。训练分布内两任务平均分，机器人单独 0.647，1:2 为 0.798；人类环境但没有机器人训练数据的条件，分别 0.285 和 0.751。极端新环境四任务分别是喷瓶、整理、插花和折衣，1:2 平均 0.627，机器人单独 0.220。它们依附录阶段得分定义，不全部是二元整任务成功率

摘要仍给出 68.5%，与当前 v2 Table IV 的极端条件平均 62.7% 不同，本卡不自行修正作者数字，也不把两个版本的口径合并。表中任务、环境和混合比例需要同时说明，否则“几倍提升”会失去分母

附录训练配置为七万步、batch 256、环境三十赫兹、动作块四十八步，扩散训练一百步、推理十六步。动作块长度不是推理频率。系统约四点六倍采集加速来自论文采集对比，不代表所有人、任务或数据清洗总工时都同倍改善。跨任务倾倒使用其他任务的机器人示范，并非完全没有机器人数据；也没有验证 DH116

## E. 不足与未来

作者讨论人类与机器人数据的互补性，以及新场景、新任务和新本体仍存在迁移差异。人类单独训练表现较差，说明自然交互多样性不能取代真实执行锚定

本库分析：启发式过滤可能漏掉细微接触错误；仅匹配指尖位置不能保证指骨不穿透、接触力可实现。相机一致安装也有机械与光学成本。平均阶段分提高，不保证每次长程任务完整完成，失败恢复系统需要独立定义和测试

对我们可先开展人类与普通夹爪共同训练的小规模对照，再扩展 DH116 的手指映射。D435i 可补充三维观察，但不提供手套的指端状态，必须单独解决遮挡和运动学。建议固定机器人示范数量，逐步增加经过筛选的人类数据，比较动作误差、接触合理性与整任务成功率，而不是只比较数据总量。以上为研究设想，不是论文已经验证的硬件迁移结果

## 相关工作与阅读入口

- [[03 论文卡片/08_数据与遥操作/DexViTac - Collecting Human Visuo-Tactile-Kinematic Demonstrations for Contact-Rich Dexterous Manipulation|P226 · DexViTac: Collecting Human Visuo-Tactile-Kinematic Demonstrations for Contact-Rich Dexterous Manipulation]]
- [[03 论文卡片/08_数据与遥操作/EgoMimic - Scaling Imitation Learning via Egocentric Video|P236 · EgoMimic: Scaling Imitation Learning via Egocentric Video]]
- [[03 论文卡片/08_数据与遥操作/DexCap - Scalable and Portable Mocap Data Collection System for Dexterous Manipulation|P009 · DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation]]

- 所属方向与专题导读：[[02 研究方向/数据与遥操作]]
- 遥操作路线：[[02 研究方向/机器人遥操作与动作重定向]]
- 数据质量路线：[[02 研究方向/机器人数据采集与数据质量]]

## 来源与核验边界

- 已阅读上述 15 页版本的正文、方法、实验与局限，含附录时一并核对；关键架构或实验表经页面渲染检查，数字位置见各节
- 日期依据官方 arXiv 提交历史，机构依据所读版本署名；正式出处与所读预印本版本分别标明，不用会议日程或演示获奖冒充正式出版
- 论文结果、作者限制和本库研究设想分开；未报告字段不补猜，未核实引用量不填 0
- 代码和数据链接用于核对公开资源，未运行第三方代码、未执行机器人动作；可访问与可完整复现分别评价
- PDF 再分发许可未统一确认，遵循现有忽略规则仅保存本地；代码许可不自动覆盖论文、数据及模型
