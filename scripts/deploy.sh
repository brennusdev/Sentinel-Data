#!/bin/bash

set -e


echo "Starting deployment..."


echo "Running migrations..."

alembic upgrade head


echo "Starting services..."

docker compose \
    -f docker-compose.production.yml \
    up -d


echo "Deployment completed."