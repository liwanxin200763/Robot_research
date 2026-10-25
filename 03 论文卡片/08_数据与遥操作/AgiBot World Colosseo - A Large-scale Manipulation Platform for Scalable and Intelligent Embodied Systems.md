---
paper_id: "P233"
title: "AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems"
aliases: ["AgiBot World Colosseo", "大规模机器人学习生态与潜动作通用策略"]
authors: ["Contributors, AgiBot World", "Bu, Qingwen", "Cai, Jisong", "Chen, Li", "Cui, Xiuqi", "Ding, Yan", "Feng, Siyuan", "Gao, Shenyuan", "He, Xindong", "Hu, Xuan", "Huang, Xu", "Jiang, Shu", "Jiang, Yuxin", "Jing, Cheng", "Li, Hongyang", "Li, Jialu", "Liu, Chiming", "Liu, Yi", "Lu, Yuxiang", "Luo, Jianlan", "Luo, Ping", "Mu, Yao", "Niu, Yuehan", "Pan, Yixuan", "Pang, Jiangmiao", "Qiao, Yu", "Ren, Guanghui", "Ruan, Cheng", "Shan, Jiaqi", "Shen, Yongjian", "Shi, Chengshi", "Shi, Mingkang", "Shi, Modi", "Sima, Chonghao", "Song, Jianheng", "Wang, Huijie", "Wang, Wenhao", "Wei, Dafeng", "Xie, Chengen", "Xu, Guo", "Yan, Junchi", "Yang, Cunbiao", "Yang, Lei", "Yang, Shukai", "Yao, Maoqing", "Zeng, Jia", "Zhang, Chi", "Zhang, Qinglin", "Zhao, Bin", "Zhao, Chengyue", "Zhao, Jiaqi", "Zhu, Jianchao"]
year: 2025
venue: "arXiv preprint；所读 v5 未据此确认正式会议"
arxiv: "2503.06669"
version: "v5"
pdf: "01 论文文库/PDFs/08_数据与遥操作/AgiBotWorldColosseo.pdf"
document_type: "research_paper"
preprint_platform: "arXiv"
first_public_date: "2025-03-09"
first_public_month: "2025-03"
first_public_scope: "arXiv v1 UTC submission; cross-platform earliest release not established"
publication_status: "arXiv preprint；所读 v5 未据此确认正式会议"
affiliations: ["The University of Hong Kong", "AgiBot Inc.", "Shanghai Innovation Institute", "Shanghai Artificial Intelligence Laboratory"]
metadata_verified_on: "2026-10-25"
metadata_sources: ["https://arxiv.org/abs/2503.06669", "https://agibot-world.com/", "https://arxiv.org/pdf/2503.06669v5"]
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Human_Demonstration", "Retargeting", "Data_Quality"]
---

# AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems

## 基本信息

- 稳定编号：P233
- 中文译名：大规模机器人学习生态与潜动作通用策略
- 作者：Contributors, AgiBot World；Bu, Qingwen；Cai, Jisong；Chen, Li；Cui, Xiuqi；Ding, Yan；Feng, Siyuan；Gao, Shenyuan；He, Xindong；Hu, Xuan；Huang, Xu；Jiang, Shu；Jiang, Yuxin；Jing, Cheng；Li, Hongyang；Li, Jialu；Liu, Chiming；Liu, Yi；Lu, Yuxiang；Luo, Jianlan；Luo, Ping；Mu, Yao；Niu, Yuehan；Pan, Yixuan；Pang, Jiangmiao；Qiao, Yu；Ren, Guanghui；Ruan, Cheng；Shan, Jiaqi；Shen, Yongjian；Shi, Chengshi；Shi, Mingkang；Shi, Modi；Sima, Chonghao；Song, Jianheng；Wang, Huijie；Wang, Wenhao；Wei, Dafeng；Xie, Chengen；Xu, Guo；Yan, Junchi；Yang, Cunbiao；Yang, Lei；Yang, Shukai；Yao, Maoqing；Zeng, Jia；Zhang, Chi；Zhang, Qinglin；Zhao, Bin；Zhao, Chengyue；Zhao, Jiaqi；Zhu, Jianchao
- 研究机构：The University of Hong Kong；AgiBot Inc.；Shanghai Innovation Institute；Shanghai Artificial Intelligence Laboratory
- 年份：2025
- 首次公开：arXiv v1，2025-03-09（UTC；仅限定该平台，不声称全平台最早）
- 出处与版本：arXiv preprint；所读 v5 未据此确认正式会议；所读 v5，9 页
- 研究主题：工业化采集、人工质量闭环、跨视频潜动作与VLA
- 引用量：待核验
- 引用量来源：Google Scholar
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/AgiBotWorldColosseo.pdf|打开本地 PDF]]（已核对文件身份；仅本地保留，不承诺 GitHub 网页可访问）
- [官方论文页](https://arxiv.org/abs/2503.06669)｜[官方 PDF](https://arxiv.org/pdf/2503.06669v5)｜[官方项目](https://agibot-world.com/)
- 官方代码：[对应 GitHub 仓库](https://github.com/OpenDriveLab/AgiBot-World)
- 数据：未核实独立完整数据集入口；代码中的示例和项目展示不等于完整数据发布

## 论文简介

AgiBot World Colosseo 不只追求把示范轨迹堆到百万条，而是讨论怎样持续生产能让机器人学会任务的数据。论文把任务可行性测试、操作者规范、边缘端完整性检查、云端人工审核和策略部署反馈连成闭环。如果模型学会了长时间停顿，就回查示范中的空闲片段并修订协议，这使“数据质量”具有可观察的下游反馈，而非只凭人工觉得视频好看

数据覆盖一百多台同系列双臂机器人、多种场景和长程任务。部分示范保留操作者犯错后成功纠正的片段，并标注原因与时间。它们对研究恢复有价值，但不能据此断言模型已经具有同样的自主纠错能力。论文还提出 GO-1：先从视频学习压缩的潜动作，再让视觉语言规划器预测潜动作，最后通过动作专家输出具体机器人的控制命令

阅读时必须区分规模、版本和评价指标。所读版本的轨迹总量与官方仓库 Beta 统计略有不同，应并列说明；主要策略评测采用零到一的部分完成得分，不是全部二元成功率。论文中“提升三十”对应分数绝对增加零点三，也不能写成所有任务成功率提升百分之三十。对我们而言，最值得借鉴的是小规模也能实践的采集—审核—训练—回查循环，以及明确区分失败样本、恢复示范和真正自主恢复测试

## A. 基本信息与研究问题

本卡读取 arXiv v5，修订于 2026-10-20，首次 arXiv 公开为 2025-03-09。PDF 集体署名 Team AgiBot-World，完整 arXiv 作者列表见元数据，不能把集体署名误读为某一位作者独立完成

论文同时贡献数据生态与层次策略 GO-1，二者需要分开评价。数据规模、任务覆盖和审核方式是资源属性；GO-1 的实验还涉及预训练、任务微调与测试条件，并不证明任意模型直接下载数据就获得同样能力

## B. 相关工作

OXE 聚合多来源数据以扩大具身范围，DROID 注重真实场景采集。AgiBot World 使用大量同系列机器人，在标准化采集条件中扩展场景和任务，减少某些格式差异，但也使本体多样性与同构部署便利性之间存在取舍

ACT 和扩散策略可以从示范学动作块，VLA 则在语言与视觉基础模型上接动作输出。直接学习具体机器人动作难以利用没有动作标签的人类视频。潜动作模型把视频相邻帧的变化编码成离散符号，再由机器人专家把高层变化落实到可执行动作

这种潜动作不是人工命名的技能，也不是关节角压缩后保证跨机器人物理一致。模型需要通过训练建立联系。论文的人工审核与回传类似数据闭环工程，重点在问题定义、质量反馈与再采集，而非提出一个自动识别所有低质量轨迹的通用评分器

## C. 核心贡献与方法

数据流程：任务预采与标准制定 → 熟练遥操作 → 边缘端查掉帧 → 云端审核和语言标注 → 策略训练部署 → 根据失败反馈修订采集

G1 平台有双七自由度臂、移动底盘与躯干，末端可更换夹爪、六自由度手或视触觉夹爪。八路相机与本体状态以三十赫兹记录。VR 控制器给腕部位姿和离散手势，动作捕捉系统再提供更细手指、躯干和头部姿态。VR 触发器不能自然记录任意手指关节

失败恢复示范约占百分之一，是人在采集过程中掉物后纠正并最终完成任务的轨迹，人工标注失败原因和时间。它与彻底失败样本、策略自主恢复测试三者不同。训练反馈还发现空闲帧使策略停顿，继而修订采集与后处理，体现质量标准应接受下游验证

GO-1 第一阶段训练视频逆动力学编码器，给定前后帧输出四个离散潜动作 token，用量化码本并通过解码器预测后帧。这里的 token 是学习出的变化表示，不是四个关节命令

第二阶段用 InternVL2.5-2B 视觉语言骨干及二十四层潜规划器，在多视角与语言条件下预测潜动作。第三阶段加入动作专家，结合视觉、语言和本体状态用扩散过程输出长度三十的动作块。训练时机器人动作监督把潜计划与硬件动作联系起来

策略预训练后还用高质量任务示范微调。论文给出的微调设置为学习率 2e-5、batch 768、三万步，不能把无微调和微调成绩混成一种“零样本”能力。部署仍需控制器与安全限制，潜动作合理不保证真实接触安全

## D. 实验与结果

论文统计 1,001,552 条轨迹、2,976.4 小时、217 任务、87 技能、106 场景和三千余物体；仓库 Beta 另给 1,003,672 条约 43.8 TB。这是版本统计差异，不强行合并。长程轨迹常约三十到六十秒，不能只用数量与更短轨迹的数据集比较监督量

评价每任务每场景每方法十次，完全成功为 1，部分完成按阶段计分。图 6 比较 RDT 在 OXE 与 Beta 预训练后，分布内平均完成分 0.47→0.77，分布外 0.38→0.67，绝对差为 0.30 和 0.29，不是把二者都称为成功率提升 30%

图 5 比较 GO-1、去潜规划器版本、RDT 与 π0。每任务合并三十次，包含十次已见和二十次变化条件。潜规划器平均增加约 0.12 完成分，表明中间表示有帮助；模型训练与资源不同，不能只按名称判定架构普遍优劣

图 7 的数据规模分析从 9.2k 到约 1M，使用预训练已见任务的直接表现，相关系数 r=0.97 是该实验拟合关系，不是任意任务都服从的定律。质量实验在擦桌任务比较 528 条已审核和 482 条未审核轨迹，报告分数约 0.41→0.59；两组并非同量随机只切换一个因素，不能把差异全归给审核算法

数据集采用 CC BY-NC-SA 4.0 等具体资源条款，代码许可不能代替数据许可。论文没有对 DH116 或普通 D435i 单机采集系统给直接成功率，不能移植结果数字

## E. 不足与未来

作者展示规模、规范与潜动作策略结合的价值，但大规模同系列硬件、审核队伍和部署设施的成本不能忽略。长程任务的部分得分有助诊断，也可能掩盖最后一步失败，应同时记录整任务完成率

我的理解是百分之一恢复示范值得保留原始时间轴、失败原因与接管事件，避免剪掉所有“难看”片段。但若没有部署时干预检测、回退规划与安全约束，不能声称闭环恢复已完成

我们的实验不必复制百万轨迹，而可先用机械臂、普通夹爪和 D435i 建立几十条示范的反馈循环：检查同步→训练→观察错误→定向补采。DH116 记录主动轴、耦合关系和接触状态，避免把六自由度手在外观上的相似当成动作空间相同。以后研究 VLA 可比较潜动作与直接动作的样本效率，并把人类视频预训练、机器人动作监督和恢复测试分别设计

## 相关工作与阅读入口

- [[03 论文卡片/08_数据与遥操作/RoboMIND - Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation|P232 · RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation]]
- [[03 论文卡片/08_数据与遥操作/EgoMimic - Scaling Imitation Learning via Egocentric Video|P236 · EgoMimic: Scaling Imitation Learning via Egocentric Video]]
- [[03 论文卡片/08_数据与遥操作/BridgeData V2 - A Dataset for Robot Learning at Scale|P203 · BridgeData V2: A Dataset for Robot Learning at Scale]]

- 所属方向与专题导读：[[02 研究方向/数据与遥操作]]
- 遥操作路线：[[02 研究方向/机器人遥操作与动作重定向]]
- 数据质量路线：[[02 研究方向/机器人数据采集与数据质量]]

## 来源与核验边界

- 已阅读上述 9 页版本的正文、方法、实验与局限，含附录时一并核对；关键架构或实验表经页面渲染检查，数字位置见各节
- 日期依据官方 arXiv 提交历史，机构依据所读版本署名；正式出处与所读预印本版本分别标明，不用会议日程或演示获奖冒充正式出版
- 论文结果、作者限制和本库研究设想分开；未报告字段不补猜，未核实引用量不填 0
- 代码和数据链接用于核对公开资源，未运行第三方代码、未执行机器人动作；可访问与可完整复现分别评价
- PDF 再分发许可未统一确认，遵循现有忽略规则仅保存本地；代码许可不自动覆盖论文、数据及模型
