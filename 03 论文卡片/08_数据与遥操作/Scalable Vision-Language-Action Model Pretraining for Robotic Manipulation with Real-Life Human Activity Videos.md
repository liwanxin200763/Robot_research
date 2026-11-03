---
paper_id: P243
title: "Scalable Vision-Language-Action Model Pretraining for Robotic Manipulation with Real-Life Human Activity Videos"
short_name: "VITRA"
authors: ["Qixiu Li", "Yu Deng", "Yaobo Liang", "Lin Luo", "Lei Zhou", "Chengtang Yao", "Lingqi Zeng", "Zhiyuan Feng", "Huizhi Liang", "Sicheng Xu", "Yizhong Zhang", "Xi Chen", "Hao Chen", "Lily Sun", "Dong Chen", "Jiaolong Yang", "Baining Guo"]
year: 2026
venue: "ICRA 2026（作者官方仓库标注；正式出版条目待核）"
arxiv: "2510.21571"
pdf: "01 论文文库/PDFs/08_数据与遥操作/Real-Life-Human-Activity.pdf"
tags: ["Human_Video", "Data_Generation", "VLA", "Dexterous_Manipulation"]
---

# Scalable Vision-Language-Action Model Pretraining for Robotic Manipulation with Real-Life Human Activity Videos

## A. 基本信息与研究问题

- 常用项目名称：VITRA。作者：Qixiu Li、Yu Deng、Yaobo Liang、Lin Luo、Lei Zhou、Chengtang Yao、Lingqi Zeng、Zhiyuan Feng、Huizhi Liang、Sicheng Xu、Yizhong Zhang、Xi Chen、Hao Chen、Lily Sun、Dong Chen、Jiaolong Yang、Baining Guo。
- 2025 年 10 月首次公开；[arXiv 2510.21571](https://arxiv.org/abs/2510.21571)，[arXiv DOI](https://doi.org/10.48550/arXiv.2510.21571)。[官方代码库](https://github.com/microsoft/VITRA)标注 ICRA 2026，正式 proceedings/独立 DOI 未核实。
- [论文 PDF](https://arxiv.org/pdf/2510.21571) · [作者项目](https://microsoft.github.io/VITRA/) · [官方代码](https://github.com/microsoft/VITRA) · [公开数据 VITRA-1M](https://huggingface.co/datasets/VITRA-VLA/VITRA-1M) · [公开权重 VITRA-VLA-3B](https://huggingface.co/VITRA-VLA/VITRA-VLA-3B) · [[01 论文文库/PDFs/08_数据与遥操作/Real-Life-Human-Activity.pdf|本地 PDF]]。已核对入口存在，未下载或运行全部数据与权重。
- 引用量：
- 引用量来源：

**问题。** 大量生活视频没有机器人示范常见的“任务开始—结束、逐帧动作、指令”结构。VITRA 研究如何自动把长视频切成可训练的短动作，补上语言和三维人手动作，让人类生活视频用于灵巧 VLA 的预训练。它与 HuRo 的区别是：主要把**人手当作可学习的末端执行器**，再用机器人数据适配；并未把所有原始画面直接渲染成机器人外观。

## B. 作者实际讨论的相关工作

- Ego4D、EPIC-KITCHENS、EgoExo4D、Something-Something V2：原始视频来源，已有动作文字通常太粗或缺少精确时间边界，作者重新自动标注（§3.4）。
- Open X-Embodiment：机器人数据对照，覆盖的手部操作及生活场景与本篇不同（§5）。
- LAPA 隐式动作预训练、VPP 视频生成预训练、π0：在消融与真机实验中比较。它们的预训练数据、架构和目标不完全相同（§5.3）。

## C1. 核心贡献

1. **自动视频转训练数据流程。** 为长视频补相机运动、三维手部轨迹、原子动作边界与命令式语言描述（§3、图 2）。
2. **大规模数据。** 生成约 **100 万个 episode、2600 万帧**；论文报告来源占比为 Ego4D 77%、EPIC-KITCHENS 12%、EgoExo4D 6%、SSV2 5%，未明确说明百分比的分母。episode 是切出的原子动作单元，不是 100 万个独立原始视频（§3.4）。
3. **灵巧手 VLA 训练与适配。** 用人手动作空间预训练，再用少量目标机器人示范微调；实验同时考察数据量与环境多样性（§4–5）。

## C2. 采用的方法

首先校正相机参数与畸变，估计每帧的人手三维姿态及相机轨迹，并把它们放在可比较的空间坐标系。然后找腕部移动速度的局部低点，以此分割抓取、放下等原子动作。**原子动作**是一次相对完整的短操作，不是整段做饭视频。最后挑选片段画面、叠加手部轨迹，用 GPT-4.1 生成动作指令，并剔除无意义片段。论文明确指出来回擦拭可能被速度低点过度切分（§3.1–3.3）。

预训练模型输入图像、语言与当前手部状态，使用扩散动作头预测未来人手动作块；双手缺失标签用 mask 标记。机器人微调时，将目标手部关节映射到人手动作维度，未对应维度不计算损失。这个映射是训练接口，不是直接姿态重定向或真机控制器（§4）。

## D. 实验与结果

- 真机任务包含已见与未见物体的抓放、功能抓取、倒水和清扫。表 3、4 的不同任务试次为 8–40，作者用同一批目标机器人数据微调所有对照方法。
- 已见物体任务平均成功率 **71.0%**，π0 为 46.9%、无 VLA 预训练为 32.1%；未见物体/背景及未见类别平均 **64.6%**，π0 为 16.1%（表 3–4）。这些是作者实验平台上的结果，不代表任意灵巧手。
- 消融：与相同 episode/指令但由 LAPA 隐式动作代替三维动作的预训练比较，后者未见场景平均 0%；作者方法 64.6%。图 10 显示 10%、20%、50%、100% 数据规模增加时，抓放表现整体改善；EgoDex 虽有更多帧，但场景覆盖窄，强调多样性不等于单纯帧数（§5.3）。
- 预训练使用 8 张 H100 约两天，目标机器人微调同规模约 8 小时（§5）。这说明流水线并非低算力即用。

## E. 不足与未来研究

**作者明确的限制（§6）。** 三维重建和语言模型标注仍有错误，需要更好的过滤；当前数据以短原子动作和第一人称视频为主，长程规划及多视角、触觉仍待扩展。真机实验主要为单手，双手交接只作初步展示。

**本库分析。** 对 DH116，可把“视频分段是否正确”“手部姿态是否可信”“能否映射到控制量”分开验收。D435i 画面可用于本地小规模标注实验，但要同步机器人命令、实际关节反馈和时间戳；人手 3D 估计不能直接当机器人的地面真值。NERO 双臂任务需明确左右手相互依赖，单手独立切片可能破坏交接语义。比较 10% 高质量与 100% 混杂视频时，应控制相同模型和机器人示范预算。

**相关阅读。** [[HuRo - Robotizing Human Videos for Scalable VLA Pretraining|HuRo]] · [[Being-H0 - Vision-Language-Action Pretraining from Large-Scale Human Videos|Being-H0]] · [[From Human Videos to Robot Manipulation - A Survey on Scalable Vision-Language-Action Learning with Human-Centric Data|人类视频综述]]。

## 核验范围

阅读 arXiv 全文§1–6、表 1–4、图 2/7/10 和相关附录；代码入口由 Microsoft 官方仓库核对。引用量留给人工核验。
