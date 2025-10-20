@echo off
echo.
echo ========================================
echo   HealthShip AI - Global Internet Access
echo ========================================
echo.
echo This will set up worldwide access to your HealthShip AI
echo.

REM Check if ngrok is installed
where ngrok >nul 2>&1
if %errorLevel% == 0 (
    echo ✅ ngrok found - Setting up global access...
    echo.
    
    echo Starting HealthShip AI server...
    start /B uvicorn app:app --host 0.0.0.0 --port 8000
    
    echo Waiting for server to start...
    timeout /t 5 /nobreak >nul
    
    echo Creating secure tunnel to internet...
    echo.
    echo ========================================
    echo   Your HealthShip AI will be available at:
    echo   https://[random-id].ngrok.io
    echo ========================================
    echo.
    ngrok http 8000
    
) else (
    echo ❌ ngrok not found - Installing ngrok...
    echo.
    echo Please follow these steps:
    echo.
    echo 1. Go to: https://ngrok.com/download
    echo 2. Download ngrok for Windows
    echo 3. Extract to C:\ngrok\ or add to PATH
    echo 4. Run: ngrok authtoken [your-token]
    echo 5. Run this script again
    echo.
    echo Alternative: Use the portable version below
    echo.
    
    REM Try to download ngrok automatically
    echo Attempting automatic download...
    powershell -Command "Invoke-WebRequest -Uri 'https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip' -OutFile 'ngrok.zip'"
    
    if exist ngrok.zip (
        echo Extracting ngrok...
        powershell -Command "Expand-Archive -Path 'ngrok.zip' -DestinationPath '.'"
        del ngrok.zip
        
        echo ✅ ngrok downloaded successfully!
        echo.
        echo Please get your auth token from: https://dashboard.ngrok.com/get-started/your-authtoken
        echo Then run: ngrok authtoken [your-token]
        echo.
    ) else (
        echo Download failed. Please install manually from https://ngrok.com/download
    )
)

pause
