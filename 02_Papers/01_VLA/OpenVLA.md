# OpenVLA: An Open-Source Vision-Language-Action Model

## 基本信息

- 年份：2024
- 会议 / 期刊：CoRL
- CCF 等级：Not CCF A (robotics venue extension)
- 官方论文：[PMLR](https://proceedings.mlr.press/v270/kim25c.html)
- 项目主页：[项目主页](https://openvla.github.io/)
- 官方代码：[GitHub](https://github.com/openvla/openvla)
- 主要分类：VLA / Robot Foundation Models / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation


- 引用量：43
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/01_VLA/OpenVLA.pdf]]
## 论文定位

这篇论文属于 VLA / Robot Foundation Models / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论现有 VLA 多为闭源，且针对新任务高效微调的方法仍不充分。
核心思路是OpenVLA 是开放的 7B VLA，在约 97 万条真实机器人轨迹上训练，支持通过微调适配新任务。
与当前项目的联系：High：有助于研究语言条件操作与 VLA 设计。

## 核心关键词

VLA、Robot Foundation Models、Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

现有 VLA 多为闭源，且针对新任务高效微调的方法仍不充分。

### 之前方法的问题

既有 VLA 多为闭源，新任务的高效微调方法也缺少系统评估。

### 核心思路

OpenVLA 是开放的 7B VLA，在约 97 万条真实机器人轨迹上训练，支持通过微调适配新任务。

### 输入

机器人相机图像和语言任务指令；具体预处理见论文方法及官方代码。

### 输出与动作

预测机器人控制动作；动作编码与本体适配以官方代码和论文方法为准。

### 数据集与评测基准

训练使用整理后的 Open X-Embodiment 混合数据，约 97 万条真机轨迹；DROID 在后期训练数据中被剔除，详见原卡。

### 为什么重要

提供可复用的 VLA 基线，同时明确了数据、算力和推理速度代价。

### 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

### 主要局限

作者指出训练数据偏单臂、第三人称视角且算力成本高；双臂/移动平台迁移仍需单独验证。

## 方法概览

任务输入 → OpenVLA 是开放的 7B VLA，在约 97 万条真实机器人轨迹上训练，支持通过微调适配新任务 → 预测机器人控制动作；动作编码与本体适配以官方代码和论文方法为准。

## 实验与结果

### 数据集与评测基准

训练使用整理后的 Open X-Embodiment 混合数据，约 97 万条真机轨迹；DROID 在后期训练数据中被剔除，详见原卡。

## 局限与启发

### 主要局限

作者指出训练数据偏单臂、第三人称视角且算力成本高；双臂/移动平台迁移仍需单独验证。

## 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

## 相关论文

- [[Octo]]
- [[DROID]]
- [[Open_X-Embodiment]]
- [[Actions_as_Language]]
- [[BridgeVLA]]
- [[CoT-VLA]]
- [[DiffusionVLA]]
- [[ReconVLA]]
- [[RoboGround]]
- [[RoboMamba]]
- [[RoboMonkey]]
- [[SP-VLA]]

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v270/kim25c.html)
- 项目主页：[项目主页](https://openvla.github.io/)
- 官方代码：[GitHub](https://github.com/openvla/openvla)
