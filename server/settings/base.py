from pathlib import Path

from server.settings import env

#
# General Settings
#

BASE_DIR = Path(__file__).parent.parent.parent

SECRET_KEY = env("DJANGO_SECRET_KEY", default="django-secret-key")

DEBUG = env.bool("DJANGO_DEBUG", default=True)

APPEND_SLASH = False

#
# Internationalization
#

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

#
# Middlewares
#

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

#
# Databases
#

DATABASES = {"default": env.db()}

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#
# URLs
#

ROOT_URLCONF = "server.urls"

#
# Apps
#

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS: list[str] = []

LOCAL_APPS = [
    "sensor",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
