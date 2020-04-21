from datetime import timedelta

from .settings import *

DATABASES = {
     'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': 'geo1',
         'USER': 'postgres',
         'PASSWORD': '',
         'HOST': 'localhost',
         'PORT': '5432',
     }
 }
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),

}

CORS_ORIGIN_WHITELIST = [
    "https://example.com",
]