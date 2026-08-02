@echo off
set "ROOT=%~dp0.."
cd /d "%ROOT%"
"%ROOT%\.venv\Scripts\python.exe" "%~dp0watch_versions.py"
