@echo off

taskkill /F /IM elife-rc-smp.exe >nul 2>&1

cd smp
where wt.exe >nul 2>&1

if %ERRORLEVEL% NEQ 0 (elife-rc-smp.exe&pause) else (elife-rc-smp.exe&pause)

