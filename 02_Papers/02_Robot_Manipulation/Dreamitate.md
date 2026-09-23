# Dreamitate: Real-World Visuomotor Policy Learning via Video Generation

## 基本信息

- 年份：2024
- 会议 / 期刊：CoRL
- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)
- 官方论文：https://proceedings.mlr.press/v270/liang24a.html
- 主要分类：VLA / Robot Foundation Models / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation

## 论文定位

这篇论文属于 VLA / Robot Foundation Models / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论机器人模仿学习策略在新视觉环境中往往难以保持稳定表现。
核心思路是Dreamitate 用人类任务示范微调视频扩散模型，再利用生成的视频辅助学习视觉运动策略。
与当前项目的联系：Medium：可借鉴视频到动作的数据利用方式，但双臂普通夹爪需单独验证。

## 核心关键词

VLA、Robot Foundation Models、Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

机器人模仿学习策略在新视觉环境中往往难以保持稳定表现。

### 之前方法的问题

少量机器人示范不足以覆盖环境外观变化；直接行为克隆的泛化有限。

### 核心思路

Dreamitate 用人类任务示范微调视频扩散模型，再利用生成的视频辅助学习视觉运动策略。

### 数据集与评测基准

论文评估四项复杂度递增的操作任务；具体任务设置见 CoRL 论文。

### 主要结果

官方摘要报告比现有行为克隆方法具有更强的视觉环境泛化；摘要未给出统一成功率数字。

### 为什么重要

探索大规模视频生成模型如何补充少量机器人示范。

### 与当前项目的关系

Medium：可借鉴视频到动作的数据利用方式，但双臂普通夹爪需单独验证。

### 主要局限

已核验摘要未明确列出全部失败情形；需读实验和局限章节。

## 实验与结果

### 数据集与评测基准

论文评估四项复杂度递增的操作任务；具体任务设置见 CoRL 论文。

### 主要结果

官方摘要报告比现有行为克隆方法具有更强的视觉环境泛化；摘要未给出统一成功率数字。

## 局限与启发

### 主要局限

已核验摘要未明确列出全部失败情形；需读实验和局限章节。

## 与当前项目的关系

Medium：可借鉴视频到动作的数据利用方式，但双臂普通夹爪需单独验证。

## 相关论文

- [[DROID]]
- [[CoT-VLA]]

## 来源

- 官方论文：https://proceedings.mlr.press/v270/liang24a.html
