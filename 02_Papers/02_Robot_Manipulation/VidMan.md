# VidMan: Exploiting Implicit Dynamics from Video Diffusion Model for Effective Robot Manipulation

## 基本信息

- 作者：Wen, Youpeng; Lin, Junfan; Zhu, Yi; Han, Jianhua; Xu, Hang; Zhao, Shen; Liang, Xiaodan
- 年份：2024
- 会议 / 期刊：NeurIPS
- CCF 等级：A
- DOI：10.52202/079017-1298 — [DOI](https://doi.org/10.52202/079017-1298)
- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/481c70828a4ff20d31a646cc6cc95f3d-Abstract-Conference.html)
- 主要分类：Robot Manipulation; VLA
- 关键词：World Model / Video Diffusion


- 引用量：3
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/02_Robot_Manipulation/VidMan.pdf]]
## 论文定位

这篇论文属于 Robot Manipulation; VLA 方向，主要讨论机器人需要利用视频数据理解物理动态并改进操作动作预测。
核心思路是VidMan 使用两阶段训练，将视频扩散模型的动态表征引入机器人操作策略。
与当前项目的联系：Medium：可帮助研究视觉预测是否改善双臂操作，但真机适配需验证。

## 核心关键词

World Model、Video Diffusion、Robot Manipulation、VLA

## 快速摘要

### 研究问题

机器人需要利用视频数据理解物理动态并改进操作动作预测。

### 之前方法的问题

单纯视频生成不保证生成的表示能直接帮助稳定的机器人控制。

### 核心思路

VidMan 使用两阶段训练，将视频扩散模型的动态表征引入机器人操作策略。

### 数据集与评测基准

CALVIN 与 OXE 小规模数据评测；具体任务和数据划分见论文。

### 为什么重要

为从视频世界模型到动作策略的连接提供对照方法。

### 与当前项目的关系

Medium：可帮助研究视觉预测是否改善双臂操作，但真机适配需验证。

### 主要局限

已核验摘要未完整报告失败类型与真机泛化边界。

## 实验与结果

### 数据集与评测基准

CALVIN 与 OXE 小规模数据评测；具体任务和数据划分见论文。

## 局限与启发

### 主要局限

已核验摘要未完整报告失败类型与真机泛化边界。

## 与当前项目的关系

Medium：可帮助研究视觉预测是否改善双臂操作，但真机适配需验证。

## 相关论文

- [[Octo]]
- [[3D_Diffuser_Actor]]
- [[DROID]]
- [[Open_X-Embodiment]]
- [[ReconVLA]]
- [[VideoVLA]]
- [[Learning_by_Watching]]
- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/481c70828a4ff20d31a646cc6cc95f3d-Abstract-Conference.html)
