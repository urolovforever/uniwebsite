FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gettext \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN DJANGO_SETTINGS_MODULE=tiu_project.settings.prod \
    DJANGO_SECRET_KEY=build-only-key \
    python manage.py collectstatic --noinput

# Compile translation messages
RUN DJANGO_SETTINGS_MODULE=tiu_project.settings.prod \
    DJANGO_SECRET_KEY=build-only-key \
    python manage.py compilemessages

EXPOSE 8000

CMD ["gunicorn", "tiu_project.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]
