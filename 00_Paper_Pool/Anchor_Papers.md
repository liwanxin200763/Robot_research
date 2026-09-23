# 锚点论文

选择锚点时综合库内被引用次数、领域作用和项目相关性，**不只按 Citation Count 排名**。引文数对应 2026-09-23 核验的一条 OpenAlex 或 Semantic Scholar 记录；Unknown 表示身份/接口覆盖尚未解决，不代表零引用。库内引用图谱仍是部分覆盖。

## [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]]

- 入选原因：汇集跨机器人本体的数据，并提供 RT-X 基线；库内多篇论文共同引用。
- Citation Count：1192 （来源：https://www.semanticscholar.org/paper/ef7d31137ef06c5be8c2824ecc5af6ce3358cc8f）。
- 库内被引用：21 verified direct edges.
- 核心思路：把不同机构、不同机器人采集的操作数据标准化，检验混合数据能否帮助跨本体策略。
- 后续方向：先检查动作归一化与数据划分，再评估双臂普通夹爪能否获益。
- 重要前置论文（已核验库内引用）：当前图谱尚无已核验的库内前置引用
- 重要后续论文（已核验库内引用）：[[02_Papers/01_VLA/Actions_as_Language|Actions as Language]], [[02_Papers/01_VLA/CoT-VLA|CoT-VLA]], [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]], [[02_Papers/01_VLA/Octo|Octo]], [[02_Papers/01_VLA/OpenVLA|OpenVLA]]

## [[02_Papers/01_VLA/OpenVLA|OpenVLA]]

- 入选原因：开放的通用 VLA 基线，便于比较微调和真机迁移。
- Citation Count：43 （来源：https://openalex.org/W4399695759）。
- 库内被引用：19 verified direct edges.
- 核心思路：以约 97 万条真机轨迹训练 7B VLA，并公开模型与代码。
- 后续方向：重点比较新任务微调、双臂动作接口和推理延迟。
- 重要前置论文（已核验库内引用）：[[02_Papers/01_VLA/Octo|Octo]], [[02_Papers/10_Benchmark_Dataset/DROID|DROID]], [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]]
- 重要后续论文（已核验库内引用）：[[02_Papers/01_VLA/Actions_as_Language|Actions as Language]], [[02_Papers/01_VLA/BridgeVLA|BridgeVLA]], [[02_Papers/01_VLA/CoT-VLA|CoT-VLA]], [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]], [[02_Papers/01_VLA/ReconVLA|ReconVLA]]

## [[02_Papers/01_VLA/Octo|Octo]]

- 入选原因：开放的通用机器人策略，是共享数据走向可复用策略的重要节点。
- Citation Count：102 （来源：https://openalex.org/W4402353985）。
- 库内被引用：18 verified direct edges.
- 核心思路：在 Open X-Embodiment 约 80 万条轨迹上训练 Transformer 策略，尝试跨任务和跨机器人泛化。
- 后续方向：比较不同本体的数据混合与动作块设计。
- 重要前置论文（已核验库内引用）：[[02_Papers/01_VLA/SayCan|SayCan]], [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]]
- 重要后续论文（已核验库内引用）：[[02_Papers/01_VLA/Actions_as_Language|Actions as Language]], [[02_Papers/01_VLA/CoT-VLA|CoT-VLA]], [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]], [[02_Papers/01_VLA/OpenVLA|OpenVLA]], [[02_Papers/01_VLA/ReconVLA|ReconVLA]]

## [[02_Papers/10_Benchmark_Dataset/DROID|DROID]]

- 入选原因：多场景真机操作数据，为泛化和数据覆盖研究提供公共资源。
- Citation Count：Unknown （来源：exact scholarly work unresolved）。
- 库内被引用：14 verified direct edges.
- 核心思路：收集约 6.5 万条示范、350 小时交互，覆盖大量场景与任务。
- 后续方向：分析示范分布、失败样本和两臂任务的数据缺口。
- 重要前置论文（已核验库内引用）：当前图谱尚无已核验的库内前置引用
- 重要后续论文（已核验库内引用）：[[02_Papers/01_VLA/Actions_as_Language|Actions as Language]], [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]], [[02_Papers/01_VLA/OpenVLA|OpenVLA]], [[02_Papers/01_VLA/RoboMonkey|RoboMonkey]], [[02_Papers/01_VLA/SpatialVLA|SpatialVLA]]

## [[02_Papers/03_Bimanual/RDT-1B|RDT-1B]]

- 入选原因：面向双臂操作的 Diffusion Transformer，与本项目硬件形态直接相关。
- Citation Count：Unknown （来源：exact scholarly work unresolved）。
- 库内被引用：10 verified direct edges.
- 核心思路：用扩散式动作生成建立双臂基础策略。
- 后续方向：检验普通夹爪、协调动作表示及真机评测的迁移条件。
- 重要前置论文（已核验库内引用）：当前图谱尚无已核验的库内前置引用
- 重要后续论文（已核验库内引用）：[[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]], [[02_Papers/01_VLA/SP-VLA|SP-VLA]], [[02_Papers/01_VLA/SimpleVLA-RL|SimpleVLA-RL]], [[02_Papers/01_VLA/SpatialVLA|SpatialVLA]], [[02_Papers/01_VLA/VideoVLA|VideoVLA]]

## [[02_Papers/01_VLA/SayCan|SayCan]]

- 入选原因：把语言规划与机器人技能可执行性结合，是 Grounding 的重要前置工作。
- Citation Count：523 （来源：https://openalex.org/W4224912544）。
- 库内被引用：7 verified direct edges.
- 核心思路：用语言模型评估技能与指令的匹配，再用技能价值估计当前是否可执行。
- 后续方向：研究动作前可行性检查、执行后成功判断和失败恢复。
- 重要前置论文（已核验库内引用）：当前图谱尚无已核验的库内前置引用
- 重要后续论文（已核验库内引用）：[[02_Papers/01_VLA/Actions_as_Language|Actions as Language]], [[02_Papers/01_VLA/Octo|Octo]], [[02_Papers/01_VLA/RoboMamba|RoboMamba]], [[02_Papers/09_Survey_Review/A_Survey_on_Robotics_with_Foundation_Models_Toward_Embodied_AI|A Survey on Robotics with Foundation Models Toward Embodied AI]], [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective|A Survey on Vision-Language-Action Models An Action Tokenization Perspective]]

## [[02_Papers/06_Diffusion_Flow_IL_RL/3D_Diffuser_Actor|3D Diffuser Actor]]

- 入选原因：代表三维场景条件化的生成式动作方法。
- Citation Count：4 （来源：https://openalex.org/W4391949089）。
- 库内被引用：6 verified direct edges.
- 核心思路：把三维场景和动作结构用于扩散式策略，比较不同表示与预测目标。
- 后续方向：研究双夹爪位姿生成及不同三维输入的成本。
- 重要前置论文（已核验库内引用）：当前图谱尚无已核验的库内前置引用
- 重要后续论文（已核验库内引用）：[[02_Papers/01_VLA/BridgeVLA|BridgeVLA]], [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]], [[02_Papers/02_Robot_Manipulation/VidMan|VidMan]], [[02_Papers/03_Bimanual/AnyBimanual|AnyBimanual]], [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI|A Survey on Vision-Language-Action Models for Embodied AI]]

## [[02_Papers/01_VLA/ReconVLA|ReconVLA]]

- 入选原因：直接研究 VLA 视觉注意与目标区域 Grounding 的偏差。
- Citation Count：3 （来源：https://openalex.org/W7137985120）。
- 库内被引用：1 verified direct edges.
- 核心思路：通过重建操作目标的注视区域，促使视觉表示更聚焦任务目标，同时保留动作预测。
- 后续方向：验证杂乱场景中的目标定位能否改善双臂真机执行。
- 重要前置论文（已核验库内引用）：[[02_Papers/01_VLA/3D-VLA|3D-VLA]], [[02_Papers/01_VLA/Octo|Octo]], [[02_Papers/01_VLA/OpenVLA|OpenVLA]], [[02_Papers/01_VLA/RoboGround|RoboGround]], [[02_Papers/02_Robot_Manipulation/VidMan|VidMan]]
- 重要后续论文（已核验库内引用）：[[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards a Unified Understanding of Robot Manipulation A Comprehensive Survey]]

Citation Count 只是社区关注/使用的一个指标。选择阅读对象还应结合年份、Venue、证据质量、开源程度、真机与双臂适配性、失败案例和研究缺口价值。
