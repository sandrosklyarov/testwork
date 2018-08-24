# -*- coding: utf-8 -*-
import os

SECRET_KEY = '6_85hwehx&=3wozc!f%*!h$z@wggh)og_qu@#8o+s76y(do4mz'

# import django
# django.setup()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!


DJANGO_SETTINGS_MODULE='correctly_settings'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'emails',
    'common',
]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

EMAIL_LOGIN = 'login@yandex.ru'
EMAIL_PASS = 'password'

ROOT_URLCONF = 'testwork.urls'

WSGI_APPLICATION = 'testwork.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'root',
        'PASSWORD': 'vasya123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        # 'init_command': 'SET storage_engine=INNODB, SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED',
        # 'OPTIONS': {'charset': 'utf8'},
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'


ELASTICSEARCH = {
    'default': {
        'hosts': [
            {
                'host': '127.0.0.1',
                'port': 9200
                # 'verify_certs': True,
                # 'use_ssl': True,
                # 'http_auth': (
                #     <auth_name>,
                #     <auth_passwd>
                # )
            }
        ]
    },
    'dev': {
        'hosts': [
            {
                'host': '127.0.0.1',
                'port': 9200
            }
        ]
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

