---
paper_id: "P221"
title: "ForceMimic: Force-Centric Imitation Learning with Force-Motion Capture System for Contact-Rich Manipulation"
aliases: ["ForceMimic", "面向接触操作的力与运动示范采集及模仿学习"]
authors: ["Liu, Wenhai", "Wang, Junbo", "Wang, Yiming", "Wang, Weiming", "Lu, Cewu"]
year: 2024
venue: "ICRA 2025"
arxiv: "2410.07554"
version: "v3"
pdf: "01 论文文库/PDFs/08_数据与遥操作/ForceMimic.pdf"
document_type: "research_paper"
preprint_platform: "arXiv"
first_public_date: "2024-10-10"
first_public_month: "2024-10"
first_public_scope: "arXiv v1 UTC submission; cross-platform earliest release not established"
publication_status: "ICRA 2025"
affiliations: ["Shanghai Jiao Tong University"]
metadata_verified_on: "2026-10-25"
metadata_sources: ["https://arxiv.org/abs/2410.07554", "https://forcemimic.github.io/", "https://arxiv.org/pdf/2410.07554v3"]
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Human_Demonstration", "Retargeting"]
doi: "10.1109/ICRA55743.2025.11128061"
---

# ForceMimic: Force-Centric Imitation Learning with Force-Motion Capture System for Contact-Rich Manipulation

## 基本信息

- 稳定编号：P221
- 中文译名：面向接触操作的力与运动示范采集及模仿学习
- 作者：Liu, Wenhai；Wang, Junbo；Wang, Yiming；Wang, Weiming；Lu, Cewu
- 研究机构：Shanghai Jiao Tong University
- 年份：2024
- 首次公开：arXiv v1，2024-10-10（UTC；仅限定该平台，不声称全平台最早）
- 出处与版本：ICRA 2025；所读 v3，8 页
- 研究主题：机器人外力数据采集、力位混合控制、示范域差异
- 引用量：待核验
- 引用量来源：Google Scholar
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/ForceMimic.pdf|打开本地 PDF]]（已核对文件身份；仅本地保留，不承诺 GitHub 网页可访问）
- [官方论文页](https://arxiv.org/abs/2410.07554)｜[官方 PDF](https://arxiv.org/pdf/2410.07554v3)｜[官方项目](https://forcemimic.github.io/)
- DOI：[ 10.1109/ICRA55743.2025.11128061 ](https://doi.org/10.1109/ICRA55743.2025.11128061)
- 官方代码：[对应 GitHub 仓库](https://github.com/ForceMimic/forcecapture)
- 数据：[官方数据入口](https://drive.google.com/drive/folders/1sKqOj9tO-luddM8XIaJvTFbRSEZet7C3)（下载内容、许可与访问权限以页面说明为准）

## 论文简介

削蔬菜这类任务不是轨迹画得像就能成功。工具沿表面移动时，需要保持合适的压力；力过大可能损伤物体，力过小又无法接触。ForceMimic 的出发点是把人演示时的力也记录下来。作者制作手持 ForceCapture，在人握持部位与工具之间放置六维力传感器，同时记录工具位姿、夹爪开合和外部 RGB-D 观察，不必让操作者通过机器人间接操作。六维力包含三个方向的力和三个方向的力矩，并不等于每个手指的触觉分布

采到力之后，论文没有简单地把所有力值作为策略输入，而是让 HybridIL 从点云和机器人位姿预测未来的位置与力参数，再由底层控制器匹配这些参数。在非接触阶段使用位置控制，在持续接触阶段切换到力位混合控制，沿运动方向跟随轨迹、在正交方向控制接触力。这个分工体现了学习模型与可执行控制之间的接口设计：模型给出希望做什么，控制器决定怎样在实际硬件上稳定实现

真实实验主要是西葫芦削皮，而不是覆盖大量灵巧操作任务。论文把“正确削下任意长度”和“连续削皮超过十厘米”分成两个指标，HybridIL 在二十次测试中分别达到全部成功和 85%。有意思的是，增加力作为输入的基线反而更差，作者将其与人类采集和机器人执行时的力分布差异联系起来。对我们的意义是先明确力的测量、补偿和执行接口，再讨论多模态学习；没有力传感与力控制接口的 DH116 或普通机械臂不能直接照搬结果

## A. 基本信息与研究问题

研究问题是如何低成本记录自然接触中的力位关系，并把这种示范转成机器人可执行控制。只记录末端位置不能区分轻贴、重压和刮擦，而双向力遥操作又有系统复杂、操作者需要训练和采集速度慢等问题

ForceCapture 有固定工具版和可开合夹爪版。六维力传感器位于工具与握柄之间，T265 跟踪运动，L515 观察场景，夹爪版还带编码器与单向自锁机构。实验机器人为具备力感知和力控能力的 Flexiv Rizon 4，不能把该能力视为所有机械臂的默认功能

## B. 相关工作

传统示教可通过拖动、主从臂或手持装置记录轨迹，但接触力往往没有进入训练目标。单纯加入力传感输入也不充分，因为人手与机器人控制器对同一物体施加的力分布可能不同，策略会在部署时进入没见过的输入区域

UMI 和 DexCap 说明机器人外采集可以降低设备占用，本作在这一思路上增加可直接测量工具环境作用力的机械路径。Diffusion Policy 原本预测动作序列，本文扩展为预测力位参数，并让底层控制器显式实现这些参数。改进点不是用一个新名字替代扩散模型，而是将数据采集、重力补偿、策略输出和接触控制接口对齐

## C. 核心贡献与方法

流程：手持工具自然演示 → 同步力、位姿和视觉 → 重力补偿与点云处理 → 扩散策略预测力位动作块 → 判断接触阶段 → 位置或力位混合控制 → 真机执行

六轴力传感器的读数同时包含工具重力与交互力。作者假设采集近似准静态，即工具运动产生的惯性力相对较小，先通过多姿态静态记录构造超定方程，用最小二乘估计质量和重心，再从读数中扣除重力。快速运动时该假设可能失效，因此不能把补偿后的所有动态变化都当作真实接触力

力传感、T265、L515 和夹爪编码器分别以 1000、200、30、30 Hz 采集，处理时对齐到视觉三十赫兹。T265 初始安装在 L515 支架上确定参考关系，之后移动到手持装置。点云剔除不一致的人与背景区域，保留工具与物体并下采样到一万个点，减少训练与执行观察差别

HybridIL 用点云编码和机器人 TCP 位姿预测未来二十步位置与 wrench 参数。TCP 是工具中心参考点。预测力连续超过经验阈值六牛顿时切换控制模式；从位置轨迹估计运动方向，将力投影到与运动方向正交的平面，使沿路径运动与法向施压不过度冲突。开始接触时还需要压靠动作，建立稳定接触后才持续跟踪

夹爪的自锁机构避免手指持续挤压握柄把非环境作用力混入传感器。这个机械细节直接影响标签是否可信。输出可执行性还依赖 Flexiv 的控制原语和力控带宽，不是训练网络后任意电机都能实现相同效果

## D. 实验与结果

Figure 5 比较削完一根西葫芦的时间：直接手工约 2.9 分钟、ForceCapture 4.5 分钟、遥操作 13 分钟。它是单技能案例的效率比较，不能推论所有接触任务都三倍加速，也没有给出足以推广的人群统计

训练数据来自十五根西葫芦，切分为 438 段削皮技能，共 30,199 个动作序列；不是 30,199 次完整削菜。模型与基线均训练五百轮，动作相对观察提前三个时间步。左臂按规则固定蔬菜，右臂学习削皮，不是双臂都由同一策略自主学习

Table I 的 Raw DP 与 HybridIL 各测二十次，另两种较弱基线各十次。正确运动指标为成功接触并削下皮且不损坏物体：Raw DP 80%，HybridIL 100%；连续削皮超过十厘米时分别为 55% 和 85%。Force DP 对应 60%/10%，Force+Hybrid DP 为 80%/20%。不等分母必须明确，不能把百分比当相同统计可靠性

Figure 7 显示 Raw DP 即使完成运动，也可能施力平均约二十牛顿、局部超过四十牛顿；HybridIL 平均约九牛顿，更接近人类示范约十牛顿。它说明同样的“成功”可能接触质量不同，但论文没有据此给出统一损伤概率模型。失败包括未接触、过大压力、输出阶段提前结束造成削皮中断。所有采集者总人数、完整训练耗时与推理延迟未统一报告

## E. 不足与未来

作者明确说明仅验证单一削皮技能，未来需要更丰富的多模态表示和更多控制原语。力作为输入在分布变化下仍是未解决挑战，不能将本文说成已经解决通用力觉学习

本库分析：准静态重力补偿不适合直接覆盖高速运动；力阈值、摩擦、工具几何和控制器切换都需要平台重新标定。打印件与编码器约五十美元不包括力传感器和相机，整套成本不能写成五十美元。压力信号也不能替代手指接触位置与剪切力

对我们的具体设想是用有力控能力的机械臂和普通工具先做低风险接触实验，分别比较纯位置、力作输入、力作输出三种设置，再考虑 DH116。D435i 可提供点云但不能提供接触力；若手部缺少可信力测量，应先做受限压力和滑移检测，不能宣称复现了 HybridIL。训练时改正示范或切换控制原语，不等于机器人能在部署失败后自动判断原因并恢复

## 相关工作与阅读入口

- [[03 论文卡片/08_数据与遥操作/FastUMI - A Scalable and Hardware-Independent Universal Manipulation Interface with Dataset|P222 · FastUMI: A Scalable and Hardware-Independent Universal Manipulation Interface with Dataset]]
- [[03 论文卡片/08_数据与遥操作/Universal Manipulation Interface - In-The-Wild Robot Teaching Without In-The-Wild Robots|P193 · Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots]]
- [[03 论文卡片/04_灵巧操作/DexUMI - Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation|P086 · DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation]]

- 所属方向：[[02 研究方向/数据与遥操作]]
- 专题导读：[[02 研究方向/数据与遥操作_从采集到可执行示范]]
- 遥操作路线：[[02 研究方向/机器人遥操作与动作重定向]]
- 数据质量路线：[[02 研究方向/机器人数据采集与数据质量]]

## 来源与核验边界

- 已阅读上述 8 页版本的正文、方法、实验与局限，含附录时一并核对；关键架构或实验表经页面渲染检查，数字位置见各节
- 日期依据官方 arXiv 提交历史，机构依据所读版本署名；正式出处与所读预印本版本分别标明，不用会议日程或演示获奖冒充正式出版
- 论文结果、作者限制和本库研究设想分开；未报告字段不补猜，未核实引用量不填 0
- 代码和数据链接用于核对公开资源，未运行第三方代码、未执行机器人动作；可访问与可完整复现分别评价
- PDF 再分发许可未统一确认，遵循现有忽略规则仅保存本地；代码许可不自动覆盖论文、数据及模型
