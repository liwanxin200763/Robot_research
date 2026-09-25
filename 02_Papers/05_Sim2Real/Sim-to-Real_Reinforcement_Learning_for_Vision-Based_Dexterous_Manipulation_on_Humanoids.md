# Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids

## 基本信息

- 年份：2025
- 会议 / 期刊：CoRL
- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)
- 官方论文：[PMLR](https://proceedings.mlr.press/v305/lin25c.html)
- 主要分类：Dexterous Manipulation / Dexterous Hand / Robot Manipulation


- 引用量：—
- 引用量来源：未可靠匹配
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/05_Sim2Real/Sim-to-Real_Reinforcement_Learning_for_Vision-Based_Dexterous_Manipulation_on_Humanoids.pdf]]
## 论文定位

这篇论文属于 Dexterous Manipulation / Dexterous Hand / Robot Manipulation 方向，主要讨论人形机器人多指操作的控制维度高，真机直接强化学习成本大。
核心思路是在仿真中训练视觉条件强化学习策略，再迁移到人形机器人完成抓取、搬箱等灵巧任务。
与当前项目的联系：Medium：可借鉴迁移流程，但人形灵巧手与普通夹爪差异较大。

## 核心关键词

Dexterous Manipulation、Dexterous Hand、Robot Manipulation

## 快速摘要

### 研究问题

人形机器人多指操作的控制维度高，真机直接强化学习成本大。

### 之前方法的问题

仿真策略可能因视觉、动力学和接触差异在真机失败。

### 核心思路

在仿真中训练视觉条件强化学习策略，再迁移到人形机器人完成抓取、搬箱等灵巧任务。

### 数据集与评测基准

论文报告 grasp-and-reach、box lift 等三项任务。

### 主要结果

已核验摘要未给可安全复述的统一量化成功率。

### 为什么重要

为接触密集任务的 Sim2Real 训练流程提供参照。

### 与当前项目的关系

Medium：可借鉴迁移流程，但人形灵巧手与普通夹爪差异较大。

### 主要局限

不能从人形任务结果直接推断双臂普通夹爪表现。

## 实验与结果

### 数据集与评测基准

论文报告 grasp-and-reach、box lift 等三项任务。

### 主要结果

已核验摘要未给可安全复述的统一量化成功率。

## 局限与启发

### 主要局限

不能从人形任务结果直接推断双臂普通夹爪表现。

## 与当前项目的关系

Medium：可借鉴迁移流程，但人形灵巧手与普通夹爪差异较大。

## 相关论文

- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v305/lin25c.html)
