"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.conf import settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qe7smplozq(nr5y2z1c5bf499zv=-s3820czw40v(#(pb0&+u&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MARTOR_ENABLE_CONFIGS = getattr(
    settings, 'MARTOR_ENABLE_CONFIGS', {
        'emoji': 'true',        # to enable/disable emoji icons.
        'imgur': 'true',        # to enable/disable imgur/custom uploader.
        'mention': 'true',     # to enable/disable mention
        'jquery': 'true',       # to include/revoke jquery (require for admin default django)
        'living': 'true',      # to enable/disable live updates in preview
        'spellcheck': 'false',  # to enable/disable spellcheck in form textareas
        'hljs': 'true',         # to enable/disable hljs highlighting in preview
    }
)

import time
MARTOR_UPLOAD_PATH = 'images/uploads/{}'.format(time.strftime("%Y/%m/%d/"))
MARTOR_UPLOAD_URL = '/api/uploader/'  # change to local uploader

MAX_IMAGE_UPLOAD_SIZE = 5242880  # 5MB

# To setup the martor editor with label or not (default is False)
MARTOR_ENABLE_LABEL = True

# Imgur API Keys
MARTOR_IMGUR_CLIENT_ID = 'your-client-id'
MARTOR_IMGUR_API_KEY   = 'your-api-key'

# Safe Mode
MARTOR_MARKDOWN_SAFE_MODE = True # default

# Markdownify
MARTOR_MARKDOWNIFY_FUNCTION = 'martor.utils.markdownify' # default
MARTOR_MARKDOWNIFY_URL = '/martor/markdownify/' # default

# Markdown extensions (default)
MARTOR_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.nl2br',
    'markdown.extensions.smarty',
    'markdown.extensions.fenced_code',

    # Custom markdown extensions.
    'martor.extensions.urlize',
    'martor.extensions.del_ins',    # ~~strikethrough~~ and ++underscores++
    'martor.extensions.mention',    # to parse markdown mention
    'martor.extensions.emoji',      # to parse markdown emoji
    'martor.extensions.mdx_video',  # to parse embed/iframe video
]

# Markdown Extensions Configs
MARTOR_MARKDOWN_EXTENSION_CONFIGS = {}

# Markdown Extensions
# MARTOR_MARKDOWN_BASE_EMOJI_URL = 'https://www.webfx.com/tools/emoji-cheat-sheet/graphics/emojis/'     # from webfx
MARTOR_MARKDOWN_BASE_EMOJI_URL = 'https://github.githubassets.com/images/icons/emoji/'                  # default from github
MARTOR_MARKDOWN_BASE_MENTION_URL = 'https://python.web.id/author/'                                      # please change this to your domain

# Application definition
CSRF_COOKIE_HTTPONLY = False

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'news',
    'category',
    'subcategory',
    'martor',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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


WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'newsdb',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST':'localhost',
        'PORT':'5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR,'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
