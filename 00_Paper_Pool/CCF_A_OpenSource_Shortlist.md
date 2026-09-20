# CCF A + Open Source Literature Shortlist

本页仅包含 CCF A 正式论文中，官方方法代码已核验为 Released 或有意义 Partial 的条目。

## 1. VLA / Robot Foundation Models

### [[02_Papers/01_VLA/ReconVLA|ReconVLA]]

- Title: ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver
- Year: 2026
- Venue: AAAI
- CCF: A
- Type: Method Paper
- Category: VLA; Robot Manipulation; Generalization; Diffusion
- Code Status: Released
- Official GitHub: https://github.com/OpenHelix-Team/ReconVLA
- Project Page: https://zionchow.github.io/ReconVLA/
- Checkpoint: Unknown — 本轮未发现作者公开的 ReconVLA checkpoint 入口
- Dataset: 仓库提供 BridgeData V2、LIBERO、CALVIN 的下载与预处理说明；不附带原始数据，完整汇编数据集入口未核实
- Embodiment: Single Arm / Parallel Gripper
- Robot Platform: Franka Panda (CALVIN simulation); real-world platform not confirmed at abstract level
- Real Robot: Yes
- Verification Status: Official AAAI proceedings and official repository verified; CCF A verified on current official CCF list

### [[02_Papers/01_VLA/BridgeVLA|BridgeVLA]]

- Title: BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models
- Year: 2025
- Venue: NeurIPS
- CCF: A
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Code Status: Released
- Official GitHub: https://github.com/BridgeVLA/BridgeVLA/tree/bridgevla
- Project Page: https://bridgevla.github.io/
- Checkpoint: https://huggingface.co/datasets/LPY/BridgeVLA/tree/main/checkpoints/bridgevla（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: README提供预训练数据及RLBench/COLOSSEUM/GemBench说明；入口存在，未下载
- Embodiment: Single Arm / Parallel Gripper
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/01_VLA/VLA-Cache|VLA-Cache]]

- Title: VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching
- Year: 2025
- Venue: NeurIPS
- CCF: A
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Code Status: Released
- Official GitHub: https://github.com/siyuhsu/vla-cache
- Project Page: https://vla-cache.github.io/
- Checkpoint: 依赖OpenVLA/OpenVLA-OFT基座；README提供下载脚本（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: README提供LIBERO部署评估说明；未确认自采真机数据是否全量公开
- Embodiment: Single Arm / Parallel Gripper
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]]

- Title: DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression
- Year: 2025
- Venue: ICML
- CCF: A
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Code Status: Partial
- Official GitHub: https://github.com/juruobenruo/DexVLA
- Project Page: https://diffusion-vla.github.io/
- Checkpoint: 公开ScaleDP权重不等于DiVLA论文完整权重；待核实（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: 作者提供DexVLA示例数据：https://huggingface.co/datasets/lesjie/dexvla_example_data；不是原论文全部实验数据
- Embodiment: Single Arm / Parallel Gripper
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/01_VLA/3D-VLA|3D-VLA]]

- Title: 3D-VLA: A 3D Vision-Language-Action Generative World Model
- Year: 2024
- Venue: ICML
- CCF: A
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Code Status: Partial
- Official GitHub: https://github.com/UMass-Embodied-AGI/3D-VLA
- Project Page: https://vis-www.cs.umass.edu/3dvla/
- Checkpoint: https://huggingface.co/anyezhy/3dvla-diffusion ; https://huggingface.co/anyezhy/3dvla-diffusion-pointcloud（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: README及model card提供OpenX来源与数据说明；完整处理后数据待核实
- Embodiment: Single Arm / Parallel Gripper
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/01_VLA/RoboMamba|RoboMamba]]

- Title: RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation
- Year: 2024
- Venue: NeurIPS
- CCF: A
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Code Status: Partial
- Official GitHub: https://github.com/lmzpai/roboMamba
- Project Page: https://sites.google.com/view/robomamba-web
- Checkpoint: test分支README提供百度网盘链接；未下载（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: 训练数据发布完整性未确认
- Embodiment: Single Arm / Parallel Gripper
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/01_VLA/VideoVLA|VideoVLA]]

- Title: VideoVLA: Video Generators Can Be Generalizable Robot Manipulators
- Year: 2025
- Venue: NeurIPS
- CCF: A
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Code Status: Partial
- Official GitHub: https://github.com/VideoVLA-Project/VideoVLA
- Project Page: https://videovla-nips2025.github.io/
- Checkpoint: 项目页提供VideoVLA模型链接；README还要求CogVideo的T5与VAE；未下载（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: README未提供完整论文训练数据准备流程
- Embodiment: Single Arm / Parallel Gripper
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

## 2. Robot Manipulation

### [[02_Papers/01_VLA/ReconVLA|ReconVLA]]

- Title: ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver
- Year: 2026
- Venue: AAAI
- CCF: A
- Type: Method Paper
- Category: VLA; Robot Manipulation; Generalization; Diffusion
- Code Status: Released
- Official GitHub: https://github.com/OpenHelix-Team/ReconVLA
- Project Page: https://zionchow.github.io/ReconVLA/
- Checkpoint: Unknown — 本轮未发现作者公开的 ReconVLA checkpoint 入口
- Dataset: 仓库提供 BridgeData V2、LIBERO、CALVIN 的下载与预处理说明；不附带原始数据，完整汇编数据集入口未核实
- Embodiment: Single Arm / Parallel Gripper
- Robot Platform: Franka Panda (CALVIN simulation); real-world platform not confirmed at abstract level
- Real Robot: Yes
- Verification Status: Official AAAI proceedings and official repository verified; CCF A verified on current official CCF list

### [[02_Papers/01_VLA/3D-VLA|3D-VLA]]

- Title: 3D-VLA: A 3D Vision-Language-Action Generative World Model
- Year: 2024
- Venue: ICML
- CCF: A
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Code Status: Partial
- Official GitHub: https://github.com/UMass-Embodied-AGI/3D-VLA
- Project Page: https://vis-www.cs.umass.edu/3dvla/
- Checkpoint: https://huggingface.co/anyezhy/3dvla-diffusion ; https://huggingface.co/anyezhy/3dvla-diffusion-pointcloud（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: README及model card提供OpenX来源与数据说明；完整处理后数据待核实
- Embodiment: Single Arm / Parallel Gripper
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/06_Diffusion_Flow_IL_RL/FlowPolicy|FlowPolicy]]

- Title: FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation
- Year: 2025
- Venue: AAAI
- CCF: A
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Code Status: Released
- Official GitHub: https://github.com/zql-kk/FlowPolicy
- Project Page: 
- Checkpoint: 本轮未发现明确完整预训练策略权重入口；可按作者说明训练（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: 提供Adroit/MetaWorld示范生成脚本与说明；未下载数据
- Embodiment: Single Arm / Parallel Gripper
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/04_Dexterous/UniGraspTransformer|UniGraspTransformer]]

- Title: UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping
- Year: 2025
- Venue: CVPR
- CCF: A
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Code Status: Released
- Official GitHub: https://github.com/microsoft/UniGraspTransformer
- Project Page: https://dexhand.github.io/UniGraspTransformer/
- Checkpoint: IsaacGym3权重说明及IsaacGym4专用策略入口存在；IsaacGym4通用策略未发布（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: 提供资产/抓取初始化数据链接和生成轨迹步骤；未下载
- Embodiment: Dexterous Hand
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/02_Robot_Manipulation/ManipLLM|ManipLLM]]

- Title: ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation
- Year: 2024
- Venue: CVPR
- CCF: A
- Type: Method Paper
- Category: Robot Manipulation
- Code Status: Partial
- Official GitHub: https://github.com/clorislili/ManipLLM
- Project Page: https://sites.google.com/view/manipllm
- Checkpoint: Unknown
- Dataset: Unknown
- Embodiment: Single Arm / Parallel Gripper
- Robot Platform: Unknown
- Real Robot: Yes
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/06_Diffusion_Flow_IL_RL/AR-VRM|AR-VRM]]

- Title: AR-VRM: Imitating Human Motions for Visual Robot Manipulation with Analogical Reasoning
- Year: 2025
- Venue: ICCV
- CCF: A
- Type: Method Paper
- Category: Robot Manipulation; Imitation Learning
- Code Status: Released
- Official GitHub: https://github.com/idejie/ar
- Project Page: https://idejie.com/AR/
- Checkpoint: Unknown
- Dataset: Unknown
- Embodiment: Single Arm / Parallel Gripper
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/10_Benchmark_Dataset/SurgicAI|SurgicAI]]

- Title: SurgicAI: A Hierarchical Platform for Fine-Grained Surgical Policy Learning and Benchmarking
- Year: 2024
- Venue: NeurIPS
- CCF: A
- Type: Dataset / Benchmark
- Category: Dataset / Benchmark; Robot Manipulation
- Code Status: Released
- Official GitHub: https://github.com/surgical-robotics-ai/SurgicAI
- Project Page: Unknown
- Checkpoint: Unknown
- Dataset: Unknown
- Embodiment: Bimanual / Surgical Robot
- Robot Platform: Unknown
- Real Robot: No
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/06_Diffusion_Flow_IL_RL/Robot_Policy_Learning_with_Temporal_Optimal_Transport_Reward|Robot Policy Learning with Temporal Optimal Transport Reward]]

- Title: Robot Policy Learning with Temporal Optimal Transport Reward
- Year: 2024
- Venue: NeurIPS
- CCF: A
- Type: Method Paper
- Category: Robot Manipulation; Reinforcement Learning
- Code Status: Released
- Official GitHub: https://github.com/fuyw/TemporalOT
- Project Page: Unknown
- Checkpoint: Unknown
- Dataset: Unknown
- Embodiment: Simulation Only
- Robot Platform: Unknown
- Real Robot: No
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/07_Generalization_LongHorizon/Closed-Loop_Visuomotor_Control_with_Generative_Expectation_for_Robotic_Manipulation|Closed-Loop Visuomotor Control with Generative Expectation for Robotic Manipulation]]

- Title: Closed-Loop Visuomotor Control with Generative Expectation for Robotic Manipulation
- Year: 2024
- Venue: NeurIPS
- CCF: A
- Type: Method Paper
- Category: Robot Manipulation
- Code Status: Released
- Official GitHub: https://github.com/OpenDriveLab/CLOVER
- Project Page: Unknown
- Checkpoint: Unknown
- Dataset: Unknown
- Embodiment: Single Arm / Parallel Gripper
- Robot Platform: Unknown
- Real Robot: Yes
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

## 3. Bimanual Manipulation

### [[02_Papers/10_Benchmark_Dataset/RoboTwin|RoboTwin]]

- Title: RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins
- Year: 2025
- Venue: CVPR
- CCF: A
- Type: Dataset / Benchmark
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Code Status: Released
- Official GitHub: https://github.com/RoboTwin-Platform/RoboTwin/tree/RoboTwin-1.0
- Project Page: https://robotwin-platform.github.io/
- Checkpoint: 
- Dataset: 作者提供资源下载与示范采集脚本；本轮未下载或核验数据完整性
- Embodiment: Bimanual / Parallel Gripper
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/03_Bimanual/ManipTrans|ManipTrans]]

- Title: ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning
- Year: 2025
- Venue: CVPR
- CCF: A
- Type: Method Paper
- Category: Bimanual Manipulation; Dexterous Manipulation
- Code Status: Released
- Official GitHub: https://github.com/ManipTrans/ManipTrans
- Project Page: https://maniptrans.github.io/
- Checkpoint: Unknown
- Dataset: Unknown
- Embodiment: Bimanual / Dexterous Hand
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

## 4. Dexterous Manipulation / Dexterous Hand

### [[02_Papers/04_Dexterous/UniGraspTransformer|UniGraspTransformer]]

- Title: UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping
- Year: 2025
- Venue: CVPR
- CCF: A
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Code Status: Released
- Official GitHub: https://github.com/microsoft/UniGraspTransformer
- Project Page: https://dexhand.github.io/UniGraspTransformer/
- Checkpoint: IsaacGym3权重说明及IsaacGym4专用策略入口存在；IsaacGym4通用策略未发布（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: 提供资产/抓取初始化数据链接和生成轨迹步骤；未下载
- Embodiment: Dexterous Hand
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/04_Dexterous/Scaffolding_Dexterous_Manipulation_with_Vision-Language_Models|Scaffolding Dexterous Manipulation with Vision-Language Models]]

- Title: Scaffolding Dexterous Manipulation with Vision-Language Models
- Year: 2025
- Venue: NeurIPS
- CCF: A
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Code Status: Released
- Official GitHub: https://github.com/vdebakker/vlm-scaffolding
- Project Page: https://sites.google.com/view/dexterous-vlm-scaffolding
- Checkpoint: 本轮未发现完整预训练策略包公开链接（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: 公开数据生成实现与任务资产；不等于所有论文轨迹均已提供
- Embodiment: Dexterous Hand
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/04_Dexterous/DextER|DextER]]

- Title: DextER: Language-driven Dexterous Grasp Generation with Embodied Reasoning
- Year: 2026
- Venue: CVPR
- CCF: A
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Code Status: Released
- Official GitHub: https://github.com/junha-l/dexter
- Project Page: https://junha-l.github.io/dexter/
- Checkpoint: https://huggingface.co/junhalee/dexter-qwen2.5-0.5B-dexgys（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: 作者提供预处理数据：https://huggingface.co/datasets/EunhaPark/project_dexter；未下载
- Embodiment: Dexterous Hand
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/03_Bimanual/ManipTrans|ManipTrans]]

- Title: ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning
- Year: 2025
- Venue: CVPR
- CCF: A
- Type: Method Paper
- Category: Bimanual Manipulation; Dexterous Manipulation
- Code Status: Released
- Official GitHub: https://github.com/ManipTrans/ManipTrans
- Project Page: https://maniptrans.github.io/
- Checkpoint: Unknown
- Dataset: Unknown
- Embodiment: Bimanual / Dexterous Hand
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/04_Dexterous/DexHandDiff|DexHandDiff]]

- Title: DexHandDiff: Interaction-aware Diffusion Planning for Adaptive Dexterous Manipulation
- Year: 2025
- Venue: CVPR
- CCF: A
- Type: Method Paper
- Category: Dexterous Manipulation
- Code Status: Partial
- Official GitHub: https://github.com/Liang-ZX/DexHandDiff
- Project Page: https://dexdiffuser.github.io/
- Checkpoint: Unknown
- Dataset: Unknown
- Embodiment: Dexterous Hand
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/04_Dexterous/Dexterous_Grasp_Transformer|Dexterous Grasp Transformer]]

- Title: Dexterous Grasp Transformer
- Year: 2024
- Venue: CVPR
- CCF: A
- Type: Method Paper
- Category: Dexterous Manipulation
- Code Status: Released
- Official GitHub: https://github.com/iSEE-Laboratory/DGTR
- Project Page: Unknown
- Checkpoint: Unknown
- Dataset: Unknown
- Embodiment: Dexterous Hand
- Robot Platform: Unknown
- Real Robot: No
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

## 5. Imitation Learning / Diffusion / Flow

### [[02_Papers/01_VLA/ReconVLA|ReconVLA]]

- Title: ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver
- Year: 2026
- Venue: AAAI
- CCF: A
- Type: Method Paper
- Category: VLA; Robot Manipulation; Generalization; Diffusion
- Code Status: Released
- Official GitHub: https://github.com/OpenHelix-Team/ReconVLA
- Project Page: https://zionchow.github.io/ReconVLA/
- Checkpoint: Unknown — 本轮未发现作者公开的 ReconVLA checkpoint 入口
- Dataset: 仓库提供 BridgeData V2、LIBERO、CALVIN 的下载与预处理说明；不附带原始数据，完整汇编数据集入口未核实
- Embodiment: Single Arm / Parallel Gripper
- Robot Platform: Franka Panda (CALVIN simulation); real-world platform not confirmed at abstract level
- Real Robot: Yes
- Verification Status: Official AAAI proceedings and official repository verified; CCF A verified on current official CCF list

### [[02_Papers/01_VLA/3D-VLA|3D-VLA]]

- Title: 3D-VLA: A 3D Vision-Language-Action Generative World Model
- Year: 2024
- Venue: ICML
- CCF: A
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Code Status: Partial
- Official GitHub: https://github.com/UMass-Embodied-AGI/3D-VLA
- Project Page: https://vis-www.cs.umass.edu/3dvla/
- Checkpoint: https://huggingface.co/anyezhy/3dvla-diffusion ; https://huggingface.co/anyezhy/3dvla-diffusion-pointcloud（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: README及model card提供OpenX来源与数据说明；完整处理后数据待核实
- Embodiment: Single Arm / Parallel Gripper
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/06_Diffusion_Flow_IL_RL/FlowPolicy|FlowPolicy]]

- Title: FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation
- Year: 2025
- Venue: AAAI
- CCF: A
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Code Status: Released
- Official GitHub: https://github.com/zql-kk/FlowPolicy
- Project Page: 
- Checkpoint: 本轮未发现明确完整预训练策略权重入口；可按作者说明训练（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: 提供Adroit/MetaWorld示范生成脚本与说明；未下载数据
- Embodiment: Single Arm / Parallel Gripper
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/04_Dexterous/UniGraspTransformer|UniGraspTransformer]]

- Title: UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping
- Year: 2025
- Venue: CVPR
- CCF: A
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Code Status: Released
- Official GitHub: https://github.com/microsoft/UniGraspTransformer
- Project Page: https://dexhand.github.io/UniGraspTransformer/
- Checkpoint: IsaacGym3权重说明及IsaacGym4专用策略入口存在；IsaacGym4通用策略未发布（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: 提供资产/抓取初始化数据链接和生成轨迹步骤；未下载
- Embodiment: Dexterous Hand
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/04_Dexterous/DexHandDiff|DexHandDiff]]

- Title: DexHandDiff: Interaction-aware Diffusion Planning for Adaptive Dexterous Manipulation
- Year: 2025
- Venue: CVPR
- CCF: A
- Type: Method Paper
- Category: Dexterous Manipulation
- Code Status: Partial
- Official GitHub: https://github.com/Liang-ZX/DexHandDiff
- Project Page: https://dexdiffuser.github.io/
- Checkpoint: Unknown
- Dataset: Unknown
- Embodiment: Dexterous Hand
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/06_Diffusion_Flow_IL_RL/AR-VRM|AR-VRM]]

- Title: AR-VRM: Imitating Human Motions for Visual Robot Manipulation with Analogical Reasoning
- Year: 2025
- Venue: ICCV
- CCF: A
- Type: Method Paper
- Category: Robot Manipulation; Imitation Learning
- Code Status: Released
- Official GitHub: https://github.com/idejie/ar
- Project Page: https://idejie.com/AR/
- Checkpoint: Unknown
- Dataset: Unknown
- Embodiment: Single Arm / Parallel Gripper
- Robot Platform: Unknown
- Real Robot: Unknown
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping

### [[02_Papers/06_Diffusion_Flow_IL_RL/Robot_Policy_Learning_with_Temporal_Optimal_Transport_Reward|Robot Policy Learning with Temporal Optimal Transport Reward]]

- Title: Robot Policy Learning with Temporal Optimal Transport Reward
- Year: 2024
- Venue: NeurIPS
- CCF: A
- Type: Method Paper
- Category: Robot Manipulation; Reinforcement Learning
- Code Status: Released
- Official GitHub: https://github.com/fuyw/TemporalOT
- Project Page: Unknown
- Checkpoint: Unknown
- Dataset: Unknown
- Embodiment: Simulation Only
- Robot Platform: Unknown
- Real Robot: No
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping
