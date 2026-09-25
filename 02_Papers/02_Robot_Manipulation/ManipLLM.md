# ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation

## 基本信息

- 作者：Li, Xiaoqi; Zhang, Mingxu; Geng, Yiran; Geng, Haoran; Long, Yuxing; Shen, Yan; Zhang, Renrui; Liu, Jiaming; Dong, Hao
- 年份：2024
- 会议 / 期刊：CVPR
- CCF 等级：A
- 官方论文：[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.html)
- 项目主页：[项目主页](https://sites.google.com/view/manipllm)
- 官方代码：[GitHub](https://github.com/clorislili/ManipLLM)
- 主要分类：Robot Manipulation
- 关键词：Multimodal / Generalization


- 引用量：82
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/02_Robot_Manipulation/ManipLLM.pdf]]
## 论文定位

这篇论文属于 Robot Manipulation 方向，主要讨论多模态大模型能理解图像和语言，但不一定能给出可执行的接触点与夹爪姿态。
核心思路是ManipLLM 结合物体类别识别、affordance 推理和位姿微调，预测接触点与夹爪朝向，并通过分步推理和主动交互改进执行。
与当前项目的联系：High：直接对应夹爪接触点、动作前可行性验证和真机操作。

## 核心关键词

Multimodal、Generalization、Robot Manipulation

## 快速摘要

### 研究问题

多模态大模型能理解图像和语言，但不一定能给出可执行的接触点与夹爪姿态。

### 之前方法的问题

物体级 Grounding 与精确接触几何没有自然地从语言推理转成机器人动作。

### 核心思路

ManipLLM 结合物体类别识别、affordance 推理和位姿微调，预测接触点与夹爪朝向，并通过分步推理和主动交互改进执行。

### 输入

物体视觉信息与操作指令；具体相机和状态接口见论文方法。

### 输出与动作

接触点、夹爪朝向及后续操作位姿。

### 数据集与评测基准

论文中的物体操作任务与消融设置；具体数据集名称见原卡实验部分。

### 为什么重要

让语言推理落到普通夹爪可执行的接触几何上。

### 与当前项目的关系

High：直接对应夹爪接触点、动作前可行性验证和真机操作。

### 主要局限

作者指出视觉位置预测仍受域变化影响；特定吸盘硬件约束需要测试时适配。

## 方法概览

任务输入 → ManipLLM 结合物体类别识别、affordance 推理和位姿微调，预测接触点与夹爪朝向，并通过分步推理和主动交互改进执行 → 接触点、夹爪朝向及后续操作位姿。

## 实验与结果

### 数据集与评测基准

论文中的物体操作任务与消融设置；具体数据集名称见原卡实验部分。

## 局限与启发

### 主要局限

作者指出视觉位置预测仍受域变化影响；特定吸盘硬件约束需要测试时适配。

## 与当前项目的关系

High：直接对应夹爪接触点、动作前可行性验证和真机操作。

## 相关论文

- [[MoManipVLA]]
- [[RoboMamba]]
- [[RobotSmith]]
- [[A_Survey_of_Embodied_Learning_for_Object-Centric_Robotic_Manipulation]]
- [[A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective]]
- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.html)
- 项目主页：[项目主页](https://sites.google.com/view/manipllm)
- 官方代码：[GitHub](https://github.com/clorislili/ManipLLM)
