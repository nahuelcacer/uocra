from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd1fh99c5hhvk2p',
        'USER': 'wrcylugcygjpte',
        'PASSWORD': '97e55cf7826b271cc1de21f1a860d68a4f88a64ff4d91b9aa93db18ca6c8f5c8',
        'HOST': 'ec2-44-206-11-200.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

import django_heroku
django_heroku.settings(locals())