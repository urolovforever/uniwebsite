#!/bin/bash
set -e

echo "=== TIU Website Deployment ==="

# Step 1: Start with initial nginx (no SSL)
echo "[1/6] Starting services with HTTP-only nginx..."
cp nginx/default.initial.conf nginx/default.conf.bak
cp nginx/default.initial.conf nginx/default.conf
docker compose up -d db
echo "Waiting for database to be ready..."
sleep 5

# Step 2: Build and start web
echo "[2/6] Building and starting web service..."
docker compose up -d --build web

# Step 3: Run migrations
echo "[3/6] Running database migrations..."
docker compose exec web python manage.py migrate --noinput

# Step 4: Create superuser (if not exists)
echo "[4/6] Creating superuser..."
docker compose exec web python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser('admin', 'admin@tiu.uz', 'TiU_Admin_2026!')
    print('Superuser created: admin / TiU_Admin_2026!')
else:
    print('Superuser already exists.')
"

# Step 5: Start nginx
echo "[5/6] Starting nginx..."
docker compose up -d nginx

# Step 6: Get SSL certificate
echo "[6/6] Getting SSL certificate..."
docker compose run --rm certbot certonly \
    --webroot --webroot-path=/var/www/certbot \
    --email admin@tiu.uz --agree-tos --no-eff-email \
    -d new.tiu.uz

# Switch to SSL nginx config
echo "Switching to SSL nginx config..."
cp nginx/default.conf.bak nginx/default.conf
# Restore the SSL config
cat > nginx/default.conf << 'NGINXEOF'
upstream django {
    server web:8000;
}

server {
    listen 80;
    server_name new.tiu.uz 165.245.177.94;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name new.tiu.uz;

    ssl_certificate /etc/letsencrypt/live/new.tiu.uz/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/new.tiu.uz/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    client_max_body_size 20M;

    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml text/javascript image/svg+xml;
    gzip_min_length 256;

    location /media/ {
        alias /app/media/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location / {
        proxy_pass http://django;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }
}
NGINXEOF

docker compose restart nginx

echo ""
echo "=== Deployment Complete! ==="
echo "Site: https://new.tiu.uz"
echo "Admin: https://new.tiu.uz/admin"
echo "Admin credentials: admin / TiU_Admin_2026!"
echo ""
echo "IMPORTANT: Change the admin password after first login!"
