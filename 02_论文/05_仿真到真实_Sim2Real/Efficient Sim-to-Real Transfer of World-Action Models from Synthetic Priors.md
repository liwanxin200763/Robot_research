---
paper_id: P181
title: "Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors"
---

# P181 · Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors

## 基本信息

- 作者：Zixing Wang; Kausik Sivakumar; Jinghuan Shang; Yafei Hu; Zhaoming Xie; Ran Gong; Xiaohan Zhang; Karl Schmeckpeper
- 年份：2026
- 发表 venue：CVPR 2026 Embodied AI Workshop（作者主页与 arXiv 记录）；**Workshop，不是 CVPR 主会论文**
- 论文类型：三页早期研究结果
- 研究方向：Sim2Real；World-Action Model；合成示范；零样本真机迁移
- 论文链接：[arXiv 正式页面](https://arxiv.org/abs/2606.31101)
- DOI：[10.48550/arXiv.2606.31101](https://doi.org/10.48550/arXiv.2606.31101)（arXiv DOI）
- arXiv：[2606.31101v1](https://arxiv.org/abs/2606.31101)
- 项目主页：[第一作者主页](https://wzx16.github.io/index.html)
- 代码：未核验到本论文专属官方代码；文中使用的 Cosmos Policy、AnyTask 不等于本研究代码已发布
- 本地 PDF：[[00_论文池/PDFs/05_仿真到真实_Sim2Real/Efficient_Sim-to-Real_Transfer_of_World-Action_Models.pdf|查看 PDF]]
- 引用量：
- 引用量来源：Google Scholar（待人工核验）

## 研究问题与相关工作

真实操作示范昂贵，而仿真数据带有视觉和物理域差异。已有 World-Action Model（世界—动作模型：在生成动作的同时预测后续画面）展示过仿真到仿真或真实到真实任务；本文问的是它能否**只用合成示范训练，再零样本部署真机**。这是一项可行性测试，不是证明联合预测目标优于普通动作模型的严格消融。（全文 §1）

## 方法流程

GPU 仿真中随机改变物体/桌面纹理、背景、相机位置、光照和物体初始位置 → AnyTask 的运动规划管线为四项任务各生成约 800 条 RGB—末端动作示范 → 在 Cosmos Policy 视频扩散基础上联合预测后续视觉与动作 → 不收集真机示范、不在真机数据上微调 → 使用腕部和第三人称 RGB 相机部署到 Franka Research 3 并统计任务成功率。（§2.1–2.4）

训练在 **40 张 H100 GPU 上进行约 72 小时、32 个 epoch**。论文仅概述了动作与未来观测的统一扩散表示，缺少足够的训练细节供直接完整复现。域随机化只说明所改变的维度，未提供每维具体取值范围。（§2）

## 实验、Baseline 与结果

四个真机任务各测试 **10 次**：举香蕉 **5/10**，举砖块 **5/10**，开抽屉 **2/10**，把草莓放入碗中 **2/10**；平均成功率 **35%**。Diffusion Policy 使用每任务 10 条真机示范时平均 **5%**，50 条时平均 **25%**。这两组是不同数据来源下的成本参照，**不是同数据量、同架构的受控优劣比较**。（表 1）

图 2 展示模型预测画面与实拍画面的定性对照；图 3 展示一次未见过的瓶子抓取。论文没有给该新物体的多次成功率，也没有分别去掉视频预训练、域随机化、AnyTask 或联合视频—动作预测的消融。作者自己说明归因分析留待后续完整工作。（§2.3–3）

## 局限与 DH116 启发

- 作者说明这是计划发布的完整研究之前的早期结果；当前仅 3 页、4 任务×10 次测试，真实成功率仍有较大提升空间。不能据此宣称通用操作已解决。（首页注释、§2–3）
- 库内分析：Franka 平行夹爪与 DH116 多指接触动力学差异大；昂贵训练与未公布完整代码也限制近期复现。对 DH116 可先借鉴“按任务统计每个真实 rollout、并列呈现纯合成与少量真实数据基线”的评测设计，再测试触觉及关节动作表示，不应直接移植其 35% 数值。

## 关联阅读

[[05_研究分类与路线图/Sim2Real 研究专题|Sim2Real 研究专题]] · [[02_论文/05_仿真到真实_Sim2Real/Grounding Sim-to-Real Generalization in Robotic Manipulation - An Empirical Study with Vision-Language-Action Models|Grounding Sim-to-Real Generalization]]
