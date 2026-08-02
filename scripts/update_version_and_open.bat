@echo off
set "ROOT=%~dp0.."
cd /d "%ROOT%"
"%ROOT%\.venv\Scripts\python.exe" "%~dp0update_index_version.py"
start "" "%ROOT%\index.html"
