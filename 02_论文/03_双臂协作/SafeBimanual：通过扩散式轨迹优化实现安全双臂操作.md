# SafeBimanual：通过扩散式轨迹优化实现安全双臂操作

## 基本信息

- 英文标题：SafeBimanual: Diffusion-based trajectory optimization for safe bimanual manipulation
- 作者：—
- 年份：2025
- 发表 venue：CoRL
- 论文类型：会议论文
- 研究方向：双臂协作
- 论文链接：[PMLR](https://proceedings.mlr.press/v305/deng25c.html)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/03_双臂协作/SafeBimanual.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：—
- 引用量来源：未可靠匹配
- 引用量来源链接：—
- 引用量查询日期：2026-09-27
- 引用量状态：待核验
- 引用量查询状态：pending_identity
- OpenAlex Work ID：—
- 排序引用量：—
- 排序引用量来源：未被统一来源可靠收录

### 出版与分类补充

- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)

## 论文定位

这篇论文属于 Bimanual Manipulation / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论双臂扩散策略生成的动作可能违反安全和协调约束。
核心思路是SafeBimanual 在测试时对预训练扩散策略的轨迹进行优化，加入安全约束。
与当前项目的联系：High：双臂普通夹爪真机部署需要碰撞与工作空间限制。

## 核心关键词

Bimanual Manipulation、Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、Bimanual

## 快速摘要

### 研究问题

双臂扩散策略生成的动作可能违反安全和协调约束。

### 之前方法的问题

训练完成后的策略不一定知道新的障碍物或当前碰撞边界。

### 核心思路

SafeBimanual 在测试时对预训练扩散策略的轨迹进行优化，加入安全约束。

### 数据集与评测基准

双臂扩散策略的测试时轨迹优化任务；具体 benchmark 见论文。

### 主要结果

已核验摘要未提供可安全复述的统一量化结果。

### 为什么重要

将安全约束放在策略与真机控制器之间，便于与现有策略组合。

### 与当前项目的关系

High：双臂普通夹爪真机部署需要碰撞与工作空间限制。

### 主要局限

优化耗时、约束保守程度和任务成功率之间的权衡需实测。

## 实验与结果

### 数据集与评测基准

双臂扩散策略的测试时轨迹优化任务；具体 benchmark 见论文。

### 主要结果

已核验摘要未提供可安全复述的统一量化结果。

## 局限与启发

### 主要局限

优化耗时、约束保守程度和任务成功率之间的权衡需实测。

## 与当前项目的关系

High：双臂普通夹爪真机部署需要碰撞与工作空间限制。

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v305/deng25c.html)
