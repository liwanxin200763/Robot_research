---
paper_id: P179
title: "Grounding Sim-to-Real Generalization in Robotic Manipulation: An Empirical Study with Vision-Language-Action Models"
---

# P179 · Grounding Sim-to-Real Generalization in Robotic Manipulation: An Empirical Study with Vision-Language-Action Models

## 基本信息

- 作者：Ruixing Jin; Zicheng Zhu; Ruixiang Ouyang; Sheng Xu; Bo Yue; Zhizheng Wu; Guiliang Liu
- 年份：2026
- 发表 venue：arXiv 预印本；未核验到正式会议或期刊
- 论文类型：实证研究；Sim2Real 评测
- 研究方向：Sim2Real；VLA；Domain Randomization；真实机器人评测
- 论文链接：[arXiv 正式页面](https://arxiv.org/abs/2603.22876)
- DOI：[10.48550/arXiv.2603.22876](https://doi.org/10.48550/arXiv.2603.22876)（arXiv DOI，不代表会议发表）
- arXiv：[2603.22876v2](https://arxiv.org/abs/2603.22876)
- 项目主页：未核验到独立官方项目页
- 代码：论文称开放评测平台，但正文与 arXiv 页面未提供可核验的官方仓库链接；具体可用性待核验
- 本地 PDF：[[00_论文池/PDFs/05_仿真到真实_Sim2Real/Grounding_Sim-to-Real_Generalization.pdf|查看 PDF]]
- 引用量：
- 引用量来源：Google Scholar（待人工核验）

## 研究问题与相关工作

从仿真轨迹训练 VLA 可减少昂贵的真机示范，但相机视角、物体位置、光照和接触动力学的差异会让仿真成功率高估真机表现。已有方法常分别使用域随机化、逼真渲染或强化学习；这篇论文的不同之处是用同一组五任务与真机变化协议逐项比较这些因素，而非提出一个新的通用 VLA 架构。（全文 §1–2）

**Reality Gap（仿真与现实的差距）**指模拟的视觉、几何和接触规律与实际机器人不一致。**Domain Randomization（域随机化）**是在生成训练数据时改变这些条件，让策略学会覆盖更多可能的真实场景；它不保证每一种随机变化都有相同价值。

## 方法流程

RoboTwin 2.0 仿真构造五项操作任务 → 每项、每种训练条件采集 100 条仿真示范 → 对 OpenVLA-OFT 做监督微调 → 逐项改变背景、杂物、相机位姿、照明、桌面高度，以及渲染和物理精度 → 可选地用仿真 rollout 做 GRPO 风格强化学习微调 → 不用目标真机示范直接部署 → 对仿真分布外和真机多种条件计算任务成功率。（§3–4）

策略输入为单路 RealSense D435 RGB 画面与语言指令，输出连续关节目标及夹爪状态的短动作段。监督基线最小化动作 L1 误差；强化学习实验改为离散动作 token 头，因此 RL 与 SFT 数字也伴随动作头变化，不能完全解释为“只增加 RL”造成的收益。域随机化区分背景、桌面杂物、相机位置、光照、桌高，还比较每回合固定与每帧重新采样。（§3.1–3.2、§4.4）

## 数据、Baseline 与真机设置

- 仿真：RoboTwin 2.0；任务为按铃、放空杯、敲积木、叠碗、取双瓶。论文 §4.1 写仿真 Cobot Magic 本体，真机段写 Piper 机器人；两者对应关系和硬件细节应以公开平台资料进一步核对，不能默认完全同构。
- 真机：Piper 平台、单台 RealSense D435（640×480）；测背景、灯光、杂物、物体实例与位置变化。作者称累计超过 10,000 次真实试验，但各结果仍应按任务与条件分别看，不能把试验总数当成单一任务样本数。（§4.1、图 2）
- Baseline：干净仿真数据监督微调；单因素与多因素随机化；每回合与每帧随机化；低、中、高画面逼真度与极端物理参数；SFT、SFT+RL、SFT+RL+DR。（表 1–3、附录表 5–8）
- 零样本含义：没有使用目标真机示范训练策略。实验仍需真机相机布置与机器人控制接口，不能理解成完全无需部署适配。（§3.2、§4.1）

## 实验结果与消融

表 1 中，按铃真机成功率从干净训练的 **2.7%** 提升至“全部随机因素”的 **49.7%**；放空杯从 **5.4%→41.0%**，叠碗从 **26.2%→63.1%**。单因素里桌高和相机位姿通常比仅改背景、照明或杂物收益大；外观变化与空间变化叠加仍有帮助。敲积木即使全因素也仅 **11.5%**，双瓶 **23.8%**，说明“全部随机化”并未解决所有任务。（表 1）

表 2 中，把相机位姿从每回合随机改成每帧随机，按铃真机成功率 **23.5%→31.9%**、放空杯 **17.5%→25.6%**；背景每帧随机在放空杯上 **10.2%→23.1%**。这里是百分点差异，不能写成相对增长百分比。图 3 和附录表 7 显示画面从低逼真度升到中、高档一般有益，但高于中档的边际收益有限；把重力、摩擦和恢复系数改到极端值也会损伤迁移，物理真实性比较只覆盖这些设定。（§4.2–4.3）

表 3 的五任务平均真机成功率：SFT **5.6%**，SFT+RL **33.4%**，SFT+RL+DR **42.8%**；同时评估仿真 OOD。RL 比较用共同 SFT 初始化，但该组采用不同于前面连续回归实验的离散动作头，应分组解释。（§4.4、表 3）

## 失败、局限与后续

- 作者结果直接显示：接触或双物体任务仍显著困难；仿真 OOD 成绩不应替代真机成绩。（表 1、3）
- 库内分析：主要研究同一 OpenVLA-OFT 系列和五任务，不能直接外推至所有 VLA、本体或高自由度手指控制。物理对照采用故意极端参数，并非完整 System Identification（系统辨识：由真机轨迹估计实际动力学参数）。
- 对机械臂 + DH116：优先复用“相机位姿/桌高单因素→组合因素→真实扰动矩阵”的设计；记录抓取、接触、整任务三个不同终点；再另做指尖摩擦、关节回差、力反馈的迁移测试。论文没有验证 DH116 灵巧手，不可把其夹爪结论当成手指关节结论。

## 关联阅读

[[05_研究分类与路线图/Sim2Real 研究专题|Sim2Real 研究专题]] · [[02_论文/10_基准测试与数据集/RoboTwin 2.0 - A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation|RoboTwin 2.0]] · [[02_论文/06_扩散模型_流匹配_IL_RL/Sim2Real-VLA - Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation|Sim2Real-VLA]]
