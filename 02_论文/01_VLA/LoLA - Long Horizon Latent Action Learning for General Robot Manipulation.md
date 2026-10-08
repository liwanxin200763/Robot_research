---
paper_id: P029
title: "LoLA: Long Horizon Latent Action Learning for General Robot Manipulation"
---

# P029 · LoLA: Long Horizon Latent Action Learning for General Robot Manipulation

## 基本信息

- 作者：Xiaofan Wang、Xingyu Gao、Jianlong Fu、Zuolei Li、Dean Fortier、Galen Mullins、Andrey Kolobov、Baining Guo
- 年份：2025
- 发表 venue：arXiv 预印本；正式会议未核验
- 论文类型：预印本；长时序 VLA 模型
- 研究方向：VLA；长程机器人操作；多视角视觉；机器人状态对齐
- 关键词：LoLA；State-Aware Latent Re-representation；Proprioception；Conditional Flow Matching
- 论文链接：[arXiv 论文](https://arxiv.org/abs/2512.20166)
- DOI：
- arXiv：[2512.20166](https://arxiv.org/abs/2512.20166)
- 项目主页：
- 代码：
- 本地 PDF：[[00_论文池/PDFs/01_VLA/LoLA.pdf|查看 PDF]]
- 引用量：9
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

复杂操作会跨越多个子任务；单帧 VLA 难辨任务进度，长程执行中的小偏差又可能逐渐累积。（论文第 1 节）

### 2. 论文要解决的问题

让策略同时利用多视角历史画面和机器人本体状态，在较长任务中输出物理尺度一致的连续动作。（第 1、3 节）

### 3. 之前方法存在的问题

纯视觉语言表征与末端动作缺少物理对齐，简单拼接关节状态并不能充分过滤背景干扰；全量视频处理成本过高。（第 2–3 节）

### 4. 核心思路

当前帧保持高保真，历史帧降采样提取运动；State-Aware Latent Re-representation（SALR）使机器人状态在 VLM 各层调制视觉语言特征，再由动作专家生成动作块。（第 3 节，图 2）

### 5. 方法与系统结构

Qwen2.5-VL-7B 编码多视角视觉和语言；并行的 State Transformer 用关节角、末端位姿等形成 Query，在逐层与 VLM Key/Value 做乘性融合，再经可学习掩码抑制动作无关特征，送入 Conditional Flow Matching Action Expert。默认取 25 个历史帧。（第 3、6.3 节）

### 6. 输入信息

多视角 RGB、当前与降采样历史画面、语言指令，以及关节角、末端位置、夹爪宽度等 Proprioception；真机使用四个摄像头。（第 3、6.2 节）

### 7. 输出 / 动作表示

动作专家用 Conditional Flow Matching 生成多步连续机器人动作；不同机器人动作维度按各自具身映射，不能简化为纯文本动作。（第 3、6.3 节）

### 8. 数据来源与采集方式

预训练混合 OXE 与 AgiBot，约 100 万条轨迹／6200 万时间点；Franka 用 Xbox 控制器遥操作采集 28 项任务，另有双臂 Aloha BusyBox。（第 4、6.1–6.2 节）

### 9. 数据处理与数据增强

当前图像 224×224、历史图像 112×112；历史序列下采样并经可学习掩码过滤。其他统一的数据增强方案：论文未报告。（第 3、6.2 节）

### 10. 训练方式

跨具身数据端到端预训练并在下游场景微调；论文报告用 32 张 A100、batch 1280 训练约 14 天。不是接到任意 VLA 就能免训练生效的插件。（第 4、6.1–6.4 节）

### 11. Benchmark 与实验设置

SIMPLER、LIBERO、Franka 长程／短程任务以及双臂 Aloha BusyBox；对比 Diffusion Policy、π0 等；Franka 设置有 7 组顺序长程任务和 6 项不重置连续任务。（第 4、6.2 节）

### 12. 真机实验

Franka Research 3 与双臂 Aloha 均有评测；BusyBox 六类任务平均成功率 LoLA 46.7%、π0 30.0%、Diffusion Policy 8.3%（附录表 9）。（第 4.4、7 节）

### 13. 主要实验结果

LIBERO 加入机器人状态对齐，平均成功率从 84.7% 到 91.2%（表 7）。Franka 多步任务三个分组至少完成两子任务的比例分别为 5.9%、33.1%、28.9%，其中首组低于 π0 的 17.8%，不可声称所有设置均领先（表 6）。

### 14. 消融实验

移除历史帧、SALR、冻结 VLM 等组件分别比较；状态对齐消融显示 84.7%→91.2%（第 4.5 节，表 5、7）。

### 15. Failure Case

作者指出长程任务中早期轻微扰动可积累成偏离训练分布；Franka 首组多步结果偏弱。没有证明重大失败后自动重新规划或恢复。（第 1、4.4、5 节）

### 16. 主要局限

作者明确指出复杂、新颖或强扰动的长程执行仍不够稳健，动态闭环恢复重大失败是未来工作；训练资源开销也高。（第 5、6.4 节）

### 17. 与已有工作的关系

相比只在末端拼接状态的 VLA，SALR 在逐层特征空间做状态锚定；相比 ContextVLA 的视觉上下文压缩，它更强调视觉与物理动作空间对齐。（第 2–3 节）

### 18. 对当前研究方向的价值

给“历史视觉＋Proprioception”提供参考，但尤其值得研究的是作者留下的强扰动下动态失败恢复缺口。（第 5 节）

### 19. 一句话总结

LoLA 用历史多视角与状态感知潜在表征支持长程操作，改善多项模拟与真机任务，但严重执行失败后的恢复仍未解决。

## 我的阅读笔记

已核对本地 PDF 的正文与附录，特别区分表 6 中的弱项与作者第 5 节提出的恢复局限。
