---
paper_id: P048
title: "TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models"
---

# P048 · TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration for Vision-Language-Action Models

## 基本信息

- 作者：Chenghao Liu、Jiachen Zhang、Chengxuan Li、Zhimu Zhou、Shixin Wu、Songfang Huang、Huiling Duan
- 年份：2026
- 发表 venue：AAAI 2026（正式论文）
- 论文类型：会议论文；免训练 VLA 推理方法
- 研究方向：VLA；相邻帧特征复用；视觉鲁棒性
- 关键词：Temporal Token Fusion；Pixel-Attention；Keyframe；OpenVLA；VLA-Cache
- 论文链接：[AAAI 正式论文](https://ojs.aaai.org/index.php/AAAI/article/view/38910)
- DOI：[10.1609/aaai.v40i22.38910](https://doi.org/10.1609/aaai.v40i22.38910)
- arXiv：[2508.19257](https://arxiv.org/abs/2508.19257)
- 项目主页：
- 代码：[官方 GitHub](https://github.com/PKU-XLab/TTF-VLA)
- 本地 PDF：[[00_论文池/PDFs/01_VLA/TTF-VLA.pdf|查看 PDF]]
- 引用量19
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

连续操作视频的相邻画面有大量静态区域，逐帧重算视觉特征浪费算力；但盲目缓存可能漏掉对任务关键的变化。（论文第 1 节）

### 2. 论文要解决的问题

在不重新训练 OpenVLA 等底座的条件下，利用相邻帧冗余加速或改进 VLA 推理，同时避免动态目标信息被错误复用。（第 1、3 节）

### 3. 之前方法存在的问题

仅按像素差决定复用会忽视语义重要性；仅看语义注意力又可能漏掉实际发生变化的区域。直接多帧输入也增加令牌开销。（第 2–3 节）

### 4. 核心思路

融合灰度像素变化和任务相关注意力：只要任一路提示 patch 应更新，就采用当前帧；否则复用上一帧令牌。周期性 keyframe 抑制累计误差。（第 3 节）

### 5. 方法与系统结构

TTF-VLA 是现有 VLA 的训练免除式推理插件。对前后两帧视觉 patch 构造像素变化和注意力掩码，用 OR 规则形成融合令牌，再交给原动作模型；按固定间隔强制刷新关键帧，典型 K=3。（第 3 节）

### 6. 输入信息

当前与上一时刻 RGB 图像、任务语言和模型内部视觉注意力；不建立跨整段任务的长期语义记忆。论文没有把 Proprioception 作为插件新输入。（第 3 节）

### 7. 输出 / 动作表示

TTF-VLA 不另定义动作空间，仍由所接入 OpenVLA／VLA-Cache 预测原有动作，主要实验为 7-DoF 操作。（第 3–4 节）

### 8. 数据来源与采集方式

使用底座既有训练权重，评估 LIBERO、SimplerEnv 和真机操作；插件本身不采集新训练数据。（第 4 节）

### 9. 数据处理与数据增强

图像灰度差分与注意力 patch 筛选用于在线令牌融合；训练数据增强：不适用，方法无需再训练。（第 3 节）

### 10. 训练方式

推理时接入，不微调底座或新增训练阶段；这是与 ContextVLA、HAMLET 的关键差别。（第 3–4 节）

### 11. Benchmark 与实验设置

LIBERO 每套 200 个 episode，SimplerEnv 和 3 项真机任务；主要对比 OpenVLA、VLA-Cache 及组件消融。（第 4 节，表 1–4）

### 12. 真机实验

3 项任务各 20 次，包含物体操作与抽屉任务；整体均值从 38.3% 到 41.7%，抽屉任务仍为 45%。（第 4 节，表 4）

### 13. 主要实验结果

LIBERO 中 OpenVLA 均值 68.4%→72.4%，Long 为 48.0%→53.5%；VLA-Cache 均值 71.3%→74.0%（表 1）。SimplerEnv 33.2%→34.9%（表 2）；真机 38.3%→41.7%（表 4）。

### 14. 消融实验

LIBERO 中仅像素变化 70.4%，仅注意力 71.3%，二者融合 72.4%（表 3）。关键帧间隔过长（如 K>30）会累积误差。（第 4 节）

### 15. Failure Case

论文未单列系统性失败案例；真机抽屉任务没有提升，关键帧过疏带来性能下降。不能将此法称为失败检测或动作重规划。（第 4 节）

### 16. 主要局限

方法只利用相邻帧复用，缺少长期任务状态与显式执行误差建模；对底座能力仍有依赖。正式论文没有独立作者局限性章节；以上是依据方法与实验的文献库分析。（第 3–4 节）

### 17. 与已有工作的关系

与 VLA-Cache 相比，它额外使用像素变化和语义注意力做当前／历史令牌融合；与长期 Memory VLA 不同，处理的是局部时序冗余。（第 2–4 节）

### 18. 对当前研究方向的价值

可作为部署时低开销的视觉历史利用模块；研究执行误差时仍需独立检测器及恢复策略，论文没有验证这些功能。（第 3–4 节）

### 19. 一句话总结

TTF-VLA 以像素变化加语义注意力免训练融合相邻帧令牌，提高现有 VLA 的任务成功率，但并非长期记忆或失败恢复模型。

## 我的阅读笔记

已核对 AAAI 正式 PDF 的方法、实验、消融、结论；数据来自表 1–4。
