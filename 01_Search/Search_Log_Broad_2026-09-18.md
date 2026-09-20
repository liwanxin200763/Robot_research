# Broad Search Log / 广泛检索日志 · 2026-09-18
## 目标与范围

本轮为 Discovery Phase（发现阶段）：2024–2026 为主，必要时纳入 2022–2023 奠基工作；覆盖 VLA/机器人基础模型、机器人操作、双臂、灵巧操作、示范学习、扩散/流匹配、世界模型、遥操作、数据集/benchmark 与综述。只做题录、官方来源、类型、venue、代码入口/状态的基础核验，不做精读、复现、批量下载 PDF 或 clone 论文仓库。
## 本轮结果

- 候选条目经标题去重：**77 篇**。暂存组装曾将已纳入的 16 条种子候选再次导入，故去重前条目数按**本地组装行**计为 **93**；去重后 **77**。
- 与既有 `Papers` 标题重复：**0**；本轮未改动 `Papers` 或 `Rejected`。正式论文版本优先于 arXiv，社区综述不当作论文发表。
- 核验范围：主要 proceedings / publisher 页面确认题名和正式发表身份；部分记录只核对官方卷目录，没有逐篇核查平台细节。代码没有逐一审仓库；`Released/Partial` 仅来自本地既有静态审计的条目；其他标为 `Unknown`。
## 检索日期、平台和入选记录数

日期：**2026-09-18**。以下是最终 Discovery 中每条记录所记的主要发现来源分布（不是搜索引擎原始命中数）：

| 平台 / 来源 | 入选记录 |
|---|---:|
| CVF Open Access | 3 |
| ICLR Proceedings | 16 |
| AAAI Proceedings | 5 |
| PMLR CoRL Proceedings | 21 |
| arXiv | 6 |
| Publisher pages | 5 |
| Community survey index | 1 |
| Cross-Venue official proceedings audit | 16 |
| RSS Official Proceedings | 3 |
| IEEE Xplore / institutional publication record | 1 |

实际打开/查询的来源入口：
- [CVF Open Access](https://openaccess.thecvf.com)
- [NeurIPS Proceedings](https://proceedings.neurips.cc)
- [ICLR Proceedings](https://proceedings.iclr.cc)
- [PMLR CoRL Proceedings](https://proceedings.mlr.press/v270/)
- [AAAI Proceedings](https://ojs.aaai.org/index.php/AAAI)
- [RSS Official Proceedings](https://roboticsproceedings.org)
- [IEEE Xplore / institutional publication record](https://ieeexplore.ieee.org/document/10611477)
- [arXiv](https://arxiv.org)
- [Publisher pages](Frontiers / Springer Nature / SAGE / Elsevier)
- [CCF official seventh edition](https://www.ccf.org.cn/Academic_Evaluation/By_category/)

CCF 信息以中国计算机学会（CCF）2026年第七版正式目录为准。目录正文页面访问受验证限制，本次未逐个导出会议行，因此 CCF A 等级字段对目标 AI/CV venue 标为“第七版标记、单行待复核”；扩展机器人 venue 不据此纳入 CCF A。既有会议信息中，ICLR A、ICRA B、IROS C、T-RO B、IJCAI B 为用户已提供的第七版口径；逐行正式目录核验仍列待办。

## 实际检索式

下列 68 条是本轮实际提交的 query/venue 精确搜索组合；query 家族覆盖 VLA、foundation model、generalist policy、bimanual/dual-arm、dexterous、diffusion/flow、imitation、long-horizon、failure recovery、world models、action tokens/chunks、cross-embodiment、人类视频/teleoperation、dataset、vision-tactile、contact-rich、affordance、3D、sim-to-real，以及 CVPR/ICCV/ICLR/NeurIPS/AAAI/CoRL/RSS/ICRA 官方 proceedings 反向检索。
1. `"robot vision language action survey 2024 2025 arXiv survey robot foundation models review"`
2. `"dexterous manipulation survey 2024 2025 robotic hand review"`
3. `"bimanual manipulation survey robot learning 2024 review"`
4. `"robot foundation models survey 2024 2025 manipulation arXiv"`
5. `"site:openreview.net bimanual robot manipulation ICLR 2025"`
6. `"site:roboticsproceedings.org RSS 2024 bimanual robot manipulation ACT diffusion policy 3D"`
7. `"site:openaccess.thecvf.com CVPR 2024 2025 robot manipulation VLA dexterous papers"`
8. `"site:proceedings.neurips.cc 2024 robot manipulation VLA dexterous policy"`
9. `"robot manipulation survey 2024 survey learning-based robotic manipulation review journal"`
10. `"bimanual robot manipulation learning 2024 2025 paper CoRL RSS official proceedings"`
11. `"dexterous manipulation 2024 2025 NeurIPS ICLR CoRL official papers robot hand"`
12. `"robot learning datasets benchmarks 2024 2025 manipulation official papers DROID RoboCasa LIBERO"`
13. `"site:proceedings.mlr.press robot bimanual manipulation CoRL 2024 bimanual"`
14. `"site:roboticsproceedings.org bimanual 2024 robot manipulation"`
15. `"site:openreview.net/forum?id bimanual manipulation robot 2025 learning"`
16. `"site:openaccess.thecvf.com robot manipulation dexterous hand CVPR 2025 UniGraspTransformer RoboTwin"`
17. `"OpenVLA CoRL 2024 official proceedings PMLR OpenVLA"`
18. `"Octo Open-Source Generalist Robot Policy RSS 2024 official proceedings"`
19. `"site:proceedings.iclr.cc 2025 RDT-1B LAPA TraceVLA"`
20. `"site:proceedings.neurips.cc/paper_files/paper/2024 RoboMamba"`
21. `"site:openaccess.thecvf.com/content/CVPR2024 robot manipulation robot policy VLA"`
22. `"site:openaccess.thecvf.com/content/CVPR2025 robot manipulation policy learning robot"`
23. `"site:openaccess.thecvf.com/content/ICCV2025 robot manipulation VLA dexterous"`
24. `"site:proceedings.iclr.cc/paper_files/paper/2025 robot manipulation robot learning dexterous"`
25. `"site:proceedings.neurips.cc/paper_files/paper/2025 robot manipulation VLA robot learning policy"`
26. `"site:proceedings.iclr.cc/paper_files/paper/2026 robot manipulation bimanual VLA"`
27. `"site:proceedings.mlr.press/v robot manipulation 2025 CoRL 2025 VLA imitation"`
28. `"site:aaai.org FlowPolicy robot manipulation 2025"`
29. `"site:proceedings.iclr.cc/paper_files/paper/2025 Action Chunking robot manipulation"`
30. `"site:proceedings.mlr.press/v305 manipulation bimanual CoRL 2025"`
31. `"site:proceedings.mlr.press/v270 robot manipulation CoRL 2024"`
32. `"site:roboticsproceedings.org/rss20 robot manipulation DROID Diffusion Policy RoboCasa"`
33. `"site:roboticsproceedings.org/rss21 manipulation VLA 2025"`
34. `"site:proceedings.neurips.cc/paper_files/paper/2024 robot manipulation diffusion policy"`
35. `"site:proceedings.neurips.cc/paper_files/paper/2025 robot manipulation dataset benchmark VLA"`
36. `"site:openaccess.thecvf.com/content/CVPR2026 robot manipulation VLA policy"`
37. `"site:openreview.net ICLR 2025 robot manipulation ET-SEED HAMSTER AdaManip"`
38. `"site:ojs.aaai.org/index.php/AAAI robotic manipulation 2025 policy learning"`
39. `"vision language action robot manipulation"`
40. `"VLA robot manipulation"`
41. `"robot foundation model manipulation"`
42. `"generalist robot policy"`
43. `"bimanual manipulation"`
44. `"dual-arm manipulation"`
45. `"bimanual imitation learning"`
46. `"bimanual robot learning"`
47. `"dexterous manipulation"`
48. `"dexterous hand robot learning"`
49. `"dexterous hand imitation learning"`
50. `"dexterous manipulation generalization"`
51. `"dexterous manipulation reinforcement learning"`
52. `"robot manipulation diffusion policy"`
53. `"robot manipulation flow matching"`
54. `"robot manipulation imitation learning"`
55. `"robot manipulation long horizon"`
56. `"robot manipulation failure recovery"`
57. `"robot manipulation world model"`
58. `"action tokenization robot"`
59. `"action chunking robot manipulation"`
60. `"cross embodiment robot learning"`
61. `"human video robot manipulation"`
62. `"teleoperation robot dataset"`
63. `"robot demonstration dataset"`
64. `"vision tactile manipulation"`
65. `"contact rich manipulation"`
66. `"affordance reasoning robot"`
67. `"3D manipulation robot learning"`
68. `"sim to real dexterous manipulation"`

## 汇总统计

**年份**：
- 2024: 28
- 2025: 35
- 2026: 14

**Venue / Source field**（社区综述及期刊按记录中的 source 标签单列）：
- CVPR: 4
- ICCV: 2
- ICLR: 20
- AAAI: 6
- CoRL: 21
- Survey / arXiv: 6
- Survey / journal: 5
- Survey / community: 1
- NeurIPS: 5
- ICML: 2
- RSS: 4
- ICRA: 1

**论文类型**：
- Method Paper: 56
- Dataset / Benchmark: 6
- System / Platform: 3
- Survey / Review: 12

**代码状态**（不代表已安装或实测）：
- Unknown: 56
- Released: 16
- Partial: 5

**交叉分类数量**（多标签可重叠，不能相加）：
- Robot Manipulation / IL / Diffusion: 43
- Bimanual: 12
- Dexterous Hand / Dexterous Manipulation: 14
- Dataset / Benchmark: 7
- VLA / Robot Foundation Models: 23
- Survey / Review: 12

- Bimanual: 15
- Dexterous Hand / Manipulation: 14
- VLA / Robot Foundation Models: 23
- Abstract/source explicitly reports real-world robot experiment (Yes or Mixed): 19; remaining 58 are Unknown or simulation-only.

**Priority（初步排序）**：
- P0: 25
- P2: 11
- P1: 41

## 新发现的检索关键词

以下为可继续检索的新增高频术语；已按组别、中文解释和用途增量加入 `Keywords.md` 及工作簿 `Keywords` sheet。

- **Bimanual Coordination**（双臂协同）｜任务与本体：区分双臂同时协同与单臂独立执行，检索交接、稳定与双臂规划。
- **Parallel Gripper**（平行夹爪）｜任务与本体：与当前NERO普通夹爪本体匹配，便于筛除仅适用于多指手的特化方法。
- **Mobile Manipulation**（移动操作）｜任务与本体：区分固定双臂与移动底盘+机械臂系统，寻找数据采集和全身控制方案。
- **Hierarchical VLA**（分层视觉-语言-动作模型）｜模型与学习：对照高层语义规划和低层闭环控制，适用于长任务。
- **Video Diffusion Policy**（视频扩散策略）｜模型与学习：连接未来视觉预测、世界模型与动作输出，查数据效率和部署延迟。
- **Equivariant Diffusion Policy**（等变扩散策略）｜模型与学习：追踪空间对称性先验如何降低示范需求并改善位姿泛化。
- **Asynchronous Inference**（异步推理）｜模型与学习：检索VLA推理与动作执行并行时的对齐、接续和失败恢复。
- **Cross-Embodiment Transfer**（跨本体迁移）｜模型与学习：比较从单臂、双臂、移动平台向目标机器人迁移策略和数据。
- **Long-Horizon Manipulation**（长时序操作）｜能力与评价：关注任务分解、阶段性目标和持续执行中的恢复机制。
- **Affordance Transfer**（可供性迁移）｜能力与评价：把物体/任务级可操作区域转化为抓取或放置策略，并评估零样本泛化。
- **Bimanual Benchmark**（双臂评测基准）｜能力与评价：查任务集、双臂协调指标、仿真随机化和真机复测协议。
- **Human Motion Capture Demonstrations**（人类动作捕捉示范）｜数据与部署：比较无机器人遥操作、手部追踪和示范重定向的数据获取路径。
- **Teleoperation Data Collection**（遥操作数据采集）｜数据与部署：检索低成本双臂采集系统、同步、多视角和数据质量。
- **Visual-Tactile Pretraining**（视觉-触觉预训练）｜数据与部署：用于灵巧操作扩展；判断触觉是否对普通夹爪操作有可迁移价值。
- **Mixed-Quality Demonstrations**（混合质量示范）｜数据与部署：检索示范质量识别、在线纠正、人工干预和失败数据利用。

## 尚待核验事项

- CCF 第七版每个目标 venue 的单行正式目录：网页验证限制导致尚未逐行复核。尤其需保留 ICLR=A、IJCAI=B、ICRA=B、IROS=C、T-RO=B 的第七版口径，并核对 CCF 官方 PDF 中的原始分类。
- Discovery 内若干篇只做题名和官方卷目录确认，未逐篇读取论文正文；机器人/手型、真机情况、具体benchmark留空或 Unknown，后续应逐条补核。
- 代码审查只覆盖既有 16 条候选的仓库静态内容；Released/Partial 不代表可在本机运行。剩余 Unknown 项需访问作者仓库/项目主页后更新。
- CoRL 2024 的会年为 2024，但 PMLR v270 在 2025-01 上线；工作簿保留会议年份 2024，并在备注解释 online publication 时间。
- ACT 原始 2023 工作按 Foundational 候选纳入；未把未确认的 workshop 记录填为正式主会。
- 2023 Diffusion Policy、VIMA、RT-1/RT-2 等经典基线及可用性记录仍需扩展；2022–2023 数量尚少。
- 未纳入被确认是 workshop/demo/竞赛技术报告的条目，避免混入正式主会论文；遇到版本差异先复核会议主会目录。

## 最值得后续筛选的 20 条

按当前 NERO 双臂/普通夹爪、示范采集、ACT/扩散策略、VLA 与操作基准作初筛；这不是精读结论或“晋升 Papers”决定。

1. **RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins**（CVPR 2025；P0）
2. **RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation**（ICLR 2025；P0）
3. **TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models**（ICLR 2026；P0）
4. **Mobile ALOHA: Learning Bimanual Mobile Manipulation Using Low-Cost Whole-Body Teleoperation**（CoRL 2024；P0）
5. **ALOHA Unleashed: A Simple Recipe for Robot Dexterity**（CoRL 2024；P0）
6. **Rethinking Bimanual Robotic Manipulation: Learning with Decoupled Interaction Framework**（ICCV 2025；P0）
7. **OPEN TEACH: A Versatile Teleoperation System for Robotic Manipulation**（CoRL 2024；P0）
8. **BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models**（NeurIPS 2025；P0）
9. **Hierarchical Diffusion Policy for Kinematics-Aware Multi-Task Robotic Manipulation**（CVPR 2024；P0）
10. **FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation**（AAAI 2025；P0）
11. **Demystifying Robot Diffusion Policies: Action Memorization and a Simple Lookup Table Alternative**（ICLR 2026；P0）
12. **VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation**（CoRL 2024；P1）
13. **UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping**（CVPR 2025；P1）
14. **DexTrack: Towards Generalizable Neural Tracking Control for Dexterous Manipulation from Human References**（ICLR 2025；P2）
15. **HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation**（ICLR 2025；P0）
16. **RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation**（NeurIPS 2024；P1）
17. **Latent Action Pretraining from Videos**（ICLR 2025；P1）
18. **VTDexManip: A Dataset and Benchmark for Visual-tactile Pretraining and Dexterous Manipulation with Reinforcement Learning**（ICLR 2025；P2）
19. **DextER: Language-driven Dexterous Grasp Generation with Embodied Reasoning**（CVPR 2026；P0）
20. **SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models**（RSS 2025；P1）

## 最值得先看的 5 篇综述

1. [What Foundation Models can Bring for Robot Learning in Manipulation: A Survey](https://journals.sagepub.com/doi/10.1177/02783649251390579)
2. [A Survey on Robotics with Foundation Models: Toward Embodied AI](https://arxiv.org/abs/2402.02385)
3. [A Survey on Vision-Language-Action Models for Embodied AI](https://arxiv.org/abs/2405.14093)
4. [A Survey on Vision-Language-Action Models: An Action Tokenization Perspective](https://arxiv.org/abs/2507.01925)
5. [Learning by Watching: A Review of Video-Based Learning Approaches for Robot Manipulation](https://arxiv.org/abs/2402.07127)

## 最值得后续复现的 10 个开源工作（静态代码状态 Released/Partial）

1. **RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation**（ICLR 2025；Released；[代码入口](https://github.com/thu-ml/RoboticsDiffusionTransformer)）
2. **TwinVLA: Data-Efficient Bimanual Manipulation with Twin Single-Arm Vision-Language-Action Models**（ICLR 2026；Released；[代码入口](https://github.com/jellyho/TwinVLA)）
3. **RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins**（CVPR 2025；Released；[代码入口](https://github.com/RoboTwin-Platform/RoboTwin/tree/RoboTwin-1.0)）
4. **BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models**（NeurIPS 2025；Released；[代码入口](https://github.com/BridgeVLA/BridgeVLA/tree/bridgevla)）
5. **OpenVLA: An Open-Source Vision-Language-Action Model**（CoRL 2024；Released；[代码入口](https://github.com/openvla/openvla)）
6. **Octo: An Open-Source Generalist Robot Policy**（RSS 2024；Released；[代码入口](https://github.com/octo-models/octo)）
7. **FlowPolicy: Enabling Fast and Robust 3D Flow-Based Policy via Consistency Flow Matching for Robot Manipulation**（AAAI 2025；Released；[代码入口](https://github.com/zql-kk/FlowPolicy)）
8. **VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching**（NeurIPS 2025；Released；[代码入口](https://github.com/siyuhsu/vla-cache)）
9. **RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation**（NeurIPS 2024；Partial；[代码入口](https://github.com/lmzpai/roboMamba)）
10. **VideoVLA: Video Generators Can Be Generalizable Robot Manipulators**（NeurIPS 2025；Partial；[代码入口](https://github.com/VideoVLA-Project/VideoVLA)）

上述代码入口均未在本机 clone、安装或执行；“复现优先”仅表示适合下一轮筛选。

## 文件

- Discovery workbook: `D:\Robot\_Research\00_Paper_Pool\Paper_Pool.xlsx`（新增 `Discovery` sheet）
- Keywords: `D:\Robot\_Research\01_Search\Keywords.md`
- Search log: `D:\Robot\_Research\01_Search\Search_Log_Broad_2026-09-18.md`
