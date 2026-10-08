---
paper_id: P021
title: "CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models"
---

# P021 · CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models

## 基本信息

- 作者：Zhao, Qingqing; Lu, Yao; Kim, Moo Jin; Fu, Zipeng; Zhang, Zhuoyang; Wu, Yecheng; Li, Zhaoshuo; Ma, Qianli; Han, Song; Finn, Chelsea; Handa, Ankur; Lin, Tsung-Yi; Wetzstein, Gordon; Liu, Ming-Yu; Xiang, Donglai
- 年份：2025
- 发表 venue：CVPR
- 论文类型：会议论文
- 研究方向：VLA
- 关键词：Visual Chain-of-Thought；Subgoal Image；Action Chunking；VILA-U；视觉推理
- 论文链接：[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html)
- DOI：—
- arXiv：[2503.22020](https://arxiv.org/abs/2503.22020)
- 项目主页：[项目主页](https://cot-vla.github.io/)
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/01_VLA/CoT-VLA.pdf|查看 PDF]]
- 引用量：610
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

许多 VLA 从当前图像和指令直接预测动作，缺少可观察的中间目标。对于目标状态与当前状态相差较大的任务，这限制了时序规划，也难直接利用没有动作标签的视频。（论文第 1 节）

### 2. 论文要解决的问题

让 VLA 在动作前显式预测未来视觉子目标，并检验这种视觉推理是否改善仿真与真机操作，以及无动作视频能否参与训练。（第 1、3 节）

### 3. 之前方法存在的问题

OpenVLA 等直接映射策略没有显式中间状态；文字、关键点或边界框形式的推理需额外标注或预处理。单独的图像生成加目标条件策略虽可用未来图像，但未融入同一个可同时预测视觉与动作的 VLA。（第 1–2 节）

### 4. 核心思路

给定当前图像和语言，先自回归生成若干步后的子目标图像，再以当前图像、指令和该目标图像为条件，并行预测短动作序列；执行后重新观察并循环。（图 2，算法 1）

### 5. 方法与系统结构

以 7B VILA-U 为基座：统一视觉编码器把图像离散化，LLM 与 depth transformer 在因果注意力下生成子目标视觉 Token；动作阶段改用全注意力，使一个 Action Chunk 的维度与时间步互相通信。图 2–3 分别说明视觉子目标到动作，以及两种注意力的切换。（第 3 节）

### 6. 输入信息

语言任务指令、当前 256×256 RGB 图像与此前执行后获取的新图像；训练时还使用未来图像作为目标监督。主模型预训练筛选第三人称相机和单臂末端动作数据，没有报告将点云、触觉或深度纳入该实验。（第 3.1–3.3 节）

### 7. 输出 / 动作表示

先输出未来子目标图像的离散视觉 Token，随后预测长度 10 的 Action Chunk。每步 7 维动作逐维按第 1–99 百分位区间量化为 256 档，与 OpenVLA 式动作 Token 接口相近；动作预测阶段采用全注意力，不是 Diffusion 或 Flow 动作头。（第 3.3 节，图 3）

### 8. 数据来源与采集方式

机器人示范来自筛选后的 Open X-Embodiment；无动作视频来自 Something-Something V2 和 EPIC-KITCHENS-100。官方补充材料表 4 列出 8 个机器人子数据集的抽样权重，Bridge 占 24.14%，两个视频数据集各 3.45%。真机 Bridge-V2 域有约 45,000 条语言标注轨迹；Franka 下游各任务有 10–150 条示范。（第 3.3、4.1 节；补充材料表 4）

### 9. 数据处理与数据增强

沿用 OpenVLA 的第三人称、单臂末端数据预处理；为不同数据集单独设置未来图像时间跨度，如 Bridge 为 5–10 步、TOTO 为 20–24 步。LIBERO 轨迹去暂停片段、统一到 256×256，并旋转图像 180°。正文未声称使用额外合成双臂数据。（第 3.3、4.1 节；补充材料表 4）

### 10. 训练方式

在 VILA-U 上联合优化图像 Token 与动作 Token 的交叉熵，训练 LLM 主干、投影层及 depth transformer，固定视觉塔。补充材料报告预训练学习率 1×10⁻⁴、批量 2048、10 epoch、约 11,000 A100 GPU 小时；LIBERO 与 Franka 适配学习率 1×10⁻⁵、150 epoch。无动作视频只监督视觉目标，不参与动作损失。（第 3.3 节；补充材料表 5）

### 11. Benchmark 与实验设置

LIBERO 的 Spatial、Object、Goal、Long 四套仿真任务各有 10 项，每项 50 条人类遥操作示范；每套测试 500 个 episode、3 个随机种子。真机 Bridge-V2 测视觉干扰、位置、语义和语言指代四类任务，各 10 次并允许论文定义的部分得分；Franka-Tabletop 测 6 项任务，含单指令与多指令。基线为 Diffusion Policy、Octo、OpenVLA，以及 Bridge 测试中的 SUSIE。（第 4.1–4.2 节，表 1–2）

### 12. 真机实验

Bridge-V2 使用 6 自由度 WidowX 单臂，Franka-Tabletop 使用 7 自由度 Franka Panda 单臂；后者设备未参与预训练。论文未报告双臂真机实验，也未给这两个设置统一控制频率、夹爪硬件细节或相机数量，不能据此推断。（第 4.1 节）

### 13. 主要实验结果

LIBERO 四套平均成功率为 **81.13±0.6%**，OpenVLA 微调为 **76.5±0.6%**，Octo 为 **75.1±0.6%**；LIBERO-Long 上 CoT-VLA **69.0±0.8%**、OpenVLA **53.7±1.3%**（表 1）。Franka 六任务平均 **78.8%**，OpenVLA **67.3%**、Diffusion Policy **51.2%**（图 4）。Bridge 四类中 CoT-VLA 为 65%／60%／50%／70%，不是每类都高于 OpenVLA（表 2）。

### 14. 消融实验

LIBERO-Spatial 从普通 VLA 的 67.5%，依次增加 Action Chunk 为 73.3%、混合注意力为 81.8%、视觉 CoT 为 87.5%；LIBERO-Goal 对应 54.9%、74.9%、79.7%、87.6%（图 6a）。Franka 去掉预训练平均从 78.8% 降为 53.7%（图 6b）。两项新组合任务改用真实目标图像时，成功率由 20%／0% 增至 60%／40%，各仅 5 次测试，属于小样本诊断（表 3）。

### 15. Failure Case

Bridge 视觉与语言类任务比 OpenVLA 更易抓取失败，作者将其与 Action Chunk 执行期间缺少细粒度反馈关联。超出训练分布的新组合任务中，模型生成的子目标图像不可靠，对应表 3 的低成功率；动作块交界也可能不连续。（第 4.2、4.4、5 节）

### 16. 主要局限

作者指出每轮先生成 256 个视觉 Token，长度 10 动作块条件下平均比直接动作生成慢约 7 倍；自回归图像质量逊于强 Diffusion 图像生成器；动作块降低高频反馈，视觉推理对全新任务的泛化也未解决。（第 5 节）

### 17. 与已有工作的关系

CoT-VLA 沿用 OpenVLA 的动作量化与数据筛选思路，但换成既能生成图像又能理解语言的 VILA-U，并在动作前显式加入像素空间子目标。与两阶段 SUSIE 不同，它在统一模型中联合生成视觉和动作；表 2 也显示其并非所有 Bridge 测试都领先。（第 2–4 节）

### 18. 对当前研究方向的价值

可将「可视化未来目标」作为双臂协同中间表征的研究假设，但论文只验证单臂真机，不能直接声称双臂有效。特别应测试目标图像质量、动作块边界和失败后重规划；这些是从作者局限推导的实验方向。

### 19. 一句话总结

CoT-VLA 在动作前生成未来子目标图像，并以它引导短动作序列，在 LIBERO 和两类单臂真机任务中验证视觉中间推理的价值与代价。

## 相关论文

- [[3D-VLA - A 3D Vision-Language-Action Generative World Model]]
- [[Octo - An Open-Source Generalist Robot Policy]]
- [[OpenVLA - An Open-Source Vision-Language-Action Model]]
- [[Dreamitate - Real-World Visuomotor Policy Learning via Video Generation]]
- [[Open X-Embodiment - Robotic Learning Datasets and RT-X Models]]
- [[Actions as Language - Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting]]
- [[RoboMonkey - Scaling Test-Time Sampling and Verification for Vision-Language-Action Models]]
- [[A Survey on Vision-Language-Action Models - An Action Tokenization Perspective]]
- [[A Survey on Vision-Language-Action Models for Embodied AI]]
- [[Learning by Watching - A Review of Video-Based Learning Approaches for Robot Manipulation]]
- [[Towards a Unified Understanding of Robot Manipulation - A Comprehensive Survey]]

## 来源

- 官方论文：[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html)
- 项目主页：[项目主页](https://cot-vla.github.io/)
