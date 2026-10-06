# OpenVLA: An Open-Source Vision-Language-Action Model

## 基本信息

- 作者：Moo Jin Kim、Karl Pertsch、Siddharth Karamcheti、Ted Xiao、Ashwin Balakrishna、Suraj Nair、Rafael Rafailov、Ethan Foster、Pannag Sanketi、Quan Vuong、Thomas Kollar、Benjamin Burchfiel、Russ Tedrake、Dorsa Sadigh、Sergey Levine、Percy Liang、Chelsea Finn
- 年份：2024
- 发表 venue：CoRL 2024
- 论文类型：会议论文；开放式 VLA 基础模型
- 研究方向：VLA；跨本体机器人操作；模仿学习
- 关键词：Open X-Embodiment；Prismatic VLM；DINOv2；SigLIP；Action Tokenization；LoRA
- 论文链接：[PMLR 论文](https://proceedings.mlr.press/v270/kim25c.html)
- DOI：—
- arXiv：[2406.09246](https://arxiv.org/abs/2406.09246)
- 项目主页：[OpenVLA 项目页](https://openvla.github.io/)
- 代码：[官方 GitHub](https://github.com/openvla/openvla)
- 本地 PDF：[[00_论文池/PDFs/01_VLA/OpenVLA.pdf|查看 PDF]]
- 引用量：4229
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

机器人模仿学习通常依赖特定机器、场景和任务的示范，面对新物体、干扰物和新语言指令时容易退化。互联网预训练 VLM 有较强的视觉与语义先验，但此前的大型 VLA 多为闭源，难以复现或微调到新机器人。（论文第 1 节）

### 2. 论文要解决的问题

建立可公开使用、能跨机器人直接执行且能用少量示范适配新任务的 VLA，并明确训练数据、动作接口和计算成本。（第 1、4 节）

### 3. 之前方法存在的问题

RT-2-X 的模型、数据配方和适配流程不公开；Octo 等通用策略可以迁移，却没有直接把成熟 VLM 的视觉—语言能力作为整个动作模型的可训练主干。任务窄时，单纯扩大 VLA 也未必优于专门训练的连续动作策略。（第 2、4.2 节）

### 4. 核心思路

以 Prismatic-7B VLM 为起点，将连续机器人动作逐维量化为语言模型可输出的 token；用多样的真实机器人示范训练整套模型，再针对新机器人做全参数或 LoRA 微调。（图 2；第 3 节）

### 5. 方法与系统结构

单张相机图像分别进入 DINOv2 和 SigLIP 视觉编码器，拼接特征经两层 MLP 映射到 Llama 2 7B 的嵌入空间；语言指令与视觉 token 一起进入模型，动作 token 经反量化成为机器人控制量。图 2 的三段是“双视觉编码器 → 特征投影 → 语言模型和动作反量化”。（图 2；第 3.1–3.2 节）

### 6. 输入信息

输入为 **224×224 单张 RGB 图像＋语言任务指令**。该版本不直接输入多相机历史帧或本体状态；论文没有给出触觉或点云输入。视觉编码器在机器人训练中参与微调。（第 3.2–3.4、5 节）

### 7. 输出 / 动作表示

输出单步 **7 维末端控制**：平移、旋转和夹爪命令。每个连续维度按训练数据第 1 至第 99 百分位划分为 256 个区间，替换 Llama tokenizer 中 256 个少用 token；模型自回归预测动作 token，再按目标数据集反归一化。原版没有 Diffusion 或 Flow Matching 动作头，也没有 action chunk。（图 2；第 3.2 节）

### 8. 数据来源与采集方式

从 Open X-Embodiment 社区汇集的真实机器人示范中筛出约 **97 万条轨迹**。只保留至少一台第三人称相机、单臂末端控制的操作数据，因此“跨本体训练”不等于已覆盖双臂或灵巧手。DROID 最初以 10% 混合权重加入，因动作 token 学习进展慢，最后三分之一训练阶段移除并重分配权重。（第 3.3 节；附录 A，表 3）

### 9. 数据处理与数据增强

沿用 Octo 的数据混合权重思路，降低重复而单一的数据集权重，提高场景和任务多样数据的占比。BridgeData V2 每条示范的首个全零动作会导致模型在评测时停住，作者过滤这一过渡步。224×224 与 384×384 的早期比较中性能相近，后者训练耗时约三倍。论文主文没有将某种图像增强报告为主要贡献，不能据此编造增强配方。（第 3.3–3.4 节；附录 E）

### 10. 训练方式

对 Prismatic VLM 端到端微调，仅在动作 token 上计算 next-token cross-entropy；最终训练约 **27 个 epoch**，学习率 **2×10⁻⁵**。附录 C 报告 64 张 A100 训练 14 天。新任务实验比较全量微调、仅末层、冻结视觉、sandwich 与 LoRA；LoRA rank 32 仅训练约 1.4% 参数。（第 3.2–3.4、4.3 节；附录 C）

### 11. Benchmark 与实验设置

零样本／直接部署评测包括 BridgeData V2 的 WidowX 真实机器人 **17 项任务×10 次＝170 次 rollout**，覆盖视觉、运动、物理、语义变化和语言指定目标；Google mobile manipulator **12 项×5 次＝60 次**。基线为 RT-1-X、Octo、RT-2-X，指标为按任务平均成功率，部分 Bridge 任务允许 0.5 的部分成功。新机器人适配在 Franka-Tabletop 和 Franka-DROID 与 Diffusion Policy、匹配输入输出的 Diffusion Policy、Octo 和无 OpenX 预训练的 OpenVLA 对比。（第 4 节；附录 B，表 4、6、7）

### 12. 真机实验

WidowX、Google mobile manipulator 和 Franka Panda 均为实体机器人。Franka-Tabletop 的控制频率为 **5 Hz**，Franka-DROID 为 **15 Hz**；后者含桌面清扫及干扰物测试。模型在单张相机画面上决策；论文没有给这三套真机平台统一的摄像头安装说明，不能写成相同观测硬件。Franka 每任务微调示范数随任务变化，正文概括为约 10–100 条，附录参数高效微调子集用 50／150 条；不同实验子集不可混为一组。（第 4.1–4.3 节；附录 B，表 7、8）

### 13. 主要实验结果

BridgeData V2 全 17 任务中 OpenVLA 平均 **70.6±3.2%**，RT-2-X **50.6±3.5%**、Octo **20.0±2.6%**、RT-1-X **18.5±2.7%**（表 4）。Google 机器人 12 任务中 OpenVLA **85.0±4.6%**，RT-2-X **78.3±5.4%**，两者误差区间重叠，论文视为相近（表 6）。Franka 适配附录表 7 在所列任务中报告 OpenVLA 的平均成功率高于对照，但单指令“倒玉米”中 Diffusion Policy 仍更好；不能概括为所有任务都领先。LoRA rank 32 在 33 次 rollout 子集中为 **68.2±7.5%**，全量微调 **69.7±7.2%**（表 1）。

### 14. 消融实验

Bridge 八任务子集里，完整 OpenVLA **76.3±4.8%**，只用 Bridge 训练 **45.6±5.6%**，再去除 DINOv2 为 **40.6±5.5%**：数据多样性的作用大于双视觉编码器增益（附录 F，表 9）。其他视觉编码器实验中，参与微调平均 **80.0%**，冻结视觉 **46.7%**，但该子集与表 9 设置不同，不能直接拼成统一对照（表 10）。4-bit 量化在八任务非阻塞评测中 **71.9±4.7%**，接近 bfloat16 的 **71.3±4.8%**；8-bit 因推理变慢降到 **58.1±5.1%**（表 2）。

### 15. Failure Case

未过滤 Bridge 的全零初始动作时，模型会反复预测零动作、在真机评测中停住；附录 E 给出过滤后改善的处理。狭窄单指令高精度任务中，连续动作的 Diffusion Policy 轨迹更平滑；对某些新物体或语言组合，表 4 仍有失败。这些是论文报告的具体边界，不推断额外双臂失败类型。（第 4.2 节；附录 E，表 4、7）

### 16. 主要局限

**作者指出：**单图输入、缺本体状态和多相机历史；模型较大导致控制频率低；模型大小、联合互联网数据训练及视觉表征等设计尚未系统探索。附录 C 报告 RTX 4090 上约 **6 Hz** 推理，难直接满足如 ALOHA 50 Hz 的任务。**文献库分析：**其预训练数据约束为单臂末端动作，移到普通夹爪双臂协同需要重建观测和联合动作接口；这是尚待实验的适配问题。（第 5 节；附录 C）

### 17. 与已有工作的关系

[[02_论文/01_VLA/Octo - An Open-Source Generalist Robot Policy|Octo]]提供开放的跨机器人策略及数据混合参照；OpenVLA 进一步用完整预训练 VLM 直接预测动作 token。[[02_论文/10_基准测试与数据集/Open X-Embodiment - Robotic Learning Datasets and RT-X Models|Open X-Embodiment]]提供核心示范来源。与 RT-2-X 的比较同时变化了模型大小、数据量和预处理，不能将全部收益归于单一视觉模块。（第 2–4 节；附录 F）

### 18. 对当前研究方向的价值

对普通夹爪双臂研究，它是可获取权重、训练与微调代码的 **VLA 基线**；需要先统一相机和动作维度，再与 [[02_论文/03_双臂协作/RDT-1B - a Diffusion Foundation Model for Bimanual Manipulation|RDT-1B]] 等双臂策略比较。优先试验高频 action chunk、双相机／本体状态输入，以及相同示范预算下的语言 grounding；这些是研究方案，不是原版已经验证的能力。

### 19. 一句话总结

OpenVLA 用开放的 7B VLM 把单帧视觉与语言直接映射为离散化的机器人末端动作，在多机器人真机任务上展示泛化与少量示范适配，同时暴露了高频控制和双臂动作接口的不足。

## 相关论文

- [[Octo - An Open-Source Generalist Robot Policy]]
- [[DROID - A Large-Scale In-The-Wild Robot Manipulation Dataset]]
- [[Open X-Embodiment - Robotic Learning Datasets and RT-X Models]]
- [[Actions as Language - Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting]]
- [[BridgeVLA - Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models]]
- [[CoT-VLA - Visual Chain-of-Thought Reasoning for Vision-Language-Action Models]]
- [[DiffusionVLA - Scaling Robot Foundation Models via Unified Diffusion and Autoregression]]
- [[ReconVLA - Reconstructive Vision-Language-Action Model as Effective Robot Perceiver]]
- [[RoboGround - Robotic Manipulation with Grounded Vision-Language Priors]]
- [[RoboMamba - Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation]]
- [[RoboMonkey - Scaling Test-Time Sampling and Verification for Vision-Language-Action Models]]
- [[SP-VLA - A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration]]

## 来源

- 官方论文：[PMLR](https://proceedings.mlr.press/v270/kim25c.html)
- 项目主页：[项目主页](https://openvla.github.io/)
- 官方代码：[GitHub](https://github.com/openvla/openvla)
