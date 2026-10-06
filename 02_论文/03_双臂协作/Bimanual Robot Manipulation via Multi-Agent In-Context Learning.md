# Bimanual Robot Manipulation via Multi-Agent In-Context Learning

## 基本信息

- 作者：Alessio Palma、Indro Spinelli、Vignesh Prasad、Luca Scofano、Yufeng Jin、Georgia Chalvatzaki、Fabio Galasso
- 年份：2026
- 发表 venue：CoRL 2026
- 论文类型：方法论文
- 研究方向：双臂协作、多智能体操作
- 关键词：multi-agent、leader-follower、in-context learning、keypose
- 论文链接：https://arxiv.org/abs/2604.20348
- DOI：https://doi.org/10.48550/arXiv.2604.20348
- arXiv：2604.20348
- 项目主页：https://alesspalma.github.io/bicicle/
- 代码：https://github.com/alesspalma/icl_bimanual
- 本地 PDF：[[00_论文池/PDFs/03_双臂协作/BiCICLe.pdf|BiCICLe.pdf]]
- 引用量：1
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

双臂任务需要空间协调；把两臂动作一次性混在单一提示中难以清楚表达先后依赖。（第 1 节）

### 2. 论文要解决的问题

利用多智能体上下文学习，在少量演示条件下生成可协调执行的左右臂关键位姿。（第 1 节）

### 3. 之前方法存在的问题

单智能体提示容易忽略另一只手已经计划的路径；端到端监督策略通常需要特定任务数据。（第 2 节）

### 4. 核心思路

为左右臂建立 leader 与 follower 两个语言模型代理；先产生 leader 动作，再把它交给 follower 以生成互补动作。（第 3 节）

### 5. 方法与系统结构

场景物体三维中心和任务示范序列化为文本，两个代理按顺序输出离散 7D 末端关键位姿。follower 提示包含 leader 轨迹；执行一个关键位姿队列后重新观察和规划。两臂有显式角色与行动消息，但没有长期共享场景记忆或独立训练的 VLA expert。（第 3 节、图 2）

### 6. 输入信息

任务语言、示范、对象三维位置、当前双臂状态，以及 leader 已提出的动作。仿真对象分割使用真值，限制真实感知难度。（第 3–4 节）

### 7. 输出 / 动作表示

左右臂 7D 末端关键位姿按 leader→follower 顺序生成，再由控制器执行；不是两个代理在每个时刻同时生成连续动作。（第 3 节）

### 8. 数据来源与采集方式

TWIN 13 项双臂任务，每项测试提示含 10 条上下文示范；真机为两台 Franka 的三项任务。（第 4 节）

### 9. 数据处理与数据增强

将场景几何与示范压缩为文本，并将连续位姿离散化以适配语言模型；论文未报告独立数据增强收益。（第 3 节）

### 10. 训练方式

主要使用已有语言模型的 in-context learning，不训练新的端到端双臂 VLA；模型对提示格式和调用次数敏感。（第 3 节）

### 11. Benchmark 与实验设置

TWIN 13 任务，三轮各 100 episode；对照 RoboPrompt-DA 等提示方法。监督式 3DFA 也列出，但其训练协议不同。（第 4 节）

### 12. 真机实验

两台 Franka、三项任务，每任务 10 次测试；平均成功率 53.3%，RoboPrompt-DA 为 33.3%。未报告一臂失败后另一臂协助恢复。（第 4 节）

### 13. 主要实验结果

TWIN 平均成功率 70.5%，RoboPrompt-DA 为 64.4%；监督式 3DFA 为 85.1%，不能视为同数据设置下被 BiCICLe 超越。（第 4 节、主表）

### 14. 消融实验

去掉 leader 条件后 65.0%；对话式交互 57.5%；更昂贵的 best-of-N 为 71.2%。（第 4 节、消融表）

### 15. Failure Case

细小物体抓取受离散化和三维位置误差影响；串行 LLM 调用增加延迟，论文报告约 125.3 秒，对照约 43.3 秒。（第 4 节）

### 16. 主要局限

**环境动态类型：**静态随机化；两臂协调执行，未系统评测执行中独立移动目标。

真实场景次数少，仿真使用理想分割。按本库分析，消息只承载计划动作，不承载失败原因或历史效果；没有 debate、LLM-as-Judge、共享 Failure Memory 和真机失败恢复实验。

### 17. 与已有工作的关系

与 [[02_论文/03_双臂协作/TAO-DA - Towards Autonomous Operation—A Dual-Arm Vision-Language-Action Model for Coordinated Manipulation|TAO-DA]] 的单一 VLA 双塔专家不同，BiCICLe 是显式的双代理顺序计划架构。

### 18. 对当前研究方向的价值

可作双臂 Multi-Agent 架构基线：把一臂的计划作为另一臂的条件。若要接入 DH116 和失败互助，应另设计共享状态、失败证据传递和快速闭环控制；论文尚未验证这些功能。

### 19. 一句话总结

BiCICLe 以 leader–follower 双代理顺序生成关键位姿，在少样本双臂任务上优于同类提示基线，但没有共享失败记忆。
