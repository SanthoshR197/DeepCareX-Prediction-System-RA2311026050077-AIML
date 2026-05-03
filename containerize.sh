#!/bin/bash

echo "Starting DeepCareX Containerization..."

docker build -t deepcarex:latest .

echo "Build complete. Launching container on port 5000..."

docker run -it -d -p 5000:5000 --name deepcarex_app deepcarex:latest

echo "Application is now running at http://localhost:5000"
echo "To see logs, run: docker logs -f deepcarex_app"
