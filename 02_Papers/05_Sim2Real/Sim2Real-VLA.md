# Sim2Real-VLA: Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation

## 基本信息

- 作者：Runyi Zhao; Sheng Xu; Ruixing Jin; Yueci Deng; Yunxin Tai; Kui Jia; Guiliang Liu
- 年份：2026
- 会议 / 期刊：ICLR
- 官方论文：https://openreview.net/pdf/a4174c2964dc0df03c26c311b73e0a2e43de2929.pdf
- 项目主页：https://edem-ai.github.io/sim2realvla.github.io/
- 官方代码：https://github.com/DexForce/EmbodiChain
- 主要分类：VLA
- 关键词：VLA; Sim2Real; Robot Manipulation; Synthetic Data; Generalization; Bimanual; Dexterous; Long-horizon
- 特别关注：是

## 论文定位

这篇论文属于 VLA 方向，主要讨论纯合成数据训练的 VLA 在真实场景中容易受到外观和动力学差异影响。
核心思路是Sim2Real-VLA 只用合成数据训练通用控制模型，并研究仿真技能迁移到真实操作。
与当前项目的联系：High：直接关联双臂普通夹爪、VLA 或真机操作。

## 核心关键词

VLA、Sim2Real、Robot Manipulation、Synthetic Data、Generalization、Bimanual、Dexterous、Long-horizon

## 快速摘要

### 研究问题

纯合成数据训练的 VLA 在真实场景中容易受到外观和动力学差异影响。

### 之前方法的问题

仿真里学到的操作技能并不自动具备真机零样本泛化。

### 核心思路

Sim2Real-VLA 只用合成数据训练通用控制模型，并研究仿真技能迁移到真实操作。

### 输入

官方摘要给出任务/数据类型；具体模型张量与接口需核对方法章节。

### 输出与动作

官方摘要未明确列出完整控制接口；需核对论文方法或代码。

### 数据集与评测基准

合成操作轨迹与真实机器人评测；具体任务见项目页。

### 主要结果

作者项目页报告多种真实操作任务的零样本迁移；完整数值和硬件条件仍需正文核验。

### 为什么重要

直接对应双臂 Sim2Real 与合成/真实数据配比问题。

### 与当前项目的关系

High：直接关联双臂普通夹爪、VLA 或真机操作。

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 方法概览

任务输入 → Sim2Real-VLA 只用合成数据训练通用控制模型，并研究仿真技能迁移到真实操作 → 官方摘要未明确列出完整控制接口；需核对论文方法或代码。

## 实验与结果

### 数据集与评测基准

合成操作轨迹与真实机器人评测；具体任务见项目页。

### 主要结果

作者项目页报告多种真实操作任务的零样本迁移；完整数值和硬件条件仍需正文核验。

## 局限与启发

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 与当前项目的关系

High：直接关联双臂普通夹爪、VLA 或真机操作。

## 相关论文

- [[OpenVLA]]

## 来源

- 官方论文：https://openreview.net/pdf/a4174c2964dc0df03c26c311b73e0a2e43de2929.pdf
- 项目主页：https://edem-ai.github.io/sim2realvla.github.io/
- 官方代码：https://github.com/DexForce/EmbodiChain
