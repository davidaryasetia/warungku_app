@echo off 

python --version 2>NUL

python -m venv venv 
CALL "%cd%\venv\Scripts\activate.bat"

@REM
pip install  -r "%cd%\Document\requirements.txt"

Pause
goto:eof

:errorNoPython
echo. 
echo Error^ : Python 3.10 is not installed
Pause