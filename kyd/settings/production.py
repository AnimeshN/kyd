from kyd.settings.base import *
import json
with open('/etc/config.json') as config_file:
        config = json.load(config_file)

DEBUG = False
ALLOWED_HOSTS = ['104.43.197.79']
SECRET_KEY = config['SECRET_KEY'] 

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': config['DBNAME'],
        'USER': config['DBUSER'],
        'PASSWORD': config['DBPASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}