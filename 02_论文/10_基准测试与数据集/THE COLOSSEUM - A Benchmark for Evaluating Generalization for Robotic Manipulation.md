---
paper_id: P006
title: "THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation"
---

# P006 · THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation

## 基本信息

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
- 引用量：193
- 引用量来源：Google Scholar

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

- [[BridgeVLA - Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models]]
- [[Towards a Unified Understanding of Robot Manipulation - A Comprehensive Survey]]

## 来源

- 官方论文：[Robotics Proceedings](https://www.roboticsproceedings.org/rss20/p133.html)
- 项目主页：[项目主页](https://robot-colosseum.github.io/)
