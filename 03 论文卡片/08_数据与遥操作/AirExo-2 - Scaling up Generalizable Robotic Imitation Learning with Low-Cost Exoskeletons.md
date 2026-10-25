---
paper_id: "P220"
title: "AirExo-2: Scaling up Generalizable Robotic Imitation Learning with Low-Cost Exoskeletons"
aliases: ["AirExo2", "利用低成本外骨骼扩展可泛化机器人模仿学习"]
authors: ["Fang, Hongjie", "Wang, Chenxi", "Wang, Yiming", "Chen, Jingjing", "Xia, Shangning", "Lv, Jun", "He, Zihao", "Yi, Xiyan", "Guo, Yunhan", "Zhan, Xinyu", "Yang, Lixin", "Wang, Weiming", "Lu, Cewu", "Fang, Hao-Shu"]
year: 2025
venue: "CoRL 2025"
arxiv: "2503.03081"
version: "v3"
pdf: "01 论文文库/PDFs/08_数据与遥操作/AirExo2.pdf"
document_type: "research_paper"
preprint_platform: "arXiv"
first_public_date: "2025-03-05"
first_public_month: "2025-03"
first_public_scope: "arXiv v1 UTC submission; cross-platform earliest release not established"
publication_status: "CoRL 2025"
affiliations: ["Shanghai Jiao Tong University", "Noematrix", "Shanghai Innovation Institute"]
metadata_verified_on: "2026-10-25"
metadata_sources: ["https://arxiv.org/abs/2503.03081", "https://airexo.tech/airexo2", "https://arxiv.org/pdf/2503.03081v3"]
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Human_Demonstration", "Retargeting"]
---

# AirExo-2: Scaling up Generalizable Robotic Imitation Learning with Low-Cost Exoskeletons

## 基本信息

- 稳定编号：P220
- 中文译名：利用低成本外骨骼扩展可泛化机器人模仿学习
- 作者：Fang, Hongjie；Wang, Chenxi；Wang, Yiming；Chen, Jingjing；Xia, Shangning；Lv, Jun；He, Zihao；Yi, Xiyan；Guo, Yunhan；Zhan, Xinyu；Yang, Lixin；Wang, Weiming；Lu, Cewu；Fang, Hao-Shu
- 研究机构：Shanghai Jiao Tong University；Noematrix；Shanghai Innovation Institute
- 年份：2025
- 首次公开：arXiv v1，2025-03-05（UTC；仅限定该平台，不声称全平台最早）
- 出处与版本：CoRL 2025；所读 v3，23 页
- 研究主题：伪机器人示范、二维三维融合、无机器人示范迁移
- 引用量：待核验
- 引用量来源：Google Scholar
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/AirExo2.pdf|打开本地 PDF]]（已核对文件身份；仅本地保留，不承诺 GitHub 网页可访问）
- [官方论文页](https://arxiv.org/abs/2503.03081)｜[官方 PDF](https://arxiv.org/pdf/2503.03081v3)｜[官方项目](https://airexo.tech/airexo2)
- 官方代码：[对应 GitHub 仓库](https://github.com/AirExo/AirExo-2)
- 数据：[官方数据入口](https://drive.google.com/drive/folders/1xfJgn1qVLBgNhaFq7sbE6C6ylM6zZS9p)（下载内容、许可与访问权限以页面说明为准）

## 论文简介

AirExo-2 面向的问题是：能否让人在没有机器人的环境里收集示范，再直接训练出能在机器人上执行的策略。前作 AirExo 已经能通过关节编码器记录与机器人对应的动作，但观察画面仍有外骨骼和人手，部署时却变成机械臂。后作不再只靠少量机器人示范微调来弥补这个差异，而是把原始示范改造成伪机器人示范：擦除人和外骨骼，补出背景，再渲染相同姿态的机器人，同时修复深度并将动作统一到相机坐标系

改图并不自动保证可学习。为了利用仍有域差异的伪示范，作者提出 RISE-2，将三维点云提供的几何位置与预训练二维视觉模型提供的语义特征对齐，再用扩散动作头预测未来动作。这样既能知道物体在哪里，也能利用图像模型区分物体与背景。它仍然需要准确的机构模型、关节校准、相机标定和可执行的示范动作，并非任意视频都能自动转换

实验把策略能力和数据采集系统分开检验：一组使用真实遥操作数据比较策略，另一组比较不同示范来源及适配方法，还测量采集效率与轨迹误差。论文中的零样本部署，是指策略没有用目标机器人的遥操作示范训练后上机，不是没有训练数据或没有设备校准。对我们的价值是提供一条“先保证动作可信，再改造观察域，再验证闭环策略”的完整路线；它不证明普通相机和 DH116 可以原样复现，需要分别检查手部结构、深度质量和接触能力

## A. 基本信息与研究问题

本作将采集扩展性拆为两个差距：运动学差距是演示动作与机器人可执行动作不一致，视觉差距是训练时看到人和外骨骼、测试时看到机器人。升级外骨骼采用一比一同构尺寸、铝型材和移动底座，双臂机构约六百美元，不含相机

论文同时提出数据系统 AirExo-2 与策略 RISE-2。二者作用不同：前者产生可用示范，后者学习如何将图像、点云映射为动作。不能将 RISE-2 在真实示范上的优势直接视为伪示范生成器的净贡献

## B. 相关工作

UMI 用手持夹爪及一致的腕部视角减小人与机器人观察差异，便于采集，但全臂和全局场景覆盖受视角限制。原 AirExo 用同构关节记录动作，再进行野外数据预训练与机器人数据微调；它没有显式把画面变成机器人域

本文选择另一条路线：利用已知关节角和机器人描述文件渲染出机器人，用视频修复模型补背景，力求同时保持动作对应与观察一致。与通用视频生成不同，机器人形状和位置受运动学约束；与纯三维策略相比，RISE-2 又增加二维基础模型的语义信息。二维语义有利于区分物体，三维几何有利于减少相机视角变化的影响，两者必须在空间上正确对应

## C. 核心贡献与方法

流程：编码器和 RGB-D 示范 → 关节与相机标定 → 动作坐标转换 → 图像适配 → 深度适配 → 伪机器人示范 → RISE-2 训练 → 真实双臂执行

动作适配器把外骨骼关节通过正向运动学转成末端状态，再统一到全局相机坐标系。这样不同采集场景和部署平台可以共享明确的动作参考系，但前提是外骨骼、相机和机器人之间的标定可信

图像适配器先渲染外骨骼掩码，与 SAM2 分割的人手掩码合并，定位需要移除的区域。ProPainter 对时序图像补背景；另一条支路根据对应关节渲染机器人，再用 ControlNet 约束的 Stable Diffusion 改善外观，最后合成伪机器人图像。掩码是需要处理区域的像素标记，不是语义任务标签。流程包含人工标注和预训练模型，不能称为完全无人工处理

深度适配器使用空场景参考深度和示范第一帧静态物体深度，填补人和外骨骼所在区域，再与渲染机器人深度合成。这样避免只修改 RGB、却让深度仍显示人手的自相矛盾数据。对运动物体、严重遮挡和背景变化，参考深度的假设仍需检查

RISE-2 的稀疏编码器处理三维点云，稠密编码器提取二维图像语义。空间对齐器根据三维点投影，插值读取图像特征并融合几何信息，再用稀疏卷积聚合。解码器和扩散头输出动作块，平移为相机坐标下的绝对位置，旋转采用六维连续表示。扩散模型是在动作空间去噪，不是靠生成视频直接控制电机

二维基础模型可冻结部分参数，论文同时列训练参数量与总参数量。部署仍需将相机坐标动作变为机器人执行命令，不能省略逆运动学、工作空间和控制接口验证

## D. 实验与结果

§4.1 使用四个真实任务，每任务五十条遥操作示范，比较 ACT、Diffusion Policy、CAGE、RISE、π0 与 RISE-2。Figure 4 的四任务平均成功率：RISE 74.4%、π0 72.5%、RISE-2 ResNet-18 为 84.4%、RISE-2 DINOv2 为 93.8%。这些是该四任务设置的平均，不是所有机器人任务上的排名

Table 1 只针对 Collect Toys：训练分布内 RISE-2 DINOv2 为 95%，新背景 85%、新物体 85%、两者同时变化 62.5%；π0 对应 85%、77.5%、82.5%、82.5%。因此本文方法在联合变化条件下低于 π0，不能只引用前三列声称全场景最优

Table 4 测三条轨迹的平移误差，AirExo-2 平均 1.737±1.713 mm、最大 6.134 mm，UMI 平均 8.855±3.228 mm、最大 20.002 mm。这是特定轨迹与测量流程下的误差，不代表机器人接触精度或所有视觉跟踪系统的水平

数据来源对比和长程 Serve Steak 见 §4.2 及附录，图示支持仅用适配后的野外示范直接真机部署。附录 Table 7 和 Figure 14 的均值相互对应，不能因抽取顺序把 74.4 和 60.6 误看成版本矛盾。文中部分协议提二十次测试而百分比出现 2.5% 步进，本卡不反推出每格成功次数，保留原始报告口径。野外示范转换总算力、全部人工掩码工时和所有实验采集者总人数没有统一汇总，不能据六百美元机构价格推算总成本

## E. 不足与未来

作者指出，伪示范目前主要适用于较强泛化策略，未来可用新视角合成扩大可用范围。视觉适配并没有彻底消除所有域差异

本库分析：图像修复可能改变接触边界，参考深度可能不适合强动态遮挡；这些是需要验证的数据可信度问题，不能只凭画面看起来真实判断。机械同构减少映射难度，却增加设备适配要求。机器人手指与人的接触拓扑不同，手臂级示范有效也不能保证多指操作可用

对我们的研究设想是先用夹爪、固定 D435i 和少量任务检查“动作误差—合成观察误差—策略成功率”的因果链，再决定是否扩展到 DH116。应保留未合成的原始记录，单独审查物体边缘与接触帧；不要把生成得更漂亮当作数据质量更高。该流程主要解决训练数据转换，失败轨迹修补也不等同于部署阶段的自动恢复系统

## 相关工作与阅读入口

- [[03 论文卡片/08_数据与遥操作/AirExo - Low-Cost Exoskeletons for Learning Whole-Arm Manipulation in the Wild|P219 · AirExo: Low-Cost Exoskeletons for Learning Whole-Arm Manipulation in the Wild]]
- [[03 论文卡片/08_数据与遥操作/FastUMI - A Scalable and Hardware-Independent Universal Manipulation Interface with Dataset|P222 · FastUMI: A Scalable and Hardware-Independent Universal Manipulation Interface with Dataset]]
- [[03 论文卡片/08_数据与遥操作/Universal Manipulation Interface - In-The-Wild Robot Teaching Without In-The-Wild Robots|P193 · Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots]]

- 所属方向：[[02 研究方向/数据与遥操作]]
- 专题导读：[[02 研究方向/数据与遥操作_从采集到可执行示范]]
- 遥操作路线：[[02 研究方向/机器人遥操作与动作重定向]]
- 数据质量路线：[[02 研究方向/机器人数据采集与数据质量]]

## 来源与核验边界

- 已阅读上述 23 页版本的正文、方法、实验与局限，含附录时一并核对；关键架构或实验表经页面渲染检查，数字位置见各节
- 日期依据官方 arXiv 提交历史，机构依据所读版本署名；正式出处与所读预印本版本分别标明，不用会议日程或演示获奖冒充正式出版
- 论文结果、作者限制和本库研究设想分开；未报告字段不补猜，未核实引用量不填 0
- 代码和数据链接用于核对公开资源，未运行第三方代码、未执行机器人动作；可访问与可完整复现分别评价
- PDF 再分发许可未统一确认，遵循现有忽略规则仅保存本地；代码许可不自动覆盖论文、数据及模型
