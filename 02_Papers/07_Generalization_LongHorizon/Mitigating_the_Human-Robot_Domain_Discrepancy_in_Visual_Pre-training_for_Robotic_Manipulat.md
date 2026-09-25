# Mitigating the Human-Robot Domain Discrepancy in Visual Pre-training for Robotic Manipulation

## 基本信息

- 作者：Zhou, Jiaming; Ma, Teli; Lin, Kun-Yu; Wang, Zifan; Qiu, Ronghe; Liang, Junwei
- 年份：2025
- 会议 / 期刊：CVPR
- CCF 等级：A
- 官方论文：[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_Mitigating_the_Human-Robot_Domain_Discrepancy_in_Visual_Pre-training_for_Robotic_CVPR_2025_paper.html)
- 主要分类：Robot Manipulation; Generalization
- 关键词：Human-Robot Domain Adaptation


- 引用量：7
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/07_Generalization_LongHorizon/Mitigating_the_Human-Robot_Domain_Discrepancy_in_Visual_Pre-training_for_Robotic_Manipulat.pdf]]
## 论文定位

这篇论文属于 Robot Manipulation; Generalization 方向，主要讨论从人类视频预训练的视觉表示与机器人视角存在域差异。
核心思路是利用配对的人类—机器人视频对视觉表示做适配，缩小两种视角/本体差距。
与当前项目的联系：Medium：人类视频可能补充双臂数据，但动作仍需重定向。

## 核心关键词

Human-Robot Domain Adaptation、Robot Manipulation、Generalization

## 快速摘要

### 研究问题

从人类视频预训练的视觉表示与机器人视角存在域差异。

### 之前方法的问题

直接将人类视频特征用于机器人操作，可能识别不到关键交互区域。

### 核心思路

利用配对的人类—机器人视频对视觉表示做适配，缩小两种视角/本体差距。

### 主要结果

作者报告多个操作任务的平均成功率提高超过 7%；具体比较条件见论文。

### 为什么重要

为低成本视频数据用于普通夹爪策略提供域适配方法。

### 与当前项目的关系

Medium：人类视频可能补充双臂数据，但动作仍需重定向。

### 主要局限

视觉特征对齐不等于动作空间和接触动力学也对齐。

## 实验与结果

### 主要结果

作者报告多个操作任务的平均成功率提高超过 7%；具体比较条件见论文。

## 局限与启发

### 主要局限

视觉特征对齐不等于动作空间和接触动力学也对齐。

## 与当前项目的关系

Medium：人类视频可能补充双臂数据，但动作仍需重定向。

## 来源

- 官方论文：[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_Mitigating_the_Human-Robot_Domain_Discrepancy_in_Visual_Pre-training_for_Robotic_CVPR_2025_paper.html)
