# CONTINUE PROMPT

继续维护 `D:\Robot\_Research`，不要重建库。先读取 `01_Search/Verification_Report.md`、`01_Search/Literature_Cleanup_Report.md` 和 `01_Search/Robotics_Core_Search_Log_2026-09-19.md`。

下一轮只处理材料性未决项：

0. 先确认 Excel 已关闭。比较 `00_Paper_Pool/Paper_Pool.xlsx` 与备份哈希；若未发生并发修改，把 `00_Paper_Pool/Paper_Pool.pending_aews_20260919.xlsx` 复核后发布为正式文件，并再次执行 reopen、公式错误和 sheet/行数检查。不要在目标文件仍被占用时覆盖。
1. 从 CCF 官方第七版原文逐行核验 ICLR、IJCAI、ICRA、IROS、T-RO、RA-L 的等级与类别，并保存页码/条目证据。不要沿用旧榜单缓存。
2. 用户确认项目采用的严格 CCF A 口径后，决定 Sim2Real-VLA 是否进入 `CCF_A_Library`；确认前保留在 Robotics Core / Important Papers，CCF Level=Unknown。
3. 补核 `Reactive_Multiarm_Coordination` 的作者信息，以及 Robotics Core 新卡的代码/数据/权重可用性；Unknown 不改为 No。
4. 若继续扩展 venue，按 venue × year × topic 记录 query、候选、正式来源与排除理由，不以数量为目标。
5. 每次修改前检查备份和工作簿并发变化，使用同一 canonical card，不复制阅读笔记。
