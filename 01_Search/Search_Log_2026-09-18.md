# Search Session（检索记录） · 2026-09-18

## Search Scope（检索范围）

2024–2026；目标为当前CCF官方A类主会Full / Regular Paper（完整正式论文）；Robot Manipulation（机器人操作）、Vision-Language-Action / VLA（视觉-语言-动作模型）、Dexterous Hand（灵巧手）、Bimanual Manipulation（双臂操作）；要求实际官方代码。只检索、静态核查和增量登记，未精读、未复现、未下载论文PDF/权重/数据，未clone任何论文代码。

本轮审计范围为25个论文条目：20篇此前不在Papers/Rejected的新候选、1篇Workshop竞赛报告、4篇已有论文的去重复查。该数不包含所有搜索引擎命中或正文参考文献。正式入库0，待复核16，新Rejected记录9（4个代码门槛、1个Workshop、4个Duplicate）。未达到15–20篇全部合格目标，原因是CCF官方等级硬门槛未完成，未降低标准。

## Search Queries（实际检索式）

下列为本轮实际提交的检索式，非预设示例；带错误venue的检索只用于发现，最终以论文集纠正。

1. `"bimanual manipulation" "imitation learning" ICLR 2025 code`
2. `"vision language action" "robot manipulation" CVPR 2025 code`
3. `"dexterous manipulation" generalization CVPR 2025 code`
4. `"robot manipulation" "flow matching" 2025 code`
5. `"RDT-1B" "TwinVLA" github`
6. `"BridgeVLA" "VLA-Cache" github`
7. `"RoboTwin" "CVPR 2025" github`
8. `"robot manipulation" "human video" "ICLR 2025"`
9. `BridgeVLA official github`
10. `VLA-Cache official github`
11. `RDT-1B official github`
12. `FlowPolicy AAAI github`
13. `DiffusionVLA official github DiVLA`
14. `AffordDexGrasp github`
15. `DexVLG github`
16. `UniGraspTransformer github`
17. `"TraceVLA" official github`
18. `"LAPA" "Latent Action" github`
19. `"RoboMamba" github`
20. `"VideoVLA" github`
21. `"AffordDexGrasp" project github weiyilin`
22. `"VideoVLA" "NeurIPS" github`
23. `"Scaffolding Dexterous Manipulation" github`
24. `"OmniManip" "CoA-VLA" github`
25. `"3D-VLA" official code github`
26. `"CoA-VLA" github`
27. `"OmniManip" github`
28. `"Hi Robot" code released`
29. `site:openaccess.thecvf.com "RoboTwin" "CVPR2025"`
30. `site:openaccess.thecvf.com "SpatialVLA"`
31. `site:iclr.cc "TwinVLA"`
32. `"DextER" "Language-driven" github`
33. `site:ccf.org.cn "第七版" "pdf"`
34. `site:ccf.org.cn "ICLR" "A类"`
35. `site:ccf.org.cn 2026 推荐 国际学术会议 期刊 目录 第七版 下载`
36. `site:openreview.net "RDT-1B" "ICLR 2025"`
37. `site:openaccess.thecvf.com "dexterous" "2025" "grasp"`
38. `site:proceedings.neurips.cc "2025" "bimanual"`
39. `"RoboTwin: Dual-Arm Robot Benchmark" CVPR official`
40. `"SpatialVLA: Exploring Spatial Representations" ICML 2025`
41. `site:proceedings.iclr.cc/paper_files/paper/2026 "TwinVLA"`
42. `"robot manipulation" "failure recovery" "2025" "ICLR"`
43. `"robot manipulation" "long horizon" "2026" "CVPR"`
44. `"3D manipulation" "data efficiency" "NeurIPS 2025"`
45. `site:roboticsproceedings.org "SpatialVLA"`
46. `"OmniManip" "official" "github" code`
47. `"Hi Robot" "official" "github" code`
48. `"robot manipulation" "diffusion policy" "AAAI" 2025 FlowPolicy`

另使用ICLR官方站内检索：https://proceedings.iclr.cc/papers/search?q=TwinVLA ，由此定位TwinVLA 2026正式论文条目。

## Sources（实际访问的来源）

CCF官方入口：https://www.ccf.org.cn/Academic_Evaluation/By_category/ 、https://www.ccf.org.cn/Academic_Evaluation/AI/ 。网页工具返回405；直接访问返回HTTP 200但内容为验证码页面，并非目录正文；浏览器导航超时。只看到官方发布公告的检索摘要，不足以核验每个会议等级。未用博客、第三方PDF或旧榜单替代。

本地参考仓库仅阅读“主题检索入口.md”作为关键词线索，未采用其中内容认定论文/代码/等级。

| 论文 | 官方论文集 | 实际访问的项目页 | 代码入口 |
| --- | --- | --- | --- |
| RDT-1B | https://proceedings.iclr.cc/paper_files/paper/2025/hash/49f80e4d2471ad4f2edf4f5f1ab62339-Abstract-Conference.html | https://rdt-robotics.github.io/rdt-robotics/ | https://github.com/thu-ml/RoboticsDiffusionTransformer |
| TwinVLA | https://proceedings.iclr.cc/paper_files/paper/2026/hash/65475a59e2a2cb707c9462e8a308e980-Abstract-Conference.html | https://jellyho.github.io/TwinVLA/ | https://github.com/jellyho/TwinVLA |
| RoboTwin | https://openaccess.thecvf.com/content/CVPR2025/html/Mu_RoboTwin_Dual-Arm_Robot_Benchmark_with_Generative_Digital_Twins_CVPR_2025_paper.html | https://robotwin-platform.github.io/ | https://github.com/RoboTwin-Platform/RoboTwin/tree/RoboTwin-1.0 |
| BridgeVLA | https://proceedings.neurips.cc/paper_files/paper/2025/hash/5c1a8aa04c1a2cf5013f28831870dafa-Abstract-Conference.html | https://bridgevla.github.io/ | https://github.com/BridgeVLA/BridgeVLA/tree/bridgevla |
| VLA-Cache | https://proceedings.neurips.cc/paper_files/paper/2025/hash/f062da1973ac9ac61fc6d44dd7fa309f-Abstract-Conference.html | https://vla-cache.github.io/ | https://github.com/siyuhsu/vla-cache |
| DiffusionVLA | https://proceedings.mlr.press/v267/wen25g.html | https://diffusion-vla.github.io/ | https://github.com/juruobenruo/DexVLA |
| 3D-VLA | https://proceedings.mlr.press/v235/zhen24a.html | https://vis-www.cs.umass.edu/3dvla/ | https://github.com/UMass-Embodied-AGI/3D-VLA |
| RoboMamba | https://proceedings.neurips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html | https://sites.google.com/view/robomamba-web | https://github.com/lmzpai/roboMamba |
| TraceVLA | https://proceedings.iclr.cc/paper_files/paper/2025/hash/8667f264f88c7938a73a53ab01eb1327-Abstract-Conference.html | https://tracevla.github.io/ | https://github.com/umd-huang-lab/tracevla |
| LAPA | https://proceedings.iclr.cc/paper_files/paper/2025/hash/45d74e190008c7bff2845ffc8e3facd3-Abstract-Conference.html | https://latentactionpretraining.github.io/ | https://github.com/LatentActionPretraining/LAPA |
| FlowPolicy | https://ojs.aaai.org/index.php/AAAI/article/view/33617 | 未找到独立项目页 | https://github.com/zql-kk/FlowPolicy |
| AffordDexGrasp | https://openaccess.thecvf.com/content/ICCV2025/html/Wei_AffordDexGrasp_Open-set_Language-guided_Dexterous_Grasp_with_Generalizable-Instructive_Affordance_ICCV_2025_paper.html | https://isee-laboratory.github.io/AffordDexGrasp/ | 未发现可核验官方仓库 |
| DexVLG | https://openaccess.thecvf.com/content/ICCV2025/html/He_DexVLG_Dexterous_Vision-Language-Grasp_Model_at_Scale_ICCV_2025_paper.html | 未找到独立项目页 | https://github.com/jiaweihe1996/DexVLG |
| UniGraspTransformer | https://openaccess.thecvf.com/content/CVPR2025/html/Wang_UniGraspTransformer_Simplified_Policy_Distillation_for_Scalable_Dexterous_Robotic_Grasping_CVPR_2025_paper.html | https://dexhand.github.io/UniGraspTransformer/ | https://github.com/microsoft/UniGraspTransformer |
| VLM Scaffolding | https://proceedings.neurips.cc/paper_files/paper/2025/hash/862644b156e51c35dea5a7446d640b14-Abstract-Conference.html | https://sites.google.com/view/dexterous-vlm-scaffolding | https://github.com/vdebakker/vlm-scaffolding |
| VideoVLA | https://proceedings.neurips.cc/paper_files/paper/2025/hash/89a3b655a8b68ae1c76b768152c9c19d-Abstract-Conference.html | https://videovla-nips2025.github.io/ | https://github.com/VideoVLA-Project/VideoVLA |
| OmniManip | https://openaccess.thecvf.com/content/CVPR2025/html/Pan_OmniManip_Towards_General_Robotic_Manipulation_via_Object-Centric_Interaction_Primitives_as_CVPR_2025_paper.html | https://omnimanip.github.io/ | 未发现可核验官方仓库 |
| Hi Robot | https://proceedings.mlr.press/v267/shi25d.html | https://www.pi.website/research/hirobot | 未发现可核验官方仓库 |
| DextER | https://openaccess.thecvf.com/content/CVPR2026/html/Lee_DextER_Language-driven_Dexterous_Grasp_Generation_with_Embodied_Reasoning_CVPR_2026_paper.html | https://junha-l.github.io/dexter/ | https://github.com/junha-l/dexter |
| SpatialVLA | https://www.roboticsproceedings.org/rss21/p011.html | https://spatialvla.github.io/ | https://github.com/SpatialVLA/SpatialVLA |

项目页/仓库无法保证始终可访问：3D-VLA作者主页直接请求出现SSL连接错误；其ICML论文集及作者组织代码仓库已可访问。AAAI论文条目信息由官方网页工具抓取核实，直接请求返回的200响应不能单独视为正文成功。

代码核查使用GitHub公开目录树API和绑定版本的raw内容：逐仓库读取README、依赖文件位置、核心模型/策略、训练/推理/评估入口。没有运行仓库代码。完整树、原始响应、所读文件URL及版本保存在99_Templates/_search_20260918_01；待复核清单列出可追踪入口。

## Papers Accepted（本轮正式入库）

**0篇。** 当前CVPR、ICCV、NeurIPS、ICML、ICLR、AAAI均为Pending Official Recheck；扩展RSS也未核验等级。既有Papers的4条数据逐单元格保留，不能把既有用户登记A级理解为本轮官方确认。

## Candidates Pending（待复核）

详见同目录[Candidates_Pending_2026-09-18.md](Candidates_Pending_2026-09-18.md)。

| 标题 | 年份 | 会议 | 主分类 | 代码状态 | 待办 |
| --- | --- | --- | --- | --- | --- |
| RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation | 2025 | ICLR | Bimanual | Released | CCF官方复核 |
| TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models | 2026 | ICLR | Bimanual | Released | CCF官方复核 |
| RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins | 2025 | CVPR | Bimanual | Released | CCF官方复核 |
| BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models | 2025 | NeurIPS | VLA | Released | CCF官方复核 |
| VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching | 2025 | NeurIPS | VLA | Released | CCF官方复核 |
| DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression | 2025 | ICML | VLA | Partial | CCF官方复核；Partial可运行性复核 |
| 3D-VLA: A 3D Vision-Language-Action Generative World Model | 2024 | ICML | VLA | Partial | CCF官方复核；Partial可运行性复核 |
| RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation | 2024 | NeurIPS | VLA | Partial | CCF官方复核；Partial可运行性复核 |
| TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies | 2025 | ICLR | VLA | Partial | CCF官方复核；Partial可运行性复核 |
| Latent Action Pretraining from Videos | 2025 | ICLR | VLA | Released | CCF官方复核 |
| FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation | 2025 | AAAI | Robot Manipulation | Released | CCF官方复核 |
| UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping | 2025 | CVPR | Dexterous Hand | Released | CCF官方复核 |
| Scaffolding Dexterous Manipulation with Vision-Language Models | 2025 | NeurIPS | Dexterous Hand | Released | CCF官方复核 |
| VideoVLA: Video Generators Can Be Generalizable Robot Manipulators | 2025 | NeurIPS | VLA | Partial | CCF官方复核；Partial可运行性复核 |
| DextER: Language-driven Dexterous Grasp Generation with Embodied Reasoning | 2026 | CVPR | Dexterous Hand | Released | CCF官方复核 |
| SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models | 2025 | RSS | VLA | Released | CCF官方复核 |

## Papers Rejected（本轮新增排除记录）

| 标题 | 原因 | 说明 |
| --- | --- | --- |
| AffordDexGrasp: Open-set Language-guided Dexterous Grasp with Generalizable-Instructive Affordance | Code_Coming_Soon | 项目页明确Code (Coming soon)、Dataset (Coming soon)；作者主页code为纯文本无链接。不能以项目网页源码算方法开源。 CCF等级本轮未确认；排除依据为代码门槛。项目页：https://isee-laboratory.github.io/AffordDexGrasp/ |
| DexVLG: Dexterous Vision-Language-Grasp Model at Scale | Code_Coming_Soon | GitHub递归树仅1个README文件；训练/推理代码及权重发布选项均未勾选。不属于实际代码开源。 CCF等级本轮未确认；排除依据为代码门槛。项目页： |
| OmniManip: Towards General Robotic Manipulation via Object-Centric Interaction Primitives as Spatial Constraints | No_Code | 本轮官网及针对性检索未找到可核实的作者方法代码；仅见论文、视频、项目页。No_Code表示未满足公开代码门槛，不是证明任何地方都不存在代码。 CCF等级本轮未确认；排除依据为代码门槛。项目页：https://omnimanip.github.io/ |
| Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models | No_Code | 本轮官方研究页及针对性检索未找到Hi Robot完整方法的官方代码；不能用底层pi0/openpi替代高层系统实现。No_Code表示未满足门槛，真实代码状态Unknown。 CCF等级本轮未确认；排除依据为代码门槛。项目页：https://www.pi.website/research/hirobot |
| Benchmarking Generalizable Bimanual Manipulation: RoboTwin Dual-Arm Collaboration Challenge at CVPR 2025 MEIS Workshop | Workshop | 竞赛官方页面明确为2nd MEIS Workshop及Technical Report：https://robotwin-benchmark.github.io/cvpr-2025-challenge/ 。不是RoboTwin CVPR 2025正式主会论文；此处无需依赖CCF等级即可排除。代码状态本轮不用于准入。 |
| ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation | Duplicate | 本轮规范化标题、官方论文URL去重命中已有P0001；主记录保留在Papers。此行仅记录重复检索，不表示主记录因研究质量或代码被否定。本轮仅复核官方论文身份，未重新认定旧CCF等级或代码状态。 |
| ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning | Duplicate | 本轮规范化标题、官方论文URL去重命中已有P0002；主记录保留在Papers。此行仅记录重复检索，不表示主记录因研究质量或代码被否定。本轮仅复核官方论文身份，未重新认定旧CCF等级或代码状态。 |
| DexHandDiff: Interaction-aware Diffusion Planning for Adaptive Dexterous Manipulation | Duplicate | 本轮规范化标题、官方论文URL去重命中已有P0003；主记录保留在Papers。此行仅记录重复检索，不表示主记录因研究质量或代码被否定。本轮仅复核官方论文身份，未重新认定旧CCF等级或代码状态。 |
| AR-VRM: Imitating Human Motions for Visual Robot Manipulation with Analogical Reasoning | Duplicate | 本轮规范化标题、官方论文URL去重命中已有P0004；主记录保留在Papers。此行仅记录重复检索，不表示主记录因研究质量或代码被否定。本轮仅复核官方论文身份，未重新认定旧CCF等级或代码状态。 |

No_Code在OmniManip、Hi Robot处表示“本轮未找到可核验的官方方法代码”，Code Status为Unknown，不作全网不存在代码的断言。AffordDexGrasp明确Coming soon；DexVLG只有README及未完成发布勾选。原有CoT-VLA、RoboGround记录和说明保持不变，未重复新增。Duplicate只记录排除重复写入的动作，Papers中的原条目没有被移除。

## Code Audit（代码核查）

| 论文 | 代码状态 | 静态核查结论 |
| --- | --- | --- |
| RDT-1B | Released | 已检查RDT模型、训练及AgileX推理实现；实际部署仍需机器人接口适配。 |
| TwinVLA | Released | 官方2026论文集确认；已查模型、训练、RoboTwin部署。论文集年份优先于2025预印本。 |
| RoboTwin | Released | 采用RoboTwin-1.0分支；已查任务环境、交接动作及评估。与早期ECCV Workshop版本、CVPR Workshop竞赛报告、2.0版本区别记录。 |
| BridgeVLA | Released | 原论文代码在bridgevla分支；main已是BridgeVLA++，不可混用。已查agent、训练、评估；PaliGemma基础权重需申请访问。 |
| VLA-Cache | Released | 已查patch相似度、层级缓存调度及模型实现；方法免训练。训练代码主要继承基座，不能当作额外方法训练贡献。 |
| DiffusionVLA | Partial | 官网明确指向后续DexVLA仓库并称可训练DiVLA；实际存在train_divla.sh、UNet策略和评估。原论文模型/完整实验对应关系未核实；Partial可运行条件待复核，不准入核心。 |
| 3D-VLA | Partial | 公开目标图像/点云扩散训练与推理、LLM训练实现；未确认完整机器人策略评测链，保守标Partial，端到端可运行性待复核。 |
| RoboMamba | Partial | 实际存在模型、src/test.py和src/script/test.sh；README要求邮件索取训练代码。test分支提供权重入口。未验证权重可下载/端到端运行，且项目页未查到直接GitHub出链，作者归属链须补核。 |
| TraceVLA | Partial | 已查TraceProcessor、推理与训练代码；README仍称轨迹标注数据Coming soon，未验证论文权重/数据完整链。保守标Partial，待可运行性复核。 |
| LAPA | Released | 已查潜动作推理、量化训练、动作部署实现。潜动作输出需要微调映射到机器人动作；不等于开箱即用机器人策略。 |
| FlowPolicy | Released | AAAI Technical Track on Intelligent Robots，14754–14762。已查FlowPolicy类、训练与评估；README说明基准统计应取训练时记录，而独立eval脚本用于部署/推理。 |
| AffordDexGrasp | Coming_Soon | 项目页明确Code (Coming soon)、Dataset (Coming soon)；作者主页code为纯文本无链接。不能以项目网页源码算方法开源。 |
| DexVLG | Coming_Soon | GitHub递归树仅1个README文件；训练/推理代码及权重发布选项均未勾选。不属于实际代码开源。 |
| UniGraspTransformer | Released | 已查在线RL和离线蒸馏实现及安装/训练/评估说明。代码Released；IsaacGym4通用策略权重仍Coming Soon，不代表代码也未发布。 |
| VLM Scaffolding | Released | 已查轨迹生成、RL训练和评估；README提供真机ROS部署说明。依赖外部Gemini服务、仿真器及机器人环境，未运行。 |
| VideoVLA | Partial | 已查动作DiT、扩散引擎、sample_video_action.py。旧Coming soon文字在HTML注释中，不能当作当前状态；训练/机器人benchmark完整流水线本轮未确认，标Partial待运行条件复核。 |
| OmniManip | Unknown | 本轮官网及针对性检索未找到可核实的作者方法代码；仅见论文、视频、项目页。No_Code表示未满足公开代码门槛，不是证明任何地方都不存在代码。 |
| Hi Robot | Unknown | 本轮官方研究页及针对性检索未找到Hi Robot完整方法的官方代码；不能用底层pi0/openpi替代高层系统实现。No_Code表示未满足门槛，真实代码状态Unknown。 |
| DextER | Released | CVF页面直接访问成功；已查核心模型、训练和测试实现。数据说明有2026-07-22修正，后续应使用修正版数据。 |
| SpatialVLA | Released | 正式venue为RSS 2025，不是CVPR/ICML。RSS当前CCF目录等级未成功从官方核实，故仅作扩展候选；不擅自标A或Not_CCF_A。 |

所有权重和数据入口仅作作者提供的发布线索，未下载或验证二进制内容。静态存在可训练/推理的源码不等于本地实测成功；Partial没有被自动当成核心准入。

## New Keywords Found（新增关键词）

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

## Open Questions（待确认事项）

1. 从CCF官方第七版正文确认6个目标会议等级；网页验证码完成前不做替代认定。既有IJCAI=A登记有历史冲突，未擅自改写，也未用作准入依据。
2. 核实RSS在当前官方目录中的归类；SpatialVLA正式venue为RSS 2025，不能误标为CVPR或ICML。
3. 对DiffusionVLA、3D-VLA、RoboMamba、TraceVLA、VideoVLA逐一确认原论文对应的可运行核心路径与缺失资源。
4. RoboMamba作者项目页未查到GitHub直接出链；仓库虽署有论文BibTeX，仍须补足作者归属证据。
5. BridgeVLA须固定bridgevla分支，RoboTwin须固定RoboTwin-1.0；不能以新版本默认分支替代正式论文实现。
6. 20篇只完成书目信息/范围与代码静态筛查，Problem、Gap、Method等深读字段尚未填写；不认定已经阅读或复现。

## Next Reading Priorities（下一轮优先阅读建议）

以下为项目匹配分析，仍待准入，不改变Reading Level：

1. **RoboTwin（CVPR 2025）**：先梳理双臂任务、示范生成和评估接口，形成与当前仿真流程的对照。
2. **RDT-1B（ICLR 2025）**：关注双臂动作表示、数据加载和微调入口。
3. **TwinVLA（ICLR 2026）**：比较单臂预训练如何用于双臂协作，以及数据效率评测。
4. **BridgeVLA（NeurIPS 2025）**：检查3D输入、动作输出和少示范学习的实验设置。
5. **DextER（CVPR 2026）**：作为灵巧手分支，阅读接触推理与语言引导抓取的连接；不假定可直接迁移到普通夹爪。

## Integrity and Results（完整性与统计）

Papers新增0、保留4；Rejected新增9、合计11；Venues更新6个目标会议核验状态、增补RSS待核验记录；Keywords增补14条，同时追加Keywords.md。Papers按主分类统计：VLA 0、Robot Manipulation 2、Dexterous Hand 2、Bimanual 0。ManipTrans涉及双臂，但其原主分类为Dexterous Hand，未为凑数改分类。

本轮20篇新候选代码状态：Released 11、Partial 5、Coming_Soon 2、Unknown 2。原Papers已有Released 2（ManipTrans、AR-VRM）、Partial 2（ManipLLM、DexHandDiff），本轮不重新改写这些状态。

最终文件完整性检查结果见本轮verification.json；只有检查通过后才替换工作簿，备份保留。
