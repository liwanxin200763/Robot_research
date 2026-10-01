# Policy Decorator：对大型策略模型进行模型无关的在线优化

## 基本信息

- 英文标题：Policy Decorator: Model-Agnostic Online Refinement for Large Policy Models
- 作者：[X Yuan](https://scholar.google.com/citations?user=wbq8hCUAAAAJ&hl=zh-CN&oi=sra) , [T Mu](https://scholar.google.com/citations?user=uVsZydYAAAAJ&hl=zh-CN&oi=sra) , [S Tao](https://scholar.google.com/citations?user=GAMO0EwAAAAJ&hl=zh-CN&oi=sra) , [Y Fang](https://scholar.google.com/citations?user=vrYHLMgAAAAJ&hl=zh-CN&oi=sra) , Z Zhang…
- 年份：2025
- 发表 venue：ICLR
- 论文类型：会议论文
- 研究方向：泛化与长程任务
- 论文链接：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/45c361d4117d598d4bb6568b407e9ac9-Abstract-Conference.html)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/07_泛化与长程任务/Policy_Decorator.pdf|查看 PDF]]
- 引用量：73
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)

## 论文定位

这篇论文属于 Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论大型模仿策略在新环境中仍可能出现局部失误。
核心思路是Policy Decorator 在已有模仿策略外加模型无关的 residual policy，对执行动作进行局部修正。
与当前项目的联系：High：可作为双臂 VLA 或 ACT 的附加纠错层。

## 核心关键词

Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

大型模仿策略在新环境中仍可能出现局部失误。

### 之前方法的问题

重新训练完整策略成本高，且难快速修复特定失败。

### 核心思路

Policy Decorator 在已有模仿策略外加模型无关的 residual policy，对执行动作进行局部修正。

### 数据集与评测基准

ManiSkill 与 Adroit，共八项任务。

### 主要结果

作者报告在两项 benchmark 的八个任务上提升所比较策略；具体幅度需查论文表格。

### 为什么重要

提供不改动主策略的轻量失败修正路线。

### 与当前项目的关系

High：可作为双臂 VLA 或 ACT 的附加纠错层。

### 主要局限

残差动作要经过安全限幅，避免真机接触中的突然修正。

## 实验与结果

### 数据集与评测基准

ManiSkill 与 Adroit，共八项任务。

### 主要结果

作者报告在两项 benchmark 的八个任务上提升所比较策略；具体幅度需查论文表格。

## 局限与启发

### 主要局限

残差动作要经过安全限幅，避免真机接触中的突然修正。

## 与当前项目的关系

High：可作为双臂 VLA 或 ACT 的附加纠错层。

## 来源

- 官方论文：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/45c361d4117d598d4bb6568b407e9ac9-Abstract-Conference.html)
