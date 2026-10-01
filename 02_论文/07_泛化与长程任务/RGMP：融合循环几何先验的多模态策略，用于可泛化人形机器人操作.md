# RGMP：融合循环几何先验的多模态策略，用于可泛化人形机器人操作

## 基本信息

- 英文标题：RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation
- 作者：[X Li](https://scholar.google.com/citations?user=mO2bWWQAAAAJ&hl=zh-CN&oi=sra)、W Huang、N Pan、[K Zhao](https://scholar.google.com/citations?user=0xX-rn4AAAAJ&hl=zh-CN&oi=sra)、[S Yang](https://scholar.google.com/citations?user=uGBdAbgAAAAJ&hl=zh-CN&oi=sra)等
- 年份：2026
- 发表 venue：AAAI
- 论文类型：会议论文
- 研究方向：泛化与长程任务
- 论文链接：[AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/38539)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/07_泛化与长程任务/RGMP.pdf|查看 PDF]]
- 引用量：2
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：A
- 关键词：Robot Manipulation; Humanoid / Generalization

## 论文定位

这篇论文属于 A (CCF 7th edition; venue category not independently extracted from official PDF) 方向，主要讨论通用人形机器人操作常依赖大量示范，未见场景中的几何推理仍薄弱。
核心思路是RGMP 用带几何先验的技能选择器推理子任务，再用递归 Gaussian 网络生成动作。
与当前项目的联系：Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 核心关键词

Robot Manipulation、Humanoid、Generalization、venue category not independently extracted from official PDF)、IL、Diffusion

## 快速摘要

### 研究问题

通用人形机器人操作常依赖大量示范，未见场景中的几何推理仍薄弱。

### 之前方法的问题

单纯数据驱动策略难以高效建模机器人与目标之间的空间关系。

### 核心思路

RGMP 用带几何先验的技能选择器推理子任务，再用递归 Gaussian 网络生成动作。

### 输入

官方摘要给出任务/数据类型；具体模型张量与接口需核对方法章节。

### 输出与动作

官方摘要未明确列出完整控制接口；需核对论文方法或代码。

### 数据集与评测基准

人形机器人与桌面机器人操作评测。

### 主要结果

AAAI 官方摘要报告泛化测试成功率 87%，数据效率约为所比较 SOTA 的 5 倍。

### 为什么重要

可启发双臂任务的几何关系表示，但硬件差异需要单独验证。

### 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 方法概览

任务输入 → RGMP 用带几何先验的技能选择器推理子任务，再用递归 Gaussian 网络生成动作 → 官方摘要未明确列出完整控制接口；需核对论文方法或代码。

## 实验与结果

### 数据集与评测基准

人形机器人与桌面机器人操作评测。

### 主要结果

AAAI 官方摘要报告泛化测试成功率 87%，数据效率约为所比较 SOTA 的 5 倍。

## 局限与启发

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 来源

- 官方论文：[AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/38539)
