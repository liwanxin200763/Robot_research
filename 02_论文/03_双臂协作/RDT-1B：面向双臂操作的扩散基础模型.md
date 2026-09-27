# RDT-1B：面向双臂操作的扩散基础模型

## 基本信息

- 英文标题：RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation
- 作者：—
- 年份：2025
- 发表 venue：ICLR
- 论文类型：会议论文
- 研究方向：双臂协作
- 论文链接：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/49f80e4d2471ad4f2edf4f5f1ab62339-Abstract-Conference.html)
- DOI：—
- arXiv：—
- 项目主页：[项目主页](https://rdt-robotics.github.io/rdt-robotics/)
- 代码：[GitHub](https://github.com/thu-ml/RoboticsDiffusionTransformer)
- 本地 PDF：[[00_论文池/PDFs/03_双臂协作/RDT-1B.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：5
- 引用量来源：OpenAlex
- 引用量来源链接：https://openalex.org/W4403364995
- 引用量查询日期：2026-09-27
- 排序引用量：5
- 排序引用量来源：OpenAlex

### 出版与分类补充

- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)

## 论文定位

这篇论文属于 VLA / Robot Foundation Models / Bimanual Manipulation / Imitation Learning / Diffusion / Flow Matching 方向，主要讨论双臂协调导致动作分布多模态，同时缺少足够训练数据。
核心思路是RDT-1B 用 Robotics Diffusion Transformer 建立双臂操作基础策略，生成协调的双臂动作。
与当前项目的联系：High：与双臂普通夹爪和真机操作直接相关。

## 核心关键词

VLA、Robot Foundation Models、Bimanual Manipulation、Imitation Learning、Diffusion、Flow Matching、Bimanual

## 快速摘要

### 研究问题

双臂协调导致动作分布多模态，同时缺少足够训练数据。

### 之前方法的问题

普通单臂策略难直接表示两臂共同运动与接触。

### 核心思路

RDT-1B 用 Robotics Diffusion Transformer 建立双臂操作基础策略，生成协调的双臂动作。

### 数据集与评测基准

论文的双臂机器人示范与真机评测；具体数据混合见原文。

### 主要结果

作者报告真机任务中优于所比较方法；摘要未给统一数值。

### 为什么重要

是项目比较双臂 Diffusion Policy 与 VLA 动作头的核心基线。

### 与当前项目的关系

High：与双臂普通夹爪和真机操作直接相关。

### 主要局限

不同夹爪、相机和动作空间的可迁移性仍需按原论文与本项目实验核验。

## 实验与结果

### 数据集与评测基准

论文的双臂机器人示范与真机评测；具体数据混合见原文。

### 主要结果

作者报告真机任务中优于所比较方法；摘要未给统一数值。

## 局限与启发

### 主要局限

不同夹爪、相机和动作空间的可迁移性仍需按原论文与本项目实验核验。

## 与当前项目的关系

High：与双臂普通夹爪和真机操作直接相关。

## 相关论文

- [[DiffusionVLA：通过统一扩散与自回归扩展机器人基础模型]]
- [[SP-VLA：通过联合模型调度与 Token 剪枝加速 VLA]]
- [[SimpleVLA-RL：通过强化学习扩展 VLA 训练]]
- [[SpatialVLA：探索 VLA 模型的空间表征]]
- [[VideoVLA：让视频生成模型成为可泛化的机器人操作策略]]
- [[AnyBimanual：迁移单臂策略以实现通用双臂操作]]
- [[从动作 Token 化视角综述 VLA 模型]]
- [[面向具身 AI 的 VLA 模型综述]]
- [[观察学习：基于视频的机器人操作学习方法综述]]
- [[迈向统一理解机器人操作：综合综述]]
- [[OpenVLA：开源视觉—语言—动作模型]]
- [[TwinVLA：以两个单臂 VLA 模型实现数据高效的双臂操作]]

## 来源

- 官方论文：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/49f80e4d2471ad4f2edf4f5f1ab62339-Abstract-Conference.html)
- 项目主页：[项目主页](https://rdt-robotics.github.io/rdt-robotics/)
- 官方代码：[GitHub](https://github.com/thu-ml/RoboticsDiffusionTransformer)
