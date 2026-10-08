---
paper_id: P123
title: "FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation"
---

# P123 · FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation

## 基本信息

- 作者：Ganlong Zhao、Zijia Tang、Xingping Chen、Zhanghui Kuang、Ye Tian、Guanbin Li
- 年份：2026
- 发表 venue：CVPR 2026
- 论文类型：方法与机器人系统
- 研究方向：失败检测、机器人操作恢复
- 关键词：in-distribution correction、out-of-distribution reset、failure monitoring
- 论文链接：https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_FLARE_A_Failure-Aware_Framework_for_Autonomous_Correction_and_Recovery_in_CVPR_2026_paper.html
- DOI：https://doi.org/10.48550/arXiv.2608.26645
- arXiv：2608.26645
- 项目主页：
- 代码：
- 本地 PDF：[[00_论文池/PDFs/07_泛化与长程任务/FLARE_Recovery.pdf|FLARE_Recovery.pdf]]
- 引用量：8
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

操作失败有轻微姿态偏移，也有物体或场景已经被破坏两种不同情形；统一“再试一次”很难有效。（第 1 节）

### 2. 论文要解决的问题

区分可直接纠正的分布内偏差与需要先重置场景的分布外失败，并自动选用相应技能。（第 1 节）

### 3. 之前方法存在的问题

通用策略对失败状态缺少训练；简单重试无法复原对象，纯人工接管也限制扩展性。（第 2 节）

### 4. 核心思路

对轻微偏差训练 bridging correction，对场景改变学习 reset skill；在线监测器决定继续任务或先复原对象。（第 3 节）

### 5. 方法与系统结构

对 ID 姿态偏差，使用扰动与桥接示范增强 π0.5；对 OOD 场景失败，离线多模态模型分析失败视频，确定需重置的对象和时机，并用少量人工示范训练 reset skill。在线多模态监测在任务策略与 reset skill 间切换；没有跨任务长期失败记忆。（第 3 节、图 2）

### 6. 输入信息

任务指令、视觉和本体观测、在线监测判断；离线还读取失败视频。没有显式 command 与实际关节执行残差字段。（第 3 节）

### 7. 输出 / 动作表示

π0.5 连续操作动作或对象 reset skill 动作；reset 后再运行原任务，但论文没有统一证明每次复原后的语义目标已被充分验证。（第 3 节）

### 8. 数据来源与采集方式

九项模拟操作任务和单 Piper 真机任务；每种需重置对象采集约 10–20 条人工示范。（第 4 节）

### 9. 数据处理与数据增强

ID 数据通过姿态扰动与 bridging trajectory 扩增，OOD 恢复数据以对象重置示范和增强构建。（第 3 节）

### 10. 训练方式

基于 π0.5 微调任务纠错策略与 reset skill；多模态模型离线提取失败类型，在线监测器选技能。（第 3 节）

### 11. Benchmark 与实验设置

九项模拟任务比较 π0.5、Phoenix 等，评估最终完成率以及失败识别和 reset 的贡献。（第 4 节）

### 12. 真机实验

单 Piper 任务各 40 次测试：blocks 62.5%→75%，U-shape 45%→55%；某些物体重置仍困难，如 coffee pod 24%、U-block 20%。（第 4 节）

### 13. 主要实验结果

模拟九任务平均成功率 84.0%，Phoenix 为 57.8%，相对 π0.5 提高 11.8 个百分点；在线 ID/OOD 判断准确率约 88%–96%。（第 4 节、主结果表）

### 14. 消融实验

对比只做 ID 纠错、只用 reset 及完整框架，显示两种恢复分支互补；额外失败示范与增强影响效果。（第 4 节、消融表）

### 15. Failure Case

硬物或狭窄空间重置仍失败；监测器若把场景破坏误判成普通姿态偏差，就可能错误重试。（第 4 节）

### 16. 主要局限

**环境动态类型：**弱动态；机器人失败导致场景破坏，D0/D1 是初始状态随机化，不是执行中独立运动目标。

**失败闭环覆盖：**在线监测识别失败并粗分 ID 姿态偏差/OOD 场景破坏，选择重试或 reset skill，执行后续接原任务；任务成功率检验整体效果。训练期从失败视频学习技能，但没有持久保存细粒度原因与每次恢复结果的 Failure Memory。

作者提出更灵巧的恢复技能为后续工作。按本库分析，任务多为初态随机化而非外部持续运动目标；没有保存失败原因—恢复结果的可检索长期记忆，也没有真机双臂恢复。

### 17. 与已有工作的关系

相较 [[02_论文/07_泛化与长程任务/Recova - Agent-Guided Failure Recovery for Autonomous Robotic Manipulation|Recova]] 的双臂任务与持续接管，FLARE 更明确地区分姿态纠错和场景重置两级恢复。

### 18. 对当前研究方向的价值

可作 Failure Detection / Recovery 的分支选择基线；对 Failure Memory 的启发是记录“判定为 ID/OOD—所选动作—复原结果”，并检验错误诊断代价。这些持久记录并非本文机制。

### 19. 一句话总结

FLARE 把轻微偏差纠错与场景破坏重置分开处理，在模拟和单臂真机提升了失败后任务完成率。
