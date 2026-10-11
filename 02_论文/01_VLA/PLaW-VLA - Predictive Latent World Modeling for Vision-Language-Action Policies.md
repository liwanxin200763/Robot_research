---
paper_id: P183
title: "PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies"
---

# P183 · PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies

## 基本信息

- 作者：Yu Liu、Hetian Guo、Tianlv Huang、Ziyi Cai、Wudi Chen、Hantang Wang、Qiutong Liu、Yingzhi Peng、Wei Han、Peijun Tang、Jianan Wang、Zipei Fan、Zhiyuan Zha、Xuan Song
- 年份：2026
- 发表 venue：CoRL 2026（作者项目页及 arXiv 标注已接收；正式论文集待核对）
- 研究方向：VLA、预测式世界模型、长程操作、泛化、双臂操作
- 论文链接：https://arxiv.org/abs/2610.12285
- DOI：10.48550/arXiv.2610.12285（arXiv DOI，注册待完成）
- arXiv：2610.12285
- 项目主页：https://rainyrobo.github.io/PLaW-VLA/
- 代码：https://github.com/RainyRobo/PLaW-VLA （训练与 LIBERO 示例已公开；本模型预训练 checkpoint 尚未发布）
- 本地 PDF：[[00_论文池/PDFs/01_VLA/PLaW-VLA.pdf|查看 PDF]]
- 引用量：
- 引用量来源：

## 研究问题与方法

视觉—语言—动作策略若只依赖当前画面，长程任务中缺少对后续场景的预期；直接预测完整未来图像又耗费计算，并会关注与控制无关的视觉细节。PLaW-VLA 在冻结的 V-JEPA 2 表征空间预测任务相关的未来状态，以 Mixture-of-Transformers 连接语言／观测专家、潜在世界模型专家与连续动作专家，使用结构化因果注意力让动作读取历史、语义及预测未来。（§1、3，图 2）

训练分三阶段：无动作视频学习潜在未来预测；机器人轨迹联合训练预测与动作；最后对具体任务微调。与单纯把世界模型放在策略旁边不同，未来潜变量直接条件化动作生成。代码仓库已提供三阶段训练管线，但官方 PLaW-VLA 预训练 checkpoint 仍待发布。（§3；官方代码 README）

## 实验、结果与消融

LIBERO 四套任务平均成功率 **97.4%**，π₀.₅ 为 **96.9%**；其中 LIBERO-Long 为 **94.6%** 对 **92.4%**。零样本 LIBERO-Plus 七类扰动加权平均 **72.7%**；相同表中的 WorldVLA 为 **25.0%**，但不同方法的预训练与结构并非完全受控。RoboTwin 2.0 的 50 项任务中，Hard Horizon III 为 **79.2%**，π₀.₅ 为 **67.4%**，差 **11.8 个百分点**。（§4.1，表 1–3）

真机使用轮式双臂人形机器人执行叠毛巾、收玩具、投篮与整理文具；各模型每任务同用 400 条示范、10 种空间配置各 3 次。作者项目页给出原始成功率与零样本变体，但论文正文将任务进度作归一化评估；因此不能把项目页的成功率直接等同于正文的进度分数。（§4.2，图 4；项目页）

消融中，去掉未来预测损失使 LIBERO-Plus 从 **72.70%→67.56%**，去掉未来条件使其降至 **69.81%**；改用重建导向的 Cosmos VAE 表征为 **70.93%**；推理时屏蔽所有未来状态令 LIBERO 从 **97.40%→93.05%**。在不使用第一阶段视频预训练、其余数据预算匹配的比较里，去掉预测世界模型使 LIBERO-Plus 从 **69.05%→65.49%**，把表征学习的额外数据优势与预测机制区分开。论文还报告相近性能下，相对生成式世界—动作建模约 **1/19** 的推理延迟。（§4.3–4.4，表 4）

## 失败案例与局限

**作者所述：**执行轨迹偏离会损害未来状态预测，错误预测又可能经未来条件动作放大偏差；需要不确定性估计、可变预测时域和恢复机制。无动作视频到机器人控制的规模效应仍缺乏足够多样的训练数据验证。（§6）

**文献库分析：**长程增益在 RoboTwin 随机化困难设置中较清楚，但尚不能证明模型会检测并修复真机执行误差。把未来预测与错误监测、物理反馈或场景恢复结合，需单独测试误预测后的闭环行为；当前模型 checkpoint 缺席也限制直接复现实验。

## 关联阅读

[[02_论文/07_泛化与长程任务/DreamTrue - Action-Faithful Robot World Model with Counterfactual Post-Training|DreamTrue]] · [[02_论文/01_VLA/Taming VLAs under Robot Execution Errors - Self-Compensation and Stress Testing|Taming VLAs]]
