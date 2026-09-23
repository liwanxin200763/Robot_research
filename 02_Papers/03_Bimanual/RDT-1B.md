# RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation

## 基本信息

- 年份：2025
- 会议 / 期刊：ICLR
- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 官方论文：https://proceedings.iclr.cc/paper_files/paper/2025/hash/49f80e4d2471ad4f2edf4f5f1ab62339-Abstract-Conference.html
- 项目主页：https://rdt-robotics.github.io/rdt-robotics/
- 官方代码：https://github.com/thu-ml/RoboticsDiffusionTransformer
- 主要分类：VLA / Robot Foundation Models / Bimanual Manipulation / Imitation Learning / Diffusion / Flow Matching

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

- [[DiffusionVLA]]
- [[SP-VLA]]
- [[SimpleVLA-RL]]
- [[SpatialVLA]]
- [[VideoVLA]]
- [[AnyBimanual]]
- [[A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective]]
- [[A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]]
- [[Learning_by_Watching]]
- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]
- [[OpenVLA]]
- [[TwinVLA]]

## 来源

- 官方论文：https://proceedings.iclr.cc/paper_files/paper/2025/hash/49f80e4d2471ad4f2edf4f5f1ab62339-Abstract-Conference.html
- 项目主页：https://rdt-robotics.github.io/rdt-robotics/
- 官方代码：https://github.com/thu-ml/RoboticsDiffusionTransformer
