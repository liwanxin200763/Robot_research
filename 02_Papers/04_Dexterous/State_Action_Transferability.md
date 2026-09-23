# Evaluating the Effect of State and Action Selection on In-Hand Manipulation Performance for Transferability

## 基本信息

- 作者：Nigel Swenson; Jeremiah Goddard; Xiaoli Z. Fern; Ravi Balasubramanian; Cindy Grimm
- 年份：2025
- 会议 / 期刊：RA-L
- 官方论文：https://ieeexplore.ieee.org/document/10955245/
- 主要分类：Dexterous
- 关键词：Dexterous; Sim2Real; Reinforcement Learning; Cross-Embodiment

## 论文定位

这篇论文属于 Dexterous 方向，主要讨论灵巧手策略要跨仿真/现实和不同手型迁移。
核心思路是比较不同 State Space 与 Action Space 的选择，检验其对两类迁移的影响。
与当前项目的联系：Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 核心关键词

Dexterous、Sim2Real、Reinforcement Learning、Cross-Embodiment、State、action-space transferability

## 快速摘要

### 研究问题

灵巧手策略要跨仿真/现实和不同手型迁移。

### 之前方法的问题

域随机化等方法不能完全弥合观测与动作定义造成的差异。

### 核心思路

比较不同 State Space 与 Action Space 的选择，检验其对两类迁移的影响。

### 输入

官方摘要给出任务/数据类型；具体模型张量与接口需核对方法章节。

### 输出与动作

官方摘要未明确列出完整控制接口；需核对论文方法或代码。

### 数据集与评测基准

两项手内操作任务；具体机器人与设置见 RA-L 正文。

### 主要结果

IEEE RA-L 摘要报告：在两项示例操作任务中，去除手型特有信息的较小状态空间更利于迁移。

### 为什么重要

提醒本项目先确定哪些状态和动作维度可跨两只夹爪复用。

### 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 方法概览

任务输入 → 比较不同 State Space 与 Action Space 的选择，检验其对两类迁移的影响 → 官方摘要未明确列出完整控制接口；需核对论文方法或代码。

## 实验与结果

### 数据集与评测基准

两项手内操作任务；具体机器人与设置见 RA-L 正文。

### 主要结果

IEEE RA-L 摘要报告：在两项示例操作任务中，去除手型特有信息的较小状态空间更利于迁移。

## 局限与启发

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 来源

- 官方论文：https://ieeexplore.ieee.org/document/10955245/
