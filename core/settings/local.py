#settting file for local environment
#DEBUG = True
#Locally we use SQLit, so we mention Database config in this file
# for code re-usability, we import base.py file

from .base import *

#SQLite3 Config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}