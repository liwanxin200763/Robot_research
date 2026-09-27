# MoManipVLA：迁移 VLA 模型以实现通用移动操作

## 基本信息

- 英文标题：MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation
- 作者：Zhenyu Wu、Yuheng Zhou、Xiuwei Xu、Ziwei Wang、Haibin Yan
- 年份：2025
- 发表 venue：CVPR 2025，页码 1714–1723
- 论文类型：会议论文
- 研究方向：VLA
- 论文链接：[CVF Open Access PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Wu_MoManipVLA_Transferring_Vision-language-action_Models_for_General_Mobile_Manipulation_CVPR_2025_paper.pdf)；[arXiv](https://arxiv.org/abs/2503.13446)
- DOI：未在本次检查的 CVF 官方论文页核实到会议 DOI；arXiv DOI：10.48550/arXiv.2503.13446
- arXiv：2503.13446
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/01_VLA/MoManipVLA.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：0
- 引用量来源：OpenAlex
- 引用量来源链接：https://openalex.org/W6967143107
- 引用量查询日期：2026-09-27
- 排序引用量：0
- 排序引用量来源：OpenAlex

### 出版与分类补充

- CCF 等级：A
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

- [[OpenVLA：开源视觉—语言—动作模型]]
- [[RDT-1B：面向双臂操作的扩散基础模型]]
