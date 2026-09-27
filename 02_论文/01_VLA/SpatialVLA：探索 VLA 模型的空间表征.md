# SpatialVLA：探索 VLA 模型的空间表征

## 基本信息

- 英文标题：SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models
- 作者：—
- 年份：2025
- 发表 venue：RSS
- 论文类型：会议论文
- 研究方向：VLA
- 论文链接：[Robotics Proceedings](https://www.roboticsproceedings.org/rss21/p011.html)
- DOI：—
- arXiv：—
- 项目主页：[项目主页](https://spatialvla.github.io/)
- 代码：[GitHub](https://github.com/SpatialVLA/SpatialVLA)
- 本地 PDF：[[00_论文池/PDFs/01_VLA/SpatialVLA.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：41
- 引用量来源：OpenAlex
- 引用量来源链接：https://openalex.org/W4414051092
- 引用量查询日期：2026-09-27
- 引用量状态：已核验
- 排序引用量：41
- 排序引用量来源：OpenAlex

### 出版与分类补充

- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)

## 论文定位

这篇论文属于 VLA / Robot Foundation Models / Robot Manipulation 方向，主要讨论机器人操作需要把视觉与语言理解落实到三维空间关系。
核心思路是SpatialVLA 加入 Ego3D Position Encoding，使空间信息参与 VLA 输入和动作预测。
与当前项目的联系：High：双臂普通夹爪需要准确的目标与相对位姿。

## 核心关键词

VLA、Robot Foundation Models、Robot Manipulation

## 快速摘要

### 研究问题

机器人操作需要把视觉与语言理解落实到三维空间关系。

### 之前方法的问题

普通 VLA 的视觉 token 可能缺少显式三维位置线索。

### 核心思路

SpatialVLA 加入 Ego3D Position Encoding，使空间信息参与 VLA 输入和动作预测。

### 主要结果

作者报告较好的分布内泛化和分布外适配；具体比较数字见论文。

### 为什么重要

为 VLA 的三维 Grounding 提供明确的表示方案。

### 与当前项目的关系

High：双臂普通夹爪需要准确的目标与相对位姿。

### 主要局限

需要检验相机标定变化与遮挡下的稳健性。

## 实验与结果

### 主要结果

作者报告较好的分布内泛化和分布外适配；具体比较数字见论文。

## 局限与启发

### 主要局限

需要检验相机标定变化与遮挡下的稳健性。

## 与当前项目的关系

High：双臂普通夹爪需要准确的目标与相对位姿。

## 相关论文

- [[3D-VLA：基于三维视觉—语言—动作的生成式世界模型]]
- [[Octo：开源通用机器人策略]]
- [[OpenVLA：开源视觉—语言—动作模型]]
- [[TraceVLA：以视觉轨迹提示增强通用机器人策略的时空感知]]
- [[RDT-1B：面向双臂操作的扩散基础模型]]
- [[BAKU：面向多任务策略学习的高效 Transformer]]
- [[DROID：大规模自然场景机器人操作数据集]]
- [[Open X-Embodiment：机器人学习数据集与 RT-X 模型]]

## 来源

- 官方论文：[Robotics Proceedings](https://www.roboticsproceedings.org/rss21/p011.html)
- 项目主页：[项目主页](https://spatialvla.github.io/)
- 官方代码：[GitHub](https://github.com/SpatialVLA/SpatialVLA)
