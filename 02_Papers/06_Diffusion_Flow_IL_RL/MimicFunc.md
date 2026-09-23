# MimicFunc: Imitating Tool Manipulation from a Single Human Video via Functional Correspondence

## 基本信息

- 年份：2025
- 会议 / 期刊：CoRL
- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)
- 官方论文：https://proceedings.mlr.press/v305/tang25a.html
- 主要分类：Imitation Learning / Diffusion / Flow Matching / Robot Manipulation

## 论文定位

这篇论文属于 Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论从一段人类工具操作视频迁移到几何形状不同的新工具仍很困难。
核心思路是MimicFunc 用三维功能关键点建立 function frame，使机器人从单段 RGB-D 人类视频迁移工具操作。
与当前项目的联系：Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 核心关键词

Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

从一段人类工具操作视频迁移到几何形状不同的新工具仍很困难。

### 之前方法的问题

只按外形对齐的模仿方法难以抓住工具的功能对应关系。

### 核心思路

MimicFunc 用三维功能关键点建立 function frame，使机器人从单段 RGB-D 人类视频迁移工具操作。

### 输入

官方摘要给出任务/数据类型；具体模型张量与接口需核对方法章节。

### 输出与动作

官方摘要未明确列出完整控制接口；需核对论文方法或代码。

### 数据集与评测基准

单段 RGB-D 人类视频与新工具操作任务。

### 主要结果

CoRL 官方摘要报告能操作功能相同但外形不同的新工具，还可生成训练视觉运动策略的 rollout；未给统一成功率。

### 为什么重要

为 Human Video → Robot Action 提供功能对齐思路，普通夹爪适配仍需验证。

### 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 方法概览

任务输入 → MimicFunc 用三维功能关键点建立 function frame，使机器人从单段 RGB-D 人类视频迁移工具操作 → 官方摘要未明确列出完整控制接口；需核对论文方法或代码。

## 实验与结果

### 数据集与评测基准

单段 RGB-D 人类视频与新工具操作任务。

### 主要结果

CoRL 官方摘要报告能操作功能相同但外形不同的新工具，还可生成训练视觉运动策略的 rollout；未给统一成功率。

## 局限与启发

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 来源

- 官方论文：https://proceedings.mlr.press/v305/tang25a.html
