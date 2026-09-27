# COMBO-Grasp：学习约束式操作以完成双臂遮挡抓取

## 基本信息

- 英文标题：COMBO-Grasp: Learning Constraint-Based Manipulation for Bimanual Occluded Grasping
- 作者：—
- 年份：2025
- 发表 venue：CoRL
- 论文类型：会议论文
- 研究方向：双臂协作
- 论文链接：[PMLR](https://proceedings.mlr.press/v305/yamada25a.html)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/03_双臂协作/COMBO-Grasp.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：0
- 引用量来源：OpenAlex
- 引用量来源链接：https://openalex.org/W4407569722
- 引用量查询日期：2026-09-27
- 排序引用量：0
- 排序引用量来源：OpenAlex

### 出版与分类补充

- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)

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

- [[ALOHA Unleashed：实现机器人灵巧操作的简明方法]]
- [[迈向统一理解机器人操作：综合综述]]

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v305/yamada25a.html)
