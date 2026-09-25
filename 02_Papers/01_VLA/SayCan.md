# SayCan: Do As I Can, Not As I Say

## 基本信息

- 正式标题：Do As I Can, Not As I Say: Grounding Language in Robotic Affordances
- 作者：Michael Ahn; Anthony Brohan; Noah Brown; Yevgen Chebotar; Omar Cortes; Byron David; Chelsea Finn; Chuyuan Fu; Keerthana Gopalakrishnan; Karol Hausman; Alex Herzog; Daniel Ho; Jasmine Hsu; Julian Ibarz; Brian Ichter; Alex Irpan; Eric Jang; Rosario Jauregui Ruano; Kyle Jeffrey; Sally Jesmonth; Nikhil J Joshi; Ryan Julian; Dmitry Kalashnikov; Yuheng Kuang; Kuang-Huei Lee; Sergey Levine; Yao Lu; Linda Luu; Carolina Parada; Peter Pastor; Jornell Quiambao; Kanishka Rao; Jarek Rettinghouse; Diego Reyes; Pierre Sermanet; Nicolas Sievers; Clayton Tan; Alexander Toshev; Vincent Vanhoucke; Fei Xia; Ted Xiao; Peng Xu; Sichun Xu; Mengyuan Yan; Andy Zeng
- 年份：2022
- 会议 / 期刊：Conference on Robot Learning (CoRL 2022), Proceedings of Machine Learning Research 205, pp. 287–318
- CCF 等级：Not CCF A (CoRL is a robotics venue; no CCF-A assignment recorded)
- DOI：10.48550/arXiv.2204.01691 — [DOI](https://doi.org/10.48550/arXiv.2204.01691)
- 官方论文：[官方论文](https://research.google/pubs/do-as-i-can-not-as-i-say-grounding-language-in-robotic-affordances/)
- 项目主页：[项目主页](https://say-can.github.io/)
- 官方代码：[GitHub](https://github.com/google-research/google-research/tree/master/saycan)
- 主要分类：VLA
- 关键词：VLA; Robot Manipulation; Language Grounding; Affordance; Long-horizon; Planning; RL; IL; Sim2Real
- 特别关注：是


- 引用量：523
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/01_VLA/SayCan.pdf]]
## 论文定位

这篇论文属于 VLA 方向，主要讨论LLM 能拆解长指令，但不知道当前机器人真正能做什么。
核心思路是SayCan 结合语言模型的技能匹配分数与技能价值/可供性估计，逐步选择当前可执行的操作。
与当前项目的联系：High：双臂普通夹爪需要在动作前判断技能是否可行。

## 核心关键词

VLA、Robot Manipulation、Language Grounding、Affordance、Long-horizon、Planning、RL、IL

## 快速摘要

### 研究问题

LLM 能拆解长指令，但不知道当前机器人真正能做什么。

### 之前方法的问题

只按语言相关性选技能，可能生成物理上不可执行的计划。

### 核心思路

SayCan 结合语言模型的技能匹配分数与技能价值/可供性估计，逐步选择当前可执行的操作。

### 数据集与评测基准

Mock Kitchen 与真实办公室厨房任务。

### 为什么重要

把语言规划和机器人可执行性明确连接起来。

### 与当前项目的关系

High：双臂普通夹爪需要在动作前判断技能是否可行。

### 主要局限

技能库、价值估计和环境假设依赖特定机器人；规划成功不保证动作完成。

## 实验与结果

### 数据集与评测基准

Mock Kitchen 与真实办公室厨房任务。

## 局限与启发

### 主要局限

技能库、价值估计和环境假设依赖特定机器人；规划成功不保证动作完成。

## 与当前项目的关系

High：双臂普通夹爪需要在动作前判断技能是否可行。

## 相关论文

- [[Actions_as_Language]]
- [[Octo]]
- [[RoboMamba]]
- [[A_Survey_on_Robotics_with_Foundation_Models_Toward_Embodied_AI]]
- [[A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective]]
- [[A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]]
- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]
- [[OpenVLA]]
- [[HAMSTER]]

## 来源

- 官方论文：[官方论文](https://research.google/pubs/do-as-i-can-not-as-i-say-grounding-language-in-robotic-affordances/)
- 项目主页：[项目主页](https://say-can.github.io/)
- 官方代码：[GitHub](https://github.com/google-research/google-research/tree/master/saycan)
