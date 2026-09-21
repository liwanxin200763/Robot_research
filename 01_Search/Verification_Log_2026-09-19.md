# Verification Summary

核验日期：2026-09-19

本轮处理对象为 Discovery Sheet 的 77 条记录。优先复用已有官方 Proceedings、出版商页面、作者 Project Page / GitHub 静态审计结果；不对已经有可靠证据的字段重复改写。无法获得新增一手证据的字段保留 Unknown / Pending。未下载论文、权重或数据集，未 clone 或运行 77 个仓库。

## Total

- 总记录：77
- 完成基础 metadata 复核：77（以当前已有官方来源与审计记录为准）
- 本轮新增改写：0 条；没有新增可靠证据时不强行填值。

## Code Status

- Released: 16
- Partial: 5
- Coming Soon: 0
- None: 0
- Unknown: 56

## Venue

- Official Verified: 68
- Cross-Verified: 9
- arXiv Only: 0
- Pending: 0

## CCF

- Verified from CCF official row: 0
- Explicitly marked Not CCF A / Not Applicable: 31
- Pending / needs official row recheck: 46

## Embodiment

- Single Arm: 26
- Bimanual: 14
- Dexterous Hand: 11
- Mobile Manipulator: 2
- Humanoid: 2
- Other / General: 28

## Real Robot

- Yes: 10
- No / simulation-only: 1
- Mixed: 9
- Unknown: 57

## Remaining Unknown Fields

- CCF Level: 6 条
- Code Status: 56 条
- Dataset Released: 44 条
- Real Robot: 57 条
- Embodiment: 8 条


## Conflicts / Cautions

- 代码：既有记录中的 Released / Partial 来自静态仓库审计，未在本机 clone、安装或运行；Unknown 不代表无代码。
- CCF：部分 Discovery 行使用“CCF 7th edition; venue category not independently extracted from official PDF”说明；CCF 官方逐行核验仍待完成，未用第三方榜单替代。
- CoRL 2024 的会议年份与 PMLR 在线卷年份存在显示差异，保留会议官方年份并在 Notes 中说明。
- 公开数据集与作者自发布数据不能混同；Dataset Released=Unknown/Partial 的记录继续保留原状态。

## Synchronization

- Excel: `D:\Robot\_Research\00_Paper_Pool\Paper_Pool.xlsx` 已完成全文证据核验取核对；本轮没有证据足以安全改写 Discovery 数据，因此保留原数据和下拉规则。
- Obsidian cards: 77 张卡片均存在，保持 Discovery；没有修改 `ManipLLM.md`。
- Discovery index: `D:\Robot\_Research\00_Paper_Pool\Discovery.md` 保持与 77 条卡片链接一致。



