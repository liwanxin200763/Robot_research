---
paper_id: P169
title: "LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models"
---

# P169 · LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models

## 基本信息

- 作者：Lin Liu、Zhicheng Bao、Lu Zhang、Ziying Song、Wu Yang、Yuzheng Zhuang、Shuai Tao、Wulong Liu、Caiyan Jia、Huchuan Lu
- 年份：2026
- 发表 venue：arXiv 预印本
- 论文类型：基准测试与数据集
- 研究方向：失败恢复、机器人操作评测
- 关键词：failure recovery、recovery difficulty、policy-generated failure
- 论文链接：https://arxiv.org/abs/2609.05178
- DOI：https://doi.org/10.48550/arXiv.2609.05178
- arXiv：2609.05178
- 项目主页：
- 代码：
- 本地 PDF：[[00_论文池/PDFs/10_基准测试与数据集/LIBERO-RECOVER.pdf|LIBERO-RECOVER.pdf]]
- 引用量：
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

常规操作成功率不说明策略在抓空、错放或场景被改变后能否继续完成原任务。（第 1 节）

### 2. 论文要解决的问题

从实际策略产生的失败状态出发，独立量化不同模型的原任务恢复能力。（第 1 节）

### 3. 之前方法存在的问题

只评估初始状态任务成功，或者人为注入单一扰动，难覆盖策略真实造成的不同难度失败。（第 2 节）

### 4. 核心思路

让六类策略在 LIBERO 子任务运行，自然收集失败，再按恢复所需动作划分四级难度并由遥操作员示范恢复。（第 3 节）

### 5. 方法与系统结构

最新版论文报告 2,178 个失败情景、130 个 LIBERO 子任务；L1 重试，L2 适配动作，L3 恢复目标物体，L4 恢复环境。Qwen3.5 视频辅助标注时间性失败，四名遥操作员在 413 个情景中收集 3,184 条恢复轨迹。此工作是评测/数据资源，不是一套新恢复策略。（第 3 节、图 2）

### 6. 输入信息

失败后的机器人与场景观测、原始任务指令及可选时间上下文；不提供真实失败原因标签给每个基线作完美决策。（第 3–4 节）

### 7. 输出 / 动作表示

被测策略输出原生机器人动作；主要评价从失败状态恢复到原任务完成的成功率 RSR。（第 4 节）

### 8. 数据来源与采集方式

六种策略在模拟器中自然产生失败，不在 rollout 过程中人为植入；人类恢复示范来自四名操作者。（第 3 节）

### 9. 数据处理与数据增强

视频辅助失败定位与分级，训练/测试按情景排除重合；混合恢复数据及时间上下文用于基线分析。（第 3–4 节）

### 10. 训练方式

基准本身不训练统一恢复算法；实验对部分基线加入恢复数据进行微调，以衡量数据能否弥补退化。（第 4 节）

### 11. Benchmark 与实验设置

比较 π0、π0-fast、OpenVLA-OFT、GR00T 与视频世界模型等；指标包括 RSR、原基准性能退化和一致性。（第 4 节）

### 12. 真机实验

论文未报告真实机器人恢复试验；所有 2,178 个情景来自模拟基准。（第 3–4 节）

### 13. 主要实验结果

OpenVLA-OFT 的 LIBERO-100 常规成功率 94.5%，恢复基准仅 19.3%；部分 L4 情景成功率为 0。加入恢复数据后，恢复平均 20.8%→25.4%，普通 LIBERO 97.1%→96.6%；时间初始帧上下文 20.8%→26.8%。（第 4 节、结果表）

### 14. 消融实验

恢复训练数据和额外时间上下文各有小幅收益；较短动作片段更利于恢复反应。不能据此认为已有策略完整解决故障归因。（第 4 节）

### 15. Failure Case

从简单重试到必须复原被移动物体/场景的 L1–L4 均被收录；高级别失败对策略尤其困难。（第 3–4 节）

### 16. 主要局限

**环境动态类型：**弱动态；失败后物体和场景状态改变，非独立持续运动目标评测。

**失败闭环覆盖：**基准离线识别并分级失败，不自带部署时检测器或根因诊断器；恢复动作由被测策略生成，以原任务恢复成功率验证，也可用恢复数据微调；没有内建跨任务 Failure Memory。

作者的评测主要限于 LIBERO 风格模拟场景。按本库分析，它识别并分层失败，但没有部署时诊断器、恢复选择器、结果验证器或持久 Failure Memory；真机转移待验证。

### 17. 与已有工作的关系

可用于衡量 [[02_论文/07_泛化与长程任务/Recova - Agent-Guided Failure Recovery for Autonomous Robotic Manipulation|Recova]] 和 [[02_论文/01_VLA/Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action Models|FailBank]] 这类恢复/学习机制是否真正处理失败状态。

### 18. 对当前研究方向的价值

适合作为 Failure Memory + Recovery 的分级基准及失败数据来源：从 L2–L4 分析命令、实际场景、原因与恢复轨迹。其失败标签和示范本身不是可直接部署的共享双臂记忆。

### 19. 一句话总结

LIBERO-RECOVER 以策略真实失败构造分级恢复评测，揭示高常规成功率与低失败恢复能力之间的落差。
