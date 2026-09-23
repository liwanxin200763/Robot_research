# BimArt: A Unified Approach for the Synthesis of 3D Bimanual Interaction with Articulated Objects

## 基本信息

- 作者：Zhang, Wanyue; Dabral, Rishabh; Golyanik, Vladislav; Choutas, Vasileios; Alvarado, Eduardo; Beeler, Thabo; Habermann, Marc; Theobalt, Christian
- 年份：2025
- 会议 / 期刊：CVPR
- CCF 等级：A
- 官方论文：https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_BimArt_A_Unified_Approach_for_the_Synthesis_of_3D_Bimanual_CVPR_2025_paper.html
- 主要分类：Bimanual Manipulation; Dexterous Manipulation

## 论文定位

这篇论文属于 Bimanual Manipulation; Dexterous Manipulation 方向，主要讨论关节物体上的双手接触与运动具有多种合理方式，难以生成。
核心思路是BimArt 先根据物体轨迹生成接触距离图，再合成与关节结构一致的三维双手交互。
与当前项目的联系：Medium：手部交互可借鉴，转换为普通夹爪动作仍需验证。

## 核心关键词

Bimanual Manipulation、Dexterous Manipulation、3D Hand-Object Interaction、Articulated Objects

## 快速摘要

### 研究问题

关节物体上的双手接触与运动具有多种合理方式，难以生成。

### 之前方法的问题

只预测单个抓点不能表达物体关节运动和双手接触关系。

### 核心思路

BimArt 先根据物体轨迹生成接触距离图，再合成与关节结构一致的三维双手交互。

### 数据集与评测基准

关节物体双手交互数据；具体对象和指标见论文。

### 主要结果

摘要说明生成的接触图可以表达多样双手交互；本轮未核验统一量化结果。

### 为什么重要

为双臂支撑—操作任务提供接触表示参考。

### 与当前项目的关系

Medium：手部交互可借鉴，转换为普通夹爪动作仍需验证。

### 主要局限

人手生成结果与真实机械臂碰撞、可达性之间的关系尚需检查。

## 实验与结果

### 数据集与评测基准

关节物体双手交互数据；具体对象和指标见论文。

### 主要结果

摘要说明生成的接触图可以表达多样双手交互；本轮未核验统一量化结果。

## 局限与启发

### 主要局限

人手生成结果与真实机械臂碰撞、可达性之间的关系尚需检查。

## 与当前项目的关系

Medium：手部交互可借鉴，转换为普通夹爪动作仍需验证。

## 相关论文

- [[TACO]]

## 来源

- 官方论文：https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_BimArt_A_Unified_Approach_for_the_Synthesis_of_3D_Bimanual_CVPR_2025_paper.html
