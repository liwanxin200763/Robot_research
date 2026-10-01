# SpatialVLA：探索 VLA 模型的空间表征

## 基本信息

- 英文标题：SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models
- 作者：Delin Qu、Haoming Song、Qizhi Chen、Yuanqi Yao、Xinyi Ye、Jiayuan Gu、Zhigang Wang、Yan Ding、Bin Zhao、Dong Wang、Xuelong Li
- 年份：2025
- 发表 venue：RSS
- 论文类型：会议论文
- 研究方向：VLA
- 关键词：Ego3D Position Encoding；Adaptive Action Grids；3D Spatial Grounding；跨本体；动作离散化
- 论文链接：[Robotics Proceedings](https://www.roboticsproceedings.org/rss21/p011.html)
- DOI：[10.15607/RSS.2025.XXI.011](https://doi.org/10.15607/RSS.2025.XXI.011)
- arXiv：[2501.15830](https://arxiv.org/abs/2501.15830)
- 项目主页：[项目主页](https://spatialvla.github.io/)
- 代码：[GitHub](https://github.com/SpatialVLA/SpatialVLA)
- 本地 PDF：[[00_论文池/PDFs/01_VLA/SpatialVLA.pdf|查看 PDF]]
- 引用量：537
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

机器人抓取和放置取决于三维位置与运动方向，但常见 VLA 主要处理二维图像 Token，并逐维均匀量化动作。跨机器人时，相机安装和动作分布不同，单一表示难兼顾空间理解与适配。（论文第 I 节）

### 2. 论文要解决的问题

在无需各机器人统一外参标定的条件下，把相机视角内的 3D 线索引入 VLA，同时让离散动作表示保留空间结构、便于迁移到新机器人。（第 I、III 节）

### 3. 之前方法存在的问题

OpenVLA 的单维均匀动作档位没有把方向与距离作为相关的 3D 单元处理；仅用 2D 视觉特征也容易在高度、布局变化时失去可靠空间定位。Octo 等跨本体策略有适配能力，但本文重点是统一观测与动作的空间表征。（第 II–III 节）

### 4. 核心思路

Ego3D Position Encoding 用估计深度把图像 Patch 放到相机坐标系，增强视觉语义；Adaptive Action Grids 按数据分布把平移和旋转分成两个三维空间格，再加夹爪 Token，单步动作只需三个 Token。新机器人微调时重新划格并插值初始化嵌入。（图 2–3；第 III 节）

### 5. 方法与系统结构

输入图像一支进入 SigLIP 提取语义，另一支经冻结的 ZoeDepth 预测深度并按相机内参反投影，再把位置编码加到视觉 Patch；PaliGemma2 主干结合语言自回归输出平移格、旋转格、夹爪三类 Token，反量化后执行。Ego3D 使用相机自身坐标，仍需要相机内参，并非无需任何几何信息。（第 III-A 节；附录 B）

### 6. 输入信息

单张第三视角 RGB 图像与自然语言指令；训练/部署中用 ZoeDepth 从 RGB 估计深度，或新域用传感器深度。预训练实验并未把触觉、多相机或原始点云作为直接输入。（第 III–IV 节；附录 B–C）

### 7. 输出 / 动作表示

单臂 7 维末端动作由平移、旋转、夹爪构成；平移变换为方位角、俯仰角、距离后拟合动作分布，旋转也建立三维格。每步输出 3 个空间动作 Token；论文部署一次预测 4 步，即 12 个 Token，随后再感知和规划。该方法仍为离散自回归动作，未使用 Flow Matching。（第 III-A、IV 节）

### 8. 数据来源与采集方式

从 Open X-Embodiment 与 RH20T 组成约 **110 万条真实机器人 episode**、28 个数据集。附录 A 表 VI 给出例子：Bridge 约 6.0 万条、Fractal 约 8.7 万、DROID 约 9.2 万、RH20T 约 10.4 万；这些来源包含多机构机器人示范，不能归成一种统一遥操作方式。Franka 新任务数据由操作者用 SpaceMouse 以 10 Hz 收集。（第 III-B 节；附录 A、D）

### 9. 数据处理与数据增强

按数据集性能调整混合权重；DROID 在最后阶段从数据混合中移除。动作按机器人域归一化并拟合高斯分布，用等概率间隔划空间格；新域重新拟合后用相邻旧格嵌入三线性插值。附录 D 指出随机裁切和颜色扰动对零样本测试重要。深度预测器固定，避免在每个数据源要求实际深度标签。（第 III-B 节；附录 A、D）

### 10. 训练方式

从 PaliGemma2 初始化，优化视觉编码器、语言主干、Ego3D MLP 与空间动作嵌入，文本 Token 嵌入保持冻结，以 next-token cross-entropy 训练。预训练 64 张 A100、约 10 天、批量 2048、学习率 2×10⁻⁵；前段完整混合数据 160k 步，去 DROID 后再 40k 步。LIBERO 新域采用 LoRA rank 32 微调 200 epoch，并重划动作格。（第 III–IV 节；附录 D）

### 11. Benchmark 与实验设置

零样本在 SimplerEnv 的 Google Robot、WidowX 仿真中测试视觉匹配与变体聚合；真实 WidowX 用 7 组任务测背景、姿态、运动干扰与语言指代，每组 11 次。新域适配包括 LIBERO 四套任务、13 项 Franka 任务；还设空间指令与高度扰动测试。基线包括 RT-1-X、RT-2-X、Octo、OpenVLA、TraceVLA、RoboVLM 与 Diffusion Policy，按各实验提供的成功率评价。（第 IV 节；表 I–III、图 4–7）

### 12. 真机实验

WidowX 250 单臂与固定安装的 RealSense D435 进行 7×11 次零样本评测；Franka Panda 单臂用三脚架 D435，数据由 SpaceMouse 遥操作采集，13 项任务每项 11 次。部署在 RTX 4090 上约 20 Hz、8.5 GB 显存；论文未报告双臂实物操作。（第 IV 节；附录 D–E）

### 13. 主要实验结果

SimplerEnv Google Robot 零样本视觉匹配平均 **71.9%**、变体聚合 **68.8%**，RT-2-X 分别 **60.7%**／**64.3%**（表 I）。WidowX 仿真四任务平均零样本 **34.4%**，Bridge 微调 **42.7%**（表 II）；这两个数字是仿真表格，不能写成 77 次真机的总成功率。LIBERO 平均 **78.1±0.7%**，OpenVLA **76.5±0.6%**；Spatial 套件 **88.2±0.5%**（表 III）。Franka 空间指令任务 #1 达 **73%**（图 7）。

### 14. 消融实验

在相同预训练子集上，移除 Ego3D 后 Google「Pick Coke Can」变体聚合由 **81.6%** 降到 **68.9%**，WidowX「Put Eggplant」成功率由 **87.5%** 降到 **37.5%**；改为逐维线性 256 档后前一任务降到 **40.7%**（表 IV）。LIBERO-Spatial 上 LoRA **83.6±0.7%**，再加新域空间嵌入适配达到 **88.2±0.5%**（表 V）。附录表 IX 对细粒度任务报告 ZoeDepth 版本平均 **72.7%**，去深度 **45.4%**。

### 15. Failure Case

作者指出 LIBERO-Long 仍较弱，虽为该表最高但仅 **55.5±1.0%**，缺少长时序历史建模。附录 A 还报告 FMB 数据权重过高造成机器人向右偏移；低分辨率动作格容易输出偏小动作、移动缓慢。真实 WidowX 的干扰物和动态移动测试仍有失败，不能把个别演示视为全任务稳健。（第 IV–V 节；附录 A、C）

### 16. 主要局限

作者明确指出高斯拟合在单轴运动等极端分布下可能让网格挤到局部，噪声也会扭曲格点；每步 3 个自回归 Token 有推理代价，高自由度双臂／灵巧手直接扩维会带来更多嵌入参数。单帧观测和有限历史限制长任务，OXE 数据质量差异也会影响训练。（第 V 节；附录 C）

### 17. 与已有工作的关系

与 OpenVLA 的二维输入和逐维量化相比，SpatialVLA 引入相机坐标下的深度位置与联合空间动作格；不同于 3D-VLA 的 3D 世界预测重点，这里把空间信息直接用于低层动作 Token。其零样本优势与数据规模、主干和表示一起变化，表 IV 消融才提供表示模块的局部证据。（第 II–IV 节）

### 18. 对当前研究方向的价值

对普通夹爪双臂协作，Ego3D 可启发相机视角下的目标相对位置编码，Adaptive Action Grids 可启发跨机械臂动作空间对齐；但目前 7D 单臂动作格不能直接当作双臂验证成果。应检验双臂联动格规模、遮挡下深度误差和接触任务精度，这是基于论文局限提出的研究问题。

### 19. 一句话总结

SpatialVLA 同时为空间视觉输入和离散动作输出加入三维结构，使 VLA 能更有效地学习机器人操作的相对位置与运动表示。

## 相关论文

- [[3D-VLA：基于三维视觉—语言—动作的生成式世界模型]]
- [[Octo：开源通用机器人策略]]
- [[OpenVLA：开源视觉—语言—动作模型]]
- [[TraceVLA：以视觉轨迹提示增强通用机器人策略的时空感知]]
- [[RDT-1B：面向双臂操作的扩散基础模型]]
- [[BAKU：面向多任务策略学习的高效 Transformer]]
- [[DROID：大规模自然场景机器人操作数据集]]
- [[Open X-Embodiment：机器人学习数据集与 RT-X 模型]]

## 来源

- 官方论文：[Robotics Proceedings](https://www.roboticsproceedings.org/rss21/p011.html)
- 项目主页：[项目主页](https://spatialvla.github.io/)
- 官方代码：[GitHub](https://github.com/SpatialVLA/SpatialVLA)
