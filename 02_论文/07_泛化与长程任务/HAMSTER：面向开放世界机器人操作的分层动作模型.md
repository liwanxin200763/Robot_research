# HAMSTER：面向开放世界机器人操作的分层动作模型

## 基本信息

- 英文标题：HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation
- 作者：[Y Li](https://scholar.google.com/citations?user=MW36lZUAAAAJ&hl=zh-CN&oi=sra) , [Y Deng](https://scholar.google.com/citations?user=jIZ6fmoAAAAJ&hl=zh-CN&oi=sra) , [J 张](https://scholar.google.com/citations?user=fSXCOfEAAAAJ&hl=zh-CN&oi=sra), [J Jang](https://scholar.google.com/citations?user=xL-7eFEAAAAJ&hl=zh-CN&oi=sra) …
- 年份：2025
- 发表 venue：ICLR
- 论文类型：会议论文
- 研究方向：泛化与长程任务
- 论文链接：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3bfee3bc6639c36e6e7b058db909f760-Abstract-Conference.html)
- DOI：—
- arXiv：—
- 项目主页：[项目主页](https://hamster-robot.github.io/)
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/07_泛化与长程任务/HAMSTER.pdf|查看 PDF]]
- 阅读状态：部分正文已核验
- 摘要依据：现有卡片资料；待本轮 PDF 复核
- 引用量：164
- 引用量来源：Google Scholar

### 出版与分类补充

- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)

## 论文定位

这篇论文属于 VLA / Robot Foundation Models / Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论开放世界操作需要利用基础模型知识，但机器人动作数据昂贵。
核心思路是HAMSTER 将高层任务理解与低层动作控制分工，降低双方负担。
与当前项目的联系：High：双臂普通夹爪可能需要高层分工和低层安全控制。

## 核心关键词

VLA、Robot Foundation Models、Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

开放世界操作需要利用基础模型知识，但机器人动作数据昂贵。

### 之前方法的问题

高层 VLM 不适合直接生成精细控制，低层策略又缺少广泛语义知识。

### 核心思路

HAMSTER 将高层任务理解与低层动作控制分工，降低双方负担。

### 主要结果

论文摘要报告该分层设计改善任务执行；统一数字需查实验表。

### 为什么重要

是比较分层规划和端到端 VLA 的阅读入口。

### 与当前项目的关系

High：双臂普通夹爪可能需要高层分工和低层安全控制。

### 主要局限

高低层接口不一致会造成目标误解或执行失败。

## 实验与结果

### 主要结果

论文摘要报告该分层设计改善任务执行；统一数字需查实验表。

## 局限与启发

### 主要局限

高低层接口不一致会造成目标误解或执行失败。

## 与当前项目的关系

High：双臂普通夹爪可能需要高层分工和低层安全控制。

## 相关论文

- [[将动作视为语言：在避免灾难性遗忘的条件下将 VLM 微调为 VLA]]
- [[从动作 Token 化视角综述 VLA 模型]]
- [[面向具身 AI 的 VLA 模型综述]]
- [[迈向统一理解机器人操作：综合综述]]
- [[SayCan：以机器人能力约束语言指令的落地执行]]

## 来源

- 官方论文：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3bfee3bc6639c36e6e7b058db909f760-Abstract-Conference.html)
- 项目主页：[项目主页](https://hamster-robot.github.io/)
