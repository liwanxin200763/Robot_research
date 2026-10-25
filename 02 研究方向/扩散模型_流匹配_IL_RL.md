# 扩散模型 / 流匹配 / IL / RL
本页依据论文主卡的分类、子类、标签、关键词和机器人形态等字段生成。论文实体按主分类保留在 `03 论文卡片` 中。

## 学习范式、运动先验与可复用技能

模仿学习（IL）从示范学习行为，行为克隆（BC）直接拟合观察到动作，强化学习（RL）通过交互回报改进策略。扩散模型用逐步去噪生成动作或运动，流匹配学习连续变换的向量场；它们可以作为策略结构或先验，不等同于一种数据来源，也不代表全部方法都用相同目标训练

| 论文 | 核心问题与方法 | 主要证据对象 | 与BeyondMimic的证据关系 |
| --- | --- | --- | --- |
| [P212 DeepMimic](../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/06_%E6%89%A9%E6%95%A3%E6%A8%A1%E5%9E%8B_%E6%B5%81%E5%8C%B9%E9%85%8D_IL_RL/DeepMimic%20-%20Example-Guided%20Deep%20Reinforcement%20Learning%20of%20Physics-Based%20Character%20Skills.md) | 参考相位与模仿奖励，把示范转成能受扰动的物理技能 | 仿真角色 | v4直接引用#32 |
| [P213 AMP](../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/06_%E6%89%A9%E6%95%A3%E6%A8%A1%E5%9E%8B_%E6%B5%81%E5%8C%B9%E9%85%8D_IL_RL/AMP%20-%20Adversarial%20Motion%20Priors%20for%20Stylized%20Physics-Based%20Character%20Control.md) | 判别器学习运动风格，减轻逐帧同步和片段编排 | 仿真角色 | v4直接引用#36 |
| [P214 ASE](../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/06_%E6%89%A9%E6%95%A3%E6%A8%A1%E5%9E%8B_%E6%B5%81%E5%8C%B9%E9%85%8D_IL_RL/ASE%20-%20Large-Scale%20Reusable%20Adversarial%20Skill%20Embeddings%20for%20Physically%20Simulated%20Characters.md) | 学习潜在技能供新任务的高层调用，强调技能复用 | 仿真角色 | 本库补充比较，未核实v4直接引用 |
| [P215 MaskedMimic](../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/06_%E6%89%A9%E6%95%A3%E6%A8%A1%E5%9E%8B_%E6%B5%81%E5%8C%B9%E9%85%8D_IL_RL/MaskedMimic%20-%20Unified%20Physics-Based%20Character%20Control%20Through%20Masked%20Motion%20Inpainting.md) | 将部分关节、时间、文字等条件补成完整运动；条件VAE＋蒸馏 | 仿真角色 | 本库补充比较；ASAP正文实际使用其运动清洗，未核实BeyondMimic直接引用 |
| [P216 ASAP](../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/05_%E4%BB%BF%E7%9C%9F%E5%88%B0%E7%9C%9F%E5%AE%9E_Sim2Real/ASAP%20-%20Aligning%20Simulation%20and%20Real-World%20Physics%20for%20Learning%20Agile%20Humanoid%20Whole-Body%20Skills.md) | 从真实轨迹学残差动作，让训练仿真更像现实，再微调策略 | 跨仿真器和G1真机 | v4直接引用#33，含增益设计对照 |
| [P217 Diffuse-CLoC](../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/06_%E6%89%A9%E6%95%A3%E6%A8%A1%E5%9E%8B_%E6%B5%81%E5%8C%B9%E9%85%8D_IL_RL/Diffuse-CLoC%20-%20Guided%20Diffusion%20for%20Physics-based%20Character%20Look-ahead%20Control.md) | 联合预测运动和动作，用代价梯度引导前瞻控制 | 仿真角色 | v4直接引用#45 |
| [P210 BeyondMimic](../03%20%E8%AE%BA%E6%96%87%E5%8D%A1%E7%89%87/06_%E6%89%A9%E6%95%A3%E6%A8%A1%E5%9E%8B_%E6%B5%81%E5%8C%B9%E9%85%8D_IL_RL/BeyondMimic%20-%20From%20Motion%20Tracking%20to%20Versatile%20Humanoid%20Control%20via%20Guided%20Diffusion.md) | 统一跟踪配方＋潜在状态动作扩散＋运行时引导 | G1真机、仿真消融 | 本专题核心 |

知识组织可以写成：DeepMimic → AMP／ASE／MaskedMimic → 可复用技能与新目标控制 → BeyondMimic；ASAP补充动力学校正，Diffuse-CLoC补充引导生成。箭头表示阅读问题递进，**不是每一篇都直接继承或引用前一篇**

阅读顺序建议：先DeepMimic理解状态、动作、奖励，再读BeyondMimic的统一配方与生成控制；若关注少量真机数据校正，读ASAP；若关注任务目标接口与多解，比较AMP、ASE、MaskedMimic、Diffuse-CLoC

### 比较时保留哪些量

将参考跟踪误差、风格分数、归一化回报、整任务成功率和生成吞吐分别报告。训练时困难片段重采样与不稳定轨迹筛除属于数据/优化策略，部署时发现抓空并重新行动属于执行系统。MaskedMimic采用条件VAE，不能因为放在本类就改称扩散方法

对现有机械臂与DH116，先固定动作语义、相机观察和训练预算，再比较动作块结构或生成头；全身G1的运动技能不能直接作为多指抓取控制器。完整路线与引用关系见 [[01 论文文库/专题阅读/全身运动技能与具身执行框架|全身运动技能与具身执行框架]]

## 优先阅读与特别关注

### [[03 论文卡片/01_VLA/ReconVLA - Reconstructive Vision-Language-Action Model as Effective Robot Perceiver|ReconVLA：以重建增强机器人感知的 VLA 模型]]

- 年份： 2026
- 会议 / 期刊： AAAI
- 代码状态：已发布
- 优先级： P1

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/Demystifying Robot Diffusion Policies - Action Memorization and a Simple Lookup Table Alternative|揭示机器人扩散策略：动作记忆与简单查找表替代方案]]

- 年份： 2026
- 会议 / 期刊： ICLR
- 代码状态：未知
- 优先级： P0

### [[03 论文卡片/03_双臂协作/You Only Teach Once - Learn One-Shot Bimanual Robotic Manipulation from Video Demonstrations|YOTO：从视频示范一次性学习双臂机器人操作]]

- 年份： 2025
- 会议 / 期刊： RSS
- 代码状态：未知
- 优先级： P0

### [[03 论文卡片/09_综述/Towards a Unified Understanding of Robot Manipulation - A Comprehensive Survey|迈向统一理解机器人操作：综合综述]]

- 年份： 2025
- 会议 / 期刊： Survey / arXiv
- 代码状态：未知
- 优先级： P0

### [[03 论文卡片/03_双臂协作/RDT-1B - a Diffusion Foundation Model for Bimanual Manipulation|RDT-1B：面向双臂操作的扩散基础模型]]

- 年份： 2025
- 会议 / 期刊： ICLR
- 代码状态：已发布
- 优先级： P0

### [[03 论文卡片/07_泛化与长程任务/HAMSTER - Hierarchical Action Models for Open-World Robot Manipulation|HAMSTER：面向开放世界机器人操作的分层动作模型]]

- 年份： 2025
- 会议 / 期刊： ICLR
- 代码状态：未知
- 优先级： P0

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/Bidirectional Decoding - Improving Action Chunking via Guided Test-Time Sampling|双向解码：通过引导式测试时采样改进动作分块]]

- 年份： 2025
- 会议 / 期刊： ICLR
- 代码状态：已发布
- 优先级： P0

### [[03 论文卡片/09_综述/What Foundation Models can Bring for Robot Learning in Manipulation - A Survey|基础模型为机器人操作学习带来了什么：综述]]

- 年份： 2024
- 会议 / 期刊： Survey / arXiv
- 代码状态：未知
- 优先级： P0

### [[03 论文卡片/10_基准测试与数据集/RoboCasa - Large-Scale Simulation of Household Tasks for Generalist Robots|RoboCasa：面向通用机器人的大规模家务任务仿真]]

- 年份： 2024
- 会议 / 期刊： RSS
- 代码状态：未知
- 优先级： P0

### [[03 论文卡片/01_VLA/OpenVLA - An Open-Source Vision-Language-Action Model|OpenVLA：开源视觉—语言—动作模型]]

- 年份： 2024
- 会议 / 期刊： CoRL
- 代码状态：已发布
- 优先级： P0

### [[03 论文卡片/01_VLA/Octo - An Open-Source Generalist Robot Policy|Octo：开源通用机器人策略]]

- 年份： 2024
- 会议 / 期刊： RSS
- 代码状态：已发布
- 优先级： P0

### [[03 论文卡片/08_数据与遥操作/OPEN TEACH - A Versatile Teleoperation System for Robotic Manipulation|OPEN TEACH：面向机器人操作的通用遥操作系统]]

- 年份： 2024
- 会议 / 期刊： CoRL
- 代码状态：未知
- 优先级： P0

### [[03 论文卡片/03_双臂协作/Mobile ALOHA - Learning Bimanual Mobile Manipulation Using Low-Cost Whole-Body Teleoperation|Mobile ALOHA：通过低成本全身遥操作学习双臂移动操作]]

- 年份： 2024
- 会议 / 期刊： CoRL
- 代码状态：未知
- 优先级： P0

### [[03 论文卡片/09_综述/Learning by Watching - A Review of Video-Based Learning Approaches for Robot Manipulation|观察学习：基于视频的机器人操作学习方法综述]]

- 年份： 2024
- 会议 / 期刊： Survey / arXiv
- 代码状态：未知
- 优先级： P0

### [[03 论文卡片/10_基准测试与数据集/DROID - A Large-Scale In-The-Wild Robot Manipulation Dataset|DROID：大规模自然场景机器人操作数据集]]

- 年份： 2024
- 会议 / 期刊： RSS
- 代码状态：已发布
- 优先级： P0

### [[03 论文卡片/03_双臂协作/ALOHA Unleashed - A Simple Recipe for Robot Dexterity|ALOHA Unleashed：实现机器人灵巧操作的简明方法]]

- 年份： 2024
- 会议 / 期刊： CoRL
- 代码状态：未知
- 优先级： P0

### [[03 论文卡片/09_综述/A Survey on Robotics with Foundation Models - Toward Embodied AI|基础模型赋能机器人：迈向具身 AI 的综述]]

- 年份： 2024
- 会议 / 期刊： Survey / arXiv
- 代码状态：未知
- 优先级： P0


## CCF A 论文

### [[03 论文卡片/01_VLA/ReconVLA - Reconstructive Vision-Language-Action Model as Effective Robot Perceiver|ReconVLA：以重建增强机器人感知的 VLA 模型]]

- 年份： 2026
- 会议 / 期刊： AAAI
- 代码状态：已发布
- 优先级： P1

### [[03 论文卡片/01_VLA/SimpleVLA-RL - Scaling VLA Training via Reinforcement Learning|SimpleVLA-RL：通过强化学习扩展 VLA 训练]]

- 年份： 2026
- 会议 / 期刊： ICLR
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/Real-Time Robot Execution with Masked Action Chunking|通过掩码动作分块实现机器人实时执行]]

- 年份： 2026
- 会议 / 期刊： ICLR
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/07_泛化与长程任务/RGMP - Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation|RGMP：融合循环几何先验的多模态策略，用于可泛化人形机器人操作]]

- 年份： 2026
- 会议 / 期刊： AAAI
- 代码状态：未知
- 优先级：未知

### [[03 论文卡片/03_双臂协作/Learning Diverse Bimanual Dexterous Manipulation Skills from Human Demonstrations|从人类示范学习多样化双臂灵巧操作技能]]

- 年份： 2026
- 会议 / 期刊： AAAI
- 代码状态：未知
- 优先级：未知

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/Learning Diffusion Policy from Primitive Skills for Robot Manipulation|从基础技能学习机器人操作扩散策略]]

- 年份： 2026
- 会议 / 期刊： AAAI
- 代码状态：未知
- 优先级：未知

### [[03 论文卡片/07_泛化与长程任务/Gentle Manipulation Policy Learning via Demonstrations from VLM Planned Atomic Skills|从 VLM 规划的原子技能示范学习轻柔操作策略]]

- 年份： 2026
- 会议 / 期刊： AAAI
- 代码状态：未知
- 优先级：未知

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/FoAM - Foresight-Augmented Multi-Task Imitation Policy for Robotic Manipulation|FoAM：面向机器人操作的前瞻增强多任务模仿策略]]

- 年份： 2026
- 会议 / 期刊： AAAI
- 代码状态：未知
- 优先级：未知

### [[03 论文卡片/04_灵巧操作/Dexterous Manipulation Transfer via Progressive Kinematic-Dynamic Alignment|通过渐进式运动学—动力学对齐迁移灵巧操作]]

- 年份： 2026
- 会议 / 期刊： AAAI
- 代码状态：未知
- 优先级：未知

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/Action Chunking and Data Augmentation Yield Exponential Improvements in Behavior Cloning for Continuous Spaces|动作分块与数据增强显著提升连续空间的行为克隆]]

- 年份： 2026
- 会议 / 期刊： ICLR
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/10_基准测试与数据集/VTDexManip - A Dataset and Benchmark for Visual-tactile Pretraining and Dexterous Manipulation with Reinforcement Learning|VTDexManip：用于视觉触觉预训练与强化学习灵巧操作的数据集和 Benchmark]]

- 年份： 2025
- 会议 / 期刊： ICLR
- 代码状态：未知
- 优先级： P2

### [[03 论文卡片/04_灵巧操作/UniGraspTransformer - Simplified Policy Distillation for Scalable Dexterous Robotic Grasping|UniGraspTransformer：通过简化策略蒸馏实现可扩展灵巧抓取]]

- 年份： 2025
- 会议 / 期刊： CVPR
- 代码状态：已发布
- 优先级：未知

### [[03 论文卡片/03_双臂协作/Rethinking Bimanual Robotic Manipulation - Learning with Decoupled Interaction Framework|重新思考双臂操作：通过解耦交互框架学习]]

- 年份： 2025
- 会议 / 期刊： ICCV
- 代码状态：未知
- 优先级：未知

### [[03 论文卡片/07_泛化与长程任务/Policy Decorator - Model-Agnostic Online Refinement for Large Policy Models|Policy Decorator：对大型策略模型进行模型无关的在线优化]]

- 年份： 2025
- 会议 / 期刊： ICLR
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/PointMapPolicy - Structured Point Cloud Processing for Multi-Modal Imitation Learning|PointMapPolicy：通过结构化点云处理实现多模态模仿学习]]

- 年份： 2025
- 会议 / 期刊： NeurIPS
- 代码状态：未知
- 优先级：未知

### [[03 论文卡片/04_灵巧操作/LatentHOI - On the Generalizable Hand Object Motion Generation with Latent Hand Diffusion|LatentHOI：利用潜空间手部扩散生成可泛化的人手—物体运动]]

- 年份： 2025
- 会议 / 期刊： CVPR
- 代码状态：未知
- 优先级：未知

### [[03 论文卡片/05_仿真到真实_Sim2Real/Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training|面向仿真与真实策略联合训练的可泛化域适应]]

- 年份： 2025
- 会议 / 期刊： NeurIPS
- 代码状态：未知
- 优先级：未知

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/FreqPolicy - Efficient Flow-based Visuomotor Policy via Frequency Consistency|FreqPolicy：通过频率一致性实现高效 Flow 视觉运动策略]]

- 年份： 2025
- 会议 / 期刊： NeurIPS
- 代码状态：未知
- 优先级：未知

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/FlowPolicy - Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation|FlowPolicy：通过一致性 Flow Matching 实现快速稳健的三维操作策略]]

- 年份： 2025
- 会议 / 期刊： AAAI
- 代码状态：已发布
- 优先级：未知

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/ET-SEED - Efficient Trajectory-Level SE(3) Equivariant Diffusion Policy|ET-SEED：高效轨迹级 SE(3) 等变扩散策略]]

- 年份： 2025
- 会议 / 期刊： ICLR
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/Dynamic Test-Time Compute Scaling in Control Policy - Difficulty-Aware Stochastic Interpolant Policy|控制策略的动态测试时计算扩展：难度感知随机插值策略]]

- 年份： 2025
- 会议 / 期刊： NeurIPS
- 代码状态：未知
- 优先级：未知

### [[03 论文卡片/01_VLA/DiffusionVLA - Scaling Robot Foundation Models via Unified Diffusion and Autoregression|DiffusionVLA：通过统一扩散与自回归扩展机器人基础模型]]

- 年份： 2025
- 会议 / 期刊： ICML
- 代码状态：部分发布
- 优先级：未知

### [[03 论文卡片/03_双臂协作/Diffusion-Based Imaginative Coordination for Bimanual Manipulation|基于扩散式想象的双臂协同操作]]

- 年份： 2025
- 会议 / 期刊： ICCV
- 代码状态：未知
- 优先级：未知

### [[03 论文卡片/04_灵巧操作/DexVLG - Dexterous Vision-Language-Grasp Model at Scale|DexVLG：规模化灵巧视觉—语言—抓取模型]]

- 年份： 2025
- 会议 / 期刊： ICCV
- 代码状态： Coming Soon
- 优先级：未知

### [[03 论文卡片/04_灵巧操作/DexHandDiff - Interaction-aware Diffusion Planning for Adaptive Dexterous Manipulation|DexHandDiff：面向自适应灵巧操作的交互感知扩散规划]]

- 年份： 2025
- 会议 / 期刊： CVPR
- 代码状态：部分发布
- 优先级：未知

### [[03 论文卡片/04_灵巧操作/Cross-Embodiment Dexterous Grasping with Reinforcement Learning|通过强化学习实现跨本体灵巧抓取]]

- 年份： 2025
- 会议 / 期刊： ICLR
- 代码状态：未知
- 优先级： P2

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/AutoCGP - Closed-Loop Concept-Guided Policies from Unlabeled Demonstrations|AutoCGP：从未标注示范学习闭环概念引导策略]]

- 年份： 2025
- 会议 / 期刊： ICLR
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/03_双臂协作/AnyBimanual - Transferring Unimanual Policy for General Bimanual Manipulation|AnyBimanual：迁移单臂策略以实现通用双臂操作]]

- 年份： 2025
- 会议 / 期刊： ICCV
- 代码状态：未知
- 优先级：未知

### [[03 论文卡片/10_基准测试与数据集/AdaManip - Adaptive Articulated Object Manipulation Environments and Policy Learning|AdaManip：自适应关节式物体操作环境与策略学习]]

- 年份： 2025
- 会议 / 期刊： ICLR
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/AR-VRM - Imitating Human Motions for Visual Robot Manipulation with Analogical Reasoning|AR-VRM：通过类比推理模仿人类动作以实现视觉机器人操作]]

- 年份： 2025
- 会议 / 期刊： ICCV
- 代码状态：已发布
- 优先级：未知

### [[03 论文卡片/02_机器人操作/VidMan - Exploiting Implicit Dynamics from Video Diffusion Model for Effective Robot Manipulation|VidMan：利用视频扩散模型的隐式动力学改进机器人操作]]

- 年份： 2024
- 会议 / 期刊： NeurIPS
- 代码状态： Coming Soon
- 优先级：未知

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/Text-Aware Diffusion for Policy Learning|面向策略学习的文本感知扩散]]

- 年份： 2024
- 会议 / 期刊： NeurIPS
- 代码状态：未知
- 优先级：未知

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/Robot Policy Learning with Temporal Optimal Transport Reward|利用时间最优传输奖励学习机器人策略]]

- 年份： 2024
- 会议 / 期刊： NeurIPS
- 代码状态：已发布
- 优先级：未知

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/Hierarchical Diffusion Policy for Kinematics-Aware Multi-Task Robotic Manipulation|面向运动学感知多任务操作的分层扩散策略]]

- 年份： 2024
- 会议 / 期刊： CVPR
- 代码状态：未知
- 优先级：未知

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/BAKU - An Efficient Transformer for Multi-Task Policy Learning|BAKU：面向多任务策略学习的高效 Transformer]]

- 年份： 2024
- 会议 / 期刊： NeurIPS
- 代码状态：未知
- 优先级：未知

### [[03 论文卡片/01_VLA/3D-VLA - A 3D Vision-Language-Action Generative World Model|3D-VLA：基于三维视觉—语言—动作的生成式世界模型]]

- 年份： 2024
- 会议 / 期刊： ICML
- 代码状态：部分发布
- 优先级：未知


## 机器人核心论文

### [[03 论文卡片/04_灵巧操作/Evaluating the Effect of State and Action Selection on In-Hand Manipulation Performance for Transferability|评估状态与动作选择对手内操作迁移性能的影响]]

- 年份： 2025
- 会议 / 期刊： RA-L
- 代码状态：未知
- 优先级： P2

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/Multimodal and Force-Matched Imitation Learning With a See-Through Visuotactile Sensor|利用透视式视觉触觉传感器进行多模态力匹配模仿学习]]

- 年份： 2024
- 会议 / 期刊： T-RO
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/08_数据与遥操作/DexCap - Scalable and Portable Mocap Data Collection System for Dexterous Manipulation|DexCap：面向灵巧操作的可扩展便携式动作捕捉数据采集系统]]

- 年份： 2024
- 会议 / 期刊： RSS
- 代码状态：未知
- 优先级： P1


## 发现池与参考论文

### [[03 论文卡片/09_综述/A Survey of Robot Learning for Bimanual Manipulation|双臂操作机器人学习综述]]

- 年份： 2026
- 会议 / 期刊： Survey / community
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/05_仿真到真实_Sim2Real/Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids|面向人形机器人的视觉灵巧操作 Sim2Real 强化学习]]

- 年份： 2025
- 会议 / 期刊： CoRL
- 代码状态：未知
- 优先级： P2

### [[03 论文卡片/03_双臂协作/SafeBimanual - Diffusion-based trajectory optimization for safe bimanual manipulation|SafeBimanual：通过扩散式轨迹优化实现安全双臂操作]]

- 年份： 2025
- 会议 / 期刊： CoRL
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/MimicFunc - Imitating Tool Manipulation from a Single Human Video via Functional Correspondence|MimicFunc：利用功能对应关系从单段人类视频模仿工具操作]]

- 年份： 2025
- 会议 / 期刊： CoRL
- 代码状态：未知
- 优先级： P2

### [[03 论文卡片/09_综述/Interactive Imitation Learning for Dexterous Robotic Manipulation - Challenges and Perspectives—a Survey|灵巧机器人操作的交互式模仿学习：挑战与展望综述]]

- 年份： 2025
- 会议 / 期刊： Survey / journal
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/09_综述/A Survey of Embodied Learning for Object-Centric Robotic Manipulation|面向物体中心机器人操作的具身学习综述]]

- 年份： 2025
- 会议 / 期刊： Survey / journal
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/03_双臂协作/VoxAct-B - Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation|VoxAct-B：用于双臂操作的体素式动作与稳定策略]]

- 年份： 2024
- 会议 / 期刊： CoRL
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/07_泛化与长程任务/SPIRE - Synergistic Planning, Imitation, and Reinforcement Learning for Long-Horizon Manipulation|SPIRE：结合规划、模仿与强化学习的长程操作]]

- 年份： 2024
- 会议 / 期刊： CoRL
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/07_泛化与长程任务/RAM - Retrieval-Based Affordance Transfer for Generalizable Zero-Shot Robotic Manipulation|RAM：通过检索式可供性迁移实现可泛化零样本操作]]

- 年份： 2024
- 会议 / 期刊： CoRL
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/08_数据与遥操作/ManiWAV - Learning Robot Manipulation from In-the-Wild Audio-Visual Data|ManiWAV：从自然场景视听数据学习机器人操作]]

- 年份： 2024
- 会议 / 期刊： CoRL
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/MILES - Making Imitation Learning Easy with Self-Supervision|MILES：通过自监督简化模仿学习]]

- 年份： 2024
- 会议 / 期刊： CoRL
- 代码状态：未知
- 优先级： P2

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching|通过条件 Flow Matching 从点云学习机器人操作策略]]

- 年份： 2024
- 会议 / 期刊： CoRL
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/Equivariant Diffusion Policy|等变扩散策略]]

- 年份： 2024
- 会议 / 期刊： CoRL
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/EquiBot - SIM(3)-Equivariant Diffusion Policy for Generalizable and Data Efficient Learning|EquiBot：兼具泛化性与数据效率的 SIM(3) 等变扩散策略]]

- 年份： 2024
- 会议 / 期刊： CoRL
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/02_机器人操作/Dreamitate - Real-World Visuomotor Policy Learning via Video Generation|Dreamitate：通过视频生成学习真实世界视觉运动策略]]

- 年份： 2024
- 会议 / 期刊： CoRL
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/10_基准测试与数据集/BiGym - A Demo-Driven Mobile Bi-Manual Manipulation Benchmark|BiGym：由示范驱动的移动双臂操作 Benchmark]]

- 年份： 2024
- 会议 / 期刊： CoRL
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/09_综述/A Survey of Demonstration Learning|示范学习综述]]

- 年份： 2024
- 会议 / 期刊： Survey / journal
- 代码状态：未知
- 优先级： P1

### [[03 论文卡片/06_扩散模型_流匹配_IL_RL/3D Diffuser Actor - Policy Diffusion with 3D Scene Representations|3D Diffuser Actor：基于三维场景表征的策略扩散]]

- 年份： 2024
- 会议 / 期刊： CoRL
- 代码状态：未知
- 优先级： P1


## 全身技能与具身执行关联阅读

人形运动跟踪、风格先验、潜在技能、部分约束补全与引导控制；其中MaskedMimic采用条件VAE，不因分类名称而改称扩散方法

- [[03 论文卡片/06_扩散模型_流匹配_IL_RL/BeyondMimic - From Motion Tracking to Versatile Humanoid Control via Guided Diffusion|P210 · BeyondMimic]]: 全身人形统一跟踪配方、潜在扩散与测试时引导；Science Robotics 2026-08-26；本地为已标明的 arXiv v4，不冒充出版定稿
- [[03 论文卡片/06_扩散模型_流匹配_IL_RL/DeepMimic - Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills|P212 · DeepMimic]]: 示范相位、模仿奖励与强化学习；物理仿真角色，不是真机灵巧手
- [[03 论文卡片/06_扩散模型_流匹配_IL_RL/AMP - Adversarial Motion Priors for Stylized Physics-Based Character Control|P213 · AMP]]: 判别器学习运动风格与组合；免同步不等于单片段精度总更好
- [[03 论文卡片/06_扩散模型_流匹配_IL_RL/ASE - Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters|P214 · ASE]]: 可复用对抗技能嵌入与高层调用；归一化回报不是成功率
- [[03 论文卡片/06_扩散模型_流匹配_IL_RL/MaskedMimic - Unified Physics-Based Character Control Through Masked Motion Inpainting|P215 · MaskedMimic]]: 结构化掩码与条件VAE运动补全；多控制条件不等于扩散模型
- [[03 论文卡片/06_扩散模型_流匹配_IL_RL/Diffuse-CLoC - Guided Diffusion for Physics-based Character Look-ahead Control|P217 · Diffuse-CLoC]]: 联合状态动作预测与代价梯度引导；仿真角色前瞻控制，未核实全流程官方代码

[[01 论文文库/专题阅读/全身运动技能与具身执行框架|统一专题]] · [[04 项目与实验/SenseNova-RoboRSI 项目资料与开放边界|RoboRSI项目开放边界]]
