@echo off
REM Build script for The Void Miner (Windows)

echo Building The Void Miner...

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

REM Install the package in development mode
echo Installing package in development mode...
pip install -e .

echo Build completed successfully!
echo.
echo To run the game:
echo   venv\Scripts\activate.bat
echo   void-miner
echo.
echo Or:
echo   python -m void_miner

pause
