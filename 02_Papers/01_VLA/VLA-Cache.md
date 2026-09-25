# VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching

## 基本信息

- 正式标题：VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching
- 作者：Siyu Xu、Yunke Wang、Chenghao Xia、Dihao Zhu、Tao Huang、Chang Xu
- 年份：2025
- 发表 venue：NeurIPS 2025 主会
- CCF 等级：A
- 发表状态：正式会议论文
- DOI：10.52202/085713-5484 — [DOI](https://doi.org/10.52202/085713-5484)
- arXiv：2502.02175；预印本标题为 VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation
- 特别关注：是




- 引用量：9
- 引用量来源：OpenAlex
- 引用量查询日期：2026-09-25
- 本地 PDF：[[00_Paper_Pool/PDFs/01_VLA/VLA-Cache.pdf]]
## 论文定位

这篇论文属于 VLA 方向，主要讨论VLA 在连续控制中反复处理相邻视觉帧的重复内容，造成在线推理延迟。
核心思路是免训练地在相邻帧间复用静态视觉 token 的 KV 表示，并用 attention 和层级自适应策略保护任务相关区域。
与当前项目的联系：可作为双臂 VLA 推理加速候选，但需在双臂动态视角与本地控制栈上单独评估。

## 核心关键词

VLA、KV Cache、Inference Acceleration、Token Reuse、Real Robot、跨帧视觉 token 缓存、实时推理加速

## 快速摘要

### 研究问题

VLA 在连续控制中反复处理相邻视觉帧的重复内容，造成在线推理延迟。

### 之前方法的问题

单帧 token pruning 可能同时移除对当前夹爪和目标物判断关键的视觉信息。

### 核心思路

免训练地在相邻帧间复用静态视觉 token 的 KV 表示，并用 attention 和层级自适应策略保护任务相关区域。

### 输入

相邻时刻的图像帧、语言任务上下文及基座 VLA 的视觉 token/decoder attention。

### 输出与动作

保持原 VLA 基座动作输出；VLA-Cache 只改变推理中的视觉 token 计算与 KV 复用。

### 数据集与评测基准

LIBERO、SIMPLER，以及 Kinova Jaco2 四项真机操作任务。

### 主要结果

LIBERO 上 OpenVLA 延迟从 51.91 ms 降至 31.83 ms，平均成功率从 75.0% 变为 74.7%；真机平均成功率为 82.1%→84.6%。

### 与当前项目的关系

可作为双臂 VLA 推理加速候选，但需在双臂动态视角与本地控制栈上单独评估。
## 分类

- 主分类：VLA
- 分类：VLA、Robot Manipulation、Inference Acceleration
- 子分类：跨帧视觉 token 缓存、实时推理加速
- 标签：`VLA`、`KV Cache`、`Inference Acceleration`、`Token Reuse`、`Real Robot`

## 论文链接

- [NeurIPS 正式论文页](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f062da1973ac9ac61fc6d44dd7fa309f-Abstract-Conference.html)
- [arXiv 正文](https://arxiv.org/abs/2502.02175)（本轮实际下载并阅读 PDF）
- [项目主页](https://vla-cache.github.io/)

## 代码与资源

- [作者官方 GitHub](https://github.com/siyuhsu/vla-cache)
- 模型权重：评测脚本提供 OpenVLA/OpenVLA-OFT 基座权重下载入口；本文未新增独立 VLA-Cache 权重。
- [NeurIPS 官方补充材料](https://proceedings.neurips.cc/paper_files/paper/2025/file/f062da1973ac9ac61fc6d44dd7fa309f-Supplemental-Conference.zip)

## 机器人与具身形态

- 真机平台：Kinova Jaco2 单臂，前视相机；评测 PickPot、PlaceCube、PutSausage、WipeTable。
- 仿真平台：LIBERO、SIMPLER。
- 论文展示单臂平行夹爪操作，不含双臂实验。

## 正文速读

### 研究问题

VLA 在闭环操作过程中连续接收相邻视觉帧，而画面中大量背景和静态区域变化很小。现有模型每个时刻重新计算视觉 token，造成推理开销并限制实时控制频率。

### 之前方法的问题

通用 token pruning / merging 方法通常在单帧内删减或合并 token；若不考虑视觉区域对当前任务的重要性，可能删掉外观变化很小、但对夹爪或目标物判断至关重要的区域。作者在 LIBERO Spatial 上展示，仅依据静态视觉相似度进行缓存会显著降低成功率。

### 核心思路

VLA-Cache 是免训练的推理加速方法：识别相邻帧间稳定的视觉 token，跨帧复用其 Key-Value（KV）表示；再利用 decoder attention 排除任务相关区域，并根据各层 attention entropy 自适应调整缓存比例。

### 输入

- 当前与上一时刻的 RGB 视觉观测，用于计算图像 patch 相似度。
- 当前 VLA 基座的视觉 token、decoder attention 和语言指令上下文。
- 机器人状态是否显式输入取决于被加速的基座模型；VLA-Cache 本身不新增状态输入。

### 输出

- VLA-Cache 本身不定义新的动作输出头，而是将缓存策略插入基座 VLA 的视觉 token/decoder 推理流程。
- 最终机器人动作与被加速基座相同；OpenVLA、OpenVLA-OFT 与 CogACT 保留各自动作接口/动作头。

### 动作表示

- VLA-Cache 不改变动作表示。
- OpenVLA 实验保留基座动作输出；OpenVLA-OFT 保留 action chunking；SIMPLER 实验的 CogACT 使用其 diffusion policy 连续控制头。
- 本论文没有给出统一适用于所有评测模型的动作维度、坐标系、旋转编码、控制频率、chunk 长度或归一化定义。不得把某一基座的动作规格推广到 VLA-Cache 方法本身。

### 方法整体流程

1. 将当前图像切分为 patch，与上一时刻对应 patch 计算 cosine similarity，挑出外观稳定的候选 token。
2. 根据 decoder attention 估计任务相关性，从可复用候选中排除夹爪、目标物等对当前动作敏感的 token。
3. 依据不同 decoder layer 的 attention entropy 动态设置复用比例。
4. 对保留的静态视觉 token 复用上一时刻 KV 表示；对动态或任务相关 token 重新计算，再由原 VLA 基座生成动作。

### 核心模块

- 静态 token 选择：对相邻帧 image patches 计算 cosine similarity，并以阈值与 Top-k 筛选，见 §3.2、Figure 2。
- 任务相关 token 过滤：用 decoder attention 估计任务相关性，避免仅凭外观静态而缓存关键区域，见 §3.3、Algorithm 1、Table 1。
- Layer-adaptive token reuse：根据不同层的 attention entropy 分配复用比例，见 §3.4、Algorithm 2。
- 跨帧 KV 复用：稳定 token 沿用上一帧 key/value，变化 token 重新计算，见 §4.1、公式 (10)。

### 数据集

- LIBERO：沿用 OpenVLA/OpenVLA-OFT 标准设置，Spatial、Object、Goal、Long 四个任务套件，每套 10 个子任务。
- SIMPLER：采用 Google robot arm 模拟设置，在 Visual Matching 与 Variant Aggregation 两种设置下评估 4 类操作任务。
- 真机数据：Kinova Jaco2 上四个单指令任务；通过 Xbox controller 以 10 Hz 遥操作采集，每项任务 150–200 条轨迹。Appendix E.4 给出 trial protocol。
- 作者没有声称发布新的通用训练数据集；主要仿真评测沿用公开基准与基座权重。

### 评测基准与任务

- LIBERO：Spatial、Object、Goal、Long，分别衡量空间关系、物体操作、目标条件和长时程操作泛化（§5.2、Table 2）。
- SIMPLER：Visual Matching、Variant Aggregation，检查仿真与视觉/场景变化下的操作策略（§5.2、Table 3）。
- 真机：PickPot、PlaceCube、PutSausage、WipeTable；另在 PickPot 中引入人手/物体背景运动（Tables 5、7）。

### 对比方法

- LIBERO：OpenVLA 为基线；SparseVLM、FastV 是单帧视觉 token 加速对照，用于比较跨帧缓存与单帧 pruning/merging 的速度和成功率（Tables 2、4）。另在 OpenVLA-OFT 上比较加入 VLA-Cache 前后结果。
- SIMPLER：CogACT 为基线，检查该方法能否适配带 diffusion policy head 的混合 VLA（Table 3）。
- 真机：OpenVLA 为基线，对照相同任务启用/关闭 VLA-Cache（Tables 5、7）。

### 评测指标

- Success Rate（SR）：任务成功率。
- FLOPs：理论计算量。
- CUDA latency：GPU 推理时延。
- Control frequency：闭环控制频率。
- 论文同时报告了任务成功与推理效率，不应只用 FLOPs 或单项延迟代表实际运行效果。

### 主要实验结果

1. LIBERO（Table 2）：OpenVLA 平均 SR 为 75.0%、延迟 51.91 ms、FLOPs 1.864 T；加入 VLA-Cache 后为 74.7%、31.83 ms、1.355 T，延迟约提升 1.63 倍，SR 下降 0.3 个百分点。OpenVLA-OFT 平均 SR 从 96.8% 到 97.4%，控制频率从 65.10 Hz 到 78.98 Hz。
2. SIMPLER（Table 3）：CogACT Visual Matching 平均 SR 74.8%→74.4%，延迟 54.29→39.63 ms；Variant Aggregation SR 61.3%→62.3%，延迟 53.54→39.11 ms，控制频率 12.36→14.48 Hz。
3. 真机（Table 5）：四任务平均 SR 82.1%→84.6%，FLOPs 1.814→1.303 T，延迟 64.16→51.85 ms。分任务看 PickPot 从 95.0% 降至 90.0%，其余三项提高；不应把总体均值概括为每项任务都提升。
4. 动态背景（Table 7）：PickPot 基线 SR 从静态环境的 95% 降至背景运动下的 80%；加入 VLA-Cache 后在该动态条件下保持 80%，FLOPs 降低 42%，延迟降低 35%。

### 消融实验

- 静态相似度缓存（Table 1）：OpenVLA SR 84.4%→74.2%，延迟 51.56→31.03 ms；再过滤 task-relevant tokens 后 SR 回升至 82.6%；加入 layer-adaptive 后 SR 为 83.8%，延迟 32.22 ms。
- 缓存 token 数量（Table 4、Appendix Table 9）：激进减少 token 会导致成功率下降；OpenVLA 上复用 100 个 token 时，SR 83.8%、延迟 31.29 ms。OpenVLA-OFT 的 k 与阈值敏感性见 Appendix Tables 9–10。
- 任务相关性代理（Appendix Table 8）：OpenVLA-OFT 使用 attention proxy 时 SR 98.3%、延迟 61.12 ms；使用 object-mask proxy 时 SR 87.4%、延迟 87.49 ms，支持 attention 过滤优于此 mask 变体。
- 方法适用性对照（Table 3）：在 SIMPLER 的 CogACT 上仍有约 1.37 倍时延加速且成功率接近，说明可与 diffusion policy head 并用；不代表可直接加速不含 VLM decoder 的 standalone diffusion policy。

### 失败案例

- 论文没有系统列出逐例失败案例。Table 7 的动态背景实验显示背景运动会使未加缓存的 OpenVLA 成功率由 95% 降至 80%；VLA-Cache 在该扰动条件下也为 80%，因此结果支持效率改善，但不能声称消除了动态干扰导致的任务失败。
- Table 5 中 PickPot 的真机成功率由 95% 降至 90%，是 VLA-Cache 相对基线的一个退化任务。
- 作者指出，大量背景或物体运动会减少可复用 token 数，降低加速收益；见 Appendix A、Figure 4。

### 作者明确指出的局限

- 动态场景中不可复用 token 会增多，因而加速效果下降（Appendix A）。
- 实验主要基于 OpenVLA、CogACT、OpenVLA-OFT 及其 LLaMA2 decoder；对不同 backbone（作者举例 Gemma2/π0）和更复杂 VLA 架构的适用性仍待验证（Appendix A）。
- 作者建议真实部署时持续监控，以保障安全、可解释和可靠行为（Appendix B）。

### 文献库分析

- 该方法针对视觉 decoder 的重复计算，适合作为既有 VLA 的推理优化层；它不解决操作策略本身的泛化或失败恢复问题。
- 任务相关区域筛选是保证缓存不明显损害精度的关键；只做相似度匹配会使成功率显著下降（Table 1）。
- 真机结果来自 Kinova Jaco2 单臂、四个任务，样本量和场景覆盖有限；不能直接推断双臂、遮挡严重或高速变化环境的控制收益。

### 仍未解决的问题

- 当场景中运动区域很多时，缓存收益会减少；需要量化不同运动比例下延迟与成功率的权衡。
- 需要在更多 VLA backbone、动作头和不同控制硬件上验证缓存策略，尤其是论文作者指出的非 LLaMA2 架构。
- 对缓存命中错误、注意力相关性误判及其触发的单次任务失败缺少细粒度失效归因。

### 与当前项目的关系

当前项目可将 VLA-Cache 作为已训练 VLA 的在线推理优化候选，重点测试双臂相机画面、腕部视角变化和机械臂运动导致的动态视觉区域，记录延迟、控制频率和任务成功率。原论文没有双臂实验，部署收益需在本项目的机器人和控制接口上重新验证。

### 研究启发

#### 设想一：基于动作风险的缓存失效策略

- 证据来源：作者指出动态场景会减少缓存收益；Table 7 显示背景扰动会使任务成功率下降。
- 研究问题：当双臂交叉、目标遮挡或动作预测不确定时，触发局部/全量重新编码能否在不显著牺牲控制频率的情况下改善成功率？
- 定位：待检索和实验验证的研究问题，不宣称新颖性。

### 重要前置工作

- OpenVLA、OpenVLA-OFT、CogACT：作为被加速基座及不同动作头的验证对象（§5）。
- SparseVLM、FastV：作为单帧视觉 token 加速对照（§5.1、Table 2）。
- Open X-Embodiment：OpenVLA 训练数据来源，见论文 References；库内卡片：[[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]]。

### 引用关系

#### 库内引用

- [[02_Papers/01_VLA/Octo|Octo]]
- [[02_Papers/01_VLA/OpenVLA|OpenVLA]]
- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]]

#### 库内后续引用

- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey]]

### 证据

- 正文来源：[arXiv 正文 PDF](https://arxiv.org/pdf/2502.02175)，与 [NeurIPS 2025 正式论文页](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f062da1973ac9ac61fc6d44dd7fa309f-Abstract-Conference.html)核对。
- 官方代码来源：[作者 GitHub](https://github.com/siyuhsu/vla-cache)；已检查 README 和官方补充包。
- 核验日期：2026-09-23
- 实际阅读：§1–§6、Appendix A–F；检查 Figure 1–5、Tables 1–5、7–11 及官方补充实现说明。
- 失败/局限来源：Appendix A–B、§5.4、Table 7；主要结果：Tables 2–5、7。
- 补充材料：NeurIPS 官方 Supplemental zip 已下载检查，含实现说明和 OpenVLA-OFT 源码包；同时查看 arXiv 附录。
