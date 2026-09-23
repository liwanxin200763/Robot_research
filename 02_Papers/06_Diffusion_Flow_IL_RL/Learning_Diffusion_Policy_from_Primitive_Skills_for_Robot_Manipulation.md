# Learning Diffusion Policy from Primitive Skills for Robot Manipulation

## 基本信息

- 年份：2026
- 会议 / 期刊：AAAI
- CCF 等级：A
- 官方论文：https://ojs.aaai.org/index.php/AAAI/article/view/38889
- 主要分类：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 关键词：Robot Manipulation; Diffusion Policy / Primitive Skills

## 论文定位

这篇论文属于 A (CCF 7th edition; venue category not independently extracted from official PDF) 方向，主要讨论长任务的高层指令与短时动作之间容易出现不一致。
核心思路是SDP 把复杂任务拆成八种 primitive skills，用 VLM 提取离散状态表示，再由轻量 router 选择技能条件化扩散策略。
与当前项目的联系：Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 核心关键词

Robot Manipulation、Diffusion Policy、Primitive Skills、venue category not independently extracted from official PDF)、IL、Diffusion

## 快速摘要

### 研究问题

长任务的高层指令与短时动作之间容易出现不一致。

### 之前方法的问题

只用全局指令条件化扩散策略，难以保证每段动作符合当前小技能。

### 核心思路

SDP 把复杂任务拆成八种 primitive skills，用 VLM 提取离散状态表示，再由轻量 router 选择技能条件化扩散策略。

### 输入

官方摘要给出任务/数据类型；具体模型张量与接口需核对方法章节。

### 输出与动作

官方摘要未明确列出完整控制接口；需核对论文方法或代码。

### 数据集与评测基准

两项仿真 benchmark 与真机操作评测。

### 主要结果

AAAI 摘要报告在两项仿真 benchmark 和真机任务中优于所比较方法；未给统一量化值。

### 为什么重要

可作为“高层技能调度 + 低层动作生成”的双臂基线。

### 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 方法概览

任务输入 → SDP 把复杂任务拆成八种 primitive skills，用 VLM 提取离散状态表示，再由轻量 router 选择技能条件化扩散策略 → 官方摘要未明确列出完整控制接口；需核对论文方法或代码。

## 实验与结果

### 数据集与评测基准

两项仿真 benchmark 与真机操作评测。

### 主要结果

AAAI 摘要报告在两项仿真 benchmark 和真机任务中优于所比较方法；未给统一量化值。

## 局限与启发

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 来源

- 官方论文：https://ojs.aaai.org/index.php/AAAI/article/view/38889
