# 通过掩码动作分块实现机器人实时执行

## 基本信息

- 英文标题：Real-Time Robot Execution with Masked Action Chunking
- 作者：—
- 年份：2026
- 发表 venue：ICLR
- 论文类型：会议论文
- 研究方向：扩散模型 / 流匹配 / IL / RL
- 论文链接：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/c35834443b7881e782e52b3519fe27c7-Abstract-Conference.html)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/Real-Time_Robot_Execution_with_Masked_Action_Chunking.pdf|查看 PDF]]
- 引用量：21
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)

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

- 官方论文：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/c35834443b7881e782e52b3519fe27c7-Abstract-Conference.html)
