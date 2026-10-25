---
paper_id: "P234"
title: "GenSim2: Scaling Robot Data Generation with Multi-modal and Reasoning LLMs"
aliases: ["GenSim2", "基于多模态与推理模型生成通用机器人示范"]
authors: ["Hua, Pu", "Liu, Minghuan", "Macaluso, Annabella", "Lin, Yunfeng", "Zhang, Weinan", "Xu, Huazhe", "Wang, Lirui"]
year: 2024
venue: "CoRL 2024"
arxiv: "2410.03645"
version: "v1"
pdf: "01 论文文库/PDFs/08_数据与遥操作/GenSim2.pdf"
document_type: "research_paper"
preprint_platform: "arXiv"
first_public_date: "2024-10-04"
first_public_month: "2024-10"
first_public_scope: "arXiv v1 UTC submission; cross-platform earliest release not established"
publication_status: "CoRL 2024"
affiliations: ["Tsinghua University", "University of California San Diego", "Shanghai Jiao Tong University", "Massachusetts Institute of Technology"]
metadata_verified_on: "2026-10-25"
metadata_sources: ["https://arxiv.org/abs/2410.03645", "https://gensim2.github.io/", "https://arxiv.org/pdf/2410.03645v1"]
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Human_Demonstration", "Retargeting", "Synthetic_Data"]
---

# GenSim2: Scaling Robot Data Generation with Multi-modal and Reasoning LLMs

## 基本信息

- 稳定编号：P234
- 中文译名：基于多模态与推理模型生成通用机器人示范
- 作者：Hua, Pu；Liu, Minghuan；Macaluso, Annabella；Lin, Yunfeng；Zhang, Weinan；Xu, Huazhe；Wang, Lirui
- 研究机构：Tsinghua University；University of California San Diego；Shanghai Jiao Tong University；Massachusetts Institute of Technology
- 年份：2024
- 首次公开：arXiv v1，2024-10-04（UTC；仅限定该平台，不声称全平台最早）
- 出处与版本：CoRL 2024；所读 v1，38 页
- 研究主题：自动任务编程、关键点约束求解、点云策略与Sim2Real
- 引用量：待核验
- 引用量来源：Google Scholar
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/GenSim2.pdf|打开本地 PDF]]（已核对文件身份；仅本地保留，不承诺 GitHub 网页可访问）
- [官方论文页](https://arxiv.org/abs/2410.03645)｜[官方 PDF](https://arxiv.org/pdf/2410.03645v1)｜[官方项目](https://gensim2.github.io/)
- 官方代码：[对应 GitHub 仓库](https://github.com/GenSim2/gensim2)
- 数据：未核实独立完整数据集入口；代码中的示例和项目展示不等于完整数据发布

## 论文简介

GenSim2 希望降低为每个新操作任务手写环境、规划器和示范的成本。前代语言模型生成任务的方法在桌面俯视取放上较容易成功，但碰到抽屉、箱盖、笔记本等关节物体，需要理解三维结构、接触位置和动作方向，只靠文字模板容易生成能运行却不能完成任务的代码

作者把多模态模型放进任务生成与求解循环：先选择物体并生成任务代码，运行后取得画面与物体关键点，再生成几何约束求末端操作姿态，并补上操作前后的运动。对于长程任务，可以先提出整体目标再分解，或从已有基本任务组合。数据生成之后，用点云、机器人本体状态和语言训练多任务策略，再测试仿真泛化与真实迁移。因此大模型编程、仿真求解和机器人策略训练是三个不同阶段，不能只看代码无报错就算机器人学会

实验展示一百种任务及真实关节物体操作，并对生成链条进行消融。真实实验每任务只有十次，组合训练平均结果提高，也有单项任务下降。它最值得关注的不是“语言模型替代一切”，而是用可检查的关键点与约束把语义落到几何，并用真实执行区分任务生成质量和策略能力。对我们的启发是先以夹爪、D435i 和少量关节物体做可验证的小闭环，DH116 的多指接触需要另行设计，不能直接套用六维末端求解器

## A. 基本信息与研究问题

研究问题是怎样扩展到一般六自由度末端运动与长程关节物体操作，同时减少人工写任务与示范。输入包含既有资产库、少量任务示例、场景渲染和物体关键点，输出包括任务代码、求解器配置、示范轨迹与学习后的视觉策略

生成任务不仅要语法正确，还要物理可执行且定义明确。论文分别使用 execution rate 与 solution rate：前者是管线运行无错误，后者是任务真的被求解。这两个指标应贯穿复现记录，不能混为一个成功率

## B. 相关工作

传统运动规划由人指定目标位姿与碰撞环境，精度较可控但设计成本高；强化学习通过奖励探索策略，却要设计奖励和付出训练成本。语言模型能写代码，但不一定理解物体的实际开合方向与可接触位置

kPAM 用物体关键点定义接触、方向和平行等几何约束，再求合适操作姿态，具有类别级复用潜力。GenSim2 让多模态模型读取场景图和关键点，生成这种可检查配置，而不是直接输出一串无法解释的关节值

相较纯语言任务生成，视觉信息帮助判断物体结构；相较只生成仿真代码，本文还训练点云多任务策略用于真机。域随机化用于改变点云观测，不能消除关节物体模型与现实的所有摩擦和柔性差异

## C. 核心贡献与方法

流程：资产与示例 → 任务提案 → 场景代码 → 渲染与关键点 → 约束与动作求解 → 仿真示范 → 多任务点云策略 → 真机验证

基本任务由模型生成描述、资产选择和环境代码。长程任务有自上而下分解与自下而上组合两条路，每个子任务仍需自己的求解器，组合目标并不自动保证子任务交界状态可行

求解阶段先生成关键点之间的重合、平行、垂直等约束，优化得到 actuation pose，即施加操作时的末端姿态。再生成操作前接近与操作后运动，构成对象中心轨迹。通过可视化和拒绝采样检查、迭代配置。论文还研究强化学习补充求解器，不能把所有任务都说成一次大模型调用直接成功

PPT 即本体状态—点云 Transformer，把点云、关节或末端状态和语言分别编码，通过交叉注意力与共享空间融合，再接动作预测头。可测试 MLP、Transformer 解码或扩散头，生成器和策略结构需要分别消融

为减小视觉差异，训练忽略点云颜色，加入裁剪、高斯扰动和丢点；真机点云做均匀采样、最远点采样和离群过滤。几何输入减少颜色依赖，但深度噪声、遮挡与相机外参仍影响结果

生成代码运行失败后的修改发生在训练数据准备阶段。真实机器人执行中遇到滑落、误抓时是否识别并恢复是另一个问题；本文的拒绝采样和提示链不能直接被称为部署故障恢复

## D. 实验与结果

生成任务规模最多一百种，覆盖约二百物体资产，不能将其当成一百个真机任务。图 5 比较多模态模型、推理模型、普通语言模型的求解比例约 0.78、0.36、0.18，各项至少十次生成。拒绝采样迭代与提示链也影响结果，有限样本不能估计任意任务生成准确率

真实平台为 Franka Research 3 与改装 TPU 平行夹爪，三台 RealSense D435（腕部一、外部二）合成点云。不是 D435i 惯性测量参与控制，也不是多指手验证

Table 2 在八任务各十次评估，仿真每任务一百条，真实每任务十条。真实数据单独训练平均 0.363，纯仿真 0.425，结合训练 0.575，分别为任务成功率的平均。结合相对真实单独提高 0.212，即约 21.2 个百分点，不能说每个任务都提升 20%

例如 OpenBox，真实单独 0.2、仿真 0.5、结合 0.0；OpenLaptop 对应 0.5、0.7、0.8。这说明平均提高不排除负迁移。纯仿真在部分任务实现零样本迁移，但结合结果使用了真实示范，不能都写成零样本

多任务仿真研究使用约 382M 参数策略，并比较任务数和未见物体实例；点云策略在特定未见实例条件下降小于三个百分点，依其训练划分成立。论文没有统一给出整套系统采集人数、所有生成审核总工时或通用部署延迟，均不补填

## E. 不足与未来

作者指出基础模型缺少机器人三维知识，会产生不合理任务与代码，仍需要少量人工介入；真机实验限于六自由度任务和有限点云观测。未来希望扩展任务复杂度、资产生成与跨本体迁移

我的理解是可执行代码与高质量示范之间还隔着任务合理性、碰撞、接触和观察标签一致性。复现应保存原提案、约束、失败类型与最终成功条件，内部日志存 Vault 外，正式笔记只保留可读结论

我们的机械臂、夹爪与 D435i 可先测试开盒或抽屉，明确相机外参、关节轴和安全运动区。DH116 需要多接触点、手指耦合与力限制，不能仅把夹爪换成手而沿用单末端求解。与 VLA 的联系主要是供给语言条件示范；与失败恢复的联系则需另设计部署反馈，而非把生成程序的修复当成自主纠错

## 相关工作与阅读入口

- [[03 论文卡片/08_数据与遥操作/DemoGen - Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning|P230 · DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning]]
- [[03 论文卡片/10_基准测试与数据集/RoboTwin 2.0 - A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation|P172 · RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation]]
- [[03 论文卡片/08_数据与遥操作/MimicGen - A Data Generation System for Scalable Robot Learning using Human Demonstrations|P202 · MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations]]

- 所属方向与专题导读：[[02 研究方向/数据与遥操作]]
- 遥操作路线：[[02 研究方向/机器人遥操作与动作重定向]]
- 数据质量路线：[[02 研究方向/机器人数据采集与数据质量]]

## 来源与核验边界

- 已阅读上述 38 页版本的正文、方法、实验与局限，含附录时一并核对；关键架构或实验表经页面渲染检查，数字位置见各节
- 日期依据官方 arXiv 提交历史，机构依据所读版本署名；正式出处与所读预印本版本分别标明，不用会议日程或演示获奖冒充正式出版
- 论文结果、作者限制和本库研究设想分开；未报告字段不补猜，未核实引用量不填 0
- 代码和数据链接用于核对公开资源，未运行第三方代码、未执行机器人动作；可访问与可完整复现分别评价
- PDF 再分发许可未统一确认，遵循现有忽略规则仅保存本地；代码许可不自动覆盖论文、数据及模型
