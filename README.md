<<<<<<< HEAD
# Docker Web App (Flask + MySQL)

## Requirements
- Ubuntu 20.04+
- Docker
- Docker Compose

## Description
This project deploys a Flask web app connected to a MySQL database.
The database uses a persistent volume (`db_data`) to store data.

## Network & Volume
- Network: `app_net`
- Volume: `db_data`

## Containers
1. **web** → Flask app on port 5000
2. **db** → MySQL on port 3306

## Instructions
```bash
./prepare-app.sh
./start-app.sh   # access at http://localhost:5000
./stop-app.sh
./remove-app.sh
=======
# 22UG2-0013
Docker-based web app for CCS3308 Assignment 1
>>>>>>> 1a6565b5f31e68741821d6e9d0fdedba74edec48
