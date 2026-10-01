# DextER：利用具身推理生成语言驱动的灵巧抓取

## 基本信息

- 英文标题：DextER: Language-driven Dexterous Grasp Generation with Embodied Reasoning
- 作者：Lee, Junha; Park, Eunha; Cho, Minsu
- 年份：2026
- 发表 venue：CVPR
- 论文类型：会议论文
- 研究方向：灵巧操作
- 论文链接：[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_DextER_Language-driven_Dexterous_Grasp_Generation_with_Embodied_Reasoning_CVPR_2026_paper.html)
- DOI：—
- arXiv：—
- 项目主页：[项目主页](https://junha-l.github.io/dexter/)
- 代码：[GitHub](https://github.com/junha-l/dexter)
- 本地 PDF：[[00_论文池/PDFs/04_灵巧操作/DextER.pdf|查看 PDF]]
- 引用量：4
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：A
- 关键词：Dexterous Hand; Contact Reasoning / Language-guided Grasp

## 论文定位

这篇论文属于 A (CCF 7th edition; venue category not independently extracted from official PDF) 方向，主要讨论语言驱动的灵巧抓取要同时理解任务语义、三维几何和接触关系。
核心思路是DextER 在抓取生成中加入基于接触的具身推理，使手部接触与任务意图对齐。
与当前项目的联系：Medium：普通夹爪也需要意图对齐，但手部接触自由度不同。

## 核心关键词

Dexterous Hand、Contact Reasoning、Language-guided Grasp、venue category not independently extracted from official PDF)、Dexterous Manipulation

## 快速摘要

### 研究问题

语言驱动的灵巧抓取要同时理解任务语义、三维几何和接触关系。

### 之前方法的问题

只预测抓取位姿未必符合语言中隐含的使用目的。

### 核心思路

DextER 在抓取生成中加入基于接触的具身推理，使手部接触与任务意图对齐。

### 数据集与评测基准

DexGYS。

### 为什么重要

将语言 Grounding 与可执行接触联系起来。

### 与当前项目的关系

Medium：普通夹爪也需要意图对齐，但手部接触自由度不同。

### 主要局限

从多指接触迁移到两只普通夹爪需重新定义动作空间。

## 实验与结果

### 数据集与评测基准

DexGYS。

## 局限与启发

### 主要局限

从多指接触迁移到两只普通夹爪需重新定义动作空间。

## 与当前项目的关系

Medium：普通夹爪也需要意图对齐，但手部接触自由度不同。

## 来源

- 官方论文：[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_DextER_Language-driven_Dexterous_Grasp_Generation_with_Embodied_Reasoning_CVPR_2026_paper.html)
- 项目主页：[项目主页](https://junha-l.github.io/dexter/)
- 官方代码：[GitHub](https://github.com/junha-l/dexter)
