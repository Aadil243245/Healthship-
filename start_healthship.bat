@echo off
echo.
echo ========================================
echo    HealthShip AI - Starting Server
echo ========================================
echo.
echo Starting HealthShip AI Medical Platform...
echo.
echo Access URLs:
echo   Local:    http://localhost:8000
echo   Mobile:   http://192.168.1.100:8000
echo   Network:  http://healthship.local:8000
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

uvicorn app:app --reload --host 0.0.0.0 --port 8000
