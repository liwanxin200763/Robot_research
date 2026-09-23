# 3D-VLA: A 3D Vision-Language-Action Generative World Model

## 基本信息

- 正式标题：3D-VLA: A 3D Vision-Language-Action Generative World Model
- 作者：Haoyu Zhen、Xiaowen Qiu、Peihao Chen、Jincheng Yang、Xin Yan、Yilun Du、Yining Hong、Chuang Gan
- 年份：2024
- 发表 venue：ICML 2024，Proceedings of Machine Learning Research（PMLR）235，页码 61229–61245
- CCF 等级：A（沿用当前库内已核验的会议等级记录；本卡不把 venue 名称本身当作等级证据）
- 发表状态：正式会议论文
- DOI：未在 PMLR 正式论文页核实到 proceedings DOI；arXiv DOI：10.48550/arXiv.2403.09631
- arXiv：2403.09631



## 论文定位

这篇论文属于 VLA 方向，主要讨论现有 2D VLA 对三维空间关系和动作后的场景变化建模不足。
核心思路是3D-VLA 结合三维场景特征、目标图像/点云生成和离散动作 token，让语言模型进行具身理解与操作规划。

## 核心关键词

VLA、Robot Manipulation、3D Scene Representation、Visual Grounding、World Model、Diffusion、3D grounding、语言条件操作规划

## 快速摘要

### 研究问题

现有 2D VLA 对三维空间关系和动作后的场景变化建模不足。

### 之前方法的问题

视觉到动作的直接映射难以显式表达物体位置、空间关系与目标状态。

### 核心思路

3D-VLA 结合三维场景特征、目标图像/点云生成和离散动作 token，让语言模型进行具身理解与操作规划。
## 分类

- 主分类：VLA
- 分类：VLA、Robot Manipulation、3D Perception、Goal Generation、Diffusion
- 子分类：3D grounding、语言条件操作规划、目标状态生成
- 标签：`VLA`、`Robot Manipulation`、`3D Scene Representation`、`Visual Grounding`、`World Model`、`Diffusion`
- 特别关注：是

## 论文链接

- [PMLR 正式论文页](https://proceedings.mlr.press/v235/zhen24a.html)
- [PMLR 官方 PDF（实际阅读）](https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhen24a/zhen24a.pdf)
- [arXiv](https://arxiv.org/abs/2403.09631)
- [项目主页](https://vis-www.cs.umass.edu/3dvla/)

## 代码与资源

- [作者官方 GitHub](https://github.com/UMass-Embodied-AGI/3D-VLA)
- 代码状态：部分开放。仓库提供目标 RGB-D 图像和点云生成相关代码/权重入口；模型卡将完整 VLA/LLM 模型标为后续发布，不能据此认定端到端策略已完整开源。
- 模型权重：仓库链接至 [RGB-D diffusion 权重](https://huggingface.co/anyezhy/3dvla-diffusion) 与 [点云 diffusion 权重](https://huggingface.co/anyezhy/3dvla-diffusion-pointcloud)；本次核验的是作者提供的入口与说明，未下载或运行权重。
- 补充材料：官方论文 PDF 内含 Appendix A–D，已检查相关实现细节、提示模板、数据表和扩展任务；未发现单独挂出的补充文件。

## 机器人与具身形态

- 论文包含仿真操作基准 RLBench、CALVIN；所检查实验未提供真机平台评测证据。
- RLBench 动作规划实验使用单臂、平行夹爪任务。不能据此推断模型已验证双臂或真实机器人部署。

## 正文速读

### 研究问题

不少 VLA 方法主要从视觉观测直接预测动作，对场景三维关系、被操作物体的位置以及动作执行后的目标状态建模不足。作者研究如何让一个模型同时处理 3D 场景理解、语言指令、目标状态生成和机器人动作规划。

### 之前方法的问题

作者指出，2D 视觉特征难以充分表达空间关系；已有 3D 多模态语言模型的预训练目标和数据未必与具身任务对齐。因此本文没有直接加载预训练 3D-LLM 权重，而是采用 BLIP2-FlanT5XL 作为语言模型骨干，并训练具身相关表示和输出。

### 核心思路

把 3D 场景特征、物体与位置标记、目标图像/点云生成，以及离散机器人动作 token 放进统一的语言模型流程。模型可以先根据任务想象目标状态，再把该状态作为动作规划的条件。

### 输入

- 视觉：单视角或多视角 RGB 图像；构造 3D 场景输入时使用深度或点云信息。
- 语言：自然语言任务指令、问答或场景描述提示。
- 目标条件：目标图像/点云生成分支以当前场景和指令为条件；控制分支可使用模型生成的目标状态。
- 机器人状态：正文所述输入与图示未能确认关节位置、关节速度或 proprioception 是否作为显式模型输入，故不补猜。

### 输出

- 语言回答、任务描述或场景定位结果。
- 预测的目标 RGB-D 图像或目标点云。
- 供机器人规划使用的离散动作 token 序列。

### 动作表示

- 论文称动作是 7-DoF，并以离散 token 表示绝对位置、旋转和夹爪开合状态。
- 位置与旋转分别通过 `<aloc0-255>`、`<arot0-255>` 类 token 表示，夹爪使用 `<gripper0/1>`；另有 `<ACT_SEP>` 分隔符。
- 论文所查部分未明确旋转参数化方式、坐标系、物理单位、动作频率、chunk 长度、归一化方案或控制器执行细节；均保持未知。不能仅凭 7-DoF 推断具体编码。

### 方法整体流程

1. 从单视角或多视角图像抽取视觉特征，并构造场景级 3D 表示。
2. 通过 Q-Former 将视觉/3D 特征接入 BLIP2-FlanT5XL 语言模型；提示中使用 `<scene>`、物体及位置标记承载场景信息。
3. 目标想象分支预测目标 RGB-D 或点云：语言模型输出经 projector 映射到 diffusion 模型条件，分别生成未来 RGB-D 图像或点云。
4. 动作规划分支根据指令与场景（可包含生成的目标状态）输出离散动作 token。

### 核心模块

- 3D 场景表示：将多视角/深度信息转成可供语言模型使用的 3D 特征；对应 Figure 2 与 §4.1。
- 物体定位 token：`<obj>` 与 `<loc0-255>` 等标记表示对象及 3D bounding box；用于空间指代和定位，见 §3.2、§4.1。
- 目标状态生成：Stable Diffusion v1.4 生成目标 RGB-D；Point-E 生成目标点云。语言模型条件经 transformer projector 传给 diffusion 模型，并使用 LoRA 微调，见 §4.2。
- 动作 token：把 7-DoF 操作动作离散化为语言模型可预测的 token，见 §4.3。
- 已检查的消融只支持部分模块作用，详见“消融实验”；不能把每个设计都说成已被单独验证。

### 数据集

- 作者从 Open X-Embodiment 中选取 12 个机器人数据集，并结合 Dobb-E、RH20T 的深度信息来源；还使用 RLBench、CALVIN 仿真数据，以及 Epic-Kitchens、HOI4D 人类活动数据。具体集合和用途见 §3.1、Appendix Table 8。
- 论文称构建了约 2M 个 3D-language-action 数据对；Appendix Table 8 另按数据源列出约 305k 个 Robotics episodes、约 11k 个 HOI episodes、合计约 316k 个表内使用 episodes。两组数字的统计口径不同，不能直接相加或视为同一单位。
- 大量原始视频不含 3D 标注。作者对逐帧图像使用 ZoeDepth 估计深度，并在固定相机条件下以 RAFT 光流对齐背景深度；Grounded-SAM 产生的 2D mask 被提升至点云空间以生成 3D bounding box。细节见 §3.1–§3.3。
- 当前材料没有给出全部训练/验证/测试划分、所有源数据逐项清洗规则或可下载的完整处理后数据集链接；不作推算。

### 评测基准与任务

- Held-in 具身推理任务：Embodied QA、Task Caption、What-if QA、Dense Caption；考察场景问答、任务描述和密集描述（Table 1）。
- 3D 定位：对物体空间定位进行 IoU、Acc@25、Acc@50 评估（Table 2）。
- 目标图像生成：在 4,000 个 Open-X 测试 episodes 上比较目标图像质量（Table 3）。
- 目标点云生成：评估生成点云与目标点云差异（Table 4）。
- RLBench：语言条件操作规划任务，包括 Put Knife、Take Umbrella、Pick up Cup 及未见的 Pick up Cup（Table 5；扩展任务见 Appendix Table 9）。
- CALVIN：连续语言条件任务序列，报告完成 1–5 个任务的比例和平均完成长度（Table 6）。
- 这些实验均不能证明真机或双臂能力。

### 对比方法

- 具身推理：3D-LLM、BLIP2-OPT、BLIP2-FlanT5XL、OpenFlamingo-4B、LLaVA-7B；用于比较 3D 表示与不同视觉语言模型在具身问答、描述等任务上的表现（Table 1）。
- 3D 定位：Kosmos-2、CoVLM；比较开放词汇物体定位表现（Table 2）。
- 目标图像生成：Instruct-P2P、SuSIE、NeXT-GPT，以及在同一机器人数据上训练的 Instruct-P2P*；用于比较指令条件图像生成（Table 3）。
- 目标点云生成：Point-E 与 Point-E*；用于比较点云生成质量（Table 4）。
- RLBench：LanCon-Learn 及带历史信息版本；比较语言条件规划策略（Table 5）。
- CALVIN：MCIL；比较长时程语言条件任务完成能力（Table 6）。

### 评测指标

- 语言任务：BLEU-1–4、METEOR、ROUGE-L、EM@1，衡量文本生成与答案匹配；不同任务使用的指标见 Table 1。
- 3D 定位：IoU、Acc@25、Acc@50，衡量预测边界框的重叠和阈值下定位准确率（Table 2）。
- 图像生成：PSNR、CLIP Similarity、SSIM（越高越好）与 FID（越低越好），衡量像素/结构/语义相似度及生成分布差异（Table 3）。
- 点云生成：P-FID、Chamfer-L1（均越低越好），衡量点云分布与几何距离（Table 4）。
- 任务规划：各任务成功率/准确率，以及 CALVIN 1–5 步任务完成率和平均完成长度（Tables 5–6）。

### 主要实验结果

1. 3D 定位（Table 2）：3D-VLA 的 IoU 为 29.33、Acc@25 为 42.26、Acc@50 为 27.09；CoVLM 对应为 19.81、25.39、16.61。
2. 目标图像生成（Table 3）：3D-VLA 的 PSNR/CLIP Similarity/SSIM/FID 为 17.21/0.920/0.636/0.177。Instruct-P2P* 为 16.67/0.941/0.628/0.178；因此 3D-VLA 的 PSNR、SSIM、FID 较好，但 CLIP Similarity 较低，不是所有指标都领先。
3. 目标点云生成（Table 4）：3D-VLA 的 P-FID/Chamfer-L1 为 4.796/0.139；Point-E* 为 5.241/0.159。
4. RLBench（Table 5）：3D-VLA 在 Put Knife、Take Umbrella、Pick up Cup、未见 Pick up Cup 上分别为 68、80、40、28；对应 LanCon-Learn with history 为 32.2、50.8、44.2、未报告。表格任务指标按原文报告为成功/准确率分数，本文不转换其单位。
5. CALVIN（Table 6）：3D-VLA 连续完成 1–5 个任务的比例为 44.7/16.3/8.1/1.6/0，平均完成长度 0.71；随着序列变长，完成率明显下降。

### 消融实验

- 目标图像生成去掉预测 bounding box（Table 3）：PSNR/CLIP/SSIM/FID 从完整模型的 17.21/0.920/0.636/0.177 变为 17.02/0.919/0.632/0.173；前三项下降，但 FID 略有改善，结果并非全面一致。
- 目标点云生成去掉预测 bounding box（Table 4）：P-FID/Chamfer-L1 从 4.796/0.139 变为 4.914/0.143，完整模型在两项指标上更好。
- RLBench 去掉目标状态生成（Table 5）：Put Knife、Take Umbrella、Pick up Cup、未见 Pick up Cup 从 68/80/40/28 降至 58/68/34/24，支持目标生成对这些任务有帮助。
- 本文只记录实际列出的组件对照，不推断未报告的模块消融。

### 失败案例

- 作者在 §6 指出，diffusion 生成可能出现物体纹理/形状改变、物体消失、预测与任务不符的未来状态，或生成后场景几乎没有变化。
- 小型立方体等精细操作会失败，作者将其与 3D 特征及离散动作 token 的精度限制联系起来（§6）。
- 长序列退化由 CALVIN Table 6 的数字直接显示：5 个连续任务完成率为 0；这是评测表现，不应扩写为作者单独列出的定性失败案例。

### 作者明确指出的局限

- 离散动作 token 与现有 3D 特征精度不足以支持小物体的精细操作（§6）。
- diffusion 目标生成可能产生不真实或不符合任务的状态（§6）。
- 跨场景真实深度尺度不一致会使 Stable Diffusion 生成效果受影响，点云也可能较噪；作者提出改进深度解码器和过滤器作为未来方向（§6）。
- 数据质量和长尾差异会影响性能；作者报告 RT-1、Bridge V2 的问答/目标生成表现较好，而 BC-Z、Roboturk 较低（§5.1、§6）。

### 文献库分析

- 证据支持的能力是 3D 场景定位、目标图像/点云生成，以及 RLBench/CALVIN 仿真规划；当前论文证据不支持把它描述成已验证的真机双臂策略。
- goal generation 为动作规划提供中间目标，但生成结果可能偏离任务，说明生成目标与实际场景/指令之间仍缺少显式一致性保障。
- 7-DoF 离散动作的坐标系、旋转编码和控制频率未报告，限制复现和跨机器人比较。

### 仍未解决的问题

- 长时程执行：CALVIN 五任务完成率为 0（Table 6），仍需提升连续任务的可靠性。
- 精细操作：作者明确报告小物体操作失败（§6），需要更精确的空间和动作表示。
- 目标一致性：作者报告目标生成可能出现错误未来状态或物体消失（§6）；需验证动作规划是否会被此类预测误导。
- 真实 3D 感知：深度尺度跨场景不一致和点云噪声仍影响生成质量（§6）。

### 与当前项目的关系

本文与 VLA grounding、三维目标表示和目标状态生成高度相关。对当前双臂普通夹爪项目，可借鉴“先预测目标状态、再条件化动作”的评测思路；但论文所查实验没有给出双臂普通夹爪或真机验证，迁移性仍需独立实验确认。

### 研究启发

#### 设想一：动作规划前的目标一致性检查

- 证据来源：§6 所述 diffusion 目标 hallucination、物体消失及任务不匹配。
- 研究问题：在目标状态进入动作规划前加入视觉/几何一致性检查，是否能减少由错误目标引起的执行失败？
- 定位：待检索和实验验证的问题线索，不宣称新颖性或优先权。

#### 设想二：面向双臂普通夹爪的三维动作表示核验

- 证据来源：本文动作 token 的坐标系、旋转参数化、频率和 chunk 长度未明确，且小物体操作受离散表示精度限制（§6）。
- 研究问题：显式报告并比较连续/离散、单臂/双臂动作表示时，能否提升跨任务复现性和双臂执行精度？
- 定位：基于本文缺口的研究问题，需进一步检索相关工作。

### 重要前置工作

- 3D-LLM: Injecting the 3D World into Large Language Models（Hong et al., NeurIPS 2023）
  - 关系：方法启发/技术前序。3D-VLA §4.1 表示沿用其 3D 特征接入语言模型的思路，但因预训练数据与具身任务对齐问题，没有直接加载 3D-LLM 权重，而采用 BLIP2-FlanT5XL。
  - [NeurIPS 正式论文页](https://proceedings.neurips.cc/paper_files/paper/2023/hash/413885e70482b95dcbeeddc1daf39177-Abstract-Conference.html)
- Open X-Embodiment: Robotic Learning Datasets and RT-X Models
  - 关系：训练数据来源。3D-VLA §3.1 说明从 Open X-Embodiment 选择 12 个机器人数据集。
  - 库内卡片：[[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]]。

### 引用关系

#### 库内引用

- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]]：数据来源；证据为 3D-VLA §3.1 及 References。

#### 库内后续引用

- [[02_Papers/01_VLA/Actions_as_Language|Actions as Language]]
- [[02_Papers/01_VLA/BridgeVLA|BridgeVLA]]
- [[02_Papers/01_VLA/CoT-VLA|CoT-VLA]]
- [[02_Papers/01_VLA/ReconVLA|ReconVLA]]
- [[02_Papers/01_VLA/SpatialVLA|SpatialVLA]]
- [[02_Papers/09_Survey_Review/A_Survey_of_Embodied_Learning_for_Object-Centric_Robotic_Manipulation|A Survey of Embodied Learning for Object-Centric Robotic Manipulation]]
- [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective|A Survey on Vision-Language-Action Models: An Action Tokenization Perspective]]
- [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI|A Survey on Vision-Language-Action Models for Embodied AI]]
- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey]]

### 证据

- 正文来源：[PMLR 官方 PDF](https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhen24a/zhen24a.pdf)
- 核验日期：2026-09-23
- 实际阅读：Introduction、§3.1–§3.3、§4.1–§4.3、§5.1–§5.3、§6、§7；Appendix A–D 中实现细节、提示模板、数据表及扩展 RLBench 任务。
- 检查图表：Figure 2、Figure 3、Figures 5–6；Tables 1–6、Appendix Tables 7–9。
- 作者局限来源：§6；定量结果来源：Tables 1–6、Appendix Table 9。
- Citation Count：14（OpenAlex，2026-09-23；Work ID [W4392886475](https://openalex.org/W4392886475)）。
