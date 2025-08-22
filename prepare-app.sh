#!/bin/bash
echo "Preparing app ..."
docker network create app_net || true
docker volume create db_data || true
docker-compose build
