# 引用量维护

论文卡只显示 `引用量` 与 `引用量来源：Google Scholar`。用户人工填写的数字是唯一排序依据；空白或 `—` 不等于 0。工具不联网，不读取旧缓存回填，也不会更改论文卡中的引用数字。

历史 API ID、来源链接、查询日期、状态及旧来源记录保存在 Vault 外内部工作区的 `.maintenance/citation/card_metadata_archive.csv` 和原有审计文件中，仅供内部追溯。技术查询信息不得重新写回论文卡。

本地命令：

```powershell
python -B .maintenance/citation/citations.py render
python -B .maintenance/citation/citations.py validate
python -B .maintenance/citation/test_citations.py -v
```

`render` 从当前工作区的主卡读取引用量，生成排序页、CSV 和待人工核验页；`validate` 检查两项可见引用字段。`bootstrap` 和 `update` 已停用。

默认内部工作区为 `D:\Robot_Internal\Research`，可通过 `ROBOT_RESEARCH_WORK_DIR` 指定其他 Vault 外目录。`render` 只将正式排序页写回文献库，CSV 与待核验清单写入内部工作区

旧卡缺少引用量时，排序将其显示为“待核验”，不会补成 0；缺少来源时明确标注来源缺失，不伪称 Google Scholar 已核验。重复字段仍拒绝生成，避免静默采用错误值。重建时保留已有显示标题，目标始终来自主卡实际路径，不从显示标题猜文件名

链接静态检查工具为 `.maintenance/validate_links.py`，可检查一个页面、多个页面或整目录；报告路径必须在当前 Vault 外。文件名中的 `2.0` 按真实文件解析，不误判成扩展名；重名短链接标为歧义，需改为完整路径。此检查只证明文件目标有效，不能代替 Obsidian 阅读模式的真实点击测试
