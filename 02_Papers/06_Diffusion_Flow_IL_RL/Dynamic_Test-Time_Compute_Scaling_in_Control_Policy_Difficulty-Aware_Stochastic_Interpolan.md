# Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy

## 基本信息

- 作者：Chun, Inkook; Lee, Seungjae; Albergo, Michael; Xie, Saining; Vanden-Eijnden, Eric
- 年份：2025
- 会议 / 期刊：NeurIPS
- CCF 等级：A
- DOI：10.52202/085713-1714
- 官方论文：https://proceedings.neurips.cc/paper_files/paper/2025/hash/49eadcc4a329fc6b74b9f8a82b78cbc3-Abstract-Conference.html
- 主要分类：Diffusion / Flow; Robot Manipulation
- 关键词：Stochastic Interpolant / Efficiency

## 论文定位

这篇论文属于 Diffusion / Flow; Robot Manipulation 方向，主要讨论扩散和 Flow Policy 能生成复杂动作，但每次推理成本较高。
核心思路是DA-SIP 根据当前控制难度动态调整测试时计算量。
与当前项目的联系：High：动作频率和失败风险都受推理延迟影响。

## 核心关键词

Stochastic Interpolant、Efficiency、Diffusion、Flow、Robot Manipulation

## 快速摘要

### 研究问题

扩散和 Flow Policy 能生成复杂动作，但每次推理成本较高。

### 之前方法的问题

所有状态都用同样计算量会浪费简单动作的时间。

### 核心思路

DA-SIP 根据当前控制难度动态调整测试时计算量。

### 主要结果

论文报告在多项操作任务中总计算时间减少约 2.6–4.4 倍；具体成功率权衡见原文。

### 为什么重要

为双臂真机部署提供按难度分配算力的思路。

### 与当前项目的关系

High：动作频率和失败风险都受推理延迟影响。

### 主要局限

难度估计错误可能使困难接触动作获得不足计算。

## 实验与结果

### 主要结果

论文报告在多项操作任务中总计算时间减少约 2.6–4.4 倍；具体成功率权衡见原文。

## 局限与启发

### 主要局限

难度估计错误可能使困难接触动作获得不足计算。

## 与当前项目的关系

High：动作频率和失败风险都受推理延迟影响。

## 来源

- 官方论文：https://proceedings.neurips.cc/paper_files/paper/2025/hash/49eadcc4a329fc6b74b9f8a82b78cbc3-Abstract-Conference.html
