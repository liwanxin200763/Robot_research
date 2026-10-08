---
paper_id: P041
title: "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning"
---

# P041 · SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning

## 基本信息

- 作者：—
- 年份：2026
- 发表 venue：ICLR
- 论文类型：会议论文
- 研究方向：VLA
- 论文链接：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/01_VLA/SimpleVLA-RL.pdf|查看 PDF]]
- 引用量：167
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)

## 论文定位

这篇论文属于 VLA / Robot Foundation Models / Robot Manipulation 方向，主要讨论预训练 VLA 在新操作任务上仍需更有效的策略改进。
核心思路是SimpleVLA-RL 针对 VLA 设计高效强化学习与探索机制，继续优化操作策略。
与当前项目的联系：High：双臂真机可关注安全约束下的策略改善。

## 核心关键词

VLA、Robot Foundation Models、Robot Manipulation

## 快速摘要

### 研究问题

预训练 VLA 在新操作任务上仍需更有效的策略改进。

### 之前方法的问题

只做监督微调可能难利用真实成功/失败反馈。

### 核心思路

SimpleVLA-RL 针对 VLA 设计高效强化学习与探索机制，继续优化操作策略。

### 数据集与评测基准

LIBERO、RoboTwin 与真机任务。

### 主要结果

作者报告 LIBERO 上达到先进水平，在 RoboTwin 和真机任务上优于所比较方法；完整数值见论文表格。

### 为什么重要

为 VLA 从示范学习走向结果反馈优化提供基线。

### 与当前项目的关系

High：双臂真机可关注安全约束下的策略改善。

### 主要局限

真机 RL 的数据成本、失败代价和安全边界必须单独评估。

## 实验与结果

### 数据集与评测基准

LIBERO、RoboTwin 与真机任务。

### 主要结果

作者报告 LIBERO 上达到先进水平，在 RoboTwin 和真机任务上优于所比较方法；完整数值见论文表格。

## 局限与启发

### 主要局限

真机 RL 的数据成本、失败代价和安全边界必须单独评估。

## 与当前项目的关系

High：双臂真机可关注安全约束下的策略改善。

## 相关论文

- [[Octo - An Open-Source Generalist Robot Policy]]
- [[OpenVLA - An Open-Source Vision-Language-Action Model]]
- [[RDT-1B - a Diffusion Foundation Model for Bimanual Manipulation]]
- [[A Survey on Vision-Language-Action Models - An Action Tokenization Perspective]]
- [[Open X-Embodiment - Robotic Learning Datasets and RT-X Models]]
- [[RoboTwin - Dual-Arm Robot Benchmark with Generative Digital Twins]]
- [[A Survey on Vision-Language-Action Models for Embodied AI]]
- [[Towards a Unified Understanding of Robot Manipulation - A Comprehensive Survey]]

## 来源

- 官方论文：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html)
