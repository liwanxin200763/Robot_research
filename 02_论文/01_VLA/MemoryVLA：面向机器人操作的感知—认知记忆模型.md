# MemoryVLA：面向机器人操作的感知—认知记忆模型

## 基本信息

- 英文标题：MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation
- 作者：Hao Shi、Bin Xie、Yingfei Liu、Lin Sun、Fengrong Liu、Tiancai Wang、Erjin Zhou、Haoqiang Fan、Xiangyu Zhang、Gao Huang
- 年份：2026
- 发表 venue：ICLR 2026
- 论文类型：会议论文；VLA 模型
- 研究方向：VLA；机器人操作；长时序决策；时序记忆
- 关键词：Cognition-Memory-Action；Working Memory；Perceptual-Cognitive Memory Bank；Memory Retrieval；Diffusion Action Expert；Long-Horizon Manipulation
- 论文链接：[arXiv 论文](https://arxiv.org/abs/2508.19236)
- DOI：[10.48550/arXiv.2508.19236](https://doi.org/10.48550/arXiv.2508.19236)
- arXiv：[2508.19236](https://arxiv.org/abs/2508.19236)
- 项目主页：[MemoryVLA 项目页](https://shihao1895.github.io/MemoryVLA/)
- 代码：[官方 GitHub](https://github.com/shihao1895/MemoryVLA)（代码、模型与训练／评测说明已公开）
- 本地 PDF：[[00_论文池/PDFs/01_VLA/MemoryVLA.pdf|查看 PDF]]
- 引用量：
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

许多 VLA 只看当前画面。长时序操作中，当前图像可能看不出按钮是否按过、前一个物体是否已移动，决策因而依赖历史。直接拼接很多帧既增加自注意力开销，也偏离单帧机器人预训练分布。（论文第 1 节，图 1）

### 2. 论文要解决的问题

让视觉—语言—动作模型在不反复输入整段视频的前提下保留低层视觉细节和高层任务语义，从而应对非马尔可夫、长时序操作。（第 1、3 节）

### 3. 之前方法存在的问题

当前帧 VLA 容易把已完成子任务当成未完成；仅用有限帧窗口难覆盖长程依赖。纯粹扩大图像输入又有计算成本和分布偏移。单一路径的视觉记忆或语义记忆各会丢失另一种信息。（第 1–2、4.6 节）

### 4. 核心思路

建立 **Cognition-Memory-Action** 流程：当前图像和指令被编码成感知、认知两类短期工作记忆；这两类 Token 去长期的 Perceptual-Cognitive Memory Bank 检索、门控融合与更新；融合后的上下文再条件化 Diffusion Action Expert 生成动作。（第 3 节，图 2–3）

### 5. 方法与系统结构

以在 Open X-Embodiment 上继续预训练的 Prismatic 7B VLM 为骨干。DINOv2 和 SigLIP 的并行视觉特征经 SE bottleneck 压缩为 **256 个 Perceptual Tokens**；图像特征与语言指令进入 LLaMA-7B，EOS 输出形成一个高层 Cognitive Token。两者构成当前时刻的 Working Memory。检索时分别作为 query，带时间位置编码地读取银行中对应的感知细节与认知语义；门控在当前信息和历史信息之间分配权重。融合表示同时用于动作预测和写回长期银行，容量满时在各流内对时间相邻且余弦相似度最高的条目取平均合并，减少冗余。（第 3.1–3.3 节，图 2–3）

### 6. 输入信息

单张第三人称 RGB 图像、自然语言任务指令，以及模型先前时刻积累的内部记忆。标准模型没有把腕部相机或 Proprioception 加入主输入；部分基线使用额外输入，表 1 和表 3 的星号应单独看待。（第 3.1–3.2、4.1 节，表 1、3）

### 7. 输出 / 动作表示

记忆增强的认知 Token 提供语义条件，感知 Token 补充细节；约 **300M 参数**的 DiT 动作专家用 **10 步 DDIM** 去噪预测长度 **16** 的 Action Chunk。每步为连续 **7-DoF** 相对动作：三维平移、欧拉角旋转和二值夹爪状态；不是预测离散语言动作 Token。（第 3.4、4.1 节）

### 8. 数据来源与采集方式

骨干先利用 Open X-Embodiment。下游分别使用 BridgeData V2、RT-1 数据、LIBERO 示范及 Mikasa-Robo 官方示范；真机在 Franka、WidowX 上用操纵杆遥操作采集。真机通用任务每项 **50–150 条**，长时序任务每项 **200–300 条**；Mikasa 五项任务各 **250 条**。不能把“150+ 任务”误写成训练轨迹数。（第 4 节；附录 C）

### 9. 数据处理与数据增强

真机 D435 正前方相机采集 640×480、30 fps RGB，缩放到 224×224；只有末端平移超过 0.01 m、转动超过 0.4 rad 或距离上次保留帧已达 120 帧时才保留新帧，之后转 RLDS。训练时对 RGB 做随机裁剪、亮度、对比度、饱和度和色调扰动，测试时关闭；LIBERO 先剔除失败轨迹。为保持记忆学习中的时序顺序，采样器按同一 episode 提取有序帧。（附录 C.2–C.4）

### 10. 训练方式

论文通用设置为 **8×A100、全局 batch 256、学习率 2×10⁻⁵**，动作专家用预测动作与真值的 MSE 去噪损失。Bridge 训练 50k 步、Fractal 80k；LIBERO 的 Spatial／Object／Goal 各 20k，Long-10 与 Long-90 联合 40k；Mikasa 五任务联合 20k；真机依任务约 5k–20k。普通任务记忆长度 16，真机长时序任务设 256。不同基准各自训练，不能将其当成一个单一联合模型的成绩。（第 3.4、4 节；附录 C.3）

### 11. Benchmark 与实验设置

仿真涵盖 **SimplerEnv-Bridge**（WidowX，四任务、每任务 24 次）、**SimplerEnv-Fractal**（Google 机器人，Visual Matching／Visual Aggregation）、**LIBERO 五套**（Franka；Spatial、Object、Goal、Long-10、Long-90）和 **Mikasa-Robo 五任务**（Franka；每任务 100 次），加上 Franka 与 WidowX 的两套真机评测，共计 **150+ 任务、500+ 变化**。基线依场景不同：Bridge／Fractal 有 CogACT、π0、OpenVLA、Octo、TraceVLA 等；LIBERO 有 CogACT、π0、Diffusion Policy 等；Mikasa 对比 OpenVLA-OFT、π0、SpatialVLA、CronusVLA；真机对比 OpenVLA、π0、CogACT。不同表中的 π0 输入、模型复现与附加状态不尽相同，不能跨表直接横比。（第 4.1–4.5 节，表 1–5）

### 12. 真机实验

真机有 **6 项通用任务＋6 项长时序任务**，使用 Franka 与 WidowX、固定正前方 Intel RealSense D435 RGB 相机，经 ROS 集成。通用任务每项通常 **15 次**，Pick Diverse Fruits 为五变体各 5 次、共 25 次；长时序任务每项 **10–15 次**，按子目标进度给 step-wise score。比较方法都只用第三人称 RGB 和语言。论文未给单一通用控制频率，不能据 30 fps 相机频率推断动作控制频率。（第 4.5 节，表 5；附录 C.2）

### 13. 主要实验结果

**表 1–4：**Bridge 平均成功率 **71.9%**（CogACT-Large 57.3%，π0-Beta 68.4%；相对 CogACT +14.6 个百分点）；Fractal 整体 **72.7%**（CogACT 68.1%，分为 VM 77.7%、VA 67.7%）；LIBERO 五套平均 **96.5%**（CogACT 93.2%，其中 Long-10 93.4%、Long-90 95.6%）；Mikasa 平均 **41.2%**（π0 29.4%，但 Intercept Medium 上本方法 24%、π0 42%，不能说逐任务都领先）。**表 5：**真机通用任务 **85%**（CogACT 76%），长时序 **83%**（CogACT 57%，+26 个百分点）；两套等权平均 **84%**。真机长时序使用进度评分，不应与仿真二元成功率混称。（第 4.2–4.5 节）

### 14. 消融实验

Bridge 表 6：只保留 Cognitive Memory **63.5%**，只保留 Perceptual Memory **64.6%**，两者联合 **71.9%**；记忆长度 4／16／64 分别 **67.7／71.9／67.7%**。表 7：不加时间位置编码 **69.8%**，门控融合 **71.9%** 对直接相加 **67.7%**，相似条目合并 **71.9%** 对 FIFO **66.7%**。这些实验支持双流记忆、时序编码及控制冗余的各自贡献。（第 4.6 节，表 6–7）

### 15. Failure Case

论文图 1 的 **Push Buttons**：按下前后视觉几乎一样，当前帧策略可能重复按；这是本文要处理的时序混淆案例。即便引入记忆，Mikasa 的 **Intercept Medium** 只有 **24%**，低于 π0 的 42%；附录 OOD 分析中未见过的相机视角会使成功率明显下降，例如文中报告一项相机变化条件为 **42.0%**。这些是报告中的任务／扰动弱项，不等于作者给出了统一的故障分类或恢复策略。（图 1；表 4；附录 B）

### 16. 主要局限

**作者提出的未来工作：**加入 memory reflection，使长期记忆与 LLM 输入空间对齐，以及通过更持久的巩固机制发展 lifelong memory，说明当前实现尚未覆盖这些能力。（第 5 节）**本库分析：**结果集中在单臂 7-DoF 动作和给定基准；Mikasa 部分任务及新相机视角仍脆弱。真机长程比较按阶段进度计分，不能据此断言它能自动发现并修复任意执行故障。（第 3.4、4.4–4.5 节；附录 B）

### 17. 与已有工作的关系

模型沿用 [[02_论文/01_VLA/OpenVLA：开源视觉—语言—动作模型|OpenVLA]] 所属的 Prismatic／Open X-Embodiment 视觉—语言骨干路线，但显式加入随执行更新的双流记忆和扩散动作专家；与 [[02_论文/01_VLA/SayCan：以机器人能力约束语言指令的落地执行|SayCan]] 的技能级语言规划不同，它直接生成连续动作。官方仓库另列 MemoryVLA+ 和 MemoryVLA++，它们不是本张主卡的同一实验版本，不能混入此卡分数。（第 2–4 节；[官方仓库](https://github.com/shihao1895/MemoryVLA)）

### 18. 对当前研究方向的价值

对长时序操作，双流记忆可分别保存“之前看到了什么”和“哪个子目标已完成”，为研究动作历史、阶段判断和跨时刻决策提供可复现实验基线。**潜在研究启发：**若接入执行错误检测，可检索错误发生前的计划、动作和视觉状态，再决定是否重试或改道；MemoryVLA 本文验证的是时序记忆带来的任务收益，**没有验证通用 Failure Recovery**。（第 1、4–5 节）

### 19. 一句话总结

MemoryVLA 把当前感知与认知 Token 同历史双流记忆结合，再驱动扩散动作专家，从而改善需要记住过去状态的机器人操作。

## 我的阅读笔记
