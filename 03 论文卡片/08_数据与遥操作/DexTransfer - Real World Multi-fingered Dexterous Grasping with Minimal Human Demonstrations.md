---
paper_id: "P229"
title: "DexTransfer: Real World Multi-fingered Dexterous Grasping with Minimal Human Demonstrations"
aliases: ["DexTransfer", "以少量人类示范学习可迁移真实多指抓取"]
authors: ["Chen, Zoey Qiuyu", "Van Wyk, Karl", "Chao, Yu-Wei", "Yang, Wei", "Mousavian, Arsalan", "Gupta, Abhishek", "Fox, Dieter"]
year: 2022
venue: "arXiv preprint；未核实正式会议出处"
arxiv: "2209.14284"
version: "v1"
pdf: "01 论文文库/PDFs/08_数据与遥操作/DexTransfer.pdf"
document_type: "research_paper"
preprint_platform: "arXiv"
first_public_date: "2022-09-28"
first_public_month: "2022-09"
first_public_scope: "arXiv v1 UTC submission; cross-platform earliest release not established"
publication_status: "arXiv preprint；未核实正式会议出处"
affiliations: ["University of Washington", "NVIDIA", "Massachusetts Institute of Technology"]
metadata_verified_on: "2026-10-25"
metadata_sources: ["https://arxiv.org/abs/2209.14284", "https://sites.google.com/view/dextransfer/home", "https://arxiv.org/pdf/2209.14284v1"]
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Human_Demonstration", "Retargeting"]
---

# DexTransfer: Real World Multi-fingered Dexterous Grasping with Minimal Human Demonstrations

## 基本信息

- 稳定编号：P229
- 中文译名：以少量人类示范学习可迁移真实多指抓取
- 作者：Chen, Zoey Qiuyu；Van Wyk, Karl；Chao, Yu-Wei；Yang, Wei；Mousavian, Arsalan；Gupta, Abhishek；Fox, Dieter
- 研究机构：University of Washington；NVIDIA；Massachusetts Institute of Technology
- 年份：2022
- 首次公开：arXiv v1，2022-09-28（UTC；仅限定该平台，不声称全平台最早）
- 出处与版本：arXiv preprint；未核实正式会议出处；所读 v1，12 页
- 研究主题：物理轨迹修正、数据扩增、点云闭环与 Sim2Real
- 引用量：待核验
- 引用量来源：Google Scholar
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/DexTransfer.pdf|打开本地 PDF]]（已核对文件身份；仅本地保留，不承诺 GitHub 网页可访问）
- [官方论文页](https://arxiv.org/abs/2209.14284)｜[官方 PDF](https://arxiv.org/pdf/2209.14284v1)｜[官方项目](https://sites.google.com/view/dextransfer/home)
- 官方代码：未核实独立官方代码仓库，不用机构主页代替
- 数据：未核实独立完整数据集入口；代码中的示例和项目展示不等于完整数据发布

## 论文简介

DexTransfer 关注人手示范如何变成大量真正能抓住物体的机器人轨迹。人手和 Allegro 的结构不同，即使运动学重定向让姿态相似，回放时也可能抓不紧、滑落或碰撞。作者先把少量人类动作映射到机器人，再在仿真里用局部无梯度搜索修正，保留成功且对物理变化较稳健的轨迹，接着变换物体姿态并扩充接近段，最后训练点云闭环策略。这条路线强调先提高示范的物理可执行性，再扩大数据覆盖

关键细节是数据漏斗。只有少数成功接触轨迹时，机器人从新的初始位置出发，可能根本无法靠近训练轨迹。作者因此补充自由空间插值，让不同初始手姿逐渐进入已有可行轨迹，再完成抓取。这部分不是装饰性数据增强，消融显示去掉后新姿态表现很差。策略还使用最近几帧运动历史和掌心相对坐标，减少物体位置变化与部分可见性带来的影响

论文既有十七种物体的仿真实验，也有 KUKA 机械臂与 Allegro 的五物体真机实验。仿真中允许最多三次尝试，并报告累计成功；真机每物体二十五次测试。第一次成功率、三次以内累计成功率和真实机器人结果必须分开，不能用最好的仿真累计值代表真机。对我们而言，它适合研究少量演示经过物理筛选后如何增值，但没有提供把任何人类动作直接迁移到 DH116 的保证，也不解决所有物体和复杂工具任务

## A. 基本信息与研究问题

研究目标是以有限人类动作捕捉数据获得多样、动力学可行的多指抓取示范，并学习从部分点云观察预测动作的闭环策略。输入是 DexYCB 的人手与物体轨迹，输出是针对各物体训练的策略

真实平台为 KUKA LBR iiwa 7 R800 加十六驱动 Allegro，共二十三个执行关节。感知由三台 RGB-D 相机提供目标分割点云，不能将这种多视角条件写成单台 D435i 已验证

## B. 相关工作

直接重定向只处理几何对应，不保证动力学抓取成功；纯强化学习又可能需要大量探索。本文先用人类轨迹提供结构，再以仿真搜索修正和增广，最后用监督学习训练视觉策略，减少从零寻找抓法的难度

MimicGen 类方法会把成功片段适配到新的物体配置，DexTransfer 更聚焦多指抓取的轨迹修正、物理随机化和不同起点进入可行轨迹。与只使用最近示范回放相比，学习策略能够根据当前点云闭环调整，而不是把训练轨迹当开环命令

这种方法仍需要物体模型、仿真与可靠目标分割；数据量放大本身不是全部创新，成功轨迹的物理筛选与接近状态覆盖才决定训练数据是否有价值

## C. 核心贡献与方法

流程：人类动作捕捉 → 模板与物体姿态对齐 → 机器人运动重定向 → 局部轨迹搜索修正 → 物理随机化与对象中心扩增 → 数据漏斗 → 点云监督策略 → 真实机器人控制

先选择稳定物体姿态并对示范归一化，把人手运动变成机器人关节与掌心轨迹。然后对控制轨迹进行相关扰动搜索，在仿真中实际回放，依据抓取效果保留更合适的动作。它不是对所有坐标加噪声后都当成功数据，失败样本会影响筛选

物理随机化使轨迹在不同物体属性下检查稳健性，对象中心变换增加可用起始配置。数据漏斗在自由空间采多个初始手姿，插值到已有成功轨迹的接近位置，再执行接触段。它主要补充进入技能的可达状态，不是凭空生成新的复杂接触技能

视觉策略用 PointNet++ 编码目标点云，运动学编码器处理最近五帧手关节、关键点和对象相对信息，融合后分三个分支预测掌心平移、旋转和手指关节。坐标统一到掌心，降低全局位置变化影响。旋转损失在旋转空间衡量，不简单把角度当普通标量相减

真机末端目标通过 geometric fabrics 等底层控制转换为高频关节命令。网络的动作输出不直接替代机械臂控制器，实际还要处理碰撞、速度和机器人工作空间

## D. 实验与结果

Table I 从十七种 YCB 物体的 426 段右手演示出发，经归一化 1,621、修正 2,566、扩增 5,181 条轨迹。各阶段数量表示数据处理结果，不是人采集了五千多次；不同物体的有效扩增率不同

仿真每物体二十次测试，物体离桌十厘米为成功，最多允许三次尝试，成功即结束。Table II 平均首次为 0.61、第二次以内累计 0.70、第三次以内累计 0.74。三列是累计恢复尝试效果，不能当三次独立成功率或直接相乘

去掉物理随机化平均首次 0.33，去掉扩增 0.47，去掉数据漏斗 0.04；完整 0.61。它们支持各模块在该配置中的重要性，但不能把差值加起来计算总贡献。部分对象仍很难，例如 pitcher base 首次 0.25，说明平均值掩盖对象差异

真实 Figure 5 五物体每项二十五次，成功次数分别为 18、17、14、11、10，表现从 40% 到 72%。这是有限对象上的真机验证，明显不能用仿真三次累计 74% 代表。论文用分割点云与已训练每物体策略，并没有证明对任意新类别零样本抓取。统一人群采集人数、端到端总运行成本和 DH116 评测未报告

## E. 不足与未来

作者展示闭环策略掉落后的后续尝试可成功，但范围是抓取任务和限定尝试协议，不是任意长程失败诊断系统。物体感知、几何与物理模型仍需配置

本库分析：每物体策略限制了大规模通用使用，仿真筛选成功也会受摩擦和驱动模型误差影响。真实三相机观察优于单视角的条件不能忽略，遮挡与分割错误会把策略带离训练分布。项目页可访问，但本卡没有用不明来源仓库冒充已核实官方代码

对我们可先用 DH116 仿真做“几何可达—物理成功—随机化稳定—真机低速回放”的分层筛选，再扩增数据；普通夹爪可用于验证漏斗接近段。D435i 单相机需单独测遮挡和目标点云质量，不能照搬三视角性能。真实失败后回退、重新感知和重抓仍应以明确安全条件实现，不能只把三次尝试平均值当成熟恢复能力

## 相关工作与阅读入口

- [[03 论文卡片/08_数据与遥操作/DexMachina - Functional Retargeting for Bimanual Dexterous Manipulation|P225 · DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation]]
- [[03 论文卡片/08_数据与遥操作/DexMV - Imitation Learning for Dexterous Manipulation from Human Videos|P227 · DexMV: Imitation Learning for Dexterous Manipulation from Human Videos]]
- [[03 论文卡片/08_数据与遥操作/SPIDER - Scalable Physics-Informed Dexterous Retargeting|P209 · SPIDER: Scalable Physics-Informed Dexterous Retargeting]]

- 所属方向与专题导读：[[02 研究方向/数据与遥操作]]
- 遥操作路线：[[02 研究方向/机器人遥操作与动作重定向]]
- 数据质量路线：[[02 研究方向/机器人数据采集与数据质量]]

## 来源与核验边界

- 已阅读上述 12 页版本的正文、方法、实验与局限，含附录时一并核对；关键架构或实验表经页面渲染检查，数字位置见各节
- 日期依据官方 arXiv 提交历史，机构依据所读版本署名；正式出处与所读预印本版本分别标明，不用会议日程或演示获奖冒充正式出版
- 论文结果、作者限制和本库研究设想分开；未报告字段不补猜，未核实引用量不填 0
- 代码和数据链接用于核对公开资源，未运行第三方代码、未执行机器人动作；可访问与可完整复现分别评价
- PDF 再分发许可未统一确认，遵循现有忽略规则仅保存本地；代码许可不自动覆盖论文、数据及模型
