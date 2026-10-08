---
paper_id: P026
title: "ECoMEM: Explicit Concept Memory for Memory-Dependent Robot Control"
---

# P026 · ECoMEM: Explicit Concept Memory for Memory-Dependent Robot Control

## 基本信息

- 作者：Yize Liu、Ke Wang、Mac Schwager、Yiqing Xu、Jiajun Wu
- 年份：2026
- 发表 venue：arXiv 预印本
- 论文类型：VLA 方法
- 研究方向：VLA、长程操作、显式记忆
- 关键词：concept memory、VLA、long-horizon manipulation、RoboMME
- 论文链接：https://arxiv.org/abs/2610.00801
- DOI：https://doi.org/10.48550/arXiv.2610.00801
- arXiv：2610.00801
- 项目主页：https://ecomem.github.io/
- 代码：项目页标注 Code · Coming soon
- 本地 PDF：[[00_论文池/PDFs/01_VLA/ECoMEM.pdf|ECoMEM.pdf]]
- 引用量：
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

多步骤操作需要记住已经移动的物体、已完成次数和操作先后顺序；当前画面并不总含这些历史信息。（论文第 1 节）

### 2. 论文要解决的问题

如何把可检查的任务相关概念记忆提供给 VLA，使其依据历史状态控制，而非仅从有限帧猜测进度。（论文第 1 节）

### 3. 之前方法存在的问题

帧采样丢失过去事件，潜在记忆虽可压缩历史却难明确检查所记对象、计数和顺序是否正确。（论文第 1–2 节）

### 4. 核心思路

以 Writer 将感知和状态更新成结构化概念库，再用 Reader 把任务所需概念映射为供 π0.5 使用的记忆 token。（论文第 3 节、图 2）

### 5. 方法与系统结构

概念库覆盖实体／空间、状态／关系、事件／进度和时间／程序四类；Writer 用 OWLv2、SAM2、机器人状态与相机标定产生并更新记录，Reader 为小型 Transformer。任务指令决定查询哪些概念；视觉编码器和 Writer 冻结，Reader、语言骨干及动作专家共同训练。（论文第 3 节）

### 6. 输入信息

相机图像、机器人本体状态、相机标定、语言任务指令与概念历史记录。（论文第 3 节）

### 7. 输出 / 动作表示

Reader 输出条件记忆 token，π0.5 动作专家以 flow matching 生成控制动作；概念库不是直接的机器人动作序列。（论文第 3 节）

### 8. 数据来源与采集方式

RoboMME 的 16 个记忆依赖任务；真机 CupSwitch、ScoopPour 使用 YAM 机械臂，GELLO 收集示范。（论文第 4 节、附录）

### 9. 数据处理与数据增强

Writer 对视频与本体信息抽取实体位置、关系、事件次数和程序状态，任务选择器只读取当前指令需要的概念。论文没有证明概念检测器对任意开放世界物体都可靠。（论文第 3 节）

### 10. 训练方式

在 16 项 RoboMME 任务上联合训练可学习部分，仿真主要实验使用 200k updates；冻结视觉编码器与 Writer。真机在预训练 π0.5 基础上对比较方法微调。（论文第 4 节、附录）

### 11. Benchmark 与实验设置

RoboMME 16 项仿真任务，每设置 50 条验证 episode、3 个随机种子；与帧采样、MemER 等记忆基线比较。真机比较有／无显式记忆的策略。（论文第 4 节、表 1–3）

### 12. 真机实验

CupSwitch 要求按指定次数往返移动，ScoopPour 要求按序重复取豆、倒豆。ECoMEM 成功 68/79；无记忆 π0.5 为 5/58，二者试验数不同且不是逐次配对。（论文第 4 节、表 3）

### 13. 主要实验结果

RoboMME 16 项等权平均成功率 82.42%，强基线 FrameSamp+Modul 为 44.51%，在 15/16 项上领先；PickHighlight 并非最佳，InsertPeg 仅 40.67%。（论文表 1）真机为 86.1%（68/79），无记忆基线 8.6%（5/58）。（论文表 3）

### 14. 消融实验

去除相应概念族后，空间任务成功率 84→18、事件任务 62→14、顺序任务 60→12；去除任务选择或语言 grounding 也显著下降。不同消融对应不同任务，不能把数值当成全基准平均。（论文第 4 节、图表及附录）

### 15. Failure Case

PickHighlight 被 MemER 超过；InsertPeg 成功率低，说明精细执行误差不会仅靠记忆消失。显式概念的错误提取、更新或任务选择亦可能传播到动作，但论文未给所有此类故障的频率。（论文表 1、第 5 节）

### 16. 主要局限

方法依赖预设概念库、外部检测／分割和任务指令解析；对未覆盖概念或感知错误的稳健性尚未由主要实验充分证明。后一判断是本库依据系统依赖关系的分析。（论文第 3–5 节）

### 17. 与已有工作的关系

与 [[02_论文/01_VLA/MemoryVLA - Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation|MemoryVLA]] 的潜在双流记忆不同，ECoMEM 把实体、事件与计数显式记录，便于检查记忆内容；两者评测设置不能直接横向排序。

### 18. 对当前研究方向的价值

为双臂多步骤任务中的“物体在哪里、做到第几步、是否该恢复”提供可追踪状态接口；若迁移到普通夹爪，应重点测概念识别失败和任务切换时的状态一致性。

### 19. 一句话总结

ECoMEM 用结构化概念记忆补足 VLA 的历史状态，在 RoboMME 16 项任务取得 82.42% 平均成功率，并在两类真机重复操作任务达到 68/79 次成功。
