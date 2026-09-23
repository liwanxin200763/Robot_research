# Real-Time Robot Execution with Masked Action Chunking

## 基本信息

- 年份：2026
- 会议 / 期刊：ICLR
- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 官方论文：https://proceedings.iclr.cc/paper_files/paper/2026/hash/c35834443b7881e782e52b3519fe27c7-Abstract-Conference.html
- 主要分类：Imitation Learning / Diffusion / Flow Matching / Robot Manipulation

## 论文定位

这篇论文属于 Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论机器人必须实时响应，但动作块策略可能错过中途变化。
核心思路是REMAC 用 masked action chunking 学习对预训练策略动作的修正。
与当前项目的联系：High：可比较动作块长度、控制频率和失败恢复。

## 核心关键词

Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

机器人必须实时响应，但动作块策略可能错过中途变化。

### 之前方法的问题

固定动作块执行快，却不容易及时修正已预测动作。

### 核心思路

REMAC 用 masked action chunking 学习对预训练策略动作的修正。

### 主要结果

作者报告仿真与真机中执行更快，并保持任务表现；具体延迟和成功率需查论文。

### 为什么重要

直接对应普通夹爪真机的实时执行与修正。

### 与当前项目的关系

High：可比较动作块长度、控制频率和失败恢复。

### 主要局限

在线修正是否产生不安全突变需在控制器层验证。

## 实验与结果

### 主要结果

作者报告仿真与真机中执行更快，并保持任务表现；具体延迟和成功率需查论文。

## 局限与启发

### 主要局限

在线修正是否产生不安全突变需在控制器层验证。

## 与当前项目的关系

High：可比较动作块长度、控制频率和失败恢复。

## 来源

- 官方论文：https://proceedings.iclr.cc/paper_files/paper/2026/hash/c35834443b7881e782e52b3519fe27c7-Abstract-Conference.html
