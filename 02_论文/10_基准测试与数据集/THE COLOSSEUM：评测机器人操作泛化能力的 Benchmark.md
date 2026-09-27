# THE COLOSSEUM：评测机器人操作泛化能力的 Benchmark

## 基本信息

- 英文标题：THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation
- 作者：Wilbert Pumacay; Ishika Singh; Jiafei Duan; Ranjay Krishna; Jesse Thomason; Dieter Fox
- 年份：2024
- 发表 venue：RSS
- 论文类型：Benchmark / Dataset
- 研究方向：基准测试与数据集
- 论文链接：[Robotics Proceedings](https://www.roboticsproceedings.org/rss20/p133.html)
- DOI：—
- arXiv：—
- 项目主页：[项目主页](https://robot-colosseum.github.io/)
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/10_基准测试与数据集/THE_COLOSSEUM.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：26
- 引用量来源：OpenAlex
- 引用量来源链接：https://openalex.org/W4402354166
- 引用量查询日期：2026-09-27
- 排序引用量：26
- 排序引用量来源：OpenAlex

### 出版与分类补充

- 关键词：Benchmark; Generalization; Robot Manipulation; Simulation; Real World

## 论文定位

这篇论文属于 Benchmark / Dataset 方向，主要讨论操作策略若只在接近训练条件的环境中评测，难以判断其鲁棒性。
核心思路是THE COLOSSEUM 通过受控环境扰动对策略进行压力测试。
与当前项目的联系：Medium：适合构建本项目的分布外评测，但需匹配实际传感器和夹爪。

## 核心关键词

Benchmark、Generalization、Robot Manipulation、Simulation、Real World、Dataset、Environmental perturbation benchmark

## 快速摘要

### 研究问题

操作策略若只在接近训练条件的环境中评测，难以判断其鲁棒性。

### 核心思路

THE COLOSSEUM 通过受控环境扰动对策略进行压力测试。

### 数据集与评测基准

THE COLOSSEUM 基准；具体扰动维度和策略清单需核对正文。

### 主要结果

官方摘要报告，仿真扰动结果与相似真实扰动实验存在相关性，调整后的 R² = 0.614。

### 为什么重要

可帮助设计跨光照、外观和几何变化的泛化评测。

### 与当前项目的关系

Medium：适合构建本项目的分布外评测，但需匹配实际传感器和夹爪。

### 主要局限

相关性并不意味着单个策略的真实成功率可由仿真精确预测。

## 实验与结果

### 数据集与评测基准

THE COLOSSEUM 基准；具体扰动维度和策略清单需核对正文。

### 主要结果

官方摘要报告，仿真扰动结果与相似真实扰动实验存在相关性，调整后的 R² = 0.614。

## 局限与启发

### 主要局限

相关性并不意味着单个策略的真实成功率可由仿真精确预测。

## 与当前项目的关系

Medium：适合构建本项目的分布外评测，但需匹配实际传感器和夹爪。

## 相关论文

- [[BridgeVLA：通过输入—输出对齐高效学习三维操作]]
- [[迈向统一理解机器人操作：综合综述]]

## 来源

- 官方论文：[Robotics Proceedings](https://www.roboticsproceedings.org/rss20/p133.html)
- 项目主页：[项目主页](https://robot-colosseum.github.io/)
