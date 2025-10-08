#!/bin/sh

# Running Migrations
echo "\n==== Applying migrations ===="
alembic -c mars_probe_api/store/mysqlstore/alembic.ini upgrade head

# Starting Application
echo "\n==== Running application ===="
uvicorn mars_probe_api.app:app --host 0.0.0.0 --port 9900
