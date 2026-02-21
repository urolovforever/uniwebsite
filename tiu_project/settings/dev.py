from .base import *  # noqa: F401,F403

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tiu',
        'USER': 'tiu',
        'PASSWORD': 'tiu',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
