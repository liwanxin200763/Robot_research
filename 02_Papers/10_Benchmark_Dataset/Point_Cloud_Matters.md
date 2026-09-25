# Point Cloud Matters: Rethinking the Impact of Different Observation Spaces on Robot Learning

## 基本信息

- 作者：Zhu, Haoyi; Wang, Yating; Huang, Di; Ye, Weicai; Ouyang, Wanli; He, Tong
- 年份：2024
- 会议 / 期刊：NeurIPS
- CCF 等级：A
- DOI：10.52202/079017-2473 — [DOI](https://doi.org/10.52202/079017-2473)
- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8e5dc5969a6174fcaaececd890c7f59b-Abstract-Datasets_and_Benchmarks_Track.html)
- 主要分类：Dataset / Benchmark; Robot Manipulation
- 关键词：3D Observation / Contact-rich


- 引用量：10
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/10_Benchmark_Dataset/Point_Cloud_Matters.pdf]]
## 论文定位

这篇论文属于 Dataset / Benchmark; Robot Manipulation 方向，主要讨论在机器人学习中，观测模态可能像策略设计一样限制操作能力。
核心思路是论文提出 OBSBench，统一比较不同观测编码器和策略基线；基准覆盖两个仿真器、125 项任务。
与当前项目的联系：Medium：可用于设计普通夹爪操作的观测消融实验。

## 核心关键词

3D Observation、Contact-rich、Dataset、Benchmark、Robot Manipulation

## 快速摘要

### 研究问题

在机器人学习中，观测模态可能像策略设计一样限制操作能力。

### 核心思路

论文提出 OBSBench，统一比较不同观测编码器和策略基线；基准覆盖两个仿真器、125 项任务。

### 数据集与评测基准

OBSBench：两个仿真器、125 项任务。

### 主要结果

摘要指出点云观测常带来更好的策略表现，并在几何与视觉变化下表现出更强泛化；具体幅度需查实验表格。

### 为什么重要

提示选择 RGB、点云等输入时，应在同一策略和任务设置下比较。

### 与当前项目的关系

Medium：可用于设计普通夹爪操作的观测消融实验。

### 主要局限

摘要未说明点云优势在传感器成本、遮挡和真实平台上的边界。

## 实验与结果

### 数据集与评测基准

OBSBench：两个仿真器、125 项任务。

### 主要结果

摘要指出点云观测常带来更好的策略表现，并在几何与视觉变化下表现出更强泛化；具体幅度需查实验表格。

## 局限与启发

### 主要局限

摘要未说明点云优势在传感器成本、遮挡和真实平台上的边界。

## 与当前项目的关系

Medium：可用于设计普通夹爪操作的观测消融实验。

## 来源

- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8e5dc5969a6174fcaaececd890c7f59b-Abstract-Datasets_and_Benchmarks_Track.html)
