# UniDomain：从真实示范预训练统一 PDDL 域以实现可泛化任务规划

## 基本信息

- 英文标题：UniDomain: Pretraining a Unified PDDL Domain from Real-World Demonstrations for Generalizable Robot Task Planning
- 作者：Ye, Haoming; Xiao, Yunxiao; Lu, Cewu; Cai, Panpan
- 年份：2025
- 发表 venue：NeurIPS
- 论文类型：会议论文
- 研究方向：泛化与长程任务
- 论文链接：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b8358a00e5b870194b974ddf8dd415c3-Abstract-Conference.html)
- DOI：10.52202/085713-4226 — [DOI](https://doi.org/10.52202/085713-4226)
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/07_泛化与长程任务/UniDomain.pdf|查看 PDF]]
- 引用量：7
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：A
- 关键词：Task Planning / Demonstrations

## 论文定位

这篇论文属于 Robot Manipulation; Generalization 方向，主要讨论真实机器人规划要理解语言和视觉中没有明说的约束。
核心思路是UniDomain 从机器人示范中预训练 PDDL domain，再用于零样本任务规划。
与当前项目的联系：Medium：可帮助双臂任务定义前提与执行检查。

## 核心关键词

Task Planning、Demonstrations、Robot Manipulation、Generalization

## 快速摘要

### 研究问题

真实机器人规划要理解语言和视觉中没有明说的约束。

### 之前方法的问题

人工写 PDDL 领域规则成本高，面对未见任务又易遗漏条件。

### 核心思路

UniDomain 从机器人示范中预训练 PDDL domain，再用于零样本任务规划。

### 主要结果

作者报告在多项真实任务中解决未见复杂任务；具体成功率见论文。

### 为什么重要

为从示范自动获得可解释规划约束提供方法。

### 与当前项目的关系

Medium：可帮助双臂任务定义前提与执行检查。

### 主要局限

推断的规则若不准确，计划可能在真机接触时失败。

## 实验与结果

### 主要结果

作者报告在多项真实任务中解决未见复杂任务；具体成功率见论文。

## 局限与启发

### 主要局限

推断的规则若不准确，计划可能在真机接触时失败。

## 与当前项目的关系

Medium：可帮助双臂任务定义前提与执行检查。

## 来源

- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b8358a00e5b870194b974ddf8dd415c3-Abstract-Conference.html)
