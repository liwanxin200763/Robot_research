# Towards Efficient and Robust Manipulation via Multi-Frame Vision-Language-Action Modeling

## 基本信息

- 作者：Hao Li、Shuai Yang、Yilun Chen、Xinyi Chen、Xiaoda Yang、Yang Tian、Hanqing Wang、Tai Wang、Dahua Lin、Feng Zhao、Jiangmiao Pang
- 年份：2026
- 发表 venue：AAAI 2026（正式论文）
- 论文类型：会议论文；多帧 VLA 模型与鲁棒性基准
- 研究方向：VLA；多帧观测；遮挡鲁棒性；长时序操作
- 关键词：CronusVLA；Feature Chunking；Cross-Frame Decoder；SimplerEnv-OR
- 论文链接：[AAAI 正式论文](https://ojs.aaai.org/index.php/AAAI/article/view/38903)
- DOI：[10.1609/aaai.v40i22.38903](https://doi.org/10.1609/aaai.v40i22.38903)
- arXiv：[2506.19816](https://arxiv.org/abs/2506.19816)
- 项目主页：[CronusVLA 项目页](https://lihaohn.github.io/CronusVLA.github.io/)
- 代码：[官方 GitHub](https://github.com/InternRobotics/CronusVLA)
- 本地 PDF：[[00_论文池/PDFs/01_VLA/CronusVLA.pdf|查看 PDF]]
- 引用量：22
- 引用量来源：Google Scholar

## 详细摘要

### 1. 研究背景

单帧 VLA 在遮挡和干扰下易失去阶段信息；直接输入多帧会增大 VLM 自注意力成本及部署延迟。（论文第 1 节）

### 2. 论文要解决的问题

把单帧预训练模型高效扩展为多帧 VLA，并量化时间／空间观测扰动下的鲁棒性。（第 1、3 节）

### 3. 之前方法存在的问题

直接多帧拼接导致速度下降；从头训练时序模型难充分利用单帧大规模预训练；原有基准缺少观测鲁棒性量化。（第 1–2 节）

### 4. 核心思路

两阶段训练：单帧数据学基础视觉语言动作能力，随后跨具身多帧后训练；缓存各帧紧凑特征，再由跨帧解码器生成动作块。（第 3 节，图 2）

### 5. 方法与系统结构

预训练时用 256-bin 离散动作 token 自回归；后训练把每帧 VLM 输出改为可学习连续特征，在推理中用 FIFO 维持 feature chunk。DiT 跨帧解码器、当前／历史特征调制和多帧正则完成动作生成；不是无需训练的插件。（第 3.1–3.2 节）

### 6. 输入信息

单视角 RGB 多帧历史和任务语言；每帧独立经 VLM 编码后特征融合，主方法并未把显式 Proprioception 作为核心记忆输入。（第 3 节）

### 7. 输出 / 动作表示

阶段一离散动作 token；阶段二跨帧解码器生成连续动作块，面向不同机器人具身映射。（第 3 节）

### 8. 数据来源与采集方式

大规模机器人示范用于单帧预训练，跨具身数据用于后训练；真机 Franka 每任务约 50 条遥操作轨迹，并以每任务 25 次测试评估。（第 3–4 节；附录 F）

### 9. 数据处理与数据增强

后训练在 batch 维重构多帧序列，在线缓存旧帧特征；SimplerEnv-OR 设计 24 种观测扰动、120 种强度。训练数据增强细节另见附录，不能将基准扰动误称为全部训练增强。（第 3.2–3.3 节）

### 10. 训练方式

先进行单帧动作 token 自回归预训练，后在跨具身多帧数据上训练视觉语言骨干和动作解码器，并加多帧正则；7B 与 0.5B 配置均报告。（第 3–4 节）

### 11. Benchmark 与实验设置

SimplerEnv、LIBERO、SimplerEnv-OR 和 Franka 真机；对比 OpenVLA、CogACT、TraceVLA、RoboVLMs、SpatialVLA、DP3、π0 等。SimplerEnv-OR 另测时间和空间扰动。（第 4 节，表 1–5）

### 12. 真机实验

Franka Research 3 第三人称相机，覆盖简单抓放、顺序按键、多个物体操作和相机遮挡／干扰；长程任务中的重复按键是单帧基线的典型状态混淆。（第 4.2 节，图 4；附录 F）

### 13. 主要实验结果

SimplerEnv 平均成功率 70.9%、推理约 8.73 Hz；直接多帧后训练基线为 32.4%／3.09 Hz，完整方法为 70.9%／8.73 Hz（表 4）。论文还报告 LIBERO 较 OpenVLA 提升 26.8%、真机平均成功率 72.6%；各数值应按其原评测设置解读。（摘要，第 4 节）

### 14. 消融实验

单帧基线 31.0%，直接多帧 32.4%，加解码器 48.2%，训练骨干 67.2%，再加正则 70.9%（表 4）。7B 最优约 7 帧，0.5B 最优约 4 帧；更多历史不一定更好（图 5）。

### 15. Failure Case

附录 G 图 20 明列：杂乱场景中单第三人称视角导致杯子抓取位置反复调整；远处抽屉深度估计不准；遮挡下缺少显式避障使机械臂碰走目标；仿真中罐子被轻触即不合理滚动。论文有个别重试成功示例，但不能概括为通用故障恢复。（附录 G）

### 16. 主要局限

作者在附录失败案例指出单视角、深度估计、遮挡避障与 sim-to-real 差距。多帧观测鲁棒性不等于具有故障原因识别或自主重规划。（附录 G；后一项为文献库分析）

### 17. 与已有工作的关系

相对 TTF-VLA 的免训练相邻令牌融合，CronusVLA 通过多帧后训练形成特征缓存与动作解码器；相对 ContextVLA，它强调跨帧动作块和观测扰动评测。（第 2–4 节）

### 18. 对当前研究方向的价值

SimplerEnv-OR 和附录 G 提供明确执行干扰、遮挡和失败类型，可用来设计错误检测与恢复测试；其自身仍主要解决感知鲁棒性。（第 3.3、4 节；附录 G）

### 19. 一句话总结

CronusVLA 用单帧预训练加多帧后训练及特征缓存提升 VLA 性能与遮挡鲁棒性，仍暴露深度、避障及 sim-to-real 失败。

## 我的阅读笔记

已读 arXiv 作者 PDF 正文与附录 G；AAAI 正式题名及 DOI 据官方论文页核验，PDF 为同论文公开作者版。
