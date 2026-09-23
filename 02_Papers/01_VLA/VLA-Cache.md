# VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching

## Basic Information（基本信息）

- Title: VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching
- Authors: Xu, Siyu; Wang, Yunke; Xia, Chenghao; Zhu, Dihao; Huang, Tao; Xu, Chang
- Year: 2025
- Venue: NeurIPS
- CCF Level: A
- Publication Status: Official Conference Paper
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Subcategory: VLA / Robot Foundation Models
- Keywords: VLA; Inference Acceleration / Token Caching

## Classification

- Primary Category: VLA
- Categories: VLA; Robot Manipulation
- Subcategories: VLA / Robot Foundation Models
- Tags: VLA; Inference Acceleration / Token Caching

## Paper Links（论文）

- Official Paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/f062da1973ac9ac61fc6d44dd7fa309f-Abstract-Conference.html
- DOI: 10.52202/085713-5484
- arXiv: 
- Project Page: https://vla-cache.github.io/

## Code & Resources（代码与资源）

- Official GitHub: https://github.com/siyuhsu/vla-cache
- Code Status: Released
- Hugging Face: Unknown
- ModelScope: Unknown
- Checkpoint / Weights: 依赖OpenVLA/OpenVLA-OFT基座；README提供下载脚本（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: README提供LIBERO部署评估说明；未确认自采真机数据是否全量公开
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

- Dataset: README提供LIBERO部署评估说明；未确认自采真机数据是否全量公开
- Benchmark: Unknown
- Simulation Environment: Unknown
- Real-world Tasks: Unknown

## Research Summary（研究摘要）

- **Problem:** 研究主题为 `VLA / Robot Foundation Models`；本卡仅按官方摘要级证据整理，未替代全文审阅。
- **Main Contribution:**
  - This paper introduces VLA-Cache, a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames.
  - Extensive experiments on two simulation platforms (LIBERO and SIMPLER) and a real-world robotic system demonstrate that VLA-Cache achieves up to 1.7× speedup in CUDA latency and a 15\% increase in control frequency, with negligible loss on task success rate.
- **Key Idea:** 以 `VLA; Inference Acceleration / Token Caching` 为主要方法/能力线索；更细的结构和消融结论待正文核验。
- **Experiment / Validation:** Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。
- **Relevance to Our Project:** 可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

## Summary Evidence（摘要证据）

- Evidence Level: Abstract-level
- Sources: https://proceedings.neurips.cc/paper_files/paper/2025/hash/f062da1973ac9ac61fc6d44dd7fa309f-Abstract-Conference.html；官方摘要/论文集元数据
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

已查patch相似度、层级缓存调度及模型实现；方法免训练。训练代码主要继承基座，不能当作额外方法训练贡献。 Static checks only; no cloning/running or download.

## Citation Metrics

- Citation Count: 9
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W7196930033
- OpenAlex Work: https://openalex.org/W7196930033

## Standardized Research Fields

### Research Problem
研究主题为 `VLA / Robot Foundation Models`；本卡仅按官方摘要级证据整理，未替代全文审阅。

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
以 `VLA; Inference Acceleration / Token Caching` 为主要方法/能力线索；更细的结构和消融结论待正文核验。

### Main Contributions
- This paper introduces VLA-Cache, a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames.

### Dataset & Benchmark
README提供LIBERO部署评估说明；未确认自采真机数据是否全量公开

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

## Full-paper Enrichment (Batch 07)

- Evidence Quality: B
- Evidence Status: Official full text was not reliably extractable in this batch; structured fields below preserve existing card evidence and mark unresolved details explicitly.

### Research Problem
研究主题为 `VLA / Robot Foundation Models`；本卡仅按官方摘要级证据整理，未替代全文审阅。

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
以 `VLA; Inference Acceleration / Token Caching` 为主要方法/能力线索；更细的结构和消融结论待正文核验。

### Architecture / Key Components
Unknown / Needs Official Full-Text Verification

### Dataset & Benchmark
README提供LIBERO部署评估说明；未确认自采真机数据是否全量公开

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
- Official GitHub: https://github.com/siyuhsu/vla-cache
- Code Status: Released
- Checkpoint: Unknown
- Dataset: README提供LIBERO部署评估说明；未确认自采真机数据是否全量公开

### Relevance to Our Project
** 可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://proceedings.neurips.cc/paper_files/paper/2025/hash/f062da1973ac9ac61fc6d44dd7fa309f-Abstract-Conference.html; https://vla-cache.github.io/; https://github.com/siyuhsu/vla-cache

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Fulltext-Unavailable
- Supplement Status: Not Found
- Code Completeness: Mostly Complete
- Robot Platform Evidence: Unknown

## Deep Enrichment (Source Checked: 2026-09-22; Full Text Pending)
- Evidence Quality: B
- Fulltext Checked: No — official OpenReview PDF identified; extraction not completed in this batch.
- Supplement Status: Not Found.
- Evidence Boundary: only official abstract/figure-level facts retained.
- Evidence Sources: https://arxiv.org/abs/2502.02175 ; https://openreview.net/pdf?id=QZYZ0Xm58q.
- Evidence Upgrade Status: B-Experiment-Not-Extracted.

## Citation Relations

### References in Library

- [[02_Papers/01_VLA/Octo|Octo]] — [arXiv full-text bibliography item 9](https://arxiv.org/html/2502.02175#bib.bib9)
- [[02_Papers/01_VLA/OpenVLA|OpenVLA]] — [arXiv full-text bibliography item 11](https://arxiv.org/html/2502.02175#bib.bib11)
- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open_X-Embodiment]] — [arXiv full-text bibliography item 6](https://arxiv.org/html/2502.02175#bib.bib6)

### Cited By in Library

- [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey]] — [arXiv full-text bibliography item 932](https://arxiv.org/html/2510.10903#bib.bib932)

### Related Work

- No curated content relation yet.

## 快速摘要

### 研究问题

VLA 反复处理相似视觉 token，会增加在线推理开销。

### 之前方法的问题

简单缓存可能损害变化场景中的目标识别或动作精度。

### 核心思路

VLA-Cache 无需重新训练，按状态自适应缓存并复用部分推理结果。

### 输入

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 输出 / 动作

已核验摘要未明确说明；需查阅论文方法与实验章节。

### 数据集 / Benchmark

LIBERO、SIMPLER 与论文真机设置。

### 主要结果

作者报告最高约 1.7 倍推理加速；具体成功率影响需按任务核对。

### 为什么重要

提供部署已有 VLA 时降低延迟的方法。

### 和当前项目的关系

High：双臂实时控制需要低延迟，但必须监测缓存失效。

### 主要局限

场景突变或接触后状态变化时，缓存复用可能延迟纠错。

### 摘要证据

官方摘要/论文页; https://arxiv.org/html/2502.02175; 核验于 2026-09-23. 仅为摘要级速读；原 Evidence Quality 不变。

- 核验层级：摘要有可追溯来源
