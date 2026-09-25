# Equivariant Diffusion Policy

## 基本信息

- 年份：2024
- 会议 / 期刊：CoRL
- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)
- 官方论文：[PMLR](https://proceedings.mlr.press/v270/wang25a.html)
- 主要分类：Imitation Learning / Diffusion / Flow Matching / Robot Manipulation


- 引用量：0
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/06_Diffusion_Flow_IL_RL/Equivariant_Diffusion_Policy.pdf]]
## 论文定位

这篇论文属于 Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论扩散策略善于表达多种动作，但少量数据下泛化仍有挑战。
核心思路是Equivariant Diffusion Policy 把空间对称性引入扩散式动作策略。
与当前项目的联系：Medium：可用于双夹爪空间变化实验。

## 核心关键词

Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

扩散策略善于表达多种动作，但少量数据下泛化仍有挑战。

### 之前方法的问题

不利用任务的几何对称性会增加学习样本需求。

### 核心思路

Equivariant Diffusion Policy 把空间对称性引入扩散式动作策略。

### 主要结果

作者报告在真机系统上可用较少示范学到有效策略；具体数值见原文。

### 为什么重要

将几何先验与生成式动作结合。

### 与当前项目的关系

Medium：可用于双夹爪空间变化实验。

### 主要局限

需要核验所假设的对称性在复杂接触和双臂协作中是否成立。

## 实验与结果

### 主要结果

作者报告在真机系统上可用较少示范学到有效策略；具体数值见原文。

## 局限与启发

### 主要局限

需要核验所假设的对称性在复杂接触和双臂协作中是否成立。

## 与当前项目的关系

Medium：可用于双夹爪空间变化实验。

## 相关论文

- [[DiffusionVLA]]
- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]
- [[3D_Diffuser_Actor]]

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v270/wang25a.html)
