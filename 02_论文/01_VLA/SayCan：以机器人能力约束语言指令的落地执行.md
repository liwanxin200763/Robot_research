# SayCan：以机器人能力约束语言指令的落地执行

## 基本信息

- 英文标题：Do As I Can, Not As I Say: Grounding Language in Robotic Affordances
- 作者：Michael Ahn; Anthony Brohan; Noah Brown; Yevgen Chebotar; Omar Cortes; Byron David; Chelsea Finn; Chuyuan Fu; Keerthana Gopalakrishnan; Karol Hausman; Alex Herzog; Daniel Ho; Jasmine Hsu; Julian Ibarz; Brian Ichter; Alex Irpan; Eric Jang; Rosario Jauregui Ruano; Kyle Jeffrey; Sally Jesmonth; Nikhil J Joshi; Ryan Julian; Dmitry Kalashnikov; Yuheng Kuang; Kuang-Huei Lee; Sergey Levine; Yao Lu; Linda Luu; Carolina Parada; Peter Pastor; Jornell Quiambao; Kanishka Rao; Jarek Rettinghouse; Diego Reyes; Pierre Sermanet; Nicolas Sievers; Clayton Tan; Alexander Toshev; Vincent Vanhoucke; Fei Xia; Ted Xiao; Peng Xu; Sichun Xu; Mengyuan Yan; Andy Zeng
- 年份：2022
- 发表 venue：Conference on Robot Learning (CoRL 2022), Proceedings of Machine Learning Research 205, pp. 287–318
- 论文类型：会议论文
- 研究方向：VLA
- 关键词：Language Grounding；Affordance；长时序规划；机器人操作；RL；IL
- 论文链接：[官方论文](https://research.google/pubs/do-as-i-can-not-as-i-say-grounding-language-in-robotic-affordances/)
- DOI：10.48550/arXiv.2204.01691 — [DOI](https://doi.org/10.48550/arXiv.2204.01691)
- arXiv：2204.01691
- 项目主页：[项目主页](https://say-can.github.io/)
- 代码：[GitHub](https://github.com/google-research/google-research/tree/master/saycan)
- 本地 PDF：[[00_论文池/PDFs/01_VLA/SayCan.pdf|查看 PDF]]
- 引用量：3844
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

LLM 能把抽象指令拆成步骤，却没有亲身执行经验，也不知道眼前是否有目标物体、机器人能否完成抓取。机器人已有的低层技能恰好提供了现实约束。（第 1 节）

### 2. 论文要解决的问题

让移动操作机器人在真实厨房执行自然语言给出的抽象、长时序任务，同时避免只凭语言合理性选择当前不可执行的动作。（第 1、3 节）

### 3. 之前方法存在的问题

直接由 LLM 生成计划可能出现技能库以外的操作；把生成文本映射到已有技能，仍不能保证当前状态下可行。单独的语言条件 BC/RL 策略则难以处理高层长指令。（第 3、5.1 节）

### 4. 核心思路

把每项技能的语言相关性「Say」与在当前状态成功执行的概率「Can」相乘，再选分数最高的技能；执行后重新评估，直到输出终止技能。价值函数承担可供性估计，LLM 承担任务语义拆解。（第 3 节，算法 1）

### 5. 方法与系统结构

输入用户指令、机器人当前观测和带有文字描述的预训练技能库；LLM 对候选技能评分，语言条件价值函数按当前图像估计成功率，二者乘积用于逐步决策；对应 BC 或 RL 控制策略执行技能。每一步都把已选技能加入提示上下文。（图 2、图 3；第 3–4 节）

### 6. 输入信息

高层自然语言指令、已有技能文本标签与当前机器人 RGB 观测。语言编码器生成技能文本嵌入；本文的主系统没有把深度、触觉或点云作为所述核心输入。（第 4 节）

### 7. 输出 / 动作表示

高层输出是一项离散技能，如寻找、抓取、搬运或终止。低层策略输出末端 6 自由度姿态、夹爪开闭、移动底盘的平移与偏航增量，以及终止指令；不是端到端连续动作 Token VLA。（第 4 节）

### 8. 数据来源与采集方式

主系统提供 551 项候选技能设计，覆盖 7 类技能和 17 种物体；实际组合评测选用当时表现较可靠的技能。低层 BC 参考 BC-Z 的真实机器人数据训练，RL 价值函数在 Everyday Robots 仿真中训练，并使用 RetinaGAN 进行 Sim2Real。人类评估者依据视频给技能成功与否标注。论文此处未给出可直接等同于 551 项技能的轨迹总数。（第 4 节及附录 C、D）

### 9. 数据处理与数据增强

技能描述先经冻结的句子编码器转为嵌入，再用于多任务策略和价值函数；仿真 RL 借助 RetinaGAN 转换视觉域。稀疏奖励按三名评估者中至少两人的判断确定。未见主系统使用大规模图像增强的统一配方。（第 4 节及附录 C）

### 10. 训练方式

低层技能由多任务 BC 或 RL 学得；语言条件价值函数通过时序差分学习估计技能可执行性。LLM 通过提示与候选评分参与规划，论文并未宣称联合端到端训练 LLM 和控制策略。（第 2–4 节）

### 11. Benchmark 与实验设置

在训练使用的模拟办公室厨房与另一真实办公室厨房测试 101 条指令、7 类任务，包括单技能、抽象名词/动词、体现当前环境状态的指令和长时序任务。两个指标分别是计划能否完成任务、机器人执行后是否完成任务，均由三位评估者按多数票判断。基线包括去掉价值函数的 No VF、生成式计划再映射技能、直接使用自然语言的 BC NL，以及嵌入检索的 BC USE。（第 5 节，表 1–2）

### 12. 真机实验

使用 Everyday Robots 移动操作平台：单个 7 自由度机械臂、两指夹爪与移动底盘；两个办公室厨房，含 15 种物体和 5 个语义位置。技能策略接收 RGB 图像。101 条指令中有 15 条长时序指令。论文未给出统一的主系统控制频率，不能据此推断 Hz。（第 4–5 节，图 4）

### 13. 主要实验结果

PaLM-SayCan 在模拟厨房的计划成功率为 84%、执行成功率 74%；迁移到真实厨房分别为 81%、60%（表 2）。在同一 101 条任务上，FLAN-SayCan 为 70%/61%，PaLM-SayCan 为 84%/74%（表 3）。新添抽屉技能后，21 条相关指令的计划成功率 100%，但执行仅 33%（第 5.2 节）。这些数字说明规划与实际动作仍有明显落差。

### 14. 消融实验

去掉可供性价值函数后，模拟厨房计划成功率由 84% 降至 67%；生成式规划后匹配技能为 74%，BC NL 在实验指令上的执行成功率为 0%（表 2）。提示示例从 0 增到 17 个时，语言模拟器中要求正确终止的规划成功率由 10% 升至 88%（附录 D.3，表 5）。

### 15. Failure Case

长任务常在只完成第一件物品后提前终止；否定指令与含糊指代也会让 LLM 出错。可供性模型有时误判薯片或海绵不可抓，导致反复导航或跳过抓取。论文把规划错误中的 65% 归于 LLM、35% 归于可供性模块。（第 5.1 节，附录图 16）

### 16. 主要局限

作者指出系统继承 LLM 偏差，能力受现有技能库和技能可靠性限制；若技能高估自身成功率但执行失败，当前系统不易及时纠正。附录中「放置」技能甚至被固定设为总是可行，表明可供性建模仍不完整。（第 8 节、附录 D.2）

### 17. 与已有工作的关系

相较只生成高层计划或把语言直接交给 BC 策略，SayCan 明确用环境相关的价值函数约束候选技能。它是技能级规划与控制组合，和 OpenVLA、Octo 这类直接从观测预测低层动作的通用策略处于不同层级。（第 3、7 节）

### 18. 对当前研究方向的价值

对于双臂普通夹爪，可以借鉴「语义有用」与「当前可执行」分开的思想，为抓取、交接、放置等技能建立条件成功率，再结合执行反馈设计失败恢复。后一方向是基于论文失败与局限提出的研究推论，不是 SayCan 已验证的双臂结果。

### 19. 一句话总结

SayCan 用语言模型负责长任务分解，再用机器人技能价值函数把每一步约束到当前真正可执行的范围。

## 相关论文

- [[将动作视为语言：在避免灾难性遗忘的条件下将 VLM 微调为 VLA]]
- [[Octo：开源通用机器人策略]]
- [[RoboMamba：用于机器人推理与操作的高效 VLA 模型]]
- [[基础模型赋能机器人：迈向具身 AI 的综述]]
- [[从动作 Token 化视角综述 VLA 模型]]
- [[面向具身 AI 的 VLA 模型综述]]
- [[迈向统一理解机器人操作：综合综述]]
- [[OpenVLA：开源视觉—语言—动作模型]]
- [[HAMSTER：面向开放世界机器人操作的分层动作模型]]

## 来源

- 官方论文：[官方论文](https://research.google/pubs/do-as-i-can-not-as-i-say-grounding-language-in-robotic-affordances/)
- 项目主页：[项目主页](https://say-can.github.io/)
- 官方代码：[GitHub](https://github.com/google-research/google-research/tree/master/saycan)
