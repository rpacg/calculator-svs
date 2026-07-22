@echo off
cd /d "%~dp0"
"c:/Users/rpacg/OneDrive/Apps/calculator svs/.venv/Scripts/python.exe" update_index_version.py
start "" index.html
