#!/bin/bash
cd /opt/tiu

# Pull latest changes
OUTPUT=$(git pull 2>&1)

# If there are new changes, rebuild
if echo "$OUTPUT" | grep -q "Already up to date"; then
    exit 0
fi

echo "[$(date)] Changes detected: $OUTPUT" >> /var/log/auto-deploy.log

# Rebuild and restart web container
docker compose up -d --build web

# Run migrations
docker compose exec -T web python manage.py migrate --noinput

echo "[$(date)] Deploy complete" >> /var/log/auto-deploy.log
