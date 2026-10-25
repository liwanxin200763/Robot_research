---
paper_id: "P230"
title: "DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning"
aliases: ["DemoGen", "面向数据高效视觉运动学习的合成示范生成"]
authors: ["Xue, Zhengrong", "Deng, Shuying", "Chen, Zhenyang", "Wang, Yixuan", "Yuan, Zhecheng", "Xu, Huazhe"]
year: 2025
venue: "RSS 2025"
arxiv: "2502.16932"
version: "v1"
pdf: "01 论文文库/PDFs/08_数据与遥操作/DemoGen.pdf"
document_type: "research_paper"
preprint_platform: "arXiv"
first_public_date: "2025-02-24"
first_public_month: "2025-02"
first_public_scope: "arXiv v1 UTC submission; cross-platform earliest release not established"
publication_status: "RSS 2025"
affiliations: ["Tsinghua University", "Shanghai Qi Zhi Institute", "Shanghai Artificial Intelligence Laboratory"]
metadata_verified_on: "2026-10-25"
metadata_sources: ["https://arxiv.org/abs/2502.16932", "https://demo-generation.github.io/", "https://arxiv.org/pdf/2502.16932v1"]
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Human_Demonstration", "Retargeting", "Synthetic_Data"]
---

# DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning

## 基本信息

- 稳定编号：P230
- 中文译名：面向数据高效视觉运动学习的合成示范生成
- 作者：Xue, Zhengrong；Deng, Shuying；Chen, Zhenyang；Wang, Yixuan；Yuan, Zhecheng；Xu, Huazhe
- 研究机构：Tsinghua University；Shanghai Qi Zhi Institute；Shanghai Artificial Intelligence Laboratory
- 年份：2025
- 首次公开：arXiv v1，2025-02-24（UTC；仅限定该平台，不声称全平台最早）
- 出处与版本：RSS 2025；所读 v1，18 页
- 研究主题：少示范扩增、物体中心轨迹变换、点云编辑
- 引用量：待核验
- 引用量来源：Google Scholar
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/DemoGen.pdf|打开本地 PDF]]（已核对文件身份；仅本地保留，不承诺 GitHub 网页可访问）
- [官方论文页](https://arxiv.org/abs/2502.16932)｜[官方 PDF](https://arxiv.org/pdf/2502.16932v1)｜[官方项目](https://demo-generation.github.io/)
- 官方代码：[对应 GitHub 仓库](https://github.com/TEA-Lab/DemoGen)
- 数据：未核实独立完整数据集入口；代码中的示例和项目展示不等于完整数据发布

## 论文简介

DemoGen 要减少一种很重复的采集劳动：同一个抓取或插放任务，仅仅因为物体换了位置，就要让人重新演示许多次。作者从一条或少量真实示范出发，同时变换机器人动作和视觉观察，生成覆盖更大工作空间的训练数据。它关注的是空间分布扩展，不是通过语言凭空创造任意任务，也不是让机器人把每条新轨迹实际执行一遍再保存

方法把一条示范拆为自由移动和接触技能。自由移动连接不同阶段，接触技能相对于目标物体表达；物体挪动时，相应技能也一起移动。观察使用三维点云，通过分割和几何变换重排物体与机器人局部点云，使合成观察与合成动作对应。随后使用三维扩散策略训练视觉到动作的映射。这样可以避免为生成每条观察搭建完整物理仿真，但也继承了遮挡、物体分割和视角不一致的问题

论文不仅比较成功率，也分析训练覆盖范围和合成量的关系。合成数据增多后，性能会饱和，因为单视角看不到的新表面无法靠平移点云补出来。作者还展示扰动恢复和障碍物扩增，但它们依赖特定变换设计与任务设置，不能推广为任意接触失败都能自动修复。对我们的直接价值是先用普通夹爪和深度相机验证“覆盖更多物体位置是否比重复同一位置更有效”，再考虑 DH116 手指接触和双臂协调的复杂扩展

## A. 基本信息与研究问题

研究问题是能否用一条质量可靠的示范，产生可训练闭环策略的空间扩增数据。输入不是纯视频，而是同步的点云观察、机器人状态、动作以及目标物体分割与任务阶段信息，输出是新的观察—动作序列

对象位置变化后，原来示范中的接触技能往往可以在物体坐标系复用；困难在于连接这些技能，并生成与新动作一致的观察。作者以此为核心设计生成器，而不是只随机改动作标签或只增强图像。论文主要解决已有任务的空间泛化，不宣称不需要任何示范、任何人工任务配置

## B. 相关工作

直接模仿学习用相机和机器人动作配对训练，演示覆盖不足时，物体移动到新位置就容易失效。常规图像增强可改变颜色与裁剪，却不能自动给出“物体真的移到另一处以后手应该如何移动”的新标签

MimicGen 在仿真中把对象中心的技能片段重新组合，通过执行验证得到新轨迹。DemoGen 保留片段变换思想，但把观察空间设为三维点云，以几何编辑取代每次完整物理重放。这样能使用真实示范的视觉结构，代价是对真实执行结果和新遮挡缺少物理验证

DP3 是把点云编码后用扩散模型逐步去噪生成动作块的策略。它是消费数据的学习器，DemoGen 是生产数据的生成器，二者不能当成同一层面的替代方法。合成数据表现优于少量人工数据，仍需要排查是否只是覆盖位置更多，而非每条示范本身更优

## C. 核心贡献与方法

流程：记录源示范 → 分割物体与技能 → 采样物体新位置 → 变换接触技能 → 规划自由移动连接 → 编辑对应点云 → 训练并部署闭环策略

点云先裁剪任务空间、分割相关物体，并通过采样控制输入点数。论文使用 Grounded-SAM 得到初始物体掩码，再依任务关系安排阶段。末端与物体的距离可帮助识别技能边界，但不是所有任务都能用同一个阈值自动理解

技能段记录相对于目标物体的运动。给定物体变换 T，新技能的末端位姿也乘同一几何变换，夹爪或手部命令保留；这样延续接触附近的相对几何。自由空间阶段则连接相邻技能的新起终点，可在简单场景插值，也可针对障碍用运动规划，避免把整条轨迹生硬平移导致连接断裂

观察生成区分尚未操作、正在操作和操作完成的物体。物体点云按相应变换更新，机器人相关局部观察与末端一起变换，最终组成新场景。状态使用实际记录状态进行变换，不把控制目标假装成真实测量。绝对末端目标经逆运动学转换给机器人，手部命令仍依具体执行器接口

几何变换不模拟摩擦、质量与碰撞后的物体响应。方法假设技能可按变换执行，生成时没有在真实机器人上验证每条轨迹。因此需要训练后的真机测试作为证据，尤其应检查精密插入、柔性物体与灵巧手接触

扰动恢复扩增在物体或末端轨迹上加入异步变化，让策略看到偏离原轨迹后的纠正观察；障碍扩增则生成绕障连接。它们是训练样本的构造方式，不是部署时一个独立、通用的故障诊断与恢复模块

## D. 实验与结果

Table I 在八个修改后的 MetaWorld 任务上比较，每个设置三个随机种子。单条源示范策略的任务平均峰值/均值为 16%/13%，DemoGen 为 91%/88%，十条源示范为 70%/68%，二十五条为 94%/91%。峰值与均值是不同汇总口径，不能只挑峰值再与另一行均值比较

真实实验共八任务、530 次评估，覆盖 Franka 配普通夹爪、Franka 配 Allegro 与 Galaxea R1 双臂，观察使用单视角 L515。七个单臂任务加一个双臂任务，并非每种平台都测试八任务。Table II 合成量依任务为 270、432、432、270、324、243、243、72 条，不是统一上千条

生成速度示例为 22 秒产生 2,214 条、约 14.7 万观察—动作对，仅衡量数据生成，不含源示范、标注、训练、视频渲染或真机评估。官方代码还说明视频渲染可明显增加耗时，所以不能把生成吞吐当端到端实验完成速度

工作空间覆盖分析在精密插入任务中比较不同采样区域，体现合成位置覆盖的重要性。继续增加数量出现饱和，原因之一是原始单视角点云无法提供新视角的完整表面。扰动与障碍实验支持特定条件下的鲁棒性；涂酱任务的覆盖分数是 0 到 100 的任务评分，不能一律当整任务成功率

论文没有统一报告所有任务的采集人数、全流程人时、功耗或实时推理延迟，不补猜测值。复现示例数据位于官方代码 source 目录，不能把项目模板里无关数据集链接当成本论文完整数据发布

## E. 不足与未来

作者明确分析视觉不一致、单条示范覆盖与性能饱和。当前结果说明空间扩增能降低重复示范成本，不证明新物体几何、复杂接触模式和新手型都可直接迁移

我的理解是先把生成质量拆成三项：新动作在运动学上可达、观察与标签对应、策略在真实执行时成功。只验证文件格式与轨迹连续不能替代后两项。DH116 的耦合关节和多指接触会让保留原手指命令的假设更脆弱，应先从普通夹爪刚体任务开始

现有机械臂与 D435i 可用于记录 RGB-D、实际关节、末端和夹爪命令，固定相机标定并保留原始时间戳。建议比较同样训练步数下，一条源示范、同量重复示范和空间扩增，而不是只比较数据条数。向灵巧手扩展时增加接触检测、碰撞过滤和指尖相对物体误差；向失败恢复扩展时另建失败类型、恢复动作与终止条件，不能仅依据一次扰动成功就宣称通用恢复

## 相关工作与阅读入口

- [[03 论文卡片/08_数据与遥操作/CyberDemo - Augmenting Simulated Human Demonstration for Real-World Dexterous Manipulation|P231 · CyberDemo: Augmenting Simulated Human Demonstration for Real-World Dexterous Manipulation]]
- [[03 论文卡片/08_数据与遥操作/GenSim2 - Scaling Robot Data Generation with Multi-modal and Reasoning LLMs|P234 · GenSim2: Scaling Robot Data Generation with Multi-modal and Reasoning LLMs]]
- [[03 论文卡片/08_数据与遥操作/MimicGen - A Data Generation System for Scalable Robot Learning using Human Demonstrations|P202 · MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations]]

- 所属方向与专题导读：[[02 研究方向/数据与遥操作]]
- 遥操作路线：[[02 研究方向/机器人遥操作与动作重定向]]
- 数据质量路线：[[02 研究方向/机器人数据采集与数据质量]]

## 来源与核验边界

- 已阅读上述 18 页版本的正文、方法、实验与局限，含附录时一并核对；关键架构或实验表经页面渲染检查，数字位置见各节
- 日期依据官方 arXiv 提交历史，机构依据所读版本署名；正式出处与所读预印本版本分别标明，不用会议日程或演示获奖冒充正式出版
- 论文结果、作者限制和本库研究设想分开；未报告字段不补猜，未核实引用量不填 0
- 代码和数据链接用于核对公开资源，未运行第三方代码、未执行机器人动作；可访问与可完整复现分别评价
- PDF 再分发许可未统一确认，遵循现有忽略规则仅保存本地；代码许可不自动覆盖论文、数据及模型
