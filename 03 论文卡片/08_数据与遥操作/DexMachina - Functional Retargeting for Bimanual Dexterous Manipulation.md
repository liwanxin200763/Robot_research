---
paper_id: "P225"
title: "DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation"
aliases: ["DexMachina", "面向双手灵巧操作的功能性动作重定向"]
authors: ["Mandi, Zhao", "Hou, Yifan", "Fox, Dieter", "Narang, Yashraj", "Mandlekar, Ajay", "Song, Shuran"]
year: 2025
venue: "ICML 2026"
arxiv: "2505.24853"
version: "ICML 2026 final"
pdf: "01 论文文库/PDFs/08_数据与遥操作/DexMachina.pdf"
document_type: "research_paper"
preprint_platform: "arXiv"
first_public_date: "2025-05-30"
first_public_month: "2025-05"
first_public_scope: "arXiv v1 UTC submission; cross-platform earliest release not established"
publication_status: "ICML 2026"
affiliations: ["Stanford University", "NVIDIA"]
metadata_verified_on: "2026-10-25"
metadata_sources: ["https://arxiv.org/abs/2505.24853", "https://proceedings.mlr.press/v306/mandi26a.html", "https://raw.githubusercontent.com/mlresearch/v306/main/assets/mandi26a/mandi26a.pdf"]
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Human_Demonstration", "Retargeting"]
---

# DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation

## 基本信息

- 稳定编号：P225
- 中文译名：面向双手灵巧操作的功能性动作重定向
- 作者：Mandi, Zhao；Hou, Yifan；Fox, Dieter；Narang, Yashraj；Mandlekar, Ajay；Song, Shuran
- 研究机构：Stanford University；NVIDIA
- 年份：2025
- 首次公开：arXiv v1，2025-05-30（UTC；仅限定该平台，不声称全平台最早）
- 出处与版本：ICML 2026；所读 ICML 2026 final，16 页
- 研究主题：物体轨迹跟踪、接触奖励、仿真课程学习
- 引用量：待核验
- 引用量来源：Google Scholar
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/DexMachina.pdf|打开本地 PDF]]（已核对文件身份；仅本地保留，不承诺 GitHub 网页可访问）
- [官方论文页](https://arxiv.org/abs/2505.24853)｜[官方 PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/mandi26a/mandi26a.pdf)｜[官方项目](https://project-dexmachina.github.io/)
- [正式发表来源](https://proceedings.mlr.press/v306/mandi26a.html)
- 官方代码：[对应 GitHub 仓库](https://github.com/MandiZhao/dexmachina)
- 数据：未核实独立完整数据集入口；代码中的示例和项目展示不等于完整数据发布

## 论文简介

DexMachina 将“动作像不像人”与“是否真正完成了物体操作”分开。两种手即使指尖轨迹相近，也可能因为手指长度、关节耦合和接触位置不同，无法以同样方式打开盒盖。因此论文定义功能性重定向：给定一次密集追踪的人类双手与物体示范，学习机器人策略，让物体的位置、旋转和铰链角度跟随目标轨迹。手的运动是指导，物体完成预期变化才是主要目标

难点是长程接触任务的探索。机器人刚抬起物体就可能因换手或开盖而掉落，导致后半段根本没有学习机会。作者引入虚拟物体控制器，早期由虚拟弹簧阻尼帮物体沿示范移动，机器人先学习保持合适姿态和接触；随着表现稳定，辅助强度逐渐下降，最终由机器人手自己完成操作。该辅助仅存在于仿真训练，不是实际机器人上的隐藏外力，也不能把辅助尚未移除时的表现当作部署成功

本卡以 ICML 2026 正式版为主，该版实验与评价说明比早期预印本更完整。它采用不同灵巧手和铰接物体进行系统比较，但没有真实机器人部署验证。更要注意，正式版部分图称成功率，附录实际使用物体部件平均距离的曲线面积指标，不能解读成二十次实验成功了多少次。对 DH116 的启发是根据功能、接触和可驱动结构设计目标，而不是强迫它模仿人手全部关节；真正上机还需要感知、模型误差和安全控制研究

## A. 基本信息与研究问题

输入是 ARCTIC 的密集双手、物体部件与关节轨迹，输出是针对物体与手本体训练的双手强化学习策略。本文不是直接从未处理的单目视频输出机器人动作，也不是一个通用跨任务视觉策略

正式出版为 ICML 2026，PMLR 306:86198–86213，会议月份为 2026-07；首次 arXiv 公开为 2025-05。这两个日期分别描述公开和正式出版来源，不能将 2025 预印本写作 ICML 2025

## B. 相关工作

运动学重定向优化关节角，使机器人指尖或手部关键点接近人的几何状态，速度快但不保证物体被稳定操纵。基于对象跟踪的强化学习把物体目标加入奖励，原则上允许机器人使用不同于人的抓法，却面临稀疏探索和长程掉落

ObjDex 等方法提供对象目标和动作指导，ManipTrans 通过物理与误差阈值课程调整训练难度。DexMachina 选择对物体本身施加逐渐衰减的虚拟辅助，让机器人先经历完整过程，再逐步承担物理工作。本文在统一 Genesis 环境中重实现相关基线，不能把重实现结果视为原作者原环境的逐字复制

接触奖励也不等于测得真实接触力。它从人手与物体网格的距离近似接触位置，帮助保留交互策略，但近距离不一定已经产生物理接触，这一代理监督仍有误差

## C. 核心贡献与方法

流程：人类手物密集轨迹 → 碰撞感知运动学初始化 → 近似接触标签 → 对象跟踪与辅助奖励 → 带虚拟物体控制器的 PPO → 根据进度衰减辅助 → 无辅助策略评估

首先把人手关键点映射为机器人关节，再在固定物体的仿真中以软控制目标回放，获取更合理的手部关节与连杆位置。对象轨迹含刚体位置、旋转和一维铰接角；目标奖励综合这三者，避免只移动物体中心却忽略开盖状态

接触近似在物体部件与 MANO 人手网格间查找距离小于一厘米的顶点，最多采样五十个，再将接触位置分配给机器人最近连杆，得到位置张量和有效性掩码。掩码用于区分没有接触和接触位置不同，避免把所有空值都当真实接触点

动作采用混合表达：手腕在参考运动上预测残差，手指直接输出按关节限位归一化的目标。奖励包含对象跟踪、关键点运动、关节模仿和接触匹配。对象任务权重更重要，因此策略可以偏离人手外观，以完成真实物体运动

虚拟物体控制器给对象根部六个虚拟关节及铰接关节施加 PD 辅助，早期增益高。课程维护历史任务与辅助奖励，只有各项达到阈值才衰减控制器，增益很小时置零。这样减少早期掉落让后续状态无法访问的问题。PPO 是通过仿真交互优化策略的强化学习算法，不是读取一条示范就无训练执行

评估时必须确认辅助已经为零，并检查对象目标不是由外力暗中完成。未来真实部署也不能依赖仿真中的对象状态、接触力和精确目标等特权信息

## D. 实验与结果

正式版包含五个铰接物体、七段示范，资产库整理六类手，核心比较使用 Inspire、Allegro、Xhand 和 Schunk 四类代表。任务包含抬起、空中翻转、开合盖等多阶段动作，不能将七段示范当七千条任务数据

附录 C.1 说明常规使用一万二千个并行环境，Dex Hand 因显存为一万个；单次训练占一张 L40s 或 H100。主要设置五个随机种子，动作消融为三个。每种子选取按任务奖励保存的最优检查点，再评估二十个回合，存在检查点选择流程，不能解释为完全独立从未选择的模型

关键指标见 C.4：分别计算各物体部件的 ADD，即预测与目标状态下对应表面点的平均距离，先在部件间平均，再计算误差阈值曲线下面积 AUC。它是跟踪质量汇总指标，不是整回合二元成功率。Figure 3 强化长程复杂任务中课程相对只有奖励的优势，但本卡不从柱图估读未经精确报告的百分比

消融包括无课程、仅任务奖励、运动学直接回放、动作表达和奖励权重。没有课程时即便奖励相同，长程操作也可能失败，支持“能否经历后半段”对学习的重要性。论文没有真实机器人、RGB-D 感知、遥操作人数或真实相机实验，不能将仿真数据与真机指标混用

## E. 不足与未来

作者强调平台可比较手部结构与能力，但仍依赖对象与示范的高质量模型。当前基准面向一维铰接对象，不能据此认为可覆盖软物体、液体和任意工具操作

本库分析：近似接触监督有噪声，仿真摩擦与耦合建模会影响结果。不同手的功能比较应保持控制预算、物体比例和观察条件可比；更多关节不天然代表更强。课程训练中的辅助消退是训练机制，不是机器人部署遇到失败后的恢复

对 DH116，我们可先建立准确模型和可驱动关节映射，测试对象功能目标是否比人手角度匹配更有效。D435i 仅能提供部分几何观察，不能直接测得仿真特权对象状态与接触力，需要状态估计或视觉策略蒸馏。建议先做仿真可执行性、无辅助验证与模型参数扰动，再考虑低风险真机迁移。这是后续研究路线，本文没有提供已验证的 DH116 真机策略

## 相关工作与阅读入口

- [[03 论文卡片/08_数据与遥操作/DexTransfer - Real World Multi-fingered Dexterous Grasping with Minimal Human Demonstrations|P229 · DexTransfer: Real World Multi-fingered Dexterous Grasping with Minimal Human Demonstrations]]
- [[03 论文卡片/08_数据与遥操作/SPIDER - Scalable Physics-Informed Dexterous Retargeting|P209 · SPIDER: Scalable Physics-Informed Dexterous Retargeting]]
- [[03 论文卡片/08_数据与遥操作/DexMimicGen - Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning|P145 · DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning]]

- 所属方向与专题导读：[[02 研究方向/数据与遥操作]]
- 遥操作路线：[[01 论文文库/专题阅读/机器人遥操作与动作重定向]]
- 数据质量路线：[[01 论文文库/专题阅读/机器人数据采集与数据质量]]

## 来源与核验边界

- 已阅读上述 16 页版本的正文、方法、实验与局限，含附录时一并核对；关键架构或实验表经页面渲染检查，数字位置见各节
- 日期依据官方 arXiv 提交历史，机构依据所读版本署名；正式出处与所读预印本版本分别标明，不用会议日程或演示获奖冒充正式出版
- 论文结果、作者限制和本库研究设想分开；未报告字段不补猜，未核实引用量不填 0
- 代码和数据链接用于核对公开资源，未运行第三方代码、未执行机器人动作；可访问与可完整复现分别评价
- PDF 再分发许可未统一确认，遵循现有忽略规则仅保存本地；代码许可不自动覆盖论文、数据及模型
