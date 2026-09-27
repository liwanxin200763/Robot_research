# 优先阅读清单

优先级面向 NERO 双臂 + 普通夹爪、robosuite、示范采集、ACT / Diffusion Policy、VLA 与真机部署。链接始终指向唯一主卡。

## P0 — 先读

1. [[02_Papers/03_Bimanual/PPI_Bimanual|以夹爪位姿与物体点流作为机器人双臂操作接口]] — 双臂、普通夹爪、仿真与真机都直接匹配。
2. [[02_Papers/03_Bimanual/YOTO|YOTO：从视频示范一次性学习双臂机器人操作]] — 人类视频、低成本示范、双臂 Diffusion Policy。
3. [[02_Papers/06_Diffusion_Flow_IL_RL/Sim2Real-VLA|Sim2Real-VLA：将合成技能零样本泛化到真实操作]] — 合成数据到真机、双臂与长时序；特别关注。
4. [[02_Papers/01_VLA/BridgeVLA|BridgeVLA：通过输入—输出对齐高效学习三维操作]] — 3D 操作与数据效率。
5. [[02_Papers/10_Benchmark_Dataset/RoboTwin|RoboTwin：基于生成式数字孪生的双臂机器人 Benchmark]] — 双臂数据与策略学习线索。

## P1 — 第二批

1. [[02_Papers/03_Bimanual/Constrained_Bimanual_Planning|结合解析逆运动学的受约束双臂规划]] — 双臂约束与规划安全。
2. [[02_Papers/03_Bimanual/Reactive_Multiarm_Coordination|通过反应式轨迹调制实现多机械臂实时协同]] — 多臂在线协同与避碰。
3. [[02_Papers/01_VLA/ReconVLA|ReconVLA：以重建增强机器人感知的 VLA 模型]] — 以凝视区域重建提升 VLA 的视觉 Grounding、精确操作和泛化；特别关注。
4. [[02_Papers/01_VLA/Octo|Octo：开源通用机器人策略]] — 开源通用机器人策略基线。
5. [[02_Papers/10_Benchmark_Dataset/DROID|DROID：大规模自然场景机器人操作数据集]] — 真机数据规模与采集设计。
6. [[02_Papers/10_Benchmark_Dataset/RoboCasa|RoboCasa：面向通用机器人的大规模家务任务仿真]] — 与仿真数据、家居操作和泛化评测相关。
7. [[02_Papers/01_VLA/VLA-Cache|VLA-Cache：利用自适应 Token 缓存提高 VLA 操作效率]] — 无需重训的跨帧 token 缓存；适合测量本地 VLA 实时推理收益，。

本表按当前项目方向列出优先阅读建议；阅读清单不代表已经完成实验复现。
