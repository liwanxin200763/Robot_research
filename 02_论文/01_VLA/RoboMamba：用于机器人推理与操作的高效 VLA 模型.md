# RoboMamba：用于机器人推理与操作的高效 VLA 模型

## 基本信息

- 英文标题：RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation
- 作者：Liu, Jiaming; Liu, Mengzhen; Wang, Zhenyu; An, Pengju; Li, Xiaoqi; Zhou, Kaichen; Yang, Senqiao; Zhang, Renrui; Guo, Yandong; Zhang, Shanghang
- 年份：2024
- 发表 venue：NeurIPS
- 论文类型：会议论文
- 研究方向：VLA
- 论文链接：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html)
- DOI：10.52202/079017-1266 — [DOI](https://doi.org/10.52202/079017-1266)
- arXiv：—
- 项目主页：[项目主页](https://sites.google.com/view/robomamba-web)
- 代码：[GitHub](https://github.com/lmzpai/roboMamba)
- 本地 PDF：[[00_论文池/PDFs/01_VLA/RoboMamba.pdf|查看 PDF]]
- 引用量：164
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：A
- 关键词：VLA; Efficient Model / Pose Prediction

## 论文定位

这篇论文属于 A (CCF 7th edition; venue category not independently extracted from official PDF) 方向，主要讨论VLA 要兼顾视觉语言推理、动作预测和可承受的微调/推理成本。
核心思路是RoboMamba 以 Mamba 架构建立端到端 VLA，重点降低适配和在线推理成本。
与当前项目的联系：High：有助于研究语言条件操作与 VLA 设计。

## 核心关键词

VLA、Efficient Model、Pose Prediction、venue category not independently extracted from official PDF)、Robot Foundation Models

## 快速摘要

### 研究问题

VLA 要兼顾视觉语言推理、动作预测和可承受的微调/推理成本。

### 之前方法的问题

已有 VLA 在复杂任务推理与微调计算成本之间存在权衡。

### 核心思路

RoboMamba 以 Mamba 架构建立端到端 VLA，重点降低适配和在线推理成本。

### 主要结果

论文报告在仿真与真机姿态预测任务中优于所比较 VLA，推理速度约为其 3 倍；具体比较对象见原文。

### 为什么重要

可作为部署时的速度—能力权衡参考。

### 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

## 实验与结果

### 主要结果

论文报告在仿真与真机姿态预测任务中优于所比较 VLA，推理速度约为其 3 倍；具体比较对象见原文。

## 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

## 相关论文

- [[OpenVLA：开源视觉—语言—动作模型]]
- [[SayCan：以机器人能力约束语言指令的落地执行]]
- [[02_论文/02_机器人操作/ManipLLM：面向物体中心机器人操作的具身多模态大语言模型|ManipLLM：面向物体中心机器人操作的具身多模态大语言模型]]
- [[从动作 Token 化视角综述 VLA 模型]]
- [[面向具身 AI 的 VLA 模型综述]]
- [[迈向统一理解机器人操作：综合综述]]

## 来源

- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html)
- 项目主页：[项目主页](https://sites.google.com/view/robomamba-web)
- 官方代码：[GitHub](https://github.com/lmzpai/roboMamba)
