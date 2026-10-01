# ALOHA Unleashed：实现机器人灵巧操作的简明方法

## 基本信息

- 英文标题：ALOHA Unleashed: A Simple Recipe for Robot Dexterity
- 作者：—
- 年份：2024
- 发表 venue：CoRL
- 论文类型：会议论文
- 研究方向：双臂协作
- 论文链接：[PMLR](https://proceedings.mlr.press/v270/zhao25b.html)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/03_双臂协作/ALOHA_Unleashed.pdf|查看 PDF]]
- 引用量：273
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)

## 论文定位

这篇论文属于 Bimanual Manipulation / Dexterous Manipulation / Dexterous Hand / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论复杂灵巧操作需要足够多的真机示范和能表达多种动作的策略。
核心思路是在 ALOHA 2 平台扩大数据采集，再用 Diffusion Policy 等表达能力较强的策略学习操作。
与当前项目的联系：High：硬件形态与本项目双臂普通夹爪接近。

## 核心关键词

Bimanual Manipulation、Dexterous Manipulation、Dexterous Hand、Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、Bimanual

## 快速摘要

### 研究问题

复杂灵巧操作需要足够多的真机示范和能表达多种动作的策略。

### 之前方法的问题

小规模模仿学习数据难以覆盖长任务与接触变化。

### 核心思路

在 ALOHA 2 平台扩大数据采集，再用 Diffusion Policy 等表达能力较强的策略学习操作。

### 数据集与评测基准

ALOHA 2 真机示范和论文列出的复杂操作任务。

### 主要结果

论文报告扩大数据规模与扩散策略组合能完成更具挑战性的操作；具体成功率见原文实验。

### 为什么重要

提供真机双臂示范规模与策略能力的实证对照。

### 与当前项目的关系

High：硬件形态与本项目双臂普通夹爪接近。

### 主要局限

不同任务、相机与夹爪配置之间的迁移仍需单独评测。

## 实验与结果

### 数据集与评测基准

ALOHA 2 真机示范和论文列出的复杂操作任务。

### 主要结果

论文报告扩大数据规模与扩散策略组合能完成更具挑战性的操作；具体成功率见原文实验。

## 局限与启发

### 主要局限

不同任务、相机与夹爪配置之间的迁移仍需单独评测。

## 与当前项目的关系

High：硬件形态与本项目双臂普通夹爪接近。

## 相关论文

- [[DexCap：面向灵巧操作的可扩展便携式动作捕捉数据采集系统]]
- [[DROID：大规模自然场景机器人操作数据集]]
- [[Open X-Embodiment：机器人学习数据集与 RT-X 模型]]
- [[DiffusionVLA：通过统一扩散与自回归扩展机器人基础模型]]
- [[COMBO-Grasp：学习约束式操作以完成双臂遮挡抓取]]

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v270/zhao25b.html)
