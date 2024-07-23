from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Seguridad básica
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
ALLOWED_HOSTS = ['.rammerbot.com']
CSRF_TRUSTED_ORIGINS=['serviexpo.rammerbot.com']

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'serviexpo',
        'USER': 'serviexpo_user',
        'PASSWORD': 'serviexpo',
        'HOST': 'localhost',  
        'PORT': '5432',       
    }
}

CSRF_COOKIE_SECURE = True
