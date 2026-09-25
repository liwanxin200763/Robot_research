# TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies

## 基本信息

- 年份：2025
- 会议 / 期刊：ICLR
- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 官方论文：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8667f264f88c7938a73a53ab01eb1327-Abstract-Conference.html)
- 项目主页：[项目主页](https://tracevla.github.io/)
- 官方代码：[GitHub](https://github.com/umd-huang-lab/tracevla)
- 主要分类：VLA / Robot Foundation Models / Robot Manipulation


- 引用量：1
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/01_VLA/TraceVLA.pdf]]
## 论文定位

这篇论文属于 VLA / Robot Foundation Models / Robot Manipulation 方向，主要讨论大规模预训练 VLA 对交互中的时空动态仍可能理解不足。
核心思路是TraceVLA 将状态—动作轨迹可视化为 trace prompt，辅助 VLA 做时空推理与动作预测。
与当前项目的联系：High：双臂任务可以比较轨迹提示与显式状态估计。

## 核心关键词

VLA、Robot Foundation Models、Robot Manipulation

## 快速摘要

### 研究问题

大规模预训练 VLA 对交互中的时空动态仍可能理解不足。

### 之前方法的问题

只看当前帧，难表示动作轨迹和目标运动方向。

### 核心思路

TraceVLA 将状态—动作轨迹可视化为 trace prompt，辅助 VLA 做时空推理与动作预测。

### 数据集与评测基准

SimplerEnv 137 种配置与 WidowX 真机四项任务。

### 为什么重要

为视觉轨迹提示如何改善 VLA 提供可测实例。

### 与当前项目的关系

High：双臂任务可以比较轨迹提示与显式状态估计。

### 主要局限

单臂 WidowX 结果不直接覆盖双臂真机。

## 实验与结果

### 数据集与评测基准

SimplerEnv 137 种配置与 WidowX 真机四项任务。

## 局限与启发

### 主要局限

单臂 WidowX 结果不直接覆盖双臂真机。

## 与当前项目的关系

High：双臂任务可以比较轨迹提示与显式状态估计。

## 相关论文

- [[Octo]]
- [[OpenVLA]]
- [[DROID]]
- [[Open_X-Embodiment]]
- [[SpatialVLA]]
- [[A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]]
- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8667f264f88c7938a73a53ab01eb1327-Abstract-Conference.html)
- 项目主页：[项目主页](https://tracevla.github.io/)
- 官方代码：[GitHub](https://github.com/umd-huang-lab/tracevla)
