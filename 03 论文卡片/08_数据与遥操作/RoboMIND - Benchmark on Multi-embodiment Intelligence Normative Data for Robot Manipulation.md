---
paper_id: "P232"
title: "RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation"
aliases: ["RoboMIND", "面向机器人操作的多具身规范数据基准"]
authors: ["Wu, Kun", "Hou, Chengkai", "Liu, Jiaming", "Che, Zhengping", "Ju, Xiaozhu", "Yang, Zhuqin", "Li, Meng", "Zhao, Yinuo", "Xu, Zhiyuan", "Yang, Guang", "Fan, Shichao", "Wang, Xinhua", "Liao, Fei", "Zhao, Zhen", "Li, Guangyu", "Jin, Zhao", "Wang, Lecheng", "Mao, Jilei", "Liu, Ning", "Ren, Pei", "Zhang, Qiang", "Lyu, Yaoxu", "Liu, Mengzhen", "He, Jingyang", "Luo, Yulin", "Gao, Zeyu", "Li, Chenxuan", "Gu, Chenyang", "Fu, Yankai", "Wu, Di", "Wang, Xingyu", "Chen, Sixiang", "Wang, Zhenyu", "An, Pengju", "Qian, Siyuan", "Zhang, Shanghang", "Tang, Jian"]
year: 2024
venue: "RSS 2025"
arxiv: "2412.13877"
version: "v3"
pdf: "01 论文文库/PDFs/08_数据与遥操作/RoboMIND.pdf"
document_type: "research_paper"
preprint_platform: "arXiv"
first_public_date: "2024-12-18"
first_public_month: "2024-12"
first_public_scope: "arXiv v1 UTC submission; cross-platform earliest release not established"
publication_status: "RSS 2025"
affiliations: ["Beijing Innovation Center of Humanoid Robotics", "Peking University", "Beijing Academy of Artificial Intelligence"]
metadata_verified_on: "2026-10-25"
metadata_sources: ["https://arxiv.org/abs/2412.13877", "https://x-humanoid-robomind.github.io/", "https://arxiv.org/pdf/2412.13877v3"]
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Human_Demonstration", "Retargeting", "Data_Quality"]
doi: "10.15607/RSS.2025.XXI.152"
---

# RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation

## 基本信息

- 稳定编号：P232
- 中文译名：面向机器人操作的多具身规范数据基准
- 作者：Wu, Kun；Hou, Chengkai；Liu, Jiaming；Che, Zhengping；Ju, Xiaozhu；Yang, Zhuqin；Li, Meng；Zhao, Yinuo；Xu, Zhiyuan；Yang, Guang；Fan, Shichao；Wang, Xinhua；Liao, Fei；Zhao, Zhen；Li, Guangyu；Jin, Zhao；Wang, Lecheng；Mao, Jilei；Liu, Ning；Ren, Pei；Zhang, Qiang；Lyu, Yaoxu；Liu, Mengzhen；He, Jingyang；Luo, Yulin；Gao, Zeyu；Li, Chenxuan；Gu, Chenyang；Fu, Yankai；Wu, Di；Wang, Xingyu；Chen, Sixiang；Wang, Zhenyu；An, Pengju；Qian, Siyuan；Zhang, Shanghang；Tang, Jian
- 研究机构：Beijing Innovation Center of Humanoid Robotics；Peking University；Beijing Academy of Artificial Intelligence
- 年份：2024
- 首次公开：arXiv v1，2024-12-18（UTC；仅限定该平台，不声称全平台最早）
- 出处与版本：RSS 2025；所读 v3，21 页
- 研究主题：多机器人数据标准、质量审核、失败与细粒度语言标注
- 引用量：待核验
- 引用量来源：Google Scholar
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/RoboMIND.pdf|打开本地 PDF]]（已核对文件身份；仅本地保留，不承诺 GitHub 网页可访问）
- [官方论文页](https://arxiv.org/abs/2412.13877)｜[官方 PDF](https://arxiv.org/pdf/2412.13877v3)｜[官方项目](https://x-humanoid-robomind.github.io/)
- DOI：[ 10.15607/RSS.2025.XXI.152 ](https://doi.org/10.15607/RSS.2025.XXI.152)
- 官方代码：[对应 GitHub 仓库](https://github.com/Open-X-Humanoid/x-humanoid-training-toolchain)
- 数据：[官方数据入口](https://huggingface.co/datasets/x-humanoid-robomind/RoboMIND)（下载内容、许可与访问权限以页面说明为准）

## 论文简介

RoboMIND 试图解决多机器人数据虽然很多，却难以放在一起训练的问题。不同实验室的相机、动作定义、任务名称与检查标准不一致，容易让模型学到采集习惯而非操作规律。作者选择在统一规范下采集不同本体的数据，覆盖单臂夹爪、双臂和带灵巧手的人形机器人，同时提供状态、语言和失败信息

论文重点不是设计一个新的手指重定向公式，而是建立可训练、可审核、可比较的数据链条。采集前定义任务，采集中使用适配机器人结构的主端或动作捕捉系统，采集后检查掉帧、抖动、重复抓取、碰撞等问题。长程轨迹先由模型划分并描述步骤，再经人工核对。每条轨迹集中保存多视角 RGB-D、关节和末端信息，使训练与故障分析有共同基础

需要特别注意规模口径。论文称约十点七万条轨迹，但正文明确包含数字孪生仿真数据，不能把全部都说成真实机器人示范；不同段落的精确分项也有差异，本卡保留这个不一致。另有五千条失败记录，它们是研究失败检测和恢复的资源，而不是已训练出通用恢复能力的证明。对我们的启发是先建立可靠任务定义、同步检查和审核规则，再扩大 DH116 或夹爪的采集规模，不必模仿大规模场地才能采用这些质量原则

## A. 基本信息与研究问题

论文比较四种机器人配置：Franka、UR5e 单臂，AgileX 双臂与 Tien Kung 人形。Table I 将机器人类型合并为单臂、双臂、人形三类，与“四种具身配置”不是矛盾。数据覆盖 479 个任务、96 类物体和 38 项技能

核心问题是规范性与多样性如何兼得。统一采集协议用于控制格式和质量，机器人本体及任务仍应保持差异。适配工具链将数据转换给 LeRobot 等训练框架，不表示不同机器人的关节索引可以直接混用

## B. 相关工作

DROID 以统一机器人设置获得自然场景多样性，Open X-Embodiment 聚合多个已有数据集获得跨本体规模，但不同来源的格式与任务定义可能不一致。RoboMIND 从采集环节建立统一规范，同时覆盖多种本体

GELLO 读取同构主端关节，适合单臂直接映射；Mobile ALOHA 式双臂主从有利于协调动作；动作捕捉服记录人体多关节，再映射到人形机器人。它们是不同采集接口，不是同一套动作无需转换地控制全部平台

ACT、Diffusion Policy、BAKU 是利用示范学习动作的策略；OpenVLA、RDT、CrossFormer 则支持更广任务或语言条件。论文用这些模型验证数据能否支撑学习，不应把某个数据集的规模当成模型在所有任务上都更好的证据。失败数据可帮助分类器和奖励学习，但当前数据基准不等于已经实现这些下游方法

## C. 核心贡献与方法

流程：定义机器人—技能—物体—场景任务 → 适配遥操作设备 → 同步记录 → 三阶段质量审核 → 成功/失败分类 → 长程语言标注 → 统一文件与训练接口

单臂主端采用三维打印结构和舵机，匹配机器人自由度；双臂使用辅助机械臂带动操作臂；人形使用 Xsens 动作捕捉并映射人体关节。每种平台都需要自身运动学、零位和控制配置，规范统一不消除硬件差异

每条 H5 文件汇集多视角 RGB-D、机器人本体状态、末端状态与遥操作状态。这样能从同一时间轴追踪“操作者命令—机器人实际运动—视觉结果”，而不只保存最终成功视频。图像丢帧和控制延迟仍需检查，格式一致本身不保证同步正确

质量审核先快速查看视频技术问题，再逐帧或慢放检查操作，最后记录问题时间与类别。图 4 给出八类标准，包括多余接触、运动不平滑、二次抓取、抖动、抓前碰撞、图像畸变、放置失败和夹爪出视野。记录失败原因可以指导重采，而不是简单把失败文件混回成功数据

细粒度语言标注覆盖约一万条成功轨迹。Gemini 先分段并生成步骤描述，人工再核对对象、关键动作、细节、时间粒度与逻辑连续性。模型自动输出不是最终真值，尤其不能把语言上说“抓住”当成实际已建立稳定接触

数字孪生环境提供相应任务仿真轨迹，可用于共同训练。仿真与真实数据的来源字段应保留，训练时明确混合比例；否则无法判断模型进步来自规模、场景覆盖还是仿真偏差

## D. 实验与结果

§IV-A 写 Franka 含 26,070 条仿真及 26,866 条真实示范，其他本体为真实示范；引言另有真实 Franka 26,856、仿真总量 30,035 的分项。论文不同段落口径不完全一致，因此只使用约 107k 总规模，并明确包含仿真，不强行给出一个“全部真实”的精确总和

额外发布五千条失败案例，约一万条长程成功轨迹具有细粒度语言标注，后者是成功集子集，不额外重复加到总规模。每轨迹的技能数量与时长随本体不同，人形和双臂通常更长，不能仅比较文件数量来衡量有效动作监督

单任务实验选择四种配置共四十五任务，Franka十五、人形十、AgileX十五、UR5e五。每模型每任务十次真机测试，用任务成功率评价。ACT 在 AgileX 十五任务平均 55.3%，Franka 30.7%，UR5e 38.0%，人形 34.0%。这是不同任务组的平均，不能据此认为同任务双臂天然优于单臂

BAKU 的默认参数来自原实现，论文讨论其真机适配不足，所以排名同时反映训练配置。VLA 实验另外选择十五任务，并测试新场景、新物体以及预训练与数字孪生共同训练；不能把这十五任务当整个 479 任务的全量评测

Franka 使用三台 D435i，UR5e 使用一台顶部 D435i；人形的实验设置写 RH56DFX 手及 Orbbec 相机。硬件概述与实验安装视角应区分。没有统一报告每条有效示范总工时和全部审核人员人数，不能估算全国或家庭部署成本

## E. 不足与未来

作者指出模型在精确定位、抓取、长程组合等方面仍存在失败。公开失败轨迹为后续恢复研究提供条件，但论文不是对所有失败类型已有闭环恢复验证

我的理解是质量审核标准本身需要适用范围：重复抓取在成功示范清洗中可能被过滤，但在恢复数据集中应保留并标注。若无来源与目的标签地统一删除，会失去研究失败恢复的重要信息

对现有机械臂、DH116、D435i 最可复用的是数据协议：任务定义、相机与状态时间戳、期望/实际动作、关节有效掩码、失败时间和原因。不能把 RH56DFX 的关节与 DH116 编码直接等同。先用少量夹爪任务检验训练数据转换与随机回放一致，再逐步加入灵巧手和双臂

未来可做跨本体动作掩码、标注一致性抽检及失败片段价值评估，明确比较成功集、未筛选集和带失败标签集。不同来源版本的数据规模、许可证和机器人控制接口应单独登记，不能将后续 RoboMIND 2.0 的规模回填成本文原始结果

## 相关工作与阅读入口

- [[03 论文卡片/08_数据与遥操作/AgiBot World Colosseo - A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems|P233 · AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems]]
- [[03 论文卡片/10_基准测试与数据集/Open X-Embodiment - Robotic Learning Datasets and RT-X Models|P002 · Open X-Embodiment: Robotic Learning Datasets and RT-X Models]]
- [[03 论文卡片/10_基准测试与数据集/DROID - A Large-Scale In-The-Wild Robot Manipulation Dataset|P010 · DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset]]

- 所属方向与专题导读：[[02 研究方向/数据与遥操作]]
- 遥操作路线：[[02 研究方向/机器人遥操作与动作重定向]]
- 数据质量路线：[[02 研究方向/机器人数据采集与数据质量]]

## 来源与核验边界

- 已阅读上述 21 页版本的正文、方法、实验与局限，含附录时一并核对；关键架构或实验表经页面渲染检查，数字位置见各节
- 日期依据官方 arXiv 提交历史，机构依据所读版本署名；正式出处与所读预印本版本分别标明，不用会议日程或演示获奖冒充正式出版
- 论文结果、作者限制和本库研究设想分开；未报告字段不补猜，未核实引用量不填 0
- 代码和数据链接用于核对公开资源，未运行第三方代码、未执行机器人动作；可访问与可完整复现分别评价
- PDF 再分发许可未统一确认，遵循现有忽略规则仅保存本地；代码许可不自动覆盖论文、数据及模型
