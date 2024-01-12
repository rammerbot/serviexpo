from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'serviexpo',
        'USER': 'serviexpo_user',
        'PASSWORD': 'ServiExpo_2024',
        'HOST': 'localhost',  
        'PORT': '5432',       
    }
}

CSRF_COOKIE_SECURE = True
