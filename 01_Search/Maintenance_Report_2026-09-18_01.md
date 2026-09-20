# 首批候选论文增量维护报告

操作日期：2026-09-17。
工作簿：D:\Robot\_Research\00_Paper_Pool\Paper_Pool.xlsx。

## 1. Venues

更新原有 CVPR、ICCV、NeurIPS、ICML、AAAI 五行；新增 ACL、IJCAI、ICRA 三行。ICLR 所有数据保持不变。

按本次用户提供值登记 AAAI A、NeurIPS A、ACL A、CVPR A、ICCV A、ICML A、IJCAI A、ICRA B。以上是用户提供值，不是本次已完成官网核验的结论。

来源保留：
- https://www.ccf.org.cn/Academic_Evaluation/AI/
- https://www.ccf.org.cn/Academic_Evaluation/By_category/

两个入口本次均返回 HTTP 405，未读取到官方正文。未改用博客、旧榜单或第三方目录。Verification_Status 均为 `Official source provided / website access pending recheck`，CCF_Edition 为 `2026年第七版`。Verified_Date 按用户要求登记为 2026-09-18，并在 Notes 明确这不是本次核验成功日期。

IJCAI=A 与此前第七版 B 类记录存在冲突，已在 Notes 单独警示；不能据此将 IJCAI 论文认定为核心合格论文。后续需回到第七版正式目录裁定。

Notes 已添加 Full / Regular Paper 逐篇核验要求，以及 Workshop、Demo、Short Paper、Technical Brief、Summary、Findings 不能直接套用依附会议等级的说明。原 Notes 文字保留并追加本次登记信息。

## 2. Papers 新增四篇

|ID|论文简称|正式发表|Reading_Level|Code_Status|
|---|---|---|---|---|
|P0001|ManipLLM|CVPR 2024|L1|Partial|
|P0002|ManipTrans|CVPR 2025|L1|Released|
|P0003|DexHandDiff|CVPR 2025|L1|Partial|
|P0004|AR-VRM|ICCV 2025|L1|Released|

完整标题、用户指定 Category/Subcategory、官方论文入口、项目页面和 GitHub 已录入。四篇均按本次要求作为 L1 候选，不表示核心资格、代码可运行性或完整复现已经通过审核。

四篇正式条目来源：
- https://openaccess.thecvf.com/content/CVPR2024/html/Li_ManipLLM_Embodied_Multimodal_Large_Language_Model_for_Object-Centric_Robotic_Manipulation_CVPR_2024_paper.html
- https://openaccess.thecvf.com/content/CVPR2025/html/Li_ManipTrans_Efficient_Dexterous_Bimanual_Manipulation_Transfer_via_Residual_Learning_CVPR_2025_paper.html
- https://openaccess.thecvf.com/content/CVPR2025/html/Liang_DexHandDiff_Interaction-aware_Diffusion_Planning_for_Adaptive_Dexterous_Manipulation_CVPR_2025_paper.html
- https://openaccess.thecvf.com/content/ICCV2025/html/Yang_AR-VRM_Imitating_Human_Motions_for_Visual_Robot_Manipulation_with_Analogical_ICCV_2025_paper.html

代码状态与用户初始清单的两处差异：
- ManipLLM：官方仓库公开训练/测试实现，但 README 明确说明公开推理不含 chain-of-thought，且公开测试数据不同于论文数据。为区分发布覆盖范围，记 Partial，未运行验证。https://github.com/clorislili/ManipLLM
- DexHandDiff：README 明确说明是部分官方实现，存在采样入口及模型/引导源码，记 Partial，未运行验证。https://github.com/Liang-ZX/DexHandDiff
- ManipTrans：已查看实际训练入口，目录包括残差策略、环境和测试使用说明，记 Released；部分手型 URDF 受许可限制，已记入 Notes。https://github.com/ManipTrans/ManipTrans
- AR-VRM：已查看 train.py 和模型实现，目录含 evaluate.py，记 Released；不表示完整依赖、权重或运行结果已经确认。https://github.com/idejie/ar

各行 Notes 保存本次检查日期和官方仓库 commit。Released 仅说明有实质实现公开，不等于已经复现论文所有实验。

## 3. Rejected 新增两篇

- CoT-VLA：真实原因 Code_Not_Verified，Notes 包含 `Code release not yet verified`。
- RoboGround：真实原因 Partial_Code，Notes 包含 `Partial release; full training/evaluation release requires recheck`。Partial 为用户提供的待复核状态，不冒充本次完整代码检查结论。

现有 Reason 列表既无上述两个值，也无 Unknown。按用户允许的兼容处理，两行用合法值 No_Code 占位，Notes 明确它不代表已经确认无代码；未更改原下拉规则。两篇官方 CVF 论文链接已录入，Code_Link 因本次未确认而留空。

## 4. 留空字段

Papers 四行以下字段未填写：Problem、Gap、Method、Contribution、Robot_or_Hand、Single_or_Bimanual、Real_Robot、Observation、Action_Space、Dataset、Benchmark、Checkpoint、Dataset_Released、Reproducibility、Relevance、Verified_Date。原因：本次不开展内容精读或运行复现，不根据标题推断；已在 Notes 标明待人工核验。

新增 ACL、IJCAI、ICRA 的 Full_Name 留空待核验。Rejected 两行 Code_Link 留空待核验。

## 5. 验证与保护

- 编辑前保存原始工作簿：`99_Templates/_maintenance_20260918_01/Paper_Pool.before.xlsx`。
- 增量保存前校验原文件哈希，确认工作期间源文件没有被其他程序改动。
- 检查四个工作表、六篇标题去重、ID、代码状态和 L1；重复论文数为 0。
- 原有数据验证、条件格式和冻结窗格保持一致；Keywords 数据及布局保持一致；ICLR 数据保持一致。
- 原有非目标单元格值逐一比对通过。目标 Venue 的更新获得本次请求授权，原值可在备份和 Notes 中追溯。
- 表格范围扩展为 Papers A1:AC5、Rejected A1:H3、Venues A1:I10；Keywords 保持 A1:D23。
- 调整新增内容相关行高和 Notes 列宽，检查渲染无内容截断。工作簿完整性检查和错误扫描通过。
- 中途发生一次终端字符编码错误和一次保存时文件句柄占用，均已修复；最终文件保存成功，无遗留 Excel 数据验证或格式错误。
- 没有下载 PDF、没有 clone 四篇论文代码、没有运行模型，没有生成摘要或填写 Problem/Gap/Contribution，没有自动提升至 L2/L3。

## 6. 后续入库规则

本次 L1 仅为候选略读级别。以后认定核心论文仍必须满足：2024–2026 正式 CCF A Full/Regular Paper、与机器人操作/VLA/灵巧操作或双臂方向相关、存在实际可访问的官方实质代码。Partial 需确认可实际运行和公开范围；本次两个 Partial 均未通过运行确认。

只有项目页、空仓库、README、Coming Soon、To be released、网页源码或无核心实现的零散模型文件，不能标 Released。Code_Status 的五个合法值不变。来源不确定的字段留空并记录待核验。

此前 README 和 Venue_List.md 为初始化记录；本次候选级别和更新状态以本报告及工作簿 Notes 为准，历史文件未被覆盖。
