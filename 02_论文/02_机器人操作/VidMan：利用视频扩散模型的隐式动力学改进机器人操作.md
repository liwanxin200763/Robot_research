# VidMan：利用视频扩散模型的隐式动力学改进机器人操作

## 基本信息

- 英文标题：VidMan: Exploiting Implicit Dynamics from Video Diffusion Model for Effective Robot Manipulation
- 作者：Wen, Youpeng; Lin, Junfan; Zhu, Yi; Han, Jianhua; Xu, Hang; Zhao, Shen; Liang, Xiaodan
- 年份：2024
- 发表 venue：NeurIPS
- 论文类型：会议论文
- 研究方向：机器人操作
- 论文链接：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/481c70828a4ff20d31a646cc6cc95f3d-Abstract-Conference.html)
- DOI：10.52202/079017-1298 — [DOI](https://doi.org/10.52202/079017-1298)
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/02_机器人操作/VidMan.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：74
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：A
- 关键词：World Model / Video Diffusion

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

- [[Octo：开源通用机器人策略]]
- [[3D Diffuser Actor：基于三维场景表征的策略扩散]]
- [[DROID：大规模自然场景机器人操作数据集]]
- [[Open X-Embodiment：机器人学习数据集与 RT-X 模型]]
- [[ReconVLA：以重建增强机器人感知的 VLA 模型]]
- [[VideoVLA：让视频生成模型成为可泛化的机器人操作策略]]
- [[观察学习：基于视频的机器人操作学习方法综述]]
- [[迈向统一理解机器人操作：综合综述]]

## 来源

- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/481c70828a4ff20d31a646cc6cc95f3d-Abstract-Conference.html)
