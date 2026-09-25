# Action Chunking and Data Augmentation Yield Exponential Improvements in Behavior Cloning for Continuous Spaces

## 基本信息

- 年份：2026
- 会议 / 期刊：ICLR
- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 官方论文：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cd96cb9a239c37b39dbf34f3f5a4c56f-Abstract-Conference.html)
- 主要分类：Imitation Learning / Diffusion / Flow Matching / Robot Manipulation


- 引用量：—
- 引用量来源：未可靠匹配
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/06_Diffusion_Flow_IL_RL/Action_Chunking_and_Data_Augmentation_Yield_Exponential_Improvements_in_Behavior_Cloning_f.pdf]]
## 论文定位

这篇论文属于 Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论模仿学习的单步误差会在长轨迹中不断积累。
核心思路是用控制理论分析动作块和数据增强对误差传播的影响，并给出相应实验。
与当前项目的联系：High：双臂长任务的误差积累需要明确评测。

## 核心关键词

Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

模仿学习的单步误差会在长轨迹中不断积累。

### 之前方法的问题

需要解释 Action Chunk 与数据增强为何能改善行为克隆，而不只看经验结果。

### 核心思路

用控制理论分析动作块和数据增强对误差传播的影响，并给出相应实验。

### 主要结果

作者报告理论分析能解释误差积累与这些训练措施的作用；具体界限与实验数字见原文。

### 为什么重要

为选择动作块长度和数据增强方式提供理论背景。

### 与当前项目的关系

High：双臂长任务的误差积累需要明确评测。

### 主要局限

理论假设与真机接触、感知噪声之间的差距需核对。

## 实验与结果

### 主要结果

作者报告理论分析能解释误差积累与这些训练措施的作用；具体界限与实验数字见原文。

## 局限与启发

### 主要局限

理论假设与真机接触、感知噪声之间的差距需核对。

## 与当前项目的关系

High：双臂长任务的误差积累需要明确评测。

## 来源

- 官方论文：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/cd96cb9a239c37b39dbf34f3f5a4c56f-Abstract-Conference.html)
