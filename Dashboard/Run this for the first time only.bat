@echo OFF
REM Check if node is installed
node -v 2> Nul
set current_dir=%cd%
echo you have to be connected to the internet the first time
if "%errorlevel%" == "9009" (
	echo it will take time only the first time
    	echo Installing Node Js
	echo please complete the setup, Please don't close the installation till it completes
	START /WAIT node-v8.9.4-x64.msi
	echo now run the "Run This to run the Website.bat" file to run the website
	pause
)

echo now run the "Run This to run the Website.bat" file to run the website
	pause