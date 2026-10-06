# UAOR: Uncertainty-aware Observation Reinjection for Vision-Language-Action Models

## 基本信息

- 作者：Jiabing Yang、Yixiang Chen、Yuan Xu、Peiyan Li、Zichen Wen、Bowen Fang、Tao Yu、Xiangnan Wu、Qisen Ma、Kai Wang、Ziheng He、Yingda Li、Zhengbo Zhang、Jing Liu、Nianfeng Liu、Yan Huang、Liang Wang
- 年份：2026
- 发表 venue：arXiv 预印本
- 论文类型：方法论文
- 研究方向：VLA、动作不确定性、视觉观测
- 关键词：action entropy、observation reinjection、uncertainty
- 论文链接：https://arxiv.org/abs/2602.18020
- DOI：https://doi.org/10.48550/arXiv.2602.18020
- arXiv：2602.18020
- 项目主页：https://uaor.jiabingyang.cn/
- 代码：
- 本地 PDF：[[00_论文池/PDFs/01_VLA/UAOR.pdf|UAOR.pdf]]
- 引用量：
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

VLA 的语言和历史上下文可能压弱当前视觉与本体信息，动作 token 在困难时刻表现出较高不确定性。（第 1 节）

### 2. 论文要解决的问题

在不重训主干的条件下，于动作不确定时强化当前观测对 VLA 内部表征的影响。（第 1 节）

### 3. 之前方法存在的问题

统一地强化全部观测可能干扰已确定的动作；只靠模型原始注意力未必能在关键层保留及时感知。（第 2 节）

### 4. 核心思路

根据动作 token 熵选择高不确定层，将当前已编码的视觉和本体特征检索并回注至模型隐藏状态。（第 3 节）

### 5. 方法与系统结构

从前馈网络内的 key-value 表征检索观测信息，在高熵位置以系数融合；最有效配置选取 top-K 约 256 项。这里的 reinjection 是同一次推理中重用当前观测，并非外部重新拍摄、等待目标稳定或维护跨时段记忆。（第 3 节、图 2）

### 6. 输入信息

当前图像、本体状态、语言指令以及模型内部动作分布；未输入失败类型或场景变化率。（第 3 节）

### 7. 输出 / 动作表示

基础 VLA 仍输出原形式动作；UAOR 修改内部表征，未增加显式停止、回滚或重新规划动作。（第 3 节）

### 8. 数据来源与采集方式

评估 LIBERO、SIMPLER、CALVIN 和真实 Franka 四任务；真机每任务 50 条示范、20 次测试。（第 4 节）

### 9. 数据处理与数据增强

核心处理是观测特征检索、熵门控与特征融合；论文未报告以数据增强作为主要贡献。（第 3 节）

### 10. 训练方式

以插入式模块适配不同 VLA，包括 OpenVLA-OFT、π0、CogACT、LLaVA-VLA；主要贡献是推理表征调节，而非重新收集失败恢复训练数据。（第 3–4 节）

### 11. Benchmark 与实验设置

比较多个基础策略的原始与回注后表现，并消融注意力检索方式、熵门控与回注层选择。（第 4 节）

### 12. 真机实验

单台 Franka Research 3 的四项任务：OpenVLA-OFT 平均 55%→72.5%，CogACT 63.8%→78.8%；未测试双臂或执行中独立移动目标。（第 4 节）

### 13. 主要实验结果

LIBERO 上 OpenVLA-OFT 97.1%→98.0%、π0 91.7%→93.2%；SIMPLER CogACT 73.1%→75.7%；CALVIN 平均连续完成长度 3.55→3.67。（第 4 节、主结果表）

### 14. 消融实验

注意力检索加熵门控为 98.0%，均值池化 96.8%，全量注意力 96.7%；阈值和回注层敏感。（第 4 节、消融表）

### 15. Failure Case

论文没有系统标注失败类型、原因及恢复结果；不确定性升高只能作为内部信号，不能自动说明物体移动或执行器未按命令动作。

### 16. 主要局限

**环境动态类型：**静态随机化；任务环境并非专门的执行中持续运动目标基准。

作者实验范围主要是既有静态或每 episode 初始化随机化的基准与单臂真机。按本库分析，熵不是已校准的任务风险概率，也不提供旧记忆清除、物理反馈或完整恢复闭环。

### 17. 与已有工作的关系

与 [[02_论文/01_VLA/SafeLoop - Risk-Aware Rollback for Vision-Language-Action Manipulation|SafeLoop]] 的外部风险决策不同，UAOR 在 VLA 推理内部强化当前观测；两种不确定性信号不可直接等同。

### 18. 对当前研究方向的价值

可作为双臂 VLA 行动不确定性探针与 Risk-Aware Action Gating 的候选特征，但必须单独验证它是否预示真实执行误差。论文没有 Failure Memory、双臂协作或 DH116 实验。

### 19. 一句话总结

UAOR 在动作高熵时回注当前观测特征，改善若干 VLA 基准，但未实现环境重观测和失败恢复。
