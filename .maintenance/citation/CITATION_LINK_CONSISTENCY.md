# Citation / Link Consistency Check

检查日期：2026-09-25

- Canonical paper cards：134
- 每张卡片均含唯一的引用量、来源和查询日期字段：是
- 高置信度匹配：OpenAlex 52；Semantic Scholar 7；未可靠匹配 75
- 未解决引用量均保留为 `—`：是
- 所有外部 URL 已包为 Markdown 链接：是；裸 URL / 格式异常：0
- 确认失效的旧链接：6，均已修正；当前确认 404/410：0
- 自动检查结果：HTTP 200=199；202=5（未视为死链）；403=5（受限/拒绝自动访问，不视为死链）；TLS/网络错误=2（SAGE 页面经官方网页核验可访问，UMass 3D-VLA 项目页待人工复核）
- canonical paper cards 内 Obsidian wikilinks：476；解析为未找到目标：0
- PDF 本地链接：130/130 目标文件均存在；位置均在论文快速摘要之前
- 重复 canonical card 标题：0
- Paper_Pool.xlsx：163 行同步；134 篇卡片引用量、来源和日期逐条匹配；不一致：0
- 工作簿结构：Papers 5×83、Discovery 78×78、CCF_A_Library 66×97、Robotics_Core_Library 14×86，未变
- 已添加 308 个链接公式；公式错误：0
- PDF 目录：130 个可解析 PDF；无效文件：0；SHA256 重复：0；所有文件均由 `.gitignore` 忽略且未被 Git 跟踪
