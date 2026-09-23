# 一次机器人学习实验怎么跑

先有明确任务和安全边界，再收数据、训练、部署、评测。任何一步的定义变化都要记录，否则不同实验的成功率不能直接比较。

| 步骤 | 输入 → 输出 | 对应代码模块 | 常见错误 |
|---|---|---|---|
| 1 定义 Task | 任务目标 → 成功/失败/复位规则 | 任务配置 | 成功条件模糊 |
| 2 确定 Observation | 相机和传感器 → 带时间戳的观测 | 相机、状态适配器 | 多视角不同步 |
| 3 确定 Action Space | 机器人能力 → 命令维度、单位和范围 | action adapter、controller | 坐标系或夹爪符号错误 |
| 4 Teleoperation | 人的控制 → 机器人运动 | 遥操作驱动 | 延迟或越界 |
| 5 收 Demonstrations | 多次操作 → 标注的示范 | recorder | 只保留成功，丢失失败信息 |
| 6 保存 Episodes | 连续采样 → 完整回合 | episode writer | 缺少终止事件 |
| 7 Dataset preprocessing | 原始数据 → 统一格式和划分 | 数据转换脚本 | 训练/测试泄漏 |
| 8 DataLoader | Episodes → batch | Dataset、`collate_fn` | 图像与动作窗口错位 |
| 9 Policy training | batch → 模型参数 | model、train loop | 输入维度错误 |
| 10 Loss | 预测和目标 → 标量误差 | loss 函数 | 错误 mask 无效时间步 |
| 11 Validation | 留出数据 → 诊断结果 | validation loop | 用测试集调参 |
| 12 Checkpoint | 权重和配置 → 可重现文件 | save/load | 未保存归一化参数 |
| 13 Inference | 当前观测 → 预测动作 | rollout、policy | 在线预处理与训练不同 |
| 14 Robot rollout | 动作命令 → 真机运动 | controller、robot API | 频率不匹配或碰撞 |
| 15 Evaluation | 多次尝试 → 成功率与延迟 | eval harness | 每次复位条件变化 |
| 16 Failure analysis | 日志/视频 → 失败分类 | 分析脚本 | 把一个演示视频当成实验结论 |

实验记录至少保存：任务 ID、数据版本、代码 commit、配置、checkpoint 标识、机器人/仿真器版本、随机种子、评测回合数、成功次数、失败类别和允许保存的视频链接。单次成功演示不是成功率。

双臂普通夹爪要额外记录：哪只手先接触物体、左右臂是否同步、是否发生碰撞/夹爪滑脱，以及失败后是否有人干预。首次成功和恢复后成功要分别统计。

具体从 [[08_Tech_Stack/Minimal_Reproduction_Path|最小复现路线]] 的 Stage 1 开始。
