#!/bin/bash
# Run this ONCE on a fresh Digital Ocean server
# ssh root@165.245.177.94 then paste this script
set -e

echo "=== TIU Server Initial Setup ==="

# 1. Install Docker
echo "[1/5] Installing Docker..."
apt update
apt install -y docker.io docker-compose-plugin git
systemctl enable docker
systemctl start docker

# 2. Clone repo
echo "[2/5] Cloning repository..."
git clone https://github.com/urolovforever/uniwebsite.git /opt/tiu
cd /opt/tiu

# 3. Create .env.prod
echo "[3/5] Creating environment file..."
cat > .env.prod << 'EOF'
DJANGO_SETTINGS_MODULE=tiu_project.settings.prod
DJANGO_SECRET_KEY=@jn34#5q53fmck4mi$*gb_+*#94(qeq$weel9)z7@35_!lj@47
ALLOWED_HOSTS=new.tiu.uz,165.245.177.94
CSRF_TRUSTED_ORIGINS=https://new.tiu.uz

DB_NAME=tiu
DB_USER=tiu
DB_PASSWORD=TiU_Pr0d_2026!xK9m
DB_HOST=db
DB_PORT=5432
EOF

# 4. Start with HTTP first (to get SSL cert)
echo "[4/5] Starting services (HTTP mode)..."
cp nginx/default.initial.conf nginx/default.conf
docker compose up -d db
sleep 5
docker compose up -d --build web
docker compose exec -T web python manage.py migrate --noinput

# Create superuser
docker compose exec -T web python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser('admin', 'admin@tiu.uz', 'TiU_Admin_2026!')
    print('Superuser created')
else:
    print('Superuser exists')
"

docker compose up -d nginx

# 5. Get SSL certificate
echo "[5/5] Getting SSL certificate..."
docker compose run --rm certbot certonly \
    --webroot --webroot-path=/var/www/certbot \
    --email admin@tiu.uz --agree-tos --no-eff-email \
    -d new.tiu.uz

# Switch to HTTPS nginx config
cp nginx/default.conf nginx/default.http.conf
cat > nginx/default.conf << 'NGINXCONF'
upstream django {
    server web:8000;
}

server {
    listen 80;
    server_name new.tiu.uz 165.245.177.94;
    location /.well-known/acme-challenge/ { root /var/www/certbot; }
    location / { return 301 https://$host$request_uri; }
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
NGINXCONF

docker compose restart nginx

echo ""
echo "=== Setup Complete! ==="
echo "Site: https://new.tiu.uz"
echo "Admin: https://new.tiu.uz/admin"
echo "Login: admin / TiU_Admin_2026!"
echo ""
echo "IMPORTANT: Change admin password after first login!"
echo "Auto-deploy is configured via GitHub Actions."
