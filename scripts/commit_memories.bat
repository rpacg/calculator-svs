@echo off
echo Adding changes under .\scripts and .\memories...
git add .\scripts .\memories
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%
git commit -m "memories update"
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%
git push
