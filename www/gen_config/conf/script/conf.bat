@echo off

if not exist ..\outputServer mkdir ..\outputServer

del /f /s /q ..\outputServer\*.*

echo "---stringres---"
cd stringres
python start.py %3
cd ..