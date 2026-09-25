# SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning

## 基本信息

- 年份：2026
- 会议 / 期刊：ICLR
- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 官方论文：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html)
- 主要分类：VLA / Robot Foundation Models / Robot Manipulation


- 引用量：—
- 引用量来源：未可靠匹配
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/01_VLA/SimpleVLA-RL.pdf]]
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

- [[Octo]]
- [[OpenVLA]]
- [[RDT-1B]]
- [[A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective]]
- [[Open_X-Embodiment]]
- [[RoboTwin]]
- [[A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]]
- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html)
