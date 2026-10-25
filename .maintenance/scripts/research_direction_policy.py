"""Fixed public research taxonomy; no topic files or subfolders here.

Run python -B .maintenance/scripts/research_direction_policy.py to validate.
New papers go to existing card categories. Topic reports belong in
01 论文文库/专题阅读; concrete project plans belong in 04 项目与实验.
"""
from pathlib import Path
import argparse

ROOT=Path(__file__).resolve().parents[2]
DIRECTION_FILES=(
    "VLA.md","机器人操作.md","双臂协作.md","灵巧操作.md",
    "仿真到真实_Sim2Real.md","扩散模型_流匹配_IL_RL.md",
    "泛化与长程任务.md","数据与遥操作.md",
)

def direction_path(root:Path,name:str)->Path:
    if name not in DIRECTION_FILES:
        raise ValueError("not an allowed research direction: "+name)
    return root/"02 研究方向"/name

def validate_directory(root:Path,*,complete:bool=True)->None:
    folder=root/"02 研究方向"
    if not folder.is_dir():
        raise ValueError("research direction directory is missing")
    actual={p.name for p in folder.iterdir() if p.is_file()}
    extra=actual-set(DIRECTION_FILES)
    subfolders=[p.name for p in folder.iterdir() if not p.is_file()]
    missing=set(DIRECTION_FILES)-actual if complete else set()
    if extra or subfolders or missing:
        raise ValueError("invalid research layout; extra="+repr(sorted(extra))+
                         "; subfolders="+repr(sorted(subfolders))+
                         "; missing="+repr(sorted(missing)))

def main()->None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root",type=Path,default=ROOT)
    args=parser.parse_args()
    try:validate_directory(args.root.resolve())
    except (OSError,ValueError) as e:parser.exit(1,str(e)+"\n")
    print("[DIRECTIONS] exactly 8 fixed pages; no extra files or subfolders")

if __name__=="__main__":main()
