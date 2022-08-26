from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://unguocra.herokuapp.com']
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd3s3cjbn8fg5nm',
        'USER': 'cqbkgalxxbswhv',
        'PASSWORD': 'ff05807bbf1a51bdb07259a7223027262abacf7f52b7491f538e9be924cc89b4',
        'HOST': 'ec2-3-213-228-206.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

import django_heroku
django_heroku.settings(locals())