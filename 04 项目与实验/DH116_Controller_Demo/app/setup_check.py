"""Static installation checks. Never loads the hand DLL or enumerates USB."""
from pathlib import Path
import argparse
import importlib.util
import os
import platform
import struct
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
SDK_FILES=('vendor/sdk/bin/LHandProLib.dll',
           'vendor/sdk/python/lhandprolib_python_sdk/__init__.py',
           'vendor/sdk/python/lhandprolib_python_sdk/lhandprolib_wrapper.py',
           'vendor/sdk/python/lhandprolib_python_sdk/lhandprolib_loader.py',
           'vendor/sdk/python/gsusb_canfd/__init__.py')


def check_environment(root=ROOT,*,version=None,bits=None,system=None,machine=None,check_dependencies=True):
    root=Path(root);errors=[]
    version=tuple(sys.version_info[:2]) if version is None else version
    bits=struct.calcsize('P')*8 if bits is None else bits
    system=platform.system() if system is None else system
    machine=platform.machine() if machine is None else machine
    if version<(3,10):errors.append('需要 Python 3.10 或更新版本，请安装64位Python后重试。')
    if bits!=64:errors.append('需要64位Python，与Windows x64厂家SDK一致。')
    if system!='Windows':errors.append('真机控制需要Windows；其他系统仅可运行 --mock。')
    if system=='Windows' and machine.lower() not in ('amd64','x86_64'):errors.append('厂家SDK需要Windows x64/AMD64 Python，不支持原生ARM64解释器。')
    missing=[name for name in SDK_FILES if not (root/name).is_file()]
    if missing:errors.append('厂家SDK文件尚未就绪。请按README将获授权的SDK放入 vendor/sdk：'+', '.join(missing))
    dll=root/SDK_FILES[0]
    if dll.is_file():
        try:
            with dll.open('rb') as stream:
                if stream.read(2)!=b'MZ':raise ValueError('MZ')
                stream.seek(0x3c);offset=struct.unpack('<I',stream.read(4))[0]
                stream.seek(offset)
                if stream.read(4)!=b'PE\0\0' or struct.unpack('<H',stream.read(2))[0]!=0x8664:raise ValueError('machine')
        except (OSError,ValueError,struct.error):errors.append('SDK DLL不是有效的Windows x64文件，请使用厂家x64版本。')
    if check_dependencies:
        for module,label in (('usb','pyusb'),('libusb_package','libusb-package')):
            if importlib.util.find_spec(module) is None:errors.append(f'缺少依赖 {label}，请先双击“首次安装.bat”。')
    return errors


def bootstrap_environment(root=ROOT):
    root=Path(root)
    if sys.version_info<(3,10) or struct.calcsize('P')!=8 or platform.system()!='Windows' or platform.machine().lower() not in ('amd64','x86_64'):
        print('安装需要Windows和64位Python 3.10+，请安装正确版本后重试。');return 1
    print('正在创建本项目虚拟环境...')
    runtime=root/'.runtime/logs';runtime.mkdir(parents=True,exist_ok=True)
    if os.name=='nt':
        import ctypes
        ctypes.windll.kernel32.SetFileAttributesW(str(root/'.runtime'),2)
    try:
        subprocess.run([sys.executable,'-m','venv',str(root/'.venv')],check=True)
        python=root/'.venv/Scripts/python.exe'
        local_config=root/'config/device.local.json'
        if not local_config.exists():
            import shutil
            shutil.copyfile(root/'config/device.example.json',local_config)
            print('已生成 config/device.local.json；请填写本机适配器SN，不要上传该文件。')
        for folder in ('vendor/sdk/bin','vendor/sdk/python'):(root/folder).mkdir(parents=True,exist_ok=True)
        print('正在安装实际依赖，需要联网；详细信息写入内部安装日志。')
        # Keep at most two installation transcripts.
        log=runtime/'install.log'
        if log.exists():log.replace(runtime/'install.log.1')
        with log.open('w',encoding='utf-8') as output:
            subprocess.run([str(python),'-m','pip','install','--disable-pip-version-check','-r',str(root/'requirements.txt')],stdout=output,stderr=subprocess.STDOUT,check=True)
        completed=subprocess.run([str(python),'-X','utf8',str(root/'app/setup_check.py'),'--check'],check=False)
        return completed.returncode
    except (OSError,subprocess.CalledProcessError) as error:
        print('安装未完成。请检查网络、Python的venv/pip组件及目录写入权限；详细信息在 .runtime/logs/install.log。')
        return 1


def main(argv=None):
    parser=argparse.ArgumentParser(description='DH116环境静态检查，不连接设备')
    parser.add_argument('--bootstrap',action='store_true');parser.add_argument('--check',action='store_true')
    args=parser.parse_args(argv)
    if args.bootstrap:return bootstrap_environment()
    errors=check_environment()
    for message in errors:print(message)
    if not errors:print('Python、依赖与SDK文件静态检查通过；尚未连接设备。')
    print('适配器需安装WinUSB驱动；本工具不自动安装/修改驱动。')
    print('如DLL报缺少VCRUNTIME/MSVCP，请从Microsoft官方安装Visual C++ 2015–2022 x64运行库。')
    print('WinUSB绑定、SDK依赖DLL及真实通信只能在获授权连接时进一步验证；文件检查不等于设备可用。')
    return 1 if errors else 0


if __name__=='__main__':raise SystemExit(main())
