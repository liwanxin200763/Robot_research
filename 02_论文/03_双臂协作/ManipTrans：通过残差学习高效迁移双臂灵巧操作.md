# ManipTrans：通过残差学习高效迁移双臂灵巧操作

## 基本信息

- 英文标题：ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning
- 作者：Li, Kailin; Li, Puhao; Liu, Tengyu; Li, Yuyang; Huang, Siyuan
- 年份：2025
- 发表 venue：CVPR
- 论文类型：会议论文
- 研究方向：双臂协作
- 论文链接：[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2025/html/Li_ManipTrans_Efficient_Dexterous_Bimanual_Manipulation_Transfer_via_Residual_Learning_CVPR_2025_paper.html)
- DOI：—
- arXiv：—
- 项目主页：[项目主页](https://maniptrans.github.io/)
- 代码：[GitHub](https://github.com/ManipTrans/ManipTrans)
- 本地 PDF：[[00_论文池/PDFs/03_双臂协作/ManipTrans.pdf|查看 PDF]]
- 引用量：106
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：A
- 关键词：Residual Learning / Sim-to-Real

## 论文定位

这篇论文属于 Bimanual Manipulation; Dexterous Manipulation 方向，主要讨论人类双手操作能力丰富，但难以直接迁移到机器人灵巧手。
核心思路是ManipTrans 用两阶段流程，在仿真中把人类双手技能迁移到机器人灵巧手策略。
与当前项目的联系：Medium：手型不同，普通夹爪适配仍需单独建模。

## 核心关键词

Residual Learning、Sim-to-Real、Bimanual Manipulation、Dexterous Manipulation

## 快速摘要

### 研究问题

人类双手操作能力丰富，但难以直接迁移到机器人灵巧手。

### 之前方法的问题

人手和机器人手的运动学、接触方式不同，逐帧模仿不能保证可执行。

### 核心思路

ManipTrans 用两阶段流程，在仿真中把人类双手技能迁移到机器人灵巧手策略。

### 数据集与评测基准

双手灵巧操作仿真任务；详细任务和基线见论文。

### 主要结果

作者报告成功率、动作保真度与训练效率优于所比较方法；摘要未给统一数字。

### 为什么重要

展示 Human Video / Human Motion 到机器人双手动作的转换思路。

### 与当前项目的关系

Medium：手型不同，普通夹爪适配仍需单独建模。

### 主要局限

仿真到真机与普通夹爪迁移尚不能从摘要确认。

## 实验与结果

### 数据集与评测基准

双手灵巧操作仿真任务；详细任务和基线见论文。

### 主要结果

作者报告成功率、动作保真度与训练效率优于所比较方法；摘要未给统一数字。

## 局限与启发

### 主要局限

仿真到真机与普通夹爪迁移尚不能从摘要确认。

## 与当前项目的关系

Medium：手型不同，普通夹爪适配仍需单独建模。

## 来源

- 官方论文：[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2025/html/Li_ManipTrans_Efficient_Dexterous_Bimanual_Manipulation_Transfer_via_Residual_Learning_CVPR_2025_paper.html)
- 项目主页：[项目主页](https://maniptrans.github.io/)
- 官方代码：[GitHub](https://github.com/ManipTrans/ManipTrans)
