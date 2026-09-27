# 论文引用图索引

从下方论文进入其 **Citation Relations**，即可在 Obsidian 中沿 wikilink 浏览。直接引用的类型、来源和核验日期以 [Citation_Network.csv](../01_Search/Citation_Graph/Citation_Network.csv) 为准。`Related` 表示技术相关，**不等于直接引用**。锚点选择见 [[00_Paper_Pool/Anchor_Papers|锚点论文]]；尚未加入主库的前置/后续论文见 [[00_Paper_Pool/Citation_Trace_Candidates|引用追踪候选]]。

## 主要锚点

- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment：机器人学习数据集与 RT-X 模型]]：共享跨机器人数据；已核验 21 篇库内论文引用。
- [[02_Papers/01_VLA/OpenVLA|OpenVLA：开源视觉—语言—动作模型]]：开放 VLA 基线；19 篇。
- [[02_Papers/01_VLA/Octo|Octo：开源通用机器人策略]]：开放通用机器人策略；18 篇。
- [[02_Papers/10_Benchmark_Dataset/DROID|DROID：大规模自然场景机器人操作数据集]]：大规模真机数据；14 篇。
- [[02_Papers/03_Bimanual/RDT-1B|RDT-1B：面向双臂操作的扩散基础模型]]：双臂扩散策略；10 篇。
- [[02_Papers/01_VLA/SayCan|SayCan：以机器人能力约束语言指令的落地执行]]：语言与技能可执行性结合；7 篇。

## 已核验的引用链

箭头 `A → B` 表示 **B 引用了 A**，不能据此直接断言 B 继承了 A 的算法。

- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment：机器人学习数据集与 RT-X 模型]] → [[02_Papers/01_VLA/Octo|Octo：开源通用机器人策略]] → [[02_Papers/01_VLA/OpenVLA|OpenVLA：开源视觉—语言—动作模型]] → [[02_Papers/01_VLA/TraceVLA|TraceVLA：以视觉轨迹提示增强通用机器人策略的时空感知]]。
- [[02_Papers/01_VLA/SayCan|SayCan：以机器人能力约束语言指令的落地执行]] → [[02_Papers/01_VLA/Octo|Octo：开源通用机器人策略]] → [[02_Papers/01_VLA/OpenVLA|OpenVLA：开源视觉—语言—动作模型]] → [[02_Papers/01_VLA/Actions_as_Language|将动作视为语言：在避免灾难性遗忘的条件下将 VLM 微调为 VLA]]。
- [[02_Papers/10_Benchmark_Dataset/DROID|DROID：大规模自然场景机器人操作数据集]] → [[02_Papers/01_VLA/OpenVLA|OpenVLA：开源视觉—语言—动作模型]] → [[02_Papers/01_VLA/CoT-VLA|CoT-VLA：面向 VLA 的视觉思维链推理]]。
- [[02_Papers/03_Bimanual/RDT-1B|RDT-1B：面向双臂操作的扩散基础模型]] → [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA：通过统一扩散与自回归扩展机器人基础模型]]。

## VLA

[[02_Papers/01_VLA/Octo|Octo：开源通用机器人策略]] · [[02_Papers/01_VLA/OpenVLA|OpenVLA：开源视觉—语言—动作模型]] · [[02_Papers/01_VLA/TraceVLA|TraceVLA：以视觉轨迹提示增强通用机器人策略的时空感知]] · [[02_Papers/01_VLA/ReconVLA|ReconVLA：以重建增强机器人感知的 VLA 模型]]。阅读时比较语言条件、动作输出和 Grounding 证据。

## 语言 / 规划 / Grounding

[[02_Papers/01_VLA/SayCan|SayCan：以机器人能力约束语言指令的落地执行]] 是技能规划锚点；[[02_Papers/01_VLA/RoboGround|RoboGround：利用有视觉定位能力的视觉—语言先验实现机器人操作]] 和 [[02_Papers/01_VLA/ReconVLA|ReconVLA：以重建增强机器人感知的 VLA 模型]] 关注视觉目标对齐。SayCan 的 BC-Z 与 MT-Opt 前置工作仍在候选清单，尚未创建主卡。

## 机器人操作

[[02_Papers/02_Robot_Manipulation/ManipLLM|ManipLLM：面向物体中心机器人操作的具身多模态大语言模型]] · [[02_Papers/01_VLA/ReconVLA|ReconVLA：以重建增强机器人感知的 VLA 模型]] · [[02_Papers/06_Diffusion_Flow_IL_RL/3D_Diffuser_Actor|3D Diffuser Actor：基于三维场景表征的策略扩散]]。

## 双臂操作

[[02_Papers/03_Bimanual/RDT-1B|RDT-1B：面向双臂操作的扩散基础模型]] · [[02_Papers/03_Bimanual/AnyBimanual|AnyBimanual：迁移单臂策略以实现通用双臂操作]] · [[02_Papers/03_Bimanual/2HandedAfforder|2HandedAfforder：从人类视频学习精确可执行的双臂可供性]] · [[02_Papers/03_Bimanual/YOTO|YOTO：从视频示范一次性学习双臂机器人操作]]。重点比较双臂数据、协调方式和普通夹爪的适配成本。

## Sim2Real

[[02_Papers/06_Diffusion_Flow_IL_RL/Sim2Real-VLA|Sim2Real-VLA：将合成技能零样本泛化到真实操作]] · [[02_Papers/03_Bimanual/ALOHA_Unleashed|ALOHA Unleashed：实现机器人灵巧操作的简明方法]] · [[02_Papers/01_VLA/OpenVLA|OpenVLA：开源视觉—语言—动作模型]]。这些是主题相关入口；直接引用仍以卡片中的证据为准。

## 扩散模型 / Flow Matching

[[02_Papers/03_Bimanual/RDT-1B|RDT-1B：面向双臂操作的扩散基础模型]] · [[02_Papers/06_Diffusion_Flow_IL_RL/3D_Diffuser_Actor|3D Diffuser Actor：基于三维场景表征的策略扩散]] · [[02_Papers/06_Diffusion_Flow_IL_RL/FlowPolicy|FlowPolicy：通过一致性 Flow Matching 实现快速稳健的三维操作策略]]。

## 模仿学习

[[02_Papers/01_VLA/Octo|Octo：开源通用机器人策略]] · [[02_Papers/01_VLA/OpenVLA|OpenVLA：开源视觉—语言—动作模型]] · [[02_Papers/03_Bimanual/RDT-1B|RDT-1B：面向双臂操作的扩散基础模型]]。ACT 和 Diffusion Policy 的代码学习入口在 [[08_Tech_Stack/Minimal_Reproduction_Path|最小复现路线]]，当前不额外复制论文主卡。

## 通用机器人策略 / 跨本体

[[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment：机器人学习数据集与 RT-X 模型]] → [[02_Papers/01_VLA/Octo|Octo：开源通用机器人策略]] → [[02_Papers/01_VLA/OpenVLA|OpenVLA：开源视觉—语言—动作模型]]（已核验引用）。跨本体训练不自动等于迁移到本项目的双臂普通夹爪。

## 长程任务 / 失败恢复

[[02_Papers/01_VLA/SayCan|SayCan：以机器人能力约束语言指令的落地执行]] · [[02_Papers/07_Generalization_LongHorizon/Policy_Decorator|Policy Decorator：对大型策略模型进行模型无关的在线优化]] · [[02_Papers/07_Generalization_LongHorizon/Self-Correcting_Robot_Manipulation_via_Gaussian-Splatted_Foresight|通过 Gaussian Splatting 前瞻实现自纠正机器人操作]]。这些是问题主题入口，不在此处暗示未核验的引用边。

## 机器人数据 / 灵巧操作

数据：[[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment：机器人学习数据集与 RT-X 模型]] · [[02_Papers/10_Benchmark_Dataset/DROID|DROID：大规模自然场景机器人操作数据集]] · [[02_Papers/10_Benchmark_Dataset/RoboCasa|RoboCasa：面向通用机器人的大规模家务任务仿真]]。灵巧操作：[[02_Papers/04_Dexterous/DexUMI|DexUMI：以人手作为灵巧操作的通用操作接口]] · [[02_Papers/04_Dexterous/UniDex|UniDex：从第一人称人类视频学习通用灵巧手控制]] · [[02_Papers/04_Dexterous/DexHandDiff|DexHandDiff：面向自适应灵巧操作的交互感知扩散规划]]。

## 覆盖边界

当前共有 **215 条**已核验有向 References；对应的 215 条 Cited By 只是反向视图，另有 20 条单独标注的 Related。没有边的论文表示尚未核验到关系，不代表互不相关。详见 [[01_Search/Citation_Graph/Research_Lineage|技术脉络]]。
