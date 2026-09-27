# DexVLG：规模化灵巧视觉—语言—抓取模型

## 基本信息

- 英文标题：DexVLG: Dexterous Vision-Language-Grasp Model at Scale
- 作者：He, Jiawei; Li, Danshi; Yu, Xinqiang; Qi, Zekun; Zhang, Wenyao; Chen, Jiayi; Zhang, Zhaoxiang; Zhang, Zhizheng; Yi, Li; Wang, He
- 年份：2025
- 发表 venue：ICCV
- 论文类型：会议论文
- 研究方向：灵巧操作
- 论文链接：[CVF Open Access](https://openaccess.thecvf.com/content/ICCV2025/html/He_DexVLG_Dexterous_Vision-Language-Grasp_Model_at_Scale_ICCV_2025_paper.html)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：[GitHub](https://github.com/jiaweihe1996/DexVLG)
- 本地 PDF：[[00_论文池/PDFs/04_灵巧操作/DexVLG.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：5
- 引用量来源：OpenAlex
- 引用量来源链接：https://openalex.org/W4417183400
- 引用量查询日期：2026-09-27
- 引用量状态：已核验
- 引用量查询状态：verified
- OpenAlex Work ID：W4417183400
- 排序引用量：5
- 排序引用量来源：OpenAlex

### 出版与分类补充

- CCF 等级：A

## 论文定位

这篇论文属于 VLA; Dexterous Manipulation 方向，主要讨论高质量灵巧抓取位姿数据不足，语言与抓取动作难对齐。
核心思路是DexVLG 结合单视角 RGB-D、点云编码、Florence-2 与 Flow Matching 位姿头，预测语言条件抓取。
与当前项目的联系：Medium：Grounding 思路可迁移，手型动作头需替换。

## 核心关键词

VLA、Dexterous Manipulation、Vision-Language-Grasp、Flow Matching

## 快速摘要

### 研究问题

高质量灵巧抓取位姿数据不足，语言与抓取动作难对齐。

### 之前方法的问题

大视觉语言模型缺少足够的三维接触监督。

### 核心思路

DexVLG 结合单视角 RGB-D、点云编码、Florence-2 与 Flow Matching 位姿头，预测语言条件抓取。

### 数据集与评测基准

LVIS-Seen、LVIS-Unseen、SamPart3D。

### 为什么重要

连接视觉语言理解与三维抓取位姿生成。

### 与当前项目的关系

Medium：Grounding 思路可迁移，手型动作头需替换。

### 主要局限

结果集中于桌面抓取，长任务与普通夹爪双臂迁移未证实。

## 实验与结果

### 数据集与评测基准

LVIS-Seen、LVIS-Unseen、SamPart3D。

## 局限与启发

### 主要局限

结果集中于桌面抓取，长任务与普通夹爪双臂迁移未证实。

## 与当前项目的关系

Medium：Grounding 思路可迁移，手型动作头需替换。

## 来源

- 官方论文：[CVF Open Access](https://openaccess.thecvf.com/content/ICCV2025/html/He_DexVLG_Dexterous_Vision-Language-Grasp_Model_at_Scale_ICCV_2025_paper.html)
- 官方代码：[GitHub](https://github.com/jiaweihe1996/DexVLG)
