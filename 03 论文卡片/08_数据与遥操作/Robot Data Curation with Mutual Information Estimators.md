---
paper_id: P205
title: "Robot Data Curation with Mutual Information Estimators"
authors: ["Hejna, Joey", "Mirchandani, Suvir", "Balakrishna, Ashwin", "Xie, Annie", "Wahid, Ayzaan", "Tompson, Jonathan", "Sanketi, Pannag", "Shah, Dhruv", "Devin, Coline", "Sadigh, Dorsa"]
year: 2025
venue: "Robotics: Science and Systems (RSS) 2025"
arxiv: "2502.08623"
arxiv_version: "v3"
pdf: "01 论文文库/PDFs/08_数据与遥操作/DemInf.pdf"
verified_on: "2026-10-15"
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Teleoperation", "Data_Quality"]
document_type: "会议论文"
preprint_platform: "arXiv"
first_public_date: "2025-02-12"
first_public_month: "2025-02"
first_public_scope: "arXiv v1 submission history (UTC)"
latest_preprint_date: "2025-04-22"
latest_preprint_version: "v3"
publication_status: "已正式发表"
published_venue: "Robotics: Science and Systems (RSS) 2025"
affiliations: ["Google DeepMind Robotics", "Stanford University"]
metadata_verified_on: "2026-10-17"
metadata_sources: ["https://arxiv.org/abs/2502.08623", "https://arxiv.org/pdf/2502.08623v3", "https://www.roboticsproceedings.org/rss21/p023.html", "https://joeyhejna.com/demonstration-info/"]
publication_year: 2025
publication_month: "2025-06"
---

# Robot Data Curation with Mutual Information Estimators

## 出处与版本

- 文献类型：会议论文
- 预印本平台与编号：[arXiv 2502.08623](https://arxiv.org/abs/2502.08623)
- 首次公开日期：2025-02-12；首次公开月份：2025 年 2 月，依据 arXiv v1 提交历史（UTC）；本字段不宣称已穷尽项目网页或其他平台可能更早的公开记录
- 最近预印本更新：2025-04-22（2025 年 4 月），v3；与首次公开日期分开
- 当前发表状态：已正式发表
- 正式发表出处：[Robotics: Science and Systems (RSS) 2025](https://www.roboticsproceedings.org/rss21/p023.html)
- 正式出版年份：2025；正式出版月份：2025 年 6 月
- 日期与状态说明：RSS XXI 官方 BibTeX 的月份与 DOI 以会议条目为准，正式来源保留于本项链接
- 作者所属机构：Google DeepMind Robotics；Stanford University
- 机构依据：正文首页：Google DeepMind Robotics、Stanford；Joey Hejna 联合署名，Suvir Mirchandani 为 Stanford，其余作者在本论文中署名 Google DeepMind Robotics；不套用其他论文的任职信息；[对应版本 PDF 首页](https://arxiv.org/pdf/2502.08623v3)
- 项目主页：[作者项目页](https://joeyhejna.com/demonstration-info/)
- 官方代码：[作者链接的仓库](https://github.com/jhejna/demonstration-information)；入口存在不等于已核实完整实现、模型或许可，开源边界沿用下文说明
- 信息核验日期：2026-10-17；来源为官方版本历史、正文署名和上述正式条目；引用量沿用原 Google Scholar 人工核验规则

## 论文简介

遥操作示范即使都完成了任务，也可能包含抖动、绕行、无关动作和互相矛盾的控制。DemInf 关注“留下哪些数据更值得学”，希望不用给每条轨迹做昂贵人工评分，就能估计相对质量

核心量是状态与动作的互信息，即知道机器人处于什么状态后，动作变得多容易预测，同时动作本身又是否足够多样。系统分别用变分自编码器压缩状态和动作，再用近邻统计估计每个样本对互信息的贡献，汇总到整条轨迹，排序后筛选数据训练策略。它区别于只删除失败回合：失败不是唯一低质来源；也区别于只追求动作稳定，因为完全重复单一动作会丢失任务覆盖（§IV–V）

作者在 Robomimic、Franka 和 ALOHA 数据上检验筛选与策略效果。图 9 的 ALOHA 评估按抓起、交还、开包装累计得分，不能当成功率；Franka 才用二元成功指标。保留一半数据通常优于随机子集，但 PenInCup 的全数据略好，说明筛选阈值和数据分布会影响收益

对我们的 D435i＋机械臂＋DH116，先把状态、动作和任务分段记录完整，再比较人工质量分、随机子集和这种统计筛选，可能比盲目增加示范更有意义。不过多指接触中的正确动作常有多种，遮挡和错误状态也会影响互信息估计。将该评分与接触阶段覆盖结合是我们的设想，不是本文已验证的灵巧手算法

## A. 基本信息与研究问题

- 作者：Hejna, Joey; Mirchandani, Suvir; Balakrishna, Ashwin; Xie, Annie; Wahid, Ayzaan; Tompson, Jonathan; Sanketi, Pannag; Shah, Dhruv; Devin, Coline; Sadigh, Dorsa
- 年份与 Venue：2025；Robotics: Science and Systems (RSS) 2025
- arXiv：[最新核验版本 2502.08623v3](https://arxiv.org/abs/2502.08623)；核验日期 2026-10-15
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/DemInf.pdf|查看全文]]；[官方 PDF](https://arxiv.org/pdf/2502.08623v3)
- [项目主页](https://joeyhejna.com/demonstration-info/)；[官方仓库](https://github.com/jhejna/demonstration-information)
- 开源边界：代码 MIT；原始 RoboMimic/RoboCrowd 等数据许可须分别检查；本轮核验发布文件，未运行作者代码或复现实验
- 引用量：待 Google Scholar 人工核验，不填写估计数量
- 关联专题：[[02 研究方向/机器人数据采集与数据质量]]；[[02 研究方向/机器人遥操作与动作重定向]]


### 研究方向与快速摘要

DemInf（Demonstration Information Estimation）研究已经采来的示范如何按可学习性筛选。只看轨迹成功、长度或视觉多样性，会漏掉“同样观察下动作是否能预测”；只挑容易预测动作又可能全剩停顿。作者用状态与动作的 mutual information（互信息）兼顾动作多样性与条件可预测性，再通过低维表示和近邻估计，给完整轨迹排序。输入状态/图像与动作块，输出相对分数和筛选子集，之后单独训练 BC、ACT 或 Diffusion Policy（§III–V）

它在 robomimic 仿真、Franka、ALOHA 数据上多次提升人工质量分组和策略表现，但不是一套不依赖任务、动作表示和训练器的普适数据价值真值。关键前提是任务相关且成功的示范，长停顿要先处理；真机 PenInCup 上全数据略优于筛选，不能把摘要的5–10%写成所有场景保证

## B. 相关工作与先前不足

视觉/语言筛选常用去重、聚类和预训练模型，可帮助覆盖却不看机器人动作标签。ReMix 调整数据群组权重，粒度太粗；相似性检索挑近目标样本，不必然判断单条示范好坏；需要人工质量标签的模型也无法直接无监督用于新数据。DemInf 直接度量状态—动作关系，无需人工标签训练评分器，人工标签仅用于评测（§II）

InfoNCE、MINE 是可学习互信息估计器，但同分布数据有限时方差大。KSG 近邻估计常用于低维统计，直接处理图像会受维数灾难影响。本文先用两个 VAE 压缩，再做非参数近邻，结合了适合小数据的距离统计与图像表示，而不是把 CLIP 相似度当机器人质量（§IV–V）

## C. 核心贡献与方法

### 1. 质量目标与隐含条件

互信息分解为 I(S;A)=H(A)−H(A|S)。第二项低意味着给定观察时动作更确定，减轻模式混合和操作员使用策略看不见信息的问题；第一项高避免只保留恒定不动的动作。但这依赖被观察状态是否包含必要任务信息。多种正确解法可能提高条件熵，低分不必然表示示范失败，策略容量也会改变多峰数据的可学性（§IV）

动作表示也会改变估计：相对末端位移、绝对关节目标和动作块不是同一个随机变量；相对动作在静止时集中、绝对动作可能直接编码当前状态。须固定单位、坐标、频率、夹爪语义和本体后再比较分数。本文未证明这些表征下排名不变，也没有把不同机器人分数校准为通用量尺，这是本卡对方法的使用边界

### 2. VAE 建立状态与动作表示

分别训练状态编码器和动作块编码器，使用尽可能小而能保留信息的潜变量。VAE 的各向同性高斯先验使欧氏距离更有意义；图像实验用 ResNet-18＋SpatialSoftmax，多个视角特征与状态拼接，不直接在原始像素做近邻。Franka 动作块四步，RoboCrowd 十步；图像分别缩至128×128，robomimic84×84。训练表征 Adam学习率10⁻⁴、batch256，状态五万步、图像十万步，三种子；使用 TPU Research Cloud，未报告可直接换算的统一消费级 GPU 总耗时（§VI-A）

### 3. KSG、轨迹平均与筛选

在状态和动作联合潜空间找第 k 个近邻，用两子空间距离的最大值作联合度量；再分别数同半径内状态、动作邻居，通过 digamma 项估计每个样本对数据集互信息的相对贡献。常数项不影响同一数据集排序，但分数不是绝对“质量概率”。为减计算，随机打乱以1024样本批计算，遍历四次并对多个 k 平均（§V-B、附录 B/C）

先把逐样本分数截在1%–99%分位，抑制异常值，再在每条轨迹内取时间平均。**已有成功示范/停顿处理 → 状态与动作 VAE → 随机批 KSG → 每帧贡献 → 轨迹平均 → 阈值筛选 → 下游策略训练与测试。** 不能直接删低分帧：抓取时机本来比自由移动难预测，逐帧过滤可能删掉任务关键接触，轨迹平均正是为避免这点（图1–2、§V-C）

## D. 实验、指标与消融

robomimic MH 的 Lift、Can、Square 每任务三百条，better/okay/worse 各一百，质量为1/2/3；这是操作者组标签，不是逐帧专家真值。Franka 的 PenInCup六十条、DishRack八十条，半数由人故意加入掉物、绕行或抖动，质量0/1；用外部与腕相机。RoboCrowd 为 ALOHA 双臂真实新手众包，HiChew、TootsieRoll各四十条、HersheyKiss一百条，并比较含/不含无关play的版本，质量0–3（§VI-A、图3）

图4–7横轴是移除轨迹数，纵轴是剩余数据人工平均质量。曲线好说明筛选更接近该标签，不能当策略成功率；图最右只剩约10%数据，也不代表建议如此激进删除。与 VIP、Compatibility、Uncertainty、InfoNCE、MINE 比较时，DemInf 在图像、小样本更稳定；不确定性适于主动补采，不一定适于离线保留高质量样本

下游 robomimic 图像 BC 训练十万步，每个三种子各两百 rollout，共六百次；Can/Square比较不同删除量，Square MH1000再加七百条 Diffusion Policy 成功rollout。DemInf多种设置超过全数据，说明策略收益，但结果依赖过滤量与数据组成（图8）

真机删除50%，同时与全数据和随机保留50%比较；RoboCrowd训练ACT、每配置十次，以抓起、交还、开包装计1/2/3分；Franka训练Diffusion Policy、十五次二元成功。因此图9左侧不是成功率，右侧才是。DemInf优于随机子集，但 PenInCup 全数据稍好，且 VIP 在故意构造的低质 Franka 数据上也很强（图9及正文）

消融显示一定范围 k 与潜变量维度、VAE β 较稳，KSG 比简单分开估熵或 BiKSG 更好。没有证明任何近邻统计都会奏效，也没有证明人工质量相关就必然带来同幅策略提升（图10–11、附录 A）

## E. 不足、当前平台复用与未来

**作者明确局限：**时间动力学关联未充分建模；可预测停顿可能得高分；先打分再删是贪心，删除后分布和互信息会变；假定示范成功；多任务可能只保留容易任务，需分离任务条件（§VII-A/B）。因此它不能替代成功检测、任务标注或传感器完整性检查

**我的推论：**VAE 忽略细微接触会让近邻失真，多峰正确解法也可能被当噪声，分数对绝对/相对动作、采样率敏感。对 D435i＋DH116，先离线核对图像/状态/动作时间戳、停顿、丢帧、单位、三指耦合与成功标签，再在同任务同动作表示内试评分，并保留随机子集与全量对照。DH116六主动轴/十一总自由度不能按夹爪空间直接混入，左手仿真资产也不能代替右手标定

当前整手/多轴仍锁定、根因未知，近期只做日志、运动学与仿真数据审计，不因高分就允许执行。评分不要求先买新手套或机械臂；后续扩大双臂数据才涉及额外硬件和标定。图像VAE与策略训练需要 GPU/云计算预算，可先用低维状态小集验证排名稳定性，再投入视觉训练与人工质量审核

## 来源与核验边界

- arXiv v3 全文19页，实看方法图1（p.4）、下游图8（p.8）、真机图9与消融（p.9），核对局限p.10与附录实现
- [RSS 2025 正式记录与 DOI](https://www.roboticsproceedings.org/rss21/p023.html)确认录用；[官方 MIT 文件](https://github.com/jhejna/demonstration-information/blob/main/LICENSE)已核验
