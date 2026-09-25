# BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models

## 基本信息

- 作者：Li, Peiyan; Chen, Yixiang; Wu, Hongtao; Ma, Xiao; Wu, Xiangnan; Huang, Yan; Wang, Liang; Kong, Tao; Tan, Tieniu
- 年份：2025
- 会议 / 期刊：NeurIPS
- CCF 等级：A
- DOI：10.52202/085713-2137 — [DOI](https://doi.org/10.52202/085713-2137)
- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5c1a8aa04c1a2cf5013f28831870dafa-Abstract-Conference.html)
- 项目主页：[项目主页](https://bridgevla.github.io/)
- 官方代码：[GitHub](https://github.com/BridgeVLA/BridgeVLA/tree/bridgevla)
- 主要分类：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 关键词：VLA; 3D Manipulation / Data Efficiency


- 引用量：0
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/01_VLA/BridgeVLA.pdf]]
## 论文定位

这篇论文属于 A (CCF 7th edition; venue category not independently extracted from official PDF) 方向，主要讨论许多 VLA 对三维空间信息的利用不足，影响操作动作的空间准确性与数据效率。
核心思路是BridgeVLA 研究视觉语言模型与三维输入/输出的对齐，让空间结构参与动作预测。
与当前项目的联系：High：有助于研究语言条件操作与 VLA 设计。

## 核心关键词

VLA、3D Manipulation、Data Efficiency、venue category not independently extracted from official PDF)、Robot Foundation Models

## 快速摘要

### 研究问题

许多 VLA 对三维空间信息的利用不足，影响操作动作的空间准确性与数据效率。

### 之前方法的问题

一些 3D VLA 尚未充分利用三维数据自带的空间结构，影响动作预测的数据效率。

### 核心思路

BridgeVLA 研究视觉语言模型与三维输入/输出的对齐，让空间结构参与动作预测。

### 数据集与评测基准

论文评估 RLBench、COLOSSEUM 与 GemBench；预训练数据和下载入口以官方仓库说明为准。

### 为什么重要

为 VLA 如何利用三维几何信息提供了可比较的基线。

### 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

### 主要局限

作者把更充分的 3D 输入/输出对齐与训练效率列为后续方向；当前结果主要验证于报告的 Franka 设置。

## 实验与结果

### 数据集与评测基准

论文评估 RLBench、COLOSSEUM 与 GemBench；预训练数据和下载入口以官方仓库说明为准。

## 局限与启发

### 主要局限

作者把更充分的 3D 输入/输出对齐与训练效率列为后续方向；当前结果主要验证于报告的 Franka 设置。

## 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

## 相关论文

- [[3D-VLA]]
- [[OpenVLA]]
- [[3D_Diffuser_Actor]]
- [[THE_COLOSSEUM]]
- [[A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]]
- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5c1a8aa04c1a2cf5013f28831870dafa-Abstract-Conference.html)
- 项目主页：[项目主页](https://bridgevla.github.io/)
- 官方代码：[GitHub](https://github.com/BridgeVLA/BridgeVLA/tree/bridgevla)
