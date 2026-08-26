#!/bin/bash

set -e


echo "====================================="
echo "Sentinel Data Deployment"
echo "====================================="


echo "[1/3] Running migrations..."

alembic upgrade head


echo "[2/3] Starting containers..."

docker compose \
    -f docker-compose.production.yml \
    up -d


echo "[3/3] Deployment completed."


docker compose \
    -f docker-compose.production.yml \
    ps