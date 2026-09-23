# HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation

## 基本信息

- 年份：2025
- 会议 / 期刊：ICLR
- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 官方论文：https://proceedings.iclr.cc/paper_files/paper/2025/hash/3bfee3bc6639c36e6e7b058db909f760-Abstract-Conference.html
- 项目主页：https://hamster-robot.github.io/
- 主要分类：VLA / Robot Foundation Models / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation

## 论文定位

这篇论文属于 VLA / Robot Foundation Models / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论开放世界操作需要利用基础模型知识，但机器人动作数据昂贵。
核心思路是HAMSTER 将高层任务理解与低层动作控制分工，降低双方负担。
与当前项目的联系：High：双臂普通夹爪可能需要高层分工和低层安全控制。

## 核心关键词

VLA、Robot Foundation Models、Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

开放世界操作需要利用基础模型知识，但机器人动作数据昂贵。

### 之前方法的问题

高层 VLM 不适合直接生成精细控制，低层策略又缺少广泛语义知识。

### 核心思路

HAMSTER 将高层任务理解与低层动作控制分工，降低双方负担。

### 主要结果

论文摘要报告该分层设计改善任务执行；统一数字需查实验表。

### 为什么重要

是比较分层规划和端到端 VLA 的阅读入口。

### 与当前项目的关系

High：双臂普通夹爪可能需要高层分工和低层安全控制。

### 主要局限

高低层接口不一致会造成目标误解或执行失败。

## 实验与结果

### 主要结果

论文摘要报告该分层设计改善任务执行；统一数字需查实验表。

## 局限与启发

### 主要局限

高低层接口不一致会造成目标误解或执行失败。

## 与当前项目的关系

High：双臂普通夹爪可能需要高层分工和低层安全控制。

## 相关论文

- [[Actions_as_Language]]
- [[A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective]]
- [[A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]]
- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]
- [[SayCan]]

## 来源

- 官方论文：https://proceedings.iclr.cc/paper_files/paper/2025/hash/3bfee3bc6639c36e6e7b058db909f760-Abstract-Conference.html
- 项目主页：https://hamster-robot.github.io/
