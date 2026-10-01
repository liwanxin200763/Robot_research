# SP-VLA：通过联合模型调度与 Token 剪枝加速 VLA

## 基本信息

- 英文标题：SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration
- 作者：[Y Li](https://scholar.google.com/citations?user=Nof6bfUAAAAJ&hl=zh-CN&oi=sra)、[Y Meng](https://scholar.google.com/citations?user=7ubFBOYAAAAJ&hl=zh-CN&oi=sra)、[Z Sun](https://scholar.google.com/citations?user=b1RbDgsAAAAJ&hl=zh-CN&oi=sra)、[K Ji](https://scholar.google.com/citations?user=bezEJJYAAAAJ&hl=zh-CN&oi=sra)、[C Tang](https://scholar.google.com/citations?user=WjZUs1AAAAAJ&hl=zh-CN&oi=sra)、[J Fan](https://scholar.google.com/citations?user=EjmzseUAAAAJ&hl=zh-CN&oi=sra)等
- 年份：2026
- 发表 venue：ICLR
- 论文类型：会议论文
- 研究方向：VLA
- 论文链接：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/4072543747a14bbed76284cf2c04b9e9-Abstract-Conference.html)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/01_VLA/SP-VLA.pdf|查看 PDF]]
- 引用量：58
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)

## 论文定位

这篇论文属于 VLA / Robot Foundation Models / Robot Manipulation 方向，主要讨论VLA 推理开销大，在线控制频率受限。
核心思路是SP-VLA 联合进行模型调度与 token 剪枝，在不同状态分配不同推理计算量。
与当前项目的联系：High：控制频率会影响双臂同步和失败恢复。

## 核心关键词

VLA、Robot Foundation Models、Robot Manipulation

## 快速摘要

### 研究问题

VLA 推理开销大，在线控制频率受限。

### 之前方法的问题

固定模型规模与统一 token 处理会浪费简单状态的计算。

### 核心思路

SP-VLA 联合进行模型调度与 token 剪枝，在不同状态分配不同推理计算量。

### 数据集与评测基准

LIBERO、SimplerEnv 与论文列出的真机任务。

### 主要结果

论文报告 LIBERO 无损加速约 1.5 倍、SimplerEnv 约 2.4 倍；平均成功率变化需按论文设置理解。

### 为什么重要

为双臂 VLA 真机控制提供延迟优化方向。

### 与当前项目的关系

High：控制频率会影响双臂同步和失败恢复。

### 主要局限

剪枝造成的少数困难状态失误，需用真实任务失败案例检验。

## 实验与结果

### 数据集与评测基准

LIBERO、SimplerEnv 与论文列出的真机任务。

### 主要结果

论文报告 LIBERO 无损加速约 1.5 倍、SimplerEnv 约 2.4 倍；平均成功率变化需按论文设置理解。

## 局限与启发

### 主要局限

剪枝造成的少数困难状态失误，需用真实任务失败案例检验。

## 与当前项目的关系

High：控制频率会影响双臂同步和失败恢复。

## 相关论文

- [[Octo：开源通用机器人策略]]
- [[OpenVLA：开源视觉—语言—动作模型]]
- [[RDT-1B：面向双臂操作的扩散基础模型]]
- [[Open X-Embodiment：机器人学习数据集与 RT-X 模型]]

## 来源

- 官方论文：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/4072543747a14bbed76284cf2c04b9e9-Abstract-Conference.html)
