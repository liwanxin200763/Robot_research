# RoboMonkey：扩展 VLA 的测试时采样与验证

## 基本信息

- 英文标题：RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models
- 作者：—
- 年份：2025
- 发表 venue：CoRL
- 论文类型：会议论文
- 研究方向：VLA
- 论文链接：[PMLR](https://proceedings.mlr.press/v305/kwok25a.html)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/01_VLA/RoboMonkey.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：73
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)

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

- [[CoT-VLA：面向 VLA 的视觉思维链推理]]
- [[Octo：开源通用机器人策略]]
- [[OpenVLA：开源视觉—语言—动作模型]]
- [[DROID：大规模自然场景机器人操作数据集]]
- [[Open X-Embodiment：机器人学习数据集与 RT-X 模型]]
- [[面向具身 AI 的 VLA 模型综述]]
- [[迈向统一理解机器人操作：综合综述]]

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v305/kwok25a.html)
