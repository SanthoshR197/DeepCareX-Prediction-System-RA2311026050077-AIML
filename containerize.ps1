Write-Host "Starting DeepCareX Containerization (Windows)..." -ForegroundColor Cyan

docker build -t deepcarex:latest .

Write-Host "Build complete. Launching container on port 5000..." -ForegroundColor Green

docker run -it -d -p 5000:5000 --name deepcarex_app deepcarex:latest

Write-Host "Application is now running at http://localhost:5000" -ForegroundColor Green
Write-Host "To see logs, run: docker logs -f deepcarex_app"
