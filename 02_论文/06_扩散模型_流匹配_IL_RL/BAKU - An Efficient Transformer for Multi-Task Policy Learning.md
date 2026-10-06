# BAKU：面向多任务策略学习的高效 Transformer

## 基本信息

- 英文标题：BAKU: An Efficient Transformer for Multi-Task Policy Learning
- 作者：Haldar, Siddhant; Peng, Zhuoran; Pinto, Lerrel
- 年份：2024
- 发表 venue：NeurIPS
- 论文类型：会议论文
- 研究方向：扩散模型 / 流匹配 / IL / RL
- 论文链接：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ff887781480973bd3cb6026feb378d1e-Abstract-Conference.html)
- DOI：10.52202/079017-4484 — [DOI](https://doi.org/10.52202/079017-4484)
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/BAKU.pdf|查看 PDF]]
- 引用量：17
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：A
- 关键词：Action Chunking / Multi-task Policy

## 论文定位

这篇论文属于 Robot Manipulation; Imitation Learning 方向，主要讨论多任务机器人策略通常需要大量专家示范。
核心思路是BAKU 用相对简洁的 Transformer 架构训练多任务机器人策略。
与当前项目的联系：High：双臂示范昂贵，值得比较数据效率。

## 核心关键词

Action Chunking、Multi-task Policy、Robot Manipulation、Imitation Learning

## 快速摘要

### 研究问题

多任务机器人策略通常需要大量专家示范。

### 之前方法的问题

复杂通用策略可能难以在少量示范下稳定学习。

### 核心思路

BAKU 用相对简洁的 Transformer 架构训练多任务机器人策略。

### 主要结果

论文报告 30 项真机操作任务、每项平均约 17 条示范时，成功率达 91%。

### 为什么重要

为小数据多任务操作提供实证基线。

### 与当前项目的关系

High：双臂示范昂贵，值得比较数据效率。

### 主要局限

30 项任务的本体与任务分布未必覆盖本项目的双臂普通夹爪。

## 实验与结果

### 主要结果

论文报告 30 项真机操作任务、每项平均约 17 条示范时，成功率达 91%。

## 局限与启发

### 主要局限

30 项任务的本体与任务分布未必覆盖本项目的双臂普通夹爪。

## 与当前项目的关系

High：双臂示范昂贵，值得比较数据效率。

## 相关论文

- [[SpatialVLA - Exploring Spatial Representations for Visual-Language-Action Models]]
- [[Towards a Unified Understanding of Robot Manipulation - A Comprehensive Survey]]

## 来源

- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ff887781480973bd3cb6026feb378d1e-Abstract-Conference.html)
