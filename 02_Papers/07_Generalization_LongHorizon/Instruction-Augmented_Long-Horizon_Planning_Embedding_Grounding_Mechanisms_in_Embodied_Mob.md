# Instruction-Augmented Long-Horizon Planning: Embedding Grounding Mechanisms in Embodied Mobile Manipulation

## 基本信息

- 年份：2025
- 会议 / 期刊：AAAI
- CCF 等级：A
- 官方论文：[AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/33610)
- 主要分类：Robot Manipulation
- 关键词：Long-Horizon / Mobile Manipulation


- 引用量：5
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/07_Generalization_LongHorizon/Instruction-Augmented_Long-Horizon_Planning_Embedding_Grounding_Mechanisms_in_Embodied_Mob.pdf]]
## 论文定位

这篇论文属于 Robot Manipulation 方向，主要讨论移动操作的长任务规划需要把语言计划落实到实时环境状态。
核心思路是IALP 把 LLM 推理、PDDL 问题与传感器反馈结合，闭环更新高层操作计划。
与当前项目的联系：High：直接关联双臂普通夹爪、VLA 或真机操作。

## 核心关键词

Long-Horizon、Mobile Manipulation、Robot Manipulation

## 快速摘要

### 研究问题

移动操作的长任务规划需要把语言计划落实到实时环境状态。

### 之前方法的问题

只依赖人工文字场景描述或 prompt，难以判断物体是否真的可操作。

### 核心思路

IALP 把 LLM 推理、PDDL 问题与传感器反馈结合，闭环更新高层操作计划。

### 输入

官方摘要给出任务/数据类型；具体模型张量与接口需核对方法章节。

### 输出与动作

官方摘要未明确列出完整控制接口；需核对论文方法或代码。

### 数据集与评测基准

多项真实环境长时序移动操作任务。

### 主要结果

AAAI 官方摘要报告包含七类操作技能的真机长任务，平均成功率超过 80%。

### 为什么重要

可比较高层重新规划与双臂底层动作执行之间的接口。

### 与当前项目的关系

High：直接关联双臂普通夹爪、VLA 或真机操作。

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 方法概览

任务输入 → IALP 把 LLM 推理、PDDL 问题与传感器反馈结合，闭环更新高层操作计划 → 官方摘要未明确列出完整控制接口；需核对论文方法或代码。

## 实验与结果

### 数据集与评测基准

多项真实环境长时序移动操作任务。

### 主要结果

AAAI 官方摘要报告包含七类操作技能的真机长任务，平均成功率超过 80%。

## 局限与启发

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 与当前项目的关系

High：直接关联双臂普通夹爪、VLA 或真机操作。

## 来源

- 官方论文：[AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/33610)
