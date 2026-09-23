# SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models

## Basic Information（基本信息）

- Title: SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models
- Year: 2025
- Venue / Source: RSS
- Publication Status: 正式主会论文：官方论文集核实
- CCF Level: Not CCF A (robotics venue extension; CCF row not asserted)
- Type: Method Paper
- Category: VLA / Robot Foundation Models / Robot Manipulation
- Subcategory: VLA / Robot Foundation Models
- Priority: P1

## Classification

- Primary Category: VLA
- Categories: VLA; Robot Manipulation
- Subcategories: VLA / Robot Foundation Models
- Tags: Unknown

## Links（链接）

- Official Paper: https://www.roboticsproceedings.org/rss21/p011.html
- arXiv: 待补充
- Project Page: https://spatialvla.github.io/
- Official GitHub: https://github.com/SpatialVLA/SpatialVLA

## Code（代码状态）

- Code Status: Released
- Checkpoint: https://huggingface.co/collections/IPEC-COMMUNITY/foundation-vision-language-action-model-6795eb96a9c661f90236acbb（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset Released: 提供OXE处理与自定义数据说明；未核实全部训练混合的再发布范围

## Embodiment（机器人形态）

- Single Arm / Bimanual / Dexterous Hand / Gripper: Single Arm / Parallel Gripper
- Real Robot: Unknown

## Why Collected（为什么被收录）

正式venue为RSS 2025，不是CVPR/ICML。RSS当前CCF目录等级未成功从官方核实，故仅作扩展候选；不擅自标A或Not_CCF_A。 Static checks only; no cloning/running or download.

## Verification（待核验）

- [x] Venue 已确认
- [ ] CCF 等级已确认
- [x] Official Paper 已确认
- [x] Official GitHub 已确认
- [ ] Code 可运行性已确认
- [ ] 是否真机已确认

## Citation Metrics

- Citation Count: 41
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4414051092
- OpenAlex Work: https://openalex.org/W4414051092

## Standardized Research Fields

### Research Problem
Unknown / Needs Full-Paper Verification

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
Unknown / Needs Full-Paper Verification

### Main Contributions
Unknown / Needs Full-Paper Verification

### Dataset & Benchmark
Unknown / Needs Full-Paper Verification

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Unknown / Needs Full-Paper Verification

### Main Results
Unknown / Needs Full-Paper Verification

### Limitations
Unknown / Needs Full-Paper Verification

### What Remains Unsolved?
Library Analysis / Research Note: Unknown / Needs Full-Paper Verification

### Relevance to Our Project
Unknown / Needs Project-Specific Review

## Full-paper Enrichment (Batch 02)

- Evidence Quality: B
- Evidence Status: Official full text was not reliably extractable in this batch; structured fields below preserve existing card evidence and mark unresolved details explicitly.

### Research Problem
Unknown / Needs Full-Paper Verification

### What Previous Problem Does This Paper Solve?
Unknown / Needs Full-Paper Verification

### Model / Method
Unknown / Needs Full-Paper Verification

### Architecture / Key Components
Unknown / Needs Official Full-Text Verification

### Dataset & Benchmark
Unknown / Needs Full-Paper Verification

### Baseline / SOTA
Unknown / Needs Full-Paper Verification

### Experiment Setup
Unknown / Needs Full-Paper Verification

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
- Official GitHub: https://github.com/SpatialVLA/SpatialVLA
- Code Status: Released
- Checkpoint: https://huggingface.co/collections/IPEC-COMMUNITY/foundation-vision-language-action-model-6795eb96a9c661f90236acbb（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: Unknown

### Relevance to Our Project
Unknown / Needs project-specific review

### Idea Clues
Unknown / Needs paper-specific evidence; no inference added from title alone.

### Evidence Sources
https://www.roboticsproceedings.org/rss21/p011.html; https://spatialvla.github.io/; https://github.com/SpatialVLA/SpatialVLA

- Evidence Level: Official paper/project metadata and abstract-level evidence
- Paper Type: Method Paper
- Evidence Upgrade Status: B-Fulltext-Unavailable
- Supplement Status: Not Found
- Code Completeness: Mostly Complete
- Robot Platform Evidence: Unknown

## Deep Enrichment (Full Text Read: 2026-09-22)
- Evidence Quality: A
- Fulltext Checked: Yes — arXiv HTML 2501.15830, method/experiment sections and project release inspected.
- Supplement Status: Available - Verified.
- Method: Ego3D Position Encoding injects spatial coordinates; Adaptive Action Grids discretize spatial movements for cross-robot transfer (Secs. II–III).
- Dataset / Results: pretraining uses 1.1M real robot episodes; zero-shot simulation/real-robot and adaptation experiments show state-of-the-art spatial generalization (abstract and Sec. IV).
- Ablation: positional encoding, action-grid design and adaptation are separately evaluated; project releases model/code.
- Failure Cases / Limitations: camera/embodiment calibration and spatial distribution shift remain difficult.
- Remaining Gap / Idea: evaluate adaptive grids for bimanual and dexterous action spaces.
- Evidence Sources: https://arxiv.org/html/2501.15830 ; https://spatialvla.github.io/ ; https://github.com/SpatialVLA.
- Evidence Upgrade Status: A-Upgraded

## Citation Relations

### References in Library

- [[02_Papers/01_VLA/3D-VLA|3D-VLA]] — [arXiv full-text bibliography item 69](https://arxiv.org/html/2501.15830#bib.bib69)
- [[02_Papers/01_VLA/Octo|Octo]] — [arXiv full-text bibliography item 48](https://arxiv.org/html/2501.15830#bib.bib48)
- [[02_Papers/01_VLA/OpenVLA|OpenVLA]] — [arXiv full-text bibliography item 30](https://arxiv.org/html/2501.15830#bib.bib30)
- [[02_Papers/01_VLA/TraceVLA|TraceVLA]] — [arXiv full-text bibliography item 71](https://arxiv.org/html/2501.15830#bib.bib71)
- [[02_Papers/03_Bimanual/RDT-1B|RDT-1B]] — [arXiv full-text bibliography item 39](https://arxiv.org/html/2501.15830#bib.bib39)
- [[02_Papers/06_Diffusion_Flow_IL_RL/BAKU|BAKU]] — [arXiv full-text bibliography item 22](https://arxiv.org/html/2501.15830#bib.bib22)
- [[02_Papers/10_Benchmark_Dataset/DROID|DROID]] — [arXiv full-text bibliography item 29](https://arxiv.org/html/2501.15830#bib.bib29)
- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open_X-Embodiment]] — [arXiv full-text bibliography item 13](https://arxiv.org/html/2501.15830#bib.bib13)

### Cited By in Library

- No verified in-library citation edge yet.

### Related Work

- No curated content relation yet.
