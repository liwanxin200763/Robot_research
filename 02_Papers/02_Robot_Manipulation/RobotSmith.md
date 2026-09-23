# RobotSmith: Generative Robotic Tool Design for Acquisition of Complex Manipulation Skills

## 基本信息

- 作者：Lin, Chunru; Yuan, Haotian; Wang, Yian; Qiu, Xiaowen; Wang, Tsun-Hsuan Johnson; Guo, Minghao; Wang, Bohan; Narang, Yashraj; Fox, Dieter; Gan, Chuang
- 年份：2025
- 会议 / 期刊：NeurIPS
- CCF 等级：A
- DOI：10.52202/085713-3684
- 官方论文：https://proceedings.neurips.cc/paper_files/paper/2025/hash/9fc291fef2f9607a46777d367f900a15-Abstract-Conference.html
- 主要分类：Robot Manipulation
- 关键词：Tool Use / Generative Design

## 论文定位

这篇论文属于 Robot Manipulation 方向，主要讨论一些复杂操作需要先设计或选择合适工具，机器人现有能力不足以直接完成。
核心思路是RobotSmith 结合 VLM 中的物理常识和仿真提供的更精确物理反馈，自动设计并使用工具。
与当前项目的联系：Medium：工具规划思路可借鉴，但本项目当前重点仍是双臂普通夹爪。

## 核心关键词

Tool Use、Generative Design、Robot Manipulation

## 快速摘要

### 研究问题

一些复杂操作需要先设计或选择合适工具，机器人现有能力不足以直接完成。

### 之前方法的问题

只靠视觉语言模型可能不了解真实物理约束；只检索现有工具也会限制任务覆盖。

### 核心思路

RobotSmith 结合 VLM 中的物理常识和仿真提供的更精确物理反馈，自动设计并使用工具。

### 数据集与评测基准

工具设计与操作任务；具体任务和基线见论文实验。

### 主要结果

论文报告平均成功率 50.0%，高于 3D 生成基线 21.4% 和工具检索基线 11.1%。

### 为什么重要

展示语言模型与物理仿真协同设计工具的可能性。

### 与当前项目的关系

Medium：工具规划思路可借鉴，但本项目当前重点仍是双臂普通夹爪。

### 主要局限

摘要未明确说明全部真机失败类型和工具制造约束。

## 实验与结果

### 数据集与评测基准

工具设计与操作任务；具体任务和基线见论文实验。

### 主要结果

论文报告平均成功率 50.0%，高于 3D 生成基线 21.4% 和工具检索基线 11.1%。

## 局限与启发

### 主要局限

摘要未明确说明全部真机失败类型和工具制造约束。

## 与当前项目的关系

Medium：工具规划思路可借鉴，但本项目当前重点仍是双臂普通夹爪。

## 相关论文

- [[ManipLLM]]
- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：https://proceedings.neurips.cc/paper_files/paper/2025/hash/9fc291fef2f9607a46777d367f900a15-Abstract-Conference.html
