# Octo：开源通用机器人策略

## 基本信息

- 英文标题：Octo: An Open-Source Generalist Robot Policy
- 作者：—
- 年份：2024
- 发表 venue：RSS
- 论文类型：会议论文
- 研究方向：VLA
- 论文链接：[Robotics Proceedings](https://roboticsproceedings.org/rss20/p090.html)
- DOI：—
- arXiv：—
- 项目主页：[项目主页](https://octo-models.github.io/)
- 代码：[GitHub](https://github.com/octo-models/octo)
- 本地 PDF：[[00_论文池/PDFs/01_VLA/Octo.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：103
- 引用量来源：OpenAlex
- 引用量来源链接：https://openalex.org/W4402353985
- 引用量查询日期：2026-09-27
- 引用量状态：已核验
- 排序引用量：103
- 排序引用量来源：OpenAlex

### 出版与分类补充

- CCF 等级：Not CCF A (robotics venue extension)

## 论文定位

这篇论文属于 VLA / Robot Foundation Models / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论通用机器人策略需要同时适配不同相机、动作空间和机器人平台。
核心思路是Octo 在 Open X-Embodiment 约 80 万条轨迹上训练 Transformer 策略，并提供可微调的通用初始化。
与当前项目的联系：High：有助于研究语言条件操作与 VLA 设计。

## 核心关键词

VLA、Robot Foundation Models、Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

通用机器人策略需要同时适配不同相机、动作空间和机器人平台。

### 之前方法的问题

各机器人平台的相机、动作空间与任务不同，单一策略难以直接跨平台使用。

### 核心思路

Octo 在 Open X-Embodiment 约 80 万条轨迹上训练 Transformer 策略，并提供可微调的通用初始化。

### 数据集与评测基准

从 Open X-Embodiment 整理约 80 万条训练轨迹，在 9 种机器人平台和多项下游任务上评估。

### 主要结果

论文在 9 种机器人平台上评测，表明 Octo 可迁移到新的观测和动作空间；具体成功率见原卡实验表。

### 为什么重要

是研究共享机器人数据与跨本体微调的重要开放基线。

### 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

### 主要局限

训练数据的腕部相机和语言覆盖不均；评测主要在论文列出的单臂/双臂平台。

## 实验与结果

### 数据集与评测基准

从 Open X-Embodiment 整理约 80 万条训练轨迹，在 9 种机器人平台和多项下游任务上评估。

### 主要结果

论文在 9 种机器人平台上评测，表明 Octo 可迁移到新的观测和动作空间；具体成功率见原卡实验表。

## 局限与启发

### 主要局限

训练数据的腕部相机和语言覆盖不均；评测主要在论文列出的单臂/双臂平台。

## 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

## 相关论文

- [[SayCan：以机器人能力约束语言指令的落地执行]]
- [[Open X-Embodiment：机器人学习数据集与 RT-X 模型]]
- [[将动作视为语言：在避免灾难性遗忘的条件下将 VLM 微调为 VLA]]
- [[CoT-VLA：面向 VLA 的视觉思维链推理]]
- [[DiffusionVLA：通过统一扩散与自回归扩展机器人基础模型]]
- [[OpenVLA：开源视觉—语言—动作模型]]
- [[ReconVLA：以重建增强机器人感知的 VLA 模型]]
- [[RoboMonkey：扩展 VLA 的测试时采样与验证]]
- [[SP-VLA：通过联合模型调度与 Token 剪枝加速 VLA]]
- [[SimpleVLA-RL：通过强化学习扩展 VLA 训练]]
- [[SpatialVLA：探索 VLA 模型的空间表征]]
- [[TraceVLA：以视觉轨迹提示增强通用机器人策略的时空感知]]

## 来源

- 官方论文：[Robotics Proceedings](https://roboticsproceedings.org/rss20/p090.html)
- 项目主页：[项目主页](https://octo-models.github.io/)
- 官方代码：[GitHub](https://github.com/octo-models/octo)
