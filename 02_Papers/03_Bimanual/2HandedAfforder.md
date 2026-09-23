# 2HandedAfforder: Learning Precise Actionable Bimanual Affordances from Human Videos

## 基本信息

- 作者：Heidinger, Marvin; Jauhri, Snehal; Prasad, Vignesh; Chalvatzaki, Georgia
- 年份：2025
- 会议 / 期刊：ICCV
- CCF 等级：A
- 官方论文：https://openaccess.thecvf.com/content/ICCV2025/html/Heidinger_2HandedAfforder_Learning_Precise_Actionable_Bimanual_Affordances_from_Human_Videos_ICCV_2025_paper.html
- 主要分类：Bimanual Manipulation; Robot Manipulation

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

- 官方论文：https://openaccess.thecvf.com/content/ICCV2025/html/Heidinger_2HandedAfforder_Learning_Precise_Actionable_Bimanual_Affordances_from_Human_Videos_ICCV_2025_paper.html
