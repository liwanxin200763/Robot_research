---
paper_id: P151
title: "OPEN TEACH: A Versatile Teleoperation System for Robotic Manipulation"
authors: ["Aadhithya Iyer", "Zhuoran Peng", "Yinlong Dai", "Irmak Guzey", "Siddhant Haldar", "Soumith Chintala", "Lerrel Pinto"]
year: 2025
conference_year: 2024
venue: "Conference on Robot Learning (CoRL) 2024; PMLR 270 (published 2025)"
arxiv: "2403.07870"
arxiv_version: "v1 (preprint; local PDF is PMLR proceedings)"
pdf: "01 论文文库/PDFs/08_数据与遥操作/OPEN_TEACH.pdf"
verified_on: "2026-10-15"
citation_status: "待 Google Scholar 人工核验"
tags: ["Teleoperation", "Retargeting", "Robot_Data", "Mixed_Reality"]
---

# OPEN TEACH: A Versatile Teleoperation System for Robotic Manipulation

## A. 基本信息与研究问题

完整七位作者与PDF首页、PMLR页核对一致。会议为CoRL 2024，正式论文集于2025年出版，PMLR 270:2372–2395；本地复用24页会议版全文。arXiv 2403.07870v1发表于2024-03-12，为另一版本入口，不能把会议年份、出版年份和预印本日期混写

### 快速摘要

OPEN TEACH解决跨机器人平台示范采集工具昂贵、专有或只支持特定形态的问题。它以Quest 3手/腕跟踪输入，通过可定制映射控制机械臂、夹爪、Allegro或移动机器人；彩色透视与机器人视频提供视觉反馈，记录观察及机器人状态供策略训练。38项遥操作展示说明接口覆盖面，十项策略学习表明数据可用，但不是38项都学会自主策略，更不是一套通用Diffusion/Flow Matching算法（§3–4）

## B. 相关工作与基本机制

ALOHA、GELLO以类似目标机械臂的装置控制机器人，将机械结构约束直接反馈给操作者，但需额外硬件及本体适配。AnyTeleop用视觉感知与优化，支持多本体及仿真；OPEN TEACH沿用统一接口方向，改以商用头显跟踪和混合现实反馈降低外部相机设置负担

Holo-Dex已有VR到Allegro手指映射；本文增加腕到臂、夹爪开关、移动平台包装器，并改善拇指工作区映射。所谓包装器就是把统一的人手关键点转换成不同机器人的原生动作，不保证不同本体具有相同可达空间（§2、3.3）

## C. 核心贡献与方法

### 1. 人手输入与操作界面

Quest 3内置手姿流90 Hz，彩色透视让用户直接看到周围场景，界面另显示机器人相机近景。头显相机已内部标定，减少外部多相机标定，但机器人的坐标、工作区和驱动仍需接入。头显约500美元为论文年代硬件报价，不包含机器人、相机、计算机或触觉设备（图2，PDF p.4）

机械臂用腕点、食指与小指掌指点建立掌平面及法向，腕位置映到末端位置，掌坐标的旋转变化映到末端旋转。普通夹爪用小指—拇指捏合触发状态切换；移动Stretch改用食指—拇指捏合，腕前后、上下和左右运动分别映到伸臂、高度及底盘移动（§3.3）

### 2. 灵巧手重定向和操作者控制

非拇指关节直接对应，忽略Allegro没有的小指；拇指用指尖位置映射后求逆运动学。相较Holo-Dex多个二维分区，本文用一个覆盖全工作区的大区域，越界时投影到最近边界以减少停滞与跨区抖动，并加入垂直掌面的高度映射（附录5.1.2、图4，pp.14–15）

提供暂停让用户重新摆手再恢复，以及降低运动分辨率/缩放的精细操作模式。它们帮助人修正姿态，不能替代关节限位、碰撞检查、故障恢复；正文没有完整量化的端到端延迟或各平台失踪帧保护/滤波参数，未报告部分须查驱动及代码

### 3. 通信、数据保存与学习

ZeroMQ连接Detector、Keypoint Transformer、Operator、Controller与Visualizer。Operator同时读目标姿态和实测机器人状态；Controller执行后发布状态；录制进程分开保存RGB/深度/触觉、关节/夹爪状态及时间戳，再按时间戳对齐。控制流频率不等于落盘频率，附录未给统一录制Hz（附录5.1.1，p.14）

Allegro采用重力补偿PD，300 Hz输出力矩；Franka用Deoxys，xArm用官方API，Jaco与Stretch各用已有控制器。表1中Franka-Allegro/Jaco-Allegro为60 Hz、双xArm夹爪90 Hz、Stretch5 Hz，Allegro模拟60 Hz、LIBERO20 Hz；不能将“最高90 Hz”套到全部平台

真机Franka-Allegro记录视觉＋Xela触觉，以TAVI示范引导残差RL学习；Allegro模拟用FISH，LIBERO模拟用Transformer BC＋GMM头及动作块。不同环境使用不同算法和传感监督，因此平均成功率衡量数据用途，不等于统一策略性能（§4.2）

## D. 实验、结果与证据边界

### 覆盖面与策略学习

六种配置包括四真机和两模拟。双xArm、Stretch等展示了长时遥操作，如双臂做三明治、插USB和移动开门；人持续观察并纠错完成，不应写成这些任务都已自主完成或从模拟迁移（§4.1/4.5、附录图5–10）

正文表2（PDF p.7）真机四任务用3/6/4/6条示范，分别开盒9/10、抓海绵7/10、拾茶包7/10、抓物扭转8/10。Allegro模拟三任务为10/10、10/10、7/10；LIBERO为10/10、9/10、9/10，十任务合86/100，即86%

附录表7（p.23）另报模拟每任务三种子、每种子25试次：Allegro翻块0.97±0.03、翻海绵0.79±0.05、捏取0.75±0.07，LIBERO关抽屉0.96±0.03、开炉0.95±0.04、放汤罐0.77±0.02。它与正文十次结果不是同一统计协议，不混算；项目页87%也不覆盖正文86%的口径

### 新用户研究

15名新用户先练习10分钟，任务顺序随机，每人约参与三任务、每任务五次，并非每人完成所有方法所有任务。因基线缺少可用臂重定向代码，Holo-Dex/AnyTeleop只对比无需臂运动的翻块和捏取；其余任务只有OPEN TEACH，不能据此宣称臂任务全面胜过基线（§4.6、附录表5）

表3汇总新用户翻块成功率三法均1，完成时间中位数为Holo-Dex6.58 s、AnyTeleop13.71 s、本文5.5 s；捏取成功率0/0.2/0.8。表3却在Holo-Dex捏取0成功时列17.49 s“成功示范中位耗时”，与附录无成功标记存在解释冲突，本卡不使用该耗时推优势。正文称新用户成功率为专家的76%、耗时2.25倍，是汇总描述而非每个任务定律

## E. 不足、项目联系与未来

**作者明确指出：**头显遮挡会降低关键点质量，有时手指识别错误令捏合关闭夹爪失灵；改进手姿跟踪可改善易用性（§5）

**我的分析：**包装器灵活也把本体约束与安全责任留给接入者；手势误触发应单独统计。真实学习含触觉及残差RL，不是纯人类裸手视频即可直接学会。论文未报告一套完整自主失败恢复机制，也没有统一端到端算力和数据量预算

**D435i＋DH116最低验证：**优先复用异步时间戳记录、暂停/分辨率设计和离线受限重定向。DH116右手六主动轴、十一总DOF需要独立耦合、关节排序和三指工作区模型，不能照搬Allegro或左手仿真资产。当前整手/多轴运动锁定、故障根因未知，仅做D435i离线观测、仿真与日志

完整复现需要Quest 3及SDK、目标臂/手和相机，TAVI还需触觉及在线训练；GPU型号与完整学习耗时预算未明确报告。双臂可先复用手腕映射与双客户端结构，另验证双臂碰撞及同步，不暗示当前已支持实机臂手联动

## 来源与全文核验

- [PMLR正式论文页](https://proceedings.mlr.press/v270/iyer25a.html)、[官方会议版PDF](https://raw.githubusercontent.com/mlresearch/v270/main/assets/iyer25a/iyer25a.pdf)
- 本地全文：[[01 论文文库/PDFs/08_数据与遥操作/OPEN_TEACH.pdf|查看 PDF]]，24页，核对正文§1–5、附录5.1–5.3、图2/4、表1/2/3/5/7
- [arXiv预印本及版本](https://arxiv.org/abs/2403.07870)、[项目页](https://open-teach.github.io/)、[官方代码](https://github.com/aadhithya14/Open-Teach)，代码MIT许可，数据/模型许可分别待核验
- 引用量：待Google Scholar人工核验，旧卡数字不作当前核实结果；核验日期2026-10-15
- 关联路线：[[02 研究方向/机器人遥操作与动作重定向]]、[[02 研究方向/机器人数据采集与数据质量]]
- 保留相关综述入口：[[Towards a Unified Understanding of Robot Manipulation - A Comprehensive Survey]]
