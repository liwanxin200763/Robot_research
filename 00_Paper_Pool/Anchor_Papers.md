# 锚点论文

选择锚点时综合库内被引用次数、领域作用和项目相关性，**不只按 Citation Count 排名**。引文数对应 2026-09-23 核验的一条 OpenAlex 或 Semantic Scholar 记录；Unknown 表示身份/接口覆盖尚未解决，不代表零引用。库内引用图谱仍是部分覆盖。

## [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment：机器人学习数据集与 RT-X 模型]]

- 入选原因：汇集跨机器人本体的数据，并提供 RT-X 基线；库内多篇论文共同引用。
- Citation Count：1192 （来源：https://www.semanticscholar.org/paper/ef7d31137ef06c5be8c2824ecc5af6ce3358cc8f）。
- 库内被引用：21 verified direct edges.
- 核心思路：把不同机构、不同机器人采集的操作数据标准化，检验混合数据能否帮助跨本体策略。
- 后续方向：先检查动作归一化与数据划分，再评估双臂普通夹爪能否获益。
- 重要前置论文（已核验库内引用）：当前图谱尚无已核验的库内前置引用
- 重要后续论文（已核验库内引用）：[[02_Papers/01_VLA/Actions_as_Language|将动作视为语言：在避免灾难性遗忘的条件下将 VLM 微调为 VLA]], [[02_Papers/01_VLA/CoT-VLA|CoT-VLA：面向 VLA 的视觉思维链推理]], [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA：通过统一扩散与自回归扩展机器人基础模型]], [[02_Papers/01_VLA/Octo|Octo：开源通用机器人策略]], [[02_Papers/01_VLA/OpenVLA|OpenVLA：开源视觉—语言—动作模型]]

## [[02_Papers/01_VLA/OpenVLA|OpenVLA：开源视觉—语言—动作模型]]

- 入选原因：开放的通用 VLA 基线，便于比较微调和真机迁移。
- Citation Count：43 （来源：https://openalex.org/W4399695759）。
- 库内被引用：19 verified direct edges.
- 核心思路：以约 97 万条真机轨迹训练 7B VLA，并公开模型与代码。
- 后续方向：重点比较新任务微调、双臂动作接口和推理延迟。
- 重要前置论文（已核验库内引用）：[[02_Papers/01_VLA/Octo|Octo：开源通用机器人策略]], [[02_Papers/10_Benchmark_Dataset/DROID|DROID：大规模自然场景机器人操作数据集]], [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment：机器人学习数据集与 RT-X 模型]]
- 重要后续论文（已核验库内引用）：[[02_Papers/01_VLA/Actions_as_Language|将动作视为语言：在避免灾难性遗忘的条件下将 VLM 微调为 VLA]], [[02_Papers/01_VLA/BridgeVLA|BridgeVLA：通过输入—输出对齐高效学习三维操作]], [[02_Papers/01_VLA/CoT-VLA|CoT-VLA：面向 VLA 的视觉思维链推理]], [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA：通过统一扩散与自回归扩展机器人基础模型]], [[02_Papers/01_VLA/ReconVLA|ReconVLA：以重建增强机器人感知的 VLA 模型]]

## [[02_Papers/01_VLA/Octo|Octo：开源通用机器人策略]]

- 入选原因：开放的通用机器人策略，是共享数据走向可复用策略的重要节点。
- Citation Count：102 （来源：https://openalex.org/W4402353985）。
- 库内被引用：18 verified direct edges.
- 核心思路：在 Open X-Embodiment 约 80 万条轨迹上训练 Transformer 策略，尝试跨任务和跨机器人泛化。
- 后续方向：比较不同本体的数据混合与动作块设计。
- 重要前置论文（已核验库内引用）：[[02_Papers/01_VLA/SayCan|SayCan：以机器人能力约束语言指令的落地执行]], [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment：机器人学习数据集与 RT-X 模型]]
- 重要后续论文（已核验库内引用）：[[02_Papers/01_VLA/Actions_as_Language|将动作视为语言：在避免灾难性遗忘的条件下将 VLM 微调为 VLA]], [[02_Papers/01_VLA/CoT-VLA|CoT-VLA：面向 VLA 的视觉思维链推理]], [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA：通过统一扩散与自回归扩展机器人基础模型]], [[02_Papers/01_VLA/OpenVLA|OpenVLA：开源视觉—语言—动作模型]], [[02_Papers/01_VLA/ReconVLA|ReconVLA：以重建增强机器人感知的 VLA 模型]]

## [[02_Papers/10_Benchmark_Dataset/DROID|DROID：大规模自然场景机器人操作数据集]]

- 入选原因：多场景真机操作数据，为泛化和数据覆盖研究提供公共资源。
- Citation Count：Unknown （来源：exact scholarly work unresolved）。
- 库内被引用：14 verified direct edges.
- 核心思路：收集约 6.5 万条示范、350 小时交互，覆盖大量场景与任务。
- 后续方向：分析示范分布、失败样本和两臂任务的数据缺口。
- 重要前置论文（已核验库内引用）：当前图谱尚无已核验的库内前置引用
- 重要后续论文（已核验库内引用）：[[02_Papers/01_VLA/Actions_as_Language|将动作视为语言：在避免灾难性遗忘的条件下将 VLM 微调为 VLA]], [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA：通过统一扩散与自回归扩展机器人基础模型]], [[02_Papers/01_VLA/OpenVLA|OpenVLA：开源视觉—语言—动作模型]], [[02_Papers/01_VLA/RoboMonkey|RoboMonkey：扩展 VLA 的测试时采样与验证]], [[02_Papers/01_VLA/SpatialVLA|SpatialVLA：探索 VLA 模型的空间表征]]

## [[02_Papers/03_Bimanual/RDT-1B|RDT-1B：面向双臂操作的扩散基础模型]]

- 入选原因：面向双臂操作的 Diffusion Transformer，与本项目硬件形态直接相关。
- Citation Count：Unknown （来源：exact scholarly work unresolved）。
- 库内被引用：10 verified direct edges.
- 核心思路：用扩散式动作生成建立双臂基础策略。
- 后续方向：检验普通夹爪、协调动作表示及真机评测的迁移条件。
- 重要前置论文（已核验库内引用）：当前图谱尚无已核验的库内前置引用
- 重要后续论文（已核验库内引用）：[[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA：通过统一扩散与自回归扩展机器人基础模型]], [[02_Papers/01_VLA/SP-VLA|SP-VLA：通过联合模型调度与 Token 剪枝加速 VLA]], [[02_Papers/01_VLA/SimpleVLA-RL|SimpleVLA-RL：通过强化学习扩展 VLA 训练]], [[02_Papers/01_VLA/SpatialVLA|SpatialVLA：探索 VLA 模型的空间表征]], [[02_Papers/01_VLA/VideoVLA|VideoVLA：让视频生成模型成为可泛化的机器人操作策略]]

## [[02_Papers/01_VLA/SayCan|SayCan：以机器人能力约束语言指令的落地执行]]

- 入选原因：把语言规划与机器人技能可执行性结合，是 Grounding 的重要前置工作。
- Citation Count：523 （来源：https://openalex.org/W4224912544）。
- 库内被引用：7 verified direct edges.
- 核心思路：用语言模型评估技能与指令的匹配，再用技能价值估计当前是否可执行。
- 后续方向：研究动作前可行性检查、执行后成功判断和失败恢复。
- 重要前置论文（已核验库内引用）：当前图谱尚无已核验的库内前置引用
- 重要后续论文（已核验库内引用）：[[02_Papers/01_VLA/Actions_as_Language|将动作视为语言：在避免灾难性遗忘的条件下将 VLM 微调为 VLA]], [[02_Papers/01_VLA/Octo|Octo：开源通用机器人策略]], [[02_Papers/01_VLA/RoboMamba|RoboMamba：用于机器人推理与操作的高效 VLA 模型]], [[02_Papers/09_Survey_Review/A_Survey_on_Robotics_with_Foundation_Models_Toward_Embodied_AI|基础模型赋能机器人：迈向具身 AI 的综述]], [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective|从动作 Token 化视角综述 VLA 模型]]

## [[02_Papers/06_Diffusion_Flow_IL_RL/3D_Diffuser_Actor|3D Diffuser Actor：基于三维场景表征的策略扩散]]

- 入选原因：代表三维场景条件化的生成式动作方法。
- Citation Count：4 （来源：https://openalex.org/W4391949089）。
- 库内被引用：6 verified direct edges.
- 核心思路：把三维场景和动作结构用于扩散式策略，比较不同表示与预测目标。
- 后续方向：研究双夹爪位姿生成及不同三维输入的成本。
- 重要前置论文（已核验库内引用）：当前图谱尚无已核验的库内前置引用
- 重要后续论文（已核验库内引用）：[[02_Papers/01_VLA/BridgeVLA|BridgeVLA：通过输入—输出对齐高效学习三维操作]], [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA：通过统一扩散与自回归扩展机器人基础模型]], [[02_Papers/02_Robot_Manipulation/VidMan|VidMan：利用视频扩散模型的隐式动力学改进机器人操作]], [[02_Papers/03_Bimanual/AnyBimanual|AnyBimanual：迁移单臂策略以实现通用双臂操作]], [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI|面向具身 AI 的 VLA 模型综述]]

## [[02_Papers/01_VLA/ReconVLA|ReconVLA：以重建增强机器人感知的 VLA 模型]]

- 入选原因：直接研究 VLA 视觉注意与目标区域 Grounding 的偏差。
- Citation Count：3 （来源：https://openalex.org/W7137985120）。
- 库内被引用：1 verified direct edges.
- 核心思路：通过重建操作目标的注视区域，促使视觉表示更聚焦任务目标，同时保留动作预测。
- 后续方向：验证杂乱场景中的目标定位能否改善双臂真机执行。
- 重要前置论文（已核验库内引用）：[[02_Papers/01_VLA/3D-VLA|3D-VLA：基于三维视觉—语言—动作的生成式世界模型]], [[02_Papers/01_VLA/Octo|Octo：开源通用机器人策略]], [[02_Papers/01_VLA/OpenVLA|OpenVLA：开源视觉—语言—动作模型]], [[02_Papers/01_VLA/RoboGround|RoboGround：利用有视觉定位能力的视觉—语言先验实现机器人操作]], [[02_Papers/02_Robot_Manipulation/VidMan|VidMan：利用视频扩散模型的隐式动力学改进机器人操作]]
- 重要后续论文（已核验库内引用）：[[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|迈向统一理解机器人操作：综合综述]]

Citation Count 只是社区关注/使用的一个指标。选择阅读对象还应结合年份、Venue、证据质量、开源程度、真机与双臂适配性、失败案例和研究缺口价值。
