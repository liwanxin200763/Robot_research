# RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation

## Basic Information（基本信息）

- Title: RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation
- Authors: Liu, Jiaming; Liu, Mengzhen; Wang, Zhenyu; An, Pengju; Li, Xiaoqi; Zhou, Kaichen; Yang, Senqiao; Zhang, Renrui; Guo, Yandong; Zhang, Shanghang
- Year: 2024
- Venue: NeurIPS
- CCF Level: A
- Publication Status: Official Conference Paper
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Subcategory: VLA / Robot Foundation Models
- Keywords: VLA; Efficient Model / Pose Prediction

## Classification

- Primary Category: VLA
- Categories: VLA; Robot Manipulation
- Subcategories: VLA / Robot Foundation Models
- Tags: VLA; Efficient Model / Pose Prediction

## Paper Links（论文）

- Official Paper: https://proceedings.neurips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html
- DOI: 10.52202/079017-1266
- arXiv: 
- Project Page: https://sites.google.com/view/robomamba-web

## Code & Resources（代码与资源）

- Official GitHub: https://github.com/lmzpai/roboMamba
- Code Status: Partial
- Hugging Face: Unknown
- ModelScope: Unknown
- Checkpoint / Weights: test分支README提供百度网盘链接；未下载（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: 训练数据发布完整性未确认
- Demo: Unknown
- Evaluation: Unknown
- Documentation: Unknown
- Other Official Resources: Unknown

## Robot / Embodiment（机器人与形态）

- Robot Platform: Unknown
- Embodiment: Single Arm / Parallel Gripper
- Single / Bimanual: Single Arm
- Gripper / Hand: Parallel Gripper
- Real Robot: Unknown
- Simulation: Unknown

## Experimental Metadata（实验基础信息）

- Dataset: 训练数据发布完整性未确认
- Benchmark: Unknown
- Simulation Environment: Unknown
- Real-world Tasks: Unknown

## Research Summary（研究摘要）

- **Problem:** 研究主题为 `VLA / Robot Foundation Models`；本卡仅按官方摘要级证据整理，未替代全文审阅。
- **Main Contribution:**
  - Inspired by this, we introduce RoboMamba, an end-to-end robotic VLA model that leverages Mamba to deliver both robotic reasoning and action capabilities, while maintaining efficient fine-tuning and inference.
  - In experiments, RoboMamba demonstrates outstanding reasoning capabilities on general and robotic evaluation benchmarks.
- **Key Idea:** 以 `VLA; Efficient Model / Pose Prediction` 为主要方法/能力线索；更细的结构和消融结论待正文核验。
- **Experiment / Validation:** Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。
- **Relevance to Our Project:** 可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

## Summary Evidence（摘要证据）

- Evidence Level: Abstract-level
- Sources: https://proceedings.neurips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html；官方摘要/论文集元数据
- Verification Status: Official proceedings verified; CCF A via user-provided CCF 7th-edition venue mapping
- Verified Date: 2026-09-19
- Evidence Boundary: 未核实的机器人平台、数据集、代码可运行性和真机细节保持 Unknown。

## Verification（核验）

- [x] Venue confirmed
- [x] Full / Regular Paper confirmed
- [x] CCF A confirmed
- [x] Official Paper confirmed
- [x] Project Page checked
- [x] Official GitHub checked
- [x] Code Status checked
- [x] Checkpoint checked
- [x] Dataset checked
- [ ] Robot Platform checked
- [ ] Real Robot checked

## Notes（备注）

实际存在模型、src/test.py和src/script/test.sh；README要求邮件索取训练代码。test分支提供权重入口。未验证权重可下载/端到端运行，且项目页未查到直接GitHub出链，作者归属链须补核。 Static checks only; no cloning/running or download.

## Citation Metrics

- Citation Count: 11
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4415797921
- OpenAlex Work: https://openalex.org/W4415797921

## Standardized Research Fields

### Research Problem
研究主题为 `VLA / Robot Foundation Models`；本卡仅按官方摘要级证据整理，未替代全文审阅。

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
以 `VLA; Efficient Model / Pose Prediction` 为主要方法/能力线索；更细的结构和消融结论待正文核验。

### Main Contributions
- Inspired by this, we introduce RoboMamba, an end-to-end robotic VLA model that leverages Mamba to deliver both robotic reasoning and action capabilities, while maintaining efficient fine-tuning and inference.

### Dataset & Benchmark
训练数据发布完整性未确认

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。

### Main Results
Unknown / Needs Full-Paper Verification

### Limitations
Unknown / Needs Full-Paper Verification

### What Remains Unsolved?
Library Analysis / Research Note: Unknown / Needs Full-Paper Verification

### Relevance to Our Project
可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

## Full-paper Enrichment (Batch 02)

- Evidence Quality: B
- Evidence Status: Official full text was not reliably extractable in this batch; structured fields below preserve existing card evidence and mark unresolved details explicitly.

### Research Problem
研究主题为 `VLA / Robot Foundation Models`；本卡仅按官方摘要级证据整理，未替代全文审阅。

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
以 `VLA; Efficient Model / Pose Prediction` 为主要方法/能力线索；更细的结构和消融结论待正文核验。

### Architecture / Key Components
Unknown / Needs Official Full-Text Verification

### Dataset & Benchmark
训练数据发布完整性未确认

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。

### Main Results
Unknown / Needs Full-Paper Verification

### Ablation Study
Unknown / Not Explicitly Reported in the currently accessible sources.

### Failure Cases
Unknown / Not Explicitly Reported in the currently accessible sources.

### Limitations
Unknown / Needs Full-Paper Verification

### What Remains Unsolved?
Library Analysis / Research Note: Unknown / Needs Full-Paper Verification

### Open Source
- Official GitHub: https://github.com/lmzpai/roboMamba
- Code Status: Partial
- Checkpoint: Unknown
- Dataset: 训练数据发布完整性未确认

### Relevance to Our Project
** 可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://proceedings.neurips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html; https://sites.google.com/view/robomamba-web; https://github.com/lmzpai/roboMamba

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Fulltext-Unavailable
- Supplement Status: Not Found
- Code Completeness: Partial
- Robot Platform Evidence: Unknown

## Deep Enrichment (Full Text Read: 2026-09-22)
- Evidence Quality: A
- Fulltext Checked: Yes — arXiv HTML 2406.04339 and NeurIPS paper sections inspected.
- Supplement Status: Available - Verified.
- Method: vision encoder features are aligned with a Mamba state-space language backbone; a lightweight policy head predicts SE(3) poses, with only 0.1% parameters fine-tuned (Secs. 3–4).
- Experiments / Results: general reasoning benchmarks plus simulated and real-world pose prediction; inference is reported 3× faster than existing VLA models (abstract and experiments).
- Ablation / Failure Cases: backbone and policy-head efficiency choices are compared; failures center on difficult spatial reasoning and pose prediction cases.
- Limitations: Library Analysis — breadth of robot/task coverage is smaller than large generalist policies.
- Remaining Gap / Idea: combine Mamba efficiency with broader multi-embodiment data.
- Evidence Sources: https://arxiv.org/html/2406.04339 ; https://proceedings.neurips.cc/paper_files/paper/2024/file/46a126492ea6fb87410e55a58df2e189-Paper-Conference.pdf.
- Evidence Upgrade Status: A-Upgraded

## Citation Relations

### References in Library

- [[02_Papers/01_VLA/OpenVLA|OpenVLA]] — [arXiv full-text bibliography item 29](https://arxiv.org/html/2406.04339#bib.bib29)
- [[02_Papers/01_VLA/SayCan|SayCan]] — [arXiv full-text bibliography item 9](https://arxiv.org/html/2406.04339#bib.bib9)
- [[02_Papers/02_Robot_Manipulation/ManipLLM|ManipLLM]] — [arXiv full-text bibliography item 15](https://arxiv.org/html/2406.04339#bib.bib15)

### Cited By in Library

- [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective|A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective]] — [arXiv full-text bibliography item 146](https://arxiv.org/html/2507.01925#bib.bib146)
- [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI|A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI]] — [arXiv full-text bibliography item 119](https://arxiv.org/html/2405.14093#bib.bib119)
- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]] — [arXiv full-text bibliography item 1089](https://arxiv.org/html/2510.10903#bib.bib1089)

### Related Work

- No curated content relation yet.

## 快速摘要

### 研究问题

VLA 要兼顾视觉语言推理、动作预测和可承受的微调/推理成本。

### 之前方法的问题

已有 VLA 在复杂任务推理与微调计算成本之间存在权衡。

### 核心思路

RoboMamba 以 Mamba 架构建立端到端 VLA，重点降低适配和在线推理成本。

### 输入

已核验的摘要或卡片未明确说明；需查阅正文。

### 输出 / 动作

已核验的摘要或卡片未明确说明；需查阅正文。

### 数据集 / Benchmark

训练数据发布完整性尚未确认；仿真与真机评测设置需对照原文。

### 主要结果

论文报告在仿真与真机姿态预测任务中优于所比较 VLA，推理速度约为其 3 倍；具体比较对象见原文。

### 为什么重要

可作为部署时的速度—能力权衡参考。

### 和当前项目的关系

High：有助于研究语言条件操作与 VLA 设计。

### 主要局限

目前证据不足以证明其机器人和任务覆盖达到大型通用策略的广度。

### 摘要证据

官方摘要/论文页; https://arxiv.org/html/2406.04339; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
