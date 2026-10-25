"""Refresh the one data/teleoperation entry without rewriting its research prose.

Usage: python -B .maintenance/scripts/update_data_teleop_index.py [--write]
Only the explicit marker region of the existing main page is replaceable.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))
from research_direction_policy import direction_path, validate_directory

ROOT=Path(__file__).resolve().parents[2]
PAGE=Path("02 研究方向/数据与遥操作.md")
CATEGORY=Path("03 论文卡片/08_数据与遥操作")
BEGIN="<!-- DATA-TELEOP-INDEX:START -->"
END="<!-- DATA-TELEOP-INDEX:END -->"

def scalar(text:str,key:str)->str:
    match=re.search(r"^"+re.escape(key)+r":\s*([^\r\n]+)",text,re.M)
    if not match:
        return ""
    raw=match[1].strip()
    try:
        result=json.loads(raw)
        return str(result) if not isinstance(result,(list,dict)) else ""
    except (ValueError,TypeError):
        return raw.strip("'\"")

def collect(root:Path)->list[dict[str,str]]:
    records=[]
    seen=set()
    folder=root/CATEGORY
    if not folder.is_dir():
        raise ValueError("paper category not found: "+str(folder))
    for path in sorted(folder.glob("*.md")):
        body=path.read_text(encoding="utf-8-sig")
        if path.name=="README.md":
            continue
        front=body.split("---",2)[1] if body.startswith("---") else ""
        pid=scalar(front,"paper_id")
        if not re.fullmatch(r"P\d{3,}",pid):
            raise ValueError("missing stable paper ID: "+str(path))
        if pid in seen:
            raise ValueError("duplicate stable paper ID: "+pid)
        seen.add(pid)
        heading=re.search(r"^# ([^\r\n]+)",body,re.M)
        title=scalar(front,"title") or (heading[1] if heading else path.stem)
        theme=re.search(r"^- 研究主题：([^\r\n]+)",body,re.M)
        metadata=[scalar(front,"year"),scalar(front,"venue")]
        if theme:
            metadata.append(theme[1].strip())
        records.append({"id":pid,"title":title,"path":path.relative_to(root).as_posix(),
                        "notes":"；".join(x for x in metadata if x)})
    if not records:
        raise ValueError("no canonical paper cards found")
    return sorted(records,key=lambda x:int(x["id"][1:]))

def cell(text:str)->str:
    return text.replace("\n"," ").replace("|",r"\|").replace("[",r"\[").replace("]",r"\]")

def render_page(text:str,records:list[dict[str,str]])->str:
    if text.count(BEGIN)!=1 or text.count(END)!=1:
        raise ValueError("expected exactly one managed index marker pair; manual page left unchanged")
    start=text.index(BEGIN)
    end=text.index(END)
    if start>=end:
        raise ValueError("managed markers are out of order")
    old=text[start+len(BEGIN):end]
    annotations={}
    for line in old.splitlines():
        parts=re.split(r"(?<!\\)\|",line)
        if len(parts)==5 and re.fullmatch(r"P\d{3,}",parts[1].strip()):
            pid=parts[1].strip()
            if pid in annotations:
                raise ValueError("duplicate index entry: "+pid)
            annotations[pid]=parts[3].strip()
    ids=[r["id"] for r in records]
    if len(set(ids))!=len(ids):
        raise ValueError("duplicate paper IDs in generated records")
    missing=set(annotations)-set(ids)
    if missing:
        raise ValueError("indexed paper missing from category: "+", ".join(sorted(missing)))
    lines=["| 编号 | 论文主卡 | 研究主题与阅读说明 |","|---|---|---|"]
    for r in records:
        target=quote("../"+r["path"],safe="/")
        # Existing notes may have escaped pipes already; don't escape them twice.
        notes=annotations.get(r["id"])
        if notes is None:
            notes=cell(r["notes"])
        lines.append("| "+r["id"]+" | ["+cell(r["title"])+"]("+target+") | "+notes+" |")
    eol="\r\n" if BEGIN+"\r\n" in text else "\n"
    replacement=BEGIN+eol+eol.join(lines)+eol+END
    return text[:start]+replacement+text[end+len(END):]

def update(root:Path,*,write:bool=False)->bool:
    validate_directory(root,complete=False)
    path=direction_path(root,PAGE.name)
    with path.open("r",encoding="utf-8-sig",newline="") as handle:
        body=handle.read()
    result=render_page(body,collect(root))
    changed=result!=body
    if changed and write:
        with path.open("w",encoding="utf-8",newline="") as handle:
            handle.write(result)
    return changed

def main()->None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root",type=Path,default=ROOT)
    ap.add_argument("--write",action="store_true")
    args=ap.parse_args()
    try:
        changed=update(args.root.resolve(),write=args.write)
    except (ValueError,OSError) as error:
        ap.exit(1,str(error)+"\n")
    print(f"[DATA-TELEOP] changed={changed} written={changed and args.write} page={PAGE.as_posix()}")

if __name__=="__main__":
    main()
