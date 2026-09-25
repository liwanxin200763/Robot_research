# Constrained Bimanual Planning with Analytic Inverse Kinematics

## 基本信息

- 作者：Thomas Cohn; Seiji Shaw; Max Simchowitz; Russ Tedrake
- 年份：2024
- 会议 / 期刊：ICRA
- 官方论文：[官方论文](https://ieeexplore.ieee.org/document/10610675/)
- 项目主页：[项目主页](https://tommycohn.com/Bimanual-Web/index.html)
- 官方代码：[GitHub](https://github.com/cohnt/constrained-bimanual-planning-example)
- 主要分类：Bimanual
- 关键词：Bimanual; Motion Planning; Collision Avoidance; Real Robot


- 引用量：11
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/03_Bimanual/Constrained_Bimanual_Planning.pdf]]
## 论文定位

这篇论文属于 Bimanual 方向，主要讨论双臂共同操作时，两只末端之间常需保持固定相对位姿。
核心思路是直接在满足双臂相对位姿约束的运动流形上搜索轨迹。
与当前项目的联系：High：双臂同步和共同约束是本项目基础问题。

## 核心关键词

Bimanual、Motion Planning、Collision Avoidance、Real Robot、Analytic IK parameterization

## 快速摘要

### 研究问题

双臂共同操作时，两只末端之间常需保持固定相对位姿。

### 之前方法的问题

这种等式约束使普通规划器难以高效搜索可行动作。

### 核心思路

直接在满足双臂相对位姿约束的运动流形上搜索轨迹。

### 数据集与评测基准

约束双臂规划场景；具体 benchmark 需核对正文。

### 主要结果

已核验摘要未提供可安全复述的统一量化结果。

### 为什么重要

为普通夹爪共同搬运物体提供几何约束基线。

### 与当前项目的关系

High：双臂同步和共同约束是本项目基础问题。

### 主要局限

需评估模型化固定相对位姿与真实滑动、形变之间的差异。

## 实验与结果

### 数据集与评测基准

约束双臂规划场景；具体 benchmark 需核对正文。

### 主要结果

已核验摘要未提供可安全复述的统一量化结果。

## 局限与启发

### 主要局限

需评估模型化固定相对位姿与真实滑动、形变之间的差异。

## 与当前项目的关系

High：双臂同步和共同约束是本项目基础问题。

## 来源

- 官方论文：[官方论文](https://ieeexplore.ieee.org/document/10610675/)
- 项目主页：[项目主页](https://tommycohn.com/Bimanual-Web/index.html)
- 官方代码：[GitHub](https://github.com/cohnt/constrained-bimanual-planning-example)
