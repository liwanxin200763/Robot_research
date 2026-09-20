# Verification Report（验收报告）

日期：2026-09-19  
执行状态：**PASS / AWAITING_USER（Excel 目标文件占用）**

## 验收矩阵

| ID | 项目 | 结果 | 证据 / 实际数量 |
|---|---|---|---|
| AC01 | 基线与范围可追溯 | PASS | 清理报告记录基线、备份和实际路径 |
| AC02 | 重复身份核验 | PASS | 19 组精确标题重复已归并；当前活动卡重复组 0 |
| AC03 | 删除可恢复 | PASS | 永久删除 0；归档 19；完整备份与 SHA-256 manifest 可用 |
| AC04 | Canonical card 唯一 | PASS | 活动卡 132；标题标准化重复组 0 |
| AC05 | Obsidian 链接 | PASS | 检查 397 个 wikilink；未解析 0 |
| AC06 | 多标签分类 | PASS | Classification_Summary 分开统计 CCF A 与 Robotics Core，并声明多标签不可相加 |
| AC07 | Sim2Real-VLA | PASS | 正式 ICLR 2026、唯一主卡、Special Attention 与请求标签证据均记录 |
| AC08 | CCF A 与 Robotics Core 分离 | PASS | Sim2Real-VLA 因 CCF 口径冲突留在 Important Papers；机器人 venue 未自动升级 |
| AC09 | 四类机器人 venue 检索 | PASS | ICRA/RSS/T-RO/RA-L 均有来源、查询、纳入或零新增说明 |
| AC10 | Unknown 未自动改 No | PASS | 新卡缺证据字段保持 Unknown；未批量把 Unknown 改为 No |
| AC11 | 研究摘要证据 | PASS | CCF A 卡 65/65 具有 Research Summary 与 Summary Evidence |
| AC12 | Excel 保真与发布 | AWAITING_USER | 暂存工作簿已重新打开、渲染和错误扫描；目标 Paper_Pool.xlsx 被另一进程占用，未覆盖 |
| AC13 | 阅读笔记保留 | PASS | 03_Reading_Notes/ManipLLM.md 未修改 |

## 实际数量

- 活动 canonical cards：132（CCF A 65、Discovery 58、Robotics Core 新卡 9）。
- 可恢复重复归档：19。
- CCF A Research Summary + Summary Evidence：65/65。
- Wikilink 检查：397；未解析：0。

## 未解析链接

- 无。

## Excel 验证

- 暂存文件：`D:\Robot\_Research\99_Templates\aews_20260919\Paper_Pool.pending_aews_20260919.xlsx`。
- 便于用户查看的副本：`D:\Robot\_Research\00_Paper_Pool\Paper_Pool.pending_aews_20260919.xlsx`。
- 重新打开后的 sheet：Papers、Rejected、Venues、Keywords、Discovery、CCF_A_Library、Robotics_Core_Library。
- CCF_A_Library：65 条，A:AT；Robotics_Core_Library：13 条，A:AJ。
- 公式错误扫描：0 个匹配；两个更新 sheet 已渲染预览。
- 原目标 `Paper_Pool.xlsx` 被另一进程占用，遵循并发写入停止规则，没有替换或覆盖。关闭 Excel 后需再次比较目标哈希，再把暂存文件发布到正式路径。

## Authority 与限制

- 发表身份/摘要：CVF、NeurIPS、AAAI、RSS 官方 proceedings，IEEE Xplore，ICLR proceedings/OpenReview。
- Sim2Real-VLA：ICLR 官方论文索引、accepted OpenReview PDF、官方项目页、官方 GitHub。
- CCF 等级：项目现有口径与“第七版”说法存在材料性冲突，且 CCF 官网正文访问受限；未静默改写严格库定义。
- 未下载 PDF 集合、未 clone 论文代码、未执行复现实验；`Released/Partial` 仍是静态资源状态，不等于本机复现成功。
