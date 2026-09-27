# SimpleVLA-RL：通过强化学习扩展 VLA 训练

## 基本信息

- 英文标题：SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning
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
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：—
- 引用量来源：未可靠匹配
- 引用量来源链接：—
- 引用量查询日期：2026-09-27
- 引用量状态：待核验
- 排序引用量：—
- 排序引用量来源：未被统一来源可靠收录

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

- [[Octo：开源通用机器人策略]]
- [[OpenVLA：开源视觉—语言—动作模型]]
- [[RDT-1B：面向双臂操作的扩散基础模型]]
- [[从动作 Token 化视角综述 VLA 模型]]
- [[Open X-Embodiment：机器人学习数据集与 RT-X 模型]]
- [[RoboTwin：基于生成式数字孪生的双臂机器人 Benchmark]]
- [[面向具身 AI 的 VLA 模型综述]]
- [[迈向统一理解机器人操作：综合综述]]

## 来源

- 官方论文：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cbfbcb4da14235bd69b134070898ae9d-Abstract-Conference.html)
