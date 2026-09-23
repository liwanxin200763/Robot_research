# CCF A 与开源论文清单

本页仅包含 CCF A 正式论文中，官方方法代码已核验为已开放或有实际内容的部分开放条目。

## 1. VLA / 机器人基础模型

### [[02_Papers/01_VLA/ReconVLA|ReconVLA]]

- 正式标题： ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver
- 年份： 2026
- 会议 / 期刊： AAAI
- CCF 等级： A
- 论文类型： 方法论文
- 分类： VLA; Robot Manipulation; Generalization; Diffusion
- 代码开放情况：已开放
- 官方代码： https://github.com/OpenHelix-Team/ReconVLA
- 项目主页： https://zionchow.github.io/ReconVLA/
- 具身形态：单臂 / 平行夹爪
- 真机验证：是

### [[02_Papers/01_VLA/BridgeVLA|BridgeVLA]]

- 正式标题： BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models
- 年份： 2025
- 会议 / 期刊： NeurIPS
- CCF 等级： A
- 论文类型： 方法论文
- 代码开放情况：已开放
- 官方代码： https://github.com/BridgeVLA/BridgeVLA/tree/bridgevla
- 项目主页： https://bridgevla.github.io/
- 模型权重： https://huggingface.co/datasets/LPY/BridgeVLA/tree/main/checkpoints/bridgevla（作者入口/说明；未验证权重文件可下载或可用性）
- 数据集： README提供预训练数据及RLBench/COLOSSEUM/GemBench说明；入口存在，未下载
- 具身形态：单臂 / 平行夹爪

### [[02_Papers/01_VLA/VLA-Cache|VLA-Cache]]

- 正式标题：VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching
- 年份：2025
- 发表 venue：NeurIPS
- CCF：A
- 类型：方法论文
- 分类：VLA、机器人操作、推理加速
- [作者官方代码](https://github.com/siyuhsu/vla-cache)
- [项目主页](https://vla-cache.github.io/)
- Checkpoint：依赖 OpenVLA/OpenVLA-OFT 基座；README 提供基座权重下载脚本
- 具身形态：单臂、平行夹爪
- 真机：是，Kinova Jaco2
- 正文证据：A

### [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]]

- 正式标题： DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression
- 年份： 2025
- 会议 / 期刊： ICML
- CCF 等级： A
- 论文类型： 方法论文
- 代码开放情况：部分开放
- 官方代码： https://github.com/juruobenruo/DexVLA
- 项目主页： https://diffusion-vla.github.io/
- 模型权重： 公开ScaleDP权重不等于DiVLA论文完整权重；待核实（作者入口/说明；未验证权重文件可下载或可用性）
- 数据集： 作者提供DexVLA示例数据：https://huggingface.co/datasets/lesjie/dexvla_example_data；不是原论文全部实验数据
- 具身形态：单臂 / 平行夹爪

### [[02_Papers/01_VLA/3D-VLA|3D-VLA]]

- 正式标题：3D-VLA: A 3D Vision-Language-Action Generative World Model
- 年份：2024
- 发表 venue：ICML
- CCF：A
- 类型：方法论文
- 分类：VLA、机器人操作、3D grounding、Diffusion
- 代码状态：部分开放；目标图像/点云生成代码与权重入口公开，完整 VLA/LLM checkpoint 未公开确认
- [作者官方代码](https://github.com/UMass-Embodied-AGI/3D-VLA)
- [项目主页](https://vis-www.cs.umass.edu/3dvla/)
- 具身形态：单臂、平行夹爪（RLBench 任务）
- 正文证据：A

- 正式标题： 3D-VLA: A 3D Vision-Language-Action Generative World Model
- 年份： 2024
- 会议 / 期刊： ICML
- CCF 等级： A
- 论文类型： 方法论文
- 代码开放情况：部分开放
- 官方代码： https://github.com/UMass-Embodied-AGI/3D-VLA
- 项目主页： https://vis-www.cs.umass.edu/3dvla/
- 模型权重： https://huggingface.co/anyezhy/3dvla-diffusion ; https://huggingface.co/anyezhy/3dvla-diffusion-pointcloud（作者入口/说明；未验证权重文件可下载或可用性）
- 数据集： README及model card提供OpenX来源与数据说明；完整处理后数据待核实
- 具身形态：单臂 / 平行夹爪

### [[02_Papers/01_VLA/RoboMamba|RoboMamba]]

- 正式标题： RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation
- 年份： 2024
- 会议 / 期刊： NeurIPS
- CCF 等级： A
- 论文类型： 方法论文
- 代码开放情况：部分开放
- 官方代码： https://github.com/lmzpai/roboMamba
- 项目主页： https://sites.google.com/view/robomamba-web
- 模型权重： test分支README提供百度网盘链接；未下载（作者入口/说明；未验证权重文件可下载或可用性）
- 具身形态：单臂 / 平行夹爪

### [[02_Papers/01_VLA/VideoVLA|VideoVLA]]

- 正式标题： VideoVLA: Video Generators Can Be Generalizable Robot Manipulators
- 年份： 2025
- 会议 / 期刊： NeurIPS
- CCF 等级： A
- 论文类型： 方法论文
- 代码开放情况：部分开放
- 官方代码： https://github.com/VideoVLA-Project/VideoVLA
- 项目主页： https://videovla-nips2025.github.io/
- 模型权重： 项目页提供VideoVLA模型链接；README还要求CogVideo的T5与VAE；未下载（作者入口/说明；未验证权重文件可下载或可用性）
- 数据集： README未提供完整论文训练数据准备流程
- 具身形态：单臂 / 平行夹爪

## 2. 机器人操作

### [[02_Papers/01_VLA/ReconVLA|ReconVLA]]

- 正式标题： ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver
- 年份： 2026
- 会议 / 期刊： AAAI
- CCF 等级： A
- 论文类型： 方法论文
- 分类： VLA; Robot Manipulation; Generalization; Diffusion
- 代码开放情况：已开放
- 官方代码： https://github.com/OpenHelix-Team/ReconVLA
- 项目主页： https://zionchow.github.io/ReconVLA/
- 具身形态：单臂 / 平行夹爪
- 真机验证：是

### [[02_Papers/01_VLA/3D-VLA|3D-VLA]]

- 正式标题： 3D-VLA: A 3D Vision-Language-Action Generative World Model
- 年份： 2024
- 会议 / 期刊： ICML
- CCF 等级： A
- 论文类型： 方法论文
- 代码开放情况：部分开放
- 官方代码： https://github.com/UMass-Embodied-AGI/3D-VLA
- 项目主页： https://vis-www.cs.umass.edu/3dvla/
- 模型权重： https://huggingface.co/anyezhy/3dvla-diffusion ; https://huggingface.co/anyezhy/3dvla-diffusion-pointcloud（作者入口/说明；未验证权重文件可下载或可用性）
- 数据集： README及model card提供OpenX来源与数据说明；完整处理后数据待核实
- 具身形态：单臂 / 平行夹爪

### [[02_Papers/06_Diffusion_Flow_IL_RL/FlowPolicy|FlowPolicy]]

- 正式标题： FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation
- 年份： 2025
- 会议 / 期刊： AAAI
- CCF 等级： A
- 论文类型： 方法论文
- 代码开放情况：已开放
- 官方代码： https://github.com/zql-kk/FlowPolicy
- 模型权重： 本轮未发现明确完整预训练策略权重入口；可按作者说明训练（作者入口/说明；未验证权重文件可下载或可用性）
- 数据集： 提供Adroit/MetaWorld示范生成脚本与说明；未下载数据
- 具身形态：单臂 / 平行夹爪

### [[02_Papers/04_Dexterous/UniGraspTransformer|UniGraspTransformer]]

- 正式标题： UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping
- 年份： 2025
- 会议 / 期刊： CVPR
- CCF 等级： A
- 论文类型： 方法论文
- 代码开放情况：已开放
- 官方代码： https://github.com/microsoft/UniGraspTransformer
- 项目主页： https://dexhand.github.io/UniGraspTransformer/
- 模型权重： IsaacGym3权重说明及IsaacGym4专用策略入口存在；IsaacGym4通用策略未发布（作者入口/说明；未验证权重文件可下载或可用性）
- 数据集： 提供资产/抓取初始化数据链接和生成轨迹步骤；未下载
- 具身形态： Dexterous Hand

### [[02_Papers/02_Robot_Manipulation/ManipLLM|ManipLLM]]

- 正式标题： ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation
- 年份： 2024
- 会议 / 期刊： CVPR
- CCF 等级： A
- 论文类型： 方法论文
- 分类： Robot Manipulation
- 代码开放情况：部分开放
- 官方代码： https://github.com/clorislili/ManipLLM
- 项目主页： https://sites.google.com/view/manipllm
- 具身形态：单臂 / 平行夹爪
- 真机验证：是

### [[02_Papers/06_Diffusion_Flow_IL_RL/AR-VRM|AR-VRM]]

- 正式标题： AR-VRM: Imitating Human Motions for Visual Robot Manipulation with Analogical Reasoning
- 年份： 2025
- 会议 / 期刊： ICCV
- CCF 等级： A
- 论文类型： 方法论文
- 分类： Robot Manipulation; Imitation Learning
- 代码开放情况：已开放
- 官方代码： https://github.com/idejie/ar
- 项目主页： https://idejie.com/AR/
- 具身形态：单臂 / 平行夹爪

### [[02_Papers/10_Benchmark_Dataset/SurgicAI|SurgicAI]]

- 正式标题： SurgicAI: A Hierarchical Platform for Fine-Grained Surgical Policy Learning and Benchmarking
- 年份： 2024
- 会议 / 期刊： NeurIPS
- CCF 等级： A
- 论文类型： Dataset / Benchmark
- 分类： Dataset / Benchmark; Robot Manipulation
- 代码开放情况：已开放
- 官方代码： https://github.com/surgical-robotics-ai/SurgicAI
- 具身形态： Bimanual / Surgical Robot
- 真机验证： No

### [[02_Papers/06_Diffusion_Flow_IL_RL/Robot_Policy_Learning_with_Temporal_Optimal_Transport_Reward|Robot Policy Learning with Temporal Optimal Transport Reward]]

- 正式标题： Robot Policy Learning with Temporal Optimal Transport Reward
- 年份： 2024
- 会议 / 期刊： NeurIPS
- CCF 等级： A
- 论文类型： 方法论文
- 分类： Robot Manipulation; Reinforcement Learning
- 代码开放情况：已开放
- 官方代码： https://github.com/fuyw/TemporalOT
- 具身形态： Simulation Only
- 真机验证： No

### [[02_Papers/07_Generalization_LongHorizon/Closed-Loop_Visuomotor_Control_with_Generative_Expectation_for_Robotic_Manipulation|Closed-Loop Visuomotor Control with Generative Expectation for Robotic Manipulation]]

- 正式标题： Closed-Loop Visuomotor Control with Generative Expectation for Robotic Manipulation
- 年份： 2024
- 会议 / 期刊： NeurIPS
- CCF 等级： A
- 论文类型： 方法论文
- 分类： Robot Manipulation
- 代码开放情况：已开放
- 官方代码： https://github.com/OpenDriveLab/CLOVER
- 具身形态：单臂 / 平行夹爪
- 真机验证：是

## 3. 双臂操作

### [[02_Papers/10_Benchmark_Dataset/RoboTwin|RoboTwin]]

- 正式标题： RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins
- 年份： 2025
- 会议 / 期刊： CVPR
- CCF 等级： A
- 论文类型： Dataset / Benchmark
- 代码开放情况：已开放
- 官方代码： https://github.com/RoboTwin-Platform/RoboTwin/tree/RoboTwin-1.0
- 项目主页： https://robotwin-platform.github.io/
- 数据集： 作者提供资源下载与示范采集脚本；本轮未下载或核验数据完整性
- 具身形态： Bimanual / Parallel Gripper

### [[02_Papers/03_Bimanual/ManipTrans|ManipTrans]]

- 正式标题： ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning
- 年份： 2025
- 会议 / 期刊： CVPR
- CCF 等级： A
- 论文类型： 方法论文
- 分类： Bimanual Manipulation; Dexterous Manipulation
- 代码开放情况：已开放
- 官方代码： https://github.com/ManipTrans/ManipTrans
- 项目主页： https://maniptrans.github.io/
- 具身形态： Bimanual / Dexterous Hand

## 4. 灵巧操作 / 灵巧手

### [[02_Papers/04_Dexterous/UniGraspTransformer|UniGraspTransformer]]

- 正式标题： UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping
- 年份： 2025
- 会议 / 期刊： CVPR
- CCF 等级： A
- 论文类型： 方法论文
- 代码开放情况：已开放
- 官方代码： https://github.com/microsoft/UniGraspTransformer
- 项目主页： https://dexhand.github.io/UniGraspTransformer/
- 模型权重： IsaacGym3权重说明及IsaacGym4专用策略入口存在；IsaacGym4通用策略未发布（作者入口/说明；未验证权重文件可下载或可用性）
- 数据集： 提供资产/抓取初始化数据链接和生成轨迹步骤；未下载
- 具身形态： Dexterous Hand

### [[02_Papers/04_Dexterous/Scaffolding_Dexterous_Manipulation_with_Vision-Language_Models|Scaffolding Dexterous Manipulation with Vision-Language Models]]

- 正式标题： Scaffolding Dexterous Manipulation with Vision-Language Models
- 年份： 2025
- 会议 / 期刊： NeurIPS
- CCF 等级： A
- 论文类型： 方法论文
- 代码开放情况：已开放
- 官方代码： https://github.com/vdebakker/vlm-scaffolding
- 项目主页： https://sites.google.com/view/dexterous-vlm-scaffolding
- 模型权重： 本轮未发现完整预训练策略包公开链接（作者入口/说明；未验证权重文件可下载或可用性）
- 数据集： 公开数据生成实现与任务资产；不等于所有论文轨迹均已提供
- 具身形态： Dexterous Hand

### [[02_Papers/04_Dexterous/DextER|DextER]]

- 正式标题： DextER: Language-driven Dexterous Grasp Generation with Embodied Reasoning
- 年份： 2026
- 会议 / 期刊： CVPR
- CCF 等级： A
- 论文类型： 方法论文
- 代码开放情况：已开放
- 官方代码： https://github.com/junha-l/dexter
- 项目主页： https://junha-l.github.io/dexter/
- 模型权重： https://huggingface.co/junhalee/dexter-qwen2.5-0.5B-dexgys（作者入口/说明；未验证权重文件可下载或可用性）
- 数据集： 作者提供预处理数据：https://huggingface.co/datasets/EunhaPark/project_dexter；未下载
- 具身形态： Dexterous Hand

### [[02_Papers/03_Bimanual/ManipTrans|ManipTrans]]

- 正式标题： ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning
- 年份： 2025
- 会议 / 期刊： CVPR
- CCF 等级： A
- 论文类型： 方法论文
- 分类： Bimanual Manipulation; Dexterous Manipulation
- 代码开放情况：已开放
- 官方代码： https://github.com/ManipTrans/ManipTrans
- 项目主页： https://maniptrans.github.io/
- 具身形态： Bimanual / Dexterous Hand

### [[02_Papers/04_Dexterous/DexHandDiff|DexHandDiff]]

- 正式标题： DexHandDiff: Interaction-aware Diffusion Planning for Adaptive Dexterous Manipulation
- 年份： 2025
- 会议 / 期刊： CVPR
- CCF 等级： A
- 论文类型： 方法论文
- 分类： Dexterous Manipulation
- 代码开放情况：部分开放
- 官方代码： https://github.com/Liang-ZX/DexHandDiff
- 项目主页： https://dexdiffuser.github.io/
- 具身形态： Dexterous Hand

### [[02_Papers/04_Dexterous/Dexterous_Grasp_Transformer|Dexterous Grasp Transformer]]

- 正式标题： Dexterous Grasp Transformer
- 年份： 2024
- 会议 / 期刊： CVPR
- CCF 等级： A
- 论文类型： 方法论文
- 分类： Dexterous Manipulation
- 代码开放情况：已开放
- 官方代码： https://github.com/iSEE-Laboratory/DGTR
- 具身形态： Dexterous Hand
- 真机验证： No

## 5. 模仿学习 / Diffusion / Flow

### [[02_Papers/01_VLA/ReconVLA|ReconVLA]]

- 正式标题： ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver
- 年份： 2026
- 会议 / 期刊： AAAI
- CCF 等级： A
- 论文类型： 方法论文
- 分类： VLA; Robot Manipulation; Generalization; Diffusion
- 代码开放情况：已开放
- 官方代码： https://github.com/OpenHelix-Team/ReconVLA
- 项目主页： https://zionchow.github.io/ReconVLA/
- 具身形态：单臂 / 平行夹爪
- 真机验证：是

### [[02_Papers/01_VLA/3D-VLA|3D-VLA]]

- 正式标题： 3D-VLA: A 3D Vision-Language-Action Generative World Model
- 年份： 2024
- 会议 / 期刊： ICML
- CCF 等级： A
- 论文类型： 方法论文
- 代码开放情况：部分开放
- 官方代码： https://github.com/UMass-Embodied-AGI/3D-VLA
- 项目主页： https://vis-www.cs.umass.edu/3dvla/
- 模型权重： https://huggingface.co/anyezhy/3dvla-diffusion ; https://huggingface.co/anyezhy/3dvla-diffusion-pointcloud（作者入口/说明；未验证权重文件可下载或可用性）
- 数据集： README及model card提供OpenX来源与数据说明；完整处理后数据待核实
- 具身形态：单臂 / 平行夹爪

### [[02_Papers/06_Diffusion_Flow_IL_RL/FlowPolicy|FlowPolicy]]

- 正式标题： FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation
- 年份： 2025
- 会议 / 期刊： AAAI
- CCF 等级： A
- 论文类型： 方法论文
- 代码开放情况：已开放
- 官方代码： https://github.com/zql-kk/FlowPolicy
- 模型权重： 本轮未发现明确完整预训练策略权重入口；可按作者说明训练（作者入口/说明；未验证权重文件可下载或可用性）
- 数据集： 提供Adroit/MetaWorld示范生成脚本与说明；未下载数据
- 具身形态：单臂 / 平行夹爪

### [[02_Papers/04_Dexterous/UniGraspTransformer|UniGraspTransformer]]

- 正式标题： UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping
- 年份： 2025
- 会议 / 期刊： CVPR
- CCF 等级： A
- 论文类型： 方法论文
- 代码开放情况：已开放
- 官方代码： https://github.com/microsoft/UniGraspTransformer
- 项目主页： https://dexhand.github.io/UniGraspTransformer/
- 模型权重： IsaacGym3权重说明及IsaacGym4专用策略入口存在；IsaacGym4通用策略未发布（作者入口/说明；未验证权重文件可下载或可用性）
- 数据集： 提供资产/抓取初始化数据链接和生成轨迹步骤；未下载
- 具身形态： Dexterous Hand

### [[02_Papers/04_Dexterous/DexHandDiff|DexHandDiff]]

- 正式标题： DexHandDiff: Interaction-aware Diffusion Planning for Adaptive Dexterous Manipulation
- 年份： 2025
- 会议 / 期刊： CVPR
- CCF 等级： A
- 论文类型： 方法论文
- 分类： Dexterous Manipulation
- 代码开放情况：部分开放
- 官方代码： https://github.com/Liang-ZX/DexHandDiff
- 项目主页： https://dexdiffuser.github.io/
- 具身形态： Dexterous Hand

### [[02_Papers/06_Diffusion_Flow_IL_RL/AR-VRM|AR-VRM]]

- 正式标题： AR-VRM: Imitating Human Motions for Visual Robot Manipulation with Analogical Reasoning
- 年份： 2025
- 会议 / 期刊： ICCV
- CCF 等级： A
- 论文类型： 方法论文
- 分类： Robot Manipulation; Imitation Learning
- 代码开放情况：已开放
- 官方代码： https://github.com/idejie/ar
- 项目主页： https://idejie.com/AR/
- 具身形态：单臂 / 平行夹爪

### [[02_Papers/06_Diffusion_Flow_IL_RL/Robot_Policy_Learning_with_Temporal_Optimal_Transport_Reward|Robot Policy Learning with Temporal Optimal Transport Reward]]

- 正式标题： Robot Policy Learning with Temporal Optimal Transport Reward
- 年份： 2024
- 会议 / 期刊： NeurIPS
- CCF 等级： A
- 论文类型： 方法论文
- 分类： Robot Manipulation; Reinforcement Learning
- 代码开放情况：已开放
- 官方代码： https://github.com/fuyw/TemporalOT
- 具身形态： Simulation Only
- 真机验证： No
