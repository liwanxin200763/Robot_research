# FlowPolicy：通过一致性 Flow Matching 实现快速稳健的三维操作策略

## 基本信息

- 英文标题：FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation
- 作者：—
- 年份：2025
- 发表 venue：AAAI
- 论文类型：会议论文
- 研究方向：扩散模型 / 流匹配 / IL / RL
- 论文链接：[AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/33617)
- DOI：—
- arXiv：—
- 项目主页：—
- 代码：[GitHub](https://github.com/zql-kk/FlowPolicy)
- 本地 PDF：[[00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/FlowPolicy.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：20
- 引用量来源：OpenAlex
- 引用量来源链接：https://openalex.org/W4409365031
- 引用量查询日期：2026-09-27
- 引用量状态：已核验
- 引用量查询状态：verified
- OpenAlex Work ID：W4409365031
- 排序引用量：20
- 排序引用量来源：OpenAlex

### 出版与分类补充

- CCF 等级：A
- 关键词：Robot Manipulation; Consistency Flow Matching / 3D Policy

## 论文定位

这篇论文属于 A (CCF 7th edition; venue category not independently extracted from official PDF) 方向，主要讨论扩散/流式动作生成往往需要多次采样，在线控制延迟较高。
核心思路是FlowPolicy 使用三维点云和 consistency flow matching，在单次推理中生成动作。
与当前项目的联系：Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 核心关键词

Robot Manipulation、Consistency Flow Matching、3D Policy、venue category not independently extracted from official PDF)、IL、Diffusion

## 快速摘要

### 研究问题

扩散/流式动作生成往往需要多次采样，在线控制延迟较高。

### 之前方法的问题

生成质量与推理速度之间存在权衡。

### 核心思路

FlowPolicy 使用三维点云和 consistency flow matching，在单次推理中生成动作。

### 输入

官方摘要给出任务/数据类型；具体模型张量与接口需核对方法章节。

### 输出与动作

官方摘要未明确列出完整控制接口；需核对论文方法或代码。

### 数据集与评测基准

Adroit、MetaWorld。

### 主要结果

AAAI 摘要报告在 Adroit 与 MetaWorld 上保持有竞争力的成功率，同时推理速度提高约 7 倍。

### 为什么重要

双臂真机尤其关注动作频率；该工作可用于比较速度与成功率。

### 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 方法概览

任务输入 → FlowPolicy 使用三维点云和 consistency flow matching，在单次推理中生成动作 → 官方摘要未明确列出完整控制接口；需核对论文方法或代码。

## 实验与结果

### 数据集与评测基准

Adroit、MetaWorld。

### 主要结果

AAAI 摘要报告在 Adroit 与 MetaWorld 上保持有竞争力的成功率，同时推理速度提高约 7 倍。

## 局限与启发

### 主要局限

本段基于官方摘要；未覆盖全文失败案例、完整 Baseline 与方法消融。

## 与当前项目的关系

Medium：方法可借鉴，但迁移到当前双臂硬件需验证。

## 相关论文

- [[迈向统一理解机器人操作：综合综述]]

## 来源

- 官方论文：[AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/33617)
- 官方代码：[GitHub](https://github.com/zql-kk/FlowPolicy)
