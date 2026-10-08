---
paper_id: P010
title: "DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset"
---

# P010 · DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset

## 基本信息

- 作者：—
- 年份：2024
- 发表 venue：RSS
- 论文类型：Benchmark / Dataset
- 研究方向：基准测试与数据集
- 论文链接：[Robotics Proceedings](https://roboticsproceedings.org/rss20/p120.html)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：[GitHub](https://github.com/droid-dataset/droid_policy_learning)
- 本地 PDF：[[00_论文池/PDFs/10_基准测试与数据集/DROID.pdf|查看 PDF]]
- 引用量：1137
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：Not CCF A (robotics venue extension)

## 论文定位

这篇论文属于 Dataset / Benchmark / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论通用操作策略需要规模大、场景多样且质量可靠的机器人交互数据。
核心思路是DROID 组织分布式采集，形成 6.5 万条示范轨迹、约 350 小时交互，覆盖 564 个场景和 86 项任务。
与当前项目的联系：Medium：可借鉴采集协议，但需核对与本项目机器人形态和动作接口的差异。

## 核心关键词

Dataset、Benchmark、Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

通用操作策略需要规模大、场景多样且质量可靠的机器人交互数据。

### 之前方法的问题

跨环境采集成本高，并受安全、硬件和人力协调限制。

### 核心思路

DROID 组织分布式采集，形成 6.5 万条示范轨迹、约 350 小时交互，覆盖 564 个场景和 86 项任务。

### 数据集与评测基准

DROID：约 6.5 万条轨迹／350 小时、564 个场景、86 项任务，50 名采集人员在 12 个月内完成。

### 主要结果

论文摘要报告，使用 DROID 训练的策略在性能、鲁棒性和泛化上改善；此处不附加未经实验表格核实的增幅。

### 为什么重要

为跨场景数据采集和数据规模设计提供具体参照。

### 与当前项目的关系

Medium：可借鉴采集协议，但需核对与本项目机器人形态和动作接口的差异。

### 主要局限

摘要不能分离数据量、场景多样性与策略结构各自的贡献。

## 实验与结果

### 数据集与评测基准

DROID：约 6.5 万条轨迹／350 小时、564 个场景、86 项任务，50 名采集人员在 12 个月内完成。

### 主要结果

论文摘要报告，使用 DROID 训练的策略在性能、鲁棒性和泛化上改善；此处不附加未经实验表格核实的增幅。

## 局限与启发

### 主要局限

摘要不能分离数据量、场景多样性与策略结构各自的贡献。

## 与当前项目的关系

Medium：可借鉴采集协议，但需核对与本项目机器人形态和动作接口的差异。

## 相关论文

- [[Actions as Language - Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting]]
- [[DiffusionVLA - Scaling Robot Foundation Models via Unified Diffusion and Autoregression]]
- [[OpenVLA - An Open-Source Vision-Language-Action Model]]
- [[RoboMonkey - Scaling Test-Time Sampling and Verification for Vision-Language-Action Models]]
- [[SpatialVLA - Exploring Spatial Representations for Visual-Language-Action Models]]
- [[TraceVLA - Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies]]
- [[Dreamitate - Real-World Visuomotor Policy Learning via Video Generation]]
- [[VidMan - Exploiting Implicit Dynamics from Video Diffusion Model for Effective Robot Manipulation]]
- [[ALOHA Unleashed - A Simple Recipe for Robot Dexterity]]
- [[AnyBimanual - Transferring Unimanual Policy for General Bimanual Manipulation]]
- [[A Survey on Vision-Language-Action Models - An Action Tokenization Perspective]]
- [[A Survey on Vision-Language-Action Models for Embodied AI]]

## 来源

- 官方论文：[Robotics Proceedings](https://roboticsproceedings.org/rss20/p120.html)
- 官方代码：[GitHub](https://github.com/droid-dataset/droid_policy_learning)
