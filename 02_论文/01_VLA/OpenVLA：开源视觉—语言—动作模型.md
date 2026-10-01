# OpenVLA：开源视觉—语言—动作模型

## 基本信息

- 英文标题：OpenVLA: An Open-Source Vision-Language-Action Model
- 作者：—
- 年份：2024
- 发表 venue：CoRL
- 论文类型：会议论文
- 研究方向：VLA
- 论文链接：[PMLR](https://proceedings.mlr.press/v270/kim25c.html)
- DOI：—
- arXiv：—
- 项目主页：[项目主页](https://openvla.github.io/)
- 代码：[GitHub](https://github.com/openvla/openvla)
- 本地 PDF：[[00_论文池/PDFs/01_VLA/OpenVLA.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：4229
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：Not CCF A (robotics venue extension)

## 论文定位

这篇论文属于 VLA / Robot Foundation Models / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论现有 VLA 多为闭源，且针对新任务高效微调的方法仍不充分。
核心思路是OpenVLA 是开放的 7B VLA，在约 97 万条真实机器人轨迹上训练，支持通过微调适配新任务。
与当前项目的联系：High：有助于研究语言条件操作与 VLA 设计。

## 核心关键词

VLA、Robot Foundation Models、Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

现有 VLA 多为闭源，且针对新任务高效微调的方法仍不充分。

### 之前方法的问题

既有 VLA 多为闭源，新任务的高效微调方法也缺少系统评估。

### 核心思路

OpenVLA 是开放的 7B VLA，在约 97 万条真实机器人轨迹上训练，支持通过微调适配新任务。

### 输入

机器人相机图像和语言任务指令；具体预处理见论文方法及官方代码。

### 输出与动作

预测机器人控制动作；动作编码与本体适配以官方代码和论文方法为准。

### 数据集与评测基准

训练使用整理后的 Open X-Embodiment 混合数据，约 97 万条真机轨迹；DROID 在后期训练数据中被剔除，详见原卡。

### 为什么重要

提供可复用的 VLA 基线，同时明确了数据、算力和推理速度代价。

### 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

### 主要局限

作者指出训练数据偏单臂、第三人称视角且算力成本高；双臂/移动平台迁移仍需单独验证。

## 方法概览

任务输入 → OpenVLA 是开放的 7B VLA，在约 97 万条真实机器人轨迹上训练，支持通过微调适配新任务 → 预测机器人控制动作；动作编码与本体适配以官方代码和论文方法为准。

## 实验与结果

### 数据集与评测基准

训练使用整理后的 Open X-Embodiment 混合数据，约 97 万条真机轨迹；DROID 在后期训练数据中被剔除，详见原卡。

## 局限与启发

### 主要局限

作者指出训练数据偏单臂、第三人称视角且算力成本高；双臂/移动平台迁移仍需单独验证。

## 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

## 相关论文

- [[Octo：开源通用机器人策略]]
- [[DROID：大规模自然场景机器人操作数据集]]
- [[Open X-Embodiment：机器人学习数据集与 RT-X 模型]]
- [[将动作视为语言：在避免灾难性遗忘的条件下将 VLM 微调为 VLA]]
- [[BridgeVLA：通过输入—输出对齐高效学习三维操作]]
- [[CoT-VLA：面向 VLA 的视觉思维链推理]]
- [[DiffusionVLA：通过统一扩散与自回归扩展机器人基础模型]]
- [[ReconVLA：以重建增强机器人感知的 VLA 模型]]
- [[RoboGround：利用有视觉定位能力的视觉—语言先验实现机器人操作]]
- [[RoboMamba：用于机器人推理与操作的高效 VLA 模型]]
- [[RoboMonkey：扩展 VLA 的测试时采样与验证]]
- [[SP-VLA：通过联合模型调度与 Token 剪枝加速 VLA]]

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v270/kim25c.html)
- 项目主页：[项目主页](https://openvla.github.io/)
- 官方代码：[GitHub](https://github.com/openvla/openvla)
