# Dreamitate：通过视频生成学习真实世界视觉运动策略

## 基本信息

- 英文标题：Dreamitate: Real-World Visuomotor Policy Learning via Video Generation
- 作者：—
- 年份：2024
- 发表 venue：CoRL
- 论文类型：会议论文
- 研究方向：机器人操作
- 论文链接：[PMLR](https://proceedings.mlr.press/v270/liang25b.html)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/02_机器人操作/Dreamitate.pdf|查看 PDF]]
- 引用量：123
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)

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

论文摘要未明确列出全部失败情形；具体失败条件以实验和局限章节为准。

## 实验与结果

### 数据集与评测基准

论文评估四项复杂度递增的操作任务；具体任务设置见 CoRL 论文。

### 主要结果

官方摘要报告比现有行为克隆方法具有更强的视觉环境泛化；摘要未给出统一成功率数字。

## 局限与启发

### 主要局限

论文摘要未明确列出全部失败情形；具体失败条件以实验和局限章节为准。

## 与当前项目的关系

Medium：可借鉴视频到动作的数据利用方式，但双臂普通夹爪需单独验证。

## 相关论文

- [[DROID - A Large-Scale In-The-Wild Robot Manipulation Dataset]]
- [[CoT-VLA - Visual Chain-of-Thought Reasoning for Vision-Language-Action Models]]

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v270/liang25b.html)
