# TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models

## 基本信息

- 年份：2026
- 会议 / 期刊：ICLR
- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 官方论文：https://proceedings.iclr.cc/paper_files/paper/2026/hash/65475a59e2a2cb707c9462e8a308e980-Abstract-Conference.html
- 项目主页：https://jellyho.github.io/TwinVLA/
- 官方代码：https://github.com/jellyho/TwinVLA
- 主要分类：VLA / Robot Foundation Models / Bimanual Manipulation / Robot Manipulation

## 论文定位

这篇论文属于 VLA / Robot Foundation Models / Bimanual Manipulation / Robot Manipulation 方向，主要讨论双臂 VLA 训练通常需要昂贵的双臂示范和大模型参数。
核心思路是TwinVLA 组合两个预训练单臂 VLA，并加入协调机制形成双臂策略。
与当前项目的联系：High：直接关系到项目未来 VLA 迁移。

## 核心关键词

VLA、Robot Foundation Models、Bimanual Manipulation、Robot Manipulation、Bimanual

## 快速摘要

### 研究问题

双臂 VLA 训练通常需要昂贵的双臂示范和大模型参数。

### 之前方法的问题

从单臂 VLA 迁移时，两只手臂仍要协调，而不能简单独立执行。

### 核心思路

TwinVLA 组合两个预训练单臂 VLA，并加入协调机制形成双臂策略。

### 数据集与评测基准

仿真与真机双臂操作任务。

### 主要结果

论文报告在若干双臂任务上优于同规模 RDT-1B，而无需双臂预训练；具体任务结果见原文。

### 为什么重要

提供低成本复用单臂模型的双臂 VLA 路线。

### 与当前项目的关系

High：直接关系到项目未来 VLA 迁移。

### 主要局限

即使无双臂预训练，协调模块与目标任务示范需求仍需具体核实。

## 实验与结果

### 数据集与评测基准

仿真与真机双臂操作任务。

### 主要结果

论文报告在若干双臂任务上优于同规模 RDT-1B，而无需双臂预训练；具体任务结果见原文。

## 局限与启发

### 主要局限

即使无双臂预训练，协调模块与目标任务示范需求仍需具体核实。

## 与当前项目的关系

High：直接关系到项目未来 VLA 迁移。

## 相关论文

- [[RDT-1B]]

## 来源

- 官方论文：https://proceedings.iclr.cc/paper_files/paper/2026/hash/65475a59e2a2cb707c9462e8a308e980-Abstract-Conference.html
- 项目主页：https://jellyho.github.io/TwinVLA/
- 官方代码：https://github.com/jellyho/TwinVLA
