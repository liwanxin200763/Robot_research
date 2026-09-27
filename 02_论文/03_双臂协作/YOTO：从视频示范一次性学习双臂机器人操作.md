# YOTO：从视频示范一次性学习双臂机器人操作

## 基本信息

- 英文标题：You Only Teach Once: Learn One-Shot Bimanual Robotic Manipulation from Video Demonstrations
- 作者：Huayi Zhou; Ruixiang Wang; Yunxin Tai; Yueci Deng; Guiliang Liu; Kui Jia
- 年份：2025
- 发表 venue：RSS
- 论文类型：会议论文
- 研究方向：双臂协作
- 论文链接：[Robotics Proceedings](https://www.roboticsproceedings.org/rss21/p149.html)
- DOI：—
- arXiv：—
- 项目主页：[项目主页](https://hnuzhy.github.io/projects/YOTO)
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/03_双臂协作/YOTO.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：7
- 引用量来源：OpenAlex
- 引用量来源链接：https://openalex.org/W4414050937
- 引用量查询日期：2026-09-27
- 引用量状态：已核验
- 引用量查询状态：verified
- OpenAlex Work ID：W4414050937
- 排序引用量：7
- 排序引用量来源：OpenAlex

### 出版与分类补充

- 关键词：Bimanual; Human Video; Imitation Learning; Diffusion Policy; Generalization; Long-horizon

## 论文定位

这篇论文属于 Bimanual 方向，主要讨论低成本示范条件下，如何学会协调的双臂技能。
核心思路是把单段人类视频转换为结构化关键帧轨迹，并扩展成机器人示范。
与当前项目的联系：High：与双臂普通夹爪和低示范预算直接相关。

## 核心关键词

Bimanual、Human Video、Imitation Learning、Diffusion Policy、Generalization、Long-horizon、Video demonstration、bimanual diffusion policy

## 快速摘要

### 研究问题

低成本示范条件下，如何学会协调的双臂技能。

### 之前方法的问题

一段人类视频不能直接提供机器人两臂的连续可执行动作。

### 核心思路

把单段人类视频转换为结构化关键帧轨迹，并扩展成机器人示范。

### 数据集与评测基准

论文评估五项复杂的长时序双臂任务。

### 主要结果

作者报告可模仿五项双臂任务，并对视觉和空间变化有一定泛化；具体数值需看原文。

### 为什么重要

可帮助研究 Human Video → Robot Action 的数据成本。

### 与当前项目的关系

High：与双臂普通夹爪和低示范预算直接相关。

### 主要局限

人类视频关键帧到真机连续控制仍需验证可达性与接触安全。

## 实验与结果

### 数据集与评测基准

论文评估五项复杂的长时序双臂任务。

### 主要结果

作者报告可模仿五项双臂任务，并对视觉和空间变化有一定泛化；具体数值需看原文。

## 局限与启发

### 主要局限

人类视频关键帧到真机连续控制仍需验证可达性与接触安全。

## 与当前项目的关系

High：与双臂普通夹爪和低示范预算直接相关。

## 相关论文

- [[迈向统一理解机器人操作：综合综述]]
- [[以夹爪位姿与物体点流作为机器人双臂操作接口]]

## 来源

- 官方论文：[Robotics Proceedings](https://www.roboticsproceedings.org/rss21/p149.html)
- 项目主页：[项目主页](https://hnuzhy.github.io/projects/YOTO)
