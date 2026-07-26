@echo off
echo.
echo ====================================================
echo   Anish's 11+ Learning App - Setup
echo ====================================================
echo.
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ERROR: Python not found. Install from python.org
    echo Make sure to tick "Add Python to PATH" during install!
    pause
    exit /b 1
)
python --version
echo.
echo Installing packages...
python -m pip install flask psycopg2-binary
echo.
if not exist config.py (
    echo ERROR: config.py not found!
    echo Copy config.example.py to config.py and add your database connection string.
    pause
    exit /b 1
)
echo Testing database connection...
python -c "from db import test_connection; ok,msg=test_connection(); print(msg); exit(0 if ok else 1)"
if %errorlevel% neq 0 (
    echo Connection failed. Check your config.py file.
    pause
    exit /b 1
)
echo.
echo ====================================================
echo   Setup complete! Double-click start.bat to begin.
echo ====================================================
echo.
pause
