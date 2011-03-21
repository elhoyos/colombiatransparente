# Settings para ColombiaTransparente
#
# Debe utilizar local_settings.py para inicializar variables especificas.
# Ver fin del archivo.

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

FIXTURE_DIRS = (
    os.path.join(PROJECT_DIR, 'fixtures'),
)

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


# local_settings.py inicializa variables especificas de la instalacion de CT.
try:
    from local_settings import * # en el mismo directorio que este archivo
except ImportError:
    import sys
    sys.stderr.write("Error: Must use a local_settings.py file to set specific settings for this CT installation.")
    sys.exit(1)
