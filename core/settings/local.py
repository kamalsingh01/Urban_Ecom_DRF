#settting file for local environment
#DEBUG = True
#Locally we use SQLit, so we mention Database config in this file
# for code re-usability, we import base.py file

from .base import *

#SQLite3 Config
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'urban_ecom',
       'USER': 'kasin',
       'PASSWORD': 'dockare22',
       'HOST': '127.0.0.1',
       'PORT': '5432',
   }
}

