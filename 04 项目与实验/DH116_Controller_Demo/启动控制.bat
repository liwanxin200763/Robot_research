@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
set "PYTHONPATH="
set "PYTHONUTF8=1"
set "PYTHONDONTWRITEBYTECODE=1"
if not exist ".venv\Scripts\python.exe" (
  echo 尚未安装本项目环境，请先双击“首次安装.bat”。
  pause
  exit /b 1
)
".venv\Scripts\python.exe" -I -X utf8 -B "app\main.py" %*
set "demo_exit=%errorlevel%"
if not "%demo_exit%"=="0" echo 控制程序未正常完成。请根据上方提示检查SDK、供电、适配器或查看内部诊断记录；不要连续重试未知故障。
echo.
echo 窗口即将关闭，请按任意键。
pause >nul
exit /b %demo_exit%
