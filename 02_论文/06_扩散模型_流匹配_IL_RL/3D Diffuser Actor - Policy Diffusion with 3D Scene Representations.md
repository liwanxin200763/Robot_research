---
paper_id: P097
title: "3D Diffuser Actor: Policy Diffusion with 3D Scene Representations"
---

# P097 · 3D Diffuser Actor: Policy Diffusion with 3D Scene Representations

## 基本信息

- 作者：—
- 年份：2024
- 发表 venue：CoRL
- 论文类型：会议论文
- 研究方向：扩散模型 / 流匹配 / IL / RL
- 论文链接：[PMLR](https://proceedings.mlr.press/v270/ke25a.html)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/3D_Diffuser_Actor.pdf|查看 PDF]]
- 引用量：4
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)

## 论文定位

这篇论文属于 Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论机器人动作有多种合理解，二维图像策略对三维几何理解不足。
核心思路是3D Diffuser Actor 在三维场景表示上生成动作，并通过扩散模型刻画多种可行轨迹。
与当前项目的联系：High：可为双普通夹爪的三维目标位姿生成提供基线。

## 核心关键词

Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

机器人动作有多种合理解，二维图像策略对三维几何理解不足。

### 之前方法的问题

直接回归动作或只用二维表示，可能难以表达多模态三维操作。

### 核心思路

3D Diffuser Actor 在三维场景表示上生成动作，并通过扩散模型刻画多种可行轨迹。

### 主要结果

论文报告与二维表示、回归及其他设计的消融比较，完整数字应以原论文表格为准。

### 为什么重要

是比较三维感知与生成式动作的基础方法。

### 与当前项目的关系

High：可为双普通夹爪的三维目标位姿生成提供基线。

### 主要局限

摘要不足以判断不同真机接触和双臂协调任务的完整覆盖。

## 实验与结果

### 主要结果

论文报告与二维表示、回归及其他设计的消融比较，完整数字应以原论文表格为准。

## 局限与启发

### 主要局限

摘要不足以判断不同真机接触和双臂协调任务的完整覆盖。

## 与当前项目的关系

High：可为双普通夹爪的三维目标位姿生成提供基线。

## 相关论文

- [[BridgeVLA - Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models]]
- [[DiffusionVLA - Scaling Robot Foundation Models via Unified Diffusion and Autoregression]]
- [[VidMan - Exploiting Implicit Dynamics from Video Diffusion Model for Effective Robot Manipulation]]
- [[AnyBimanual - Transferring Unimanual Policy for General Bimanual Manipulation]]
- [[A Survey on Vision-Language-Action Models for Embodied AI]]
- [[Towards a Unified Understanding of Robot Manipulation - A Comprehensive Survey]]
- [[Equivariant Diffusion Policy]]

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v270/ke25a.html)
