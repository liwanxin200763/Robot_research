# PEARS: Physical-Prior-Guided Efficient Adaptation via Failure Reasoning and Diffusion Steering for Tactile Manipulation

## 基本信息

- 作者：Kun Song、Yiming Wang、Yilin Chen、Tianyi Ding、Jiaxin Tian、Tianqi Gong、Daolin Ma、Jia Pan
- 年份：2026
- 发表 venue：arXiv 预印本；未见正式会议或期刊接收信息
- 论文类型：触觉操作与部署期在线适应方法
- 研究方向：机器人操作、VLA 部署期适应、失败原因判断、力反馈、接触丰富操作
- 关键词：PFR、DSRL、tactile feedback、force–position control、flow matching、failure reasoning
- 论文链接：https://arxiv.org/abs/2610.08784
- DOI：未见独立 DOI；arXiv 记录未列 DOI
- arXiv：2610.08784
- 项目主页：https://song-kun.github.io/pears/
- 代码：作者项目页的 Code 按钮尚不可用；未见可访问的官方仓库
- 本地 PDF：[[00_论文池/PDFs/02_机器人操作/PEARS.pdf|PEARS.pdf]]
- 引用量：
- 引用量来源：

## 详细摘要

### 1. 研究背景与问题

预训练 VLA／VTLA 在部署环境的物体属性、接触动力学或位置变化下，可能出现对位、接触时机及接触力错误。直接用真机 RL 纠错需要大量可能损坏物体的试验。论文要减少接触丰富操作中部署期适应所需的交互次数。（第 I 节）

### 2. 核心方法

PEARS 将两条纠错途径分开：触觉条件化 DSRL 在冻结的 GR00T N1.7 flow-matching 策略的初始噪声空间训练轻量 actor–critic，主要纠正自由空间轨迹和接触时机；Physics-guided Force Reasoning（PFR）在每回合后根据最终接触画面、触觉力轨迹和本回合力区间判断用力不足、过大或非力相关错误，再更新力区间。50 Hz 的混合力—位置控制器只在接触阶段约束选定力轴，其他自由度仍跟随基础策略。PFR 判断为对位／轨迹错误时不改力区间。（第 III–IV 节、图 1–2、算法 1）

### 3. 输入、动作与数据

基础策略读取腕部与外部 RGB、语言指令、末端位姿和夹爪宽度；两指尖 6D 力／力矩可加入 VTLA 输入。策略预测 32 步的 10 维末端动作块，每次执行前 10 步再观测。RL actor 使用视觉特征、本体状态及双指尖力信号，在 10 维潜在噪声空间学习；基础模型参数保持冻结。每项任务用 50 条离线示范微调基础策略，在线适应另用成功／失败终止奖励。（第 III–V 节）

### 4. 实验、基线与结果

Isaac Sim 三任务是 Thin Sheet Transfer、Bottle Cap Twisting、Fragile Fruit Picking；基线为冻结策略、Residual RL、AWR、DPPO、DSRL。每种在线方法进行 3 次各 100 回合适应，随后每次 100 个测试回合。PEARS 最终成功率分别为 **94.7%、87.7%、77.7%**；各任务最强对照分别为 DSRL **82.3%**、Residual RL **68.0%**、DSRL **40.3%**，提升 12.4、19.7、37.4 个百分点。Bottle Cap Twisting 达到 80% 在线成功率的回合数为 22，对照 Residual RL 为 47。真机 Whiteboard Erasing 为 **19/20**，Pipette Liquid Aspiration 为 **18/20**；冻结策略分别为 11/20、8/20，DSRL 为 15/20、12/20。真机方法各用 40 次在线交互后评估 20 次。（第 V 节、表 I、III、图 3）

### 5. 消融与失败案例

去掉 PFR／外部力控制，仅保留 DSRL 时三任务成功率为 82.3%、57.7%、40.3%；去掉 DSRL，仅保留 PFR／力控制时为 77.0%、84.7%、61.7%；完整模型为 94.7%、87.7%、77.7%。固定初始力区间、随机搜索力区间及替换 VLM 为 Qwen3-VL-2B 的结果也见表 II，说明力区间适应与噪声空间运动纠错有互补性。真机最终剩余失败：白板擦拭 1 次对位不准，移液管吸液 2 次初始抓取偏位；作者明确指出 PFR 目前只为用力不当提供定向纠正，其他错误仍依赖常规 RL。（第 V–VI 节、表 II–III）

### 6. 局限与研究线索

**作者所述：**PFR 的定向推理目前限于接触力错误；未来需让失败原因推理指导更一般的 RL 探索与策略更新。（第 VI 节）

**文献库分析：**力控制轴在训练前仍需人工审核纠正；真机只验证两类接触任务，尚不能推出普通夹爪双臂或长程失败恢复的性能。可对照 [[02_论文/01_VLA/Taming VLAs under Robot Execution Errors - Self-Compensation and Stress Testing|Taming VLAs]] 的命令—实际运动残差补偿与 [[02_论文/07_泛化与长程任务/Recova - Agent-Guided Failure Recovery for Autonomous Robotic Manipulation|Recova]] 的失败后恢复，单独测试“检测到失败原因 → 调整力／轨迹 → 再执行”的收益。（第 IV–VI 节；后两项为研究建议）
