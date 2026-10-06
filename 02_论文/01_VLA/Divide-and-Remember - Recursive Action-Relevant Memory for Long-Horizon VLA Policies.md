# Divide-and-Remember: Recursive Action-Relevant Memory for Long-Horizon VLA Policies

## 基本信息

- 作者：Xuehui Yu、Eason Yu、Meiyi Wang、Haozhe Du、Stefano V. Albrecht、Harold Soh
- 年份：2026
- 发表 venue：arXiv 预印本
- 论文类型：VLA 记忆方法
- 研究方向：VLA、长程操作、动作相关记忆
- 关键词：Divide-and-Remember、D&R、long-horizon、RoboMME、memory selection
- 论文链接：https://arxiv.org/abs/2610.00982
- DOI：https://doi.org/10.48550/arXiv.2610.00982
- arXiv：2610.00982
- 项目主页：https://dnr-memory.github.io/
- 代码：论文声称项目页提供代码与权重，但核查时项目页仍标注 Code (coming soon)；未见可访问的官方仓库
- 本地 PDF：[[00_论文池/PDFs/01_VLA/Divide-and-Remember.pdf|Divide-and-Remember.pdf]]
- 引用量：
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景与问题

历史依赖操作中，当前画面不足以决定下一步动作。固定采样帧或按像素变化挑帧，可能保留与动作无关的画面，却丢失先前抓取方式、对象位置或事件次数。论文把“记什么”表述为在当前观测已知时，保留历史中对动作仍有用的信息。（第 1、4 节）

### 2. 方法

Divide-and-Remember（D&R）以条件互信息 `I(a_t; m_t | o_t)` 解释理想记忆；实际训练使用 VLA 动作损失优化选择器，并不直接计算该互信息。方法在预训练视觉 token 空间保留历史图像 patch：共享的轻量选择器每次从 2K 个 token 选 K 个，再将相邻结果递归合并、重选。SigLIP 视觉编码器冻结，选择器用时空位置编码与自注意力评分，训练时借助可微近似和 Gumbel 噪声，部署时取 Top-K。记忆接入 π0.5 动作专家。（第 4–5 节、图 3–4）

### 3. 数据、基线与实验

RoboMME 含 16 项长程操作任务，涉及计数、遮挡后跟踪、回忆早期片段及模仿先前动作。所有模型在同一多任务示范集上训练；比较 FrameSamp、TokenDrop、HAMLET、RB-VLA、TTT 和无记忆 π0.5。仿真中记忆预算统一为 64 token，每任务评估 50 个 episode，并跨最后三个 checkpoint 和三个随机种子统计。（第 6.1 节、表 1／7）

### 4. 主要结果与消融

RoboMME 16 项平均成功率：D&R 38.6%，HAMLET 32.2%，FrameSamp 27.9%，无记忆 π0.5 17.9%。D&R 对依赖具体历史画面的任务更强；对持续累积的状态类事实，潜在记忆仍有竞争力。Franka Panda 真机四项任务、每项 10 次测试中，D&R 成功 35/40，FrameSamp 22/40，无记忆策略 3/40；这些是真机小样本结果。（第 6.2 节、表 1–2）

候选池扩大并非单调增益：64-token 预算下，512-token 候选池平均 38.58%，1024-token 候选池下降到 34.42%。加入世界预测辅助损失时平均成功率由 36.89% 降至 33.55%，加入历史文本 token 降至 30.32%；这两项消融固定候选池为 256 token，不能与 512-token 主设置直接比较。（第 6.3 节、表 4–6）

### 5. 失败与局限

InsertPeg 中各方法成功率都很低；论文观察到策略能找到正确插入位置，但精密插入仍失败，说明记忆无法替代接触控制。真机 D&R 在 RepickCube 的一次失败中选错第二个方块；在 TrackCube 的一次测试中虽找到正确杯子，却因提前停止而判失败。（第 6.2 节、附录真机失败分析）

**作者指出：**D&R 在状态类事实方面仅与潜在记忆相当，在 StopCube 和 ButtonUnmask 上落后；直接保存历史 token 不如潜在记忆善于压缩、聚合信息，多任务共享记忆也可能有冗余。（第 7 节）**本库分析：**方法改善历史信息选择，但没有建立针对物理执行偏差的在线检测与恢复。对当前项目可检验的组合是把历史关键状态与执行反馈对齐，判断偏差属于记忆错误、目标绑定错误还是机械执行错误；这不是本文已有结论。
