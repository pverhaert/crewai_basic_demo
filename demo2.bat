@echo off

REM Check if the virtual environment exists
if not exist .venv (
    echo Virtual environment not found. Please create it first.
    echo Run install.bat first.
    pause
    exit /b
)

REM Activate the virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Start the Crew AI terminal application
echo Starting Crew AI terminal application...
echo.
echo.
set PYTHONWARNINGS=ignore
python demo2/main.py

REM Reminder message
echo.
echo.
echo All the generated files are located in the "demo1/output" folder.
echo.

pause
