# RoboGround：利用有视觉定位能力的视觉—语言先验实现机器人操作

## 基本信息

- 英文标题：RoboGround: Robotic Manipulation with Grounded Vision-Language Priors
- 作者：Huang, Haifeng; Chen, Xinyi; Chen, Yilun; Li, Hao; Han, Xiaoshen; Wang, Zehan; Wang, Tai; Pang, Jiangmiao; Zhao, Zhou
- 年份：2025
- 发表 venue：CVPR
- 论文类型：会议论文
- 研究方向：VLA
- 论文链接：[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2025/html/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.html)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/01_VLA/RoboGround.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：10
- 引用量来源：OpenAlex
- 引用量来源链接：https://openalex.org/W4413147462
- 引用量查询日期：2026-09-27
- 引用量状态：已核验
- 排序引用量：10
- 排序引用量来源：OpenAlex

### 出版与分类补充

- CCF 等级：A
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

- [[OpenVLA：开源视觉—语言—动作模型]]
- [[通过生成式预期实现机器人操作的闭环视觉运动控制]]
- [[RoboCasa：面向通用机器人的大规模家务任务仿真]]
- [[ReconVLA：以重建增强机器人感知的 VLA 模型]]

## 来源

- 官方论文：[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2025/html/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.html)
