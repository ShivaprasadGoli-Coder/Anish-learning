@echo off
echo.
echo ====================================================
echo   Anish's 11+ Learning App - Starting...
echo ====================================================
echo.
echo Keep this window open while using the app.
echo To stop, close this window or press Ctrl+C.
echo.
start "" cmd /c "timeout /t 2 >nul && start http://127.0.0.1:5151"
python app.py
pause
