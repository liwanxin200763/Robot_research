# ContextVLA: Vision-Language-Action Model with Amortized Multi-Frame Context

## 基本信息

- 作者：Huiwon Jang、Sihyun Yu、Heeseung Kwon、Hojin Jeon、Younggyo Seo、Jinwoo Shin
- 年份：2025
- 发表 venue：arXiv 预印本；正式录用信息未核验
- 论文类型：预印本；VLA 多帧微调方法
- 研究方向：VLA；多帧上下文；视觉令牌压缩
- 关键词：ContextVLA；Multi-Frame；Context Token；KV Cache；Amortized Context
- 论文链接：[arXiv 论文](https://arxiv.org/abs/2510.04246)
- DOI：
- arXiv：[2510.04246](https://arxiv.org/abs/2510.04246)
- 项目主页：[ContextVLA 项目页](https://huiwon-jang.github.io/contextvla/)
- 代码：[官方 GitHub](https://github.com/huiwon-jang/ContextVLA)
- 本地 PDF：[[00_论文池/PDFs/01_VLA/ContextVLA.pdf|查看 PDF]]
- 引用量：37
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

当前帧可能无法表明物体是否已移动或目标是否曾被遮挡；多帧有帮助，但把全部图像 token 送入 VLM 会显著增加训练和推理成本。（论文第 1 节）

### 2. 论文要解决的问题

让已有 VLA 有效接收固定窗口的历史视觉上下文，同时维持接近单帧模型的计算量和推理延迟。（第 1、3 节）

### 3. 之前方法存在的问题

直接拼接 8 帧令牌开销高；只看当前帧会丢失长程任务阶段信息；过度池化历史又可能损失可操作细节。（第 2–3 节）

### 4. 核心思路

把历史帧在 VLM 中间层汇聚为紧凑的 context token，保留当前帧的完整视觉令牌，借助因果注意力和 KV cache 复用过去计算。（第 3 节）

### 5. 方法与系统结构

8 帧图像进入视觉编码器和 VLM；论文默认在第 2 个 VLM block 后对每帧历史 token 平均池化，形成历史 context token，并保留当前帧高分辨率 token。因果掩码允许过去表征预计算，动作头仍由原底座承担。（第 3 节、图 2）

### 6. 输入信息

任务语言及当前／历史多帧视觉观测；具体底座可有自己的机器人状态接口，本文的核心增量是视觉历史压缩，不应称其为通用 Proprioception 记忆法。（第 3 节）

### 7. 输出 / 动作表示

兼容 π0、π0-FAST 与 GR00T 等底座；动作生成沿用底座的自回归或 flow-matching 头，并非新的统一动作表示。（第 3–4 节）

### 8. 数据来源与采集方式

仿真使用 LIBERO、SimplerEnv-WidowX（Bridge v2）与 RoboCasa；真机三类任务各收集 50 条演示。（第 4 节）

### 9. 数据处理与数据增强

关键处理为历史视觉令牌池化、因果注意力和缓存；额外数据增强并非论文主要贡献，未单独报告统一方案。（第 3–4 节）

### 10. 训练方式

在既有 VLA 上微调多帧上下文，仿真设置报告 60k 更新、batch 32。需要模型适配和训练，不是 TTF-VLA 式免训练推理插件。（第 4 节）

### 11. Benchmark 与实验设置

LIBERO 40 项任务、SimplerEnv-WidowX、RoboCasa 24 项任务和三类真机任务；比较单帧、直接多帧和压缩多帧方案。（第 4 节，表 1–4）

### 12. 真机实验

覆盖 Clench/Unclench、PnP Twice、CoverNStack 等需要历史信息的任务，每项 20 次测试；报告在 CoverNStack 上 π0 完整 8 帧和单帧均为 45%，ContextVLA 为 60%。（第 4 节）

### 13. 主要实验结果

LIBERO 中 π0 94.6%→96.5%，π0-FAST 93.4%→95.8%，GR00T 95.9%→97.0%；SimplerEnv 中 π0 41.8%→56.2%，π0-FAST 59.0%→70.7%；RoboCasa π0 57.0%→58.7%（第 4 节，主结果表）。8 帧训练比直接完整多帧快 5.5 倍，推理延迟 227.2 ms→96.3 ms（压缩加缓存）。（效率表）

### 14. 消融实验

SimplerEnv 中压缩 context token 的相关消融从 49.0% 提升到 56.2%；第 2 个 VLM block 是论文测试中的最佳压缩位置。缓存进一步降低延迟。（第 4 节）

### 15. Failure Case

论文未单列系统失败案例；部分底座在个别 SimplerEnv 任务并非全面提高。实验不等于证明模型可检测执行错误后自主恢复。（第 4 节）

### 16. 主要局限

主要建模固定长度视觉窗口，未给出分钟级语义记忆或显式失败原因表示；额外微调成本仍在。论文未在结论中给出独立作者局限章节，以上为文献库分析。（第 3–5 节）

### 17. 与已有工作的关系

比直接多帧输入更省算力；与 HAMLET 的 moment token 外部记忆相比，ContextVLA 在 VLM 中间层压缩历史；与 MEM 的长短期双层记忆不同，它重点是摊销式视觉窗口。（第 2–3 节；跨论文比较）

### 18. 对当前研究方向的价值

给执行阶段视觉历史接入现有 VLA 提供效率基线，但若目标是错误诊断与恢复，还需要监督信号或反馈闭环。（第 4 节；文献库分析）

### 19. 一句话总结

ContextVLA 将历史多帧压成少量 context token，在保留当前视觉细节的同时降低多帧 VLA 的训练和推理开销。

## 我的阅读笔记

已核对本地 PDF 的方法、仿真／真机实验、效率与消融；正式会议状态仍需官方页面确认。
