# Open X-Embodiment: Robotic Learning Datasets and RT-X Models

## 基本信息

- 年份：2024
- 会议 / 期刊：ICRA
- 官方论文：https://ieeexplore.ieee.org/document/10611477
- 官方代码：https://github.com/google-deepmind/open_x_embodiment
- 主要分类：VLA / Robot Foundation Models / Dataset / Benchmark / Robot Manipulation

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

- [[3D-VLA]]
- [[Actions_as_Language]]
- [[CoT-VLA]]
- [[DiffusionVLA]]
- [[Octo]]
- [[OpenVLA]]
- [[ReconVLA]]
- [[RoboMonkey]]
- [[SP-VLA]]
- [[SimpleVLA-RL]]
- [[SpatialVLA]]
- [[TraceVLA]]

## 来源

- 官方论文：https://ieeexplore.ieee.org/document/10611477
- 官方代码：https://github.com/google-deepmind/open_x_embodiment
