# Sim2Real 专题检索与核验记录（2026-10-10）

## 版本与安全

- 修改前 Git HEAD：`60c30ab792ccccc4d1b09621aafed2091aa65e21`。
- 修改前目标索引及 Git 状态的本地备份：系统临时目录 `sim2real-prechange-2026-10-10`；不包含或覆盖用户已有工作区修改。
- 本轮开始前已有未提交的 `00 开始这里.md` 修改、两处论文池文件删除、`文献阅读.drawio` 删除，以及 `.maintenance/reading/temporal_memory_batch_2026-10-04.md` 和 `.maintenance/research_gap/` 未跟踪内容；均留待原任务处理，不在本批提交。
- 新增 PDF 从官方开放页面获取，许可再分发尚未核验，留在本地并由 Git 忽略。

## 本轮全文核验

| 编号 | 来源与版本 | 实际阅读范围 | 状态 |
| --- | --- | --- | --- |
| P179 | https://arxiv.org/abs/2603.22876；v2，2026-06-29 | 27 页；§1–5、表 1–3，附录实验设置和表 4–8 | 全文已读；官方代码链接未确认；论文仿真/真机本体表述待作者资料澄清 |
| P180 | https://arxiv.org/abs/2609.31770；v1，2026-09-24；https://github.com/hesd10/astra-robot-sim2real | 23 页；§1–9、表 1–2、附录表 3–6、真机判定注释；官方 GitHub README 和目录核对 | 全文已读；12 次真机“成功”仅是操作员确认接触 |
| P181 | https://arxiv.org/abs/2606.31101；v1，2026-06-30；https://wzx16.github.io/index.html | 3 页全文、表 1、图 1–3 | 全文已读；CVPR 2026 Embodied AI Workshop，非主会；官方专属代码未确认 |

## 主卡复查与专题边界

- P172 RoboTwin 2.0、P145 DexMimicGen、P152 RDGen：现有卡片记录了真机实验和来源章节，属于实质 Sim2Real 实验；原主分类和手填引用量保持不变，仅增加专题说明。
- P001 Sim2Real-VLA、P094 Sim-and-Real Policy Co-Training、P095 Simulation-Guided Fine-Tuning、P096 视觉灵巧操作 Sim2Real RL：属于核心方向，但旧卡片的实验细节仍有摘要级缺口；专题不补造数值。
- P053 π0.5：验证未见真实场景，旧卡片并未证明直接“仿真训练→真机”迁移，暂不归入专题。
- P171 RoboTwin 1.0：旧卡片描述数字孪生与现实数据，但直接迁移实验细节不足；列为复查候选。
- RSS 2026 Reactive Catching（https://roboticsproceedings.org/rss22/p148.html）官方页面可核对题名、作者、DOI `10.15607/RSS.2026.XXII.148`；当前 PDF 入口返回网页，未合法取得有效 PDF。本轮不建主卡，下次换官方/作者入口后再核全文。
- CoRL 2025 Human2Sim2Robot（https://proceedings.mlr.press/v305/lum25a.html）官方会议摘要已查，尚未读全文；列为候选，不建主卡。

## 下次继续

1. 从上述两个候选的正式 PDF 和本地 PDF 下载状态开始，按题名/arXiv/DOI 复查重后再决定收录；不要重建 P179–P181。
2. 深读 P001、P094、P095、P096 的本地 PDF，补 baseline、每任务真机数值、代码状态；不碰人工引用量。
3. 对 P179 核验公开评测平台地址和仿真 Cobot Magic / 真机 Piper 的配置对应关系。若官方澄清，再更新卡片。
4. DH116 实验规划中明确接触检测、指尖力阈值和多指关节校准，不把夹爪任务表现直接外推到灵巧手。
