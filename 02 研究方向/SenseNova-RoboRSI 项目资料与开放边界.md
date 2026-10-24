# SenseNova-RoboRSI 项目资料与开放边界

本页是项目与模型发布资料的研究整理，不是独立论文卡，不分配论文编号。核验日期为 2026-10-24；关联报告是 [[03 论文卡片/01_VLA/Has GPT-6-Astra Achieved Embodied Intelligence|P211 · Has GPT-6-Astra Achieved Embodied Intelligence?]]，不能把项目后续发布结果回填成报告 v2 的实验

## 一、先区分四件事

| 对象 | 改进或测试什么 | 是否更新模型权重 | 可确认来源 |
| --- | --- | --- | --- |
| GPT-6-Astra 能力报告 | 十二个评测设置、执行框架消融、八种真机配置 | GPT 在该测试中冻结；部分实验调用任务微调 π0.5 | [arXiv v2](https://arxiv.org/abs/2610.22471v2)正文、附录 C–E |
| 任务知识包与 ICL | 从训练示范组织目标、参考动作、工具与检查信息 | 不更新 GPT；测试前冻结包，每测试回合独立 | 报告图2–3 |
| Harness RSI | 用执行轨迹和反馈修订提示、工具、记忆组织及恢复逻辑，再复测 | 可以始终冻结基础模型 | [官方 README](https://github.com/OpenSenseNova/SenseNova-RoboRSI)Overview |
| RoboRSI-27B-Preview | 从交互经验后训练开放27B视觉语言模型 | **更新模型权重**，基于Qwen3.8-27B | [官方模型卡](https://huggingface.co/sensenova/sensenova-roborsi-27b-preview)；独立详细技术报告仍coming soon |

ICL（上下文学习）是在会话与工具中利用经验；RSI（递归自我改进）是系统根据反馈迭代的流程名，不天然等价强化学习，也不能仅凭名字推断更新了哪一层参数

## 二、公开材料实际到哪一步

本轮读取官方 README、CONTRIBUTING、模型使用指南、模型卡和主分支代码压缩快照，代码快照提交为 `b513a1c7289ab11eb844856588b64c378705c405`。未执行GPU训练、仿真评测或任何真实机器人命令

### 已有运行和评测入口

仓库包含 `roborsi/runtime`、`agents`、`planner`、`evaluation`、`session`、`tools` 和模型接口；有固定动作与模型Agent、批量任务执行、恢复未完成运行、结果与轨迹记录。`robots/` 中当前能看到 LIBERO、Bench2Dex、DexJoCo、BEHAVIOR、RoboCasa 的适配代码，不应由目录名“robots”就认为其中全是实体设备驱动

[BenchZoo](https://github.com/OpenSenseNova/SenseNova-RoboRSI#benchzoo)列出LIBERO家族、Bench2Dex、DexJoCo、BEHAVIOR、RoboCasa365的准备包或构建指引；[知识包数据集](https://huggingface.co/datasets/sensenova/SenseNova-RoboRSI-Packages)提供版本目录。RoboDojo、RoboLab、SIMPLE和部分导航入口仍标Coming soon，不能将报告全部基准写成已经公开复现

文档说明Python运行层可连接已有HTTP环境，但原生仿真镜像面向Linux，部分需要NVIDIA GPU与Docker。我们当前Windows知识库能阅读代码，不代表本机已具备所有仿真环境。用户配置需匹配模型服务、仿真器、任务版本、知识包与预算，不能把“能启动命令”当“已复现实验”

### 模型发布已经发生，完整训练流程尚不能确认

官方2026-10-22消息及模型卡提供27B权重和部署指南，模型卡标Apache-2.0。使用文档包括LIBERO-Pro的VLA协作／直接VLM控制与RoboCasa365评测命令，RoboDojo复现说明仍待发布

模型卡报告RoboCasa365成功率26.0%→46.5%、平均输出token59.5K→15.9K，LIBERO-Pro为协作92.5%／直接95.0%，RoboDojo协作为平均分26.13／成功20.83%。这些是**项目模型发布声明**，不是P211里GPT实验的结果；当前文档未完整交代各数字全部种子、任务覆盖与统计误差，不能把它们与P211的不同表格相减或组成统一排行榜

公开权重不等于完整的交互训练数据、训练优化器、采样流程、模型—Harness共同迭代配方全部公开。本轮代码快照未找到足以确认完整模型训练流水线的入口，README中的技术报告也未勾选发布。后续可继续核验，但本次不凭空创建“RoboRSI技术论文”或拟定其作者、DOI与接收会议

## 三、54.17%与81.9%为什么必须分开

P211图7／表13的54.17%为“ICL＋闭环VLA”条件，SR按五个类别等权宏平均，另有平均得分60.08，token约19.335M。表5的81.90%来自直接控制＋ICL的210回合扩展预算实验，42任务等权平均，其同运行1×截断为27.62%，并非54.17%

README还引用官方榜单不同时间快照、不同厨房划分的RoboCasa成绩。项目自己注明跨设置仅供背景，不构成同协议排名。复用数据时应同时写：模型、是否任务微调VLA、知识包、标准／扩展预算、任务与布局、SR还是部分完成分、聚合方式、token统计范围

## 四、可以借鉴什么，仍要补什么

执行前审核候选动作与执行后确认物体真的被支撑，是两个不同模块。D435i中杯柄与钩重叠不保证真实挂住，模型说“抓住”不等于DH116已有稳定接触；驱动状态、试提后的几何变化和可见接触证据需要独立检查

可先在仿真比较：固定程序 → 高层选择低层技能 → 加状态核验 → 加有限恢复。每次保留相同初态、目标、步数和冻结包，再单独研究跨回合经验更新。记录整回合成功、状态误判、损坏已有进度、恢复可达性、墙钟时间与调用量；不能只挑成功视频判断能力

这套实验尚未在我们的机械臂、DH116、D435i完成，也不是官方现成的完整真机适配。当前仓库代码Apache-2.0与外部模型、数据、模拟器许可分开；公开网页和示范视频的可观看性也不自动授予再分发权

## 五、对应资料

- [[03 论文卡片/01_VLA/Has GPT-6-Astra Achieved Embodied Intelligence|P211 报告完整论文卡]]：协议、表格、成本和真机案例
- [[02 研究方向/全身运动技能与具身执行框架|全身技能与高层执行的共同研究问题]]：与BeyondMimic对照及未来实验思路
- [官方仓库](https://github.com/OpenSenseNova/SenseNova-RoboRSI)／[当前使用指南](https://github.com/OpenSenseNova/SenseNova-RoboRSI/tree/main/docs)／[模型使用文档](https://github.com/OpenSenseNova/SenseNova-RoboRSI/blob/main/docs/sensenova-roborsi-27b-preview.md)
