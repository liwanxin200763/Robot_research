# 引用量核验口径（2026-09-27）

- 全部 134 张 canonical 论文卡均重新请求 OpenAlex，并使用论文标题、作者、年份及可用 DOI / arXiv 信息核对身份；本地 PDF 只用于身份核对，不作引用量来源。
- 仅在身份核对通过且 OpenAlex 明确返回整数 `cited_by_count` 时写入引用量。本轮共 116 篇有数值，其中 35 篇由 API 明确返回 0。
- 原有 36 个零中，35 个得到零的明确信号，1 个因身份无法可靠确认改为 `— / 待核验`。`null`、缺字段、无匹配、请求失败均不转成 0。
- 对未确认记录尝试 Crossref DOI 身份查询；本轮无可补充的可靠 DOI 匹配。Crossref 不用作主要引用量来源。
- Semantic Scholar Academic Graph API 的 DOI 测试返回 404，完整标题检索返回 HTTP 429；无合法可用结果，因此未用其请求失败推断数值，也未绕过限流。Google Scholar 未执行批量抓取。
- 工作区维护脚本已搜索默认零写法：`citation = 0`、`citation_count = 0`、`value or 0`、`fillna(0)`、`int(value or 0)`、`get("citationCount", 0)`；未发现把缺失引用量转为 0 的命中。
- 每篇最终数值、来源链接、核验日期和身份匹配原因见 `CITATION_FULL_AUDIT.csv`；原零逐项记录见 `zero_reverification.csv`。
