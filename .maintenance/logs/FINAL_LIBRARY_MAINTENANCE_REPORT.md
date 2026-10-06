# 最终文献库维护报告

日期：2026-09-25。统计范围仅限 `02_论文/` 下的 canonical paper cards；未将 首页、README、阅读笔记、分类索引等计入。

- Canonical papers: 134
- Citation resolved: 113
- Citation unresolved: 21
- Citation coverage: 84.33%
- OpenAlex: 96
- Semantic Scholar: 7
- Crossref: 10
- Manual fallback: 0
- PDF available locally: 130 / 134
- PDF missing: 4
- PDF redistributable: 7
- PDF tracked by Git: 7
- PDF local only: 123
- Total PDF size: 1,255,002,415 bytes (1.169 GiB)
- Broken links fixed: 6（上一轮已确认的 404 外链）
- Broken wikilinks: 0
- Duplicate cards: 0
- Excel synchronized: Yes（163 条记录、134 篇主卡的引用量、来源、来源链接、日期差异 0）

## 引用量补全与来源

- Canonical papers: 134
- Citation numeric: 113 / 134
- Coverage: 84.33%
- Citation missing: 21
- Google Scholar: 0
- Semantic Scholar: 7
- OpenAlex: 96
- Publisher / Other（Crossref）: 10
- Zero-citation papers: 39
- 四字段存在率：134 / 134
- 有数字的记录中来源链接覆盖率：113 / 113
- 全库有效来源链接覆盖率：113 / 134

本轮 Crossref 新增 10 条精确作品匹配；未将服务未收录视为 0。Google Scholar 当前显示验证码，未绕过；Semantic Scholar API 返回 HTTP 429；OpenAlex 明确返回共享 IP 免费日额度耗尽，需在其午夜 UTC 重置后或使用账户 API key 才能继续查询。21 篇仍无可靠 citation 数字，不能如实报告 134 / 134。

## 一致性与安全检查

- 134 张主卡路径与更新前基线一致；每卡仅有一组引用量、来源和 2026-09-25 查询日期。
- 130 份本地 PDF 已通过存在性、大小、`%PDF` 文件头、解析器、页数和 SHA256 校验；130 张主卡的本地 PDF 链接均可在当前本地文献库打开。
- 主卡 wiki 链接断链 0；快速摘要与深度阅读章节相对上一轮开始时逐字未改；原有分类、文件名和 Citation Graph 内容未删改。
- Excel 的 4 个业务工作表行列数不变，163 条记录与论文卡的 citation 字段一致；新增可用的在线 PDF 到原来为空的 `Fulltext URL` 单元格共 151 处；既有非空全文链接未覆盖。
- Git LFS 已安装，7 份确认 CC BY 4.0 的 arXiv PDF 共 36,667,940 bytes 由 LFS 管理；其余 PDF 继续被 `.gitignore` 排除。
- 公开可下载不等于获得第三方再托管权。CVF 页面保留权利人限制，arXiv 默认非独占分发许可也不自动授权本库公开再分发；逐条证据见 PDF 许可审计表。
- OpenAlex、Semantic Scholar 与 Crossref 为不同来源的独立计数，不合并不同版本，也未为达到覆盖率采用模糊标题匹配。Semantic Scholar API 在本次复查中对部分请求返回 429；已有匹配保留其原有核验记录。

## 未解决引用量

逐篇身份、现有论文入口和人工检索链接见 [[CITATION_MANUAL_REVIEW]]。

- [[Actions as Language - Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting]] — Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting
- [[DiffusionVLA - Scaling Robot Foundation Models via Unified Diffusion and Autoregression]] — DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression
- [[RoboMonkey - Scaling Test-Time Sampling and Verification for Vision-Language-Action Models]] — RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models
- [[SimpleVLA-RL - Scaling VLA Training via Reinforcement Learning]] — SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning
- [[Mobile ALOHA - Learning Bimanual Mobile Manipulation Using Low-Cost Whole-Body Teleoperation]] — Mobile ALOHA: Learning Bimanual Mobile Manipulation Using Low-Cost Whole-Body Teleoperation
- [[SafeBimanual - Diffusion-based trajectory optimization for safe bimanual manipulation]] — SafeBimanual: Diffusion-based trajectory optimization for safe bimanual manipulation
- [[DexUMI - Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation]] — DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation
- [[Rapidly Adapting Policies to the Real-World via Simulation-Guided Fine-Tuning]] — Rapidly Adapting Policies to the Real-World via Simulation-Guided Fine-Tuning
- [[Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids]] — Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids
- [[Sim2Real-VLA - Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation]] — Sim2Real-VLA: Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation
- [[Action Chunking and Data Augmentation Yield Exponential Improvements in Behavior Cloning for Continuous Spaces]] — Action Chunking and Data Augmentation Yield Exponential Improvements in Behavior Cloning for Continuous Spaces
- [[AutoCGP - Closed-Loop Concept-Guided Policies from Unlabeled Demonstrations]] — AutoCGP: Closed-Loop Concept-Guided Policies from Unlabeled Demonstrations
- [[Demystifying Robot Diffusion Policies - Action Memorization and a Simple Lookup Table Alternative]] — Demystifying Robot Diffusion Policies: Action Memorization and a Simple Lookup Table Alternative
- [[VidBot - Learning Generalizable 3D Actions from In-the-Wild 2D Human Videos for Zero-Shot Robotic Manipulation]] — VidBot: Learning Generalizable 3D Actions from In-the-Wild 2D Human Videos for Zero-Shot Robotic Manipulation
- [[Latent Action Pretraining from Videos]] — Latent Action Pretraining from Videos
- [[ManiWAV - Learning Robot Manipulation from In-the-Wild Audio-Visual Data]] — ManiWAV: Learning Robot Manipulation from In-the-Wild Audio-Visual Data
- [[A Survey of Robot Learning for Bimanual Manipulation]] — A Survey of Robot Learning for Bimanual Manipulation
- [[Dexterous Hand towards Intelligent Manufacturing - A Review of Technologies, Trends, and Potential Applications]] — Dexterous Hand towards Intelligent Manufacturing: A Review of Technologies, Trends, and Potential Applications
- [[AdaManip - Adaptive Articulated Object Manipulation Environments and Policy Learning]] — AdaManip: Adaptive Articulated Object Manipulation Environments and Policy Learning
- [[DexH2R - A Benchmark for Dynamic Dexterous Grasping in Human-to-Robot Handover]] — DexH2R: A Benchmark for Dynamic Dexterous Grasping in Human-to-Robot Handover
- [[VTDexManip - A Dataset and Benchmark for Visual-tactile Pretraining and Dexterous Manipulation with Reinforcement Learning]] — VTDexManip: A Dataset and Benchmark for Visual-tactile Pretraining and Dexterous Manipulation with Reinforcement Learning

## 缺失 PDF

以下仅保留论文或资料入口，不将网页伪装为 PDF：

- [[Real-Time Coordination of Multiple Robotic Arms With Reactive Trajectory Modulation]] — https://ieeexplore.ieee.org/document/10758213/
- [[Evaluating the Effect of State and Action Selection on In-Hand Manipulation Performance for Transferability]] — https://ieeexplore.ieee.org/document/10955245/
- [[A Survey of Robot Learning for Bimanual Manipulation]] — https://github.com/Destiny000621/awesome-bimanual-robot-learning/blob/main/SURVEY.md
- [[Dexterous Hand towards Intelligent Manufacturing - A Review of Technologies, Trends, and Potential Applications]] — https://www.sciencedirect.com/science/article/pii/S0736584525000754

## 本地保留、未上传 GitHub 的 PDF

下列 PDF 目前无法确认允许公开再托管，或带有需要额外确认的条件。在线原始来源与逐项许可说明见 [[00_论文池/PDFs/PDF_LICENSE_AUDIT.csv]]。

- 00_论文池/PDFs/01_VLA/3D-VLA.pdf — Unconfirmed
- 00_论文池/PDFs/01_VLA/Actions_as_Language.pdf — Unconfirmed
- 00_论文池/PDFs/01_VLA/BridgeVLA.pdf — Unconfirmed
- 00_论文池/PDFs/01_VLA/CoT-VLA.pdf — Unconfirmed
- 00_论文池/PDFs/01_VLA/DiffusionVLA.pdf — Unconfirmed
- 00_论文池/PDFs/01_VLA/MoManipVLA.pdf — Unconfirmed
- 00_论文池/PDFs/01_VLA/Octo.pdf — Unconfirmed
- 00_论文池/PDFs/01_VLA/OpenVLA.pdf — Unconfirmed
- 00_论文池/PDFs/01_VLA/ReconVLA.pdf — Unconfirmed
- 00_论文池/PDFs/01_VLA/RoboGround.pdf — Unconfirmed
- 00_论文池/PDFs/01_VLA/RoboMamba.pdf — Unconfirmed
- 00_论文池/PDFs/01_VLA/RoboMonkey.pdf — Unconfirmed
- 00_论文池/PDFs/01_VLA/SayCan.pdf — arXiv non-exclusive distribution
- 00_论文池/PDFs/01_VLA/SimpleVLA-RL.pdf — Unconfirmed
- 00_论文池/PDFs/01_VLA/SP-VLA.pdf — Unconfirmed
- 00_论文池/PDFs/01_VLA/SpatialVLA.pdf — Unconfirmed
- 00_论文池/PDFs/01_VLA/TraceVLA.pdf — Unconfirmed
- 00_论文池/PDFs/01_VLA/VideoVLA.pdf — Unconfirmed
- 00_论文池/PDFs/01_VLA/VLA-Cache.pdf — Unconfirmed
- 00_论文池/PDFs/02_机器人操作/Dreamitate.pdf — Unconfirmed
- 00_论文池/PDFs/02_机器人操作/ManipLLM.pdf — Unconfirmed
- 00_论文池/PDFs/02_机器人操作/RobotSmith.pdf — Unconfirmed
- 00_论文池/PDFs/02_机器人操作/SPIN.pdf — Unconfirmed
- 00_论文池/PDFs/02_机器人操作/VidMan.pdf — Unconfirmed
- 00_论文池/PDFs/03_双臂协作/2HandedAfforder.pdf — Unconfirmed
- 00_论文池/PDFs/03_双臂协作/ALOHA_Unleashed.pdf — Unconfirmed
- 00_论文池/PDFs/03_双臂协作/AnyBimanual.pdf — Unconfirmed
- 00_论文池/PDFs/03_双臂协作/BimArt.pdf — Unconfirmed
- 00_论文池/PDFs/03_双臂协作/COMBO-Grasp.pdf — Unconfirmed
- 00_论文池/PDFs/03_双臂协作/Diffusion-Based_Imaginative_Coordination_for_Bimanual_Manipulation.pdf — Unconfirmed
- 00_论文池/PDFs/03_双臂协作/Forecasting_Bimanual_Object_Manipulation_Sequences_from_Unimanual_Observations.pdf — Unconfirmed
- 00_论文池/PDFs/03_双臂协作/HumanoidGen.pdf — Unconfirmed
- 00_论文池/PDFs/03_双臂协作/Learning_Diverse_Bimanual_Dexterous_Manipulation_Skills_from_Human_Demonstrations.pdf — Unconfirmed
- 00_论文池/PDFs/03_双臂协作/ManipTrans.pdf — Unconfirmed
- 00_论文池/PDFs/03_双臂协作/Mobile_ALOHA.pdf — Unconfirmed
- 00_论文池/PDFs/03_双臂协作/PPI_Bimanual.pdf — Unconfirmed
- 00_论文池/PDFs/03_双臂协作/RDT-1B.pdf — Unconfirmed
- 00_论文池/PDFs/03_双臂协作/Rethinking_Bimanual_Robotic_Manipulation_Learning_with_Decoupled_Interaction_Framework.pdf — Unconfirmed
- 00_论文池/PDFs/03_双臂协作/SafeBimanual.pdf — Unconfirmed
- 00_论文池/PDFs/03_双臂协作/TwinVLA.pdf — Unconfirmed
- 00_论文池/PDFs/03_双臂协作/VoxAct-B.pdf — Unconfirmed
- 00_论文池/PDFs/03_双臂协作/YOTO.pdf — Unconfirmed
- 00_论文池/PDFs/04_灵巧操作/Cross-Embodiment_Dexterous_Grasping_with_Reinforcement_Learning.pdf — Unconfirmed
- 00_论文池/PDFs/04_灵巧操作/DexHandDiff.pdf — Unconfirmed
- 00_论文池/PDFs/04_灵巧操作/DextER.pdf — Unconfirmed
- 00_论文池/PDFs/04_灵巧操作/Dexterous_Grasp_Transformer.pdf — Unconfirmed
- 00_论文池/PDFs/04_灵巧操作/Dexterous_Manipulation_Transfer_via_Progressive_Kinematic-Dynamic_Alignment.pdf — Unconfirmed
- 00_论文池/PDFs/04_灵巧操作/DexTrack.pdf — Unconfirmed
- 00_论文池/PDFs/04_灵巧操作/DexUMI.pdf — Unconfirmed
- 00_论文池/PDFs/04_灵巧操作/DexVLG.pdf — Unconfirmed
- 00_论文池/PDFs/04_灵巧操作/LatentHOI.pdf — Unconfirmed
- 00_论文池/PDFs/04_灵巧操作/Learning_Object-Centric_Motion_Priors_from_Human_for_Robotic_Dexterous_Manipulation.pdf — Unconfirmed
- 00_论文池/PDFs/04_灵巧操作/Scaffolding_Dexterous_Manipulation_with_Vision-Language_Models.pdf — Unconfirmed
- 00_论文池/PDFs/04_灵巧操作/Towards_Affordance-Aware_Robotic_Dexterous_Grasping_with_Human-like_Priors.pdf — Unconfirmed
- 00_论文池/PDFs/04_灵巧操作/UniDex.pdf — Unconfirmed
- 00_论文池/PDFs/04_灵巧操作/UniGraspTransformer.pdf — Unconfirmed
- 00_论文池/PDFs/05_仿真到真实_Sim2Real/Generalizable_Domain_Adaptation_for_Sim-and-Real_Policy_Co-Training.pdf — Unconfirmed
- 00_论文池/PDFs/05_仿真到真实_Sim2Real/Rapidly_Adapting_Policies_to_the_Real-World_via_Simulation-Guided_Fine-Tuning.pdf — Unconfirmed
- 00_论文池/PDFs/05_仿真到真实_Sim2Real/Sim-to-Real_Reinforcement_Learning_for_Vision-Based_Dexterous_Manipulation_on_Humanoids.pdf — Unconfirmed
- 00_论文池/PDFs/05_仿真到真实_Sim2Real/Sim2Real-VLA.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/3D_Diffuser_Actor.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/Action_Chunking_and_Data_Augmentation_Yield_Exponential_Improvements_in_Behavior_Cloning_f.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/AR-VRM.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/AutoCGP.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/BAKU.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/Bidirectional_Decoding.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/Demystifying_Robot_Diffusion_Policies_Action_Memorization_and_a_Simple_Lookup_Table_Altern.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/Dynamic_Test-Time_Compute_Scaling_in_Control_Policy_Difficulty-Aware_Stochastic_Interpolan.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/EquiBot.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/Equivariant_Diffusion_Policy.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/ET-SEED.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/FlowPolicy.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/FoAM.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/Force_Matched_Visuotactile_IL.pdf — arXiv non-exclusive distribution
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/FreqPolicy.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/Hierarchical_Diffusion_Policy_for_Kinematics-Aware_Multi-Task_Robotic_Manipulation.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/Learning_Diffusion_Policy_from_Primitive_Skills_for_Robot_Manipulation.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/Learning_Robotic_Manipulation_Policies_from_Point_Clouds_with_Conditional_Flow_Matching.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/MILES.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/MimicFunc.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/PointMapPolicy.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/Real-Time_Robot_Execution_with_Masked_Action_Chunking.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/Robot_Policy_Learning_with_Temporal_Optimal_Transport_Reward.pdf — Unconfirmed
- 00_论文池/PDFs/06_扩散模型_流匹配_IL_RL/Text-Aware_Diffusion_for_Policy_Learning.pdf — Unconfirmed
- 00_论文池/PDFs/07_泛化与长程任务/Closed-Loop_Visuomotor_Control_with_Generative_Expectation_for_Robotic_Manipulation.pdf — Unconfirmed
- 00_论文池/PDFs/07_泛化与长程任务/Enhancing_LLM_Planning_for_Robotics_Manipulation_through_Hierarchical_Procedural_Knowledge.pdf — Unconfirmed
- 00_论文池/PDFs/07_泛化与长程任务/Gentle_Manipulation_Policy_Learning_via_Demonstrations_from_VLM_Planned_Atomic_Skills.pdf — Unconfirmed
- 00_论文池/PDFs/07_泛化与长程任务/GMAP.pdf — Unconfirmed
- 00_论文池/PDFs/07_泛化与长程任务/HAMSTER.pdf — Unconfirmed
- 00_论文池/PDFs/07_泛化与长程任务/Instruction-Augmented_Long-Horizon_Planning_Embedding_Grounding_Mechanisms_in_Embodied_Mob.pdf — Unconfirmed
- 00_论文池/PDFs/07_泛化与长程任务/Mitigating_the_Human-Robot_Domain_Discrepancy_in_Visual_Pre-training_for_Robotic_Manipulat.pdf — Unconfirmed
- 00_论文池/PDFs/07_泛化与长程任务/OWMM-Agent.pdf — Unconfirmed
- 00_论文池/PDFs/07_泛化与长程任务/Policy_Decorator.pdf — Unconfirmed
- 00_论文池/PDFs/07_泛化与长程任务/RAM.pdf — Unconfirmed
- 00_论文池/PDFs/07_泛化与长程任务/RGMP.pdf — Unconfirmed
- 00_论文池/PDFs/07_泛化与长程任务/Self-Correcting_Robot_Manipulation_via_Gaussian-Splatted_Foresight.pdf — Unconfirmed
- 00_论文池/PDFs/07_泛化与长程任务/SPIRE.pdf — Unconfirmed
- 00_论文池/PDFs/07_泛化与长程任务/TASTE-Rob.pdf — Unconfirmed
- 00_论文池/PDFs/07_泛化与长程任务/Think_Small,_Act_Big.pdf — Unconfirmed
- 00_论文池/PDFs/07_泛化与长程任务/UniDomain.pdf — Unconfirmed
- 00_论文池/PDFs/07_泛化与长程任务/VidBot.pdf — Unconfirmed
- 00_论文池/PDFs/08_数据与遥操作/DexCap.pdf — Unconfirmed
- 00_论文池/PDFs/08_数据与遥操作/DynScene.pdf — Unconfirmed
- 00_论文池/PDFs/08_数据与遥操作/Latent_Action_Pretraining_from_Videos.pdf — Unconfirmed
- 00_论文池/PDFs/08_数据与遥操作/ManiWAV.pdf — Unconfirmed
- 00_论文池/PDFs/08_数据与遥操作/OPEN_TEACH.pdf — Unconfirmed
- 00_论文池/PDFs/08_数据与遥操作/Robo2VLM.pdf — Unconfirmed
- 00_论文池/PDFs/09_综述/A_Survey_of_Demonstration_Learning.pdf — CC BY-NC-ND 4.0
- 00_论文池/PDFs/09_综述/A_Survey_of_Embodied_Learning_for_Object-Centric_Robotic_Manipulation.pdf — Unconfirmed
- 00_论文池/PDFs/09_综述/A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective.pdf — arXiv non-exclusive distribution
- 00_论文池/PDFs/09_综述/A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI.pdf — arXiv non-exclusive distribution
- 00_论文池/PDFs/09_综述/What_Foundation_Models_can_Bring_for_Robot_Learning_in_Manipulation_A_Survey.pdf — arXiv non-exclusive distribution
- 00_论文池/PDFs/10_基准测试与数据集/AdaManip.pdf — Unconfirmed
- 00_论文池/PDFs/10_基准测试与数据集/BiGym.pdf — Unconfirmed
- 00_论文池/PDFs/10_基准测试与数据集/DexH2R.pdf — Unconfirmed
- 00_论文池/PDFs/10_基准测试与数据集/DROID.pdf — Unconfirmed
- 00_论文池/PDFs/10_基准测试与数据集/Point_Cloud_Matters.pdf — Unconfirmed
- 00_论文池/PDFs/10_基准测试与数据集/RoboCasa.pdf — Unconfirmed
- 00_论文池/PDFs/10_基准测试与数据集/RoboTwin.pdf — Unconfirmed
- 00_论文池/PDFs/10_基准测试与数据集/SurgicAI.pdf — Unconfirmed
- 00_论文池/PDFs/10_基准测试与数据集/TACO.pdf — Unconfirmed
- 00_论文池/PDFs/10_基准测试与数据集/THE_COLOSSEUM.pdf — Unconfirmed
- 00_论文池/PDFs/10_基准测试与数据集/VTDexManip.pdf — Unconfirmed

## 仍需人工决定

1. 对 21 篇无可靠引用量的论文，若可提供官方 DOI、arXiv 或作者页面，可进一步人工核对。
2. 对 4 条缺失 PDF 的文献，检查机构访问权限、作者自存档及其中一条仅为 GitHub SURVEY.md 的资料身份。
3. 对 123 份仅本地保存的 PDF，若要上传公开仓库，需要逐份取得明确的再分发许可；其中一份 arXiv 页面为 CC BY-NC-ND 4.0，因再托管条件未确认，仍保留本地。
4. 部分热门论文的 OpenAlex 计数可能低于其他平台，源间覆盖口径不同；若需要特定平台口径，可手工交叉核验，不能相加。

## 相关文件

- [[PRE_FINAL_UPDATE_GIT_STATUS]]：修改前 Git 状态。
- [[CITATION_MANUAL_REVIEW]]：未解决引用量、论文身份和人工检索入口。
- [[00_论文池/PDFs/PDF_LICENSE_AUDIT.csv]]：逐份许可与 Git 状态。
- [[00_论文池/PDFs/PDF_INDEX.csv]]：PDF、DOI、arXiv、校验值、页数与在线链接。
- [[CITATION_LINK_UPDATE_REPORT]]：上一轮修复外链的记录。
