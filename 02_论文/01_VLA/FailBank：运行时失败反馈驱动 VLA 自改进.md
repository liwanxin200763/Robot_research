# FailBank：运行时失败反馈驱动 VLA 自改进

## 基本信息

- 英文标题：Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action Models
- 作者：Mingyue Cui、Zheyuan Liu、Yihan Zhu、Zheyuan Zhang、Meng Jiang
- 年份：2026
- 发表 venue：arXiv 预印本
- 论文类型：VLA 运行时反馈与策略后训练
- 研究方向：VLA；失败恢复；安全操作；Self-Improvement
- 关键词：Failure Bank；Runtime Shield；Control Barrier Function；LoRA；VLA-Arena
- 论文链接：[arXiv 论文](https://arxiv.org/abs/2609.39820)
- DOI：[10.48550/arXiv.2609.39820](https://doi.org/10.48550/arXiv.2609.39820)
- arXiv：[2609.39820](https://arxiv.org/abs/2609.39820)
- 项目主页：[作者项目页](https://mingyuee88.github.io/FailBank/)
- 代码：[官方 GitHub](https://github.com/Mingyuee88/FailBank)（含代码、测试、最小示例；依赖 VLA-Arena 与相应权重）
- 本地 PDF：—
- 引用量：
- 引用量来源：Google Scholar

## 领域地图级总结

**问题与缺口。**运行时安全屏蔽器可改掉当下危险动作，但原策略不变，同类动作会反复被纠正，甚至停滞。本文将“安全模块提议的纠正”转成后续策略训练信号，位于“执行反馈 → 失败记录 → 策略更新”，不只是部署时套一层 shield。

**方法与数据。**四阶段为：让策略自主执行、CBF 教师旁路提出反事实纠正；按结果筛选有效记录并保留成功原动作作稳定锚；累计 failure bank；用受约束的 LoRA 更新并通过留出数据筛选新策略。数据来自策略自己的执行轨迹和教师提议，而非一般离线 teleoperation。部署仍须另行确认感知与硬件条件。

**观测与动作。**沿用 π₀.₅、π₀ 等 VLA 的视觉与本体状态、连续动作接口；CBF 教师在采集阶段使用额外几何信息，不能把其输入当成部署时策略天然可得。官方项目页说明部署策略只需 RGB 与本体状态。

**评测与结果。**在 VLA-Arena 静态障碍任务的两种难度及两种骨干上，作者报告相对原策略任务成功率分别增加 **8.5、6.9 个百分点**，策略造成的累计代价分别减少 **35.6%、23.8%**；相对 AEGIS 运行时 shield，成功率增加 **25.4、9.5 个百分点**，代价相近。更新数据仅从 Level 1 Mango 收集；另外九项任务未参与该收集。不能把这些仿真结果写作真机成功率。

**失败、局限与价值。**项目页消融显示，直接把 shield 放入采集闭环会产生 shield 自己造成的失败轨迹；旁路教师可减少这种偏差。论文将动态障碍、跨平台实体部署等列为边界，现阶段不应称已经解决真实机器人在线恢复。对双臂普通夹爪，可测试“纠正建议是否形成有用训练样本”，但需要先设计碰撞代价和安全的数据收集协议。
