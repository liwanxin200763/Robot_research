# MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation

## 基本信息

- 作者：Zhenyu Wu、Yuheng Zhou、Xiuwei Xu、Ziwei Wang、Haibin Yan
- 年份：2025
- 会议 / 期刊：CVPR 2025，页码 1714–1723
- CCF 等级：A
- DOI：未在本次检查的 CVF 官方论文页核实到会议 DOI；arXiv DOI：10.48550/arXiv.2503.13446
- 主要分类：VLA
- 关键词：`VLA`、`Mobile Manipulation`、`Whole-body Planning`、`Waypoint`、`Collision Avoidance`、`Generalization`
- 特别关注：是

## 论文定位

这篇论文属于 VLA 方向，主要讨论固定底座 VLA 不会生成移动底盘与机械臂协同运动轨迹。
核心思路是用预训练 VLA 生成末端 waypoint，再以 reachability、smoothness 和 collision objective 做双层底盘/机械臂轨迹优化。
与当前项目的联系：可参考子目标到可行轨迹的分层处理；本文没有双臂实验。

## 核心关键词

VLA、Mobile Manipulation、Whole-body Planning、Waypoint、Collision Avoidance、Generalization、固定底座 VLA 到移动操作的策略迁移、双层轨迹优化

## 快速摘要

### 研究问题

固定底座 VLA 不会生成移动底盘与机械臂协同运动轨迹。

### 之前方法的问题

移动操作示范昂贵，端到端方法难以覆盖多任务；分离式导航与操作可能产生错误累积。

### 核心思路

用预训练 VLA 生成末端 waypoint，再以 reachability、smoothness 和 collision objective 做双层底盘/机械臂轨迹优化。

### 输入

RGB-D、相机位姿、底盘和末端 proprioception、夹爪开合度、语言指令。

### 输出与动作

末端 waypoint，以及双层优化生成的移动底盘和机械臂协同轨迹。

### 数据集与评测基准

OVMM 仿真 benchmark 与三类移动操作真机任务。

### 主要结果

OVMM Overall SR 为 15.8%，比 KUZHUM 高 4.2 个百分点；真机 Stack Block、Open Drawer、Put in Bowl 分别为 30%、10%、40%（每项 10 次）。

### 与当前项目的关系

可参考子目标到可行轨迹的分层处理；本文没有双臂实验。

## 方法概览

任务输入 → 用预训练 VLA 生成末端 waypoint，再以 reachability、smoothness 和 collision objective 做双层底盘/机械臂轨迹优化 → 末端 waypoint，以及双层优化生成的移动底盘和机械臂协同轨迹。

## 实验与结果

### 数据集与评测基准

OVMM 仿真 benchmark 与三类移动操作真机任务。

### 主要结果

OVMM Overall SR 为 15.8%，比 KUZHUM 高 4.2 个百分点；真机 Stack Block、Open Drawer、Put in Bowl 分别为 30%、10%、40%（每项 10 次）。

## 与当前项目的关系

可参考子目标到可行轨迹的分层处理；本文没有双臂实验。

## 相关论文

- [[OpenVLA]]
- [[RDT-1B]]
