# Rethinking Bimanual Robotic Manipulation: Learning with Decoupled Interaction Framework

## 基本信息

- 作者：Jiang, Jian-Jian; Wu, Xiao-Ming; He, Yi-Xiang; Zeng, Ling-An; Wei, Yi-Lin; Zhang, Dandan; Zheng, Wei-Shi
- 年份：2025
- 会议 / 期刊：ICCV
- CCF 等级：A
- 官方论文：https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_Rethinking_Bimanual_Robotic_Manipulation_Learning_with_Decoupled_Interaction_Framework_ICCV_2025_paper.html
- 主要分类：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 关键词：bimanual manipulation; decoupled interaction; RoboTwin

## 论文定位

这篇论文属于 A (CCF 7th edition; venue category not independently extracted from official PDF) 方向，主要讨论不同双臂任务的交互结构不同，统一耦合方式未必合适。
核心思路是按任务交互特点设计解耦框架，让双臂策略分别处理可分解的部分并保持必要协调。
与当前项目的联系：High：普通夹爪常有支撑—操作分工。

## 核心关键词

bimanual manipulation、decoupled interaction、RoboTwin、venue category not independently extracted from official PDF)、Robot Manipulation、IL、Diffusion、Bimanual

## 快速摘要

### 研究问题

不同双臂任务的交互结构不同，统一耦合方式未必合适。

### 之前方法的问题

始终联合预测双臂动作，可能忽略支撑手与操作手的不同职责。

### 核心思路

按任务交互特点设计解耦框架，让双臂策略分别处理可分解的部分并保持必要协调。

### 数据集与评测基准

RoboTwin 七项任务。

### 主要结果

论文报告在七项 RoboTwin 任务上较所比较 SOTA 提升 23.5%；具体指标定义见原文。

### 为什么重要

为联合预测与分臂预测的实验对照提供方法。

### 与当前项目的关系

High：普通夹爪常有支撑—操作分工。

### 主要局限

仿真 benchmark 上的优势仍需真机接触任务验证。

## 实验与结果

### 数据集与评测基准

RoboTwin 七项任务。

### 主要结果

论文报告在七项 RoboTwin 任务上较所比较 SOTA 提升 23.5%；具体指标定义见原文。

## 局限与启发

### 主要局限

仿真 benchmark 上的优势仍需真机接触任务验证。

## 与当前项目的关系

High：普通夹爪常有支撑—操作分工。

## 来源

- 官方论文：https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_Rethinking_Bimanual_Robotic_Manipulation_Learning_with_Decoupled_Interaction_Framework_ICCV_2025_paper.html
