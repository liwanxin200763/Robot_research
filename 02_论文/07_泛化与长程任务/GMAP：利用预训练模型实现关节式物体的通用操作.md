# GMAP：利用预训练模型实现关节式物体的通用操作

## 基本信息

- 英文标题：GMAP: Generalized Manipulation of Articulated Objects in Robotic Using Pre-trained Model
- 作者：[H Zeng](https://scholar.google.com/citations?user=CPfyv1gAAAAJ&hl=zh-CN&oi=sra) , P 张, F Li, Q Yi, [T Ye](https://scholar.google.com/citations?user=B8fwxmkAAAAJ&hl=zh-CN&oi=sra) , J Wang
- 年份：2025
- 发表 venue：AAAI
- 论文类型：会议论文
- 研究方向：泛化与长程任务
- 论文链接：[AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/33615)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/07_泛化与长程任务/GMAP.pdf|查看 PDF]]
- 引用量：0
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：A
- 关键词：Articulated Object / Affordance

## 论文定位

这篇论文属于 Robot Manipulation; Generalization 方向，主要讨论关节物体操作需要同时识别可动部件、关节参数和可行的末端轨迹。
核心思路是GMAP 结合部件分割、关节几何估计与可操作点预测，再规划末端位姿/轨迹。
与当前项目的联系：Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 核心关键词

Articulated Object、Affordance、Robot Manipulation、Generalization

## 快速摘要

### 研究问题

关节物体操作需要同时识别可动部件、关节参数和可行的末端轨迹。

### 之前方法的问题

既有方法多只解决感知或 affordance 的一部分，缺少从指令到动作的完整链条。

### 核心思路

GMAP 结合部件分割、关节几何估计与可操作点预测，再规划末端位姿/轨迹。

### 输入

官方摘要给出任务/数据类型；具体模型张量与接口需核对方法章节。

### 输出与动作

官方摘要未明确列出完整控制接口；需核对论文方法或代码。

### 数据集与评测基准

关节物体操作任务；具体 benchmark 见论文。

### 主要结果

AAAI 摘要报告在关节物体任务上优于对比方法；具体数值需核对论文表格。

### 为什么重要

可为普通夹爪操作抽屉、柜门等任务提供几何约束参考。

### 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 方法概览

任务输入 → GMAP 结合部件分割、关节几何估计与可操作点预测，再规划末端位姿/轨迹 → 官方摘要未明确列出完整控制接口；需核对论文方法或代码。

## 实验与结果

### 数据集与评测基准

关节物体操作任务；具体 benchmark 见论文。

### 主要结果

AAAI 摘要报告在关节物体任务上优于对比方法；具体数值需核对论文表格。

## 局限与启发

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 来源

- 官方论文：[AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/33615)
