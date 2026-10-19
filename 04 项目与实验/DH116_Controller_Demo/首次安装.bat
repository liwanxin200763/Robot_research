@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
set "PYTHONPATH="
set "PYTHONUTF8=1"
set "PYTHONDONTWRITEBYTECODE=1"
echo DH116 控制Demo首次安装：需要Windows、64位Python 3.10+和联网。
where py >nul 2>nul
if not errorlevel 1 goto use_py
where python >nul 2>nul
if not errorlevel 1 goto use_python
echo 未找到Python。请从 https://www.python.org/downloads/windows/ 安装64位Python 3.10或更新版，勾选添加到PATH后重试。
pause
exit /b 1
:use_py
py -3 -X utf8 -B "app\setup_check.py" --bootstrap
goto finished
:use_python
python -X utf8 -B "app\setup_check.py" --bootstrap
:finished
set "install_exit=%errorlevel%"
if not "%install_exit%"=="0" echo 环境检查未全部通过。请按上方提示补齐SDK或依赖，再运行本安装程序；不会自动修改驱动。
if "%install_exit%"=="0" echo 首次安装完成。请阅读README、退出LHandPro并准备好设备后，再双击“启动控制.bat”。
pause
exit /b %install_exit%
