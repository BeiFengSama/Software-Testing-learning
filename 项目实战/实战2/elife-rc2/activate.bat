@echo off
cd scp
where wt.exe >nul 2>&1

if %ERRORLEVEL% NEQ 0 (elife-rc-scp.exe activate&pause) else (wt.exe elife-rc-scp.exe activate)

