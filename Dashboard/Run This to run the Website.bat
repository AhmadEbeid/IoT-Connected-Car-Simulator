@echo OFF

echo please run "Run this for the first time only.bat" firstly if you didn't run it
pause

http-server -o -p 4200 2> Nul

if "%errorlevel%" == "9009" (
	echo Installing Live Server
	npm install -g http-server
	http-server -o -p 4200
)