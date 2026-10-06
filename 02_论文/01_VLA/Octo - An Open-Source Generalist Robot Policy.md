# Octo: An Open-Source Generalist Robot Policy

## 基本信息

- 作者：Dibya Ghosh、Homer Walke、Karl Pertsch、Kevin Black、Oier Mees、Sudeep Dasari、Joey Hejna、Tobias Kreiman、Charles Xu、Jianlan Luo、You Liang Tan、Lawrence Yunliang Chen、Quan Vuong、Ted Xiao、Pannag Sanketi、Dorsa Sadigh、Chelsea Finn、Sergey Levine
- 年份：2024
- 发表 venue：RSS
- 论文类型：会议论文
- 研究方向：VLA
- 关键词：通用机器人策略；Open X-Embodiment；Diffusion Policy；跨本体；双臂操作；IL
- 论文链接：[Robotics Proceedings](https://roboticsproceedings.org/rss20/p090.html)
- DOI：[10.15607/RSS.2024.XX.090](https://doi.org/10.15607/RSS.2024.XX.090)
- arXiv：[2405.12213](https://arxiv.org/abs/2405.12213)
- 项目主页：[项目主页](https://octo-models.github.io/)
- 代码：[GitHub](https://github.com/octo-models/octo)
- 本地 PDF：[[00_论文池/PDFs/01_VLA/Octo.pdf|查看 PDF]]
- 引用量：2275
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

针对每个机器人和任务从零收集示范、单独训练策略成本很高；跨机器人共享的数据已有规模，但观测、动作空间和任务标注并不统一。（论文第 I–II 节）

### 2. 论文要解决的问题

建立可公开复现的通用机器人策略，让同一预训练模型既能在已有机器人上直接执行，也能以少量目标域示范适配新相机、传感器、动作空间及双臂形态。（第 I、III 节）

### 3. 之前方法存在的问题

RT-X 等模型对输入和动作接口要求较固定，较大模型未完全开放，针对新传感器或新动作维度微调困难。单一机器人数据训练的策略泛化范围更窄。（第 I–II 节）

### 4. 核心思路

把语言或目标图像、历史视觉观测分别转成 Token，送入可按模块扩展的 Transformer，随后由轻量 Diffusion Head 生成连续 Action Chunk。遇到新机器人时增加输入适配器和动作头，保留并微调预训练主干。（第 III 节，图 2）

### 5. 方法与系统结构

冻结的 T5-base 编码语言，浅层 CNN 将第三视角/腕部图像切为 Patch；Block-wise attention 的 Transformer 汇合任务与观察 Token，独立 Readout Token 读出动作条件。小型 Diffusion Head 迭代去噪，输出连续动作序列；主干只需前向一次，去噪集中在动作头。（第 III-A、III-C 节，图 2）

### 6. 输入信息

语言指令或目标图像，加上最多两个时间步的 RGB 图像；预训练兼容第三视角及腕部相机。新域微调可加力/力矩或本体状态，但论文附录指出，预训练中直接增加本体状态输入的探索反而不佳，不能说原模型普遍依赖本体状态。（第 III、IV 节；附录 E、F）

### 7. 输出 / 动作表示

预训练数据统一为末端位置/姿态增量与夹爪状态，预测连续 Action Chunk；Diffusion Head 按 DDPM 目标训练。针对 ALOHA 双臂任务，重新初始化输出到 14 维动作空间的动作头，即双臂各 6 维关节位置加各 1 维夹爪位置。（第 III-C 节；附录 F）

### 8. 数据来源与采集方式

从 Open X-Embodiment 约 150 万条机器人 episode 中挑选 25 个数据集、约 80 万条轨迹。原始数据汇集不同机构的真实机器人示范，包含语言标注或目标图像；例如双臂下游实验使用单独采集的 ALOHA 示范。论文没有把全部 80 万条都描述成统一采集方式。（第 III-B 节，附录 C、F）

### 9. 数据处理与数据增强

筛掉缺图像、非末端增量控制、低分辨率、重复或过于狭窄的数据；按多样性调整数据集抽样权重，缺失相机通道用零填充，统一夹爪开闭表示。用未来帧重标记目标图像，随机丢弃语言/目标条件；第三视角随机裁切、缩放到 256×256 并做颜色扰动，腕部相机不做随机裁切、缩放到 128×128。（第 III-B、III-D 节，附录 C–D）

### 10. 训练方式

多数据集模仿学习预训练，连续动作使用 DDPM 去噪目标。Octo-Base 为 93M 参数，论文报告 TPU v4-128、300k 步、批量 2048、约 14 小时；下游约 100 条示范、微调 50k 步，单张 A5000 约 5 小时。论文方法是 Diffusion，不是 Flow Matching。（第 III-C、III-D 节）

### 11. Benchmark 与实验设置

9 个真实机器人设置、4 家机构：零样本任务覆盖 WidowX、UR5、RT-1 Robot；6 个新域微调任务包括精密插入、咖啡胶囊、烘焙、拾取、可乐罐与双臂取笔帽。指标为任务成功率；零样本对照 RT-1-X、RT-2-X，微调对照从头训练的 ResNet+Transformer Diffusion Policy 和 VC-1 视觉预训练。（第 IV 节，图 4–5、表 I）

### 12. 真机实验

WidowX、UR5、Google Robot 等执行零样本桌面操作；各选两项语言任务，每项 10 次。6 个微调域各约 100 条示范、每域 20 次评测。双臂任务在两台 ViperX 组成的 ALOHA 上，以左右腕部相机观察、关节位置与夹爪为动作，取下笔帽，测试 10 次；训练预测 64 步动作，执行 12 步后重规划。实验设置不同，控制频率不能归成一个统一值；附录给出 CMU Baking 15 Hz、Peg Insertion 策略 5 Hz 等具体例子。（第 IV 节，附录 F）

### 13. 主要实验结果

零样本语言任务：WidowX、UR5、RT-1 Robot 成功率分别为 50%、70%、80%，对应 RT-1-X 为 20%、35%、60%（图 5；项目页结果表）。六项微调任务 Octo 平均 72%，从头训练 20%，VC-1 15%；Berkeley Bimanual 80%（10 次中的 8 次），Stanford Coffee 75%，Berkeley Insertion 70%（表 I）。上述零样本测试选自预训练数据分布，不能等同未知技能泛化。

### 14. 消融实验

WidowX 四项任务平均成功率：完整 Octo-Small 83%；RT-X 较窄数据混合 60%，只用 Bridge 43%；离散动作头 18%，MSE 连续动作头 35%，ResNet-50+Transformer 70%（表 II／附录表 VI）。附录 E 还发现动作分块、两帧历史和较小视觉 Patch 有益；简单增加历史长度未进一步获益。

### 15. Failure Case

零样本新技能最困难：在 WidowX 上，新场景平均 40%，翻杯子与插槽等新技能平均仅 5%，其中插槽任务为 0%（附录表 VII）。MSE 动作头容易缓慢犹豫，离散动作头常抓取位置不准；腕部相机加入后有时反而降低微调效果。（附录 E；第 IV 节结论）

### 16. 主要局限

作者指出仅 27% 预训练数据含腕部相机、56% 含语言标注，导致腕部信息利用和语言条件表现不足；训练主要来自最优示范，尚未利用次优/在线交互数据。新技能和新场景表现下降，移动操作未覆盖。（第 IV 节结论、附录表 VII）

### 17. 与已有工作的关系

相较 RT-X 的固定接口，Octo 用模块化 Token 与动作头实现传感器、动作空间微调；与从头训练的 Diffusion Policy 或 VC-1 表征基线相比，它提供跨机器人预训练的完整策略初始化。它直接做低层控制，而 SayCan 负责高层技能选取。（第 II、IV 节）

### 18. 对当前研究方向的价值

Octo 已在 ALOHA 双臂普通夹爪取笔帽实验中达到 80%（表 I），可作为双臂少样本微调基线。对复杂双臂任务，可进一步检验双腕相机、关节动作表示和失败后重规划；这些扩展是基于论文局限的研究设想，不能当作已验证结果。

### 19. 一句话总结

Octo 用跨机器人示范预训练可扩展的 Diffusion Transformer 策略，并通过轻量输入与动作接口把它快速适配到新机器人，包括双臂任务。

## 相关论文

- [[Do As I Can, Not As I Say - Grounding Language in Robotic Affordances]]
- [[Open X-Embodiment - Robotic Learning Datasets and RT-X Models]]
- [[Actions as Language - Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting]]
- [[CoT-VLA - Visual Chain-of-Thought Reasoning for Vision-Language-Action Models]]
- [[DiffusionVLA - Scaling Robot Foundation Models via Unified Diffusion and Autoregression]]
- [[OpenVLA - An Open-Source Vision-Language-Action Model]]
- [[ReconVLA - Reconstructive Vision-Language-Action Model as Effective Robot Perceiver]]
- [[RoboMonkey - Scaling Test-Time Sampling and Verification for Vision-Language-Action Models]]
- [[SP-VLA - A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration]]
- [[SimpleVLA-RL - Scaling VLA Training via Reinforcement Learning]]
- [[SpatialVLA - Exploring Spatial Representations for Visual-Language-Action Models]]
- [[TraceVLA - Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies]]

## 来源

- 官方论文：[Robotics Proceedings](https://roboticsproceedings.org/rss20/p090.html)
- 项目主页：[项目主页](https://octo-models.github.io/)
- 官方代码：[GitHub](https://github.com/octo-models/octo)
