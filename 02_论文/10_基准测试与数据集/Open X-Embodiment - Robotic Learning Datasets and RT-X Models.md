# Open X-Embodiment：机器人学习数据集与 RT-X 模型

## 基本信息

- 英文标题：Open X-Embodiment: Robotic Learning Datasets and RT-X Models
- 作者：—
- 年份：2024
- 发表 venue：ICRA
- 论文类型：Benchmark / Dataset
- 研究方向：基准测试与数据集
- 论文链接：[官方论文](https://ieeexplore.ieee.org/document/10611477)
- DOI：—
- arXiv：2310.08864
- 项目主页：—
- 代码：[GitHub](https://github.com/google-deepmind/open_x_embodiment)
- 本地 PDF：[[00_论文池/PDFs/10_基准测试与数据集/Open_X-Embodiment.pdf|查看 PDF]]
- 引用量：1593
- 引用量来源：Google Scholar

## 论文定位

这篇论文属于 VLA / Robot Foundation Models / Dataset / Benchmark / Robot Manipulation 方向，主要讨论机器人数据分散在不同机构、平台和格式中，难以训练通用策略。
核心思路是Open X-Embodiment 整合标准化的跨机器人数据，并训练 RT-X 模型测试共享学习。
与当前项目的联系：Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 核心关键词

VLA、Robot Foundation Models、Dataset、Benchmark、Robot Manipulation

## 快速摘要

### 研究问题

机器人数据分散在不同机构、平台和格式中，难以训练通用策略。

### 之前方法的问题

每个机器人和任务单独训练模型，跨平台复用成本高。

### 核心思路

Open X-Embodiment 整合标准化的跨机器人数据，并训练 RT-X 模型测试共享学习。

### 输入

官方摘要给出任务/数据类型；具体模型张量与接口需核对方法章节。

### 输出与动作

官方摘要未明确列出完整控制接口；需核对论文方法或代码。

### 数据集与评测基准

Open X-Embodiment 数据混合及 RT-X 评测。

### 主要结果

官方项目与论文报告跨机器人训练带来的泛化收益；具体任务数值见原论文。

### 为什么重要

是审计跨本体数据、动作格式和策略迁移的基础入口。

### 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 方法概览

任务输入 → Open X-Embodiment 整合标准化的跨机器人数据，并训练 RT-X 模型测试共享学习 → 官方摘要未明确列出完整控制接口；需核对论文方法或代码。

## 实验与结果

### 数据集与评测基准

Open X-Embodiment 数据混合及 RT-X 评测。

### 主要结果

官方项目与论文报告跨机器人训练带来的泛化收益；具体任务数值见原论文。

## 局限与启发

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 相关论文

- [[3D-VLA - A 3D Vision-Language-Action Generative World Model]]
- [[Actions as Language - Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting]]
- [[CoT-VLA - Visual Chain-of-Thought Reasoning for Vision-Language-Action Models]]
- [[DiffusionVLA - Scaling Robot Foundation Models via Unified Diffusion and Autoregression]]
- [[Octo - An Open-Source Generalist Robot Policy]]
- [[OpenVLA - An Open-Source Vision-Language-Action Model]]
- [[ReconVLA - Reconstructive Vision-Language-Action Model as Effective Robot Perceiver]]
- [[RoboMonkey - Scaling Test-Time Sampling and Verification for Vision-Language-Action Models]]
- [[SP-VLA - A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration]]
- [[SimpleVLA-RL - Scaling VLA Training via Reinforcement Learning]]
- [[SpatialVLA - Exploring Spatial Representations for Visual-Language-Action Models]]
- [[TraceVLA - Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies]]

## 来源

- 官方论文：[官方论文](https://ieeexplore.ieee.org/document/10611477)
- 官方代码：[GitHub](https://github.com/google-deepmind/open_x_embodiment)
