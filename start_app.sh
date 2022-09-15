#!/bin/bash

env="$1"

if [ -z "$env" ]; then
    env="dev"
fi

echo "Start '$env' environment"

mkdir -p storage

docker compose \
    -f docker-compose.$env.yml \
    up \
    --build \
    --remove-orphans