# Text-Aware Diffusion for Policy Learning

## 基本信息

- 作者：Luo, Calvin; He, Mandy; Zeng, Zilai; Sun, Chen
- 年份：2024
- 会议 / 期刊：NeurIPS
- CCF 等级：A
- DOI：10.52202/079017-1469 — [DOI](https://doi.org/10.52202/079017-1469)
- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5227ce00add5aa0a12d1c4ee92fcd2dc-Abstract-Conference.html)
- 主要分类：Diffusion / Flow; Reinforcement Learning
- 关键词：Text-conditioned Reward


- 引用量：1
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/06_Diffusion_Flow_IL_RL/Text-Aware_Diffusion_for_Policy_Learning.pdf]]
## 论文定位

这篇论文属于 Diffusion / Flow; Reinforcement Learning 方向，主要讨论机器人策略需要按文字目标学习行为，而奖励设计成本较高。
核心思路是TADPoLe 利用冻结的文本条件模型，为策略学习提供语言相关的信号。
与当前项目的联系：Medium：对未来 VLA 有参考价值，真机双臂需独立验证。

## 核心关键词

Text-conditioned Reward、Diffusion、Flow、Reinforcement Learning

## 快速摘要

### 研究问题

机器人策略需要按文字目标学习行为，而奖励设计成本较高。

### 之前方法的问题

普通扩散生成不能自动判断行为是否符合语言描述。

### 核心思路

TADPoLe 利用冻结的文本条件模型，为策略学习提供语言相关的信号。

### 数据集与评测基准

Meta-World 机器人操作环境。

### 主要结果

作者报告在 Meta-World 任务上有竞争力的表现；具体数字见实验表。

### 为什么重要

可比较语言约束进入奖励还是进入动作生成器。

### 与当前项目的关系

Medium：对未来 VLA 有参考价值，真机双臂需独立验证。

### 主要局限

冻结模型的语言判断可能与真实物理成功不一致。

## 实验与结果

### 数据集与评测基准

Meta-World 机器人操作环境。

### 主要结果

作者报告在 Meta-World 任务上有竞争力的表现；具体数字见实验表。

## 局限与启发

### 主要局限

冻结模型的语言判断可能与真实物理成功不一致。

## 与当前项目的关系

Medium：对未来 VLA 有参考价值，真机双臂需独立验证。

## 来源

- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5227ce00add5aa0a12d1c4ee92fcd2dc-Abstract-Conference.html)
