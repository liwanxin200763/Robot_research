# Robot Policy Learning with Temporal Optimal Transport Reward

## 基本信息

- 作者：Fu, Yuwei; Zhang, Haichao; Wu, Di; Xu, Wei; Boulet, Benoit
- 年份：2024
- 会议 / 期刊：NeurIPS
- CCF 等级：A
- DOI：10.52202/079017-3879 — [DOI](https://doi.org/10.52202/079017-3879)
- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/dcd297696d0bb304ba426b3c5a679c37-Abstract-Conference.html)
- 官方代码：[GitHub](https://github.com/fuyw/TemporalOT)
- 主要分类：Robot Manipulation; Reinforcement Learning
- 关键词：Video Demonstration / Reward Learning


- 引用量：1
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/06_Diffusion_Flow_IL_RL/Robot_Policy_Learning_with_Temporal_Optimal_Transport_Reward.pdf]]
## 论文定位

这篇论文属于 Robot Manipulation; Reinforcement Learning 方向，主要讨论强化学习的奖励设计通常要大量人工工程。
核心思路是Temporal Optimal Transport Reward 把时间顺序纳入示范与策略轨迹的匹配，构造学习奖励。
与当前项目的联系：Medium：双臂轨迹评价可参考，但真实接触仍需验证。

## 核心关键词

Video Demonstration、Reward Learning、Robot Manipulation、Reinforcement Learning

## 快速摘要

### 研究问题

强化学习的奖励设计通常要大量人工工程。

### 之前方法的问题

只比较单帧状态容易忽略示范中的动作时间顺序。

### 核心思路

Temporal Optimal Transport Reward 把时间顺序纳入示范与策略轨迹的匹配，构造学习奖励。

### 主要结果

已核验摘要没有可安全复述的统一量化结果。

### 为什么重要

为长时序操作提供不依赖逐步手写奖励的方向。

### 与当前项目的关系

Medium：双臂轨迹评价可参考，但真实接触仍需验证。

### 主要局限

时间对齐错误可能误导奖励；需审计长任务失败样例。

## 实验与结果

### 主要结果

已核验摘要没有可安全复述的统一量化结果。

## 局限与启发

### 主要局限

时间对齐错误可能误导奖励；需审计长任务失败样例。

## 与当前项目的关系

Medium：双臂轨迹评价可参考，但真实接触仍需验证。

## 来源

- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/dcd297696d0bb304ba426b3c5a679c37-Abstract-Conference.html)
- 官方代码：[GitHub](https://github.com/fuyw/TemporalOT)
