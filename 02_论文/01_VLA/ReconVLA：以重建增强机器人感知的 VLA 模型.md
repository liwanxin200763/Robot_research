# ReconVLA：以重建增强机器人感知的 VLA 模型

## 基本信息

- 英文标题：ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver
- 作者：Wenxuan Song; Ziyang Zhou; Han Zhao; Jiayi Chen; Pengxiang Ding; Haodong Yan; Yuxin Huang; Feilong Tang; Donglin Wang; Haoang Li
- 年份：2026
- 发表 venue：AAAI
- 论文类型：会议论文
- 研究方向：VLA
- 论文链接：[AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/38921)
- DOI：10.1609/aaai.v40i22.38921 — [DOI](https://doi.org/10.1609/aaai.v40i22.38921)
- arXiv：—
- 项目主页：[项目主页](https://zionchow.github.io/ReconVLA/)
- 代码：[GitHub](https://github.com/OpenHelix-Team/ReconVLA)
- 本地 PDF：[[00_论文池/PDFs/01_VLA/ReconVLA.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：3
- 引用量来源：OpenAlex
- 引用量来源链接：https://openalex.org/W7137985120
- 引用量查询日期：2026-09-27
- 引用量状态：已核验
- 引用量查询状态：verified
- OpenAlex Work ID：W7137985120
- 排序引用量：3
- 排序引用量来源：OpenAlex

### 出版与分类补充

- CCF 等级：A
- 关键词：VLA; Robot Manipulation; Visual Grounding; Robot Perception; Implicit Grounding; Gaze-Region Reconstruction; Generalization; Diffusion Transformer
- 特别关注：是

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

- [[3D-VLA：基于三维视觉—语言—动作的生成式世界模型]]
- [[Octo：开源通用机器人策略]]
- [[OpenVLA：开源视觉—语言—动作模型]]
- [[RoboGround：利用有视觉定位能力的视觉—语言先验实现机器人操作]]
- [[VidMan：利用视频扩散模型的隐式动力学改进机器人操作]]
- [[通过生成式预期实现机器人操作的闭环视觉运动控制]]
- [[Open X-Embodiment：机器人学习数据集与 RT-X 模型]]
- [[迈向统一理解机器人操作：综合综述]]

## 来源

- 官方论文：[AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/38921)
- 项目主页：[项目主页](https://zionchow.github.io/ReconVLA/)
- 官方代码：[GitHub](https://github.com/OpenHelix-Team/ReconVLA)
