#!/bin/bash

cd tests
docker compose up -d --always-recreate-deps

#docker exec -t fal_db /bin/bash -c 'mysql -hlocalhost -uroot -se "create user admin identified by \"ui-proxy-server\""'
#psql -U postgres -d your_database -c "CREATE SCHEMA dbt_fal;"
cleanup() {
  echo "Received SIGINT. Cleaning up and exiting..."
  docker compose rm -fs
  exit 0
}

trap cleanup SIGINT

echo "DevEnv is ready. Press Ctrl+C to stop"

# Keep the script running indefinitely
while true; do
  sleep 1
done