from .settings import *

DATABASES = {
     'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': 'geo1',
         'USER': 'postgres',
         'PASSWORD': '',
         'HOST': '',
         'PORT': '5432',
     }
 }

CORS_ORIGIN_WHITELIST = [
    "https://example.com",
]