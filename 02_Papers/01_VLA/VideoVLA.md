# VideoVLA: Video Generators Can Be Generalizable Robot Manipulators

## 基本信息

- 作者：Shen, Yichao; Wei, Fangyun; Du, Zhiying; Liang, Yaobo; Lu, Yan; Yang, Jiaolong; Zheng, Nanning; Guo, Baining
- 年份：2025
- 会议 / 期刊：NeurIPS
- CCF 等级：A
- DOI：10.52202/085713-3197 — [DOI](https://doi.org/10.52202/085713-3197)
- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/89a3b655a8b68ae1c76b768152c9c19d-Abstract-Conference.html)
- 项目主页：[项目主页](https://videovla-nips2025.github.io/)
- 官方代码：[GitHub](https://github.com/VideoVLA-Project/VideoVLA)
- 主要分类：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 关键词：VLA; Video-Action Model / Generalization


- 引用量：3
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/01_VLA/VideoVLA.pdf]]
## 论文定位

这篇论文属于 A (CCF 7th edition; venue category not independently extracted from official PDF) 方向，主要讨论开放环境操作需要预见动作后果并适应新场景。
核心思路是VideoVLA 将视频生成模型用于 VLA，利用想象的未来画面帮助动作选择。
与当前项目的联系：High：可用于双臂动作前预期与动作后验证。

## 核心关键词

VLA、Video-Action Model、Generalization、venue category not independently extracted from official PDF)、Robot Foundation Models

## 快速摘要

### 研究问题

开放环境操作需要预见动作后果并适应新场景。

### 之前方法的问题

只从当前视觉预测动作，可能缺少对未来状态的理解。

### 核心思路

VideoVLA 将视频生成模型用于 VLA，利用想象的未来画面帮助动作选择。

### 主要结果

作者报告想象未来质量与动作可靠性、任务成功相关；具体数字见实验章节。

### 为什么重要

把世界模型式视觉预期与机器人动作生成连接起来。

### 与当前项目的关系

High：可用于双臂动作前预期与动作后验证。

### 主要局限

视频看起来合理不一定代表接触力与夹爪动作正确。

## 实验与结果

### 主要结果

作者报告想象未来质量与动作可靠性、任务成功相关；具体数字见实验章节。

## 局限与启发

### 主要局限

视频看起来合理不一定代表接触力与夹爪动作正确。

## 与当前项目的关系

High：可用于双臂动作前预期与动作后验证。

## 相关论文

- [[Octo]]
- [[OpenVLA]]
- [[VidMan]]
- [[RDT-1B]]
- [[TASTE-Rob]]
- [[Open_X-Embodiment]]
- [[A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]]

## 来源

- 官方论文：[NeurIPS Proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/89a3b655a8b68ae1c76b768152c9c19d-Abstract-Conference.html)
- 项目主页：[项目主页](https://videovla-nips2025.github.io/)
- 官方代码：[GitHub](https://github.com/VideoVLA-Project/VideoVLA)
