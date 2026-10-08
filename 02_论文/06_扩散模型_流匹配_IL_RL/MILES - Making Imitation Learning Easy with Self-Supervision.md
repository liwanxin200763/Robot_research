---
paper_id: P114
title: "MILES: Making Imitation Learning Easy with Self-Supervision"
---

# P114 · MILES: Making Imitation Learning Easy with Self-Supervision

## 基本信息

- 作者：[G Papagiannis](https://scholar.google.com/citations?user=OLggmh4AAAAJ&hl=zh-CN&oi=sra), [E Johns](https://scholar.google.com/citations?user=dHec-LkAAAAJ&hl=zh-CN&oi=sra)
- 年份：2024
- 发表 venue：CoRL
- 论文类型：会议论文
- 研究方向：扩散模型 / 流匹配 / IL / RL
- 论文链接：[PMLR](https://proceedings.mlr.press/v270/papagiannis25a.html)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/MILES.pdf|查看 PDF]]
- 引用量：19
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)

## 论文定位

这篇论文属于 Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论模仿学习的数据采集通常需要多次人工示范和环境复位。
核心思路是MILES 从单条示范出发，以自主自监督方式继续收集训练经验。
与当前项目的联系：High：项目可测自主采集是否安全且节省人力。

## 核心关键词

Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

模仿学习的数据采集通常需要多次人工示范和环境复位。

### 之前方法的问题

昂贵的人工监督限制新任务的快速适配。

### 核心思路

MILES 从单条示范出发，以自主自监督方式继续收集训练经验。

### 为什么重要

可以减少普通夹爪真机的示范采集成本。

### 与当前项目的关系

High：项目可测自主采集是否安全且节省人力。

### 主要局限

自主收集失败轨迹时的安全和错误标签需要严格控制。

## 局限与启发

### 主要局限

自主收集失败轨迹时的安全和错误标签需要严格控制。

## 与当前项目的关系

High：项目可测自主采集是否安全且节省人力。

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v270/papagiannis25a.html)
