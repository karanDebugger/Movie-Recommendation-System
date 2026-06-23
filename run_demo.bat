@echo off
REM Movie Recommendation System - Demo Mode Launcher for Windows

echo.
echo 🎬 Movie Recommendation System - DEMO MODE
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

REM Get Python version
for /f "tokens=*" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✓ %PYTHON_VERSION%

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo ✓ Virtual environment activated
call venv\Scripts\activate.bat

REM Install/upgrade requirements
echo 📥 Installing dependencies...
python -m pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt >nul 2>&1

REM Run the demo app
echo.
echo ==========================================
echo 🚀 Starting Demo App
echo ==========================================
echo 📍 Access the app at: http://localhost:5000
echo 🎯 Try these movies: Avatar, Interstellar, Inception, The Matrix, Gravity
echo 😄 Bonus: Visit /api/joke for random jokes!
echo 🛑 Press Ctrl+C to stop
echo ==========================================
echo.

python app_demo.py

pause
