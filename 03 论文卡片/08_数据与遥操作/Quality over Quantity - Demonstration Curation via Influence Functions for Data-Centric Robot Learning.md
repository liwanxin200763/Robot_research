---
paper_id: P206
title: "Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning"
authors: ["Lee, Haeone", "Min, Taywon", "Kim, Junsu", "Kang, Sinjae", "Liu, Fangchen", "Pinto, Lerrel", "Lee, Kimin"]
year: 2026
venue: "ICRA 2026"
arxiv: "2603.09056"
arxiv_version: "v1"
pdf: "01 论文文库/PDFs/08_数据与遥操作/QoQ.pdf"
verified_on: "2026-10-15"
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Data_Curation"]
document_type: "会议论文（已接收）"
preprint_platform: "arXiv"
first_public_date: "2026-03-10"
first_public_month: "2026-03"
first_public_scope: "arXiv v1 submission history (UTC)"
latest_preprint_date: "2026-03-10"
latest_preprint_version: "v1"
publication_status: "已接收；正式出版记录待核验"
published_venue: "IEEE ICRA 2026（官方日程已核实）"
affiliations: ["KAIST", "University of California Berkeley", "New York University"]
metadata_verified_on: "2026-10-17"
metadata_sources: ["https://arxiv.org/abs/2603.09056", "https://arxiv.org/pdf/2603.09056v1", "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html", "https://github.com/rl-max/quality_over_quantity"]
conference_month: "2026-06"
---

# Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning

## 出处与版本

- 文献类型：会议论文（已接收）
- 预印本平台与编号：[arXiv 2603.09056](https://arxiv.org/abs/2603.09056)
- 首次公开日期：2026-03-10；首次公开月份：2026 年 3 月，依据 arXiv v1 提交历史（UTC）；本字段不宣称已穷尽项目网页或其他平台可能更早的公开记录
- 最近预印本版本：v1，日期 2026-03-10；当前未记录后续修订
- 当前发表状态：已接收；正式出版记录待核验
- 正式发表出处：[IEEE ICRA 2026（官方日程已核实）](https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html)
- 会议月份：2026 年 6 月；不是录用通知日期
- 日期与状态说明：官方日程列 2026-06-04 的 ThI2I.153，arXiv comments 标明 Accepted to ICRA 2026；日程不是正式出版 DOI，不据此编造出版日或录用通知日
- 作者所属机构：KAIST；University of California Berkeley；New York University
- 机构依据：Haeone Lee、Taywon Min、Junsu Kim、Sinjae Kang、Kimin Lee：KAIST；Fangchen Liu：UC Berkeley；Lerrel Pinto：NYU，正文首页与官方日程一致；[对应版本 PDF 首页](https://arxiv.org/pdf/2603.09056v1)
- 项目主页：[作者项目页](https://github.com/rl-max/quality_over_quantity)
- 官方代码：[作者链接的仓库](https://github.com/rl-max/quality_over_quantity)；入口存在不等于已核实完整实现、模型或许可，开源边界沿用下文说明
- 信息核验日期：2026-10-17；来源为官方版本历史、正文署名和上述正式条目；引用量沿用原 Google Scholar 人工核验规则

## 论文简介

一条示范“看起来顺”未必最适合当前策略，某些已成功数据也可能与目标任务无关。QoQ 把数据价值定义成：提高它的训练权重后，能否帮助模型降低高质量验证示范上的损失，从而按当前学习目标挑选数据

它用影响函数近似训练样本对模型的作用，不必为每条数据完整重训一次。对一个状态—动作样本，先找它最能帮助的验证样本，再把同条轨迹的影响汇总，整条选择而非只摘取好看的帧。这比按视觉相似度取片段更注意动作前后联系，也不同于只按成功或失败做二元过滤（§III–IV）

论文包含仿真和 Franka 真机。图 2 的真机香蕉任务，QoQ 训练出的策略成功率均值为 86.7%，全数据为 36.7%；是真机三次独立运行的平均，单次评估回合数未清楚报告，不从百分比反推次数。表 I 另列的 83.6% 是所选状态—动作对来自成功轨迹的比例，两种指标不可混用

对我们，先收集少量可信的 DH116 目标验证示范，再判断哪些遥操作数据真正有助于目标抓取，是比无条件追求数量更具体的路线。但验证集可能遗漏新的可行抓法，影响估计也依赖模型和计算预算。将 D435i 的物体状态、手指接触和失败原因纳入验证覆盖是研究设想，不能直接沿用二指 Franka 的动作接口或成绩

## A. 基本信息与研究问题

- 作者：Lee, Haeone; Min, Taywon; Kim, Junsu; Kang, Sinjae; Liu, Fangchen; Pinto, Lerrel; Lee, Kimin
- 年份：2026
- Venue：ICRA 2026
- arXiv：[2603.09056v1](https://arxiv.org/abs/2603.09056v1)
- DOI：[10.48550/arXiv.2603.09056](https://doi.org/10.48550/arXiv.2603.09056)
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/QoQ.pdf|查看 PDF]]
- 官方 PDF：[v1](https://arxiv.org/pdf/2603.09056v1)
- 项目主页：https://github.com/rl-max/quality_over_quantity
- GitHub：https://github.com/rl-max/quality_over_quantity
- 代码状态：公开 robomimic 筛选源码；未安装运行，真机全栈待核验
- 引用量：待 Google Scholar 人工核验
- 查询与核验日期：2026-10-15
- 关联：[[02 研究方向/机器人数据采集与数据质量]] · [[02 研究方向/机器人遥操作与动作重定向]]

研究方向：示范质量、目标任务数据选择、模仿学习。**Behavior Cloning（行为克隆）**是把机器人在某个观察下执行的动作作为监督标签；标签中混入抓空、犹豫或错误策略，模型也可能学会这些行为

本篇不设计新遥操作器，而是研究已有示范应该保留哪些。作者把质量定义为“加入这条数据是否有助于降低目标验证示范的学习损失”，让质量随目标任务和当前策略改变，而不只看轨迹是否短、画面是否漂亮（第 1–3 页）

快速摘要：混合示范＋少量理想验证轨迹 → 训练基础策略 → 比较样本梯度 → 按整条轨迹聚合 → 重新训练。关键收益是真机香蕉抓取成功率由最强对照的 56.7% 提高到 86.7%；这不是通用质量保证，也不是直接测量真实成功率的打分器（图 2）

## B. 相关工作

Behavior Retrieval 把状态与动作压缩成特征，再找接近专家的数据；Flow Retrieval 使用图像运动估计得到的光流，比较运动相似性。两者容易把“看起来像”当成“训练后有帮助”，在不同物体或视角下可能检索错

DemInf 用状态多样性和动作可预测性衡量数据；DataMIL 及 CUPID 用**影响函数**近似估计提高某条数据训练权重后，验证误差或闭环回报怎样变化。QoQ 属于后者，但改为对每个训练样本取最相关验证样本的最大梯度相似度，再选择整条轨迹。论文讨论这些方法，不意味着所有方法都进入同一真机对照表（§II、IV）

## C. 核心贡献与方法

### 1. 把“有价值”联系到学习目标

输入训练轨迹中的状态—动作对，以及少量成功验证示范。先用全部训练集学一个基础策略，再分别计算训练样本与验证样本使模型参数改变的方向，即梯度。如果两个方向一致，学习训练样本更可能同时改善验证行为（图 1）

严格影响函数包含表示损失曲率的 Hessian 逆矩阵。作者为降低成本，使用忽略该项的归一化梯度内积近似；高分是估计的有益方向，不是对删除数据后性能的精确因果测量（式 3–6）

### 2. 为什么取最大值而不平均

一次抓取的接近、捏合、移动属于不同阶段。如果把全部验证梯度平均，互不相关的行为可能抵消。QoQ 对一个训练样本寻找最相符的验证样本，取最大内积，再对该训练轨迹所有时间步求均值。最后按轨迹分数选前 N 条，保留完整动作链

只挑高分帧容易留下大量抓住物体的瞬间，却丢掉到达物体或移走物体的过程。整轨迹筛选减轻这种阶段偏置，但也会把一条轨迹中的坏片段一起留下（§IV-B）

### 3. 算力与重新训练

作者只计算部分网络层的梯度，用 OPORP 随机投影压缩向量，尽量保留内积关系。仿真对 Transformer 模块计算，真机对 GR00T N1 动作头计算；后者使用流匹配损失梯度，而非声称能直接获得精确动作概率

流程：同步观察／动作轨迹 → 划出验证集 → 基础模型训练 → 梯度评分与整轨迹选择 → 微调或重训 → 独立部署评估。输出是数据子集和训练后的策略，不直接输出遥操作控制命令。筛选预算通常对应成功轨迹数；未知时作者取一半，并建议比较多个预算（第 4 页）

### 4. 失败数据怎样利用

没有额外专家验证集时，先运行策略，分别保留成功和失败 rollout。对成功参考的支持应加分，对失败参考的支持减分，并按验证样本量加权。失败轨迹因此既可作为被剔除的监督，也可提供负向判断依据；这不等于把失败动作原样当正确标签训练（§V-D）

## D. 实验与结果

仿真使用 Robomimic 的易拉罐放置任务；真机是 Franka Research 3，包含香蕉抓取、多物体抓放与开柜。仿真训练 1000 epoch；真机 GR00T N1 用 LoRA 训练 2 万步，DROID 异质数据实验为 5 万步且不用 LoRA。相机型号、采集频率、端到端控制延迟和完整 GPU 预算在本文中未报告

### 筛选指标与策略指标分开

仿真候选为 100 成功＋100 失败，验证集 10 条成功；香蕉候选为 60 成功＋40 失败，另用 10 条成功验证。表 I 的筛选准确率按所选数据中**来自成功轨迹的状态—动作对比例**计算，QoQ 为 99.4%／83.6%，不是机器人部署成功率。文字有按轨迹描述的简写，回查以表注分母为准

图 2 中下游仿真成功率为 99.2%，最强对照 Flow Retrieval 为 76.0%，差 23.2 个百分点；真机香蕉为 86.7%，Behavior Retrieval 为 56.7%，差 30.0 个百分点。图注报告仿真 5 次、真机 3 次独立运行的均值和标准差，单次评估 rollout 数未明确报告，不能从百分比反推

多物体实验用四种物体各 20 条、合计 80 条成功示范，选择一半辅助香蕉目标任务，成功率 93.3%，全部数据为 56.7%。这些源数据原本都成功，说明目标相关性和组合也影响价值，不能简化成只删失败数据

DROID 的 200 条笔／铅笔轨迹中有 133 成功、67 失败，另有 20 条成功验证。图 4 的 78.2% 是筛选准确率，没有在这里报告新策略真机成功率。开柜借助策略反馈筛选，成功率 25.0%→43.3%（图 5）

消融中去掉最大影响评分或整轨迹选择，香蕉策略成功率分别降至 30.0%／26.7%，完整方法为 86.7%；预算改变也会改变结果，不能认为越少越好（图 6、表 III）

## E. 不足与未来

**作者明确指出：**整轨迹选择不能保留好片段而去掉坏片段；影响估计仍近似且昂贵；训练和验证默认同一本体，跨机器人还需扩展（第 7 页）

**本库分析：**验证集决定了“好”的含义，偏向单一抓法可能排除有效少数策略。本文对照的验证处理也不完全一致：仿真 QoQ 去掉无区分力的接近阶段，而检索对照保留该阶段（第 4 页脚注），评价时应记住这一条件

对 DH116，可先用既有仿真或离线日志训练小型行为克隆模型，比较随机选择、动作平滑阈值和梯度评分，按物体与采集批次隔离测试集。D435i 的图像不能替代关节、实际动作和时间戳；当前多轴联动未验收，不直接收集整手真机示范

未来可研究接触阶段的片段选择，并给罕见但成功的纠正轨迹保留配额。需要先评估训练耗时、数据覆盖和闭环成功率，不能仅凭验证损失下降宣布抓取更可靠。官方代码已开放 robomimic 筛选流程，真机全栈与环境配置的可复现程度仍需单独验收


## 来源与核验边界

- 全文第1–7页；图1/2/4/5/6；表I–IV；架构与主要实验页已渲染核对
- 论文许可：http://arxiv.org/licenses/nonexclusive-distrib/1.0/；PDF 沿现有忽略规则仅本地保存，公开仓库提供官方链接
- 正式录用与代码状态仅按以上来源记录；未运行第三方系统，未经人工核验不填引用量

- 会议身份：ICRA 2026 官方日程 ThI2I.153，2026-06-04；[会议条目](https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html)；正式 proceedings DOI 未确认
