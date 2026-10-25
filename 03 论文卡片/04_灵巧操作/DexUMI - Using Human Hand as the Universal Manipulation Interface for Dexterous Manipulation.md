---
paper_id: P086
title: "DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation"
authors: ["Xu, Mengda", "Zhang, Han", "Hou, Yifan", "Xu, Zhenjia", "Fan, Linxi", "Veloso, Manuela", "Song, Shuran"]
year: 2025
venue: "CoRL 2025; PMLR 305:437-459"
arxiv: "2505.21864"
version: "v2"
arxiv_version: "v2"
arxiv_latest_version: "v3"
pdf: "01 论文文库/PDFs/04_灵巧操作/DexUMI.pdf"
verified_on: "2026-10-15"
citation_status: "待 Google Scholar 人工核验"
tags: ["Dexterous_Manipulation", "Human_Demonstration", "Exoskeleton", "Data_Collection", "Tactile"]
---

# DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation

## A. 基本信息与研究问题

- 作者：Mengda Xu、Han Zhang、Yifan Hou、Zhenjia Xu、Linxi Fan、Manuela Veloso、Shuran Song
- 正式发表：Conference on Robot Learning（CoRL）2025，PMLR 305:437–459
- [正确论文集页](https://proceedings.mlr.press/v305/xu25b.html)｜[arXiv 2505.21864](https://arxiv.org/abs/2505.21864)｜[项目页](https://dex-umi.github.io/)
- 本地 PDF：[[01 论文文库/PDFs/04_灵巧操作/DexUMI.pdf|查看 PDF]]；保留原有效v2，2025-05-29，共22页；已另核正式23页版
- 最新arXiv为v3，2025-10-02；正文方法与主表已与正式版对照。下文PDF页码默认指本地v2，正式版附录分页稍有变化
- [官方代码](https://github.com/real-stanford/DexUMI)公开，MIT；引用量待 Google Scholar 人工核验，旧卡111未经本次人工确认不沿用

DexUMI让人穿外骨骼直接接触物体采集示范，再把人手动作和画面转换为目标机器人手的数据。目标是同时缩小运动学、接触与视觉本体差异，不是用任意裸手视频零样本控制所有手。外骨骼按目标手设计，策略也针对手和任务训练；“Universal”指接口设计原则可复用（§1、3）

## B. 相关工作

UMI用手持平行夹爪对齐采集和部署，但指间协调与手侧接触能力有限；DexUMI把工具扩成可穿戴多指机构，使人仍能直接感受物体。相对视觉重定向先估人手关键点再优化，本文把可行动作约束前移到机械结构和编码器映射，减少纯视觉姿态误差（§2）

DexCap等动捕方案能记录自然手运动，却仍要处理人手与机器人形态差异；同构主从设备采真实机器人数据，又需要现场机器人。DexUMI在采集时不带机械臂，但并非整个流程不需目标手：它仍要标定编码器到电机命令，并让真实手回放动作拍摄外观，才能合成训练视频（§3–4）

## C. 核心贡献与方法

### 1. 让穿戴机构先服从机器人可达性

外骨骼同时追求可穿戴和指尖工作空间相符。双层优化采样机器人与外骨骼构型，最小化两个方向的指尖姿态距离：一项鼓励覆盖目标手工作空间，另一项防止外骨骼产生机器人达不到的姿态；连杆长度、关节位置与限位约束兼顾穿戴，尤其将拇指机构后移避免与人手争空间（p3–4，图2–3、式1）

XHand可从URDF／网格提取几何；Inspire闭环四连杆不能只靠普通树形URDF表达，作者用动捕记录真实指尖轨迹，拟合等效机构。为补偿打印件形变，实际还收紧关节范围、调整尺寸。这是几何和材料共同设计，不是下载目标手URDF便自动完成可穿戴设备（附录C）

### 2. 标定编码器、腕位姿与触觉

每主动关节配Alps电阻位置传感器；因摩擦和回差，编码器角到机器人电机命令非线性，用逐关节成对采样拟合回归。腕6DoF用iPhone ARKit／Record3D，腕下OAK-1相机150°对角视野在采集与部署保持相同安装关系。相机固定于腕不等于整个世界中不能移动，而是不能随意改变相机相对手的位置（p4–5）

人手直接接触产生的是操作者自然触感；策略要使用触觉，还需在外骨骼和目标手装同类型传感器。Inspire用FSR电阻触觉，XHand用磁式阵列；人手触感不会自动成为机器人监督。电阻编码器同时测供电电压做归一化，串口包带头和校验，降低供电漂移及解码失真（附录D）

### 3. 消除人手外观，并保留正确遮挡

SAM2分割人手和外骨骼，ProPainter修补背景；随后把同一关节命令在真实目标手上回放，拍下并分割机器人手图像。再求外骨骼掩膜和机器人手掩膜交集，只把可见的机器人手像素合入背景，避免把手错误贴到物体前方。固定起始手势使SAM2可复用提示点（p5–6，图4）

因此该合成不是纯CAD渲染，更不是仅做绿色遮罩。掩膜漏分、背景模糊、光照差、结构形变和电机回差都会同时影响视觉与动作；合成外观漂亮不等于接触几何已经准确

### 4. 时间管理和策略接口

Inspire采集全部流45 FPS，XHand因触觉不稳定降为30 FPS。保存接收时间后减各传感器延迟得捕获时间；iPhone／相机用滚动二维码测延迟，编码器靠动作回放叠图调齐，再对关节和触觉插值至相机时间，训练前下采样3倍（p22，附录E）

DINOv2视觉CLS与触觉拼接进Diffusion Policy，预测16步“腕6DoF＋手6或12主动维”动作，执行前8步后重观察；训练400 epochs，DINOv2参与更新。策略10 Hz，UR5底层125 Hz，Inspire10 Hz、XHand60 Hz，动作经插值适配。XHand还用累积已执行相对动作的虚拟当前位置减轻弹性工具导致的读数漂移，属于硬件特定补偿，不能不加验证直接移植（p19、22）

## D. 实验与结果

### 数据与主表口径

四种任务、五个手—任务设置为Inspire方块、开蛋盒、镊子夹茶；XHand夹茶与厨房操作。数据分别为方块310条、蛋盒175条、两种手夹茶各400条，厨房370条加单独关旋钮100条。每设置20次评估，初态用参考图对齐；两种手因相机可视范围不同，夹茶初态并非严格一模一样（§5、附录B/E）

| 相对手动作＋触觉＋图像合成 | 最后阶段累计成功率 |
|---|---:|
| Inspire Cube | 100% |
| Inspire Carton | 85% |
| Inspire Tea | 85% |
| XHand Tea | 85% |
| XHand Kitchen | 75% |

五设置算术平均为86%，不能称每种任务／每个阶段都86%。Tea需稳定拿镊子并把至少部分茶叶转入杯；Kitchen为关旋钮、移锅、取盐撒入锅的累计阶段，前段失败后段自动计失败。它们可解释为整链难度，不能和只测独立末阶段的百分比混用（p7，表1；p19）

### 相对动作、视觉和触觉的收益不同

同为带触觉合成图像，手动作改为绝对后，方块100%→10%、Inspire夹茶85%→0%、厨房75%→0%；腕动作两组始终相对，因此该对比不能解释成腕坐标效果。无触觉、相对动作时，蛋盒90%反而高于带触觉85%，Inspire夹茶90%也高于85%，表明触觉噪声会损害部分任务（表1）

厨房取盐对照最清楚：相对动作下去触觉75%→15%，明显力接触能弥补碗口遮挡；镊子只有微弱力信号，收益不稳定。视觉消融在无触觉／相对动作下，蛋盒Inpaint90%、Mask10%、Raw5%，支持外观适配对精确交互的价值，而不是所有任务都相同幅度提升（p7–8，图6）

同一操作者各15分钟采夹茶，DexUMI36条、裸手51条、遥操作11条，约3.2倍效率；这是单任务采集吞吐，未包含外骨骼设计、标定、视频合成与策略训练全部时间（p8，图7）

## E. 不足与未来

**作者指出：**每手都需专用外骨骼和穿戴调参；只匹配指尖，未完整建模手掌接触；打印材料会形变，触觉会受安装和压力漂移影响；图像合成仍需真实手、固定相机关系且有模糊／光照差；目标手回差使同一电机数值受运动方向影响（§7）

**我的理解：**DH116可先做6主动轴、11总自由度的离线耦合与三指工作空间匹配，再决定是否制作机构；不能照抄论文Inspire“12总DoF”或现成XHand映射。当前多轴与臂手控制未验收，不进行命令回放。D435i适合先做外部RGB-D记录和遮挡诊断，替换腕下150°相机后需重建视觉一致性，不能继承86%结果

最小可复用模块是标定数据定义、相对动作、时间戳及图像遮挡检查；完整系统还需定制机构、编码器／采集板、iPhone、腕相机、匹配触觉、目标手和机械臂。论文未给完整一致BOM与GPU墙钟训练预算，应明确待核验，而非据“人手采集”判断低成本即可全复现

## 来源与核验边界

- 本地v2全22页核对§1–7、附录A–E；图2–4和表1已渲染目视核对，并与[正式23页PDF](https://raw.githubusercontent.com/mlresearch/v305/main/assets/xu25b/xu25b.pdf)对照主结果
- 复用原有效PDF，不覆盖或新增同篇正式PDF副本；最新v3的存在与日期已核官方arXiv，不能把本地v2标作v3
- 原卡PMLR xu25a错误指向Stack It Up，现已修正为xu25b；P086及文件路径保持不变
- 官方代码MIT不代表所有第三方模型／数据都同许可；本地预印本登记许可见arXiv，未据代码许可推断PDF再分发权
- 关联专题：[[02 研究方向/机器人遥操作与动作重定向]]；[[02 研究方向/机器人数据采集与数据质量]]

## 延伸阅读：数据采集与可执行示范

- [[03 论文卡片/08_数据与遥操作/ForceMimic - Force-Centric Imitation Learning with Force-Motion Capture System for Contact-Rich Manipulation|P221 · ForceMimic: Force-Centric Imitation Learning with Force-Motion Capture System for Contact-Rich Manipulation]]：机器人外力数据采集、力位混合控制、示范域差异
- [[03 论文卡片/08_数据与遥操作/DexViTac - Collecting Human Visuo-Tactile-Kinematic Demonstrations for Contact-Rich Dexterous Manipulation|P226 · DexViTac: Collecting Human Visuo-Tactile-Kinematic Demonstrations for Contact-Rich Dexterous Manipulation]]：视觉触觉同步、指关节状态、触觉表示预训练
