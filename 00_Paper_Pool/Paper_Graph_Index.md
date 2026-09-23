# Paper Graph Index

Citation graph verified on 2026-09-23. Open a paper link below and follow its **Citation Relations** section. Directed references are recorded in [Citation_Network.csv](../01_Search/Citation_Graph/Citation_Network.csv); the CSV is the auditable source for edge type, evidence URL and verification date. A `Related` link describes technical proximity and does not assert a citation.

## Anchor Papers

- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]] — shared cross-robot data and RT-X models; cited by 21 library papers in the verified subgraph.
- [[02_Papers/01_VLA/OpenVLA|OpenVLA]] — open generalist VLA baseline; cited by 19.
- [[02_Papers/01_VLA/Octo|Octo]] — open generalist robot policy; cited by 18.
- [[02_Papers/10_Benchmark_Dataset/DROID|DROID]] — large real-robot dataset; cited by 14.
- [[02_Papers/03_Bimanual/RDT-1B|RDT-1B]] — bimanual diffusion policy; cited by 10.
- [[02_Papers/01_VLA/SayCan|SayCan]] — language-to-skill affordance grounding; cited by 7.

Anchor rationale and follow-up directions are maintained in the separate anchor index.

## Major Citation Chains

The arrow means **the paper on the right cites the paper on the left**. It does not imply direct algorithm inheritance.

- [[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]] ← [[02_Papers/01_VLA/Octo|Octo]] ← [[02_Papers/01_VLA/OpenVLA|OpenVLA]] ← [[02_Papers/01_VLA/TraceVLA|TraceVLA]].
- [[02_Papers/01_VLA/SayCan|SayCan]] ← [[02_Papers/01_VLA/Octo|Octo]] ← [[02_Papers/01_VLA/OpenVLA|OpenVLA]] ← [[02_Papers/01_VLA/Actions_as_Language|Actions as Language]].
- [[02_Papers/10_Benchmark_Dataset/DROID|DROID]] ← [[02_Papers/01_VLA/OpenVLA|OpenVLA]] ← [[02_Papers/01_VLA/CoT-VLA|CoT-VLA]].
- [[02_Papers/03_Bimanual/RDT-1B|RDT-1B]] ← [[02_Papers/01_VLA/DiffusionVLA|DiffusionVLA]].

## VLA

[[02_Papers/01_VLA/SayCan|SayCan]] · [[02_Papers/01_VLA/Octo|Octo]] · [[02_Papers/01_VLA/OpenVLA|OpenVLA]] · [[02_Papers/01_VLA/TraceVLA|TraceVLA]] · [[02_Papers/01_VLA/ReconVLA|ReconVLA]]

## Bimanual

[[02_Papers/03_Bimanual/RDT-1B|RDT-1B]] · [[02_Papers/03_Bimanual/TwinVLA|TwinVLA]] · [[02_Papers/03_Bimanual/YOTO|YOTO]] · [[02_Papers/03_Bimanual/PPI_Bimanual|PPI Bimanual]]

## Sim2Real

[[02_Papers/05_Sim2Real/Sim2Real-VLA|Sim2Real-VLA]] · [[02_Papers/03_Bimanual/ALOHA_Unleashed|ALOHA Unleashed]] · [[02_Papers/01_VLA/OpenVLA|OpenVLA]]

## Diffusion / Flow

[[02_Papers/03_Bimanual/RDT-1B|RDT-1B]] · [[02_Papers/06_Diffusion_Flow_IL_RL/3D_Diffuser_Actor|3D Diffuser Actor]] · [[02_Papers/06_Diffusion_Flow_IL_RL/Equivariant_Diffusion_Policy|Equivariant Diffusion Policy]]

## Language Grounding

[[02_Papers/01_VLA/SayCan|SayCan]] · [[02_Papers/02_Robot_Manipulation/ManipLLM|ManipLLM]] · [[02_Papers/01_VLA/ReconVLA|ReconVLA]] · [[02_Papers/01_VLA/RoboGround|RoboGround]]

## Generalist Policy

[[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]] · [[02_Papers/01_VLA/Octo|Octo]] · [[02_Papers/01_VLA/OpenVLA|OpenVLA]] · [[02_Papers/03_Bimanual/RDT-1B|RDT-1B]]

## Robot Data

[[02_Papers/10_Benchmark_Dataset/Open_X-Embodiment|Open X-Embodiment]] · [[02_Papers/10_Benchmark_Dataset/DROID|DROID]] · [[02_Papers/10_Benchmark_Dataset/RoboCasa|RoboCasa]] · [[02_Papers/08_Data_Teleoperation/DexCap|DexCap]]

## Coverage and Limits

The first graph pass contains 215 verified directional reference edges from 31 arXiv full-text bibliographies and exact OpenAlex `referenced_works` matches. The reciprocal `Cited By` rows are views of those same 215 citations, not additional citations. Papers with no verified edge show a clearly labeled empty section; they are not assumed unrelated.

