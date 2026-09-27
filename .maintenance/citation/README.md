# 引用量维护工具

本目录的 `citations.py` 只维护论文卡中的引用量及其索引，不读取或修改 PDF、摘要、Excel。项目采用现有中文 Markdown 字段；`引用量状态` 维持“已核验 / 待核验”显示，新增 `引用量查询状态` 保存最近一次请求的技术状态，`OpenAlex Work ID` 保存已确认的身份。

## 首次迁移与日常使用

在仓库根目录运行：

```powershell
python .maintenance/citation/citations.py bootstrap --dry-run
python .maintenance/citation/citations.py bootstrap
python .maintenance/citation/citations.py validate
python .maintenance/citation/citations.py update --offline
python .maintenance/citation/citations.py update
```

`bootstrap` 从已核验的 `CITATION_FULL_AUDIT.csv` 把 116 个 OpenAlex Work ID 和 134 篇现有数值装入 `citation_cache.json`；可重复执行，但遇到缓存与卡片数值不一致会停止，不用旧审计覆盖新结果。`update` 默认只请求到期论文，先直接按保存的 Work ID 查询；无 ID 时依次尝试 DOI、arXiv 对应 DOI、完整标题搜索。`--offline` 只列出到期条目；`--force` 忽略刷新周期；`--limit N` 限制当次处理数量；`--paper 标题片段` 只处理指定论文。`render` 重新生成现有的排序和待人工核验两页，`validate` 检查数字、状态、ID 与缓存一致性。

刷新周期、超时、请求间隔、最大重试次数和指数退避在 `config.json` 配置。OpenAlex 与 Semantic Scholar 串行访问，不启用无约束并发。Semantic Scholar API key 如有需要，只从环境变量 `SEMANTIC_SCHOLAR_API_KEY` 读取，不写入仓库。Google Scholar 不做批量访问；Crossref 不作为引用量数值源。

## 状态与写入规则

`verified`：身份确认且 API 明确返回正整数。`verified_zero`：身份确认且 API 明确返回整数 0。`pending_identity`：候选无法唯一确认。`not_found`：未收录。`rate_limited`：HTTP 429。`api_error`：HTTP 5xx 等服务异常。`network_error`：超时或网络异常。`parse_error`：成功响应缺少合法引用量字段或 JSON 解析失败。`suspicious_decrease`：候选新值低于现有已核验值。`pending`：尚未查询。

任何失败都只更新最近查询状态与技术日志，不覆盖已有可信数值、来源和核验日期。`suspicious_decrease` 保留旧数值并进入待人工核验页。未查到、`null`、字段缺失都显示 `—`，不会转换为 0。`citation_cache.json` 同时按卡片、OpenAlex Work ID 与 DOI / arXiv 别名保存身份及数值；查询事件追加至 `query_log.csv`。缓存与两张用户页面可由脚本更新，历史审计表保留作初次迁移证据。

运行回归检查：

```powershell
python .maintenance/citation/test_citations.py -v
python .maintenance/citation/citations.py validate
git diff --check
```
