# 引用量维护

论文卡中的 `引用量`由用户手工维护。每张卡只保留：

```markdown
- 引用量：—
- 引用量来源：Google Scholar
```

`引用量来源`是此后人工维护的统一字段值；历史数字并未在本次字段清理中重新核验。请先在 Google Scholar 人工确认论文身份和引用量，再直接修改对应论文卡的 `引用量`。本工具不联网、不读取历史缓存来覆盖论文卡数字，也不会自动修改任何引用量。`citation_cache.json` 和旧审计文件仅作历史记录，不再参与日常写回。

新加入的论文若依照具体任务从 OpenAlex 或 Semantic Scholar 的身份匹配记录核得明确整数，可以如实填写该来源，并保留来源链接、查询日期和核验状态。2026-10-01 加入的 ACE-Ego-0 即按 arXiv DOI 精确匹配 OpenAlex，返回明确的 0。来源未收录、请求失败或返回空值时应填 `—`，绝不能换算为 0；本地排序仍只读论文卡中的 `引用量`，不会联网重新查询，也不会更改已有人工数字。

本地维护命令：

```powershell
python .maintenance/citation/citations.py clean          # 预览字段清理
python .maintenance/citation/citations.py clean --apply  # 仅清理字段结构和来源
python .maintenance/citation/citations.py render         # 直接读取论文卡数字生成排序页、CSV 和待核验页
python .maintenance/citation/citations.py validate       # 检查引用量、来源和可核验来源证据
python .maintenance/citation/test_citations.py -v
```

原 `bootstrap` 和 `update` 命令已停用，以免恢复旧缓存或覆盖人工填写的数字。排序页把数字按降序排列，将 `—`、空白及其他非数字内容放在末尾；待核验页列出这些条目及尚待人工确认的 Google Scholar 0 值，不回写论文卡。已由身份匹配 API 明确核验的 0 保留在排序页，但不列入待人工确认区。
