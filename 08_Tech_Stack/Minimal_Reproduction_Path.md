# 最小复现路线

目标是先打通“数据 → 策略 → 动作 → 评测”的小闭环，再考虑双臂真机和大型 VLA。命令会随仓库版本变化，实际运行以官方 README 为准；不为完成路线而下载大型数据集或权重。

## Stage 1：看懂一条数据

- **学什么：** Episode（回合）、Observation（观测）、Action（动作）、时间戳、坐标系和归一化。
- **跑什么：** 用本地已有的一条 LeRobot episode 或官方最小样例，打印图像、机器人状态与动作的 shape，并可视化五个时间步。[LeRobot 文档](https://huggingface.co/docs/lerobot/main/index)。
- **看哪些文件：** 数据集 metadata、episode 索引、单条轨迹和数据读取示例。
- **预期输出：** 一页数据说明，列明相机、关节/动作维度、单位和频率。
- **常见问题：** 时间戳错位、隐藏归一化、左右臂对调、缺少标定。
- **完成标准：** 能解释策略每一步输入什么、输出命令实际表示什么。

## Stage 2：跑一个小型模仿学习例子

- **学什么：** Behavior Cloning（行为克隆）与 ACT 的 Action Chunk（动作块）。
- **跑什么：** 依照 [LeRobot 官方训练说明](https://huggingface.co/docs/lerobot/main/index) 或 [ACT 官方仓库](https://github.com/tonyzhaozh/act)，在许可的小样本/仿真任务上做一次短运行；也可加载现成的小 checkpoint。
- **看哪些文件：** README、配置、DataLoader、Policy、Loss 和训练入口。
- **预期输出：** 与配置、随机种子对应的 loss 曲线和 checkpoint。
- **常见问题：** 依赖版本、GPU 要求、动作预测长度、内存不足。
- **完成标准：** 一个 batch 能经过模型与损失函数，保存的模型能重新加载。

## Stage 3：跑 Evaluation（评测）

- **学什么：** 复位、rollout、成功判定、失败记录和推理延迟。
- **跑什么：** 在同一小型仿真任务上运行官方评测，固定回合数和随机种子。[LeRobot 评测说明](https://huggingface.co/docs/lerobot/main/adding_benchmarks)。
- **看哪些文件：** eval 脚本、成功判定、动作后处理和环境包装器。
- **预期输出：** 成功次数/总次数、失败原因和一段动作轨迹。
- **常见问题：** 训练与评测预处理不一致、加载旧 checkpoint、复位不一致。
- **完成标准：** 能指出某次 observation 如何变成 action，并复查指标变化。

## Stage 4：比较动作生成方法

- **学什么：** ACT 动作块、Diffusion Policy（扩散策略）和 Flow Matching（流匹配）。
- **跑什么：** 在现有环境允许时试 [Diffusion Policy 官方小例子](https://github.com/real-stanford/diffusion_policy)，否则先走读推理代码；比较输出 shape 和延迟。
- **看哪些文件：** policy 配置、噪声/采样器、loss、采样和评测。
- **预期输出：** 带维度和单位的动作序列，以及一次推理的耗时。
- **常见问题：** 采样器不匹配、延迟过大、动作归一化不一致。
- **完成标准：** 能解释生成式方法为什么能表示多种可行动作，以及速度代价。

## Stage 5：理解 OpenVLA 管线

- **学什么：** 视觉/语言编码、机器人数据混合、动作 token、微调与在线解码。
- **跑什么：** 先阅读 [OpenVLA 官方仓库](https://github.com/openvla/openvla) 的配置和推理示例；只有本地已有合适权重且资源、许可允许时才运行模型。
- **看哪些文件：** README、RLDS 数据转换、`vla-scripts/train.py`、动作解码和评测。
- **预期输出：** “Vision + Language + Robot State → Model → Action”的数据流图，外加显存和延迟估算。
- **常见问题：** 动作尺度与平台不匹配、7B 权重缺失、相机视角变化。
- **完成标准：** 能指出语言和图像在哪里融合、动作如何转成机器人命令。

## Stage 6：理解 SayCan 与 VLA 的区别

- **学什么：** Say（语言上合适）、Can（当前可执行）、Skill（技能）、Affordance（可供性）和 Value Function（价值函数）。
- **跑什么：** 对照 [[02_Papers/01_VLA/SayCan|SayCan]] 与 [[02_Papers/01_VLA/OpenVLA|OpenVLA]]，手画一项任务的输入、中间决策、输出和失败点；不需要下载模型。[SayCan 项目](https://say-can.github.io/)。
- **看哪些文件：** 两篇论文的方法、失败案例以及已发布的官方代码。
- **预期输出：** 高层技能规划与端到端动作预测的对照图。
- **常见问题：** 把“规划选对技能”误当成“物理执行成功”。
- **完成标准：** 能解释 SayCan 为什么需要底层技能策略，以及 VLA 为什么仍可能需要任务监控。

## Stage 7：连接双臂普通夹爪真机

- **学什么：** 双臂坐标系、同步、夹爪语义、碰撞边界、安全和数据来源。
- **跑什么：** 先离线回放一条双臂 episode，再在仿真中 dry run；真机仅按本地批准的安全规程进行。
- **看哪些文件：** 机器人接口、标定、数据 schema、动作适配器、评测和急停文档。
- **预期输出：** 一项任务的可重复 dry run 与成功/失败记录方案。
- **常见问题：** 左右臂交叉、坐标系错位、异步动作、未知接触力。
- **完成标准：** 能说明所需数据、动作空间、双臂协调、评测和失败恢复，并安全完成监督下的 rollout。

**明天第一件事：** 只打开一条能合法访问的 episode，写下 observation/action 的 shape、单位、坐标系和采样频率。不要先训练大型 VLA。
