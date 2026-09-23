# FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation

## 基本信息

- 年份：2025
- 会议 / 期刊：AAAI
- CCF 等级：A
- 官方论文：https://ojs.aaai.org/index.php/AAAI/article/view/33617
- 官方代码：https://github.com/zql-kk/FlowPolicy
- 主要分类：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 关键词：Robot Manipulation; Consistency Flow Matching / 3D Policy

## 论文定位

这篇论文属于 A (CCF 7th edition; venue category not independently extracted from official PDF) 方向，主要讨论扩散/流式动作生成往往需要多次采样，在线控制延迟较高。
核心思路是FlowPolicy 使用三维点云和 consistency flow matching，在单次推理中生成动作。
与当前项目的联系：Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 核心关键词

Robot Manipulation、Consistency Flow Matching、3D Policy、venue category not independently extracted from official PDF)、IL、Diffusion

## 快速摘要

### 研究问题

扩散/流式动作生成往往需要多次采样，在线控制延迟较高。

### 之前方法的问题

生成质量与推理速度之间存在权衡。

### 核心思路

FlowPolicy 使用三维点云和 consistency flow matching，在单次推理中生成动作。

### 输入

官方摘要给出任务/数据类型；具体模型张量与接口需核对方法章节。

### 输出与动作

官方摘要未明确列出完整控制接口；需核对论文方法或代码。

### 数据集与评测基准

Adroit、MetaWorld。

### 主要结果

AAAI 摘要报告在 Adroit 与 MetaWorld 上保持有竞争力的成功率，同时推理速度提高约 7 倍。

### 为什么重要

双臂真机尤其关注动作频率；该工作可用于比较速度与成功率。

### 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 方法概览

任务输入 → FlowPolicy 使用三维点云和 consistency flow matching，在单次推理中生成动作 → 官方摘要未明确列出完整控制接口；需核对论文方法或代码。

## 实验与结果

### 数据集与评测基准

Adroit、MetaWorld。

### 主要结果

AAAI 摘要报告在 Adroit 与 MetaWorld 上保持有竞争力的成功率，同时推理速度提高约 7 倍。

## 局限与启发

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 相关论文

- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：https://ojs.aaai.org/index.php/AAAI/article/view/33617
- 官方代码：https://github.com/zql-kk/FlowPolicy
