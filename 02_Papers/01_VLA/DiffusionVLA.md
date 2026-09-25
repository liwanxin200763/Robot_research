# DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression

## 基本信息

- 作者：Junjie Wen; Yichen Zhu; Minjie Zhu; Zhibin Tang; Jinming Li; Zhongyi Zhou; Xiaoyu Liu; Chaomin Shen; Yaxin Peng; Feifei Feng
- 年份：2025
- 会议 / 期刊：ICML
- CCF 等级：A
- 官方论文：[PMLR](https://proceedings.mlr.press/v267/wen25g.html)
- 项目主页：[项目主页](https://diffusion-vla.github.io/)
- 官方代码：[GitHub](https://github.com/juruobenruo/DexVLA)
- 主要分类：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 关键词：VLA; Autoregressive Reasoning / Diffusion


- 引用量：—
- 引用量来源：未可靠匹配
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/01_VLA/DiffusionVLA.pdf]]
## 论文定位

这篇论文属于 A (CCF 7th edition; venue category not independently extracted from official PDF) 方向，主要讨论自回归 VLA 的动作精度与鲁棒性可能不足，而独立的扩散策略又缺少语言推理。
核心思路是DiffusionVLA 将自回归推理与扩散式动作生成结合，尝试兼顾语义理解和连续控制。
与当前项目的联系：High：有助于研究语言条件操作与 VLA 设计。

## 核心关键词

VLA、Autoregressive Reasoning、Diffusion、venue category not independently extracted from official PDF)、Robot Foundation Models

## 快速摘要

### 研究问题

自回归 VLA 的动作精度与鲁棒性可能不足，而独立的扩散策略又缺少语言推理。

### 之前方法的问题

纯自回归动作预测的精度可能不足；只做扩散控制又较难利用语言推理。

### 核心思路

DiffusionVLA 将自回归推理与扩散式动作生成结合，尝试兼顾语义理解和连续控制。

### 数据集与评测基准

作者提供 DexVLA 示例数据，但该样例不等于论文全部训练和评测数据。

### 为什么重要

为双臂 VLA 动作头选择提供“推理 + 生成式控制”的比较对象。

### 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

### 主要局限

实验覆盖的任务与本体有限；逐任务失败次数未从已访问页面完整提取。

## 实验与结果

### 数据集与评测基准

作者提供 DexVLA 示例数据，但该样例不等于论文全部训练和评测数据。

## 局限与启发

### 主要局限

实验覆盖的任务与本体有限；逐任务失败次数未从已访问页面完整提取。

## 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

## 相关论文

- [[Octo]]
- [[OpenVLA]]
- [[ALOHA_Unleashed]]
- [[RDT-1B]]
- [[3D_Diffuser_Actor]]
- [[Equivariant_Diffusion_Policy]]
- [[DROID]]
- [[Open_X-Embodiment]]

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v267/wen25g.html)
- 项目主页：[项目主页](https://diffusion-vla.github.io/)
- 官方代码：[GitHub](https://github.com/juruobenruo/DexVLA)
