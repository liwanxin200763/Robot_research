# Gentle Manipulation Policy Learning via Demonstrations from VLM Planned Atomic Skills

## 基本信息

- 年份：2026
- 会议 / 期刊：AAAI
- CCF 等级：A
- 官方论文：[AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/38955)
- 主要分类：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 关键词：Robot Manipulation; Long-Horizon / Visual-Tactile Policy


- 引用量：0
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/07_Generalization_LongHorizon/Gentle_Manipulation_Policy_Learning_via_Demonstrations_from_VLM_Planned_Atomic_Skills.pdf]]
## 论文定位

这篇论文属于 A (CCF 7th edition; venue category not independently extracted from official PDF) 方向，主要讨论长时序接触操作既要完成任务，也要避免过大接触力损伤物体。
核心思路是在仿真中用带力约束的 RL 训练原子技能，再由 VLM 规划任务，最后蒸馏到视觉—触觉 Diffusion Policy。
与当前项目的联系：Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 核心关键词

Robot Manipulation、Long-Horizon、Visual-Tactile Policy、venue category not independently extracted from official PDF)、IL、Diffusion

## 快速摘要

### 研究问题

长时序接触操作既要完成任务，也要避免过大接触力损伤物体。

### 之前方法的问题

真机专家示范昂贵，分层技能和安全约束难以同时获得。

### 核心思路

在仿真中用带力约束的 RL 训练原子技能，再由 VLM 规划任务，最后蒸馏到视觉—触觉 Diffusion Policy。

### 输入

官方摘要给出任务/数据类型；具体模型张量与接口需核对方法章节。

### 输出与动作

官方摘要未明确列出完整控制接口；需核对论文方法或代码。

### 数据集与评测基准

仿真与实体机器人接触操作任务。

### 主要结果

AAAI 官方摘要报告仿真与实体机器人验证，并进行了规划器和蒸馏方法消融；未给统一数值。

### 为什么重要

为普通夹爪的接触安全和低成本技能数据生成提供参考。

### 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 方法概览

任务输入 → 在仿真中用带力约束的 RL 训练原子技能，再由 VLM 规划任务，最后蒸馏到视觉—触觉 Diffusion Policy → 官方摘要未明确列出完整控制接口；需核对论文方法或代码。

## 实验与结果

### 数据集与评测基准

仿真与实体机器人接触操作任务。

### 主要结果

AAAI 官方摘要报告仿真与实体机器人验证，并进行了规划器和蒸馏方法消融；未给统一数值。

## 局限与启发

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 来源

- 官方论文：[AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/38955)
