"""Check real wiki/Markdown targets without changing any content.
Run with python -B; output reports belong outside the Vault.
Exit nonzero for missing or ambiguous targets. This does not certify GUI clicks.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote,urlsplit

ROOT=Path(__file__).resolve().parents[1]

def resolve(root:Path, source:Path, target:str)->list[Path]:
    target=unquote(target.strip().strip("<>")).split("#",1)[0].split("^",1)[0]
    if not target:
        return [source]
    if urlsplit(target).scheme or target.startswith("//"):
        return []
    # A dot in "RoboTwin 2.0" is part of the title. Try actual files first,
    # then the Markdown suffix, regardless of Path.suffix.
    options=[target] if target.casefold().endswith(".md") else [target,target+".md"]
    for base in (source.parent,root):
        hits=[]
        for option in options:
            p=(base/option).resolve()
            if p.is_relative_to(root.resolve()) and p.is_file():hits.append(p)
        if hits:return sorted(set(hits))
    if "/" not in target and "\\" not in target:
        names={Path(o).name.casefold() for o in options}
        return sorted(p.resolve() for p in root.rglob("*") if p.is_file() and p.name.casefold() in names and not any(x.startswith(".") for x in p.relative_to(root).parts))
    return []

def targets(body:str):
    # Ignore fenced source examples, which are not rendered navigable links.
    body=re.sub(r"(?ms)^(\x60{3,}|~{3,}).*?^\1[^\n]*","",body)
    for match in re.finditer(r"!?\[\[([^\]\n]+)\]\]",body):
        yield "wiki",match[1].split("|",1)[0]
    for match in re.finditer(r"(?<!!)\[[^\]\n]*\]\((<[^>\n]+>|[^)\n]+)\)",body):
        target=match[1].strip()
        if not urlsplit(target.strip("<>")).scheme and not target.startswith("//"):
            yield "markdown",target

def inspect(root:Path,paths:list[Path])->dict:
    rows=[]
    for p in paths:
        for kind,target in targets(p.read_text(encoding="utf-8-sig")):
            hits=resolve(root,p,target)
            rows.append({"source":p.relative_to(root).as_posix(),"kind":kind,"target":target,"status":"valid" if len(hits)==1 else "missing" if not hits else "ambiguous","resolved":[h.relative_to(root.resolve()).as_posix() for h in hits]})
    return {"total":len(rows),"valid":sum(r["status"]=="valid" for r in rows),"missing":sum(r["status"]=="missing" for r in rows),"ambiguous":sum(r["status"]=="ambiguous" for r in rows),"links":rows}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("paths",nargs="+");ap.add_argument("--root",type=Path,default=ROOT);ap.add_argument("--output",type=Path)
    args=ap.parse_args();root=args.root.resolve()
    paths=[]
    for q in args.paths:
        p=Path(q);p=p if p.is_absolute() else root/p
        paths.extend(sorted(p.rglob("*.md")) if p.is_dir() else [p])
    report=inspect(root,paths)
    if args.output:
        output=args.output.resolve()
        if output.is_relative_to(root.parent.resolve()):
            ap.error("report must be outside the active Vault")
        output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k!="links"}))
    for r in report["links"]:
        if r["status"]!="valid":print(json.dumps(r,ensure_ascii=False))
    raise SystemExit(1 if report["missing"] or report["ambiguous"] else 0)
if __name__=="__main__":main()
