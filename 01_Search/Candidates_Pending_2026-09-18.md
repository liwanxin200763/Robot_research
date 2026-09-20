# Candidates Pending（待复核候选） · 2026-09-18

本文件暂存16篇候选，**不属于Papers核心库，也不表示已读或已复现**。CCF等级留空，统一为Pending Official Recheck（等待官方复核）。Reading Level（阅读等级）暂记L1（相关/略读计划），尚未执行略读。正式发表身份已查官方论文集；代码状态依据当前公开实现的静态核查。Released（已发布实现）不等于已复现；Partial（部分实现）还须确认核心方法可实际运行。

| 候选编号 | 标题 | 年份 / 会议 | 主分类 | 代码状态 |
| --- | --- | --- | --- | --- |
| C001 | RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation | 2025 / ICLR | Bimanual | Released |
| C002 | TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models | 2026 / ICLR | Bimanual | Released |
| C003 | RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins | 2025 / CVPR | Bimanual | Released |
| C004 | BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models | 2025 / NeurIPS | VLA | Released |
| C005 | VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching | 2025 / NeurIPS | VLA | Released |
| C006 | DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression | 2025 / ICML | VLA | Partial |
| C007 | 3D-VLA: A 3D Vision-Language-Action Generative World Model | 2024 / ICML | VLA | Partial |
| C008 | RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation | 2024 / NeurIPS | VLA | Partial |
| C009 | TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies | 2025 / ICLR | VLA | Partial |
| C010 | Latent Action Pretraining from Videos | 2025 / ICLR | VLA | Released |
| C011 | FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation | 2025 / AAAI | Robot Manipulation | Released |
| C014 | UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping | 2025 / CVPR | Dexterous Hand | Released |
| C015 | Scaffolding Dexterous Manipulation with Vision-Language Models | 2025 / NeurIPS | Dexterous Hand | Released |
| C016 | VideoVLA: Video Generators Can Be Generalizable Robot Manipulators | 2025 / NeurIPS | VLA | Partial |
| C019 | DextER: Language-driven Dexterous Grasp Generation with Embodied Reasoning | 2026 / CVPR | Dexterous Hand | Released |
| C020 | SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models | 2025 / RSS | VLA | Released |

## C001 · RDT-1B

| Official Facts（官方事实与核查结果） | 内容 |
| --- | --- |
| Title（标题） | RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation |
| Year / Venue（年份/会议） | 2025 / ICLR；正式主会论文：官方论文集核实 |
| CCF Level（等级） | 未填写；Pending Official Recheck |
| Official Paper（官方论文） | https://proceedings.iclr.cc/paper_files/paper/2025/hash/49f80e4d2471ad4f2edf4f5f1ab62339-Abstract-Conference.html |
| Project Page（项目主页） | https://rdt-robotics.github.io/rdt-robotics/ |
| Official GitHub（代码入口） | https://github.com/thu-ml/RoboticsDiffusionTransformer |
| Code Status（代码状态） | Released |
| Commit（核查版本） | cd79363a1387e8f81c7724d070ef7e45fd23150f |
| Core Source（核心实现） | models/rdt/model.py；train/train.py；scripts/agilex_inference.py |
| Environment（依赖说明） | requirements.txt；requirements_data.txt |
| Training / Evaluation（训练/评估） | 已检查RDT模型、训练及AgileX推理实现；实际部署仍需机器人接口适配。 |
| Checkpoint（权重） | https://huggingface.co/robotics-diffusion-transformer/rdt-1b（作者入口/说明；未验证权重文件可下载或可用性） |
| Dataset Released（数据公开） | 作者提供rdt-ft-data及数据加载说明：https://huggingface.co/datasets/robotics-diffusion-transformer/rdt-ft-data；未下载 |
| Reproducibility（复现状态） | 仅静态核查公开材料；未安装、训练、推理、复现或下载权重/数据。 |
| Reading Level（阅读等级） | L1；未自动升级 |
| Checked Date（本轮核查日期） | 2026-09-18 |

Project Relevance（项目相关性分析）：Bimanual / Diffusion Foundation Model / Cross-Embodiment。分类仅用于检索组织，不代表已验证可迁移到NERO/robosuite。

## C002 · TwinVLA

| Official Facts（官方事实与核查结果） | 内容 |
| --- | --- |
| Title（标题） | TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models |
| Year / Venue（年份/会议） | 2026 / ICLR；正式主会论文：官方论文集核实 |
| CCF Level（等级） | 未填写；Pending Official Recheck |
| Official Paper（官方论文） | https://proceedings.iclr.cc/paper_files/paper/2026/hash/65475a59e2a2cb707c9462e8a308e980-Abstract-Conference.html |
| Project Page（项目主页） | https://jellyho.github.io/TwinVLA/ |
| Official GitHub（代码入口） | https://github.com/jellyho/TwinVLA |
| Code Status（代码状态） | Released |
| Commit（核查版本） | 31d00ba7a7ae3b56ff694dfb7a4242d2ec296adf |
| Core Source（核心实现） | twinvla/model/base_models.py；scripts/train_twinvla.py；TwinVLA_robotwin/deploy_policy.py |
| Environment（依赖说明） | requirements.txt；scripts/rlds_gen/requirements_rlds.txt；setup.py |
| Training / Evaluation（训练/评估） | 官方2026论文集确认；已查模型、训练、RoboTwin部署。论文集年份优先于2025预印本。 |
| Checkpoint（权重） | https://huggingface.co/collections/jellyho/twinvla（作者入口/说明；未验证权重文件可下载或可用性） |
| Dataset Released（数据公开） | 作者提供数据集合：https://huggingface.co/collections/jellyho/twinvla-datasets；未下载 |
| Reproducibility（复现状态） | 仅静态核查公开材料；未安装、训练、推理、复现或下载权重/数据。 |
| Reading Level（阅读等级） | L1；未自动升级 |
| Checked Date（本轮核查日期） | 2026-09-18 |

Project Relevance（项目相关性分析）：Bimanual / VLA / Data Efficiency / Joint Attention。分类仅用于检索组织，不代表已验证可迁移到NERO/robosuite。

## C003 · RoboTwin

| Official Facts（官方事实与核查结果） | 内容 |
| --- | --- |
| Title（标题） | RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins |
| Year / Venue（年份/会议） | 2025 / CVPR；正式主会论文：官方论文集核实 |
| CCF Level（等级） | 未填写；Pending Official Recheck |
| Official Paper（官方论文） | https://openaccess.thecvf.com/content/CVPR2025/html/Mu_RoboTwin_Dual-Arm_Robot_Benchmark_with_Generative_Digital_Twins_CVPR_2025_paper.html |
| Project Page（项目主页） | https://robotwin-platform.github.io/ |
| Official GitHub（代码入口） | https://github.com/RoboTwin-Platform/RoboTwin/tree/RoboTwin-1.0 |
| Code Status（代码状态） | Released |
| Commit（核查版本） | 65a6f5bb74794ba193c6bf17d8eae3b74fc2df70 |
| Core Source（核心实现） | envs/base_task.py；envs/block_handover.py；script/eval_policy.py |
| Environment（依赖说明） | policy/3D-Diffusion-Policy/3D-Diffusion-Policy/setup.py；policy/Diffusion-Policy/pyproject.toml；policy/RDT/requirements.txt；policy/openpi/examples/aloha_real/requirements.txt；policy/openpi/examples/aloha_sim/requirements.txt；policy/openpi/examples/libero/requirements.txt；policy/openpi/examples/simple_client/requirements.txt；policy/openpi/packages/openpi-client/pyproject.toml；policy/openpi/pyproject.toml；policy/openpi/scripts/docker/install_docker_ubuntu22.sh |
| Training / Evaluation（训练/评估） | 采用RoboTwin-1.0分支；已查任务环境、交接动作及评估。与早期ECCV Workshop版本、CVPR Workshop竞赛报告、2.0版本区别记录。 |
| Checkpoint（权重） | 本轮未核实完整权重发布 |
| Dataset Released（数据公开） | 作者提供资源下载与示范采集脚本；本轮未下载或核验数据完整性 |
| Reproducibility（复现状态） | 仅静态核查公开材料；未安装、训练、推理、复现或下载权重/数据。 |
| Reading Level（阅读等级） | L1；未自动升级 |
| Checked Date（本轮核查日期） | 2026-09-18 |

Project Relevance（项目相关性分析）：Bimanual / Benchmark / Synthetic Demonstrations。分类仅用于检索组织，不代表已验证可迁移到NERO/robosuite。

## C004 · BridgeVLA

| Official Facts（官方事实与核查结果） | 内容 |
| --- | --- |
| Title（标题） | BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models |
| Year / Venue（年份/会议） | 2025 / NeurIPS；正式主会论文：官方论文集核实 |
| CCF Level（等级） | 未填写；Pending Official Recheck |
| Official Paper（官方论文） | https://proceedings.neurips.cc/paper_files/paper/2025/hash/5c1a8aa04c1a2cf5013f28831870dafa-Abstract-Conference.html |
| Project Page（项目主页） | https://bridgevla.github.io/ |
| Official GitHub（代码入口） | https://github.com/BridgeVLA/BridgeVLA/tree/bridgevla |
| Code Status（代码状态） | Released |
| Commit（核查版本） | d5199839650f834eac9b3a92ec27f7866f59e57d |
| Core Source（核心实现） | finetune/bridgevla/models/bridgevla_agent.py；finetune/RLBench/train.py；finetune/RLBench/eval.py |
| Environment（依赖说明） | finetune/Colosseum/install_colosseum.sh；finetune/Colosseum/robot-colosseum/docs/requirements.txt；finetune/Colosseum/robot-colosseum/pyproject.toml；finetune/Colosseum/robot-colosseum/requirements-dev.txt；finetune/Colosseum/robot-colosseum/requirements.txt；finetune/Colosseum/robot-colosseum/setup.py；finetune/GemBench/install_gembench.sh；finetune/GemBench/setup.py；finetune/RLBench/install_rlbench.sh；finetune/bridgevla/libs/YARR/requirements.txt |
| Training / Evaluation（训练/评估） | 原论文代码在bridgevla分支；main已是BridgeVLA++，不可混用。已查agent、训练、评估；PaliGemma基础权重需申请访问。 |
| Checkpoint（权重） | https://huggingface.co/datasets/LPY/BridgeVLA/tree/main/checkpoints/bridgevla（作者入口/说明；未验证权重文件可下载或可用性） |
| Dataset Released（数据公开） | README提供预训练数据及RLBench/COLOSSEUM/GemBench说明；入口存在，未下载 |
| Reproducibility（复现状态） | 仅静态核查公开材料；未安装、训练、推理、复现或下载权重/数据。 |
| Reading Level（阅读等级） | L1；未自动升级 |
| Checked Date（本轮核查日期） | 2026-09-18 |

Project Relevance（项目相关性分析）：VLA / 3D Manipulation / Data Efficiency。分类仅用于检索组织，不代表已验证可迁移到NERO/robosuite。

## C005 · VLA-Cache

| Official Facts（官方事实与核查结果） | 内容 |
| --- | --- |
| Title（标题） | VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching |
| Year / Venue（年份/会议） | 2025 / NeurIPS；正式主会论文：官方论文集核实 |
| CCF Level（等级） | 未填写；Pending Official Recheck |
| Official Paper（官方论文） | https://proceedings.neurips.cc/paper_files/paper/2025/hash/f062da1973ac9ac61fc6d44dd7fa309f-Abstract-Conference.html |
| Project Page（项目主页） | https://vla-cache.github.io/ |
| Official GitHub（代码入口） | https://github.com/siyuhsu/vla-cache |
| Code Status（代码状态） | Released |
| Commit（核查版本） | a4909880573868dee2769343d52e793c0341678b |
| Core Source（核心实现） | src/openvla/experiments/robot/vla_cache_utils.py；src/openvla/prismatic/extern/hf/modeling_prismatic.py |
| Environment（依赖说明） | src/openvla-oft/experiments/robot/aloha/requirements_aloha.txt；src/openvla-oft/pyproject.toml；src/openvla/pyproject.toml；src/openvla/requirements-min.txt |
| Training / Evaluation（训练/评估） | 已查patch相似度、层级缓存调度及模型实现；方法免训练。训练代码主要继承基座，不能当作额外方法训练贡献。 |
| Checkpoint（权重） | 依赖OpenVLA/OpenVLA-OFT基座；README提供下载脚本（作者入口/说明；未验证权重文件可下载或可用性） |
| Dataset Released（数据公开） | README提供LIBERO部署评估说明；未确认自采真机数据是否全量公开 |
| Reproducibility（复现状态） | 仅静态核查公开材料；未安装、训练、推理、复现或下载权重/数据。 |
| Reading Level（阅读等级） | L1；未自动升级 |
| Checked Date（本轮核查日期） | 2026-09-18 |

Project Relevance（项目相关性分析）：VLA / Inference Acceleration / Token Caching。分类仅用于检索组织，不代表已验证可迁移到NERO/robosuite。

## C006 · DiffusionVLA

| Official Facts（官方事实与核查结果） | 内容 |
| --- | --- |
| Title（标题） | DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression |
| Year / Venue（年份/会议） | 2025 / ICML；正式主会论文：官方论文集核实 |
| CCF Level（等级） | 未填写；Pending Official Recheck |
| Official Paper（官方论文） | https://proceedings.mlr.press/v267/wen25g.html |
| Project Page（项目主页） | https://diffusion-vla.github.io/ |
| Official GitHub（代码入口） | https://github.com/juruobenruo/DexVLA |
| Code Status（代码状态） | Partial |
| Commit（核查版本） | fc21a822f4c774e242eb6f1ab4a235788de7aba9 |
| Core Source（核心实现） | scripts/train_divla.sh；policy_heads/models/unet_diffusion/modeling_unet_diffusion.py；evaluate/smart_eval_agilex.py |
| Environment（依赖说明） | policy_heads/setup.py；requirements.txt；setup.py |
| Training / Evaluation（训练/评估） | 官网明确指向后续DexVLA仓库并称可训练DiVLA；实际存在train_divla.sh、UNet策略和评估。原论文模型/完整实验对应关系未核实；Partial可运行条件待复核，不准入核心。 |
| Checkpoint（权重） | 公开ScaleDP权重不等于DiVLA论文完整权重；待核实（作者入口/说明；未验证权重文件可下载或可用性） |
| Dataset Released（数据公开） | 作者提供DexVLA示例数据：https://huggingface.co/datasets/lesjie/dexvla_example_data；不是原论文全部实验数据 |
| Reproducibility（复现状态） | 仅静态核查公开材料；未安装、训练、推理、复现或下载权重/数据。 |
| Reading Level（阅读等级） | L1；未自动升级 |
| Checked Date（本轮核查日期） | 2026-09-18 |

Project Relevance（项目相关性分析）：VLA / Autoregressive Reasoning / Diffusion。分类仅用于检索组织，不代表已验证可迁移到NERO/robosuite。

## C007 · 3D-VLA

| Official Facts（官方事实与核查结果） | 内容 |
| --- | --- |
| Title（标题） | 3D-VLA: A 3D Vision-Language-Action Generative World Model |
| Year / Venue（年份/会议） | 2024 / ICML；正式主会论文：官方论文集核实 |
| CCF Level（等级） | 未填写；Pending Official Recheck |
| Official Paper（官方论文） | https://proceedings.mlr.press/v235/zhen24a.html |
| Project Page（项目主页） | https://vis-www.cs.umass.edu/3dvla/ |
| Official GitHub（代码入口） | https://github.com/UMass-Embodied-AGI/3D-VLA |
| Code Status（代码状态） | Partial |
| Commit（核查版本） | 517680c352cb996630ae8099815441e79126bb9c |
| Core Source（核心实现） | inference_ldm_goal_image.py；train_ldm_goal_image.py；lavis/models/blip2_models/blip2_t5.py |
| Environment（依赖说明） | requirements.txt |
| Training / Evaluation（训练/评估） | 公开目标图像/点云扩散训练与推理、LLM训练实现；未确认完整机器人策略评测链，保守标Partial，端到端可运行性待复核。 |
| Checkpoint（权重） | https://huggingface.co/anyezhy/3dvla-diffusion ; https://huggingface.co/anyezhy/3dvla-diffusion-pointcloud（作者入口/说明；未验证权重文件可下载或可用性） |
| Dataset Released（数据公开） | README及model card提供OpenX来源与数据说明；完整处理后数据待核实 |
| Reproducibility（复现状态） | 仅静态核查公开材料；未安装、训练、推理、复现或下载权重/数据。 |
| Reading Level（阅读等级） | L1；未自动升级 |
| Checked Date（本轮核查日期） | 2026-09-18 |

Project Relevance（项目相关性分析）：VLA / World Model / 3D Generation。分类仅用于检索组织，不代表已验证可迁移到NERO/robosuite。

## C008 · RoboMamba

| Official Facts（官方事实与核查结果） | 内容 |
| --- | --- |
| Title（标题） | RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation |
| Year / Venue（年份/会议） | 2024 / NeurIPS；正式主会论文：官方论文集核实 |
| CCF Level（等级） | 未填写；Pending Official Recheck |
| Official Paper（官方论文） | https://proceedings.neurips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html |
| Project Page（项目主页） | https://sites.google.com/view/robomamba-web |
| Official GitHub（代码入口） | https://github.com/lmzpai/roboMamba |
| Code Status（代码状态） | Partial |
| Commit（核查版本） | c2f52c49217a0e383eadb71a5751567fb05b452c |
| Core Source（核心实现） | src/model/manip.py；src/model/vlm.py |
| Environment（依赖说明） | requirements.txt |
| Training / Evaluation（训练/评估） | 实际存在模型、src/test.py和src/script/test.sh；README要求邮件索取训练代码。test分支提供权重入口。未验证权重可下载/端到端运行，且项目页未查到直接GitHub出链，作者归属链须补核。 |
| Checkpoint（权重） | test分支README提供百度网盘链接；未下载（作者入口/说明；未验证权重文件可下载或可用性） |
| Dataset Released（数据公开） | 训练数据发布完整性未确认 |
| Reproducibility（复现状态） | 仅静态核查公开材料；未安装、训练、推理、复现或下载权重/数据。 |
| Reading Level（阅读等级） | L1；未自动升级 |
| Checked Date（本轮核查日期） | 2026-09-18 |

Project Relevance（项目相关性分析）：VLA / Efficient Model / Pose Prediction。分类仅用于检索组织，不代表已验证可迁移到NERO/robosuite。

## C009 · TraceVLA

| Official Facts（官方事实与核查结果） | 内容 |
| --- | --- |
| Title（标题） | TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies |
| Year / Venue（年份/会议） | 2025 / ICLR；正式主会论文：官方论文集核实 |
| CCF Level（等级） | 未填写；Pending Official Recheck |
| Official Paper（官方论文） | https://proceedings.iclr.cc/paper_files/paper/2025/hash/8667f264f88c7938a73a53ab01eb1327-Abstract-Conference.html |
| Project Page（项目主页） | https://tracevla.github.io/ |
| Official GitHub（代码入口） | https://github.com/umd-huang-lab/tracevla |
| Code Status（代码状态） | Partial |
| Commit（核查版本） | d5454af9ebe51e996005e13061ac3f6964e2923f |
| Core Source（核心实现） | prismatic/eval/trace_processor.py；prismatic/eval/tracevla_simpler.py；vla-scripts/train.py |
| Environment（依赖说明） | pyproject.toml |
| Training / Evaluation（训练/评估） | 已查TraceProcessor、推理与训练代码；README仍称轨迹标注数据Coming soon，未验证论文权重/数据完整链。保守标Partial，待可运行性复核。 |
| Checkpoint（权重） | 项目页Models入口与README基座链接须区分；论文权重待核实（作者入口/说明；未验证权重文件可下载或可用性） |
| Dataset Released（数据公开） | 视觉轨迹标注数据仍标Coming soon；基础数据另行获取 |
| Reproducibility（复现状态） | 仅静态核查公开材料；未安装、训练、推理、复现或下载权重/数据。 |
| Reading Level（阅读等级） | L1；未自动升级 |
| Checked Date（本轮核查日期） | 2026-09-18 |

Project Relevance（项目相关性分析）：VLA / Visual Trace Prompting。分类仅用于检索组织，不代表已验证可迁移到NERO/robosuite。

## C010 · LAPA

| Official Facts（官方事实与核查结果） | 内容 |
| --- | --- |
| Title（标题） | Latent Action Pretraining from Videos |
| Year / Venue（年份/会议） | 2025 / ICLR；正式主会论文：官方论文集核实 |
| CCF Level（等级） | 未填写；Pending Official Recheck |
| Official Paper（官方论文） | https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html |
| Project Page（项目主页） | https://latentactionpretraining.github.io/ |
| Official GitHub（代码入口） | https://github.com/LatentActionPretraining/LAPA |
| Code Status（代码状态） | Released |
| Commit（核查版本） | 46aca51d7faebcec02d7d323bbb3820c2df07bc6 |
| Core Source（核心实现） | latent_pretraining/inference.py；latent_pretraining/deploy.py；laq/train_sthv2.py |
| Environment（依赖说明） | SimplerEnv/ManiSkill2_real2sim/pyproject.toml；SimplerEnv/ManiSkill2_real2sim/requirements.txt；SimplerEnv/ManiSkill2_real2sim/setup.py；SimplerEnv/pyproject.toml；SimplerEnv/requirements_full_install.txt；SimplerEnv/setup.py；laq/setup.py；requirements.txt |
| Training / Evaluation（训练/评估） | 已查潜动作推理、量化训练、动作部署实现。潜动作输出需要微调映射到机器人动作；不等于开箱即用机器人策略。 |
| Checkpoint（权重） | https://huggingface.co/latent-action-pretraining/LAPA-7B-openx（作者入口/说明；未验证权重文件可下载或可用性） |
| Dataset Released（数据公开） | 作者提供预训练数据入口及Something-Something V2/自定义数据转换说明；未下载 |
| Reproducibility（复现状态） | 仅静态核查公开材料；未安装、训练、推理、复现或下载权重/数据。 |
| Reading Level（阅读等级） | L1；未自动升级 |
| Checked Date（本轮核查日期） | 2026-09-18 |

Project Relevance（项目相关性分析）：VLA / Human Video / Latent Action。分类仅用于检索组织，不代表已验证可迁移到NERO/robosuite。

## C011 · FlowPolicy

| Official Facts（官方事实与核查结果） | 内容 |
| --- | --- |
| Title（标题） | FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation |
| Year / Venue（年份/会议） | 2025 / AAAI；正式主会论文：官方论文集核实 |
| CCF Level（等级） | 未填写；Pending Official Recheck |
| Official Paper（官方论文） | https://ojs.aaai.org/index.php/AAAI/article/view/33617 |
| Project Page（项目主页） | 未找到独立主页；使用作者仓库 |
| Official GitHub（代码入口） | https://github.com/zql-kk/FlowPolicy |
| Code Status（代码状态） | Released |
| Commit（核查版本） | 86d10c14972b4eab083abec9026749c340f8e5ed |
| Core Source（核心实现） | FlowPolicy/flow_policy_3d/policy/flowpolicy.py；FlowPolicy/train.py；FlowPolicy/eval.py |
| Environment（依赖说明） | FlowPolicy/setup.py；install.md；third_party/Metaworld/setup.py；third_party/gym-0.21.0/requirements.txt；third_party/gym-0.21.0/setup.py；third_party/mujoco-py-2.1.2.14/pyproject.toml；third_party/mujoco-py-2.1.2.14/requirements.dev.txt；third_party/mujoco-py-2.1.2.14/requirements.txt；third_party/mujoco-py-2.1.2.14/setup.py；third_party/pytorch3d_simplified/setup.py |
| Training / Evaluation（训练/评估） | AAAI Technical Track on Intelligent Robots，14754–14762。已查FlowPolicy类、训练与评估；README说明基准统计应取训练时记录，而独立eval脚本用于部署/推理。 |
| Checkpoint（权重） | 本轮未发现明确完整预训练策略权重入口；可按作者说明训练（作者入口/说明；未验证权重文件可下载或可用性） |
| Dataset Released（数据公开） | 提供Adroit/MetaWorld示范生成脚本与说明；未下载数据 |
| Reproducibility（复现状态） | 仅静态核查公开材料；未安装、训练、推理、复现或下载权重/数据。 |
| Reading Level（阅读等级） | L1；未自动升级 |
| Checked Date（本轮核查日期） | 2026-09-18 |

Project Relevance（项目相关性分析）：Robot Manipulation / Consistency Flow Matching / 3D Policy。分类仅用于检索组织，不代表已验证可迁移到NERO/robosuite。

## C014 · UniGraspTransformer

| Official Facts（官方事实与核查结果） | 内容 |
| --- | --- |
| Title（标题） | UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping |
| Year / Venue（年份/会议） | 2025 / CVPR；正式主会论文：官方论文集核实 |
| CCF Level（等级） | 未填写；Pending Official Recheck |
| Official Paper（官方论文） | https://openaccess.thecvf.com/content/CVPR2025/html/Wang_UniGraspTransformer_Simplified_Policy_Distillation_for_Scalable_Dexterous_Robotic_Grasping_CVPR_2025_paper.html |
| Project Page（项目主页） | https://dexhand.github.io/UniGraspTransformer/ |
| Official GitHub（代码入口） | https://github.com/microsoft/UniGraspTransformer |
| Code Status（代码状态） | Released |
| Commit（核查版本） | 58753be89024267bb2348d0bf9a224fadbe5f35a |
| Core Source（核心实现） | dexgrasp/run_offline.py；dexgrasp/run_online.py |
| Environment（依赖说明） | install.sh；pytorch_kinematics/setup.py；setup.py |
| Training / Evaluation（训练/评估） | 已查在线RL和离线蒸馏实现及安装/训练/评估说明。代码Released；IsaacGym4通用策略权重仍Coming Soon，不代表代码也未发布。 |
| Checkpoint（权重） | IsaacGym3权重说明及IsaacGym4专用策略入口存在；IsaacGym4通用策略未发布（作者入口/说明；未验证权重文件可下载或可用性） |
| Dataset Released（数据公开） | 提供资产/抓取初始化数据链接和生成轨迹步骤；未下载 |
| Reproducibility（复现状态） | 仅静态核查公开材料；未安装、训练、推理、复现或下载权重/数据。 |
| Reading Level（阅读等级） | L1；未自动升级 |
| Checked Date（本轮核查日期） | 2026-09-18 |

Project Relevance（项目相关性分析）：Dexterous Hand / Policy Distillation / Generalization。分类仅用于检索组织，不代表已验证可迁移到NERO/robosuite。

## C015 · VLM Scaffolding

| Official Facts（官方事实与核查结果） | 内容 |
| --- | --- |
| Title（标题） | Scaffolding Dexterous Manipulation with Vision-Language Models |
| Year / Venue（年份/会议） | 2025 / NeurIPS；正式主会论文：官方论文集核实 |
| CCF Level（等级） | 未填写；Pending Official Recheck |
| Official Paper（官方论文） | https://proceedings.neurips.cc/paper_files/paper/2025/hash/862644b156e51c35dea5a7446d640b14-Abstract-Conference.html |
| Project Page（项目主页） | https://sites.google.com/view/dexterous-vlm-scaffolding |
| Official GitHub（代码入口） | https://github.com/vdebakker/vlm-scaffolding |
| Code Status（代码状态） | Released |
| Commit（核查版本） | 496809c00b9c9dc0b9cb8616d3e28b299324dd22 |
| Core Source（核心实现） | train/train.py；train/eval.py；build_dataset/build_dataset.py |
| Environment（依赖说明） | requirements.txt |
| Training / Evaluation（训练/评估） | 已查轨迹生成、RL训练和评估；README提供真机ROS部署说明。依赖外部Gemini服务、仿真器及机器人环境，未运行。 |
| Checkpoint（权重） | 本轮未发现完整预训练策略包公开链接（作者入口/说明；未验证权重文件可下载或可用性） |
| Dataset Released（数据公开） | 公开数据生成实现与任务资产；不等于所有论文轨迹均已提供 |
| Reproducibility（复现状态） | 仅静态核查公开材料；未安装、训练、推理、复现或下载权重/数据。 |
| Reading Level（阅读等级） | L1；未自动升级 |
| Checked Date（本轮核查日期） | 2026-09-18 |

Project Relevance（项目相关性分析）：Dexterous Hand / Residual RL / VLM Planning。分类仅用于检索组织，不代表已验证可迁移到NERO/robosuite。

## C016 · VideoVLA

| Official Facts（官方事实与核查结果） | 内容 |
| --- | --- |
| Title（标题） | VideoVLA: Video Generators Can Be Generalizable Robot Manipulators |
| Year / Venue（年份/会议） | 2025 / NeurIPS；正式主会论文：官方论文集核实 |
| CCF Level（等级） | 未填写；Pending Official Recheck |
| Official Paper（官方论文） | https://proceedings.neurips.cc/paper_files/paper/2025/hash/89a3b655a8b68ae1c76b768152c9c19d-Abstract-Conference.html |
| Project Page（项目主页） | https://videovla-nips2025.github.io/ |
| Official GitHub（代码入口） | https://github.com/VideoVLA-Project/VideoVLA |
| Code Status（代码状态） | Partial |
| Commit（核查版本） | 05b5cca7d4ec32e786b7e10dcbfbf5926637b293 |
| Core Source（核心实现） | dit_video_concat_withact.py；sample_video_action.py；diffusion_video.py |
| Environment（依赖说明） | requirements.txt |
| Training / Evaluation（训练/评估） | 已查动作DiT、扩散引擎、sample_video_action.py。旧Coming soon文字在HTML注释中，不能当作当前状态；训练/机器人benchmark完整流水线本轮未确认，标Partial待运行条件复核。 |
| Checkpoint（权重） | 项目页提供VideoVLA模型链接；README还要求CogVideo的T5与VAE；未下载（作者入口/说明；未验证权重文件可下载或可用性） |
| Dataset Released（数据公开） | README未提供完整论文训练数据准备流程 |
| Reproducibility（复现状态） | 仅静态核查公开材料；未安装、训练、推理、复现或下载权重/数据。 |
| Reading Level（阅读等级） | L1；未自动升级 |
| Checked Date（本轮核查日期） | 2026-09-18 |

Project Relevance（项目相关性分析）：VLA / Video-Action Model / Generalization。分类仅用于检索组织，不代表已验证可迁移到NERO/robosuite。

## C019 · DextER

| Official Facts（官方事实与核查结果） | 内容 |
| --- | --- |
| Title（标题） | DextER: Language-driven Dexterous Grasp Generation with Embodied Reasoning |
| Year / Venue（年份/会议） | 2026 / CVPR；正式主会论文：官方论文集核实 |
| CCF Level（等级） | 未填写；Pending Official Recheck |
| Official Paper（官方论文） | https://openaccess.thecvf.com/content/CVPR2026/html/Lee_DextER_Language-driven_Dexterous_Grasp_Generation_with_Embodied_Reasoning_CVPR_2026_paper.html |
| Project Page（项目主页） | https://junha-l.github.io/dexter/ |
| Official GitHub（代码入口） | https://github.com/junha-l/dexter |
| Code Status（代码状态） | Released |
| Commit（核查版本） | fd60c6ccbd7f4197ed431d5113007b8a1aaf9c3d |
| Core Source（核心实现） | src/dexter/models/dexter/modeling_dexter.py；scripts/train.py；scripts/test.py |
| Environment（依赖说明） | benchmark/dexgys/isaacgym-env/pyproject.toml；pyproject.toml；thirdparty/csdf/pyproject.toml；thirdparty/csdf/setup.py；thirdparty/pytorch_kinematics/pyproject.toml；thirdparty/pytorch_kinematics/setup.py |
| Training / Evaluation（训练/评估） | CVF页面直接访问成功；已查核心模型、训练和测试实现。数据说明有2026-07-22修正，后续应使用修正版数据。 |
| Checkpoint（权重） | https://huggingface.co/junhalee/dexter-qwen2.5-0.5B-dexgys（作者入口/说明；未验证权重文件可下载或可用性） |
| Dataset Released（数据公开） | 作者提供预处理数据：https://huggingface.co/datasets/EunhaPark/project_dexter；未下载 |
| Reproducibility（复现状态） | 仅静态核查公开材料；未安装、训练、推理、复现或下载权重/数据。 |
| Reading Level（阅读等级） | L1；未自动升级 |
| Checked Date（本轮核查日期） | 2026-09-18 |

Project Relevance（项目相关性分析）：Dexterous Hand / Contact Reasoning / Language-guided Grasp。分类仅用于检索组织，不代表已验证可迁移到NERO/robosuite。

## C020 · SpatialVLA

| Official Facts（官方事实与核查结果） | 内容 |
| --- | --- |
| Title（标题） | SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models |
| Year / Venue（年份/会议） | 2025 / RSS；正式主会论文：官方论文集核实 |
| CCF Level（等级） | 未填写；Pending Official Recheck |
| Official Paper（官方论文） | https://www.roboticsproceedings.org/rss21/p011.html |
| Project Page（项目主页） | https://spatialvla.github.io/ |
| Official GitHub（代码入口） | https://github.com/SpatialVLA/SpatialVLA |
| Code Status（代码状态） | Released |
| Commit（核查版本） | 18fd74b2a633ec8d9ec7aadcd803969555cc9fbd |
| Core Source（核心实现） | model/modeling_spatialvla.py；train/spatialvla_finetune.py |
| Environment（依赖说明） | pyproject.toml；requirements.txt |
| Training / Evaluation（训练/评估） | 正式venue为RSS 2025，不是CVPR/ICML。RSS当前CCF目录等级未成功从官方核实，故仅作扩展候选；不擅自标A或Not_CCF_A。 |
| Checkpoint（权重） | https://huggingface.co/collections/IPEC-COMMUNITY/foundation-vision-language-action-model-6795eb96a9c661f90236acbb（作者入口/说明；未验证权重文件可下载或可用性） |
| Dataset Released（数据公开） | 提供OXE处理与自定义数据说明；未核实全部训练混合的再发布范围 |
| Reproducibility（复现状态） | 仅静态核查公开材料；未安装、训练、推理、复现或下载权重/数据。 |
| Reading Level（阅读等级） | L1；未自动升级 |
| Checked Date（本轮核查日期） | 2026-09-18 |

Project Relevance（项目相关性分析）：VLA / Spatial Representation / Action Tokenization。分类仅用于检索组织，不代表已验证可迁移到NERO/robosuite。

## Admission Checklist（后续准入）

1. 完成CCF官方第七版等级核查；RSS不得凭领域重要性自动认定A。
2. 对Partial补齐原论文对应版本、权重/数据与可运行核心方法证据。
3. 补核RoboMamba的作者代码归属链及3D-VLA项目页访问问题。
4. 人工检查后才增量加入Papers；正式会议版优先，保持L1，独立记录阅读和复现进度。
