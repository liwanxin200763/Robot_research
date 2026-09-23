# PointMapPolicy: Structured Point Cloud Processing for Multi-Modal Imitation Learning

## 基本信息

- 作者：Jia, Xiaogang; Wang, Qian; Wang, Anrui; Wang, Han; Gyenes, Balázs; Gospodinov, Emiliyan; Jiang, Xinkai; Li, Ge; Zhou, Hongyi; Liao, Weiran; Huang, Xi; Beck, Maximilian; Reuss, Moritz; Lioutikov, Rudolf; Neumann, Gerhard
- 年份：2025
- 会议 / 期刊：NeurIPS
- CCF 等级：A
- DOI：10.52202/085713-5353
- 官方论文：https://proceedings.neurips.cc/paper_files/paper/2025/hash/eacc8ae341d15d2c13c02fef88189db3-Abstract-Conference.html
- 主要分类：Robot Manipulation; Imitation Learning
- 关键词：3D Manipulation / Multimodal Policy

## 论文定位

这篇论文属于 Robot Manipulation; Imitation Learning 方向，主要讨论多种传感输入各有优势，如何保留点云中的局部几何信息。
核心思路是PointMapPolicy 把结构化点网格作为扩散策略条件，减少对大幅下采样的依赖。
与当前项目的联系：Medium：双臂空间定位相关，部署延迟需验证。

## 核心关键词

3D Manipulation、Multimodal Policy、Robot Manipulation、Imitation Learning

## 快速摘要

### 研究问题

多种传感输入各有优势，如何保留点云中的局部几何信息。

### 之前方法的问题

点云下采样可能丢掉接触附近的关键结构。

### 核心思路

PointMapPolicy 把结构化点网格作为扩散策略条件，减少对大幅下采样的依赖。

### 数据集与评测基准

RoboCasa、CALVIN 与真机评测。

### 主要结果

论文报告在上述 benchmark 和真机任务中取得较好表现；具体数值见正文。

### 为什么重要

有助于研究普通夹爪接触区域的三维表示。

### 与当前项目的关系

Medium：双臂空间定位相关，部署延迟需验证。

### 主要局限

高密度点数据会增加显存与在线计算成本。

## 实验与结果

### 数据集与评测基准

RoboCasa、CALVIN 与真机评测。

### 主要结果

论文报告在上述 benchmark 和真机任务中取得较好表现；具体数值见正文。

## 局限与启发

### 主要局限

高密度点数据会增加显存与在线计算成本。

## 与当前项目的关系

Medium：双臂空间定位相关，部署延迟需验证。

## 来源

- 官方论文：https://proceedings.neurips.cc/paper_files/paper/2025/hash/eacc8ae341d15d2c13c02fef88189db3-Abstract-Conference.html
