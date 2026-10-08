---
paper_id: P077
title: "TAO-DA: Towards Autonomous Operation—A Dual-Arm Vision-Language-Action Model for Coordinated Manipulation"
---

# P077 · TAO-DA: Towards Autonomous Operation—A Dual-Arm Vision-Language-Action Model for Coordinated Manipulation

## 基本信息

- 作者：Yongsheng Zhao、Han Gao、Baoping Cheng、Jingyao Tang、Dian Zhou、Deng Liang、Ji Ge、Xuanzhang Wen、Lei Zhao、Ye Wang
- 年份：2026
- 发表 venue：arXiv 预印本
- 论文类型：方法与机器人系统
- 研究方向：双臂协作、VLA
- 关键词：dual-arm VLA、dual-tower、intent routing、task progress
- 论文链接：https://arxiv.org/abs/2609.33197
- DOI：https://doi.org/10.48550/arXiv.2609.33197
- arXiv：2609.33197
- 项目主页：
- 代码：
- 本地 PDF：[[00_论文池/PDFs/03_双臂协作/TAO-DA.pdf|TAO-DA.pdf]]
- 引用量：
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

双臂任务既有单臂分工，也有共同操作；单个共享动作头容易受到非活动手臂状态干扰。（第 1 节）

### 2. 论文要解决的问题

让一个 VLA 根据指令和视觉判断当前参与的手臂，并以相对独立的左右臂动作专家执行协调任务。（第 1 节）

### 3. 之前方法存在的问题

单动作塔可能把另一臂无关状态混入动作生成；刚性指定参与手臂难适应不同任务阶段。（第 2 节）

### 4. 核心思路

冻结共享视觉语言骨干，为左右臂建立独立 DiT 动作塔，并加入双臂意图路由和任务进度估计。（第 3 节）

### 5. 方法与系统结构

Eagle2.5-VL/SigLIP 特征共享，两个 flow-matching 动作塔分别预测左右臂动作；语言初始路由，再由视觉分类器调整活动手臂。GRU 加交叉注意力估计归一化轨迹时间作为进度。左右臂是独立 expert，不是两个可对话的 agent；没有显式通信、debate 或共享长期记忆。（第 3 节、图 2）

### 6. 输入信息

视觉、语言、双臂关节状态与任务上下文；进度目标来自轨迹时间，不能等同于语义目标完成或失败验证。（第 3 节）

### 7. 输出 / 动作表示

左右动作塔分别生成连续动作并按路由执行；两个专家可服务同一双臂任务，但不是 leader 先向 follower 发消息。（第 3 节）

### 8. 数据来源与采集方式

AGIBOT G1 双臂真机 9,080 条遥操作轨迹，覆盖六类任务；每臂 7 自由度。（第 4 节）

### 9. 数据处理与数据增强

为左右臂动作分别建立监督，利用轨迹相对时间训练进度分支；论文未报告独立图像或状态增强贡献。（第 3–4 节）

### 10. 训练方式

视觉语言骨干冻结，双 DiT 塔以 flow matching 学习动作；路由器学习活动手臂类别，进度头学习轨迹时间。（第 3 节）

### 11. Benchmark 与实验设置

比较 Single Tower、Dual-Mask、Dual-Tower 及 GR00T、π0.5，评估六项真机任务、路由准确率与非活动臂状态扰动。（第 4 节）

### 12. 真机实验

AGIBOT G1 双臂；Collaborative Tea 成功率 100%，Desktop Organization 95%。六台机器人餐厅系统 101 次完整任务成功率 92.08%，该系统结果不能单独归因于 VLA。（第 4 节）

### 13. 主要实验结果

单臂任务平均 88.4%，GR00T 82.0%，π0.5 80.5%。非活动臂关节扰动下 Dual-Tower 两任务保持 100%/95%，Single Tower 降至 25%/20%。（第 4 节、结果表）

### 14. 消融实验

Single/Dual-Mask/Dual-Tower 比较支持分离动作塔对状态串扰的鲁棒性；路由类别准确率报告 85.37%/83.31%/96.13%，但没有充分隔离路由模块对最终成功率的因果贡献。（第 4 节）

### 15. Failure Case

未报告“一臂失败，另一臂协助恢复”的系统实验；非活动臂状态扰动是输入噪声/干扰，不等于外部动态物体或真实执行失败。（第 4 节）

### 16. 主要局限

**环境动态类型：**静态随机化；非活动臂状态扰动不等于外部场景持续运动。

论文中比较模型参数规模与训练配置并非完全匹配。按本库分析，进度是时间代理变量，不是任务成功核验；系统无失败原因通信、持久共享记忆或恢复选择。

### 17. 与已有工作的关系

相较 [[02_论文/03_双臂协作/Bimanual Robot Manipulation via Multi-Agent In-Context Learning|BiCICLe]] 的双代理顺序关键位姿，TAO-DA 是共享感知主干下双动作专家的端到端 VLA。

### 18. 对当前研究方向的价值

可作双臂普通夹爪 VLA 的专家隔离与意图路由基线。若研究 DH116 加双臂共享 Failure Memory，需要另建语义进度验证及跨臂失败信息交换；本文尚无这些实验。

### 19. 一句话总结

TAO-DA 通过共享视觉语言骨干和左右独立动作塔降低双臂动作串扰，但不是多代理通信或失败互助系统。
