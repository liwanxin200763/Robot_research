# SafeBimanual: Diffusion-based trajectory optimization for safe bimanual manipulation

## 基本信息

- 年份：2025
- 会议 / 期刊：CoRL
- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)
- 官方论文：https://proceedings.mlr.press/v305/deng25c.html
- 主要分类：Bimanual Manipulation / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation

## 论文定位

这篇论文属于 Bimanual Manipulation / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论双臂扩散策略生成的动作可能违反安全和协调约束。
核心思路是SafeBimanual 在测试时对预训练扩散策略的轨迹进行优化，加入安全约束。
与当前项目的联系：High：双臂普通夹爪真机部署需要碰撞与工作空间限制。

## 核心关键词

Bimanual Manipulation、Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、Bimanual

## 快速摘要

### 研究问题

双臂扩散策略生成的动作可能违反安全和协调约束。

### 之前方法的问题

训练完成后的策略不一定知道新的障碍物或当前碰撞边界。

### 核心思路

SafeBimanual 在测试时对预训练扩散策略的轨迹进行优化，加入安全约束。

### 数据集与评测基准

双臂扩散策略的测试时轨迹优化任务；具体 benchmark 见论文。

### 主要结果

已核验摘要未提供可安全复述的统一量化结果。

### 为什么重要

将安全约束放在策略与真机控制器之间，便于与现有策略组合。

### 与当前项目的关系

High：双臂普通夹爪真机部署需要碰撞与工作空间限制。

### 主要局限

优化耗时、约束保守程度和任务成功率之间的权衡需实测。

## 实验与结果

### 数据集与评测基准

双臂扩散策略的测试时轨迹优化任务；具体 benchmark 见论文。

### 主要结果

已核验摘要未提供可安全复述的统一量化结果。

## 局限与启发

### 主要局限

优化耗时、约束保守程度和任务成功率之间的权衡需实测。

## 与当前项目的关系

High：双臂普通夹爪真机部署需要碰撞与工作空间限制。

## 来源

- 官方论文：https://proceedings.mlr.press/v305/deng25c.html
