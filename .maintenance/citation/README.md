# 引用量维护

论文卡只显示 `引用量` 与 `引用量来源：Google Scholar`。用户人工填写的数字是唯一排序依据；空白或 `—` 不等于 0。工具不联网，不读取旧缓存回填，也不会更改论文卡中的引用数字。

历史 API ID、来源链接、查询日期、状态及旧来源记录保存在本目录的 `card_metadata_archive.csv` 和原有审计文件中，仅供内部追溯。技术查询信息不得重新写回论文卡。

本地命令：

```powershell
python .maintenance/citation/citations.py render
python .maintenance/citation/citations.py validate
python .maintenance/citation/test_citations.py -v
```

`render` 从当前工作区的主卡读取引用量，生成排序页、CSV 和待人工核验页；`validate` 检查两项可见引用字段。`bootstrap` 和 `update` 已停用。
