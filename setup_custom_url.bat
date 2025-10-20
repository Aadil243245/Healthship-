@echo off
echo.
echo ========================================
echo   HealthShip AI - Custom URL Setup
echo ========================================
echo.
echo This will add a custom domain name for easier access
echo.
echo Adding healthship.local to your hosts file...
echo.

REM Check if running as administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running as Administrator - Good!
    echo.
    
    REM Add custom domain to hosts file
    echo 127.0.0.1 healthship.local >> C:\Windows\System32\drivers\etc\hosts
    echo 192.168.1.100 healthship.local >> C:\Windows\System32\drivers\etc\hosts
    
    echo Custom URL added successfully!
    echo.
    echo You can now access HealthShip AI at:
    echo   http://healthship.local:8000
    echo.
) else (
    echo ERROR: Please run this as Administrator
    echo Right-click and select "Run as administrator"
    echo.
)

pause
