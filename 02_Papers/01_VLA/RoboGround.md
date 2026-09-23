# RoboGround: Robotic Manipulation with Grounded Vision-Language Priors

## 基本信息

- 作者：Huang, Haifeng; Chen, Xinyi; Chen, Yilun; Li, Hao; Han, Xiaoshen; Wang, Zehan; Wang, Tai; Pang, Jiangmiao; Zhao, Zhou
- 年份：2025
- 会议 / 期刊：CVPR
- CCF 等级：A
- 官方论文：https://openaccess.thecvf.com/content/CVPR2025/html/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.html
- 主要分类：Robot Manipulation; Generalization
- 关键词：Grounding / Synthetic Data

## 论文定位

这篇论文属于 Robot Manipulation; Generalization 方向，主要讨论机器人策略需要可靠地定位目标物体与放置区域，才能在新场景中泛化。
核心思路是RoboGround 使用 Grounding mask 作为中间表示，向操作策略提供目标及空间形状信息。
与当前项目的联系：High：有助于研究语言条件操作与 VLA 设计。

## 核心关键词

Grounding、Synthetic Data、Robot Manipulation、Generalization

## 快速摘要

### 研究问题

机器人策略需要可靠地定位目标物体与放置区域，才能在新场景中泛化。

### 之前方法的问题

只靠最终动作监督，策略未必能学会稳定识别目标物体和放置区域。

### 核心思路

RoboGround 使用 Grounding mask 作为中间表示，向操作策略提供目标及空间形状信息。

### 主要结果

官方摘要报告 Grounding mask 能改善策略泛化；快速摘要不填入未核对实验表的数字。

### 为什么重要

可与 ReconVLA 比较“显式 mask”与“隐式目标区域重建”两种 Grounding 路线。

### 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

### 主要局限

合成数据和 mask 质量会影响迁移；真机覆盖范围仍需按论文实验表核验。

## 实验与结果

### 主要结果

官方摘要报告 Grounding mask 能改善策略泛化；快速摘要不填入未核对实验表的数字。

## 局限与启发

### 主要局限

合成数据和 mask 质量会影响迁移；真机覆盖范围仍需按论文实验表核验。

## 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

## 相关论文

- [[OpenVLA]]
- [[Closed-Loop_Visuomotor_Control_with_Generative_Expectation_for_Robotic_Manipulation]]
- [[RoboCasa]]
- [[ReconVLA]]

## 来源

- 官方论文：https://openaccess.thecvf.com/content/CVPR2025/html/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.html
