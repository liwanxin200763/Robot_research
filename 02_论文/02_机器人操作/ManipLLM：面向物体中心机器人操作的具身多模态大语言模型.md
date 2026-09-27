# ManipLLM：面向物体中心机器人操作的具身多模态大语言模型

## 基本信息

- 英文标题：ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation
- 作者：Li, Xiaoqi; Zhang, Mingxu; Geng, Yiran; Geng, Haoran; Long, Yuxing; Shen, Yan; Zhang, Renrui; Liu, Jiaming; Dong, Hao
- 年份：2024
- 发表 venue：CVPR
- 论文类型：会议论文
- 研究方向：机器人操作
- 论文链接：[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.html)
- DOI：—
- arXiv：—
- 项目主页：[项目主页](https://sites.google.com/view/manipllm)
- 代码：[GitHub](https://github.com/clorislili/ManipLLM)
- 本地 PDF：[[00_论文池/PDFs/02_机器人操作/ManipLLM.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：82
- 引用量来源：OpenAlex
- 引用量来源链接：https://openalex.org/W4402727730
- 引用量查询日期：2026-09-27
- 引用量状态：已核验
- 排序引用量：82
- 排序引用量来源：OpenAlex

### 出版与分类补充

- CCF 等级：A
- 关键词：Multimodal / Generalization

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

- [[MoManipVLA：迁移 VLA 模型以实现通用移动操作]]
- [[RoboMamba：用于机器人推理与操作的高效 VLA 模型]]
- [[RobotSmith：通过生成式机器人工具设计习得复杂操作技能]]
- [[面向物体中心机器人操作的具身学习综述]]
- [[从动作 Token 化视角综述 VLA 模型]]
- [[迈向统一理解机器人操作：综合综述]]

## 来源

- 官方论文：[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.html)
- 项目主页：[项目主页](https://sites.google.com/view/manipllm)
- 官方代码：[GitHub](https://github.com/clorislili/ManipLLM)
