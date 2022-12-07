@echo off
set STATVARNAME=IoC-CA
set date=%date:~-4,4%%date:~-10,2%%date:~7,2%
set NAME=%date%-%STATVARNAME%
cls
echo "**********************************************"
echo This batch file will create a project directory
echo Taken from Tutorial 12 and modified slightly
echo "**********************************************"
echo *** press [ctrl][c] to exit or any key to continue ***
pause
echo Creating %NAME%
mkdir %NAME%
cd %NAME%
mkdir Documentation
mkdir Tests
mkdir Examples
mkdir Source
cls
dir
echo "**********************************************"
echo Finished creating project %NAME%
echo "**********************************************"
cd ..