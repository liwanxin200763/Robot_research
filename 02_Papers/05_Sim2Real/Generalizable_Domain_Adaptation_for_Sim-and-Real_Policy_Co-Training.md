# Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training

## 基本信息

- 作者：Cheng, Shuo; Ma, Liqian; Chen, Zhenyang; Mandlekar, Ajay; Garrett, Caelan; Xu, Danfei
- 年份：2025
- 会议 / 期刊：NeurIPS
- CCF 等级：A
- DOI：10.52202/085713-0399
- 官方论文：https://proceedings.neurips.cc/paper_files/paper/2025/hash/1185c89347a3f21ffc48c9d083c9437c-Abstract-Conference.html
- 主要分类：Robot Manipulation; Generalization
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

- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：https://proceedings.neurips.cc/paper_files/paper/2025/hash/1185c89347a3f21ffc48c9d083c9437c-Abstract-Conference.html
