# VLA
此页根据论文主卡中的分类、子分类、标签、关键词和机器人形态字段维护。每篇论文只保留一张实体主卡。

## 新收录的交叉入口

- [[02_论文/01_VLA/Same Scene, Different Task - Skill Alignment for Compositional Generalization in VLAs|CRAFT]]：针对 VLA 微调时的 vision shortcut，用反事实指令与可复用技能表示训练未示范的技能组合；Piper 真机未示范组合成功 43/60，完整微调为 9/60。
- [[02_论文/01_VLA/Divide-and-Remember - Recursive Action-Relevant Memory for Long-Horizon VLA Policies|Divide-and-Remember]]：递归选择与动作相关的历史视觉 token；RoboMME 16 项平均成功率 38.6%，真机四项任务 35/40。
- [[02_论文/01_VLA/Taming VLAs under Robot Execution Errors - Self-Compensation and Stress Testing|Taming VLAs]]：部署时依靠命令—执行残差调整 π0／π0.5 动作专家；RoboStress 压力测试与两台 Piper 真机验证机械误差预补偿。
- [[02_论文/07_泛化与长程任务/LT-Mem - Volatility-Aware Spatio-Temporal Memory for Lifelong Scene Understanding|LT-Mem]]：跨会话世界状态记忆，可作为长程 VLA 的潜在外部状态输入；本文没有训练 VLA 策略。
- [[02_论文/01_VLA/ECoMEM - Explicit Concept Memory for Memory-Dependent Robot Control|ECoMEM]]：显式概念库接入 VLA，记录对象、事件次数和程序状态；RoboMME 16 任务平均成功率 82.42%。
- [[02_论文/01_VLA/MemoryVLA - Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation|MemoryVLA]]：VLA 主卡；双流记忆支持长时序操作，ICLR 2026，官方代码已开放。
- [[02_论文/02_机器人操作/FP2 - Equipping Robotic Foundation Models with Force Control|FP2]]：机器人操作主卡；给 VLA／世界模型式基础策略增加高频受力调节，arXiv 2026，代码尚未公开。
- [[02_论文/02_机器人操作/PEARS - Physical-Prior-Guided Efficient Adaptation via Failure Reasoning and Diffusion Steering for Tactile Manipulation|PEARS]]：机器人操作主卡；在冻结 VLA／VTLA 基础策略上，以触觉失败判断调整接触力，并在潜在噪声空间学习运动纠错。
- [[02_论文/07_泛化与长程任务/RESETTLE - Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control|RESETTLE]]：失败恢复主卡；监测冻结 VLA／WAM 的动作提议分歧，并用同任务示范做单步纠正；动作稳定但错误时可能漏检。

## 优先级与特别关注

### [[02_论文/01_VLA/ReconVLA - Reconstructive Vision-Language-Action Model as Effective Robot Perceiver|ReconVLA：以重建增强机器人感知的 VLA 模型]]

- 年份： 2026
- 会议 / 期刊： AAAI
- 代码开放情况：已开放
- 阅读优先级： P1

### [[02_论文/03_双臂协作/TwinVLA - Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models|TwinVLA：以两个单臂 VLA 模型实现数据高效的双臂操作]]

- 年份： 2026
- 会议 / 期刊： ICLR
- 代码开放情况：已开放
- 阅读优先级： P0

### [[02_论文/06_扩散模型_流匹配_IL_RL/Sim2Real-VLA - Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation|Sim2Real-VLA：将合成技能零样本泛化到真实操作]]

- 年份： 2026
- 会议 / 期刊： ICLR
- 代码开放情况：部分开放
- 阅读优先级： P0

### [[02_论文/03_双臂协作/RDT-1B - a Diffusion Foundation Model for Bimanual Manipulation|RDT-1B：面向双臂操作的扩散基础模型]]

- 年份： 2025
- 会议 / 期刊： ICLR
- 代码开放情况：已开放
- 阅读优先级： P0

### [[02_论文/07_泛化与长程任务/HAMSTER - Hierarchical Action Models for Open-World Robot Manipulation|HAMSTER：面向开放世界机器人操作的分层动作模型]]

- 年份： 2025
- 会议 / 期刊： ICLR
- 阅读优先级： P0

### [[02_论文/09_综述/What Foundation Models can Bring for Robot Learning in Manipulation - A Survey|基础模型为机器人操作学习带来了什么：综述]]

- 年份： 2024
- 会议 / 期刊： Survey / arXiv
- 阅读优先级： P0

### [[02_论文/01_VLA/OpenVLA - An Open-Source Vision-Language-Action Model|OpenVLA：开源视觉—语言—动作模型]]

- 年份： 2024
- 会议 / 期刊： CoRL
- 代码开放情况：已开放
- 阅读优先级： P0

### [[02_论文/10_基准测试与数据集/Open X-Embodiment - Robotic Learning Datasets and RT-X Models|Open X-Embodiment：机器人学习数据集与 RT-X 模型]]

- 年份： 2024
- 会议 / 期刊： ICRA
- 代码开放情况：已开放
- 阅读优先级： P0

### [[02_论文/01_VLA/Octo - An Open-Source Generalist Robot Policy|Octo：开源通用机器人策略]]

- 年份： 2024
- 会议 / 期刊： RSS
- 代码开放情况：已开放
- 阅读优先级： P0

### [[02_论文/09_综述/A Survey on Vision-Language-Action Models for Embodied AI|面向具身 AI 的 VLA 模型综述]]

- 年份： 2024
- 会议 / 期刊： Survey / arXiv
- 阅读优先级： P0

### [[02_论文/09_综述/A Survey on Robotics with Foundation Models - Toward Embodied AI|基础模型赋能机器人：迈向具身 AI 的综述]]

- 年份： 2024
- 会议 / 期刊： Survey / arXiv
- 阅读优先级： P0


## CCF A 论文

### [[02_论文/01_VLA/ReconVLA - Reconstructive Vision-Language-Action Model as Effective Robot Perceiver|ReconVLA：以重建增强机器人感知的 VLA 模型]]

- 年份： 2026
- 会议 / 期刊： AAAI
- 代码开放情况：已开放
- 阅读优先级： P1

### [[02_论文/04_灵巧操作/UniDex - A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos|UniDex：从第一人称人类视频学习通用灵巧手控制]]

- 年份： 2026
- 会议 / 期刊： CVPR
### [[02_论文/01_VLA/SimpleVLA-RL - Scaling VLA Training via Reinforcement Learning|SimpleVLA-RL：通过强化学习扩展 VLA 训练]]

- 年份： 2026
- 会议 / 期刊： ICLR
- 阅读优先级： P1

### [[02_论文/01_VLA/SP-VLA - A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration|SP-VLA：通过联合模型调度与 Token 剪枝加速 VLA]]

- 年份： 2026
- 会议 / 期刊： ICLR
- 阅读优先级： P1

### [[02_论文/01_VLA/Actions as Language - Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting|将动作视为语言：在避免灾难性遗忘的条件下将 VLM 微调为 VLA]]

- 年份： 2026
- 会议 / 期刊： ICLR
- 阅读优先级： P1

### [[02_论文/01_VLA/VideoVLA - Video Generators Can Be Generalizable Robot Manipulators|VideoVLA：让视频生成模型成为可泛化的机器人操作策略]]

- 年份： 2025
- 会议 / 期刊： NeurIPS
- 代码开放情况：部分开放
### [[02_论文/01_VLA/VLA-Cache - Efficient Vision-Language-Action Manipulation via Adaptive Token Caching|VLA-Cache：利用自适应 Token 缓存提高 VLA 操作效率]]

- 年份：2025
- 发表 venue：NeurIPS
- 代码状态：部分开放
- 正文证据：A
- 优先级：P1

### [[02_论文/01_VLA/TraceVLA - Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies|TraceVLA：以视觉轨迹提示增强通用机器人策略的时空感知]]

- 年份： 2025
- 会议 / 期刊： ICLR
- 代码开放情况：部分开放
- 阅读优先级： P1

### [[02_论文/07_泛化与长程任务/OWMM-Agent - Open World Mobile Manipulation With Multi-modal Agentic Data Synthesis|OWMM-Agent：通过多模态智能体数据合成实现开放世界移动操作]]

- 年份： 2025
- 会议 / 期刊： NeurIPS
### [[02_论文/01_VLA/MoManipVLA - Transferring Vision-language-action Models for General Mobile Manipulation|MoManipVLA：迁移 VLA 模型以实现通用移动操作]]

- 年份： 2025
- 会议 / 期刊： CVPR
### [[02_论文/08_数据与遥操作/Latent Action Pretraining from Videos|从视频进行潜在动作预训练]]

- 年份： 2025
- 会议 / 期刊： ICLR
- 代码开放情况：已开放
- 阅读优先级： P1

### [[02_论文/01_VLA/DiffusionVLA - Scaling Robot Foundation Models via Unified Diffusion and Autoregression|DiffusionVLA：通过统一扩散与自回归扩展机器人基础模型]]

- 年份： 2025
- 会议 / 期刊： ICML
- 代码开放情况：部分开放
### [[02_论文/04_灵巧操作/DexVLG - Dexterous Vision-Language-Grasp Model at Scale|DexVLG：规模化灵巧视觉—语言—抓取模型]]

- 年份： 2025
- 会议 / 期刊： ICCV
- 代码开放情况： Coming Soon
### [[02_论文/01_VLA/CoT-VLA - Visual Chain-of-Thought Reasoning for Vision-Language-Action Models|CoT-VLA：面向 VLA 的视觉思维链推理]]

- 年份： 2025
- 会议 / 期刊： CVPR
### [[02_论文/01_VLA/BridgeVLA - Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models|BridgeVLA：通过输入—输出对齐高效学习三维操作]]

- 年份： 2025
- 会议 / 期刊： NeurIPS
- 代码开放情况：已开放
### [[02_论文/02_机器人操作/VidMan - Exploiting Implicit Dynamics from Video Diffusion Model for Effective Robot Manipulation|VidMan：利用视频扩散模型的隐式动力学改进机器人操作]]

- 年份： 2024
- 会议 / 期刊： NeurIPS
- 代码开放情况： Coming Soon
### [[02_论文/01_VLA/RoboMamba - Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation|RoboMamba：用于机器人推理与操作的高效 VLA 模型]]

- 年份： 2024
- 会议 / 期刊： NeurIPS
- 代码开放情况：部分开放
### [[02_论文/01_VLA/3D-VLA - A 3D Vision-Language-Action Generative World Model|3D-VLA：基于三维视觉—语言—动作的生成式世界模型]]

- 年份： 2024
- 会议 / 期刊： ICML
- 代码开放情况：部分开放
## 机器人核心论文

本组暂无条目。

## 发现池与参考论文

### 2026-10-01 arXiv 速读收录

- [[02_论文/01_VLA/When Instructions Retrieve Trajectories - Diagnosing and Mitigating Generalization Failures in VLA Models|指令检索轨迹]] — A；反事实训练与语言—视觉动作绑定；LIBERO-PRO、UR5e。
- [[02_论文/01_VLA/Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action Models|FailBank]] — A；旁路安全反馈进入失败库并更新策略；VLA-Arena；代码已开放。
- [[02_论文/01_VLA/Dream4ACT - A Shared Visual Action Interface for Multi-Embodiment Video-Action Modeling|Dream4ACT]] — B；URDF action views 统一视频与动作；RoboTwin 2.0、TriWorldBench；代码待核。
- [[02_论文/08_数据与遥操作/Ego4WAM - What Matters When Scaling Egocentric Human Data for Robot Learning|Ego4WAM]] — A；第一视角数据监督与对齐的受控比较；RoboDojo、真机。

### [[02_论文/01_VLA/DIAL - Decoupling Intent and Action via Latent World Modeling for End-to-End VLA|DIAL：通过潜在世界建模解耦意图与动作]]

- 年份：2026
- 发表 venue：arXiv 预印本
- 方法定位：潜在世界建模 → 意图瓶颈 → flow-matching 动作；RoboCasa 与人形真机验证
- 阅读优先级：A（精读）；官方代码与权重已公开

### [[02_论文/01_VLA/ACE-Ego-0 - Unifying Egocentric Human and Robotic Data for VLA Pretraining|ACE-Ego-0：统一第一视角人类与机器人数据用于VLA预训练]]

- 年份：2026
- 发表 venue：arXiv 预印本
- 研究定位：第一视角人类视频与机器人数据的跨执行体 VLA 预训练
- 代码状态：部分开放
- 全文证据：PDF 已核验；RoboCasa、RoboTwin 2.0、ARX 真机

### [[02_论文/01_VLA/SpatialVLA - Exploring Spatial Representations for Visual-Language-Action Models|SpatialVLA：探索 VLA 模型的空间表征]]

- 年份： 2025
- 会议 / 期刊： RSS
- 代码开放情况：已开放
- 阅读优先级： P1

### [[02_论文/01_VLA/RoboMonkey - Scaling Test-Time Sampling and Verification for Vision-Language-Action Models|RoboMonkey：扩展 VLA 的测试时采样与验证]]

- 年份： 2025
- 会议 / 期刊： CoRL
- 阅读优先级： P1

### [[02_论文/09_综述/A Survey on Vision-Language-Action Models - An Action Tokenization Perspective|从动作 Token 化视角综述 VLA 模型]]

- 年份： 2025
- 会议 / 期刊： Survey / arXiv
- 阅读优先级： P1

### [[02_论文/02_机器人操作/Dreamitate - Real-World Visuomotor Policy Learning via Video Generation|Dreamitate：通过视频生成学习真实世界视觉运动策略]]

- 年份： 2024
- 会议 / 期刊： CoRL
- 阅读优先级： P1

### [[02_论文/01_VLA/Do As I Can, Not As I Say - Grounding Language in Robotic Affordances|SayCan：以机器人能力约束语言指令的落地执行]]

- 年份： 2022
- 会议 / 期刊： CoRL
- 代码开放情况：部分开放 (official tabletop simulation released)
- 阅读优先级： P0
- Special Attention: Yes
- Primary Category: VLA
- 标签： Language Grounding; Affordance; Long-horizon; Planning; Robot Manipulation
