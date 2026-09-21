# Obsidian Structure Migration Report（Obsidian 结构迁移报告）

日期：2026-09-19

## 结果

- Canonical paper cards：**132**；初次统一后位于单一主卡目录，现已按 Primary Category 迁移到 `02_Papers` 下的 11 个分类文件夹。
- 标准化标题重复组：**0**。
- 检查 Wikilinks：**762**；broken：**0**。
- Taxonomy indexes：**8**。
- Home 的 8 个 Research Taxonomy 入口：**通过**。
- 旧论文实体/方向目录残留：**0**。
- 旧 Card 目录 Wikilink 残留文件：**0**。
- Sim2Real-VLA：**唯一主卡且 Special Attention / Evidence Level 保留**。
- Research Summary：74 张；Summary Evidence：74 张；Evidence Level：132 张。

## Taxonomy 数量

| Index | 论文数 |
|---|---:|
| VLA | 31 |
| Robot_Manipulation | 130 |
| Bimanual_Manipulation | 27 |
| Dexterous_Manipulation | 29 |
| Sim2Real | 5 |
| Diffusion_Flow_IL_RL | 72 |
| Generalization_LongHorizon | 34 |
| Data_Teleoperation | 29 |

分类为多标签，同一论文可出现在多个索引中，数量不能相加当作唯一论文总数。

## 旧目录处理

- `Bimanual`、`Dexterous_Hand`、`VLA` 原为空目录，已移入可恢复归档。
- `Robot_Manipulation` 中的 ManipLLM `paper.pdf` 和 `supplementary.pdf` 已随原目录完整归档：**通过**。
- `CCF_A_Cards`、`Discovery_Cards`、`Robotics_Core_Cards` 的卡片迁入统一目录后，原空目录已归档。
- 归档位置：`D:\Robot\_Research\99_Archive\obsidian_restructure_20260919`。
- 修改前备份：`D:\Robot\_Research\99_Archive\obsidian_restructure_backup_20260919_220410`；包含 `manifest.json` 和 SHA-256。
- 文件迁移映射：`D:\Robot\_Research\99_Archive\obsidian_restructure_20260919\migration_mapping.json`。

## Excel

本轮没有修改 `Paper_Pool.xlsx` 或其论文内容。之前生成的 pending workbook 中如果含 Canonical Card Path，路径同步留待正式发布前处理，避免改动仍被占用的工作簿。

## 最终目录树

```text
D:\Robot\_Research
├─ 00_Paper_Pool
│  ├─ CCF_A_Library.md
│  ├─ CCF_A_OpenSource_Shortlist.md
│  ├─ Core_Papers.md
│  ├─ Discovery.md
│  ├─ Priority_Reading_List.md
│  └─ Robotics_Core_Library.md
├─ 02_Papers
│  └─ Paper_Cards                 (132 张唯一主卡)
├─ 03_Reading_Notes
│  └─ ManipLLM.md
├─ 06_Taxonomy
│  ├─ VLA.md
│  ├─ Robot_Manipulation.md
│  ├─ Bimanual_Manipulation.md
│  ├─ Dexterous_Manipulation.md
│  ├─ Sim2Real.md
│  ├─ Diffusion_Flow_IL_RL.md
│  ├─ Generalization_LongHorizon.md
│  └─ Data_Teleoperation.md
└─ 99_Archive
   ├─ obsidian_restructure_backup_20260919_220410
   └─ obsidian_restructure_20260919
```
