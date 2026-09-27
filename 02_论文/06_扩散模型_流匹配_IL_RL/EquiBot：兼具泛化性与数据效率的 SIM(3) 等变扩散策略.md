# EquiBot：兼具泛化性与数据效率的 SIM(3) 等变扩散策略

## 基本信息

- 英文标题：EquiBot: SIM(3)-Equivariant Diffusion Policy for Generalizable and Data Efficient Learning
- 作者：—
- 年份：2024
- 发表 venue：CoRL
- 论文类型：会议论文
- 研究方向：扩散模型 / 流匹配 / IL / RL
- 论文链接：[PMLR](https://proceedings.mlr.press/v270/yang25a.html)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/EquiBot.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：4
- 引用量来源：OpenAlex
- 引用量来源链接：https://openalex.org/W4400373516
- 引用量查询日期：2026-09-27
- 引用量状态：已核验
- 引用量查询状态：verified
- OpenAlex Work ID：W4400373516
- 排序引用量：4
- 排序引用量来源：OpenAlex

### 出版与分类补充

- CCF 等级：Not CCF A (robotics venue extension; CCF row not asserted)

## 论文定位

这篇论文属于 Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论少量示范条件下，操作策略要面对物体和空间变化。
核心思路是EquiBot 在模仿学习策略中加入等变结构，提高数据效率和空间泛化。
与当前项目的联系：Medium：双臂空间变化可能受益，但平台不同。

## 核心关键词

Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

少量示范条件下，操作策略要面对物体和空间变化。

### 之前方法的问题

普通网络不一定充分利用旋转、平移等几何对称性。

### 核心思路

EquiBot 在模仿学习策略中加入等变结构，提高数据效率和空间泛化。

### 主要结果

作者报告在六项移动操作任务的多个真机变化中展示泛化；具体数值见论文。

### 为什么重要

提供以结构先验替代部分示范数据的路线。

### 与当前项目的关系

Medium：双臂空间变化可能受益，但平台不同。

### 主要局限

移动操作结果不能直接替代普通夹爪双臂评测。

## 实验与结果

### 主要结果

作者报告在六项移动操作任务的多个真机变化中展示泛化；具体数值见论文。

## 局限与启发

### 主要局限

移动操作结果不能直接替代普通夹爪双臂评测。

## 与当前项目的关系

Medium：双臂空间变化可能受益，但平台不同。

## 相关论文

- [[迈向统一理解机器人操作：综合综述]]

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v270/yang25a.html)
