# AnyBimanual：迁移单臂策略以实现通用双臂操作

## 基本信息

- 英文标题：AnyBimanual: Transferring Unimanual Policy for General Bimanual Manipulation
- 中文标题：AnyBimanual：迁移单臂策略以实现通用双臂操作

- 作者：Lu, Guanxing; Yu, Tengbo; Deng, Haoyuan; Chen, Season Si; Tang, Yansong; Wang, Ziwei
- 年份：2025
- 会议 / 期刊：ICCV
- CCF 等级：A
- 官方论文：[CVF Open Access](https://openaccess.thecvf.com/content/ICCV2025/html/Lu_AnyBimanual_Transferring_Unimanual_Policy_for_General_Bimanual_Manipulation_ICCV_2025_paper.html)
- 主要分类：Bimanual Manipulation; Imitation Learning


- 引用量：2
- 引用量来源：OpenAlex
- 引用量来源链接：https://openalex.org/W4405254485
- 引用量查询日期：2026-09-27
- 排序引用量：2
- 排序引用量来源：OpenAlex
- 本地 PDF：[[00_论文池/PDFs/03_双臂协作/AnyBimanual.pdf|查看 PDF]]
## 论文定位

这篇论文属于 Bimanual Manipulation; Imitation Learning 方向，主要讨论语言条件双臂操作的示范成本高，动作空间也更复杂。
核心思路是用技能管理器安排双臂子技能，并以体素/视觉对齐模块协调两臂输入，使预训练单臂策略可复用。
与当前项目的联系：High：直接针对从单臂到普通夹爪双臂任务的迁移。

## 核心关键词

Bimanual Manipulation、Imitation Learning、Policy Transfer、Generalization

## 快速摘要

### 研究问题

语言条件双臂操作的示范成本高，动作空间也更复杂。

### 之前方法的问题

从单臂策略直接迁移到双臂时，两臂观测和动作不一定对齐。

### 核心思路

用技能管理器安排双臂子技能，并以体素/视觉对齐模块协调两臂输入，使预训练单臂策略可复用。

### 数据集与评测基准

12 项仿真任务和 9 项真机任务。

### 为什么重要

提供节约双臂数据成本的一条可测试路线。

### 与当前项目的关系

High：直接针对从单臂到普通夹爪双臂任务的迁移。

### 主要局限

仍依赖少量双臂示范，且假设单臂预训练表示可以复用。

## 实验与结果

### 数据集与评测基准

12 项仿真任务和 9 项真机任务。

## 局限与启发

### 主要局限

仍依赖少量双臂示范，且假设单臂预训练表示可以复用。

## 与当前项目的关系

High：直接针对从单臂到普通夹爪双臂任务的迁移。

## 相关论文

- [[Octo：开源通用机器人策略]]
- [[OpenVLA：开源视觉—语言—动作模型]]
- [[RDT-1B：面向双臂操作的扩散基础模型]]
- [[VoxAct-B：用于双臂操作的体素式动作与稳定策略]]
- [[3D Diffuser Actor：基于三维场景表征的策略扩散]]
- [[DexCap：面向灵巧操作的可扩展便携式动作捕捉数据采集系统]]
- [[DROID：大规模自然场景机器人操作数据集]]
- [[Open X-Embodiment：机器人学习数据集与 RT-X 模型]]
- [[迈向统一理解机器人操作：综合综述]]

## 来源

- 官方论文：[CVF Open Access](https://openaccess.thecvf.com/content/ICCV2025/html/Lu_AnyBimanual_Transferring_Unimanual_Policy_for_General_Bimanual_Manipulation_ICCV_2025_paper.html)
