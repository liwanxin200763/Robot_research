# 机器人学习仓库代码阅读顺序

拿到新 repo 时，先追踪“一条数据如何变成动作”，不要从模型类逐行读起。文件名因仓库而异，可以按函数和配置键搜索。

| 顺序 | 常见文件 | 重点看什么 | 看完应能回答 |
|---|---|---|---|
| README | `README.md` | 支持哪些任务、环境安装、最小训练/评测命令 | 最小官方例子是什么？ |
| environment / requirements | `requirements.txt`、`environment.yml`、`pyproject.toml` | Python、CUDA、仿真器、机器人驱动版本 | 当前机器能否隔离运行？ |
| config | `configs/*.yaml` | 数据路径、相机、动作维度、预测长度、随机种子 | 哪份配置对应论文基线？ |
| dataset | `dataset.py`、数据说明 | Episode 格式、单位、划分、许可、归一化 | 单个样本是什么？ |
| dataloader | `dataloader.py`、`collate_fn` | 图像变换、时间窗口、mask、左右臂顺序 | 一个 batch 是否时序对齐？ |
| model / policy | `policy.py`、`model.py` | 观测编码、语言融合、动作预测 | 从哪个张量得到动作？ |
| action head | `action_head.py`、decoder | token/位姿解码、夹爪符号、输出维度 | 每个输出量对应哪条物理命令？ |
| loss | `loss.py` | 监督目标、权重、mask、扩散时间步 | 模型具体在优化什么？ |
| train | `train.py`、launcher | 采样、优化器、日志、保存周期 | 能否完成一次短运行？ |
| checkpoint | 加载与保存代码 | 权重、配置、归一化参数、版本 | 重载后输出是否一致？ |
| inference | `inference.py`、rollout | 在线预处理、动作解码、控制频率 | 真机上每一步运行什么？ |
| eval | `eval.py`、成功判定 | 复位、回合数、指标、失败日志 | 不同实验结果能否直接比较？ |
| robot interface | driver、controller、IK | 坐标变换、限幅、急停、碰撞规则 | 命令在目标硬件上是否有效？ |

具体做法：先打印一条 episode 和一个 batch 的 shape；再沿 `batch → policy → loss` 与 `observation → policy → action → environment` 两条线走读。双臂项目要在每个边界检查左/右顺序、单位和时间同步。

可练习的官方仓库：[ACT](https://github.com/tonyzhaozh/act)、[LeRobot](https://github.com/huggingface/lerobot)、[Diffusion Policy](https://github.com/real-stanford/diffusion_policy)、[OpenVLA](https://github.com/openvla/openvla)。
