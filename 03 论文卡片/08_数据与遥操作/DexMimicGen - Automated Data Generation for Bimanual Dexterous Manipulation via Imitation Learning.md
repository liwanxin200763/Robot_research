---
paper_id: P145
title: "DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning"
document_type: "会议论文"
preprint_platform: "arXiv"
first_public_date: "2024-10-31"
first_public_month: "2024-10"
first_public_scope: "arXiv v1 submission history (UTC)"
latest_preprint_date: "2025-03-06"
latest_preprint_version: "v2"
publication_status: "已正式发表"
published_venue: "IEEE ICRA 2025"
affiliations: ["NVIDIA Research", "The University of Texas at Austin", "University of California San Diego"]
metadata_verified_on: "2026-10-17"
metadata_sources: ["https://arxiv.org/abs/2410.24185", "https://arxiv.org/pdf/2410.24185v2", "https://ieeexplore.ieee.org/document/11127809", "https://dexmimicgen.github.io/"]
publication_year: 2025
publisher_indexed_date: "2025-09-02"
conference_month: "2025-05"
arxiv: "2410.24185"
---

# P145 · DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning

## 基本信息

- 作者：Zhenyu Jiang; Yuqi Xie; Kevin Lin; Zhenjia Xu; Weikang Wan; Ajay Mandlekar; Linxi Fan; Yuke Zhu
- 年份：2025
- 发表 venue：ICRA 2025（arXiv 首发于 2024）
- 论文类型：会议论文；示范数据生成框架
- 研究方向：数据与遥操作；双臂灵巧操作
- 关键词：Bimanual Dexterous Manipulation；MimicGen；Imitation Learning；Object-Centric Transformation；Real2Sim2Real
- 论文链接：[arXiv 论文](https://arxiv.org/abs/2410.24185)
- DOI：[10.1109/ICRA55743.2025.11127809](https://doi.org/10.1109/ICRA55743.2025.11127809)
- arXiv：[2410.24185](https://arxiv.org/abs/2410.24185)
- 项目主页：[DexMimicGen](https://dexmimicgen.github.io/)
- 代码：[NVlabs/dexmimicgen](https://github.com/NVlabs/dexmimicgen/)
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/DexMimicGen.pdf|查看 PDF]]
- 引用量：
- 引用量来源：Google Scholar

## 出处与版本

- 文献类型：会议论文
- 预印本平台与编号：[arXiv 2410.24185](https://arxiv.org/abs/2410.24185)
- 首次公开日期：2024-10-31；首次公开月份：2024 年 10 月，依据 arXiv v1 提交历史（UTC）；本字段不宣称已穷尽项目网页或其他平台可能更早的公开记录
- 最近预印本更新：2025-03-06（2025 年 3 月），v2；与首次公开日期分开
- 当前发表状态：已正式发表
- 正式发表出处：[IEEE ICRA 2025](https://ieeexplore.ieee.org/document/11127809)
- 正式出版年份：2025；正式出版月份：待核验；IEEE Xplore 上架日期：2025-09-02
- 会议月份：2025 年 5 月；不是录用通知日期
- 日期与状态说明：IEEE 记录会议日期为 2025-05-19–23，加入 Xplore 日期为 2025-09-02；DOI：10.1109/ICRA55743.2025.11127809；会议月份与数据库上架月份分开记录
- 作者所属机构：NVIDIA Research；The University of Texas at Austin；University of California San Diego
- 机构依据：正文首页脚注署名 NVIDIA Research、UT Austin、UC San Diego；不采用作者当前个人主页上的后续雇主；[对应版本 PDF 首页](https://arxiv.org/pdf/2410.24185v2)
- 项目主页：[作者项目页](https://dexmimicgen.github.io/)
- 官方代码：[作者链接的仓库](https://github.com/NVlabs/dexmimicgen)；入口存在不等于已核实完整实现、模型或许可，开源边界沿用下文说明
- 信息核验日期：2026-10-17；来源为官方版本历史、正文署名和上述正式条目；引用量沿用原 Google Scholar 人工核验规则

## 论文简介

双臂加灵巧手的示范很难采：操作者要同时安排左右臂、手指和交接时机，逐条重做不仅费时，还容易只覆盖少数物体位置。DexMimicGen 从少量已有机器人示范出发，研究怎样在仿真里可靠地扩增，而不是再造一个大型策略模型

流程是“源示范 → 按物体和双臂关系分段 → 在新物体位姿下变换末端轨迹 → 约束同步与先后顺序 → 仿真执行成功才保存”。物体中心变换指物体移动后，相关抓取轨迹也随它一起变换。相较给动作简单加噪，作者显式区分两臂各做各的、共同托举和先交接再行动，解决单臂 MimicGen 不能直接表达的协调问题

60 条源示范生成约 2.1 万条示范，衡量的是数据生成规模，不是 2.1 万次真机成功。下游在这些数据上训练模仿策略；真机 GR-1＋Inspire 的罐子分类中，4 条源示范扩成 40 条成功示范，策略成功率由 0% 到 90%，红蓝两类各测试 10 次，范围仍很窄（§VI-D、图 6）

局限是需要子任务标注、物体位姿、可用仿真资产和控制器，并不能任意拿一段网络视频直接扩增。对我们的机械臂与 DH116，可先借鉴“分段、变换、成功门控”的离线数据设计，用 D435i 估计物体位置；适配多指关节、接触与双臂可达性仍是本项目待验证工作，生成阶段的过滤也不等于部署时能自主失败恢复

## 详细摘要

### 1. 研究背景

双臂加多指灵巧手的同步遥操作负担很高，少量真人示范难以直接训练可靠的视觉策略。仿真中自动扩增真实可执行轨迹可降低采集瓶颈。（全文 §I–II）

### 2. 论文要解决的问题

如何把少量双臂示范转为多初始状态、多任务的操作轨迹，同时保留左右臂异步、协同以及先后顺序约束。（§I、IV）

### 3. 之前方法存在的问题

原 MimicGen 侧重单臂、单条固定子任务顺序，直接复制到双臂会失去异步并行、交接同步与跨臂顺序控制；给原轨迹加噪也不能覆盖新初始状态。（§II–IV、VI-C）

### 4. 核心思路

按每只臂把示范分为平行、协同、顺序三类子任务；在新物体位姿下进行 object-centric SE(3) 轨迹变换，执行成功后才保留生成示范。（§IV，图 2–3）

### 5. 方法与系统结构

每臂各有动作队列，平行子任务异步执行；协同阶段两臂共享变换并同步结束时刻，交接可选择直接 Replay 以免超出运动学限制；顺序阶段以前置/后继约束阻止另一臂提前动作。手指动作相对末端沿用源示范。这里是双臂轨迹数据生成，不是训练两个独立智能体；同步与顺序机制用于避免时序冲突，论文未报告通用碰撞规划或在线失败恢复。（§IV-A–D）

### 6. 输入信息

少量人类操作示范、按臂标出的子任务及参考物体、新仿真场景中的物体位姿和初始机器人状态。（§IV–V）

### 7. 输出 / 动作表示

生成每臂末端动作轨迹及灵巧手关节命令，按控制器转换为机器人执行动作；最终形成可用于 BC-RNN 或 Diffusion Policy 的视觉—动作示范。（§IV–VI）

### 8. 数据来源与采集方式

9 个仿真任务、3 种本体：平行夹爪双 Panda、灵巧手双 Panda、灵巧手 GR-1。论文以 60 条人类源示范生成约 2.1 万条示范；真机 Can Sorting 从 4 条源示范经数字孪生生成 40 条成功示范。每次仿真生成仅保留成功执行；论文没有提供同规模真人数据所需小时或统一生成成本表。（§I、V–VI）

### 9. 数据处理与数据增强

对参考物体位姿及场景初始状态重新采样，以 SE(3) 物体中心变换产生新的末端轨迹；D0/D1/D2 扩大重置分布。多样性以跨任务、本体和 reset distribution 展示，未独立计算 state coverage、action diversity 或每条数据边际价值。（§IV、VI-B/C，表 II）

### 10. 训练方式

数据生成系统不学习轨迹扩增网络；在生成示范上训练 BC-RNN、BC-RNN-GMM 和 Diffusion Policy 等模仿策略，比较 100、500、1000、5000 条示范规模。真机视觉策略采用 Diffusion Policy。（§VI，图 5）

### 11. Benchmark 与实验设置

Robosuite/MuJoCo 的 9 任务和三种本体；以源示范直接训练、Demo-Noise 数据生成、不同数据量、Replay/Transform、顺序约束和策略架构作为对照，报告成功率并对多个种子取平均。（§V–VI，表 I–III）

### 12. 真机实验

Fourier GR-1 搭载双 Inspire 灵巧手、头部和外部 RealSense 相机。先以 RGB-D 和 GroundingDINO 初始化数字孪生物体位姿，仿真生成成功轨迹后传至真机；40 条成功示范训练 Can Sorting 视觉策略，以红/蓝杯各 10 次测试。（§VI-D，图 6）

### 13. 主要实验结果

21K 示范来自 60 条源示范；仿真 Piece Assembly 中源示范训练的 DP 为 3.3±0.9%，生成数据训练为 80.7±0.9%；Can Sorting 0.7±0.9%→97.3±0.9%（表 I）。Demo-Noise 对比中 Piece Assembly 为 12.7±3.4% 对 74.0±2.8%，Pouring 26.7±2.5% 对 79.3±0.9%（表 III）。真机 4 条源示范策略 0%，40 条生成示范策略 90%（§VI-D）。

### 14. 消融实验

协调子任务 Replay 与 Transform：Transport 63.3% 对 46.0%；顺序约束下 Pouring 88.7%，无约束 76.7%（§VI-C）。100→500/1000 条通常改善策略，但 1000→5000 不总增益（图 5）；说明扩增数量并非唯一质量因素。

### 15. Failure Case

生成过程排除未成功执行轨迹；协调轨迹的 Transform 可能超运动学范围，因此交接任务常用 Replay。论文未给出系统化真机失败类型统计，也未实现部署后的在线失败检测/恢复。（§IV-B、VI-C/D）

### 16. 主要局限

库内分析：源示范仍需按臂子任务分段与类型标注；SE(3) 变换和仿真成功门控依赖可知物体位姿、可重置环境及数字孪生精度。真机仅以单一 Can Sorting 任务、少量测试验证，跨未知任务泛化尚未证实。（§IV、VI）

### 17. 与已有工作的关系

继承 MimicGen 的物体中心轨迹重组，但扩展为双臂异步队列、同步协调与跨臂顺序约束；下游使用现有 BC/DP 学习器，而非提出新 VLA。（§II、IV）

### 18. 对当前研究方向的价值

对普通夹爪双臂的数据扩增尤其可借鉴“平行/协调/顺序”划分和物体中心变换；研究执行错误时可进一步收集被过滤的失败样本，检验其对恢复策略的价值。（§IV–VI）

### 19. 一句话总结

DexMimicGen 把少量人类双臂示范按协作结构重组，在仿真和数字孪生中生成可训练的灵巧操作数据。

## 我的阅读笔记

全文依据：本地 PDF §I–VII、图 1–6、表 I–III；ICRA 身份以作者项目页为准。生成机制属于数据扩增，而非按策略边际效用筛选。

## Sim2Real 专题关联

本论文通过数字孪生把 4 条真实源示范扩成 40 条成功轨迹，并在 GR-1 双灵巧手 Can Sorting 真机上测视觉策略（§VI-D）；属于 Real2Sim2Real 数据扩增，不是没有真实源数据的零样本迁移。见 [[02 研究方向/Sim2Real 研究专题|Sim2Real 研究专题]]。
