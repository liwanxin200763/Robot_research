---
paper_id: P052
title: "When Instructions Retrieve Trajectories: Diagnosing and Mitigating Generalization Failures in VLA Models"
---

# P052 · When Instructions Retrieve Trajectories: Diagnosing and Mitigating Generalization Failures in VLA Models

## 基本信息

- 作者：Hung-Jen Chen、Yu-Hsun Hou、Yan-Hong Chen、Yan-Fu Chen、Binghua Cai、Min Sun、Chun-Yi Lee
- 年份：2026
- 发表 venue：arXiv 预印本
- 论文类型：VLA 失效诊断与反事实训练方法
- 研究方向：VLA；视觉语言 grounding；泛化
- 关键词：Instruction-Action Binding；Equivariant Counterfactual Training；LIBERO-PRO；CALVIN；UR5e
- 论文链接：[arXiv 论文](https://arxiv.org/abs/2609.39971)
- DOI：[10.48550/arXiv.2609.39971](https://doi.org/10.48550/arXiv.2609.39971)
- arXiv：[2609.39971](https://arxiv.org/abs/2609.39971)
- 项目主页：—
- 代码：—
- 本地 PDF：—
- 引用量：
- 引用量来源：Google Scholar

## 领域地图级总结

**问题与缺口。**VLA 在原分布任务成功，并不说明能在“同一指令、不同场景需采取不同动作”时重新选择行为。作者把这种错误称为 *instruction-action binding*：语言可能检索出熟悉轨迹，视觉只微调其执行。位于“语言／视觉 grounding → 数据监督 → 泛化失败诊断”。

**方法。**分析微调后的 π₀.₅ 与 GR00T-N1.7，区分不改变所需动作的外观扰动和要求不同动作的反事实扰动。Equivariant Counterfactual Training（ECT）一方面构造动作有效的场景—动作配对示范，另一方面在一次优化中共同训练原示范和对应反事实；关键是补足同一语言条件下不同场景需要不同动作的监督，而非单纯增加相似示范。

**数据、观测与动作。**研究在已有 VLA 的图像＋语言→连续动作接口上加入反事实训练，不提出新的统一动作空间。反事实构造、动作有效性、训练预算与数据增强细节待读全文核对。

**评测与结果。**官方摘要报告 LIBERO-PRO 受控比较中，π₀.₅ 的位置交换成功率 **36%→59%**；真实 UR5e、固定示范预算下，未见位置成功率 **8%→88%**。CALVIN 上在没有新增示范的情况下提升五任务完成，但摘要没有给出具体数值，故不补猜。上述两个数字属于不同场景设置。

**失败、局限与价值。**作者在 381 个针对性 π₀.₅ 轨迹中观察到约 **69%** 延续原任务、切换到其他已示范任务或形成混合轨迹，说明问题不等于完全忽略语言。官方 HTML 的局限章节说明，方法需要动作有效、依赖场景的替代示范；未测无任务微调的通用部署、接触密集操作、移动操作和导航。对当前普通夹爪双臂研究，优先测试“换物体位置后指令是否真正改变动作选择”。与 [[02_论文/01_VLA/ReconVLA - Reconstructive Vision-Language-Action Model as Effective Robot Perceiver|ReconVLA]] 的视觉 grounding 问题相关，但失效机制不应视为相同。
