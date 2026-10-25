---
paper_id: "P226"
title: "DexViTac: Collecting Human Visuo-Tactile-Kinematic Demonstrations for Contact-Rich Dexterous Manipulation"
aliases: ["DexViTac", "面向接触丰富灵巧操作的视觉触觉运动学示范采集"]
authors: ["Chen, Xitong", "Pan, Yifeng", "Li, Min", "Ding, Xiaotian"]
year: 2026
venue: "arXiv preprint；未核实正式录用"
arxiv: "2603.17851"
version: "v1"
pdf: "01 论文文库/PDFs/08_数据与遥操作/DexViTac.pdf"
document_type: "research_paper"
preprint_platform: "arXiv"
first_public_date: "2026-03-18"
first_public_month: "2026-03"
first_public_scope: "arXiv v1 UTC submission; cross-platform earliest release not established"
publication_status: "arXiv preprint；未核实正式录用"
affiliations: ["Huazhong University of Science and Technology", "Wuhan Huaweike Intelligent Technology Co., Ltd."]
metadata_verified_on: "2026-10-25"
metadata_sources: ["https://arxiv.org/abs/2603.17851", "https://xitong-c.github.io/DexViTac/", "https://arxiv.org/pdf/2603.17851v1"]
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Human_Demonstration", "Retargeting"]
---

# DexViTac: Collecting Human Visuo-Tactile-Kinematic Demonstrations for Contact-Rich Dexterous Manipulation

## 基本信息

- 稳定编号：P226
- 中文译名：面向接触丰富灵巧操作的视觉触觉运动学示范采集
- 作者：Chen, Xitong；Pan, Yifeng；Li, Min；Ding, Xiaotian
- 研究机构：Huazhong University of Science and Technology；Wuhan Huaweike Intelligent Technology Co., Ltd.
- 年份：2026
- 首次公开：arXiv v1，2026-03-18（UTC；仅限定该平台，不声称全平台最早）
- 出处与版本：arXiv preprint；未核实正式录用；所读 v1，9 页
- 研究主题：视觉触觉同步、指关节状态、触觉表示预训练
- 引用量：待核验
- 引用量来源：Google Scholar
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/DexViTac.pdf|打开本地 PDF]]（已核对文件身份；仅本地保留，不承诺 GitHub 网页可访问）
- [官方论文页](https://arxiv.org/abs/2603.17851)｜[官方 PDF](https://arxiv.org/pdf/2603.17851v1)｜[官方项目](https://xitong-c.github.io/DexViTac/)
- 官方代码：[对应 GitHub 仓库](https://github.com/xitong-c/DexViTac_Code)
- 数据：[官方数据入口](https://huggingface.co/datasets/xitong-c/DexViTac_Dataset)（下载内容、许可与访问权限以页面说明为准）

## 论文简介

DexViTac 研究一个容易被纯视频采集忽略的问题：挤压软胶球、保持擦拭压力或调整手中物体时，关键接触过程可能被手指遮住，图像并不包含足够的力与接触分布信息。作者在人类演示端组合广角相机、动作捕捉手套、手腕追踪和指尖触觉阵列，记录同一动作的视觉、手部状态与接触变化；机器人端使用相同型号触觉传感器，减少由传感器本身不同带来的域差异

它不只是多装几个传感器。系统以触觉时间轴为锚点，对异步视觉、手部运动与位姿数据进行对齐，清理触觉零点漂移，再将人类手部表示转换为机器人可控制关节。学习部分用手部运动学给触觉特征提供空间参照，再与视觉特征进行对比预训练，最后接入 ACT 预测动作块。这样同样一块触觉响应可以结合手指姿态理解，而不是当作与接触位置无关的任意数字

论文报告四类代表任务的真实机器人实验，包括移液、擦白板、插笔和收集水果，完整方法在每项三十次测试中的平均成功率为 85.8%。这个数字来自固定单臂与特定灵巧手，不能外推为任意手和所有接触任务。对我们的直接价值是同步与传感器一致性设计，尤其适合讨论 DH116 是否能够获得可比较的触觉和关节标签。D435i 可参与视觉采集，但不能补出缺失的指端触觉或替代手部动作捕捉，跨硬件迁移仍需独立验证

## A. 基本信息与研究问题

核心问题是如何低成本扩展可用于接触技能的多模态人类示范，同时处理视觉遮挡、触觉歧义、异步采样和人机自由度差别。首次 arXiv 公开为 2026-03，当前没有以项目页宣传自动推断正式会议录用

采集端是 GoPro Hero 12、177° 鱼眼镜头、Manus Quantum Metagloves、T265 和五指触觉模块。真机为 RealMan RM-65 与 Inspire RH56DFTP。论文的结果不能当作 DH116 的型号性能，名称相近也不代表结构相同

## B. 相关工作

视觉手部估计容易在抓取时被物体和其他手指遮挡。动作捕捉手套可以改善这种观测退化，但额外设备成本和标定仍存在。以夹爪为主的 UMI 接口记录的是整体开合，不能描述复杂多指接触

已有视觉触觉学习通常在机器人自身采集数据，标签与部署一致，却受机器人数量和采集效率限制。本文把触觉放在人类示范接口上，并在机器人端复制传感模块。相同模块仅减少硬件差异，人的指腹、机器人表面材料和接触几何仍然不同

ACT 从观察生成未来动作块；本文的创新重点在可靠多模态数据和预训练表征，而非证明 ACT 自身解决了力控。触觉阵列测局部压力分布，与六维腕部力矩传感器提供的信息不同，二者不能混称为同一力觉输入

## C. 核心贡献与方法

流程：自然人手视觉触觉运动学采集 → 触觉锚定时间同步 → 手部和手腕重定向 → 触觉去噪 → 运动学条件预训练 → ACT 微调 → 同构感知真机执行

传感器标称触觉阵列为 8×16、量程零到二十牛顿、灵敏度 0.01 N；硬件可达千赫兹，但系统软件触觉流采用六十赫兹。必须区分硬件能力与实际训练时间轴。运动学一百二十赫兹下采样，位姿二百赫兹用最近邻时间匹配，视觉六十赫兹按帧对齐。共享 ROS2 时钟与缓存减少丢帧，但最近邻匹配不等于所有传感器在物理上严格同时曝光

人手用十九维伸展和外展参数表达，再经过两层映射进入机器人描述的关节空间与控制空间。手腕通过初始末端位姿和相机到机器人基座的旋转变换进行增量映射，旋转关系仍需校准。论文同时使用“无外部复杂校准”和自动标定描述，不能简化成任何坐标下都可直接执行

触觉预处理从原始阵列减去无负载基线和噪声阈值，再截断负值，减少假接触。预训练将触觉卷积特征与手部运动学特征融合，视觉编码器冻结作为语义参照，对齐当前视觉与当前及邻近时刻触觉，学习跨模态和时间一致性。随后把视觉、触觉和手部状态一起输入 ACT，监督预测多步动作

该机制让接触表征更可解释，但时序一致性损失不等于因果推断，也没有直接证明所有压力变化由某一动作因果引起。数据质量仍需逐段检查接触、释放和遮挡时刻

## D. 实验与结果

§IV 数据包含超过 2,400 条、四十多项任务、十多个环境。真实策略评价只选其中四项代表任务，不能把整套数据集全部视为已完成同规模机器人基准

Table I 每任务三十次：完整方法移液 83.3%、擦白板 86.7%、插笔 80.0%、水果收集 93.3%，平均 85.8%；纯视觉 ACT 平均 17.5%，无预训练平均 48.3%，去掉运动学与时间耦合平均 58.4%。这些是不同模型配置在该四任务中的结果，并非触觉传感器单一变量的完全控制因果实验

例如水果收集从无预训练 53.3% 到完整 93.3%，是四十个百分点差，不是相对增加四十个百分点之外再加其他消融收益。图示追踪比较显示视觉方法在遮挡时抖动，但未给出可推广到所有手型的统一毫米误差

Figure 7 描述代表任务采集吞吐超过每小时 248 条，而结论概述写超过一百条，后者是更保守量级，不能当成两个互斥的完整数据集统计。单位是示范/小时，不是每条示范成功率。采集者总人数、所有设备完整价格、预训练总算时与统一端到端延迟未完整汇总，本卡不补猜

## E. 不足与未来

作者指出固定基座限制长距离操作，单臂不足以处理复杂非对称双臂协作，未来希望增加移动与双臂能力。该方向尚不是当前实验证据

本库分析：相同触觉传感器并不能消除人机表面柔顺性、指长和接触面积差别；动态基线去噪也可能抹掉轻微持续接触。触觉与运动学同步需要检查真实时间戳，不能只看输出文件帧数相同。系统没有独立的自动失败诊断和长程恢复机制

我们的设想是先确认 DH116 能读出哪些关节与触觉字段，再决定能否复用预训练。若没有等价触觉阵列，可先研究 D435i 加关节状态的时间对齐与接触事件人工标签，避免宣称已经实现同等视觉触觉系统。新手和熟练者数据质量、软物体接触强度与失效回退都应单独测量，本文的四任务结果不能代替这些平台验证

## 相关工作与阅读入口

- [[03 论文卡片/08_数据与遥操作/DexWild - Dexterous Human Interactions for In-the-Wild Robot Policies|P224 · DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies]]
- [[03 论文卡片/08_数据与遥操作/ForceMimic - Force-Centric Imitation Learning with Force-Motion Capture System for Contact-Rich Manipulation|P221 · ForceMimic: Force-Centric Imitation Learning with Force-Motion Capture System for Contact-Rich Manipulation]]
- [[03 论文卡片/04_灵巧操作/DexUMI - Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation|P086 · DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation]]

- 所属方向与专题导读：[[02 研究方向/数据与遥操作]]
- 遥操作路线：[[01 论文文库/专题阅读/机器人遥操作与动作重定向]]
- 数据质量路线：[[01 论文文库/专题阅读/机器人数据采集与数据质量]]

## 来源与核验边界

- 已阅读上述 9 页版本的正文、方法、实验与局限，含附录时一并核对；关键架构或实验表经页面渲染检查，数字位置见各节
- 日期依据官方 arXiv 提交历史，机构依据所读版本署名；正式出处与所读预印本版本分别标明，不用会议日程或演示获奖冒充正式出版
- 论文结果、作者限制和本库研究设想分开；未报告字段不补猜，未核实引用量不填 0
- 代码和数据链接用于核对公开资源，未运行第三方代码、未执行机器人动作；可访问与可完整复现分别评价
- PDF 再分发许可未统一确认，遵循现有忽略规则仅保存本地；代码许可不自动覆盖论文、数据及模型
