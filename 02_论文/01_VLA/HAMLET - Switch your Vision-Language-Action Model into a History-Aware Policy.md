# HAMLET：将现有VLA改造成历史感知策略

## 基本信息

- 英文标题：HAMLET: Switch your Vision-Language-Action Model into a History-Aware Policy
- 作者：Myungkyu Koo、Daewon Choi、Taeyoung Kim、Kyungmin Lee、Changyeon Kim、Younggyo Seo、Jinwoo Shin
- 年份：2026
- 发表 venue：ICLR 2026（论文 PDF 首页载明已发表）
- 论文类型：会议论文；已有 VLA 的历史感知微调框架
- 研究方向：VLA；历史感知；长时序操作；部分可观测
- 关键词：HAMLET；Moment Tokens；Time-Contrastive Learning；Memory Module；GR00T
- 论文链接：[arXiv 论文](https://arxiv.org/abs/2510.00695)
- DOI：
- arXiv：[2510.00695](https://arxiv.org/abs/2510.00695)
- 项目主页：[HAMLET 项目页](https://myungkyukoo.github.io/hamlet/)
- 代码：[作者 GitHub](https://github.com/myungkyuKoo/HAMLET-Isaac-GR00T)
- 本地 PDF：[[00_论文池/PDFs/01_VLA/HAMLET.pdf|查看 PDF]]
- 引用量：54
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

当目标被遮住或任务有多步依赖时，当前帧不足以判断已拿起、已覆盖或已放置的对象；直接叠加多帧导致昂贵延迟和显存占用。（论文第 1 节，图 1）

### 2. 论文要解决的问题

不从头预训练 VLA，而在既有策略上以轻量模块引入历史信息，并保持推理效率和通用任务表现。（第 1、3 节）

### 3. 之前方法存在的问题

朴素 4 帧输入相对单帧前向慢约 35%，峰值附加显存约 3.6 倍；历史帧还可能带入静态背景或伪时序相关性，降低泛化。（第 1、4 节，表 4）

### 4. 核心思路

每时刻用少量 moment tokens 摘要任务相关视觉，再由轻量 Memory Transformer 聚合历史；先用时间对比学习初始化令牌，强化不同时刻可区分的变化。（第 3 节，图 2）

### 5. 方法与系统结构

在 VLM 输入追加 moment tokens；其表示与视觉、语言交互后被缓存。2 层 Memory Transformer 对历史 token 产生记忆条件，再交给原动作专家。默认 4 个 token／时刻、历史长度 4；这是微调框架，不是无训练插件。（第 3、4 节）

### 6. 输入信息

当前视觉、任务语言、缓存 moment token；原底座动作专家仍可接机器人 Proprioception。论文方法本身并非只存历史动作或长期自然语言摘要。（第 3 节，式 1–2）

### 7. 输出 / 动作表示

沿用 GR00T N1.5 或 CogACT 原动作专家与动作块；HAMLET 提供历史条件，不发明新的统一动作空间。（第 3–4 节）

### 8. 数据来源与采集方式

真机设计三类历史依赖任务，单任务分别训练并以 24 次试验评估；仿真使用 RoboCasa Kitchen、LIBERO、SimplerEnv-Bridge 的原有示范。（第 4.1 节；附录 A）

### 9. 数据处理与数据增强

时间对比学习把同帧的颜色／模糊／噪声／遮挡扰动样本作正例，同一轨迹其他时刻作难负例；训练历史令牌而非缓存原始全帧。（第 3.1 节）

### 10. 训练方式

先以时间对比目标初始化 moment tokens，再按既有底座的微调配置训练 VLA 加记忆模块；不能误写成从零预训练或完全免训练。（第 3、4.1 节）

### 11. Benchmark 与实验设置

真机 PnP Twice、CoverNStack、Swap Cubes 等三项长程历史任务；仿真 RoboCasa Kitchen、LIBERO、SimplerEnv-Bridge；对比 π0、π0-FAST、GR00T N1/N1.5、CogACT 和朴素多帧。（第 4 节，表 1–3）

### 12. 真机实验

Franka Research 3 及第三人称／腕部视觉设置，三项任务各 24 次；GR00T N1.5 完整成功率均值 29.2%，朴素多帧 45.8%，加 HAMLET 76.4%（表 1；附录 A）。

### 13. 主要实验结果

RoboCasa Kitchen 100 示范设置 62.6%→65.4%，论文摘要所述 64.1%→66.4% 对应 300 示范，不能混淆；LIBERO 95.6%→97.6%（表 2）。CogACT 在 SimplerEnv-Bridge 52.1%→63.5%（表 3）。4 帧推理 80.5 ms 基线、108.5 ms 朴素多帧、82.4 ms HAMLET（表 4）。

### 14. 消融实验

RoboCasa 100 示范：无记忆 62.6%，仅 moment token 63.1%，再加时间对比 63.4%，记忆模块加时间对比 65.4%；Transformer 优于简单 token 拼接 62.7%（表 5）。

### 15. Failure Case

附录 B 描述无历史底座因遮挡或中间状态不明而动作混乱，朴素多帧可能过早进入下一步且不能从失败状态返回。HAMLET 主要补足状态识别；论文未建立通用故障原因诊断或显式重规划器。（附录 B.2，图 13）

### 16. 主要局限

**环境动态类型：**静态随机化；历史观测用于动作决策，未验证外部持续运动目标。

作者明确写出时间对比初始化带来额外训练成本，而且方案未必直接适用于自回归 VLA；目前主要在扩散型动作模型上验证。（附录 C Discussion）

### 17. 与已有工作的关系

区别于 ContextVLA 在 VLM 中间层池化历史，HAMLET 在底座外使用时刻 token 和记忆模块；区别于 MEM 的语言长时记忆，它主要处理较短的视觉历史。（第 2–3 节；跨论文比较）

### 18. 对当前研究方向的价值

可作为现成 VLA 接入历史上下文的高效基线；尤其适合测试“观察到失败前后状态”是否足以改善后续动作，但显式执行误差解释仍需补充。（第 4 节；文献库分析）

### 19. 一句话总结

HAMLET 通过时间对比初始化的 moment tokens 和轻量记忆模块，为已有 VLA 增加低开销历史感知，显著改善遮挡和多步任务。

## 我的阅读笔记

已核对本地 PDF 正文及附录 B／C；表 2 的 100 与 300 示范结果分别记录。
