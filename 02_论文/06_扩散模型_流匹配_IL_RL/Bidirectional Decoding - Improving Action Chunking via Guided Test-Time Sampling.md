---
paper_id: P102
title: "Bidirectional Decoding: Improving Action Chunking via Guided Test-Time Sampling"
---

# P102 · Bidirectional Decoding: Improving Action Chunking via Guided Test-Time Sampling

## 基本信息

- 作者：—
- 年份：2025
- 发表 venue：ICLR
- 论文类型：会议论文
- 研究方向：扩散模型 / 流匹配 / IL / RL
- 论文链接：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/0d78dd998f7b9ac79604d47a2d79bb0d-Abstract-Conference.html)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：[GitHub](https://github.com/YuejiangLIU/bid_diffusion)
- 本地 PDF：[[00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/Bidirectional_Decoding.pdf|查看 PDF]]
- 引用量：1
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)

## 论文定位

这篇论文属于 Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论Action Chunk 减少推理调用，却可能降低中途修正能力。
核心思路是Bidirectional Decoding 在测试时调整生成式策略的动作解码，连接动作块与在线反馈。
与当前项目的联系：High：真机操作需要在动作块速度和失败恢复之间折中。

## 核心关键词

Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

Action Chunk 减少推理调用，却可能降低中途修正能力。

### 之前方法的问题

固定动作块开环执行与每步重新规划之间存在速度—反应性权衡。

### 核心思路

Bidirectional Decoding 在测试时调整生成式策略的动作解码，连接动作块与在线反馈。

### 主要结果

作者报告在七项仿真任务上提升两类生成式策略表现；详细数值见论文。

### 为什么重要

可用来设计低延迟但可中途纠正的双臂控制。

### 与当前项目的关系

High：真机操作需要在动作块速度和失败恢复之间折中。

### 主要局限

测试时解码的额外延迟和真机接触效果需核验。

## 实验与结果

### 主要结果

作者报告在七项仿真任务上提升两类生成式策略表现；详细数值见论文。

## 局限与启发

### 主要局限

测试时解码的额外延迟和真机接触效果需核验。

## 与当前项目的关系

High：真机操作需要在动作块速度和失败恢复之间折中。

## 来源

- 官方论文：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/0d78dd998f7b9ac79604d47a2d79bb0d-Abstract-Conference.html)
- 官方代码：[GitHub](https://github.com/YuejiangLIU/bid_diffusion)
