# Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching

## 基本信息

- 年份：2024
- 会议 / 期刊：CoRL
- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)
- 官方论文：[PMLR](https://proceedings.mlr.press/v270/chisari25a.html)
- 主要分类：Imitation Learning / Diffusion / Flow Matching / Robot Manipulation


- 引用量：1
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/06_Diffusion_Flow_IL_RL/Learning_Robotic_Manipulation_Policies_from_Point_Clouds_with_Conditional_Flow_Matching.pdf]]
## 论文定位

这篇论文属于 Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论少量示范条件下，策略输入和动作生成目标的选择影响操作表现。
核心思路是PointFlowMatch 从点云观测学习条件 Flow Matching 策略，生成机器人操作动作。
与当前项目的联系：Medium：双夹爪三维定位可借鉴，但真机点云质量需检查。

## 核心关键词

Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

少量示范条件下，策略输入和动作生成目标的选择影响操作表现。

### 之前方法的问题

二维图像可能丢失三维几何；迭代生成动作又增加延迟。

### 核心思路

PointFlowMatch 从点云观测学习条件 Flow Matching 策略，生成机器人操作动作。

### 数据集与评测基准

RLBench。

### 主要结果

作者报告在 RLBench 上达到有竞争力的结果；完整数值需看论文表格。

### 为什么重要

为点云输入加流式动作生成提供基线。

### 与当前项目的关系

Medium：双夹爪三维定位可借鉴，但真机点云质量需检查。

### 主要局限

仿真点云与真机深度噪声之间可能存在差距。

## 实验与结果

### 数据集与评测基准

RLBench。

### 主要结果

作者报告在 RLBench 上达到有竞争力的结果；完整数值需看论文表格。

## 局限与启发

### 主要局限

仿真点云与真机深度噪声之间可能存在差距。

## 与当前项目的关系

Medium：双夹爪三维定位可借鉴，但真机点云质量需检查。

## 相关论文

- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v270/chisari25a.html)
