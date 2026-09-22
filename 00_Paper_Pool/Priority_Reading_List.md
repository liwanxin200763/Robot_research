# Priority Reading List（优先阅读清单）

优先级面向 NERO 双臂 + 普通夹爪、robosuite、示范采集、ACT / Diffusion Policy、VLA 与真机部署。链接始终指向唯一主卡。

## P0 — 先读

1. [[02_Papers/03_Bimanual/PPI_Bimanual|PPI：Gripper Pose and Object Pointflow]] — 双臂、普通夹爪、仿真与真机都直接匹配。
2. [[02_Papers/03_Bimanual/YOTO|YOTO]] — 人类视频、低成本示范、双臂 Diffusion Policy。
3. [[02_Papers/05_Sim2Real/Sim2Real-VLA|Sim2Real-VLA]] — 合成数据到真机、双臂与长时序；Special Attention。
4. [[02_Papers/01_VLA/BridgeVLA|BridgeVLA]] — 3D 操作与数据效率。
5. [[02_Papers/10_Benchmark_Dataset/RoboTwin|RoboTwin]] — 双臂数据与策略学习线索。

## P1 — 第二批

1. [[02_Papers/03_Bimanual/Constrained_Bimanual_Planning|Constrained Bimanual Planning]] — 双臂约束与规划安全。
2. [[02_Papers/03_Bimanual/Reactive_Multiarm_Coordination|Reactive Multi-arm Coordination]] — 多臂在线协同与避碰。
3. [[02_Papers/01_VLA/ReconVLA|ReconVLA]] — 以凝视区域重建提升 VLA 的视觉 grounding、精确操作和泛化；Special Attention。
4. [[02_Papers/01_VLA/Octo|Octo]] — 开源通用机器人策略基线。
5. [[02_Papers/10_Benchmark_Dataset/DROID|DROID]] — 真机数据规模与采集设计。
6. [[02_Papers/10_Benchmark_Dataset/RoboCasa|RoboCasa]] — 与仿真数据、家居操作和泛化评测相关。

本表用于安排后续核验与实验，不代表已复现。

## SayCan

### [[02_Papers/01_VLA/SayCan|SayCan: Do As I Can, Not As I Say: Grounding Language in Robotic Affordances]]

- Year: 2022
- Venue: CoRL
- Priority: P0
- Special Attention: Yes
- Why: Foundational language-to-robot affordance grounding and interpretable long-horizon skill composition; directly relevant to feasibility scoring and failure-aware replanning.
