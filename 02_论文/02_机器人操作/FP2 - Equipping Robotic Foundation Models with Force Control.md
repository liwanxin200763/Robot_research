# FP2: Equipping Robotic Foundation Models with Force Control

## 基本信息

- 作者：Hongjie Fang、Shirun Tang、Junjian Hu、Shidong Zhang、Derek Zhang、Linhao Chen、Dehai Li、Mingyu Mei、Wanxi Liu、Cewu Lu、Shiquan Wang
- 年份：2026
- 发表 venue：arXiv 预印本
- 论文类型：预印本；机器人操作与力控制方法
- 研究方向：接触丰富的机器人操作；机器人基础模型；VLA；力控制
- 关键词：Action-Regulation Decomposition；Force Feedback；Contact-Rich Manipulation；Hybrid Force-Position Control；Execution Error
- 论文链接：[arXiv 论文](https://arxiv.org/abs/2609.37433)
- DOI：[10.48550/arXiv.2609.37433](https://doi.org/10.48550/arXiv.2609.37433)
- arXiv：[2609.37433](https://arxiv.org/abs/2609.37433)
- 项目主页：[FP2 项目页](https://force-policy.github.io/fp2/)
- 代码：—
- 本地 PDF：[[00_论文池/PDFs/02_机器人操作/FP2.pdf|查看 PDF]]
- 引用量：
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

机器人基础模型已能依据视觉、语言和本体状态生成任务级动作，但插入、翻转和擦拭等接触任务需要快速根据实际受力调整执行。几何与摩擦的小偏差会使合理的运动轨迹仍然失效。（论文第 I 节，图 1）

### 2. 论文要解决的问题

在保留预训练基础模型动作生成能力的同时，为其补上可响应力反馈的物理交互调节，而不要求基础模型重新学习一种新的力传感输入。（第 I、III 节）

### 3. 之前方法存在的问题

把力直接并入 VLA 输入会改变预训练时的观测接口，下游少量数据须重新对齐视觉、动作与受力。专门训练的力控策略能够调节接触，却不一定保留基础模型的任务语义和运动先验；已有全局—局部力控方法还会在下游重复预测动作，增加延迟和泛化负担。（第 I–II 节）

### 4. 核心思路

采用 **Action-Regulation Decomposition**：先将基础模型适配到任务并冻结，让它继续产生动作序列；另训练轻量、高频的 Force-Control Policy，只预测执行该动作时所需的力控参数。两个策略职责分开，力反馈只进入后者。（第 III 节，图 2）

### 5. 方法与系统结构

Foundation Policy 从原生观测和指令生成 Action Chunk 与上下文 Token。压缩器以可学习 query 对 Token 做 cross-attention，压成单个上下文 Token；训练时重建原 Token，之后丢弃解码器。Force-Control Policy 将缓存的压缩上下文与最近的 Wrench（六维力／力矩）及 Proprioceptive History（机器人自身状态历史）结合，预测 **interaction frame Σ、force-position selection mask S、desired wrench Ŵ**。Σ 定义局部作用坐标，S 选择各方向由力还是位置控制，Ŵ 给力控方向的目标受力；它们与基础策略的轨迹一起送入 Hybrid Force-Position Controller，形成受力调节后的运动。（第 III-A–D 节，图 2）

### 6. 输入信息

基础策略继续使用各自原生的视觉、语言、本体观测，**没有力输入**。下游力控策略使用压缩的基础策略上下文、近期 Wrench 与 Proprioception；本设计不再给下游力控策略额外输入腕部相机画面。实验平台仍安装全局与腕部相机，不能据此误称整个系统没有腕部视觉。（第 III-B–C、IV-A 节）

### 7. 输出 / 动作表示

基础策略约 **2 Hz** 生成含 **15 Hz waypoints** 的动作块。对齐因推理延迟产生的 waypoint 偏差后，五次样条将轨迹重采样为 **50 Hz** 参考；力控策略也在 **50 Hz** 输出 Σ、S、Ŵ，混合力—位置控制器内部以 **1 kHz** 执行。压缩上下文在两次 2 Hz 基础策略更新之间缓存复用。力控分支**不重新生成动作**。（第 III-B–D 节）

### 8. 数据来源与采集方式

在 Flexiv Rizon 4、GN-02 夹爪和法兰六轴力／力矩传感器上，经带力反馈的 arm-to-arm 遥操作采集同步视觉、动作与受力示范：Flip Box、Wipe Curve、Insert EV Charger 各 **50 条**，Insert Peg **200 条**。论文没有把这些规模说成跨任务共享训练集。（第 IV-A 节）

### 9. 数据处理与数据增强

基础策略按各模型原有任务适配流程学习无力动作；压缩器从固定基础策略提取上下文 Token，以 MSE 与余弦距离重建它们。力控监督信号从带受力的示范恢复。执行时用 waypoint dropout 和动态时间规整找合适起点，再以五次样条平滑。正文未将特定图像增强配方作为 FP2 的贡献。（第 III-B–D、IV-A 节）

### 10. 训练方式

三阶段：①无力输入适配 RFM；②冻结 RFM，自监督训练上下文压缩器；③冻结 RFM 与压缩器，仅训练 Force-Control Policy 的结构化力控输出。实验使用 **GR00T N1.7、LaWAM、π0（LoRA）、π0.5（全量适配）** 四种基础策略，其中 LaWAM 不是 VLA 的同义词，而是世界模型式 RFM。（第 III、IV-A 节，图 2、表 I）

### 11. Benchmark 与实验设置

四项真机任务：Flip Box、Insert EV Charger、Insert Peg、Wipe Curve；每种方法每项任务 **25 组测试配置／试次**。前三项以成功率 SR 衡量，擦拭用清除标记区域的完成率 CR；另报告成功执行时受力偏离示范范围的 **Normalized Force Error（NFE，越低越好）**。平均分是三项 SR 与一项 CR 的算术平均，不能解释为四项都采用相同的成功率指标。基线分为原 Foundation Policy、显式力控的 HybridIL／ACP／Force Policy，以及把力直接输入模型的 TA-VLA／ForceVLA；后两者与 FP2 的受控比较共用 π0 LoRA、示范与测试配置。（第 IV-A 节，表 I）

### 12. 真机实验

全部四项为真实 Flexiv Rizon 4 机械臂实验，使用全局与腕部 Intel RealSense D415 RGB-D 相机、法兰 FT-03S 六轴力矩传感器和 RTX 5090 工作站。充电枪插入需要沿正确方向建立较大接触力；插销实验的圆孔公差为 **0.02 mm**，容易卡住；曲面擦拭须持续贴合。（第 IV-A 节，图 3）

### 13. 主要实验结果

表 I：π0 LoRA 的四任务平均分 **15%→80%（+65 个百分点）**；四项分别为翻箱 **44→68%**、充电枪 **0→92%**、插销 **12→76%**、擦拭完成率 **4→84%**。π0.5 的平均分 **42→75%**，GR00T N1.7 **12→39%**，LaWAM **25→39%**；因此不能说 FP2 解决了所有任务，例如 GR00T N1.7＋FP2 的插销仍为 **0%**。π0＋FP2 在充电枪成功执行上的 NFE 为 **0.249**，但原 π0 无成功试次，NFE 不能按 0 处理。成功试次限定的 NFE 与任务成功率应分开比较。（第 IV-B 节，表 I）

### 14. 消融实验

Flip Box＋π0.5 的表 II：只用模型上下文在新物体上平均 **5%**，只用受力／本体历史 **18%**，结合后 FP2 为 **88%**；简单平均池化上下文为 **75%**，动作 latent 为 **80%**。加入腕部视觉的新物体结果为 **73%**、延迟 **5.97 ms**；下游重新预测动作时为 **53%**、**13.03 ms**；原方案 **88%**、**4.48 ms**。新物体测试跨颜色、纹理、软硬和几何四类共 **40 次**，延迟仅指力控策略，不是全系统时延。（第 IV-D 节，表 II）

### 15. Failure Case

原基础策略常因接触丢失、插入力不足、受力不稳定而失败；FP2 对这些交互相关错误有效。图 5 按每种策略 **25 次** 拆分成成功、位置错误和交互相关错误；加入 FP2 后剩余失败更多与目标位置不符或几何对齐相关。图 4 展示插销搜索时未接触孔位、曲面擦拭失去接触等实例。（第 IV-B–C 节，图 4–5）

### 16. 主要局限

**作者明确指出：**FP2 假设基础策略已经能提出可行的任务级运动，不能完整纠正错误的动作生成或几何推理；力调节目前按任务学习，跨任务共享力控尚未完成。**本库分析：**文中只在一套 Flexiv 平台和四种接触任务测试；对其他机械臂、夹爪或更长时序的恢复控制仍需新实验，不能外推为已验证。（第 V 节）

### 17. 与已有工作的关系

它承接 [[02_论文/01_VLA/OpenVLA - An Open-Source Vision-Language-Action Model|OpenVLA]] 一类基础策略的“根据视觉与语言生成动作”路线，也与任务专用的 Force Policy 比较；不同点是**保留基础策略的动作输出，仅在其后叠加交互调节**。[[02_论文/01_VLA/Taming VLAs under Robot Execution Errors - Self-Compensation and Stress Testing|Taming VLAs]] 则用命令—执行残差在线更新动作专家，提前补偿机械跟踪偏差；FP2 的反馈是力／力矩和本体历史，调节的是高频接触控制，两者并非同一种执行错误方法。与 [[02_论文/01_VLA/Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action Models|FailBank]] 的训练反馈循环不同，FP2 研究的是本次执行过程中的物理调节。（第 II–IV 节；Taming VLAs 第 3–5 节）

### 18. 对当前研究方向的价值

对普通夹爪执行接触操作，可把“计划／几何错误”和“受力／接触错误”作为两个可测故障来源。**潜在研究启发：**在 Execution Error 检测后，按错误类型选择力调节、重新定位或重规划，并比较有无受力历史的效果。FP2 已验证的是交互调节收益，**没有证明自己能完成通用 Failure Recovery**。（第 IV-C、V 节）

### 19. 一句话总结

FP2 不改动基础模型的动作生成接口，而用压缩模型上下文和实时受力历史驱动高频力控，让可行轨迹更可靠地完成接触操作。

## 我的阅读笔记
