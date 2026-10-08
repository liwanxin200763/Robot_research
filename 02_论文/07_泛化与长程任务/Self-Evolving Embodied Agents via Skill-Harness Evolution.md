---
paper_id: P138
title: "Self-Evolving Embodied Agents via Skill-Harness Evolution"
---

# P138 · Self-Evolving Embodied Agents via Skill-Harness Evolution

## 基本信息

- 作者：Peidong Wang、Zhiming Ma、Ying Chang、Xufang Luo、Yiqun Zhang、Zihan Wang、Xiaocui Yang、Shi Feng、Yuqing Yang、Dongsheng Li
- 年份：2026
- 发表 venue：arXiv 预印本
- 论文类型：方法论文
- 研究方向：具身智能体、自我改进、长程操作
- 关键词：skill evolution、harness evolution、rollout feedback、self-improvement
- 论文链接：https://arxiv.org/abs/2608.11350
- DOI：https://doi.org/10.48550/arXiv.2608.11350
- arXiv：2608.11350
- 项目主页：
- 代码：
- 本地 PDF：[[00_论文池/PDFs/07_泛化与长程任务/SHAPER.pdf|SHAPER.pdf]]
- 引用量：
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

具身代理反复遇到相似任务和失败，固定的技能提示与执行代码不会自动吸收经验。（第 1 节）

### 2. 论文要解决的问题

让代理从 rollout 结果中同时改进技能描述和执行框架，而无需更新底层 VLM/VLA 参数。（第 1 节）

### 3. 之前方法存在的问题

只更新技能库会保留僵硬的执行流程；只修改框架又难积累任务特定技能。（第 2 节）

### 4. 核心思路

把文本技能与 Python 执行 harness 作为可修订的外部记忆，由成功/失败 rollout 摘要驱动候选改写、沙箱检查与选择。（第 3 节）

### 5. 方法与系统结构

冻结 VLM 规划器及 VLA 执行器，利用执行前后视觉判断器生成反馈；同一模型根据 episode 摘要改写技能和 harness，经沙箱验证后采用 top-K beam 搜索。储存的是可重用技能和流程，不是结构化的失败前观测、命令、实际执行、原因、恢复结果全链记录。（第 3 节、图 2）

### 6. 输入信息

任务目标、视觉观测、现有技能/harness、执行轨迹与视觉结果判断。未显式估计场景变化率或机器人执行残差。（第 3 节）

### 7. 输出 / 动作表示

产出更新的文本技能、Python 执行流程及下一次代理调用；底层动作由冻结执行器/API 完成。可通过新策略再次执行，但不是实时安全回滚。（第 3 节）

### 8. 数据来源与采集方式

在 VLABench 与 ESI Bench 任务中收集代理 rollout；VLABench 报告 15 个训练与 24 个验证任务。（第 4 节）

### 9. 数据处理与数据增强

将前后视觉证据和执行结果压缩为 episode 摘要，候选代码经沙箱检查；论文未报告传统图像数据增强的独立收益。（第 3 节）

### 10. 训练方式

不微调基础模型，迭代生成、执行、评估、改写技能与 harness；比较不同记忆/流程修订配置。（第 3–4 节）

### 11. Benchmark 与实验设置

VLABench 四组各 200 episode；ESI Bench 231 项子集，并分别统计 micro/macro 成功率。（第 4 节）

### 12. 真机实验

论文未报告真实机器人实验；结果主要来自模拟或 API 执行环境。（第 4 节）

### 13. 主要实验结果

VLABench Seed Agent 28.25%、SHAPER 34.5%、直接 VLA 23.25%；ESI Bench micro 32.5%→49.8%、macro 31.2%→42.9%。（第 4 节、结果表）

### 14. 消融实验

仅技能进化 33.5%，仅 harness 进化 30.5%，两者联合 34.5%，支持双层改写互补。（第 4 节、消融表）

### 15. Failure Case

案例显示代理识别执行停滞并修改后续指令；但视觉判断错误或候选代码未覆盖新物理状态时仍会失败。论文没有系统量化失败原因诊断准确率。（第 4 节）

### 16. 主要局限

**环境动态类型：**静态随机化；rollout 经验跨回合积累，未验证外部持续运动目标。

**失败闭环覆盖：**前后视觉判断器评价 rollout，摘要驱动下一轮技能与 harness 改写；可从失败中非参数化改进，但不是部署当下的故障根因诊断、恢复选择、回滚及原任务续接系统。

作者提出跨执行体与真实机器人迁移为后续方向。按本库分析，改写代码和提示的离线迭代不等于部署时毫秒级失败恢复；缺少动态目标、双臂和 DH116 证据。

### 17. 与已有工作的关系

与 [[02_论文/01_VLA/Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action Models|FailBank]] 同样利用失败经验，但 SHAPER 主要修订代理技能和执行框架，而非更新基础 VLA 权重。

### 18. 对当前研究方向的价值

适合作为“失败经验怎样转化为未来改进”的 agent 层基线；可探索将结构化 Failure Memory 蒸馏成共享双臂恢复技能，但这种记忆结构与真机互助尚未在论文中实现。

### 19. 一句话总结

SHAPER 利用执行结果共同改写技能和外部执行框架，在模拟基准提升具身代理的长期表现。
