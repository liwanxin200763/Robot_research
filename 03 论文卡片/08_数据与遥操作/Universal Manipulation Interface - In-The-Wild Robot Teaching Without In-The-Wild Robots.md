---
paper_id: P193
title: "Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots"
authors: ["Chi, Cheng", "Xu, Zhenjia", "Pan, Chuer", "Cousineau, Eric", "Burchfiel, Benjamin", "Feng, Siyuan", "Tedrake, Russ", "Song, Shuran"]
year: 2024
venue: "Robotics: Science and Systems (RSS) 2024"
arxiv: "2402.10329"
version: "v3"
arxiv_version: "v3"
pdf: "01 论文文库/PDFs/08_数据与遥操作/UMI.pdf"
verified_on: "2026-10-15"
citation_status: "待 Google Scholar 人工核验"
tags: ["Teleoperation", "Data_Collection", "Retargeting", "Imitation_Learning"]
document_type: "会议论文"
preprint_platform: "arXiv"
first_public_date: "2024-02-15"
first_public_month: "2024-02"
first_public_scope: "arXiv v1 submission history (UTC)"
latest_preprint_date: "2024-03-06"
latest_preprint_version: "v3"
publication_status: "已正式发表"
published_venue: "Robotics: Science and Systems (RSS) 2024"
affiliations: ["Stanford University", "Columbia University", "Toyota Research Institute"]
metadata_verified_on: "2026-10-17"
metadata_sources: ["https://arxiv.org/abs/2402.10329", "https://arxiv.org/pdf/2402.10329v3", "https://www.roboticsproceedings.org/rss20/p045.html", "https://umi-gripper.github.io/"]
publication_year: 2024
publication_month: "2024-07"
---

# Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots

## 出处与版本

- 文献类型：会议论文
- 预印本平台与编号：[arXiv 2402.10329](https://arxiv.org/abs/2402.10329)
- 首次公开日期：2024-02-15；首次公开月份：2024 年 2 月，依据 arXiv v1 提交历史（UTC）；本字段不宣称已穷尽项目网页或其他平台可能更早的公开记录
- 最近预印本更新：2024-03-06（2024 年 3 月），v3；与首次公开日期分开
- 当前发表状态：已正式发表
- 正式发表出处：[Robotics: Science and Systems (RSS) 2024](https://www.roboticsproceedings.org/rss20/p045.html)
- 正式出版年份：2024；正式出版月份：2024 年 7 月
- 日期与状态说明：RSS XX 官方 BibTeX：2024 年 7 月；DOI：10.15607/RSS.2024.XX.045
- 作者所属机构：Stanford University；Columbia University；Toyota Research Institute
- 机构依据：正文首页列 Stanford、Columbia 和 Toyota Research Institute；Cheng Chi、Zhenjia Xu、Shuran Song 为前两者联合署名，Chuer Pan 为 Stanford，其余作者署名 TRI；[对应版本 PDF 首页](https://arxiv.org/pdf/2402.10329v3)
- 项目主页：[作者项目页](https://umi-gripper.github.io/)
- 官方代码：[作者链接的仓库](https://github.com/real-stanford/universal_manipulation_interface)；入口存在不等于已核实完整实现、模型或许可，开源边界沿用下文说明
- 信息核验日期：2026-10-17；来源为官方版本历史、正文署名和上述正式条目；引用量沿用原 Google Scholar 人工核验规则

## 论文简介

带机器人到每个房间采数据很昂贵，普通人手视频又缺少能直接训练机器人的动作标签。UMI（通用操作接口）选了中间路线：人手持带相机和传感器的夹爪，在自然环境中操作物体，再把记录转为机器人可以执行的观察—动作数据

这不是“把视频直接喂给模型”。流程是“手持示范 → 视觉惯性定位恢复运动 → 对齐夹爪开合和时间戳 → 用相对末端轨迹训练扩散策略（逐步去噪生成动作序列的模型） → 匹配真实部署延迟”。视觉惯性定位结合相机与惯性传感器估计运动；相对动作降低对机器人绝对坐标的依赖；延迟匹配让策略不要执行已经过时的目标。相比实验台遥操作，它扩大采集地点；相比裸手视频，它保留与夹爪执行更接近的接触和动作接口（§III）

真机投掷测试中，有延迟匹配为 105/120＝87.5%，去掉后为 69/120＝57.5%；分母是投掷物体数，不是整回合数。杯子摆放同一模型从 UR5 迁至 Franka 得到 18/20 次成功，两次关节限位失败也说明“通用”仍受工作空间约束（§IV）

对我们的研究，应先学习相对轨迹和时间对齐，而非仅仿造夹爪外壳。D435i 并不能未经验证替换其 GoPro、惯性传感与镜面视角；DH116 的多指接触还需单独动作接口。把便携采集推广到灵巧手是可研究方向，本文的平行夹爪结果不是已有五指验证

## A. 基本信息与研究问题

- 作者：Cheng Chi、Zhenjia Xu、Chuer Pan、Eric Cousineau、Benjamin Burchfiel、Siyuan Feng、Russ Tedrake、Shuran Song
- 正式发表：Robotics: Science and Systems（RSS）2024；arXiv 2402.10329 最新v3，2024-03-06
- [官方会议页](https://www.roboticsproceedings.org/rss20/p045.html)｜[arXiv](https://arxiv.org/abs/2402.10329)｜[项目页](https://umi-gripper.github.io/)
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/UMI.pdf|查看 PDF]]；按官方arXiv v3全文18页核验
- [官方代码](https://github.com/real-stanford/universal_manipulation_interface)，MIT；引用量待 Google Scholar 人工核验

UMI把采集地点从机器人工作台扩展到家庭、办公室和餐馆：人直接拿带相机的夹爪示范，离线恢复动作，再训练机器人策略。它既不是从任意网络人类视频直接学动作，也不是完全无需标定的任意硬件迁移。关键是让手持采集和机器人部署具有接近的视觉、末端动作与时间接口（§III）

## B. 相关工作

ALOHA、GELLO获得真实从臂动作，几何约束清楚，却必须携带机器人；裸手视频地点多，但缺少可信动作标签，手和夹爪外观差异也大。手持工具是折中：保留便携性，同时用与机器人接近的夹爪接触物体。此前手持接口常只支持慢速抓放，因为单目尺度、追踪与延迟问题会阻断动态技能转移（§II）

UMI不是另造策略模型，而是把视觉惯性SLAM、连续夹爪宽度、相对轨迹和部署延迟匹配接成一致数据管线，用Diffusion Policy表达多峰行为。其价值在于各模块共同满足动作可部署条件；只有一个便宜夹爪而没有这些接口，不等于完成UMI复现

## C. 核心贡献与方法

### 1. 一份视频包含观察和动作恢复所需信息

手持3D打印平行夹爪装软手指、GoPro和155°鱼眼镜头。大视野减少物体离开腕部视野的概率；两块侧镜形成隐式双目，网络输入前对镜内图像翻转并左右交换。部署在机器人上时保持相机相对指爪位置相同，让策略不必适应完全不同的手与机器人外观（p2–5，图2–4）

GoPro的MP4同时保存RGB及IMU，ORB-SLAM3视觉惯性优化恢复公制尺度和快速运动轨迹；短暂视觉模糊时惯性信息可维持追踪，但长期无纹理仍会失败。夹爪上的标记连续估计开口宽度，软指形变提供隐式夹持调节，不是直接测量接触力。单夹爪780 g，打印机构BOM73美元、相机及附件298美元，共371美元；这不含部署机器人和工业夹爪（p5）

### 2. 相对轨迹与双臂同步

采集新场景先建图，再将各示范、各夹爪定位到共享地图。动作块中的每个未来SE(3)目标都相对本次推理的当前末端，而非相对前一步动作；后者是会累积误差的delta表示。历史末端轨迹也用相对表示，双臂额外输入两夹爪相对位姿，才能在两腕相机视野重叠少时协调同时抓取（p6，图6）

这降低对机器人基座世界坐标精确标定的依赖，但仍需相机／IMU内参、传感器时间关系、末端安装及目标机器人运动学。手持工具能做出的动作未必机器人能做；作者根据已知基座与运动学过滤不可行轨迹，不能把采集自由度当成机械臂已具备的可执行范围

### 3. 延迟匹配是部署接口的一部分

观察流分别测真实延迟，以最慢流通常为图像的捕获时间为基准，对臂位姿、夹爪宽度插值；双腕相机软同步。输出动作有目标时间戳，分别按臂与夹爪执行延迟提前发送，删除已因采集、推理和执行等待而过期的动作。图5的100 ms臂／120 ms夹爪为该图系统示意，不能转写成所有平台固定值（p5–6、附录A）

“同步腕部RGB＋相对末端历史＋宽度／双夹爪关系→Diffusion Policy→未来相对末端与宽度轨迹→各硬件定时执行”是完整管线。论文通常用10–20 Hz策略观察，不能与臂底层125 Hz或相机录制帧率混称同一种控制频率。这里没有远端操作者视觉回传环节，因为人直接拿工具接触现场

## D. 实验与结果

### 能力测试与明确计数

| 任务／设置 | 数据量 | 结果与对照 |
|---|---:|---|
| Cup Arrangement | 305条 | UR5 20/20；同checkpoint迁移Franka 18/20 |
| Dynamic Tossing | 280条 | 105/120个物体=87.5%；去延迟匹配69/120=57.5% |
| 双臂折衣 | 250条 | 14/20=70%；去相对夹爪状态6/20=30% |
| Dish Washing | 258条 | ViT组14/20=70%；ResNet对照0/10 |

杯子任务要求杯直立放在碟上且把手角度在目标±15°。Franka两次失败为关节限位，支持共享末端接口的可迁移性，同时暴露基座布局边界。投掷按120个物体统计，不能写成120个完整任务回合；洗碗包括恢复额外污渍的明确示范，不能推导为无需恢复数据的通用纠错（p7–10，图7–8）

杯子消融中去鱼眼为11/20；绝对动作5/20、delta16/20。侧镜未经正确图像变换只有17/20，去镜18/20，正确处理后20/20，表明增加视觉信息本身也可能制造表征困难。绝对动作差还受SLAM到基座标定误差影响，不能证明所有场景中绝对动作天然劣于相对动作（p7–8）

### 野外泛化与采集效率

三位示范者12人时采集30地点、15种杯子的1400条示范，ViT-L/14策略在两个未见环境合计43/60=71.7%，其中见过杯28/40、未见杯15/20；只用单实验室数据、同预训练骨干的对照为0%。结论支持多样场景数据的必要性，不等于对任何新物体零样本通用（p9–10，图9）

吞吐实验包含重置和机器人故障耗时，杯子为UMI111条/小时、SpaceMouse35、裸手231；动态投掷149、0、237。MoCap基准的单夹爪轨迹均值误差6.1 mm／3.5°，双夹爪相对位姿10.1 mm／0.8°；“小于1 cm”不能无条件覆盖双夹爪平移误差（p11，图11–12）

## E. 不足与未来

**作者指出：**采集时不知道下游机器人限位，只能事后筛轨迹；SLAM依赖纹理；夹爪笨重且自由度少，效率仍不如裸手。未来应改进可行性学习、无纹理恢复及设备人体工学（§VIII）

**我的理解：**本项目可先用D435i录离线RGB-D，研究统一时间戳、相对轨迹与质量过滤，但它不能直接替换GoPro鱼眼／IMU后继承UMI结果。DH116为欠驱动多指手，不等同80 mm平行夹爪，需要新的接触与手指动作接口；先离线检查三指重定向、耦合和工作空间，多轴动作仍未验收。完整复现另需手持机构、镜头侧镜、相机同步、目标臂、兼容夹爪与计算资源；371美元只对应采集端单工具

## 来源与核验边界

- [官方PDF](https://arxiv.org/pdf/2402.10329v3)；已逐段核对方法、实验、失败与局限，并渲染架构图及主结果表核对行列
- 以上论文数值来自对应PDF页码；当前官方仓库状态与论文实验设置分开，未运行其代码或任何机器人动作
- PDF许可：http://arxiv.org/licenses/nonexclusive-distrib/1.0/；仓库代码许可不自动覆盖PDF、数据和第三方依赖
- [正式发表来源](https://www.roboticsproceedings.org/rss20/p045.html)、[项目页](https://umi-gripper.github.io/)与官方仓库已核验；引用量仍待人工核验
- 关联专题：[[02 研究方向/机器人遥操作与动作重定向]]；[[02 研究方向/机器人数据采集与数据质量]]
