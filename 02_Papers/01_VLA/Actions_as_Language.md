# Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting

## 基本信息

- 年份：2026
- 会议 / 期刊：ICLR
- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 官方论文：https://proceedings.iclr.cc/paper_files/paper/2026/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html
- 项目主页：https://vlm2vla.github.io/
- 主要分类：VLA / Robot Foundation Models / Robot Manipulation

## 论文定位

这篇论文属于 VLA / Robot Foundation Models / Robot Manipulation 方向，主要讨论直接用机器人动作微调 VLM，可能损伤原有语言与多模态推理能力。
核心思路是VLM2VLA 先把底层动作写成自然语言形式，使机器人动作数据与 VLM 的原有输出形式更一致。
与当前项目的联系：High：有助于研究语言条件操作与 VLA 设计。

## 核心关键词

VLA、Robot Foundation Models、Robot Manipulation

## 快速摘要

### 研究问题

直接用机器人动作微调 VLM，可能损伤原有语言与多模态推理能力。

### 之前方法的问题

直接把底层动作当作特殊 token 微调，可能与 VLM 的语言预训练形式不一致。

### 核心思路

VLM2VLA 先把底层动作写成自然语言形式，使机器人动作数据与 VLM 的原有输出形式更一致。

### 数据集与评测基准

BridgeData V2 遥操作轨迹被重新标成分层语言；标注成本和抽查方法见 Appendix 6.1。

### 主要结果

在 “Item Above Ash Ketchum” 任务上，VLM2VLA 成功率为 60%，动作 token 消融为 30%；动作生成周期中位延迟为 6.1 s（Sec. 4.2.2、5.1）。

### 为什么重要

提出一种尽量保留 VLM 推理能力的 VLA 微调接口；延迟也提示真机部署成本。

### 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

### 主要局限

作者报告动作生成中位延迟 6.1 s，实验控制维度和本体范围有限；复杂旋转及跨本体迁移仍需验证。

## 实验与结果

### 数据集与评测基准

BridgeData V2 遥操作轨迹被重新标成分层语言；标注成本和抽查方法见 Appendix 6.1。

### 主要结果

在 “Item Above Ash Ketchum” 任务上，VLM2VLA 成功率为 60%，动作 token 消融为 30%；动作生成周期中位延迟为 6.1 s（Sec. 4.2.2、5.1）。

## 局限与启发

### 主要局限

作者报告动作生成中位延迟 6.1 s，实验控制维度和本体范围有限；复杂旋转及跨本体迁移仍需验证。

## 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

## 相关论文

- [[3D-VLA]]
- [[CoT-VLA]]
- [[Octo]]
- [[OpenVLA]]
- [[SayCan]]
- [[HAMSTER]]
- [[DROID]]
- [[Open_X-Embodiment]]
- [[A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]]

## 来源

- 官方论文：https://proceedings.iclr.cc/paper_files/paper/2026/hash/7a0f8055c838df8e62329a76c7c6403d-Abstract-Conference.html
- 项目主页：https://vlm2vla.github.io/
