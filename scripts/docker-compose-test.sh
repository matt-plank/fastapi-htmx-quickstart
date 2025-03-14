#!/bin/bash
PROJECT_NAME=$(basename "$PWD")-test
COMMAND="${@:1}"

echo "Clearing old containers..."
docker compose -p $PROJECT_NAME -f docker-compose.test.yaml down

echo "Running tests..."
docker compose -p $PROJECT_NAME -f docker-compose.test.yaml $COMMAND
EXIT_CODE=$?

echo "Clearing test containers..."
docker compose -p $PROJECT_NAME -f docker-compose.test.yaml down

exit $EXIT_CODE
