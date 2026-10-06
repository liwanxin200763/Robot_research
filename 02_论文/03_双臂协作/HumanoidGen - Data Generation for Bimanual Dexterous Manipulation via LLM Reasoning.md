# HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning

## 基本信息

- 作者：Jing, Zhi; Yang, Siyuan; Ao, Jicong; Xiao, Ting; Jiang, Yu-Gang; Bai, Chenjia
- 年份：2025
- 发表 venue：NeurIPS
- 论文类型：会议论文
- 研究方向：双臂协作
- 论文链接：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e4ef7454447baa15a424314e6284441b-Abstract-Conference.html)
- DOI：10.52202/085713-5220 — [DOI](https://doi.org/10.52202/085713-5220)
- arXiv：—
- 项目主页：[项目主页](https://openhumanoidgen.github.io)
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/03_双臂协作/HumanoidGen.pdf|查看 PDF]]
- 引用量：17
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：A

## 论文定位

这篇论文属于 Bimanual Manipulation; Dexterous Manipulation; Dataset / Benchmark 方向，主要讨论许多机器人操作数据和仿真 benchmark 偏机械臂，缺少人形机器人操作数据。
核心思路是HumanoidGen 扩展人形机器人操作数据，用生成数据训练和评估 2D/3D Diffusion Policy。
与当前项目的联系：Medium：本项目不是人形手，但双臂数据覆盖问题相通。

## 核心关键词

Bimanual Manipulation、Dexterous Manipulation、Dataset、Benchmark、Humanoid、Synthetic Demonstrations、LLM Planning

## 快速摘要

### 研究问题

许多机器人操作数据和仿真 benchmark 偏机械臂，缺少人形机器人操作数据。

### 之前方法的问题

数据本体分布不足会限制策略对人形平台的适配。

### 核心思路

HumanoidGen 扩展人形机器人操作数据，用生成数据训练和评估 2D/3D Diffusion Policy。

### 数据集与评测基准

生成的人形操作数据；具体任务与数据规模见论文。

### 主要结果

摘要报告 2D 与 3D 扩散策略表现会随生成数据增加而提升；未核验统一成功率。

### 为什么重要

提醒跨本体数据设计比单纯增加示范数量更重要。

### 与当前项目的关系

Medium：本项目不是人形手，但双臂数据覆盖问题相通。

### 主要局限

仿真生成数据到普通夹爪真机的迁移需另行验证。

## 实验与结果

### 数据集与评测基准

生成的人形操作数据；具体任务与数据规模见论文。

### 主要结果

摘要报告 2D 与 3D 扩散策略表现会随生成数据增加而提升；未核验统一成功率。

## 局限与启发

### 主要局限

仿真生成数据到普通夹爪真机的迁移需另行验证。

## 与当前项目的关系

Medium：本项目不是人形手，但双臂数据覆盖问题相通。

## 相关论文

- [[Towards a Unified Understanding of Robot Manipulation - A Comprehensive Survey]]

## 来源

- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e4ef7454447baa15a424314e6284441b-Abstract-Conference.html)
- 项目主页：[项目主页](https://openhumanoidgen.github.io)
