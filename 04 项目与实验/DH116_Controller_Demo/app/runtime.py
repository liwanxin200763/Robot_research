"""Bounded, hidden diagnostics; logging does not replace control cleanup."""
import csv
import io
from datetime import datetime
import os
from pathlib import Path
import shutil
from threading import RLock

from app import bootstrap
from dh116_dev.logging import RunRecorder


class RollingText:
    def __init__(self,path,*,max_bytes=1024*1024,backups=3,header=''):
        self.path=Path(path);self.path.parent.mkdir(parents=True,exist_ok=True)
        self.max_bytes=max_bytes;self.backups=backups;self.lock=RLock();self.header=header
        self.stream=self.path.open('a',encoding='utf-8',newline='')
        self.size=self.path.stat().st_size
    def write(self,text):
        with self.lock:
            size=len(text.encode('utf-8'))
            if self.size and self.size+size>self.max_bytes:
                self.stream.close()
                for index in range(self.backups,0,-1):
                    old=self.path if index==1 else self.path.with_name(self.path.name+f'.{index-1}')
                    target=self.path.with_name(self.path.name+f'.{index}')
                    if old.exists():old.replace(target)
                self.stream=self.path.open('w',encoding='utf-8',newline='');self.size=0
                if self.header:
                    self.stream.write(self.header);self.size=len(self.header.encode('utf-8'))
            count=self.stream.write(text);self.stream.flush();self.size+=size
            return count
    def flush(self):
        with self.lock:self.stream.flush()
    def close(self):
        with self.lock:self.stream.close()


def hidden_logs(root):
    runtime=Path(root)/'.runtime';logs=runtime/'logs';logs.mkdir(parents=True,exist_ok=True)
    if os.name=='nt':
        import ctypes
        kernel=ctypes.windll.kernel32
        kernel.GetFileAttributesW.restype=ctypes.c_uint32
        attrs=kernel.GetFileAttributesW(str(runtime))
        if attrs!=0xffffffff:kernel.SetFileAttributesW(str(runtime),attrs|2)
    return logs


class DiagnosticStream:
    """Capture internal Python output, tee only with explicit --debug."""
    def __init__(self,path,output,*,debug=False,notice=None):
        self.writer=RollingText(path);self.output=output;self.debug=debug;self.notice=notice
        self.pending='';self.lock=RLock()
    def write(self,text):
        with self.lock:
            self.writer.write(text)
            if self.debug:self.output.write(text);self.output.flush()
            self.pending+=text
            while '\n' in self.pending:
                line,self.pending=self.pending.split('\n',1)
                if line.startswith('INPUT_REJECTED:') and self.notice:
                    self.notice('输入未执行：'+line.split(':',1)[1].strip())
            return len(text)
    def flush(self):self.writer.flush()
    def close(self):self.writer.close()


class DemoRecorder(RunRecorder):
    def __init__(self,root,config,dll_path,*,notice=None):
        logs=hidden_logs(root)
        # Only prune completed application-owned run directories, never SDK,
        # configs or an active session. Interrupted runs remain available.
        complete=sorted((p for p in logs.iterdir() if p.is_dir() and
                         (p/'summary.md').exists() and (p/'config.json').exists()),key=lambda p:p.name)
        for old in complete[:-4]:
            resolved=old.resolve()
            if resolved.parent==logs.resolve() and not old.is_symlink():shutil.rmtree(resolved)
        self.notice=notice
        super().__init__(root,'dh116_controller',config,dll_path,output_root=logs)
        self._events.close();self._raw.close();self._samples.close()
        self._events=RollingText(self.jsonl_path)
        self._raw=RollingText(self.raw_path)
        header=io.StringIO(newline='');csv.DictWriter(header,fieldnames=self.COLUMNS).writeheader()
        self._samples=RollingText(self.csv_path,header=header.getvalue())
        self._writer=csv.DictWriter(self._samples,fieldnames=self.COLUMNS)
    def event(self,name,**fields):
        super().event(name,**fields)
        if self.notice:self.notice(name,fields)
