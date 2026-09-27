# 2HandedAfforder：从人类视频学习精确可执行的双臂可供性

## 基本信息

- 英文标题：2HandedAfforder: Learning Precise Actionable Bimanual Affordances from Human Videos
- 作者：Heidinger, Marvin; Jauhri, Snehal; Prasad, Vignesh; Chalvatzaki, Georgia
- 年份：2025
- 发表 venue：ICCV
- 论文类型：会议论文
- 研究方向：双臂协作
- 论文链接：[CVF Open Access](https://openaccess.thecvf.com/content/ICCV2025/html/Heidinger_2HandedAfforder_Learning_Precise_Actionable_Bimanual_Affordances_from_Human_Videos_ICCV_2025_paper.html)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/03_双臂协作/2HandedAfforder.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：0
- 引用量来源：OpenAlex
- 引用量来源链接：https://openalex.org/W4416031407
- 引用量查询日期：2026-09-27
- 引用量状态：已核验
- 引用量查询状态：verified_zero
- OpenAlex Work ID：W4416031407
- 排序引用量：0
- 排序引用量来源：OpenAlex

### 出版与分类补充

- CCF 等级：A

## 论文定位

这篇论文属于 Bimanual Manipulation; Robot Manipulation 方向，主要讨论人类视频包含丰富双手交互，但普通 affordance 标签难指出左右手各自可操作的区域。
核心思路是用 VLM 产生分割提示，再由左右手 mask 解码器预测可执行区域，并分类单手或双手交互。
与当前项目的联系：High：可用于双臂 joint affordance 和动作前检查。

## 核心关键词

Bimanual Manipulation、Robot Manipulation、Human Video、Affordance

## 快速摘要

### 研究问题

人类视频包含丰富双手交互，但普通 affordance 标签难指出左右手各自可操作的区域。

### 之前方法的问题

只标记物体可抓取，不足以指导双手分工和具体接触位置。

### 核心思路

用 VLM 产生分割提示，再由左右手 mask 解码器预测可执行区域，并分类单手或双手交互。

### 数据集与评测基准

ActAffordance 等双手 affordance 评测；具体分数见官方 PDF。

### 主要结果

已访问的官方 PDF 支持方法与评测设置；快速摘要暂不填入未重新提取的数值。

### 为什么重要

直接关系到普通夹爪在同一物体上的双臂接触分工。

### 与当前项目的关系

High：可用于双臂 joint affordance 和动作前检查。

### 主要局限

精确数值与失败图例仍需对照论文图表；人手区域到普通夹爪的迁移需验证。

## 实验与结果

### 数据集与评测基准

ActAffordance 等双手 affordance 评测；具体分数见官方 PDF。

### 主要结果

已访问的官方 PDF 支持方法与评测设置；快速摘要暂不填入未重新提取的数值。

## 局限与启发

### 主要局限

精确数值与失败图例仍需对照论文图表；人手区域到普通夹爪的迁移需验证。

## 与当前项目的关系

High：可用于双臂 joint affordance 和动作前检查。

## 来源

- 官方论文：[CVF Open Access](https://openaccess.thecvf.com/content/ICCV2025/html/Heidinger_2HandedAfforder_Learning_Precise_Actionable_Bimanual_Affordances_from_Human_Videos_ICCV_2025_paper.html)
