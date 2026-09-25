# ReconVLA

## 基本信息

- 正式标题：ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver
- 作者：Wenxuan Song; Ziyang Zhou; Han Zhao; Jiayi Chen; Pengxiang Ding; Haodong Yan; Yuxin Huang; Feilong Tang; Donglin Wang; Haoang Li
- 年份：2026
- 会议 / 期刊：AAAI
- CCF 等级：A
- DOI：10.1609/aaai.v40i22.38921 — [DOI](https://doi.org/10.1609/aaai.v40i22.38921)
- 官方论文：[AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/38921)
- 项目主页：[项目主页](https://zionchow.github.io/ReconVLA/)
- 官方代码：[GitHub](https://github.com/OpenHelix-Team/ReconVLA)
- 主要分类：VLA
- 关键词：VLA; Robot Manipulation; Visual Grounding; Robot Perception; Implicit Grounding; Gaze-Region Reconstruction; Generalization; Diffusion Transformer
- 特别关注：是


- 引用量：3
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/01_VLA/ReconVLA.pdf]]
## 论文定位

这篇论文属于 VLA 方向，主要讨论VLA 的视觉注意可能落在任务无关区域，削弱精细操作与泛化。
核心思路是ReconVLA 用扩散式重建目标注视区域，促使视觉表示聚焦被操作物体，同时保留动作预测。
与当前项目的联系：High：有助于研究语言条件操作与 VLA 设计。

## 核心关键词

VLA、Robot Manipulation、Visual Grounding、Robot Perception、Implicit Grounding、Gaze-Region Reconstruction、Generalization、Diffusion Transformer

## 快速摘要

### 研究问题

VLA 的视觉注意可能落在任务无关区域，削弱精细操作与泛化。

### 之前方法的问题

原有 VLA 难以稳定把视觉注意对准目标区域；显式标注 Grounding 的方案又可能增加数据要求。

### 核心思路

ReconVLA 用扩散式重建目标注视区域，促使视觉表示聚焦被操作物体，同时保留动作预测。

### 输入

RGB 图像历史和语言指令；重建注视区域作为中间视觉目标（Sec. 3、Fig. 2）。

### 为什么重要

直接对应本项目的目标 Grounding 与动作前目标核验。

### 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

### 主要局限

作者指出性能取决于目标区域重建是否正确；公开评测主要集中在 CALVIN 与有限真机任务。跨本体和新相机条件仍需验证。

## 局限与启发

### 主要局限

作者指出性能取决于目标区域重建是否正确；公开评测主要集中在 CALVIN 与有限真机任务。跨本体和新相机条件仍需验证。

## 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

## 相关论文

- [[3D-VLA]]
- [[Octo]]
- [[OpenVLA]]
- [[RoboGround]]
- [[VidMan]]
- [[Closed-Loop_Visuomotor_Control_with_Generative_Expectation_for_Robotic_Manipulation]]
- [[Open_X-Embodiment]]
- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：[AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/38921)
- 项目主页：[项目主页](https://zionchow.github.io/ReconVLA/)
- 官方代码：[GitHub](https://github.com/OpenHelix-Team/ReconVLA)
