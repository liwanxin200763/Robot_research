# 机器人实验技术栈

**Human Task（人的任务）→ Language Instruction（语言指令）→ Observation（观测）→ Teleoperation（遥操作）→ Demonstration（示范）→ Episode / Trajectory（回合 / 轨迹）→ Dataset（数据集）→ DataLoader（数据加载器）→ Policy（策略）→ Training（训练）→ Loss（损失）→ Checkpoint（模型检查点）→ Inference（推理）→ Action（动作）→ Controller（控制器）→ Robot（机器人）→ Environment（环境）→ Evaluation（评测）**。

一项实验不是“训练一个模型”这么简单。前半段决定数据是否可信，中间决定策略到底学到了什么，后半段决定动作能否安全执行、结果能否重复。

| 环节 | 输入 → 输出 | 常见实现 | 与当前项目的关系 |
|---|---|---|---|
| Human Task | 目标 → 成功、失败和复位规则 | 任务说明与评测配置 | 先定义一个可重复的双臂任务。 |
| Language Instruction | 目标 → 给模型或规划器的文字 | prompt、数据字段 | 检查语言是否指向正确物体与动作。 |
| Observation | 相机和机器人传感器 → 带时间戳的状态 | 相机驱动、状态适配器 | 对齐两只手臂、夹爪和多个相机。 |
| Teleoperation | 人的操作 → 机器人指令 | 主从臂、手柄、VR | 安全采集普通夹爪的动作。 |
| Demonstration | 一次操作 → 有标签的样例 | 录制器 | 成功和失败的示范分开记录。 |
| Episode / Trajectory | 连续采样 → 一次完整尝试 | 回合存储 | 保留左右臂同步与任务终止信息。 |
| Dataset | 多个回合 → 统一格式和划分 | LeRobot、RLDS 等 | 写清坐标系、单位、物体和场景划分。 |
| DataLoader | 存储样本 → 训练 batch | PyTorch Dataset | 保证图像、语言、状态和动作窗口对齐。 |
| Policy | 当前输入 → 动作建议 | ACT、Diffusion Policy、VLA | 比较双臂动作头的表达方式。 |
| Training / Loss | batch 与目标动作 → 更新参数 | 训练循环、BC 或生成式损失 | 检查左右臂是否被正确监督。 |
| Checkpoint | 参数和配置 → 可重现模型 | 权重、配置、归一化参数 | 每次实验绑定数据版本和动作定义。 |
| Inference | 实时观测 → 在线预测 | rollout 循环 | 测量延迟，并留出失败检测接口。 |
| Action | 预测结果 → 有单位的命令 | action decoder | 明确关节/笛卡尔空间、频率和夹爪方向。 |
| Controller | 命令 → 满足约束的执行目标 | IK、轨迹控制、限幅 | 加入工作空间和碰撞约束。 |
| Robot / Environment | 执行目标 → 下一时刻的真实状态 | 驱动、真机或仿真器 | 记录接触、复位和 Sim2Real 差异。 |
| Evaluation | 多次 rollout → 成功率和失败类型 | 评测脚本 | 首次成功与恢复后成功分开统计。 |

两只普通夹爪尤其要明确：左/右通道顺序、各自坐标系、夹爪开合符号、同步策略和允许的接触区域。数据写错这些，模型即使能运行也可能学到错误动作。

入门时参照 [LeRobot 文档](https://huggingface.co/docs/lerobot/main/index)、[ACT 官方仓库](https://github.com/tonyzhaozh/act)、[Diffusion Policy 官方仓库](https://github.com/real-stanford/diffusion_policy) 和 [OpenVLA 官方仓库](https://github.com/openvla/openvla)。术语见 [[08_Tech_Stack/Glossary|Glossary]]。
