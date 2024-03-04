@echo off

taskkill /F /IM elife-rc-scp.exe >nul 2>&1

cd scp
where wt.exe >nul 2>&1

if %ERRORLEVEL% NEQ 0 (elife-rc-scp.exe&pause) else (wt.exe elife-rc-scp.exe)

