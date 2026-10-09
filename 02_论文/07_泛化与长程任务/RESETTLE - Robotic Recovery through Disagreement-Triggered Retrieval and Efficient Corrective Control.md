---
paper_id: P177
title: "RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control"
---

# P177 · RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control

## 基本信息

- 作者：Yuxin Chen、Senqiao Yang、Zixuan Wang、Jinhui Ye、Changsheng Lu、Pengguang Chen、Shu Liu、Zhuotao Tian、Jiaya Jia
- 年份：2026
- 发表 venue：arXiv 预印本；未见正式会议或期刊接收信息
- 论文类型：机器人操作失败检测与局部恢复方法
- 研究方向：失败恢复、VLA、世界动作模型、部署期动作纠正
- 关键词：action disagreement、demonstration retrieval、V-JEPA 2-AC、state-servo、visual residual
- 论文链接：https://arxiv.org/abs/2610.12185
- DOI：10.48550/arXiv.2610.12185（arXiv 所列，注册待完成）
- arXiv：2610.12185
- 代码：https://github.com/JIA-Lab-research/RESETTLE（论文所列仓库当前为空，未见实现文件）
- 本地 PDF：[[00_论文池/PDFs/07_泛化与长程任务/RESETTLE.pdf|RESETTLE.pdf]]
- 引用量：
- 引用量来源：

## 详细摘要

### 1. 研究问题与先前不足

机器人策略在执行中遇到位置偏差、掉落或接触阻塞时，需要及时纠正。反复调用 VLM 或在线优化轨迹会增加延迟；额外训练基础策略又需要纠错数据。RESETTLE 研究的是**不更新基础策略权重**时，如何在动作执行接口检测异常并进行一次低延迟局部纠正。（第 1–2 节）

### 2. 核心方法

对同一观测和任务条件，用独立随机种子生成两个动作块；若时序加权的动作差异连续两次超过训练数据推理分布的 P95 阈值，就触发恢复。适配后的 V-JEPA 2-AC 编码器从同任务成功示范中检索最近的视觉帧及对应机器人状态。当前与参考状态之差给出 state-servo 先验，再以当前／参考画面的 guarded visual residual 作有限修正。每次只执行**一个原生控制动作**，重新观测后把控制权交还冻结的基础策略；部署时不运行辅助动力学预测器，也不额外调用 VLM。（第 3–4 节、图 2）

### 3. 数据、训练与实验设置

恢复模块离线使用专家示范训练，结合残差动作监督、原生动作对齐、潜在动力学预测及约束损失；同一评测环境的多种基础策略共享模块，但各基础策略阈值单独校准。仿真覆盖 LIBERO-Plus、Meta-World、RoboCasa Tabletop 与 LIBERO-Pro Swap；真机为单台 Franka Research 3 的四项**单臂**任务。基础策略包括 FastWAM、π0.5、QwenPI、SmolVLA、LDA、QwenGR00T；还测试与 Harness VLA 高层规划器组合。成对比较中基础策略权重不变。（第 5 节、图 3；附录 C、E）

### 4. 主要结果与基线

LIBERO-Plus 上，FastWAM 由 **49.3%→58.0%**，π0.5 由 **70.0%→73.7%**，QwenPI 由 **80.2%→84.6%**（表 1）；Meta-World 四难度组的非加权均值，QwenPI 为 **60.66%→65.99%**，SmolVLA 为 **59.20%→65.48%**（表 2）；RoboCasa Tabletop 的 QwenGR00T 为 **53.67%→60.50%**（表 3）。Harness VLA 在 LIBERO-Pro Swap 由 **42%→50%**（表 4）。真机每任务／方法 20 次，QwenPI 的四任务混合指标均值由 **66.67%→78.75%**，VLAct 由 **86.25%→92.92%**；其中 Use Spoon 使用阶段完成率，其余三项用成功率，不能把混合均值直接称为总成功率（表 5）。

在 QwenPI 实现上，监控加生成一次恢复动作的计算时间约 **83.6 ms**；与 VoLoAgent 的监控加规划 **322–1300 ms** 相比低 74.04%–93.57%。这一测量**不包含**基础策略推理、物理执行与端到端响应时间；两次连续超阈值也限制了触发速度。（第 6 节、表 6；附录 D.2）

### 5. 消融与失败案例

仅用 state-servo 时，LIBERO-Plus 三种基础策略的均值分别到 55.9%、72.9%、83.1%；加入 guarded visual residual 后到 58.0%、73.7%、84.6%（表 1）。P85、P90、P95、P99 阈值下的 QwenPI 总成功率分别为 83.1%、83.9%、84.6%、83.6%；更敏感的阈值并非在噪声扰动上最优（附录表 12）。

**作者展示的未触发失败：**碗被碰离位置、物品放错、抽屉卡住、指令不符或抓错物体时，两个动作提议仍可能一致（附录 D.3、图 8）。**触发后仍失败：**掉落后介入过晚、双物体误抓、抽屉卡住、动作预算耗尽、目标语义不符等（附录 D.3、图 9）。动作一致性并不证明动作正确，局部伺服也不保证无碰撞或目标符合指令。

### 6. 局限与本项目关联

**作者所述：**稳定但错误的动作可能避开 disagreement 触发器；即使触发，局部纠正也未必能处理物体丢失、复杂接触或语义目标错误。加入进度、接触或规划信号有潜力，但需要额外计算。（第 6 节、附录 D.3）

**文献库分析：**当前真机只验证单臂，尚无普通夹爪双臂协同证据；检索同任务成功示范依赖训练数据覆盖。可与 [[02_论文/07_泛化与长程任务/Recova - Agent-Guided Failure Recovery for Autonomous Robotic Manipulation|Recova]] 的独立恢复策略、[[02_论文/01_VLA/Taming VLAs under Robot Execution Errors - Self-Compensation and Stress Testing|Taming VLAs]] 的机械残差补偿比较，并设计“动作分歧＋接触／进度证据”的检测器，在双臂技能交接时验证触发率、错误恢复率与延迟。这些是研究建议，非论文已验证结论。
