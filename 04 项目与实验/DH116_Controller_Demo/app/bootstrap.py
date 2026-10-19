"""Resolve all application dependencies relative to this copied folder."""
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
ENGINE=ROOT/'app/_engine'
sys.dont_write_bytecode=True
sys.path.insert(0,str(ENGINE))
for name in ('dh116_dev','controller'):
    loaded=sys.modules.get(name)
    if loaded and getattr(loaded,'__file__',None) and not Path(loaded.__file__).resolve().is_relative_to(ENGINE):
        raise RuntimeError('检测到其他工程的控制模块，请使用本目录的启动控制.bat')
