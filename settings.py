"""
Django settings for todosite project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l44%32bsez_5q_75*zu3kz^v)66%=-11h=u3zg2f@#z@pxweu2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':
        ('rest_framework.authentication.OAuth2Authentication',
         'rest_framework.authentication.SessionAuthentication'),

    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.ModelSerializer',

    'DEFAULT_PERMISSION_CLASSES':
    ('rest_framework.permissions.IsAdminUser',)
}

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'rest_framework',
    'provider',
    'provider.oauth2',
    'todo'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'todosite.urls'

WSGI_APPLICATION = 'todosite.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
