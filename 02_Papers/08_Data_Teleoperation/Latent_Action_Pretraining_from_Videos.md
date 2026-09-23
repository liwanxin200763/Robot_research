# Latent Action Pretraining from Videos

## 基本信息

- 年份：2025
- 会议 / 期刊：ICLR
- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 官方论文：https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html
- 项目主页：https://latentactionpretraining.github.io/
- 官方代码：https://github.com/LatentActionPretraining/LAPA
- 主要分类：VLA / Robot Foundation Models / Robot Manipulation

## 论文定位

这篇论文属于 VLA / Robot Foundation Models / Robot Manipulation 方向，主要讨论互联网视频规模大，但缺少机器人动作标签。
核心思路是LAPA 从无动作标签视频学习潜在动作，再用这些表示预训练视觉语言动作模型。
与当前项目的联系：High：双臂示范稀缺，可研究潜在动作是否可迁移。

## 核心关键词

VLA、Robot Foundation Models、Robot Manipulation

## 快速摘要

### 研究问题

互联网视频规模大，但缺少机器人动作标签。

### 之前方法的问题

传统 VLA 预训练高度依赖昂贵的机器人动作数据。

### 核心思路

LAPA 从无动作标签视频学习潜在动作，再用这些表示预训练视觉语言动作模型。

### 主要结果

作者报告部分真机操作任务上优于使用机器人动作标签训练的对照 VLA；具体协议见论文。

### 为什么重要

提供低成本视频数据进入 VLA 预训练的路线。

### 与当前项目的关系

High：双臂示范稀缺，可研究潜在动作是否可迁移。

### 主要局限

潜在动作与真实普通夹爪命令之间需要可靠解码。

## 实验与结果

### 主要结果

作者报告部分真机操作任务上优于使用机器人动作标签训练的对照 VLA；具体协议见论文。

## 局限与启发

### 主要局限

潜在动作与真实普通夹爪命令之间需要可靠解码。

## 与当前项目的关系

High：双臂示范稀缺，可研究潜在动作是否可迁移。

## 相关论文

- [[A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective]]
- [[A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]]
- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html
- 项目主页：https://latentactionpretraining.github.io/
- 官方代码：https://github.com/LatentActionPretraining/LAPA
