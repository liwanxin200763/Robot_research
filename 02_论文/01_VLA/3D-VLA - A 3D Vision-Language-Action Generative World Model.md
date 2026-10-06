# 3D-VLA：基于三维视觉—语言—动作的生成式世界模型

## 基本信息

- 英文标题：3D-VLA: A 3D Vision-Language-Action Generative World Model
- 作者：Haoyu Zhen、Xiaowen Qiu、Peihao Chen、Jincheng Yang、Xin Yan、Yilun Du、Yining Hong、Chuang Gan
- 年份：2024
- 发表 venue：ICML 2024，PMLR 235，61229–61245
- 论文类型：会议论文；三维具身生成世界模型
- 研究方向：VLA；机器人操作；三维感知；目标状态生成
- 关键词：3D Grounding；World Model；Goal Generation；RGB-D Diffusion；Point Cloud；Action Tokenization
- 论文链接：[PMLR 正式论文](https://proceedings.mlr.press/v235/zhen24a.html)
- DOI：[arXiv DOI：10.48550/arXiv.2403.09631](https://doi.org/10.48550/arXiv.2403.09631)（PMLR 页面未列单独 proceedings DOI）
- arXiv：[2403.09631](https://arxiv.org/abs/2403.09631)
- 项目主页：[作者项目页](https://vis-www.cs.umass.edu/3dvla/)
- 代码：[官方 GitHub](https://github.com/UMass-Embodied-AGI/3D-VLA)（目标图像／点云生成代码与权重入口已开放；完整 VLA 策略未见全量发布）
- 本地 PDF：[[00_论文池/PDFs/01_VLA/3D-VLA.pdf|查看 PDF]]
- 引用量：456
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

2D VLA 往往由当前图像直接生成动作，对物体的三维位置、场景关系以及执行后的目标状态表达不足。作者希望把三维场景理解与“未来会变成什么样”的生成式世界模型用于动作规划。（论文第 1–2 节）

### 2. 论文要解决的问题

构建同一具身模型，使其能够在语言和三维场景条件下完成推理、物体定位、目标 RGB-D／点云生成与机器人动作预测，并检验生成目标是否帮助操作。（第 1、4–5 节，图 1–2）

### 3. 之前方法存在的问题

2D 图像特征不直接表明物体深度和空间关系；仅把视觉输入映射到动作忽略未来场景动态。已有 3D-LLM 的训练数据主要是物体和室内场景，与具身动作不完全对齐；通用图像扩散模型可能擅自改变视角、纹理或物体形状，不适合作为直接的机器人目标预测器。（第 1–2、4.2–4.3 节）

### 4. 核心思路

从已有机器人和人手—物体数据构建三维具身指令数据；给语言模型加入场景、物体、位置、图像／点云目标和动作 Token；训练面向机器人状态变化的 RGB-D 与点云扩散生成器，并把生成器与语言模型对齐。生成的目标状态可以再作为动作预测条件。（第 3–4 节，图 2）

### 5. 方法与系统结构

沿用 3D-LLM 的多视角特征汇聚和 Q-Former 接口，但**没有直接加载 3D-LLM 预训练权重**，改以 BLIP2-FlanT5XL 初始化。场景特征经 Q-Former 接入语言模型；`<obj>`、`<loc0-255>` 和 `<scene>` 标记对象、三维位置与场景。语言模型在 `<image>`／`<pcd>` 标记之间给出目标生成条件，经 Transformer projector 对齐到分别以 Stable Diffusion v1.4、Point-E 为起点的 RGB-D／点云扩散解码器；行动分支生成离散动作 Token。（第 4.1–4.3 节，图 2）

### 6. 输入信息

依据任务可输入单视角或多视角 RGB、估计或原有的深度／点云、自然语言任务指令以及可选的目标状态。三维场景构建使用相机内参与位姿；论文没有把关节速度或受力描述为统一、必需的模型输入，不能据其“7-DoF 动作”推断这些观测存在。（第 3.1–3.3、4.1 节）

### 7. 输出 / 动作表示

模型可输出具身问答、任务描述、物体的三维边界框、目标 RGB-D／点云，以及机器人动作。动作由 `<aloc0-255>`、`<arot0-255>`、`<gripper0/1>` 和 `<ACT_SEP>` 等离散 Token 表示 7-DoF 绝对位置、旋转与夹爪状态。论文未明确报告统一的控制频率、动作块长度和完整坐标系约定，不能补猜。（第 4.2.2 节，图 2）

### 8. 数据来源与采集方式

从 Open X-Embodiment 选取 12 个机器人数据集，另用有深度信息的 Dobb-E、RH20T，RLBench／CALVIN 仿真与 Epic-Kitchens／HOI4D 人手—物体数据。作者报告约 **200 万个三维—语言—动作训练数据对**；附录表 8 按原始 episode 另统计机器人约 **305k**、HOI 约 **11k**、合计约 **316k**。数据对数与 episode 数单位不同，不能相加。论文不是另采集并评测真实机器人示范。（第 3.1 节；附录 B，表 8）

### 9. 数据处理与数据增强

对多数缺少深度的视频用 ZoeDepth 估深、RAFT 算光流；固定相机片段借未动背景对齐跨帧深度尺度，再按相机参数提升为点云。spaCy 从指令提取名词短语，Grounded-SAM 给 2D mask，再投影得到 3D bounding box；用高光流且高置信的区域定位被操作对象。模板组织验证、描述、定位、生成和动作任务，GPT-3.5 基于对象位置与少量人工示例改写提示以增加表达多样性。对复杂机器人场景做筛选，HOI 数据增加目标生成时的场景多样性。（第 3.2–3.3 节；附录 B，表 7–8）

### 10. 训练方式

先训练三维场景／语言模型和交互 Token，再分别在具身数据上训练 RGB-D→RGB-D 与点云→点云扩散模型，最后通过 projector 把语言模型输出对齐到生成器。动作预测可用真实或生成的目标状态作提示；LLM 用交叉熵，生成器用去噪损失，扩散模型以 LoRA 适配。正式 PMLR PDF 的附录 A 给出 6×32 V100 的前期训练、6×64 V100 的对齐训练、学习率前 1k 步预热至 10⁻⁵ 后余弦下降，以及 AdamW；这些是不同阶段的配置，不应与旧 arXiv v1 附录混写。（第 4.2–4.3 节；附录 A）

### 11. Benchmark 与实验设置

评测分三组：①在 RoboVQA、Open X 和 RT-1 来源的 held-in 数据上做 Embodied QA、Task Caption、What-if QA、Dense Caption 与三维定位；问答对比 3D-LLM、BLIP2、OpenFlamingo、LLaVA，定位对比 Kosmos-2、CoVLM。②从 Open X 测试集抽 **4,000 episodes** 测目标 RGB／点云生成，对比 Instruct-P2P、SuSIE、NeXT-GPT、Point-E，指标包括 PSNR、CLIP Similarity、SSIM、FID、P-FID、Chamfer-L1。③RLBench 比较 LanCon-Learn，CALVIN 五步任务序列比较 MCIL；这些基线属于不同实验，不是同一张总榜。（第 5.1–5.3 节，表 1–6）

### 12. 真机实验

论文测试的动作规划任务是 **RLBench 与 CALVIN 仿真**。数据来源包含真实机器人记录，图像生成也展示互联网／日常场景样例，但这不构成真机闭环控制评测；本文没有可报告的实体机械臂试次、控制频率或真机成功率。Impact Statement 谈到未来在人工监督下部署，不是已经完成的实验。（第 5–7 节）

### 13. 主要实验结果

表 1 的 What-if QA，3D-VLA 的 BLEU-1 为 **53.09**、BLEU-4 为 **29.38**，相同 held-in 对照 BLIP2-FlanT5XL 为 **28.23／0.06**；表 2 定位 IoU／Acc@25／Acc@50 为 **29.33／42.26／27.09**，CoVLM 为 **19.81／25.39／16.61**。表 3 的目标图像 PSNR／CLIP／SSIM／FID 为 **17.21／0.920／0.636／0.177**，同数据训练的 Instruct-P2P* 为 **16.67／0.941／0.628／0.178**；CLIP 相似度并未领先。表 4 的点云 P-FID／Chamfer-L1 为 **4.796／0.139**，Point-E* 为 **5.241／0.159**。正式版表 5 的 RLBench 四项 Put Knife／Take Umbrella／Pick up Cup／未见 Pick up Cup 为 **68／80／40／28**；表 6 的 CALVIN 连续完成 1–5 项比例为 **44.7／16.3／8.1／1.6／0**，平均完成长度 **0.71**。这些实验设置和指标不可合成一个“总体成功率”。（第 5 节，表 1–6）

### 14. 消融实验

正式版表 5 去掉生成目标后，RLBench 四任务从 **68／80／40／28** 降到 **58／68／34／24**，但“放刀”任务仍有物体碰撞失败，不能把全部误差归因于目标生成。表 3 去掉预测 BBox 后，PSNR／CLIP／SSIM 从 **17.21／0.920／0.636** 变为 **17.02／0.919／0.632**，但 FID **0.177→0.173** 反而略好；表 4 点云 P-FID／Chamfer-L1 从 **4.796／0.139** 变为 **4.914／0.143**。消融只支持这些具体对照，不代表每个模块均已单独验证。（第 5.2–5.3 节，表 3–5）

### 15. Failure Case

作者在第 6 节报告小立方体精细抓取失败，受三维特征与离散动作精度限制；Diffusion 目标有时改变物体纹理／形状、令物体消失、生成错误任务的未来状态或几乎不发生变化。表 6 还显示 CALVIN 五任务连续完成率为 **0**；这是量化的长序列弱项，不应混同作者单列的定性失败案例。（第 6 节，表 6）

### 16. 主要局限

**作者明确指出：**小物体精细控制不足；目标图像可能 hallucinate；真实环境跨场景深度尺度不统一、点云噪声影响生成；BC-Z、Roboturk 等数据质量差异会降低任务表现。作者提出改进深度解码与点云过滤。（第 6 节）**本库分析：**缺少真机与双臂闭环证据，CALVIN 长程成绩仍有限；生成目标进入动作规划前的可信度检查尚未被单独验证。后两点是由实验范围与表 6 推出的研究判断，非作者声称已解决。（第 5–6 节）

### 17. 与已有工作的关系

方法借鉴 [3D-LLM](https://proceedings.neurips.cc/paper_files/paper/2023/hash/413885e70482b95dcbeeddc1daf39177-Abstract-Conference.html) 的三维场景特征接入思路，但重训具身对齐部分；从 [[02_论文/10_基准测试与数据集/Open X-Embodiment - Robotic Learning Datasets and RT-X Models|Open X-Embodiment]] 取得训练数据。相较 [[02_论文/01_VLA/OpenVLA - An Open-Source Vision-Language-Action Model|OpenVLA]] 一类直接动作预测，本文显式生成目标状态；与 [[02_论文/01_VLA/DIAL - Decoupling Intent and Action via Latent World Modeling for End-to-End VLA|DIAL]] 的潜在意图表征可比较“可视化未来目标”和“潜在空间未来意图”对执行的影响，但跨论文效果不能直接横比。（第 2–5 节）

### 18. 对当前研究方向的价值

对 VLA grounding 和双臂普通夹爪研究，三维目标状态可作为动作前的可检查中间表示。**潜在研究启发：**检测生成目标与当前物体、语言指令、可达几何是否一致，再决定是否执行或重新生成；同时比较连续与离散动作表示对精细操作的影响。本文没有验证这类一致性检查或双臂恢复流程，必须另做实验。（第 5–6 节）

### 19. 一句话总结

3D-VLA 用三维具身数据、交互 Token 和目标状态扩散生成，把空间理解、未来想象与动作预测接入同一个模型，但精细操作、长时序和真机部署仍有明显边界。

## 我的阅读笔记
