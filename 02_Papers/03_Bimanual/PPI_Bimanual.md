# Gripper Pose and Object Pointflow as Interfaces for Robotic Bimanual Manipulation

## 基本信息

- 作者：Yuyin Yang; Zetao Cai; Yang Tian; Jia Zeng; Jiangmiao Pang
- 年份：2025
- 会议 / 期刊：RSS
- 官方论文：https://www.roboticsproceedings.org/rss21/p160.html
- 项目主页：https://yuyinyang3y.github.io/PPI/
- 主要分类：Bimanual
- 关键词：Bimanual; Gripper; Robot Manipulation; Generalization; Real Robot

## 论文定位

这篇论文属于 Bimanual 方向，主要讨论双臂策略要兼顾目标的空间定位和连续轨迹的灵活性。
核心思路是PPI 用空间接口引导连续双臂动作生成。
与当前项目的联系：High：直接对应双臂空间接口和连续动作。

## 核心关键词

Bimanual、Gripper、Robot Manipulation、Generalization、Real Robot、Gripper keypose and object pointflow interfaces

## 快速摘要

### 研究问题

双臂策略要兼顾目标的空间定位和连续轨迹的灵活性。

### 之前方法的问题

单独使用离散空间提示或连续动作预测，可能难同时实现定位与平滑控制。

### 核心思路

PPI 用空间接口引导连续双臂动作生成。

### 数据集与评测基准

仿真与真机双臂任务；完整 benchmark 见论文。

### 为什么重要

适合比较空间表示如何约束普通夹爪的双臂动作。

### 与当前项目的关系

High：直接对应双臂空间接口和连续动作。

### 主要局限

需进一步核验任务分布、失败类型和动作频率。

## 实验与结果

### 数据集与评测基准

仿真与真机双臂任务；完整 benchmark 见论文。

## 局限与启发

### 主要局限

需进一步核验任务分布、失败类型和动作频率。

## 与当前项目的关系

High：直接对应双臂空间接口和连续动作。

## 相关论文

- [[YOTO]]

## 来源

- 官方论文：https://www.roboticsproceedings.org/rss21/p160.html
- 项目主页：https://yuyinyang3y.github.io/PPI/
