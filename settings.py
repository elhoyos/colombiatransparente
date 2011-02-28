# Settings para ColombiaTransparente

# local_settings.py debe de exister
# con los siguiente variables
"""
DEBUG = False
TEMPLATE_DEBUG = DEBUG
STAGING = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite',.
        'NAME': 'transparente.db', 
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = 'KEYLOCAasjahjshdlkjsajhsa*A98798hjdhsdj'
"""

from local_settings import *

import os.path
PROJECT_DIR = os.path.dirname(__file__)

# A estos usarios se les manda emails 
# cuando hay excepciones
ADMINS = (
    ('Julian Pulgarin', 'jp@julianpulgarin.com'),
)

SEND_BROKEN_LINK_EMAILS = True
MANAGERS = ADMINS

TIME_ZONE = 'America/Bogota'

LANGUAGE_CODE = 'es-co'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media/')

if STAGING:
    MEDIA_URL = 'http://staging.colombiatransparente.co/media/'
    ADMIN_MEDIA_PREFIX = 'http://staging.colombiatransparente.co/media/admin/'
elif DEBUG:
    MEDIA_URL = 'http://localhost:8000/media/'
    ADMIN_MEDIA_PREFIX = 'http://localhost:8000/media/admin/'
else:
    MEDIA_URL = 'http://www.colombiatransparente.co/media/'
    ADMIN_MEDIA_PREFIX = 'http://www.colombiatransparente.co/media/admin/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages"
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'transparencia',
    'sorl.thumbnail',
    'django_bcrypt',
    'django.contrib.markup',
)
