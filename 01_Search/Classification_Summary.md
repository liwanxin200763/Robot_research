# Classification Summary（分类统计）

统计日期：2026-09-19。严格 CCF A 视图以现有 65 个唯一 ID 为分母；Robotics Core 以 13 个唯一记录为分母。多标签会重叠，以下方向数量不能相加当作唯一论文总数。

## 词表与别名

- Bimanual Manipulation = Dual-arm Manipulation = 双臂操作。
- VLA = Vision-Language-Action；Robot Foundation Model 仅在论文/项目明确使用或主题确切匹配时作为相邻标签。
- Dexterous Manipulation / Dexterous Hand 为灵巧操作扩展线；普通夹爪研究只继承可迁移的方法标签。
- Sim2Real 与 Real2Sim 分开；`Unknown` 不等于 `No`。
- Venue Type、Publication Type、CCF Level 与 Library Membership 分列，互不替代。

## 严格 CCF A 主库（65）

- VLA / Robot Foundation：14
- Bimanual / Dual-arm：13
- Dexterous：17
- Diffusion / Flow：26
- Real Robot = Yes 或 Mixed：24

Venue 分布：NeurIPS 22, CVPR 21, AAAI 13, ICCV 7, ICML 2。

## Robotics Core / Important Papers（13）

- Venue 分布：RSS 7, ICRA 2, T-RO 2, ICLR 1, RA-L 1。
- Bimanual / Multi-arm：5（按唯一 ID 对 Bimanual、Dual-arm、Multi-arm 标签取并集）。
- Dexterous：3
- Sim2Real：2
- VLA：3

## 阅读优先级

当前硬件主线是双臂普通夹爪，因此优先：双臂协同与动作表示 → 示范采集与模仿/扩散策略 → 3D/空间接口 → VLA 与合成数据泛化 → 真机安全与失败恢复。灵巧手条目保留为后续扩展，除非其数据采集、表征或 Sim2Real 方法能直接迁移到夹爪平台。
