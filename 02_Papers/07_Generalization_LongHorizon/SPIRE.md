# SPIRE: Synergistic Planning, Imitation, and Reinforcement Learning for Long-Horizon Manipulation

## 基本信息

- 年份：2024
- 会议 / 期刊：CoRL
- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)
- 官方论文：[PMLR](https://proceedings.mlr.press/v270/zhou25a.html)
- 主要分类：Imitation Learning / Diffusion / Flow Matching / Robot Manipulation


- 引用量：1
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/07_Generalization_LongHorizon/SPIRE.pdf]]
## 论文定位

这篇论文属于 Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论复杂操作任务需要既能规划步骤，又能执行可靠动作。
核心思路是SPIRE 先用 Task and Motion Planning（TAMP）分解任务，再将学习策略用于具体执行。
与当前项目的联系：High：双臂长任务可测试分解与执行后检查。

## 核心关键词

Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

复杂操作任务需要既能规划步骤，又能执行可靠动作。

### 之前方法的问题

只用模仿学习或强化学习，可能难以组织长时序任务。

### 核心思路

SPIRE 先用 Task and Motion Planning（TAMP）分解任务，再将学习策略用于具体执行。

### 主要结果

作者报告相对其他结合模仿学习、强化学习与规划的方法取得更好表现；数字见原文。

### 为什么重要

提供规划与学习策略组合的系统基线。

### 与当前项目的关系

High：双臂长任务可测试分解与执行后检查。

### 主要局限

规划模型与真实接触差异可能造成执行偏差。

## 实验与结果

### 主要结果

作者报告相对其他结合模仿学习、强化学习与规划的方法取得更好表现；数字见原文。

## 局限与启发

### 主要局限

规划模型与真实接触差异可能造成执行偏差。

## 与当前项目的关系

High：双臂长任务可测试分解与执行后检查。

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v270/zhou25a.html)
