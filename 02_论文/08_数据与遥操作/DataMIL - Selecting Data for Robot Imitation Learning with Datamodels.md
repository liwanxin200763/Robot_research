# DataMIL: Selecting Data for Robot Imitation Learning with Datamodels

## 基本信息

- 作者：Shivin Dass; Alaa Khaddaj; Logan Engstrom; Aleksander Mądry; Andrew Ilyas; Roberto Martín-Martín
- 年份：2026
- 发表 venue：ICLR 2026（arXiv 首发于 2025）
- 论文类型：会议论文；机器人示范数据选择方法
- 研究方向：数据与遥操作；模仿学习数据筛选
- 关键词：Data Selection；Datamodels；Influence；Imitation Learning；Cross-Embodiment
- 论文链接：[ICLR 2026 正式论文](https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html)
- DOI：
- arXiv：[2505.09603](https://arxiv.org/abs/2505.09603)
- 项目主页：[作者项目页](https://robin-lab.cs.utexas.edu/datamodels4imitation/)
- 代码：[UT-Austin-RobIn/datamil](https://github.com/UT-Austin-RobIn/datamil)
- 本地 PDF：[[00_论文池/PDFs/08_数据与遥操作/DataMIL.pdf|查看 PDF]]
- 引用量：
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

通用机器人数据集很大但异质，针对新任务简单使用全部旧数据可能产生负迁移；目标任务示范又少，需要知道哪部分旧数据真正有用。（全文 §1）

### 2. 论文要解决的问题

在不做大量真机 rollout 的前提下，为既有示范估计其对目标任务最终模仿策略表现的贡献，并选出值得联合训练的子集。（§1、§3–4）

### 3. 之前方法存在的问题

视觉、语言、动作相似度是启发式代理，未必等于训练后的策略收益；真实机器人 rollout 昂贵且不可微。只用目标任务少量示范或混用所有历史数据也可能很差。（§1–2）

### 4. 核心思路

用 datamodel 估计训练数据子集变化对目标策略指标的影响；以目标任务保留示范上的 proxy loss 替代在线成功率，在轨迹/片段簇粒度排序，选高正贡献数据与目标示范 co-training。（§3–4，图 1）

### 5. 方法与系统结构

给历史数据簇分数 τ，目标是预测训练子集加入/移除后策略评价的变化。小策略可在随机子集上反复训练，用回归估分；大策略用对数据权重求 metagradient 估影响。以 held-out target loss 作为可微代理，缓解真机 rollout 成本；结果是在固定选择比例下选分数最高的旧数据，而非生成新轨迹或给所有样本持续加权。分数是特定目标任务和训练算法条件下的影响估计，不是任务无关的绝对“质量”。（§3–4）

### 6. 输入信息

大规模旧示范 D、少量目标示范 Dtarget、可训练策略 A、目标示范上的代理评价指标；在视觉设置中还输入图像、语言、动作轨迹。（§3–5）

### 7. 输出 / 动作表示

输出对旧数据轨迹/片段簇的影响分数和选中子集 Dsel；下游 Octo/MLP 策略再学习动作。DataMIL 本身不产生新的关节或末端控制动作。（§4.3）

### 8. 数据来源与采集方式

MetaWorld 50 任务：专家示范加 SAC 探索轨迹，每任务 5 条目标专家示范；LIBERO-90 的 4500 条遥操作示范作旧数据，LIBERO-10 每目标任务取 5 条；真机从异质 OXE13/OXE23/OXE24 子集选数据，目标任务另行遥操作采集 10–40 条。OXE 选择比例 0.5%–1%，研究的是筛选现有数据而非扩增规模；计算成本详见附录 G。（§5、附录 F 表 2–3）

### 9. 数据处理与数据增强

把样本聚成轨迹或短片段以降噪，LIBERO 用长度 15 的片段、按影响分数选前 10%；真机按整条轨迹筛选，并拆分目标数据以减小代理评价的分布偏移。多样性不是单独最大化指标；实验发现可从不同本体、不同来源选出正迁移数据。未给单独的 state coverage 或 action diversity 优化目标。（§4.2–4.3、§5.2、附录 F）

### 10. 训练方式

MetaWorld 用回归估计 datamodel；LIBERO/OXE 因 Octo 训练昂贵采用 metagradient。选完数据按 α=0.5 混合目标数据和选中旧数据做 BC/Octo 微调；LIBERO 训练 10k 步，OXE 50k 步。附录 G 指出 metagradient 通常比普通训练慢 3–5 倍，OXE 的估分在 4 张 A100 上需 3–4 天。（§4–5、附录 F–G）

### 11. Benchmark 与实验设置

MetaWorld 50 任务、LIBERO-10、四类真实任务（Franka-Ball、Franka-Pouch、Tiago-Sink、Droid-Multitask）；对照 Target-Only、All-Data/Random、基于状态或动作的检索、Behavior Retrieval、Flow Retrieval、STRAP。LIBERO 每任务 50 次 rollout、5 个随机种子；真机按附录 F 表 3 的固定次数评测且只有一个种子。（§5、附录 F）

### 12. 真机实验

OXE 异质数据支持 Franka 两任务、未在旧数据出现的 Tiago 本体任务和 DROID 三任务组合；比较以固定物体位姿的真机 rollout 评估。其跨本体结果是“选择相关旧轨迹”的证据，并非模型无微调零样本执行。（§5.1–5.2、附录 F）

### 13. 主要实验结果

LIBERO-10 平均成功率 DataMIL 37.76%，优于 BR 36.4% 与 All-Data 27.72%；OXE 真机平均 61.0%，对比 Flow 40.0%、BR 39.4%、All-Data 30.9%；Franka-Pouch 为 70.6%，Tiago-Sink 为 64.1%，均见附录表 1。并非每个单独 LIBERO 任务都第一，如 Bowl-Cabinet 低于 STRAP。（§5、附录 C.7 表 1）

### 14. 消融实验

LIBERO-5 上比较选取比例、簇长度和 co-training 比例：5%–10% 选择比例时优势明显，≥20% 时方法差距缩小；长度 15 片段优于更粗聚类；α=0.5 效果较好。也比较 rollout 真指标与 proxy loss、回归与 metagradient，代理和高效估计稍有精度损失但避免昂贵 rollout。（§4.2、附录 C.3–C.5、图 2、13）

### 15. Failure Case

相似状态可对应相反或无益动作，启发式检索会选到视觉接近但损害目标策略的样本；DataMIL 在部分 LIBERO 任务仍弱于特定基线，说明影响估计并非万能。论文未提供在线机器人执行错误恢复机制。（§5.2、附录 A、C.7）

### 16. 主要局限

作者指出估分成本仍高，选择比例与簇粒度缺乏原则化设定，主要评价仍偏单目标任务，超大规模多任务推广待验证；真机仅单种子评估。（§6、附录 F–G）

### 17. 与已有工作的关系

Re-Mix 优化数据域的混合比例；相似度/“Data Quality”规则根据表观属性判断；CUPID 用在线 rollout 的 policy-gradient influence 做单任务筛选。DataMIL 关注目标任务策略表现的离线影响估计，可在异质数据集选择片段/轨迹，而不是简单固定域权重或凭视觉相似度打分。（§2）

### 18. 对当前研究方向的价值

可用于判断跨本体轨迹、普通夹爪双臂数据中哪些片段真正改善目标 VLA/IL 策略；若面向失败恢复，可以把目标验证集设为执行误差场景，但这是库内研究设想，论文未直接实证。（§4–6）

### 19. 一句话总结

DataMIL 用离线 datamodel 估计旧示范对目标机器人策略的条件性贡献，选择高收益数据进行模仿学习。

## 我的阅读笔记

全文依据：本地 PDF §1–6、图 1–6、附录 C/F/G 与附录表 1。正式标题包含副标题，ICLR 身份以会议 proceedings 页面为准。
