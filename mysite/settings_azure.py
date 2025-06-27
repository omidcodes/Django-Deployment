from .settings import *
import os


import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'


DEBUG = False
ALLOWED_HOSTS = ['django-deployment-01-arf6e0edczdqgqc8.canadacentral-01.azurewebsites.net'] # TODO : Hardcoded, remove me

# SECRET_KEY = os.environ['DJANGO_SECRET_KEY']  # TODO : FIXME 
