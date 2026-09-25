# VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation

## 基本信息

- 年份：2024
- 会议 / 期刊：CoRL
- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)
- 官方论文：[PMLR](https://proceedings.mlr.press/v270/liu25i.html)
- 主要分类：Bimanual Manipulation / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation


- 引用量：1
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/03_Bimanual/VoxAct-B.pdf]]
## 论文定位

这篇论文属于 Bimanual Manipulation / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论细粒度双臂操作需要在三维场景中同时定位两只手的关键区域。
核心思路是VoxAct-B 用 VLM 关注关键区域，再在体素空间中生成语言条件的双臂动作。
与当前项目的联系：High：可参考两只普通夹爪的空间目标表示。

## 核心关键词

Bimanual Manipulation、Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL、Bimanual

## 快速摘要

### 研究问题

细粒度双臂操作需要在三维场景中同时定位两只手的关键区域。

### 之前方法的问题

直接从全局图像预测高维双臂动作，可能忽略局部空间线索。

### 核心思路

VoxAct-B 用 VLM 关注关键区域，再在体素空间中生成语言条件的双臂动作。

### 数据集与评测基准

仿真细粒度双臂任务；真机覆盖需进一步核验。

### 主要结果

作者报告在仿真任务上优于所比较基线；摘要未给统一量化值。

### 为什么重要

把视觉目标定位与双臂三维动作表示连接起来。

### 与当前项目的关系

High：可参考两只普通夹爪的空间目标表示。

### 主要局限

体素分辨率与真机延迟、遮挡和接触误差需验证。

## 实验与结果

### 数据集与评测基准

仿真细粒度双臂任务；真机覆盖需进一步核验。

### 主要结果

作者报告在仿真任务上优于所比较基线；摘要未给统一量化值。

## 局限与启发

### 主要局限

体素分辨率与真机延迟、遮挡和接触误差需验证。

## 与当前项目的关系

High：可参考两只普通夹爪的空间目标表示。

## 相关论文

- [[AnyBimanual]]
- [[Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]]

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v270/liu25i.html)
