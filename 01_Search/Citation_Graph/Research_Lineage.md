# 研究技术脉络

本文用两类箭头：**已核验引用**表示右侧论文在正式 bibliography 中引用了左侧论文，证据见 [Citation_Network.csv](Citation_Network.csv)；**技术梳理**只是文献库对方法演化的解释，不能当成直接引用或继承关系。图谱当前只覆盖部分可访问的 bibliography，缺边不代表没有引用。

## 1. Language Planning / Grounding

**已核验引用：** [[02_Papers/01_VLA/SayCan|SayCan]] → [[02_Papers/01_VLA/Octo|Octo]] → [[02_Papers/01_VLA/OpenVLA|OpenVLA]] → [[02_Papers/01_VLA/TraceVLA|TraceVLA]]。

**技术梳理：** SayCan 把语言上合适的技能与当前机器人可执行的技能结合；后续通用策略和 VLA 越来越多地直接从视觉、语言生成动作。[[02_Papers/01_VLA/ReconVLA|ReconVLA]] 又把目标区域的视觉 Grounding（落到真实物体/区域）作为重点。这里的“技能规划 → 端到端动作预测 → 视觉目标对齐”是比较视角，不宣称每一步是算法直接继承。SayCan 明确使用的 BC-Z、MT-Opt 见 [[00_Paper_Pool/Citation_Trace_Candidates|引用追踪候选]]。

**待检验的问题：** 对双臂普通夹爪，语言规划选对技能后，如何验证动作确实完成？错误目标定位又怎样触发安全重规划？

## 2. Imitation / Action Generation

**技术梳理（非直接引用链）：** Behavior Cloning（行为克隆）→ ACT 的 Action Chunk（动作块）→ Diffusion Policy（扩散式动作生成）→ Flow Matching（流匹配）→ VLA Action Head（动作输出头）。这条路线说明动作预测从单步监督学习，逐渐扩展到多步生成、分布建模与视觉语言条件化；它不是按唯一时间顺序排列的祖谱。

**库内证据：** [[02_Papers/06_Diffusion_Flow_IL_RL/3D_Diffuser_Actor|3D Diffuser Actor]] 研究三维条件化动作生成；[[02_Papers/03_Bimanual/RDT-1B|RDT-1B]] 研究双臂扩散策略，且被 [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]] 在 bibliography 中引用。可运行的学习顺序见 [[08_Tech_Stack/Minimal_Reproduction_Path|最小复现路线]]。

## 3. Generalist Robot Policy / Cross-Embodiment

**已核验引用：** [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]] → [[02_Papers/01_VLA/Octo|Octo]] → [[02_Papers/01_VLA/OpenVLA|OpenVLA]]。

**技术梳理：** 标准化多机器人数据使共享训练成为可能，Octo 展示开放的通用机器人策略，OpenVLA 则结合视觉语言预训练和机器人示范。跨本体训练不自动等于在另一种双臂夹爪上成功；动作空间和相机布局仍需对齐。

## 4. Single-arm → Bimanual

**技术梳理：** 单臂通用策略（[[02_Papers/01_VLA/OpenVLA|OpenVLA]]）与双臂示范/策略（[[02_Papers/03_Bimanual/RDT-1B|RDT-1B]]、[[02_Papers/03_Bimanual/ALOHA_Unleashed|ALOHA Unleashed]]）可放在同一对照框架；[[02_Papers/03_Bimanual/2HandedAfforder|2HandedAfforder]] 则关注双手可行动作区域。这些方法不构成单一直接引用链。

**待检验的问题：** 左右臂动作怎样同步？一只手固定物体、另一只手操作时，动作表示和评测该怎样定义？

## 5. Simulation → Real Robot

**技术梳理：** Simulation（仿真）→ synthetic data（合成数据）→ domain adaptation/randomization（域适配/随机化）→ Sim2Real（仿真到现实）→ [[02_Papers/05_Sim2Real/Sim2Real-VLA|Sim2Real-VLA]]。这是一条实验设计线，不是逐篇引用链。

**待检验的问题：** 合成训练对真实双臂接触、夹爪滑脱和多步误差积累的帮助，需要在同一任务、同一数据预算下测量。

## 图谱边界

截至 2026-09-23，库内有 215 条已核验的有向 References 关系；Cited By 是它们的反向视图，不能再加一次当作新引用。Related Work 只表示技术相关。引用关系说明“作者讨论过”，不等同于“直接继承方法”。
