# CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models

## 基本信息

- 作者：Zhao, Qingqing; Lu, Yao; Kim, Moo Jin; Fu, Zipeng; Zhang, Zhuoyang; Wu, Yecheng; Li, Zhaoshuo; Ma, Qianli; Han, Song; Finn, Chelsea; Handa, Ankur; Lin, Tsung-Yi; Wetzstein, Gordon; Liu, Ming-Yu; Xiang, Donglai
- 年份：2025
- 会议 / 期刊：CVPR
- CCF 等级：A
- 官方论文：[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html)
- 项目主页：[项目主页](https://cot-vla.github.io/)
- 主要分类：VLA; Robot Foundation Model
- 关键词：Visual Chain-of-Thought


- 引用量：58
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/01_VLA/CoT-VLA.pdf]]
## 论文定位

这篇论文属于 VLA; Robot Foundation Model 方向，主要讨论直接从视觉和语言映射动作的 VLA 缺少显式中间推理，复杂操作时容易失去目标感。
核心思路是CoT-VLA 先自回归预测未来图像作为视觉子目标，再生成短动作序列，使中间视觉推理参与控制。
与当前项目的联系：High：有助于研究语言条件操作与 VLA 设计。

## 核心关键词

Visual Chain-of-Thought、VLA、Robot Foundation Model

## 快速摘要

### 研究问题

直接从视觉和语言映射动作的 VLA 缺少显式中间推理，复杂操作时容易失去目标感。

### 之前方法的问题

直接输入到动作的映射没有显式中间目标，复杂操作缺少可检查的推理步骤。

### 核心思路

CoT-VLA 先自回归预测未来图像作为视觉子目标，再生成短动作序列，使中间视觉推理参与控制。

### 数据集与评测基准

使用 Open X-Embodiment 示范及 EPIC-KITCHENS、Something-Something V2 视频；下游任务包括 BridgeData V2、Franka-Tabletop。

### 为什么重要

可检验“先预测视觉目标再行动”是否改善长任务和双臂目标协调。

### 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

### 主要局限

依赖 7B VILA-U 和任务适配；推理/控制效率与更广的机器人本体仍需核验。

## 实验与结果

### 数据集与评测基准

使用 Open X-Embodiment 示范及 EPIC-KITCHENS、Something-Something V2 视频；下游任务包括 BridgeData V2、Franka-Tabletop。

## 局限与启发

### 主要局限

依赖 7B VILA-U 和任务适配；推理/控制效率与更广的机器人本体仍需核验。

## 与当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

## 相关论文

- [[3D-VLA]]
- [[Octo]]
- [[OpenVLA]]
- [[Dreamitate]]
- [[Open_X-Embodiment]]
- [[Actions_as_Language]]
- [[RoboMonkey]]
- [[A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective]]
- [[A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]]
- [[Learning_by_Watching]]
- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html)
- 项目主页：[项目主页](https://cot-vla.github.io/)
