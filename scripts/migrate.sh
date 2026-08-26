#!/bin/bash

set -e


echo "====================================="
echo "Sentinel Data - Database Migration"
echo "====================================="


echo "Running migrations..."


alembic upgrade head


echo "Migrations completed successfully."