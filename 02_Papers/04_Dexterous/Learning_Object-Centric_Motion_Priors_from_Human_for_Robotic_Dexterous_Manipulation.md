# Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation

## 基本信息

- 年份：2026
- 会议 / 期刊：AAAI
- CCF 等级：A
- 官方论文：[AAAI](https://ojs.aaai.org/index.php/AAAI/article/download/38892/42854)
- 主要分类：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 关键词：Dexterous Manipulation; Human Demonstrations / Motion Prior


- 引用量：—
- 引用量来源：未可靠匹配
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/04_Dexterous/Learning_Object-Centric_Motion_Priors_from_Human_for_Robotic_Dexterous_Manipulation.pdf]]
## 论文定位

这篇论文属于 A (CCF 7th edition; venue category not independently extracted from official PDF) 方向，主要讨论多指灵巧手操作不同物体时，任务奖励设计和跨手型泛化都很难。
核心思路是从人—物交互数据学习物体运动先验，预测未来物体状态，再把它用于强化学习奖励。
与当前项目的联系：Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 核心关键词

Dexterous Manipulation、Human Demonstrations、Motion Prior、venue category not independently extracted from official PDF)、Dexterous Hand

## 快速摘要

### 研究问题

多指灵巧手操作不同物体时，任务奖励设计和跨手型泛化都很难。

### 之前方法的问题

只模仿人手轨迹，难以把物体未来状态变成通用训练目标。

### 核心思路

从人—物交互数据学习物体运动先验，预测未来物体状态，再把它用于强化学习奖励。

### 输入

官方摘要给出任务/数据类型；具体模型张量与接口需核对方法章节。

### 输出与动作

官方摘要未明确列出完整控制接口；需核对论文方法或代码。

### 数据集与评测基准

三类灵巧操作任务；具体数据集见官方论文。

### 主要结果

官方 AAAI 摘要报告三类仿真与真机任务上的成功率和新物体泛化优于对比方法，并展示跨机械手部署；摘要未给统一数值。

### 为什么重要

提出“预测物体状态作为奖励”的路线，可与普通夹爪任务中的目标状态验证比较。

### 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 方法概览

任务输入 → 从人—物交互数据学习物体运动先验，预测未来物体状态，再把它用于强化学习奖励 → 官方摘要未明确列出完整控制接口；需核对论文方法或代码。

## 实验与结果

### 数据集与评测基准

三类灵巧操作任务；具体数据集见官方论文。

### 主要结果

官方 AAAI 摘要报告三类仿真与真机任务上的成功率和新物体泛化优于对比方法，并展示跨机械手部署；摘要未给统一数值。

## 局限与启发

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 来源

- 官方论文：[AAAI](https://ojs.aaai.org/index.php/AAAI/article/download/38892/42854)
