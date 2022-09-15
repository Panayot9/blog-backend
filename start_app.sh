#!/bin/bash

mkdir -p storage

docker compose \
    -f docker-compose.yml \
    up \
    --build \
    --remove-orphans