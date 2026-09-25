# Self-Correcting Robot Manipulation via Gaussian-Splatted Foresight

## 基本信息

- 年份：2025
- 会议 / 期刊：AAAI
- CCF 等级：A
- 官方论文：[AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/34866)
- 主要分类：Robot Manipulation
- 关键词：Failure Recovery / 3D Gaussian Splatting


- 引用量：0
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/07_Generalization_LongHorizon/Self-Correcting_Robot_Manipulation_via_Gaussian-Splatted_Foresight.pdf]]
## 论文定位

这篇论文属于 Robot Manipulation 方向，主要讨论策略执行后可能没有达到预测的场景状态，却仍继续下一步。
核心思路是利用 Gaussian Splatting 预测下一场景，将真实观测与预测比较，必要时回退并修正动作；与 PerACT 结合。
与当前项目的联系：Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 核心关键词

Failure Recovery、3D Gaussian Splatting、Robot Manipulation

## 快速摘要

### 研究问题

策略执行后可能没有达到预测的场景状态，却仍继续下一步。

### 之前方法的问题

缺少可靠的执行结果检查会让局部误差在长任务中累积。

### 核心思路

利用 Gaussian Splatting 预测下一场景，将真实观测与预测比较，必要时回退并修正动作；与 PerACT 结合。

### 输入

官方摘要给出任务/数据类型；具体模型张量与接口需核对方法章节。

### 输出与动作

官方摘要未明确列出完整控制接口；需核对论文方法或代码。

### 数据集与评测基准

RLBench：10 项任务、166 种变化。

### 主要结果

AAAI 官方摘要报告在 RLBench 10 项任务、166 种变化上，平均成功率比所比较方法高 12.0 个百分点。

### 为什么重要

直接对应项目中的动作后验证与失败恢复。

### 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 方法概览

任务输入 → 利用 Gaussian Splatting 预测下一场景，将真实观测与预测比较，必要时回退并修正动作；与 PerACT 结合 → 官方摘要未明确列出完整控制接口；需核对论文方法或代码。

## 实验与结果

### 数据集与评测基准

RLBench：10 项任务、166 种变化。

### 主要结果

AAAI 官方摘要报告在 RLBench 10 项任务、166 种变化上，平均成功率比所比较方法高 12.0 个百分点。

## 局限与启发

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 来源

- 官方论文：[AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/34866)
