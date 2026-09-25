# Rapidly Adapting Policies to the Real-World via Simulation-Guided Fine-Tuning

## 基本信息

- 年份：2025
- 会议 / 期刊：ICLR
- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 官方论文：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e68274fc4f158dbcbd4dddc672f7ee9c-Abstract-Conference.html)
- 主要分类：Dexterous Manipulation / Dexterous Hand / Robot Manipulation


- 引用量：—
- 引用量来源：未可靠匹配
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/05_Sim2Real/Rapidly_Adapting_Policies_to_the_Real-World_via_Simulation-Guided_Fine-Tuning.pdf]]
## 论文定位

这篇论文属于 Dexterous Manipulation / Dexterous Hand / Robot Manipulation 方向，主要讨论机器人策略泛化需要大量高质量真实数据。
核心思路是Simulation-Guided Fine-Tuning 从物理仿真提取结构先验，加速真机策略适配。
与当前项目的联系：High：双臂普通夹爪的真实示范预算有限。

## 核心关键词

Dexterous Manipulation、Dexterous Hand、Robot Manipulation

## 快速摘要

### 研究问题

机器人策略泛化需要大量高质量真实数据。

### 之前方法的问题

普通微调方法在真机新任务上仍需要较多示范。

### 核心思路

Simulation-Guided Fine-Tuning 从物理仿真提取结构先验，加速真机策略适配。

### 主要结果

作者报告所需真实样本最多减少约一个数量级，并优于基线微调方法；具体任务见论文。

### 为什么重要

提供小数据真机适配的可比较路线。

### 与当前项目的关系

High：双臂普通夹爪的真实示范预算有限。

### 主要局限

仿真先验对接触和相机变化的稳定性需在目标硬件验证。

## 实验与结果

### 主要结果

作者报告所需真实样本最多减少约一个数量级，并优于基线微调方法；具体任务见论文。

## 局限与启发

### 主要局限

仿真先验对接触和相机变化的稳定性需在目标硬件验证。

## 与当前项目的关系

High：双臂普通夹爪的真实示范预算有限。

## 来源

- 官方论文：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e68274fc4f158dbcbd4dddc672f7ee9c-Abstract-Conference.html)
