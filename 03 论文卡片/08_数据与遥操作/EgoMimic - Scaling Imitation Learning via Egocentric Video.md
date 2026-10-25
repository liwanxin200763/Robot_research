---
paper_id: "P236"
title: "EgoMimic: Scaling Imitation Learning via Egocentric Video"
aliases: ["EgoMimic", "通过第一人称视频扩展模仿学习"]
authors: ["Kareer, Simar", "Patel, Dhruv", "Punamiya, Ryan", "Mathur, Pranay", "Cheng, Shuo", "Wang, Chen", "Hoffman, Judy", "Xu, Danfei"]
year: 2024
venue: "ICRA 2025"
arxiv: "2410.24221"
version: "v1"
pdf: "01 论文文库/PDFs/08_数据与遥操作/EgoMimic.pdf"
document_type: "research_paper"
preprint_platform: "arXiv"
first_public_date: "2024-10-31"
first_public_month: "2024-10"
first_public_scope: "arXiv v1 UTC submission; cross-platform earliest release not established"
publication_status: "ICRA 2025"
affiliations: ["Georgia Institute of Technology", "Stanford University"]
metadata_verified_on: "2026-10-25"
metadata_sources: ["https://arxiv.org/abs/2410.24221", "https://egomimic.github.io/", "https://arxiv.org/pdf/2410.24221v1"]
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Human_Demonstration", "Retargeting", "Data_Quality"]
doi: "10.1109/ICRA55743.2025.11127989"
---

# EgoMimic: Scaling Imitation Learning via Egocentric Video

## 基本信息

- 稳定编号：P236
- 中文译名：通过第一人称视频扩展模仿学习
- 作者：Kareer, Simar；Patel, Dhruv；Punamiya, Ryan；Mathur, Pranay；Cheng, Shuo；Wang, Chen；Hoffman, Judy；Xu, Danfei
- 研究机构：Georgia Institute of Technology；Stanford University
- 年份：2024
- 首次公开：arXiv v1，2024-10-31（UTC；仅限定该平台，不声称全平台最早）
- 出处与版本：ICRA 2025；所读 v1，12 页
- 研究主题：第一人称采集、人机动作对齐、共同训练与样本效率
- 引用量：待核验
- 引用量来源：Google Scholar
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/EgoMimic.pdf|打开本地 PDF]]（已核对文件身份；仅本地保留，不承诺 GitHub 网页可访问）
- [官方论文页](https://arxiv.org/abs/2410.24221)｜[官方 PDF](https://arxiv.org/pdf/2410.24221v1)｜[官方项目](https://egomimic.github.io/)
- DOI：[ 10.1109/ICRA55743.2025.11127989 ](https://doi.org/10.1109/ICRA55743.2025.11127989)
- 官方代码：[对应 GitHub 仓库](https://github.com/SimarKareer/EgoMimic)
- 数据：[官方数据入口](https://huggingface.co/datasets/gatech/EgoMimic/tree/main)（下载内容、许可与访问权限以页面说明为准）

## 论文简介

EgoMimic 希望把人日常操作时记录的数据用于机器人学习，同时保留真实机器人示范的执行约束。直接看人类视频有两个难题：人的头会动，相机坐标不断变化；人的手和机器人机械臂外观、关节与抓取方式不同，不能直接把画面当成机器人动作监督。作者为人和机器人都配置相似的第一人称视角，并建立坐标、外观和动作分布的对齐流程

人类端使用 Project Aria 眼镜记录图像、头部位置和手部位置，机器人端使用类似人类上肢布局的双臂与眼镜。人类手部未来位置先转换到当前相机坐标，避免把未来头动混入目标；手与机械臂在图像中被掩掉，并用简化线条提示位置。共同训练的模型共享视觉和时序表征，但保留人类手位置与机器人关节动作两个不同输出头。人类数据提供更广的任务经验，机器人数据帮助模型学习实际关节与夹爪控制

实验涉及碗、衣物与杂货整理，既有分阶段累计得分，也有整任务成功率。两类数字不能互换，例如碗任务的一百二十八分不是百分之一百二十八的成功率。长程任务依然困难，杂货整理整体成功率只有百分之三十。对我们的价值是用便宜人类数据扩大场景覆盖，同时谨慎设计坐标系、分域归一化和机器人锚定；它没有完整手指或力标签，不能直接把这套手位置数据当作 DH116 灵巧抓取监督

## A. 基本信息与研究问题

研究问题是如何让可穿戴人类数据与机器人示范共同训练，并减少对昂贵机器人采集的依赖。人的动作标签是三维手位置，机器人的动作是双臂关节与夹爪，二者并不完全同构，方法需要保留这种差异

人类端 Aria 眼镜约七十五克，RGB 加两侧定位相机，通过运动感知服务估计设备轨迹和手位置。机器人使用两台 ViperX300S 六自由度臂、两路 D405 腕部相机与 WidowX 主端，倒装布局接近人体双臂。低于一千美元的支架成本不包含机械臂、相机和完整系统

## B. 相关工作

纯机器人行为克隆能学习真实动作，却受采集速度限制；纯人类视频方法容易只学视觉，缺少可执行标签。MimicPlay 从人类轨迹学习高层计划，再训练机器人低层；EgoMimic 则用同一个策略主体共同学习两种动作头，尝试让表征共享更直接

UMI 通过手持夹爪对齐观察与末端动作，适合平行夹爪；EgoMimic 保留自然人手，但只能从眼镜可靠取得部分手位置，不具有夹爪开合的直接等价标签。跨具身学习不是把缺失的人类夹爪动作强行补成零

ACT 用 Transformer 预测动作块，通过一段未来动作降低逐帧误差累积。本文沿用其基本策略骨架，并添加视觉、坐标和动作统计对齐，所以与 ACT 的结果差异既包括数据也包括模型设计；需要无人工数据的同架构消融来分离因素

## C. 核心贡献与方法

流程：Aria 记录第一人称视频与手轨迹 → 统一到当前相机坐标 → 人机图像掩码与线条提示 → 分域标准化 → 共享策略与分输出头训练 → 机器人关节动作部署

设世界到相机时刻 t 的位姿为 T_t，未来手位置为 p_i，转换可写成 T_t 的逆乘未来世界位置。这里始终固定在当前相机坐标，使目标描述“从现在看到的手应该去哪里”，而不是把未来头部转动当作手的运动

SAM2 分割人手或机械臂并遮掉外观，再叠加简化红线，减少人体皮肤、衣服和机器结构差异。人和机器人动作分别做均值方差归一化，避免不同活动范围主导共享模型。掩码能降低外观差异，但不能补出被遮住的物体或接触信息

共享 ResNet18 与 Transformer，机器人训练同时监督末端姿态与两侧各七维的关节/夹爪输出；人类端仅监督位置输出。部署采用关节头，避免再求逆运动学时的奇异位形或不连续解。不是所有数据都有相同动作维度，也没有把人类手指关节直接映射到机器人

主文算法用均方损失作简化说明，附录实际实现含 L1 重建与条件变分自编码器的 KL 项。人类动作块覆盖约一秒、机器人约四秒，均可采样为一百点，不能据此说原始采样率相同；原始数据约三十与五十赫兹

训练十二万步、batch 128，四张 A40 约二十四小时；四编码层、七解码层、隐藏 512、八头注意力。部署 4090 约一赫兹生成未来四秒动作，每次执行约一秒，再以二十五赫兹控制。预测跨度、推理频率与底层控制频率是三种不同量

## D. 实验与结果

Table II 三任务人类/机器人数据分别为：碗 1,400 条/60 分钟与 270 条/120 分钟；衣物 590 条/100 分钟与 430 条/300 分钟；杂货 160 条/80 分钟与 300 条/300 分钟。轨迹切分与任务时长不同，不能简单用条数比计算人类快多少倍

Table III 碗任务累计得分 EgoMimic 为 128，ACT 为 39，同架构无人工数据为 68，MimicPlay 为 71。碗共四十五次、九种组合，每次四十秒，是累计阶段分，不是二元成功率。128/39 的相对增长约 228%，不能写成成功率提高 228 个百分点

衣物整任务成功率 EgoMimic 88%、ACT 55%、无人数据版本 73%；杂货整任务为 30%、22%、28%。这些比例按论文四舍五入，衣物四十次与杂货五十次不能据近似百分比推断额外试次数。杂货开袋子子阶段 70% 不等于整任务 70%

新衣物颜色 ACT 25%、EgoMimic 85%；新场景使用该场景人类数据，EgoMimic 63 分、MimicPlay 4 分，不能宣称完全没见过目标域。两小时机器人加一小时人类达 128 分，而三小时 ACT 约 74 分，包含架构差异，不是纯采集时间的唯一因果实验

Table IV 碗得分完整模型 128、无线条 112、无线条及掩码 95、无动作归一化 79、无人类数据 68，支持这些对齐模块的作用。官方 Hugging Face 入口提供示例 HDF5，不能声称完整训练语料全部可下载

## E. 不足与未来

作者讨论对机器人种子数据的依赖，以及开袋、对齐物体、单袖等细节失败。用更多人类数据不自动消除接触和长程执行困难，三十个百分点级的杂货整任务表现也提醒不要只看更高的子步骤成绩

我的理解是当前相机坐标和分域归一化很值得复用，但硬件布局与 Aria 服务是额外前提。D435i 固定在桌边或机械臂上不能直接替代可穿戴定位链，需要另行估计相机运动和人手位置，并做遮挡与坐标漂移评估

现有夹爪可先复现相机视角与少量机器人锚定的思想；DH116 的手指、耦合与力接触不在本文人类标签中，应另加手部跟踪、标定和实际关节反馈。未来可研究多输出头、动作有效掩码与接触标签融合，分别比较视觉迁移和可执行性，不能把人类轨迹平滑等同于真实机器人失败恢复

## 相关工作与阅读入口

- [[03 论文卡片/08_数据与遥操作/MimicPlay - Long-Horizon Imitation Learning by Watching Human Play|P235 · MimicPlay: Long-Horizon Imitation Learning by Watching Human Play]]
- [[03 论文卡片/08_数据与遥操作/DexWild - Dexterous Human Interactions for In-the-Wild Robot Policies|P224 · DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies]]
- [[03 论文卡片/08_数据与遥操作/Universal Manipulation Interface - In-The-Wild Robot Teaching Without In-The-Wild Robots|P193 · Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots]]

- 所属方向与专题导读：[[02 研究方向/数据与遥操作]]
- 遥操作路线：[[01 论文文库/专题阅读/机器人遥操作与动作重定向]]
- 数据质量路线：[[01 论文文库/专题阅读/机器人数据采集与数据质量]]

## 来源与核验边界

- 已阅读上述 12 页版本的正文、方法、实验与局限，含附录时一并核对；关键架构或实验表经页面渲染检查，数字位置见各节
- 日期依据官方 arXiv 提交历史，机构依据所读版本署名；正式出处与所读预印本版本分别标明，不用会议日程或演示获奖冒充正式出版
- 论文结果、作者限制和本库研究设想分开；未报告字段不补猜，未核实引用量不填 0
- 代码和数据链接用于核对公开资源，未运行第三方代码、未执行机器人动作；可访问与可完整复现分别评价
- PDF 再分发许可未统一确认，遵循现有忽略规则仅保存本地；代码许可不自动覆盖论文、数据及模型
