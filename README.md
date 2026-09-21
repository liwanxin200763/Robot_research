# Robot Research Literature Library

这是一个面向机器人学习研究的文献库，使用 Obsidian Markdown 组织论文卡片、分类索引和阅读笔记，并使用 Excel 保存结构化元数据。

主要方向：

- VLA（Vision-Language-Action）
- Robot Manipulation
- Bimanual Manipulation
- Dexterous Manipulation
- Sim2Real
- Diffusion / Flow / IL / RL
- Generalization / Long-horizon
- Robot Data / Teleoperation

## Start Here

首先查看 [Home.md](Home.md)。

## Obsidian

1. Clone 或 Download 本仓库。
2. 打开 Obsidian。
3. 选择 **Open folder as vault**。
4. 选择仓库根目录。
5. 从 `Home.md` 开始浏览。

## Structured Database

结构化数据库位于：

`00_Paper_Pool/Paper_Pool.xlsx`

Excel 用于去重、筛选、统计和维护结构化字段；Obsidian 用于日常浏览、论文卡片、分类入口、内部链接和阅读笔记。

## Library Structure

- `00_Paper_Pool/`：正式主库、候选池、开源候选与 Excel 数据库
- `01_Search/`：检索记录、关键词和核验报告
- `02_Papers/`：按主分类存放的 canonical paper cards
- `03_Reading_Notes/`：阅读笔记
- `05_Benchmark_Dataset/`：Benchmark 与 Dataset 记录
- `06_Taxonomy/`：研究方向索引
- `07_Gap_Idea/`：研究问题、差距和待验证想法
- `99_Templates/`：长期复用的模板

## Evidence and Verification

论文卡片不等于已经完成全文证据核验。`Discovery` 表示仅完成元数据或摘要级整理。代码公开也不等于已经在本地成功复现。

每张主卡包含 `Citation Metrics`、结构化研究字段和证据边界。引用量及来源见 [Citation_Update_Log.md](01_Search/Citation_Update_Log.md)，字段覆盖率见 [Literature_Field_Completeness_Report.md](01_Search/Literature_Field_Completeness_Report.md)。

正式发表状态、代码状态、数据和实验信息应回到论文 Proceedings、作者项目页和官方代码仓库核验。缺少证据的字段保留为 `Unknown`，不根据论文标题或二手资料推断。

## Scope

仓库公开维护研究索引、结构化元数据和原创阅读记录。第三方论文 PDF、模型权重、数据集、克隆的第三方 Git 仓库、本地应用状态和历史备份不纳入版本控制。
