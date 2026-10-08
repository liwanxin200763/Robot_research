---
paper_id: P047
title: "TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies"
---

# P047 · TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies

## 基本信息

- 作者：Ruijie Zheng、Yongyuan Liang、Shuaiyi Huang、Jianfeng Gao、Hal Daumé III、Andrey Kolobov、Furong Huang、Jianwei Yang
- 年份：2025
- 发表 venue：ICLR
- 论文类型：会议论文
- 研究方向：VLA
- 关键词：Visual Trace Prompting；CoTracker；时空感知；OpenVLA；运动轨迹
- 论文链接：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8667f264f88c7938a73a53ab01eb1327-Abstract-Conference.html)
- DOI：—
- arXiv：[2412.10345](https://arxiv.org/abs/2412.10345)
- 项目主页：[项目主页](https://tracevla.github.io/)
- 代码：[GitHub](https://github.com/umd-huang-lab/tracevla)
- 本地 PDF：[[00_论文池/PDFs/01_VLA/TraceVLA.pdf|查看 PDF]]
- 引用量：313
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

只看当前图像的 VLA 容易忽略机器人刚刚如何移动及物体是否被推动；直接堆叠多张历史图像又带来大量冗余视觉 Token。（论文第 1、3.1 节）

### 2. 论文要解决的问题

在不改动原有低层动作接口的前提下，把短期运动历史压缩成 VLA 易读取的视觉提示，提高相机视角、背景、干扰物和新目标变化下的操作成功率。（第 1、3 节）

### 3. 之前方法存在的问题

OpenVLA 的单帧输入缺少运动记忆；直接输入 6 帧历史图像在论文消融中从 40.2% 降到 34.2%。仅把轨迹写成文本虽然有用，却多约 150 个文字 Token，效果弱于把轨迹画到图像上。（第 3.1、4.3 节，图 7–8）

### 4. 核心思路

用 CoTracker 从最近 6 帧追踪运动明显的点，挑 5 条点轨迹画到当前画面；将原图与画有轨迹的图同时输入 VLA，让模型直观看到近期末端和物体的运动方向，再预测动作。（图 1–2；第 3.1 节）

### 5. 方法与系统结构

图像历史 → CoTracker 密集点追踪 → 筛出运动超过阈值的点 → 采样并绘制彩色视觉轨迹 → 与未覆盖原图、语言指令经分隔 Token 一起送入 OpenVLA 视觉语言主干 → 输出动作 Token。保留原图是为了避免轨迹遮挡夹爪或目标物；训练时随机丢弃轨迹以应对追踪失败。（第 3 节，图 1–2）

### 6. 输入信息

当前 256×256 RGB 画面、最近约 6 帧图像历史和自然语言指令。点轨迹由历史图像计算，非额外深度或真实机器人状态传感器。视觉提示与原始图像同时输入。（第 3–4 节）

### 7. 输出 / 动作表示

继承 OpenVLA 的离散化末端动作 Token，表示位置/旋转增量和夹爪动作；视觉轨迹是输入提示，而非模型预测的未来轨迹，也不是独立的高层规划结果。（第 2–3 节）

### 8. 数据来源与采集方式

在 BridgeData V2 与 Google RT-1 机器人数据上计算视觉轨迹，合计约 **15 万条**带轨迹提示的操作轨迹；另为真机 4 个任务各采集 30 条示范，共 120 条。7B 主干在 Open X-Embodiment 预训练，4B Phi-3-Vision 分支另用约 97 万条 OpenX 轨迹预训练。不能把这几种数据量相加称为一个同质数据集。（第 3.3 节）

### 9. 数据处理与数据增强

CoTracker 使用 40×40 点网格，选出移动显著的点，再随机采样 5 条，历史窗为 6 帧；训练时对重叠的 12 帧片段做稀疏追踪以节省计算。随机用原图替换轨迹图，增强无追踪结果时的稳健性。附录 C 比较线宽、透明度和颜色，合理范围内性能变化很小。（第 3.1–3.3 节；附录 C）

### 10. 训练方式

在 OpenVLA 7B 基础上追加微调 5 个 epoch；Phi-3-Vision 4B 分支先按 OpenVLA 配方在 OXE 预训练 30 epoch、32 张 H100，然后同样微调 5 epoch。两种分支的对照都在相同数据上做了无视觉轨迹的额外微调，用于隔离轨迹贡献。（第 3.3、4.3 节）

### 11. Benchmark 与实验设置

SimplerEnv Google Robot 测 3 类任务、合计 137 种仿真配置；视觉匹配与变体聚合指标分别关注真实外观对齐和光照、相机、桌面纹理、背景、干扰物变化。基线是 OpenVLA、OpenVLA-Phi3、Octo-Base、RT-1-X。补充材料另在 LIBERO 四套任务测试多任务迁移，每套 10 项、每项 50 条示范。（第 4.1 节，表 1；附录 F）

### 12. 真机实验

固定第三视角相机观察 WidowX-250 单臂，每次输入 256×256 RGB。正文和图 6 共报告 **8 项**真机任务：4 项主任务及 4 项未见物体/目标/指令的追加泛化任务，每项 10 次；除折布外还放置 2–3 个干扰物。附录 A 给出具体成功标准，例如折布要抓住右边并翻向左边，推布要接近桌子右缘 1 英寸内。论文未给统一低层控制 Hz。（第 4.2 节，图 5–6；附录 A）

### 13. 主要实验结果

SimplerEnv 六项指标平均 TraceVLA **47.7%**，OpenVLA **40.2%**；Phi3 版 **44.0%** 对同基座 **39.9%**（表 1）。真机未见的玉米搬运任务 TraceVLA **8/10**、OpenVLA **1/10**（图 6a）；未见 AAA 电池抓取为 **9/10** 对 **4/10**（图 6b）。LIBERO 补充评测平均 **74.8±0.4%**，对应 OpenVLA **70.6±0.4%**（附录表 5）。

### 14. 消融实验

同数据额外微调但不加轨迹，7B 仅由 **40.2%** 到 **41.3%**；加轨迹为 **47.7%**。直接加入 6 帧历史反降到 **34.2%**（图 7）。文本形式轨迹相对基线只增约 2.4 个百分点，视觉轨迹再多约 6.4 个百分点（第 4.3 节）。历史长度 3、6、9、12 帧分别约 43.5%、47.7%、47.5%、46.6%，显示轨迹太短或过长均不理想（图 9）。

### 15. Failure Case

香蕉任务中 TraceVLA 的失败主要是抓取未成功；OpenVLA 有时抓住香蕉却放到盘上而非指令中的盘右侧。轨迹线过密会遮住夹爪或目标，低光下 CoTracker 也可能无法可靠追踪，故作者加入原图与训练时轨迹 Dropout。（第 3.2、4.2–4.3 节；附录 B）

### 16. 主要局限

作者测得额外一张图及 CoTracker 带来开销：每步额外文字/图像 Token 约 0.002 秒、5 点追踪约 0.03 秒、密集点追踪摊销约 0.004 秒；训练时批量 32 的显存差小于 10 GB，但并非免费。作者提出未来仍需预测性轨迹与 3D 点云信息；现有方法只编码**已发生**的 2D 运动，评测仍限单臂真机。（第 5、7 节）

### 17. 与已有工作的关系

TraceVLA 保留 OpenVLA 主干与动作 Token，只在输入侧提供视觉化短期历史；与 SpatialVLA 直接编码 3D 相机空间不同，它不需要深度但依赖点追踪。与把历史堆帧相比，图 7 的对照表明轨迹的选择性表示更有效。（第 3–4 节）

### 18. 对当前研究方向的价值

双臂普通夹爪任务可试验分别标出两只末端和被操作物体的短时轨迹，再与显式状态估计比较；但追踪遮挡、双臂交叉与失败恢复仍须单独验证。论文已有证据主要支持单臂操作和 SimplerEnv 泛化，不支持直接推断双臂成功率。

### 19. 一句话总结

TraceVLA 把近期运动轨迹画在当前图像上作为 VLA 的视觉记忆，让现有模型在多种环境变化和真机操作中更好地利用时空信息。

## 相关论文

- [[Octo - An Open-Source Generalist Robot Policy]]
- [[OpenVLA - An Open-Source Vision-Language-Action Model]]
- [[DROID - A Large-Scale In-The-Wild Robot Manipulation Dataset]]
- [[Open X-Embodiment - Robotic Learning Datasets and RT-X Models]]
- [[SpatialVLA - Exploring Spatial Representations for Visual-Language-Action Models]]
- [[A Survey on Vision-Language-Action Models for Embodied AI]]
- [[Towards a Unified Understanding of Robot Manipulation - A Comprehensive Survey]]

## 来源

- 官方论文：[ICLR Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8667f264f88c7938a73a53ab01eb1327-Abstract-Conference.html)
- 项目主页：[项目主页](https://tracevla.github.io/)
- 官方代码：[GitHub](https://github.com/umd-huang-lab/tracevla)
