import os

env = os.environ.get('DJANGO_SETTINGS_MODULE')
if not env:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tiu_project.settings.dev')
