---
paper_id: "P227"
title: "DexMV: Imitation Learning for Dexterous Manipulation from Human Videos"
aliases: ["DexMV", "从人类视频学习灵巧操作的示范转换平台"]
authors: ["Qin, Yuzhe", "Wu, Yueh-Hua", "Liu, Shaowei", "Jiang, Hanwen", "Yang, Ruihan", "Fu, Yang", "Wang, Xiaolong"]
year: 2021
venue: "ECCV 2022"
arxiv: "2108.05877"
version: "v5"
pdf: "01 论文文库/PDFs/08_数据与遥操作/DexMV.pdf"
document_type: "research_paper"
preprint_platform: "arXiv"
first_public_date: "2021-08-12"
first_public_month: "2021-08"
first_public_scope: "arXiv v1 UTC submission; cross-platform earliest release not established"
publication_status: "ECCV 2022"
affiliations: ["University of California San Diego"]
metadata_verified_on: "2026-10-25"
metadata_sources: ["https://arxiv.org/abs/2108.05877", "https://yzqin.github.io/dexmv/", "https://arxiv.org/pdf/2108.05877v5"]
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Human_Demonstration", "Retargeting"]
---

# DexMV: Imitation Learning for Dexterous Manipulation from Human Videos

## 基本信息

- 稳定编号：P227
- 中文译名：从人类视频学习灵巧操作的示范转换平台
- 作者：Qin, Yuzhe；Wu, Yueh-Hua；Liu, Shaowei；Jiang, Hanwen；Yang, Ruihan；Fu, Yang；Wang, Xiaolong
- 研究机构：University of California San Diego
- 年份：2021
- 首次公开：arXiv v1，2021-08-12（UTC；仅限定该平台，不声称全平台最早）
- 出处与版本：ECCV 2022；所读 v5，25 页
- 研究主题：手物姿态重建、任务空间向量、动作估计与模仿强化学习
- 引用量：待核验
- 引用量来源：Google Scholar
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/DexMV.pdf|打开本地 PDF]]（已核对文件身份；仅本地保留，不承诺 GitHub 网页可访问）
- [官方论文页](https://arxiv.org/abs/2108.05877)｜[官方 PDF](https://arxiv.org/pdf/2108.05877v5)｜[官方项目](https://yzqin.github.io/dexmv/)
- 官方代码：[对应 GitHub 仓库](https://github.com/yzqin/dexmv-sim)
- 数据：未核实独立完整数据集入口；代码中的示例和项目展示不等于完整数据发布

## 论文简介

DexMV 是理解“人类视频怎样变成机器人学习信号”的基础工作。视频里只有像素，机器人训练却需要状态、动作或奖励，直接把人的关节角抄给机器人也不成立。本文搭建真实人手与物体拍摄系统，以及对应的多指手仿真任务，先估计三维手物姿态，再做运动学重定向，必要时从平滑关节轨迹估算控制动作，最后让模仿学习与强化学习结合。真实人类示范与机器人任务之间存在一条明确的数据转换链，而不是由视频直接输出最终电机命令

重定向部分不仅匹配指尖到掌心的向量，还加入指骨关系，防止“指尖到了但手指弯曲不合理”。时间平滑和最小加加速度轨迹拟合则减少噪声，因为后续逆动力学需要求速度和加速度，原始抖动会被微分放大。作者比较需要状态动作的模仿方法与只需要状态的方法，说明缺失动作标签时可以采用不同学习路径，但二者在复杂接触和液体任务上的表现不一样

实验在仿真中评价搬移、倾倒和放入容器。一个重要阅读细节是，倾倒图中虽然有 success 一类字样，正文定义的是倒入容器的粒子比例；放入容器评价的是物体体积进入比例，也不都是整回合二元成功率。对我们而言，论文适合用来拆解 DH116 重定向的几何与平滑问题，但并未证明真实 DH116 的接触可行性，真实人类视频来源也不等于已经完成机器人真机迁移

## A. 基本信息与研究问题

研究问题是怎样从相机记录的人类操作中得到可辅助多指机器人学习的示范。平台同时包含拍摄、手物估计、机器人仿真与训练算法，使每一步误差都能通过后续学习效果检验

输入为人类操作视频和物体模型，输出为仿真机器人示范与策略。所读 arXiv v5 为 2022-07 修订，首次公开为 2021-08，两者都不能被直接写成同一个月份。论文主要验证的是仿真学习而非真实机械手部署

## B. 相关工作

直接遥操作能够给出机器人动作，但多指控制设备昂贵、学习成本高。仅根据视频做行为克隆又缺少真实机器人控制信号。早期指尖重定向保留了指端位置，却可能丢失中间指骨姿态，让机器人手穿入物体或进入不良姿态

本文增加任务空间向量与时序一致性，再比较 GAIL、DAPG 和 SOIL。GAIL 匹配示范与策略的状态动作分布，DAPG 把示范辅助加入策略梯度，SOIL 可以利用只有状态的示范并学习逆动力学补充动作。它们仍利用任务奖励与仿真交互，不是纯离线监督训练

与后来物体功能驱动的 DexMachina 相比，本作是早期完整转换与评测平台；它揭示姿态估计、动作恢复和任务学习相互影响，但没有消除仿真物理与真实接触差距

## C. 核心贡献与方法

流程：多视角人类视频 → 三维手与物体姿态 → 平滑与机器人手重定向 → 连续关节轨迹 → 动作估计和时间对齐 → 示范辅助强化学习

手物估计先恢复人的形状、姿态与物体位姿，使相机像素落入三维空间。重定向用机器人正向运动学计算任务空间向量，与人手对应向量匹配；加入掌心到指骨等信息，避免只约束指尖而无法确定手指弯曲。每帧以上一帧优化结果初始化，并惩罚相邻关节变化，提升时间连续性

若算法需要动作，不能把关节角直接当力矩。作者先把离散角度拟合为连续 q(t)，通过一阶、二阶导数得到速度、加速度，再使用逆动力学得到控制力矩。最小 jerk 约束限制三阶导数，减少不自然突变和微分噪声。这里得到的是模型下的估算动作，不是真实人类对物体施力的传感测量

拍摄约三十赫兹、仿真一百二十赫兹，通过连续轨迹重采样对齐，避免机械重复帧造成控制速度不一致。之后根据学习器选择使用状态动作或只有状态的示范，并与任务奖励结合学习闭环行为

可执行性来自机器人运动学、仿真动力学和后续策略优化共同作用。几何匹配成功不代表整段动作物理成功，物体姿态误差、摩擦与接触模型都可能影响标签

## D. 实验与结果

Table 1 搬移五种物体，每设置一百次测试、三个随机种子，成功定义为二百步后物体到目标距离小于 0.1 仿真长度单位。DAPG 在芥末瓶为 0.93±0.05，纯 RL 为 0.06±0.01；但糖盒上 DAPG 为零、SOIL 为 0.67±0.47，说明不同方法并非所有物体一致最优

Table 2 在番茄罐搬移八百次训练迭代处，一百条示范 SOIL 为 1.00±0.00，五十条为 0.59±0.39，十条为 0.36±0.21，纯 RL 为 0.13±0.19。它是固定迭代下的数据规模对照，不能声称达到一百次示范后所有任务必定满分

Table 3 的手部平均关节点位置误差从单相机 41.7 降为双相机加后处理 32.5，学习成功率也总体改善。姿态误差在 DexYCB 有真值数据上测量，策略性能在操作任务测量，两者不是同一数据集直接逐帧对应的因果证据

Figure 7 倾倒正文将结果解释为粒子倒入比例，DAPG 为 27.2±18.4%，纯 RL 为 1.3±0.7%；Place Inside 的 Inside Score 为物体进入杯子体积比例，DAPG 31.3±30.0，不能把两者都写成整任务成功率。论文没有给出相应真实机器人成功次数、全体采集人数和面向 DH116 的实验，卡片明确保留这些空缺

## E. 不足与未来

姿态重建误差会传到动作估计，特别是在微分过程中放大。作者的消融显示时间平滑重要，但平滑太强也可能去掉快速接触事件。物体模型和仿真任务仍需人工配置

本库分析：逆动力学求得的力矩依赖机器人惯性和接触模型，不能直接发给不同驱动器；关节位置控制和力矩控制也应分开。论文的物理变化实验增强了对模型差距的认识，并不替代真机 Sim2Real 证明。未展示独立部署失败恢复系统

对我们的设想是先在 DH116 仿真模型上复查指尖和指骨向量、被动耦合与连续轨迹，再用低速位置控制测试。D435i 的深度可帮助手物几何，但遮挡和手套估计仍需选型。建议先比较重定向误差与真实接触成功，避免把几何平均误差低当作灵巧操作已经解决

## 相关工作与阅读入口

- [[03 论文卡片/08_数据与遥操作/Hand-Object Interaction Pretraining from Videos|P237 · Hand-Object Interaction Pretraining from Videos]]
- [[03 论文卡片/08_数据与遥操作/DexTransfer - Real World Multi-fingered Dexterous Grasping with Minimal Human Demonstrations|P229 · DexTransfer: Real World Multi-fingered Dexterous Grasping with Minimal Human Demonstrations]]
- [[03 论文卡片/04_灵巧操作/Hand2Robot - Object-Centric 4D Hand Reconstruction from Human Demonstrations for Robotics|P184 · Hand2Robot: Object-Centric 4D Hand Reconstruction from Human Demonstrations for Robotics]]

- 所属方向与专题导读：[[02 研究方向/数据与遥操作]]
- 遥操作路线：[[01 论文文库/专题阅读/机器人遥操作与动作重定向]]
- 数据质量路线：[[01 论文文库/专题阅读/机器人数据采集与数据质量]]

## 来源与核验边界

- 已阅读上述 25 页版本的正文、方法、实验与局限，含附录时一并核对；关键架构或实验表经页面渲染检查，数字位置见各节
- 日期依据官方 arXiv 提交历史，机构依据所读版本署名；正式出处与所读预印本版本分别标明，不用会议日程或演示获奖冒充正式出版
- 论文结果、作者限制和本库研究设想分开；未报告字段不补猜，未核实引用量不填 0
- 代码和数据链接用于核对公开资源，未运行第三方代码、未执行机器人动作；可访问与可完整复现分别评价
- PDF 再分发许可未统一确认，遵循现有忽略规则仅保存本地；代码许可不自动覆盖论文、数据及模型
