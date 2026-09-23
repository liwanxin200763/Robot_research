# SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration

## 基本信息

- 年份：2026
- 会议 / 期刊：ICLR
- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 官方论文：https://proceedings.iclr.cc/paper_files/paper/2026/hash/4072543747a14bbed76284cf2c04b9e9-Abstract-Conference.html
- 主要分类：VLA / Robot Foundation Models / Robot Manipulation

## 论文定位

这篇论文属于 VLA / Robot Foundation Models / Robot Manipulation 方向，主要讨论VLA 推理开销大，在线控制频率受限。
核心思路是SP-VLA 联合进行模型调度与 token 剪枝，在不同状态分配不同推理计算量。
与当前项目的联系：High：控制频率会影响双臂同步和失败恢复。

## 核心关键词

VLA、Robot Foundation Models、Robot Manipulation

## 快速摘要

### 研究问题

VLA 推理开销大，在线控制频率受限。

### 之前方法的问题

固定模型规模与统一 token 处理会浪费简单状态的计算。

### 核心思路

SP-VLA 联合进行模型调度与 token 剪枝，在不同状态分配不同推理计算量。

### 数据集与评测基准

LIBERO、SimplerEnv 与论文列出的真机任务。

### 主要结果

论文报告 LIBERO 无损加速约 1.5 倍、SimplerEnv 约 2.4 倍；平均成功率变化需按论文设置理解。

### 为什么重要

为双臂 VLA 真机控制提供延迟优化方向。

### 与当前项目的关系

High：控制频率会影响双臂同步和失败恢复。

### 主要局限

剪枝造成的少数困难状态失误，需用真实任务失败案例检验。

## 实验与结果

### 数据集与评测基准

LIBERO、SimplerEnv 与论文列出的真机任务。

### 主要结果

论文报告 LIBERO 无损加速约 1.5 倍、SimplerEnv 约 2.4 倍；平均成功率变化需按论文设置理解。

## 局限与启发

### 主要局限

剪枝造成的少数困难状态失误，需用真实任务失败案例检验。

## 与当前项目的关系

High：控制频率会影响双臂同步和失败恢复。

## 相关论文

- [[Octo]]
- [[OpenVLA]]
- [[RDT-1B]]
- [[Open_X-Embodiment]]

## 来源

- 官方论文：https://proceedings.iclr.cc/paper_files/paper/2026/hash/4072543747a14bbed76284cf2c04b9e9-Abstract-Conference.html
