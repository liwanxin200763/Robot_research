# Dexterous Grasp Transformer

## 基本信息

- 作者：Xu, Guo-Hao; Wei, Yi-Lin; Zheng, Dian; Wu, Xiao-Ming; Zheng, Wei-Shi
- 年份：2024
- 会议 / 期刊：CVPR
- CCF 等级：A
- 官方论文：https://openaccess.thecvf.com/content/CVPR2024/html/Xu_Dexterous_Grasp_Transformer_CVPR_2024_paper.html
- 官方代码：https://github.com/iSEE-Laboratory/DGTR
- 主要分类：Dexterous Manipulation
- 关键词：Dexterous Grasping

## 论文定位

这篇论文属于 Dexterous Manipulation 方向，主要讨论灵巧手抓取不仅要可行，还要生成多样姿态。
核心思路是Dexterous Grasp Transformer 用判别式 Transformer 生成和筛选多样灵巧抓取。
与当前项目的联系：Medium：双普通夹爪也可能需要多候选抓取与可行性筛选。

## 核心关键词

Dexterous Grasping、Dexterous Manipulation

## 快速摘要

### 研究问题

灵巧手抓取不仅要可行，还要生成多样姿态。

### 之前方法的问题

单一回归结果容易忽略同一物体的多个可用抓法。

### 核心思路

Dexterous Grasp Transformer 用判别式 Transformer 生成和筛选多样灵巧抓取。

### 主要结果

作者报告保持抓取质量时，预测姿态多样性优于先前方法；具体数值需核对表格。

### 为什么重要

提醒抓取策略不应只保留单一候选动作。

### 与当前项目的关系

Medium：双普通夹爪也可能需要多候选抓取与可行性筛选。

### 主要局限

灵巧手抓取多样性指标不能直接替代双臂任务成功率。

## 实验与结果

### 主要结果

作者报告保持抓取质量时，预测姿态多样性优于先前方法；具体数值需核对表格。

## 局限与启发

### 主要局限

灵巧手抓取多样性指标不能直接替代双臂任务成功率。

## 与当前项目的关系

Medium：双普通夹爪也可能需要多候选抓取与可行性筛选。

## 相关论文

- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：https://openaccess.thecvf.com/content/CVPR2024/html/Xu_Dexterous_Grasp_Transformer_CVPR_2024_paper.html
- 官方代码：https://github.com/iSEE-Laboratory/DGTR
