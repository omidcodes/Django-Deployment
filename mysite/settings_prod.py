from .settings import *
import os

DEBUG = False
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com'] # TODO : CHANGE it 

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']  # TODO : FIXME 

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
