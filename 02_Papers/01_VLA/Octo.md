# Octo: An Open-Source Generalist Robot Policy

## 基本信息

- 年份：2024
- 会议 / 期刊：RSS
- CCF 等级：Not CCF A (robotics venue extension)
- 官方论文：https://roboticsproceedings.org/rss20/p090.html
- 项目主页：https://octo-models.github.io/
- 官方代码：https://github.com/octo-models/octo
- 主要分类：VLA / Robot Foundation Models / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation

## 论文定位

这篇论文属于 VLA / Robot Foundation Models / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论通用机器人策略需要同时适配不同相机、动作空间和机器人平台。
核心思路是Octo 在 Open X-Embodiment 约 80 万条轨迹上训练 Transformer 策略，并提供可微调的通用初始化。
与当前项目的联系：High：有助于研究语言条件操作与 VLA 设计。

## 核心关键词

VLA、Robot Foundation Models、Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

通用机器人策略需要同时适配不同相机、动作空间和机器人平台。

### 之前方法的问题

各机器人平台的相机、动作空间与任务不同，单一策略难以直接跨平台使用。

### 核心思路

Octo 在 Open X-Embodiment 约 80 万条轨迹上训练 Transformer 策略，并提供可微调的通用初始化。

### 数据集与评测基准

从 Open X-Embodiment 整理约 80 万条训练轨迹，在 9 种机器人平台和多项下游任务上评估。

### 主要结果

论文在 9 种机器人平台上评测，表明 Octo 可迁移到新的观测和动作空间；具体成功率见原卡实验表。

### 为什么重要

是研究共享机器人数据与跨本体微调的重要开放基线。

### 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

### 主要局限

训练数据的腕部相机和语言覆盖不均；评测主要在论文列出的单臂/双臂平台。

## 实验与结果

### 数据集与评测基准

从 Open X-Embodiment 整理约 80 万条训练轨迹，在 9 种机器人平台和多项下游任务上评估。

### 主要结果

论文在 9 种机器人平台上评测，表明 Octo 可迁移到新的观测和动作空间；具体成功率见原卡实验表。

## 局限与启发

### 主要局限

训练数据的腕部相机和语言覆盖不均；评测主要在论文列出的单臂/双臂平台。

## 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

## 相关论文

- [[SayCan]]
- [[Open_X-Embodiment]]
- [[Actions_as_Language]]
- [[CoT-VLA]]
- [[DiffusionVLA]]
- [[OpenVLA]]
- [[ReconVLA]]
- [[RoboMonkey]]
- [[SP-VLA]]
- [[SimpleVLA-RL]]
- [[SpatialVLA]]
- [[TraceVLA]]

## 来源

- 官方论文：https://roboticsproceedings.org/rss20/p090.html
- 项目主页：https://octo-models.github.io/
- 官方代码：https://github.com/octo-models/octo
