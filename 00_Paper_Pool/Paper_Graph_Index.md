# 论文关系图入口

从下方论文进入其 **Citation Relations**，即可在 Obsidian 中沿 wikilink 浏览。直接引用的类型、来源和核验日期以 [Citation_Network.csv](../01_Search/Citation_Graph/Citation_Network.csv) 为准。`Related` 表示技术相关，**不等于直接引用**。锚点选择见 [[00_Paper_Pool/Anchor_Papers|锚点论文]]；尚未加入主库的前置/后续论文见 [[00_Paper_Pool/Citation_Trace_Candidates|引用追踪候选]]。

## 主要锚点

- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]]：共享跨机器人数据；已核验 21 篇库内论文引用。
- [[02_Papers/01_VLA/OpenVLA|OpenVLA]]：开放 VLA 基线；19 篇。
- [[02_Papers/01_VLA/Octo|Octo]]：开放通用机器人策略；18 篇。
- [[02_Papers/10_Benchmark_Dataset/DROID|DROID]]：大规模真机数据；14 篇。
- [[02_Papers/03_Bimanual/RDT-1B|RDT-1B]]：双臂扩散策略；10 篇。
- [[02_Papers/01_VLA/SayCan|SayCan]]：语言与技能可执行性结合；7 篇。

## 已核验的引用链

箭头 `A → B` 表示 **B 引用了 A**，不能据此直接断言 B 继承了 A 的算法。

- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]] → [[02_Papers/01_VLA/Octo|Octo]] → [[02_Papers/01_VLA/OpenVLA|OpenVLA]] → [[02_Papers/01_VLA/TraceVLA|TraceVLA]]。
- [[02_Papers/01_VLA/SayCan|SayCan]] → [[02_Papers/01_VLA/Octo|Octo]] → [[02_Papers/01_VLA/OpenVLA|OpenVLA]] → [[02_Papers/01_VLA/Actions_as_Language|Actions as Language]]。
- [[02_Papers/10_Benchmark_Dataset/DROID|DROID]] → [[02_Papers/01_VLA/OpenVLA|OpenVLA]] → [[02_Papers/01_VLA/CoT-VLA|CoT-VLA]]。
- [[02_Papers/03_Bimanual/RDT-1B|RDT-1B]] → [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]]。

## VLA

[[02_Papers/01_VLA/Octo|Octo]] · [[02_Papers/01_VLA/OpenVLA|OpenVLA]] · [[02_Papers/01_VLA/TraceVLA|TraceVLA]] · [[02_Papers/01_VLA/ReconVLA|ReconVLA]]。阅读时比较语言条件、动作输出和 Grounding 证据。

## Language / Planning / Grounding

[[02_Papers/01_VLA/SayCan|SayCan]] 是技能规划锚点；[[02_Papers/01_VLA/RoboGround|RoboGround]] 和 [[02_Papers/01_VLA/ReconVLA|ReconVLA]] 关注视觉目标对齐。SayCan 的 BC-Z 与 MT-Opt 前置工作仍在候选清单，尚未创建主卡。

## Robot Manipulation

[[02_Papers/02_Robot_Manipulation/ManipLLM|ManipLLM]] · [[02_Papers/01_VLA/ReconVLA|ReconVLA]] · [[02_Papers/06_Diffusion_Flow_IL_RL/3D_Diffuser_Actor|3D Diffuser Actor]]。

## Bimanual

[[02_Papers/03_Bimanual/RDT-1B|RDT-1B]] · [[02_Papers/03_Bimanual/AnyBimanual|AnyBimanual]] · [[02_Papers/03_Bimanual/2HandedAfforder|2HandedAfforder]] · [[02_Papers/03_Bimanual/YOTO|YOTO]]。重点比较双臂数据、协调方式和普通夹爪的适配成本。

## Sim2Real

[[02_Papers/05_Sim2Real/Sim2Real-VLA|Sim2Real-VLA]] · [[02_Papers/03_Bimanual/ALOHA_Unleashed|ALOHA Unleashed]] · [[02_Papers/01_VLA/OpenVLA|OpenVLA]]。这些是主题相关入口；直接引用仍以卡片中的证据为准。

## Diffusion / Flow

[[02_Papers/03_Bimanual/RDT-1B|RDT-1B]] · [[02_Papers/06_Diffusion_Flow_IL_RL/3D_Diffuser_Actor|3D Diffuser Actor]] · [[02_Papers/06_Diffusion_Flow_IL_RL/FlowPolicy|FlowPolicy]]。

## Imitation Learning

[[02_Papers/01_VLA/Octo|Octo]] · [[02_Papers/01_VLA/OpenVLA|OpenVLA]] · [[02_Papers/03_Bimanual/RDT-1B|RDT-1B]]。ACT 和 Diffusion Policy 的代码学习入口在 [[08_Tech_Stack/Minimal_Reproduction_Path|最小复现路线]]，当前不额外复制论文主卡。

## Generalist Robot Policy / Cross-Embodiment

[[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]] → [[02_Papers/01_VLA/Octo|Octo]] → [[02_Papers/01_VLA/OpenVLA|OpenVLA]]（已核验引用）。跨本体训练不自动等于迁移到本项目的双臂普通夹爪。

## Long-Horizon / Failure Recovery

[[02_Papers/01_VLA/SayCan|SayCan]] · [[02_Papers/07_Generalization_LongHorizon/Policy_Decorator|Policy Decorator]] · [[02_Papers/07_Generalization_LongHorizon/Self-Correcting_Robot_Manipulation_via_Gaussian-Splatted_Foresight|Gaussian-Splatted Foresight]]。这些是问题主题入口，不在此处暗示未核验的引用边。

## Robot Data / Dexterous

数据：[[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]] · [[02_Papers/10_Benchmark_Dataset/DROID|DROID]] · [[02_Papers/10_Benchmark_Dataset/RoboCasa|RoboCasa]]。灵巧操作：[[02_Papers/04_Dexterous/DexUMI|DexUMI]] · [[02_Papers/04_Dexterous/UniDex|UniDex]] · [[02_Papers/04_Dexterous/DexHandDiff|DexHandDiff]]。

## 覆盖边界

当前共有 **215 条**已核验有向 References；对应的 215 条 Cited By 只是反向视图，另有 20 条单独标注的 Related。没有边的论文表示尚未核验到关系，不代表互不相关。详见 [[01_Search/Citation_Graph/Research_Lineage|技术脉络]]。
