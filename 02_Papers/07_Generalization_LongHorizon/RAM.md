# RAM: Retrieval-Based Affordance Transfer for Generalizable Zero-Shot Robotic Manipulation

## 基本信息

- 年份：2024
- 会议 / 期刊：CoRL
- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)
- 官方论文：[PMLR](https://proceedings.mlr.press/v270/kuang25a.html)
- 主要分类：Imitation Learning / Diffusion / Flow Matching / Robot Manipulation


- 引用量：2
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/07_Generalization_LongHorizon/RAM.pdf]]
## 论文定位

这篇论文属于 Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论新任务缺少目标域示范时，机器人如何零样本操作。
核心思路是RAM 检索相关已有行为，再把它迁移到当前物体和操作设置。
与当前项目的联系：Medium：可用于双臂任务的技能复用，但动作适配需验证。

## 核心关键词

Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

新任务缺少目标域示范时，机器人如何零样本操作。

### 之前方法的问题

为每项任务单独收集示范的成本太高。

### 核心思路

RAM 检索相关已有行为，再把它迁移到当前物体和操作设置。

### 为什么重要

展示通过检索复用经验而非每次重训的路径。

### 与当前项目的关系

Medium：可用于双臂任务的技能复用，但动作适配需验证。

### 主要局限

检索到的动作若与当前夹爪或物体不匹配，可能无法执行。

## 局限与启发

### 主要局限

检索到的动作若与当前夹爪或物体不匹配，可能无法执行。

## 与当前项目的关系

Medium：可用于双臂任务的技能复用，但动作适配需验证。

## 相关论文

- [[A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective]]
- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v270/kuang25a.html)
