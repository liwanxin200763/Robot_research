# 面向仿真与真实策略联合训练的可泛化域适应

## 基本信息

- 英文标题：Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training
- 作者：Cheng, Shuo; Ma, Liqian; Chen, Zhenyang; Mandlekar, Ajay; Garrett, Caelan; Xu, Danfei
- 年份：2025
- 发表 venue：NeurIPS
- 论文类型：会议论文
- 研究方向：仿真到真实
- 论文链接：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/1185c89347a3f21ffc48c9d083c9437c-Abstract-Conference.html)
- DOI：10.52202/085713-0399 — [DOI](https://doi.org/10.52202/085713-0399)
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/05_仿真到真实_Sim2Real/Generalizable_Domain_Adaptation_for_Sim-and-Real_Policy_Co-Training.pdf|查看 PDF]]
- 引用量：16
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：A
- 关键词：Sim-to-Real / Behavior Cloning

## 论文定位

这篇论文属于 Robot Manipulation; Generalization 方向，主要讨论真机示范采集成本高，但只靠仿真训练又难泛化到现实。
核心思路是联合训练仿真和少量真实机器人数据，并做域适配，学习更可迁移的操作策略。
与当前项目的联系：High：项目需要以有限真机数据训练双臂策略。

## 核心关键词

Sim-to-Real、Behavior Cloning、Robot Manipulation、Generalization

## 快速摘要

### 研究问题

真机示范采集成本高，但只靠仿真训练又难泛化到现实。

### 之前方法的问题

仿真与真实数据分布不同，简单混合训练可能利用不好少量真机样本。

### 核心思路

联合训练仿真和少量真实机器人数据，并做域适配，学习更可迁移的操作策略。

### 主要结果

作者报告在挑战性真机任务上成功率最高提升约 30%；具体比较条件见正文。

### 为什么重要

帮助设计合成数据与真实示范的使用比例。

### 与当前项目的关系

High：项目需要以有限真机数据训练双臂策略。

### 主要局限

不同机器人与任务的 Sim2Real 差异需独立测量。

## 实验与结果

### 主要结果

作者报告在挑战性真机任务上成功率最高提升约 30%；具体比较条件见正文。

## 局限与启发

### 主要局限

不同机器人与任务的 Sim2Real 差异需独立测量。

## 与当前项目的关系

High：项目需要以有限真机数据训练双臂策略。

## 相关论文

- [[Towards a Unified Understanding of Robot Manipulation - A Comprehensive Survey]]

## 来源

- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/1185c89347a3f21ffc48c9d083c9437c-Abstract-Conference.html)
