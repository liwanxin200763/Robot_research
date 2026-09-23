# UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping

## 基本信息

- 作者：Wang, Wenbo; Wei, Fangyun; Zhou, Lei; Chen, Xi; Luo, Lin; Yi, Xiaohan; Zhang, Yizhong; Liang, Yaobo; Xu, Chang; Lu, Yan; Yang, Jiaolong; Guo, Baining
- 年份：2025
- 会议 / 期刊：CVPR
- CCF 等级：A
- 官方论文：https://openaccess.thecvf.com/content/CVPR2025/html/Wang_UniGraspTransformer_Simplified_Policy_Distillation_for_Scalable_Dexterous_Robotic_Grasping_CVPR_2025_paper.html
- 项目主页：https://dexhand.github.io/UniGraspTransformer/
- 官方代码：https://github.com/microsoft/UniGraspTransformer
- 主要分类：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 关键词：Dexterous Hand; Policy Distillation / Generalization

## 论文定位

这篇论文属于 A (CCF 7th edition; venue category not independently extracted from official PDF) 方向，主要讨论通用灵巧手抓取需要在不同物体类别上预测稳定抓法。
核心思路是UniGraspTransformer 用统一的 Transformer 网络预测灵巧抓取，并简化训练过程。
与当前项目的联系：Medium：模型结构可参考，但需重做普通夹爪动作输出。

## 核心关键词

Dexterous Hand、Policy Distillation、Generalization、venue category not independently extracted from official PDF)、Robot Manipulation、IL、Diffusion、Dexterous Manipulation

## 快速摘要

### 研究问题

通用灵巧手抓取需要在不同物体类别上预测稳定抓法。

### 之前方法的问题

复杂训练流程和手型依赖限制方法复用。

### 核心思路

UniGraspTransformer 用统一的 Transformer 网络预测灵巧抓取，并简化训练过程。

### 主要结果

作者报告在多个物体类别上优于 UniDexGrasp++；具体成功率需查实验表。

### 为什么重要

提供跨物体抓取模型的简洁架构基线。

### 与当前项目的关系

Medium：模型结构可参考，但需重做普通夹爪动作输出。

### 主要局限

灵巧手抓取 benchmark 与双臂真机任务仍有差距。

## 实验与结果

### 主要结果

作者报告在多个物体类别上优于 UniDexGrasp++；具体成功率需查实验表。

## 局限与启发

### 主要局限

灵巧手抓取 benchmark 与双臂真机任务仍有差距。

## 与当前项目的关系

Medium：模型结构可参考，但需重做普通夹爪动作输出。

## 相关论文

- [[Survey_of_Learning-Based_Approaches_for_Robotic_In-Hand_Manipulation]]

## 来源

- 官方论文：https://openaccess.thecvf.com/content/CVPR2025/html/Wang_UniGraspTransformer_Simplified_Policy_Distillation_for_Scalable_Dexterous_Robotic_Grasping_CVPR_2025_paper.html
- 项目主页：https://dexhand.github.io/UniGraspTransformer/
- 官方代码：https://github.com/microsoft/UniGraspTransformer
