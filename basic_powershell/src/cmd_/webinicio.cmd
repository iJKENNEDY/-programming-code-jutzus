@echo off
cls
:start
set /p webpag=ingrese un abr...
if %webpag%==gh start www.github.com
if %webpag%==hr start www.hackerrank.com
if %webpag%==hn start www.hackernoon.com
if %webpag%==n exit
:win
color 0a
goto start
echo. hasta luego
pause >nul