# RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models

## 基本信息

- 年份：2025
- 会议 / 期刊：CoRL
- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)
- 官方论文：https://proceedings.mlr.press/v305/kwok25a.html
- 主要分类：VLA / Robot Foundation Models / Robot Manipulation

## 论文定位

这篇论文属于 VLA / Robot Foundation Models / Robot Manipulation 方向，主要讨论VLA 在开放真实环境中容易遇到未见状态，执行鲁棒性不足。
核心思路是RoboMonkey 在测试时增加动作验证与计算调度，为 VLA 选择更可靠的执行动作。
与当前项目的联系：High：与双臂动作前检查和失败预防直接相关。

## 核心关键词

VLA、Robot Foundation Models、Robot Manipulation

## 快速摘要

### 研究问题

VLA 在开放真实环境中容易遇到未见状态，执行鲁棒性不足。

### 之前方法的问题

只靠训练好的动作预测器，测试时缺少可靠的候选动作验证。

### 核心思路

RoboMonkey 在测试时增加动作验证与计算调度，为 VLA 选择更可靠的执行动作。

### 主要结果

作者报告在新机器人设置中，同时微调 VLA 与动作验证器，比只调整部分模块高约 7%。

### 为什么重要

把 Action Verification 放入 VLA 真机执行环节。

### 与当前项目的关系

High：与双臂动作前检查和失败预防直接相关。

### 主要局限

额外验证会增加在线延迟，真机安全收益需单独评测。

## 实验与结果

### 主要结果

作者报告在新机器人设置中，同时微调 VLA 与动作验证器，比只调整部分模块高约 7%。

## 局限与启发

### 主要局限

额外验证会增加在线延迟，真机安全收益需单独评测。

## 与当前项目的关系

High：与双臂动作前检查和失败预防直接相关。

## 相关论文

- [[CoT-VLA]]
- [[Octo]]
- [[OpenVLA]]
- [[DROID]]
- [[Open_X-Embodiment]]
- [[A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]]
- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：https://proceedings.mlr.press/v305/kwok25a.html
