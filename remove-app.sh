#!/bin/bash
echo "Removing app ..."
docker-compose down -v --rmi all
docker network rm app_net || true
docker volume rm db_data || true
