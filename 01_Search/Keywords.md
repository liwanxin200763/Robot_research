# 检索关键词树

适用年份：2024–2026。组合检索只发现线索，不自动判定论文合格。不同平台对 AND、OR 和站点限定的支持不同，应按平台调整。

## 任务与本体

- Robot Manipulation（机器人操作）
- Bimanual Manipulation（双臂操作）
- Dual-arm Manipulation（双臂操作同义词）
- Dexterous Manipulation（灵巧操作）
- Dexterous Hand（灵巧手）

## 模型与学习

- Vision-Language-Action（视觉-语言-动作）
- VLA（视觉-语言-动作缩写）
- Robot Foundation Model（机器人基础模型）
- Imitation Learning（模仿学习）
- Behavior Cloning（行为克隆）
- Diffusion Policy（扩散策略）
- Flow Matching（流匹配）
- Reinforcement Learning（强化学习）

## 能力与评价

- Generalization（泛化）
- Zero-shot（零样本）
- Failure Recovery（失败恢复）
- Long-horizon（长时序）
- Data Efficiency（数据效率）

## 数据与部署

- Human Demonstration（人类示范）
- Teleoperation（遥操作）
- Human Video（人类视频）
- Real-world Robot Manipulation（真实世界机器人操作）

## 组合检索式示例

```text
("vision-language-action" OR VLA) AND (manipulation OR grasping)
```

```text
("bimanual manipulation" OR "dual-arm manipulation") AND ("imitation learning" OR "diffusion policy")
```

```text
("dexterous manipulation" OR "dexterous hand") AND (generalization OR "data efficiency")
```

```text
("robot foundation model" OR VLA) AND ("failure recovery" OR "long-horizon")
```

```text
("human demonstration" OR teleoperation OR "human video") AND "robot manipulation"
```

```text
("flow matching" OR "behavior cloning" OR "reinforcement learning") AND manipulation
```

```text
"VLA" "CVPR" "2025"
```

```text
"bimanual manipulation" "ICLR" "2026"
```

```text
site:openaccess.thecvf.com "manipulation" "2024"
```

```text
site:proceedings.neurips.cc "robot" "2025"
```

分别叠加 2024、2025、2026 与候选 Venue。命中论文后必须核验正式 Proceedings、论文类型、官方代码归属及实际代码内容。搜索结果中的会议或代码标签不构成入库证据。


## Incremental Keywords（增量关键词） · 2026-09-18

本轮从官方论文及作者实现核查中提取，关键词不自动赋予论文准入资格。来源和核查状态见[Search Log（检索日志）](Search_Log_2026-09-18.md)。

- **Action Chunking（动作分块）**：联系RDT的连续动作片段与当前ACT/双臂控制。
- **Action Tokenization（动作标记化）**：追踪SpatialVLA、LAPA如何连接离散表示与实际动作。
- **Cross-Embodiment（跨机器人本体迁移）**：RDT、TwinVLA、VideoVLA涉及跨本体知识迁移；检索数据与动作对齐。
- **World Model（世界模型）**：3D-VLA通过预测未来视觉状态联系动作；用于追踪预测与控制的连接。
- **Affordance Reasoning（可供性推理）**：AffordDexGrasp、OmniManip连接任务语义与可操作区域/约束。
- **Contact-rich Manipulation（接触密集型操作）**：DexHandDiff及DextER强调接触；追踪接触约束与动作成功的关系。
- **Visual Trace Prompting（视觉轨迹提示）**：TraceVLA利用历史运动轨迹增强时空感知，可继续比较历史观测表示。
- **Latent Action Pretraining（潜动作预训练）**：LAPA从缺少动作标签的视频学习；适合追踪人类视频到机器人数据的转换。
- **Consistency Flow Matching（一致性流匹配）**：FlowPolicy用一致性约束减少推理步数；便于比较扩散策略的部署代价。
- **Policy Distillation（策略蒸馏）**：UniGraspTransformer把专用策略经验汇总为通用策略。
- **Generative Digital Twin（生成式数字孪生）**：RoboTwin关联场景生成、专家示范和双臂评测。
- **Residual Reinforcement Learning（残差强化学习）**：ManipTrans与VLM Scaffolding通过残差策略修正参考动作。
- **Sim-to-Real Transfer（仿真到现实迁移）**：Scaffolding与RoboTwin涉及仿真/真机关系，适合后续核查部署前提。
- **Joint Attention（联合注意力）**：TwinVLA连接两个单臂分支；适合检索双臂信息交换结构。


## Broad Discovery Additions（广泛发现阶段增量关键词） · 2026-09-18

本轮按官方题录/摘要补充，以下为与既有关键词表不重复的净增量；仅作检索线索。详细来源见 [Search_Log_Broad_2026-09-18.md](Search_Log_Broad_2026-09-18.md)。

- **Bimanual Coordination**（双臂协同）｜任务与本体：区分双臂同时协同与单臂独立执行，检索交接、稳定与双臂规划。
- **Parallel Gripper**（平行夹爪）｜任务与本体：与当前NERO普通夹爪本体匹配，便于筛除仅适用于多指手的特化方法。
- **Mobile Manipulation**（移动操作）｜任务与本体：区分固定双臂与移动底盘+机械臂系统，寻找数据采集和全身控制方案。
- **Hierarchical VLA**（分层视觉-语言-动作模型）｜模型与学习：对照高层语义规划和低层闭环控制，适用于长任务。
- **Video Diffusion Policy**（视频扩散策略）｜模型与学习：连接未来视觉预测、世界模型与动作输出，查数据效率和部署延迟。
- **Equivariant Diffusion Policy**（等变扩散策略）｜模型与学习：追踪空间对称性先验如何降低示范需求并改善位姿泛化。
- **Asynchronous Inference**（异步推理）｜模型与学习：检索VLA推理与动作执行并行时的对齐、接续和失败恢复。
- **Cross-Embodiment Transfer**（跨本体迁移）｜模型与学习：比较从单臂、双臂、移动平台向目标机器人迁移策略和数据。
- **Long-Horizon Manipulation**（长时序操作）｜能力与评价：关注任务分解、阶段性目标和持续执行中的恢复机制。
- **Affordance Transfer**（可供性迁移）｜能力与评价：把物体/任务级可操作区域转化为抓取或放置策略，并评估零样本泛化。
- **Bimanual Benchmark**（双臂评测基准）｜能力与评价：查任务集、双臂协调指标、仿真随机化和真机复测协议。
- **Human Motion Capture Demonstrations**（人类动作捕捉示范）｜数据与部署：比较无机器人遥操作、手部追踪和示范重定向的数据获取路径。
- **Teleoperation Data Collection**（遥操作数据采集）｜数据与部署：检索低成本双臂采集系统、同步、多视角和数据质量。
- **Visual-Tactile Pretraining**（视觉-触觉预训练）｜数据与部署：用于灵巧操作扩展；判断触觉是否对普通夹爪操作有可迁移价值。
- **Mixed-Quality Demonstrations**（混合质量示范）｜数据与部署：检索示范质量识别、在线纠正、人工干预和失败数据利用。
