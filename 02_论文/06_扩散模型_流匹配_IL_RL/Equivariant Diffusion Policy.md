---
paper_id: P106
title: "Equivariant Diffusion Policy"
---

# P106 · Equivariant Diffusion Policy

## 基本信息

- 作者：—
- 年份：2024
- 发表 venue：CoRL
- 论文类型：会议论文
- 研究方向：扩散模型 / 流匹配 / IL / RL
- 论文链接：[PMLR](https://proceedings.mlr.press/v270/wang25a.html)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/Equivariant_Diffusion_Policy.pdf|查看 PDF]]
- 引用量：123
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)

## 论文定位

这篇论文属于 Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论扩散策略善于表达多种动作，但少量数据下泛化仍有挑战。
核心思路是Equivariant Diffusion Policy 把空间对称性引入扩散式动作策略。
与当前项目的联系：Medium：可用于双夹爪空间变化实验。

## 核心关键词

Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

扩散策略善于表达多种动作，但少量数据下泛化仍有挑战。

### 之前方法的问题

不利用任务的几何对称性会增加学习样本需求。

### 核心思路

Equivariant Diffusion Policy 把空间对称性引入扩散式动作策略。

### 主要结果

作者报告在真机系统上可用较少示范学到有效策略；具体数值见原文。

### 为什么重要

将几何先验与生成式动作结合。

### 与当前项目的关系

Medium：可用于双夹爪空间变化实验。

### 主要局限

需要核验所假设的对称性在复杂接触和双臂协作中是否成立。

## 实验与结果

### 主要结果

作者报告在真机系统上可用较少示范学到有效策略；具体数值见原文。

## 局限与启发

### 主要局限

需要核验所假设的对称性在复杂接触和双臂协作中是否成立。

## 与当前项目的关系

Medium：可用于双夹爪空间变化实验。

## 相关论文

- [[DiffusionVLA - Scaling Robot Foundation Models via Unified Diffusion and Autoregression]]
- [[Towards a Unified Understanding of Robot Manipulation - A Comprehensive Survey]]
- [[3D Diffuser Actor - Policy Diffusion with 3D Scene Representations]]

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v270/wang25a.html)
