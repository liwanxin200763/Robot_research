# Demystifying Robot Diffusion Policies: Action Memorization and a Simple Lookup Table Alternative

## 基本信息

- 年份：2026
- 会议 / 期刊：ICLR
- CCF 等级：A (CCF 7th edition; venue category not independently extracted from official PDF)
- 官方论文：https://proceedings.iclr.cc/paper_files/paper/2026/hash/122ea6470232ee5e79a2649243348005-Abstract-Conference.html
- 项目主页：https://stanfordmsl.github.io/alt/
- 主要分类：Imitation Learning / Diffusion / Flow Matching / Robot Manipulation

## 论文定位

这篇论文属于 Imitation Learning / Diffusion / Flow Matching / Robot Manipulation 方向，主要讨论Diffusion Policy 在少量示范下表现强，但其成功来源不够清楚。
核心思路是提出 Action Lookup Table 作为简单对照，分析 Diffusion Policy 与 ACT 在动作记忆和插值上的差异。
与当前项目的联系：High：项目需用未见物体和场景测试真实泛化。

## 核心关键词

Imitation Learning、Diffusion、Flow Matching、Robot Manipulation、IL

## 快速摘要

### 研究问题

Diffusion Policy 在少量示范下表现强，但其成功来源不够清楚。

### 之前方法的问题

需要区分动作分布建模、记忆和插值各自的贡献。

### 核心思路

提出 Action Lookup Table 作为简单对照，分析 Diffusion Policy 与 ACT 在动作记忆和插值上的差异。

### 主要结果

论文报告 Diffusion Policy 有较强动作记忆，ACT 更偏动作插值；精确性能比较需看实验表。

### 为什么重要

防止把复杂模型的优势误判成真正泛化。

### 与当前项目的关系

High：项目需用未见物体和场景测试真实泛化。

### 主要局限

简单查表基线的有效性依赖示范分布；真机长任务仍需验证。

## 实验与结果

### 主要结果

论文报告 Diffusion Policy 有较强动作记忆，ACT 更偏动作插值；精确性能比较需看实验表。

## 局限与启发

### 主要局限

简单查表基线的有效性依赖示范分布；真机长任务仍需验证。

## 与当前项目的关系

High：项目需用未见物体和场景测试真实泛化。

## 来源

- 官方论文：https://proceedings.iclr.cc/paper_files/paper/2026/hash/122ea6470232ee5e79a2649243348005-Abstract-Conference.html
- 项目主页：https://stanfordmsl.github.io/alt/
