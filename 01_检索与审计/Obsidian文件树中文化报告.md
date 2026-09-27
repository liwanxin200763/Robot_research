# Obsidian 文件树中文化报告

核验日期：2026-09-27。重命名之前已生成完整映射并检查大小写不敏感的目标路径冲突。

- 根目录已重命名：13
- 论文主分类子目录已重命名：10（`01_VLA` 保留正式术语）
- 论文主卡文件已重命名：134 / 134
- 常用索引及导航文件名已重命名：33
- Wikilink 目标改写：1850
- Markdown 链接目标改写：12
- 已跟踪维护脚本的路径引用：0（仓库没有已跟踪的维护脚本；文档和 CSV 中的旧路径已改写）
- 目标路径冲突：0
- 断开的 Wikilink：0
- 断开的本地 Markdown 链接：0
- 可用 PDF 链接：130 / 130；全部文件与既有 SHA256 一致
- `Paper_Pool.xlsx`：仅随父目录移动，文件 SHA256 与移动前 Git 版本相同
- 未修改论文正文的快速摘要或全文笔记内容；论文 H1 与英文标题元数据保留

后续引用量核验时发现 3D-VLA 与 DexUMI 的旧归档 PDF 实为其他论文，已更换为核对首页标题的正确版本并更新 PDF 索引与 SHA256。上方“与既有 SHA256 一致”是重命名完成时的检查结果；修正详情见 [[01_检索与审计/引用量修正报告|引用量修正报告]]。

## 首页到 PDF 的 20 条路径抽查

下表逐层验证：`首页.md` → 主题分类页 → 论文主卡 → 本地 PDF 文件，均为实际存在的目标路径。

| 序号 | 分类 | 论文卡 | PDF |
|---:|---|---|---|
| 1 | 机器人操作 | OPEN TEACH：面向机器人操作的通用遥操作系统 | OPEN_TEACH.pdf |
| 2 | 泛化与长程任务 | SPIN：联合感知、交互与导航 | SPIN.pdf |
| 3 | 灵巧操作 | 通过强化学习实现跨本体灵巧抓取 | Cross-Embodiment_Dexterous_Grasping_with_Reinforcement_Learning.pdf |
| 4 | 机器人操作 | 从动作 Token 化视角综述 VLA 模型 | A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective.pdf |
| 5 | 机器人操作 | OWMM-Agent：通过多模态智能体数据合成实现开放世界移动操作 | OWMM-Agent.pdf |
| 6 | 机器人操作 | MoManipVLA：迁移 VLA 模型以实现通用移动操作 | MoManipVLA.pdf |
| 7 | 灵巧操作 | 灵巧抓取 Transformer | Dexterous_Grasp_Transformer.pdf |
| 8 | 泛化与长程任务 | VidBot：从自然场景二维人类视频学习可零样本迁移的三维动作 | VidBot.pdf |
| 9 | 机器人操作 | 面向物体中心机器人操作的具身学习综述 | A_Survey_of_Embodied_Learning_for_Object-Centric_Robotic_Manipulation.pdf |
| 10 | 机器人操作 | 3D-VLA：基于三维视觉—语言—动作的生成式世界模型 | 3D-VLA.pdf |
| 11 | 灵巧操作 | DexHandDiff：面向自适应灵巧操作的交互感知扩散规划 | DexHandDiff.pdf |
| 12 | 泛化与长程任务 | AnyBimanual：迁移单臂策略以实现通用双臂操作 | AnyBimanual.pdf |
| 13 | 泛化与长程任务 | 缓解机器人操作视觉预训练中的人—机器人域差异 | Mitigating_the_Human-Robot_Domain_Discrepancy_in_Visual_Pre-training_for_Robotic_Manipulat.pdf |
| 14 | 机器人操作 | PointMapPolicy：通过结构化点云处理实现多模态模仿学习 | PointMapPolicy.pdf |
| 15 | 泛化与长程任务 | RGMP：融合循环几何先验的多模态策略，用于可泛化人形机器人操作 | RGMP.pdf |
| 16 | 机器人操作 | TwinVLA：以两个单臂 VLA 模型实现数据高效的双臂操作 | TwinVLA.pdf |
| 17 | 泛化与长程任务 | 面向仿真与真实策略联合训练的可泛化域适应 | Generalizable_Domain_Adaptation_for_Sim-and-Real_Policy_Co-Training.pdf |
| 18 | 灵巧操作 | DexCap：面向灵巧操作的可扩展便携式动作捕捉数据采集系统 | DexCap.pdf |
| 19 | 机器人操作 | SurgicAI：面向精细手术策略学习与评测的分层平台 | SurgicAI.pdf |
| 20 | 机器人操作 | RDT-1B：面向双臂操作的扩散基础模型 | RDT-1B.pdf |

## 保留的例外

- 历史备份与第三方参考仓库不重写内部内容，以免改动外部材料；这两类目录的顶层名称已中文化且继续受 Git 忽略。
- Excel 内部的旧路径字符串未改写，因为本轮明确要求不修改工作簿；后续如需在 Excel 中使用新主卡路径，须单独同步。
- 审计计划保留 `old_path` 列，便于核对 Git rename；其他在用文档和 CSV 中未检出旧目录名。
