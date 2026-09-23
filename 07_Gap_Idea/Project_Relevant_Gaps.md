# 与当前项目相关的研究问题

项目主线：**双臂 + 普通夹爪 + 真机操作 + 未来可能加入 VLA**。本页是实验设计清单，不是创新性声明。每个方向都要回到论文卡与原文核验；同一论文出现在多行不表示有多个独立证据。

| 方向 | 相关论文 | 现有做法 | 尚需弄清 / 为什么重要 | 下一步核验 |
|---|---|---|---|---|
| 单臂策略迁移双臂 | [[02_Papers/01_VLA/OpenVLA|OpenVLA]]、[[02_Papers/03_Bimanual/RDT-1B|RDT-1B]] | 通用 VLA 与双臂扩散策略分别解决不同设置 | 单臂动作头能否适配两只普通夹爪 | 固定任务、示范预算和真机复位规则，对比成功率 |
| 双臂 joint affordance | [[02_Papers/03_Bimanual/2HandedAfforder|2HandedAfforder]]、[[02_Papers/03_Bimanual/VoxAct-B|VoxAct-B]] | 预测可操作区域和双臂协调动作 | 支撑手与操作手的接触时机需共同决定 | 检查遮挡、碰撞、物体滑动和普通夹爪适配 |
| VLA action feasibility | [[02_Papers/01_VLA/SayCan|SayCan]]、[[02_Papers/01_VLA/ReconVLA|ReconVLA]] | 给技能估计可执行性，或改进目标 Grounding | 目标看着对，动作仍可能不可达或不安全 | 在未见物体上校准可行性判断 |
| 动作前验证 | [[02_Papers/01_VLA/ReconVLA|ReconVLA]]、[[02_Papers/02_Robot_Manipulation/ManipLLM|ManipLLM]] | 检查目标、可操作区域或动作计划 | 接触前应确认目标和位姿 | 统计误通过、误拒绝与额外延迟 |
| 动作后成功验证 | [[02_Papers/01_VLA/SayCan|SayCan]]、[[02_Papers/07_Generalization_LongHorizon/Self-Correcting_Robot_Manipulation_via_Gaussian-Splatted_Foresight|Gaussian-Splatted Foresight]] | 技能规划或预测场景与真实观测对比 | 规划正确不等于物理动作完成 | 遮挡和接触后的成功检测准确率 |
| 失败检测 | [[02_Papers/01_VLA/ReconVLA|ReconVLA]]、[[02_Papers/07_Generalization_LongHorizon/Self-Correcting_Robot_Manipulation_via_Gaussian-Splatted_Foresight|Gaussian-Splatted Foresight]] | Grounding 检查或视觉预期差异 | 要区分短暂观测噪声与真正失败 | 建立失败类别，测检测延迟和相机位移影响 |
| 失败恢复与重规划 | [[02_Papers/01_VLA/SayCan|SayCan]]、[[02_Papers/07_Generalization_LongHorizon/Policy_Decorator|Policy Decorator]] | 技能级重新规划或局部策略修正 | 恢复动作不能反复造成危险接触 | 分开统计首次成功、恢复成功和人为干预 |
| 长时序误差积累 | [[02_Papers/01_VLA/SayCan|SayCan]]、[[02_Papers/07_Generalization_LongHorizon/SPIRE|SPIRE]] | 多技能组合与长时序策略 | 前一步放置偏差会影响后续双臂动作 | 每步状态检查和最终成功率一起评测 |
| Sim2Real 双臂鲁棒性 | [[02_Papers/05_Sim2Real/Sim2Real-VLA|Sim2Real-VLA]]、[[02_Papers/03_Bimanual/RDT-1B|RDT-1B]] | 合成技能与双臂动作生成 | 真机接触、视觉和时序可能与仿真不同 | 匹配仿真/真机任务，记录物体和光照变化 |
| 跨相机、夹爪和本体 | [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]]、[[02_Papers/01_VLA/OpenVLA|OpenVLA]] | 多本体数据和通用策略 | 标定、TCP 和动作约定可能主导迁移结果 | 留出相机视角/夹爪类型，检查归一化 |
| 合成数据与真实数据联合训练 | [[02_Papers/05_Sim2Real/Sim2Real-VLA|Sim2Real-VLA]]、[[02_Papers/10_Benchmark_Dataset/DROID|DROID]] | 合成预训练与真机示范 | 哪个比例最节省真实数据尚未在本项目硬件上测量 | 固定真实示范预算，比较不同混合比例 |
| 双臂 Action Representation | [[02_Papers/03_Bimanual/RDT-1B|RDT-1B]]、[[02_Papers/06_Diffusion_Flow_IL_RL/3D_Diffuser_Actor|3D Diffuser Actor]] | 不同动作空间中的联合生成 | 关节、末端位姿和动作块会改变同步与延迟 | 等量数据消融，记录单位、频率和接触失败 |
| Human Video → Robot Action | [[02_Papers/06_Diffusion_Flow_IL_RL/MimicFunc|MimicFunc]]、[[02_Papers/03_Bimanual/YOTO|YOTO]] | 从人类视频提取功能对应或关键帧 | 人与机器人的手部结构和动作空间不同 | 检查是否能转成普通夹爪的可执行动作 |

**优先核验的五个问题：** 双臂 joint affordance、动作前验证、动作后成功验证、失败恢复、Sim2Real 双臂鲁棒性。先选一个小型真机任务，把失败类型和评价标准定清楚，再判断是否值得投入方法研究。
