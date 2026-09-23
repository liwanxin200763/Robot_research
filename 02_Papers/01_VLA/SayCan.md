# SayCan: Do As I Can, Not As I Say

## Basic Information

- Title: Do As I Can, Not As I Say: Grounding Language in Robotic Affordances
- Short Name: SayCan / PaLM-SayCan
- Authors: Michael Ahn; Anthony Brohan; Noah Brown; Yevgen Chebotar; Omar Cortes; Byron David; Chelsea Finn; Chuyuan Fu; Keerthana Gopalakrishnan; Karol Hausman; Alex Herzog; Daniel Ho; Jasmine Hsu; Julian Ibarz; Brian Ichter; Alex Irpan; Eric Jang; Rosario Jauregui Ruano; Kyle Jeffrey; Sally Jesmonth; Nikhil J Joshi; Ryan Julian; Dmitry Kalashnikov; Yuheng Kuang; Kuang-Huei Lee; Sergey Levine; Yao Lu; Linda Luu; Carolina Parada; Peter Pastor; Jornell Quiambao; Kanishka Rao; Jarek Rettinghouse; Diego Reyes; Pierre Sermanet; Nicolas Sievers; Clayton Tan; Alexander Toshev; Vincent Vanhoucke; Fei Xia; Ted Xiao; Peng Xu; Sichun Xu; Mengyuan Yan; Andy Zeng
- Year: 2022
- Venue: Conference on Robot Learning (CoRL 2022), Proceedings of Machine Learning Research 205, pp. 287–318
- Publication Status: Formal CoRL paper; PMLR volume published 2023; arXiv v2 2022-08-16
- CCF Level: Not CCF A (CoRL is a robotics venue; no CCF-A assignment recorded)
- DOI: 10.48550/arXiv.2204.01691
- Reading Status: Discovery / 已完成全文核验
- Priority: P0

## Classification

- Primary Category: VLA
- Categories: VLA; Robot Manipulation; Language Grounding; Affordance; Planning; Long-horizon; Robot Learning; Sim2Real
- Subcategories: Language-conditioned planning; skill composition; value-function affordance grounding; mobile manipulation
- Tags: VLA; Robot Manipulation; Language Grounding; Affordance; Long-horizon; Planning; RL; IL; Sim2Real
- Special Attention: Yes

## Paper Links

- Official Paper: https://research.google/pubs/do-as-i-can-not-as-i-say-grounding-language-in-robotic-affordances/
- arXiv: https://arxiv.org/abs/2204.01691
- Full-text HTML: https://arxiv.org/html/2204.01691
- CoRL / PMLR: https://proceedings.mlr.press/v205/ichter23a.html
- Project Page: https://say-can.github.io/
- PaLM-SayCan Demo: https://sites.research.google/palm-saycan
- Google Research Blog: https://research.google/blog/towards-helpful-robots-grounding-language-in-robotic-affordances/

## Code & Resources

- Official GitHub: https://github.com/google-research/google-research/tree/master/saycan
- Code Status: Released; official tabletop simulation / Colab implementation is public. The original Everyday Robots kitchen stack and learned robot fleet policies are not released as a complete reproduction package.
- Checkpoint: Not released as a complete public PaLM / robot-policy checkpoint
- Dataset: SayCan dataset v0 maps natural-language instructions to one solution and is linked from the project page; the full 68k demonstration collection is not released as a complete training dump.
- Demo: https://sites.research.google/palm-saycan
- Supplement: Appendix A–E included in the arXiv full text; official project page also documents drawer, chain-of-thought and multilingual extensions.

## Embodiment and System

- Robot: Everyday Robots mobile manipulator; 7-DoF arm with two-finger gripper; RGB observation; known semantic locations.
- Environment: Real office kitchen and matched mock kitchen; 15 objects and 5 locations in the main evaluation.
- Skill inventory: 551 candidate skills spanning 7 skill families and 17 objects. Families include pick, place, rearrange, drawer open/close, navigation/find/go-to and configuration-specific placement; only high-performing/composable skills are used in the main long-horizon evaluation.
- Data: Blog/project page reports 68,000 demonstrations from 10 robots over 11 months plus 12,000 successful autonomous episodes. The paper distinguishes real demonstrations from simulation/RL data and does not present these values as a single benchmark dataset.

## Research Summary

### Research Problem

Large language models contain semantic knowledge for decomposing abstract, temporally extended instructions but are not grounded in a robot embodiment, current scene, action repertoire or execution consequences. A text-only answer can therefore be sensible in language yet infeasible or unsafe for the robot.

### Previous Unsolved Problem

Prior language-conditioned robot systems typically handle short atomic commands, while LLM planning can suggest actions outside the robot's skill set. The missing bridge is a shared interface that scores usefulness toward the instruction and feasibility in the current physical state.

### Method: Say + Can

Let `i` be a high-level user instruction, `s_n` the current state, and `Π` a set of short-horizon skills. Each skill `π ∈ Π` has a policy `π`, language description `ℓ_π`, and affordance/value function `p(c_π | s_n, ℓ_π)`, the probability that the skill completes successfully from the current state. The LLM supplies `p(ℓ_π | i, history)`, the probability that the skill is a useful next step. The paper factorizes progress as:

`p(c_i | i, s_n, ℓ_π) ∝ p(c_π | s_n, ℓ_π) · p(ℓ_π | i)`

and selects:

`π_n = argmax_{π∈Π} p(c_π | s_n, ℓ_π) p(ℓ_π | i, ℓ_{π_{n-1}}, …, ℓ_{π_0})`.

“Say” is task grounding from the LLM; “Can” is world grounding from the affordance/value model. The selected skill is executed, the state is updated, the chosen text is appended to the dialogue, and the system replans until `done`. This receding-horizon loop makes the plan inspectable and constrains generation to the available skill set.

### Policy, Value and Training Details

- BC-Z: image-based behavioral-cloning policies use a language embedding and a ResNet-18/FiLM-style architecture to predict arm, orientation, gripper and terminate actions.
- MT-Opt / RL: language-conditioned value functions use a multi-task RL architecture similar to MT-Opt, with TD backups and sparse success reward. In the undiscounted sparse-reward setting, a successful terminal reward of 1 and failure reward of 0 makes the value an affordance estimate.
- Universal Sentence Encoder: BC USE projects a user instruction and candidate skill sequences into known commands by cosine similarity; it is a no-LLM baseline, not the PaLM-SayCan method.
- Affordance calibration: learned Q-values are calibrated to probabilities; pick uses a normalized value, navigation uses distance, place is set to 1 after a pick, and terminate is assigned 0.1. Completed skills are capped/blocked to avoid repeating no-op actions.
- Simulation-to-real: RL value functions are trained in an Everyday Robots simulator using RetinaGAN image translation, simulation demonstrations for bootstrap successes, and online data collection.

### Dataset / Benchmark

The main test contains 101 natural-language instructions in 7 families: NL single primitive, NL nouns, NL verbs, structured language, embodiment variations, crowd-sourced requests and long-horizon instructions. The main evaluation uses both a training/mock kitchen and a real office kitchen. Horizon ranges from one primitive to 10+ composed skills; Appendix E lists every instruction.

### Baselines

- No VF: removes the value function and selects the highest LLM language score.
- Generative: generates a plan then projects each skill to the nearest known command using USE; it loses explicit option probabilities and affordance composition.
- FLAN-SayCan: same affordance-grounded system with 137B FLAN instead of 540B PaLM.
- BC NL / BC USE: language-conditioned behavioral-cloning controls without LLM planning.
- Language-model scale ablations: PaLM 8B, 62B and 540B, plus 137B FLAN.

### Experiment / Validation

Table 2 reports instruction-family success rates in Mock Kitchen and Real Kitchen. Plan success checks whether the selected sequence is correct; Execute success additionally requires the robot to carry out the sequence. Table 3 compares PaLM-SayCan and FLAN-SayCan across the same 101 tasks. Appendix E and Table 6 enumerate per-instruction outcomes; Appendix E.3 adds drawer skills, E.4 tests chain-of-thought reasoning, and E.5 tests multilingual queries.

### Main Results

- Mock Kitchen / training environment (Table 2): PaLM-SayCan plan 84%, execute 74% over 101 instructions.
- Real office kitchen (Table 2): plan 81%, execute 60%.
- PaLM vs FLAN (Table 3): PaLM-SayCan 84% plan / 74% execute; FLAN-SayCan 70% / 61%.
- No affordance grounding (Table 2): No VF 67% plan; Generative 74% plan. BC NL executes 0%; BC USE executes 9% overall.
- Drawer extension (Table 8 / Appendix E.3): 100% planning and 33% execution over 21 queries; execution failures were mainly drawer manipulation failures.
- Case studies show 8-step and 16-step plans, chain-of-thought helps with negation/reasoning, and English-to-Chinese/French/Spanish planning has almost no drop in the reported multilingual test.

### Ablation Study

The central ablation removes the affordance/value function (No VF) or replaces option scoring with a generative projection (Generative), showing that language-only selection is weaker. Language-model scaling compares 8B, 62B and 540B PaLM plus 137B FLAN; larger PaLM generally improves generative problems and PaLM beats FLAN in the full robotics evaluation, although 62B versus 540B is close. BC NL and BC USE isolate the role of LLM planning. Appendix tables additionally vary prompt examples/termination, drawer skill additions, chain-of-thought prompting and multilingual queries.

### Failure Cases

- Planning: LLM language scores can choose the wrong object, mishandle negation or produce an incomplete sequence; long-horizon and embodiment families expose this gap.
- Execution: low-level pick/place/navigation or chained drawer manipulation can fail even when the plan is correct, explaining the plan–execute gaps (84→74% mock; 81→60% real).
- Embodiment grounding: the one-arm robot must temporarily remove objects from a drawer, close it, and pick them again; the skill library and affordances are embodiment-specific.
- Author evidence: drawer tasks plan at 100% but execute at 33%, with failures from opening the drawer too little or not closing it completely. The paper does not provide a universal post-action success detector.

### Limitations

- Author-stated: vanilla SayCan only receives environmental feedback through current-step value functions; after a skill fails or the environment changes, necessary feedback may be unavailable. The authors point to closed-loop feedback through success detectors, scene descriptors or human feedback as future work.
- Author-stated: fixed natural-language skill descriptions require supervision and may be a poor ontology for some tasks; additional skills must be supplied with policies, affordances and prompt examples.
- Library Analysis: the method composes a fixed atomic skill library and does not synthesize unseen low-level behaviors; continuous contact-rich action grounding is delegated to pretrained policies.
- Library Analysis: value-function calibration, known object/location assumptions and separation between planning and control limit transfer to unseen embodiments, bimanual coordination and failure recovery.

### Remaining Unsolved Problem

1. Open-ended tasks outside the fixed skill library remain unsupported (Sec. 3–4 evidence).
2. Continuous action and contact-level grounding remain inside pretrained policies rather than the LLM planner (Sec. 4 / Appendix C).
3. Execution verification and recovery after an unsuccessful skill are not closed-loop in vanilla SayCan (Sec. 5.2 and project page).
4. Long-horizon compounding failures remain visible in plan–execute gaps and drawer results (Tables 2, 3 and 8).
5. Joint feasibility and role allocation for bimanual ordinary-gripper systems are not evaluated (library/project analysis).

## SayCan vs Modern VLA

SayCan is a modular language-conditioned planner over pretrained atomic skills: LLM scores task usefulness, affordance/value scores feasibility, and a receding-horizon controller executes one skill at a time. Modern end-to-end VLAs generally predict action tokens or trajectories directly from visual-language context and may learn broader action representations, but often make feasibility, execution verification and failure recovery less explicit. SayCan remains a useful interpretable baseline for testing whether a VLA's proposed subgoal is feasible before action execution.

## Relevance to Our Project

For NERO's dual-arm, ordinary-gripper, real-world manipulation, SayCan is a planning-and-grounding reference rather than a drop-in bimanual policy. Three direct inspirations are: (1) score candidate subgoals by both language usefulness and execution feasibility; (2) replace single-skill affordance with a joint two-arm feasibility model for handoff, stabilization and coordinated placement; (3) add pre/post-action verification and replanning so execution failures update the plan instead of silently propagating.

## Idea Clues

- Idea 1 — Joint-affordance SayCan for bimanual ordinary grippers. Evidence: SayCan multiplies task-grounding and world-grounding; Library Analysis: extend `p(c_π|s,ℓ_π)` to a joint action/role feasibility score; relevance: directly targets NERO dual-arm coordination. Keywords: bimanual; affordance; role allocation.
- Idea 2 — VLA visual subgoal grounding with affordance veto. Evidence: No VF and Generative underperform PaLM-SayCan; Library Analysis: use a VLA to propose visual subgoals and a learned feasibility head to veto unsafe/infeasible actions; relevance: connects SayCan interpretability to modern VLA control. Keywords: VLA; visual grounding; feasibility.
- Idea 3 — Failure-aware receding-horizon recovery. Evidence: plan–execute gaps and drawer 100%/33% results; Library Analysis: add post-action success detection, state refresh and retry/alternative-skill selection; relevance: practical real-robot recovery. Keywords: failure recovery; replanning; verification.
- Idea 4 — Affordance-calibrated sim2real skill library. Evidence: TD value functions, sparse reward and RetinaGAN simulation transfer; Library Analysis: calibrate skill feasibility on NERO objects and dual-arm states before long-horizon execution. Keywords: Sim2Real; value calibration; long-horizon.

## Verification and Evidence

- Full-text read: arXiv HTML v2, Sections 1–8 and Appendices A–E, including Tables 2, 3 and 8 and the policy/value-function details.
- Official paper and metadata: Google Research publication page; CoRL/PMLR record; arXiv 2204.01691.
- Official project/code: say-can.github.io and Google Research `google-research/saycan` tabletop simulation entry.
- Citation metrics: OpenAlex Work W4224912544, 523 citations, checked 2026-09-22. Citation source identifier recorded in Master_Status.csv and Paper_Pool.xlsx.
- Verification date: 2026-09-22.
- Evidence Quality: A
- Evidence Upgrade Status: A-Upgraded
- Supplement Status: Available - Verified
- Code Completeness: Partial (official tabletop environment; original kitchen stack/checkpoints not fully released)
- Robot Platform Evidence: Yes — Everyday Robots mobile manipulator, 7-DoF arm, two-finger gripper
- Fulltext Checked: Yes
- Experiment Extracted: Yes
- Results Extracted: Yes
- Ablation Extracted: Yes
- Failure Cases Extracted: Yes
- Limitations Extracted: Yes
- Remaining Gap Extracted: Yes
- Deep Enrichment Completed: true
- Queue Status: Completed-A

## Citation Metrics

- Citation Count: 523
- Citation Source: OpenAlex
- Citation Checked Date: 2026-09-23
- Citation Source Identifier: https://openalex.org/W4224912544
- OpenAlex Work: https://openalex.org/W4224912544
