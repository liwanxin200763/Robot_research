# Anchor Papers

Selection combines verified in-library citations, foundational role and project fit. Global citation counts are **one exact OpenAlex or Semantic Scholar work** as checked on 2026-09-23; Unknown means identity/API coverage is unresolved, not zero. In-library counts are partial because the graph is still growing.

## [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]]

- Why Anchor: Shared cross-embodiment data and RT-X baselines.
- Citation Count: 1192 (source: https://www.semanticscholar.org/paper/ef7d31137ef06c5be8c2824ecc5af6ce3358cc8f).
- Referenced By library papers: 21 verified direct edges.
- Main Idea: We present Open X-Embodiment, a standardized multi-institution dataset mixture with RT-X generalist policy experiments.
- Later Directions: Build a controlled cross-robot data split; inspect action normalization.
- Important Predecessors (verified in-library citations): None verified in current graph.
- Important Successors (verified in-library citations): [[02_Papers/01_VLA/Actions_as_Language|Actions as Language]], [[02_Papers/01_VLA/CoT-VLA|CoT-VLA]], [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]], [[02_Papers/01_VLA/Octo|Octo]], [[02_Papers/01_VLA/OpenVLA|OpenVLA]].

## [[02_Papers/01_VLA/OpenVLA|OpenVLA]]

- Why Anchor: Open generalist VLA and reusable fine-tuning baseline.
- Citation Count: 43 (source: https://openalex.org/W4399695759).
- Referenced By library papers: 19 verified direct edges.
- Main Idea: Addressing these challenges, we introduce OpenVLA, a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations.
- Later Directions: Test fast adaptation and bimanual action interfaces.
- Important Predecessors (verified in-library citations): [[02_Papers/01_VLA/Octo|Octo]], [[02_Papers/10_Benchmark_Dataset/DROID|DROID]], [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]].
- Important Successors (verified in-library citations): [[02_Papers/01_VLA/Actions_as_Language|Actions as Language]], [[02_Papers/01_VLA/BridgeVLA|BridgeVLA]], [[02_Papers/01_VLA/CoT-VLA|CoT-VLA]], [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]], [[02_Papers/01_VLA/ReconVLA|ReconVLA]].

## [[02_Papers/01_VLA/Octo|Octo]]

- Why Anchor: Open generalist policy trained across diverse robot data.
- Citation Count: 102 (source: https://openalex.org/W4402353985).
- Referenced By library papers: 18 verified direct edges.
- Main Idea: As a first step, we introduce Octo, a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, the largest robot manipulation dataset to date.
- Later Directions: Compare embodiment transfer and action chunking.
- Important Predecessors (verified in-library citations): [[02_Papers/01_VLA/SayCan|SayCan]], [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]].
- Important Successors (verified in-library citations): [[02_Papers/01_VLA/Actions_as_Language|Actions as Language]], [[02_Papers/01_VLA/CoT-VLA|CoT-VLA]], [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]], [[02_Papers/01_VLA/OpenVLA|OpenVLA]], [[02_Papers/01_VLA/ReconVLA|ReconVLA]].

## [[02_Papers/10_Benchmark_Dataset/DROID|DROID]]

- Why Anchor: Large real-robot manipulation dataset.
- Citation Count: 1192 (source: https://www.semanticscholar.org/paper/ef7d31137ef06c5be8c2824ecc5af6ce3358cc8f).
- Referenced By library papers: 14 verified direct edges.
- Main Idea: In this work, we introduce DROID (Distributed Robot Interaction Dataset), a diverse robot manipulation dataset with 65k demonstration trajectories or 350h of interaction data, collected across 564 scenes and 86 tasks by 50 data collectors in North America, Asia, and Europe over the course of 12 months.
- Later Directions: Study demonstration coverage and failure data.
- Important Predecessors (verified in-library citations): None verified in current graph.
- Important Successors (verified in-library citations): [[02_Papers/01_VLA/Actions_as_Language|Actions as Language]], [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]], [[02_Papers/01_VLA/OpenVLA|OpenVLA]], [[02_Papers/01_VLA/RoboMonkey|RoboMonkey]], [[02_Papers/01_VLA/SpatialVLA|SpatialVLA]].

## [[02_Papers/03_Bimanual/RDT-1B|RDT-1B]]

- Why Anchor: Bimanual diffusion foundation model.
- Citation Count: 1192 (source: https://www.semanticscholar.org/paper/ef7d31137ef06c5be8c2824ecc5af6ce3358cc8f).
- Referenced By library papers: 10 verified direct edges.
- Main Idea: In this paper, we present the Robotics Diffusion Transformer (RDT), a pioneering diffusion foundation model for bimanual manipulation.
- Later Directions: Compare coordinated dual-arm action representation.
- Important Predecessors (verified in-library citations): None verified in current graph.
- Important Successors (verified in-library citations): [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]], [[02_Papers/01_VLA/SP-VLA|SP-VLA]], [[02_Papers/01_VLA/SimpleVLA-RL|SimpleVLA-RL]], [[02_Papers/01_VLA/SpatialVLA|SpatialVLA]], [[02_Papers/01_VLA/VideoVLA|VideoVLA]].

## [[02_Papers/01_VLA/SayCan|SayCan]]

- Why Anchor: Affordance-grounded language-to-skill planning.
- Citation Count: 523 (source: https://openalex.org/W4224912544).
- Referenced By library papers: 7 verified direct edges.
- Main Idea: We propose to provide real-world grounding by means of pretrained skills, which are used to constrain the model to propose natural language actions that are both feasible and contextually appropriate.
- Later Directions: Connect high-level task choice to grounded low-level execution.
- Important Predecessors (verified in-library citations): None verified in current graph.
- Important Successors (verified in-library citations): [[02_Papers/01_VLA/Actions_as_Language|Actions as Language]], [[02_Papers/01_VLA/Octo|Octo]], [[02_Papers/01_VLA/RoboMamba|RoboMamba]], [[02_Papers/09_Survey_Review/A_Survey_on_Robotics_with_Foundation_Models_Toward_Embodied_AI|A Survey on Robotics with Foundation Models Toward Embodied AI]], [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_An_Action_Tokenization_Perspective|A Survey on Vision-Language-Action Models An Action Tokenization Perspective]].

## [[02_Papers/06_Diffusion_Flow_IL_RL/3D_Diffuser_Actor|3D Diffuser Actor]]

- Why Anchor: 3D scene-conditioned diffusion action generator.
- Citation Count: 4 (source: https://openalex.org/W4391949089).
- Referenced By library papers: 6 verified direct edges.
- Main Idea: Through thorough comparisons with the current SOTA policies and ablations of our model, we show 3D Diffuser Actor ’s design choices dramatically outperform 2D representations, regression and classification objectives, absolute attentions, and holistic non-tokenized 3D scene embeddings.
- Later Directions: Study pose/action prediction for two ordinary grippers.
- Important Predecessors (verified in-library citations): None verified in current graph.
- Important Successors (verified in-library citations): [[02_Papers/01_VLA/BridgeVLA|BridgeVLA]], [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]], [[02_Papers/02_Robot_Manipulation/VidMan|VidMan]], [[02_Papers/03_Bimanual/AnyBimanual|AnyBimanual]], [[02_Papers/09_Survey_Review/A_Survey_on_Vision-Language-Action_Models_for_Embodied_AI|A Survey on Vision-Language-Action Models for Embodied AI]].

## [[02_Papers/01_VLA/ReconVLA|ReconVLA]]

- Why Anchor: Reconstruction-based visual grounding for VLA.
- Citation Count: 3 (source: https://openalex.org/W7137985120).
- Referenced By library papers: 1 verified direct edges.
- Main Idea: A diffusion transformer reconstructs the gaze region of the manipulated object conditioned on the VLA visual outputs, jointly encouraging task-specific visual representations while preserving action prediction.
- Later Directions: Test whether target-region perception improves real-robot execution.
- Important Predecessors (verified in-library citations): [[02_Papers/01_VLA/3D-VLA|3D-VLA]], [[02_Papers/01_VLA/Octo|Octo]], [[02_Papers/01_VLA/OpenVLA|OpenVLA]], [[02_Papers/01_VLA/RoboGround|RoboGround]], [[02_Papers/02_Robot_Manipulation/VidMan|VidMan]].
- Important Successors (verified in-library citations): [[02_Papers/09_Survey_Review/Towards_a_Unified_Understanding_of_Robot_Manipulation_A_Comprehensive_Survey|Towards a Unified Understanding of Robot Manipulation A Comprehensive Survey]].

Citation count measures one facet of community attention, not paper quality. Prioritize with venue, year, evidence quality, open code, real-robot fit, bimanual relevance, limitations and research-gap value.
