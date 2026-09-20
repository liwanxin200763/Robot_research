# DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression

## Basic Information（基本信息）

- Title: DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression
- Authors: Junjie Wen; Yichen Zhu; Minjie Zhu; Zhibin Tang; Jinming Li; Zhongyi Zhou; Xiaoyu Liu; Chaomin Shen; Yaxin Peng; Feifei Feng
- Year: 2025
- Venue: ICML
- CCF Level: A
- Publication Status: Official Conference Paper
- Type: Method Paper
- Category: A (CCF 7th edition; venue category not independently extracted from official PDF)
- Subcategory: VLA / Robot Foundation Models
- Keywords: VLA; Autoregressive Reasoning / Diffusion

## Classification

- Primary Category: VLA
- Categories: VLA; Robot Manipulation; Diffusion / Flow / IL / RL
- Subcategories: VLA / Robot Foundation Models
- Tags: VLA; Autoregressive Reasoning / Diffusion

## Paper Links（论文）

- Official Paper: https://proceedings.mlr.press/v267/wen25g.html
- DOI: Unknown
- arXiv: 
- Project Page: https://diffusion-vla.github.io/

## Code & Resources（代码与资源）

- Official GitHub: https://github.com/juruobenruo/DexVLA
- Code Status: Partial
- Hugging Face: Unknown
- ModelScope: Unknown
- Checkpoint / Weights: 公开ScaleDP权重不等于DiVLA论文完整权重；待核实（作者入口/说明；未验证权重文件可下载或可用性）
- Dataset: 作者提供DexVLA示例数据：https://huggingface.co/datasets/lesjie/dexvla_example_data；不是原论文全部实验数据
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

- Dataset: 作者提供DexVLA示例数据：https://huggingface.co/datasets/lesjie/dexvla_example_data；不是原论文全部实验数据
- Benchmark: Unknown
- Simulation Environment: Unknown
- Real-world Tasks: Unknown

## Research Summary（研究摘要）

- **Problem:** 研究主题为 `VLA / Robot Foundation Models`；本卡仅按官方摘要级证据整理，未替代正文精读。
- **Main Contribution:**
  - DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and AutoregressionJunjie Wen, Yichen Zhu, Minjie Zhu, Zhibin Tang, Ji...
  - DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and AutoregressionJunjie Wen, Yichen Zhu, Minjie Zhu, Zhibin Tang, Ji...
- **Key Idea:** 以 `VLA; Autoregressive Reasoning / Diffusion` 为主要方法/能力线索；更细的结构和消融结论待正文核验。
- **Experiment / Validation:** Real Robot 字段为 `Unknown`；Dataset、Benchmark、Robot Platform 中的 Unknown 继续保留，不从题名推断。
- **Relevance to Our Project:** 可用于 VLA/机器人基础模型路线对比；应重点核对动作头、训练数据与真机部署成本是否适合当前平台。

## Summary Evidence（摘要证据）

- Reading Depth: Abstract-level / 未精读
- Sources: https://proceedings.mlr.press/v267/wen25g.html；官方摘要/论文集元数据
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

## Reading Status（阅读状态）

Discovery / 未读

## Notes（备注）

官网明确指向后续DexVLA仓库并称可训练DiVLA；实际存在train_divla.sh、UNet策略和评估。原论文模型/完整实验对应关系未核实；Partial可运行条件待复核，不准入核心。 Static checks only; no cloning/running or download.
