---
paper_id: P009
title: "DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation"
authors: ["Wang, Chen", "Shi, Haochen", "Wang, Weizhuo", "Zhang, Ruohan", "Fei-Fei, Li", "Liu, C. Karen"]
year: 2024
venue: "Robotics: Science and Systems (RSS) 2024"
arxiv: "2403.07788"
arxiv_version: "v2"
pdf: "01 论文文库/PDFs/08_数据与遥操作/DexCap.pdf"
pdf_source: "RSS 2024 proceedings; existing local official PDF retained"
verified_on: "2026-10-15"
citation_status: "待 Google Scholar 人工核验"
tags: ["Robot_Data", "Motion_Capture", "Dexterous_Manipulation", "Retargeting"]
---

# DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation

## A. 基本信息与研究问题

- 作者：Chen Wang; Haochen Shi; Weizhuo Wang; Ruohan Zhang; Li Fei-Fei; C. Karen Liu
- 年份 / Venue：2024 / Robotics: Science and Systems (RSS) 2024
- [RSS 正式记录与 DOI](https://www.roboticsproceedings.org/rss20/p043.html)；DOI 10.15607/RSS.2024.XX.043
- [arXiv](https://arxiv.org/abs/2403.07788)：当前最新 v2，2024-07-04；核验日期2026-10-15
- 本地 PDF：[[01 论文文库/PDFs/08_数据与遥操作/DexCap.pdf|查看全文]]；[官方 RSS PDF](https://www.roboticsproceedings.org/rss20/p043.pdf)
- 本轮保留已有二十页 RSS 会议 PDF，未重下载；arXiv v2 是线上版本元信息，未宣称本地文件与其逐字相同
- [项目主页](https://dex-cap.github.io/)；[官方 GitHub](https://github.com/j96w/DexCap)，代码 MIT，已见采集/处理/训练模块，未运行或复现实验；数据许可需另查
- 引用量：待 Google Scholar 人工核验；原卡未经本轮核验的数字不沿用
- 关联：[[01 论文文库/专题阅读/机器人数据采集与数据质量]]；[[01 论文文库/专题阅读/机器人遥操作与动作重定向]]

### 研究方向与快速摘要

DexCap 把“无需机器人采集自然人手示范”变成可执行工程系统：手套测手指相对运动，SLAM 追踪腕部与胸部，胸前 RGBD 记录环境，数据统一在世界坐标。DexIL 再把手形与环境转换到机器人空间，用点云扩散策略学习操作，困难任务可加入人在回路纠正。输入是专用可穿戴动捕和三维观察，输出目标腕姿与目标手关节，不是从普通 RGB 视频直接训练（§III–IV）

六项真机任务显示点云表示与纠正数据的价值，但最复杂剪切/泡茶仅靠人类动捕并未完成完整任务。论文同时提供采集系统、转换算法与训练实验，不能把策略收益完全归为手套本身“更高质量”。对本项目，最值得借鉴的是统一坐标、轨迹切分、采样率管理和把采集数据与纠正数据区分

## B. 相关工作与先前不足

相机手姿估计容易被抓物遮挡，IMU 位置积分会漂移；EMF 手套能测手指但缺世界系六维腕姿；固定多相机动捕又不便在不同场景穿戴采集。本文组合三类传感器，不主张某一个传感器解决全部问题（§II–III）

DexMV、VideoDex 等人类视频方法常用视觉/动作先验后再补机器人数据；手持夹爪系统适合平行夹爪，缺多指精细动作。DexCap 用手指几何和三维场景直接构造低层监督，DexIL 用 Diffusion Policy 表达双臂高维动作。它仍有本体差异，尤其人手与 LEAP 的尺寸、指厚、接触力不同，所以保留纠正接口而非声称几何对齐已解决迁移（§II、§IV-C）

## C. 核心贡献与方法

### 1. 硬件、坐标标定与记录

Rokoko 动捕手套提供相对手背 hub 的指尖位置；按论文描述采用 EMF。每只手背安装一台 T265，以双鱼眼＋IMU 的 SLAM 跟踪腕姿；胸部另有一台固定 T265 和 L515 LiDAR RGBD。胸架卡槽给相机已知初始变换，先全部放胸架建图，再把下面两台移至手背固定插槽；胸部主 T265 初始位姿定义世界系。由固定外参把腕姿、手指和环境点云放到共同坐标，不能省略胸部运动补偿（图2、§III-A、附录 A）

采集背包含 NUC 13 Pro、64GB RAM、2TB SSD、40000mAh电源，约四十分钟续航；文中采集系统约四千美元是当时系统预算，不含双臂机器人，也非当前采购价。正文约十秒标定与附录约十五秒准备口径不同，不据此承诺固定用时

关键工程边界是缓存：原始记录60fps，RAM约十五分钟后转SSD会降至20fps，并可能影响SLAM产生跳变，因此实际优先取每session前十分钟。采后写盘约三至五分钟。作者人工标记每项示范起止、剔除复位运动，训练再降至20Hz；纠正数据直接20Hz。60Hz采集、20Hz控制及端到端延迟是不同指标，本文未报告统一时延与跨设备同步误差（§V-A、附录 A-B）

### 2. 动作重定向与观察转换

LEAP 四指十六关节，人手小指不参与IK；以人腕六维姿态初始化、匹配其余指尖位置。末端姿态与十六手关节构成本体状态，下一时刻状态作位置目标监督，不是简单复制人手关节角。两臂配两手形成46维动作表示，其中每腕位姿用七维位置/四元数；不能把它误作两臂全部关节角（§IV-A、图4）

RGBD先变彩色点云，用胸部SLAM变到世界系，再人工一次调整到机器人工作区；同地点共用变换，手轨迹必须做同样变换。去掉桌下与无关点，保存5000点到HDF5，训练下采样1000点。用机器人正向运动学渲染手点云并并入观察，减轻外观差异；二维随机平移同时作用点云与轨迹，不能只动图不动动作（附录 A-C/E）

### 3. 策略与人在回路纠正

**动捕/场景 → 统一世界系 → 同步观察与动作变换 → 指尖IK → 点云Perceiver＋本体状态 → 扩散未来动作 → 控制器。** 训练输入历史三步，batch16、学习率10⁻⁴、3000epoch，DDIM训练100扩散步/推理10步。机械臂OSC、手关节阻抗执行位置目标；未到目标超十步重新查询。GPU型号、总训练时间未报告（附录 A-D/E，表VII）

可选纠正有小幅残差与完整遥操作两模式，脚踏切换。前者把人腕/手指相对初态增量叠加到策略，后者暂时接管；纠正日志保存发给控制器的目标命令，而非把未达到的实际位置误当命令。新纠正集与原始集等概率采样微调，故复杂任务的改进包含真机在回路数据（§IV-C、附录 A-G）

## D. 实验与结果

前三级任务 Sponge picking、Ball collecting、Plate wiping 的三十分钟采集分别得到251/179/102条；Packaging一小时多于十个场景，104条；Scissor cutting与Tea preparing各一小时96/55条。一般每配置每任务二十次，Packaging为六个训练物体各五次、九个新物体各五次，分别30/45次；表中Subtask与All必须分开（§V-A）

| 数据/配置 | 海绵 | 收球 | 擦盘 | 平均 |
|---|---:|---:|---:|---:|
| 仅动捕 DP-img | 0% | 0% | 0% | 0% |
| DP-point | 75% | 65% | 50% | 63% |
| DexIL DP-perc | 85% | 60% | 70% | 72% |

Perceiver并非每项都胜PointNet，收球60%低于65%；遮罩图像DP平均42%。纯图像失效说明这些条件下外观/视角迁移困难，不证明所有图像策略无效（表I）

Packaging全任务训练物体47%、新物体40%；加三十条纠正后57%/42%，新物体收益很小。剪切完整任务由0到20%，泡茶0到25%；泡茶开盖子任务由30%到65%，不是整任务65%。这些改进都含新真机纠正，不能宣传为仅人类动捕零机器人数据（表II–IV）

漂移表VIII在两条回起点轨迹上，IMU-only为8.0±3.1/11.3±4.7cm，SLAM-IMU为0.4±0.2/0.8±0.3cm，是端点漂移诊断，不是所有复杂抓取条件下的三维指尖误差。Ball collecting吞吐约遥操作三倍也仅对应这项演示，不宜扩成所有任务三倍效率（图8、附录 B-A）

## E. 不足、当前平台复用与未来

**作者承认：**续航约四十分钟；指厚与比例差异使指尖IK不保证可用接触；没有力传感。Packaging中稳箱力不足、盒盖离开胸相机视野；剪刀需要深入指环、镊子抓取需精确指尖，几何复制不足（§V、§VI）。缓存降帧与SLAM跳变是附录明确工程限制，不应在使用摘要时遗漏

**我的推论：**统一坐标不等于无漂移或完全同步，传感器标定、异常追踪、点云裁剪与手—物关系都应有日志。D435i可先承担离线场景点云，但没有T265腕部/胸部位姿与手套，就不能按原系统生成同质量人手动作。可先搭低成本模块验证坐标、时间戳、静态重投影与三指可达性，再决定手套/追踪设备投入

DH116右手六主动轴/十一总自由度与十六主动关节LEAP不兼容，应重新定义三指受限IK和耦合，左手仿真资产不能代替右手真机标定。当前整手/多轴仍锁定且原因未知，优先离线运动学、仿真与数据审计；机械臂/双臂、视觉训练GPU、动捕设备均是额外条件，不能据论文暗示已完成臂手验收。后续可单独消融点云、纠正与重定向误差，避免把高策略分数当成普适采集质量证明

## 来源与核验边界

- 已有官方RSS PDF二十页，全文与附录核对；实看图2（p.3）、图4（p.5）、表I–IV（p.10）及缓存/漂移页（p.16/20）
- [官方MIT许可](https://github.com/j96w/DexCap/blob/main/LICENSE)已核验；当前仓库有2024-08硬件更新目录，本文记录原论文配置，不将后续工程改动混作论文验证

## 延伸阅读：数据采集与可执行示范

- [[03 论文卡片/08_数据与遥操作/Bunny-VisionPro - Real-Time Bimanual Dexterous Teleoperation for Imitation Learning|P218 · Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning]]：双臂遥操作、运动学约束与振动反馈
- [[03 论文卡片/08_数据与遥操作/DexWild - Dexterous Human Interactions for In-the-Wild Robot Policies|P224 · DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies]]：自然人手采集、跨具身共同训练、数据筛选
