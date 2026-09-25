# Closed-Loop Visuomotor Control with Generative Expectation for Robotic Manipulation

## 基本信息

- 作者：Bu, Qingwen; Zeng, Jia; Chen, Li; Yang, Yanchao; Zhou, Guyue; Yan, Junchi; Luo, Ping; Cui, Heming; Ma, Yi; Li, Hongyang
- 年份：2024
- 会议 / 期刊：NeurIPS
- CCF 等级：A
- DOI：10.52202/079017-4411 — [DOI](https://doi.org/10.52202/079017-4411)
- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/fad8962279154544ed69bb63eb14d677-Abstract-Conference.html)
- 官方代码：[GitHub](https://github.com/OpenDriveLab/CLOVER)
- 主要分类：Robot Manipulation
- 关键词：Long-Horizon / Failure Recovery


- 引用量：10
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/07_Generalization_LongHorizon/Closed-Loop_Visuomotor_Control_with_Generative_Expectation_for_Robotic_Manipulation.pdf]]
## 论文定位

这篇论文属于 Robot Manipulation 方向，主要讨论机器人长任务容易因局部错误累积而失败。
核心思路是CLOVER 借鉴闭环控制，把生成式未来预期与视觉运动策略结合，持续比较执行进展。
与当前项目的联系：High：双臂长任务尤其需要检查每步结果。

## 核心关键词

Long-Horizon、Failure Recovery、Robot Manipulation

## 快速摘要

### 研究问题

机器人长任务容易因局部错误累积而失败。

### 之前方法的问题

只按当前观测输出动作，缺少对下一状态的预期与检查。

### 核心思路

CLOVER 借鉴闭环控制，把生成式未来预期与视觉运动策略结合，持续比较执行进展。

### 数据集与评测基准

CALVIN 与真机操作任务。

### 为什么重要

为动作后验证和失败检测提供闭环思路。

### 与当前项目的关系

High：双臂长任务尤其需要检查每步结果。

### 主要局限

未来预测误差与真实接触误差如何区分仍需验证。

## 实验与结果

### 数据集与评测基准

CALVIN 与真机操作任务。

## 局限与启发

### 主要局限

未来预测误差与真实接触误差如何区分仍需验证。

## 与当前项目的关系

High：双臂长任务尤其需要检查每步结果。

## 相关论文

- [[ReconVLA]]
- [[RoboGround]]
- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/fad8962279154544ed69bb63eb14d677-Abstract-Conference.html)
- 官方代码：[GitHub](https://github.com/OpenDriveLab/CLOVER)
