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
- 引用量：949
- 引用量来源：Google Scholar

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

- [[DiffusionVLA - Scaling Robot Foundation Models via Unified Diffusion and Autoregression]]
- [[SP-VLA - A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration]]
- [[SimpleVLA-RL - Scaling VLA Training via Reinforcement Learning]]
- [[SpatialVLA - Exploring Spatial Representations for Visual-Language-Action Models]]
- [[VideoVLA - Video Generators Can Be Generalizable Robot Manipulators]]
- [[AnyBimanual - Transferring Unimanual Policy for General Bimanual Manipulation]]
- [[A Survey on Vision-Language-Action Models - An Action Tokenization Perspective]]
- [[A Survey on Vision-Language-Action Models for Embodied AI]]
- [[Learning by Watching - A Review of Video-Based Learning Approaches for Robot Manipulation]]
- [[Towards a Unified Understanding of Robot Manipulation - A Comprehensive Survey]]
- [[OpenVLA - An Open-Source Vision-Language-Action Model]]
- [[TwinVLA - Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models]]

## 来源

- 官方论文：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/49f80e4d2471ad4f2edf4f5f1ab62339-Abstract-Conference.html)
- 项目主页：[项目主页](https://rdt-robotics.github.io/rdt-robotics/)
- 官方代码：[GitHub](https://github.com/thu-ml/RoboticsDiffusionTransformer)
