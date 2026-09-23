# COMBO-Grasp: Learning Constraint-Based Manipulation for Bimanual Occluded Grasping

## 基本信息

- 年份：2025
- 会议 / 期刊：CoRL
- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)
- 官方论文：https://proceedings.mlr.press/v305/yamada25a.html
- 主要分类：Bimanual Manipulation / Robot Manipulation

## 论文定位

这篇论文属于 Bimanual Manipulation / Robot Manipulation 方向，主要讨论目标抓取位姿可能被障碍物遮挡，单臂难以直接到达。
核心思路是COMBO-Grasp 用两个协调策略处理遮挡抓取，让双臂先调整环境再完成目标抓取。
与当前项目的联系：High：适合普通夹爪双臂的支撑、移动与抓取任务。

## 核心关键词

Bimanual Manipulation、Robot Manipulation、Bimanual

## 快速摘要

### 研究问题

目标抓取位姿可能被障碍物遮挡，单臂难以直接到达。

### 之前方法的问题

只规划目标夹爪的直接抓取，缺少另一只手协助移动物体/障碍物。

### 核心思路

COMBO-Grasp 用两个协调策略处理遮挡抓取，让双臂先调整环境再完成目标抓取。

### 数据集与评测基准

论文的遮挡抓取评测任务；具体平台和基线见实验章节。

### 主要结果

官方摘要报告成功率优于所比较基线，并对未见设置有一定泛化；未给统一数值。

### 为什么重要

展示双臂协作不只是同步抓取，也可以分工解除遮挡。

### 与当前项目的关系

High：适合普通夹爪双臂的支撑、移动与抓取任务。

### 主要局限

需进一步核验复杂杂乱场景与真机接触安全边界。

## 实验与结果

### 数据集与评测基准

论文的遮挡抓取评测任务；具体平台和基线见实验章节。

### 主要结果

官方摘要报告成功率优于所比较基线，并对未见设置有一定泛化；未给统一数值。

## 局限与启发

### 主要局限

需进一步核验复杂杂乱场景与真机接触安全边界。

## 与当前项目的关系

High：适合普通夹爪双臂的支撑、移动与抓取任务。

## 相关论文

- [[ALOHA_Unleashed]]
- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：https://proceedings.mlr.press/v305/yamada25a.html
