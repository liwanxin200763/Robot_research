# FreqPolicy：通过频率一致性实现高效 Flow 视觉运动策略

## 基本信息

- 英文标题：FreqPolicy: Efficient Flow-based Visuomotor Policy via Frequency Consistency
- 作者：Su, Yifei; Liu, Ning; Chen, Dong; Zhao, Zhen; Wu, Kun; Li, Meng; Xu, Zhiyuan; Che, Zhengping; Tang, Jian
- 年份：2025
- 发表 venue：NeurIPS
- 论文类型：会议论文
- 研究方向：扩散模型 / 流匹配 / IL / RL
- 论文链接：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/282c3318be1b047b7bb5ba94fa4f3231-Abstract-Conference.html)
- DOI：10.52202/085713-0937 — [DOI](https://doi.org/10.52202/085713-0937)
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/FreqPolicy.pdf|查看 PDF]]
- 引用量：19
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：A
- 关键词：Flow Matching / Visuomotor Policy

## 论文定位

这篇论文属于 Diffusion / Flow; Robot Manipulation 方向，主要讨论生成式视觉运动策略在复杂动作上表现好，但在线推理可能偏慢。
核心思路是FreqPolicy 给流式动作生成加入频率一致性约束，并尝试融入 VLA。
与当前项目的联系：High：推理延迟直接影响双臂同步和失败检测。

## 核心关键词

Flow Matching、Visuomotor Policy、Diffusion、Flow、Robot Manipulation

## 快速摘要

### 研究问题

生成式视觉运动策略在复杂动作上表现好，但在线推理可能偏慢。

### 之前方法的问题

常规 Flow Policy 未充分利用动作中的不同频率结构。

### 核心思路

FreqPolicy 给流式动作生成加入频率一致性约束，并尝试融入 VLA。

### 为什么重要

为实时双臂控制提供动作频率建模视角。

### 与当前项目的关系

High：推理延迟直接影响双臂同步和失败检测。

### 主要局限

需核验高频控制对真机安全与接触稳定性的影响。

## 局限与启发

### 主要局限

需核验高频控制对真机安全与接触稳定性的影响。

## 与当前项目的关系

High：推理延迟直接影响双臂同步和失败检测。

## 相关论文

- [[Towards a Unified Understanding of Robot Manipulation - A Comprehensive Survey]]

## 来源

- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/282c3318be1b047b7bb5ba94fa4f3231-Abstract-Conference.html)
