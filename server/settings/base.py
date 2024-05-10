from server.settings import BASE_DIR, env

#
# General Settings
#

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
# Database
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

THIRD_PARTY_APPS = []

LOCAL_APPS = [
    "apps.sensor",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

#
# Authentication
#

BASE_PASSWORD_VALIDATOR = "django.contrib.auth.password_validation"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": f"{BASE_PASSWORD_VALIDATOR}.UserAttributeSimilarityValidator"},
    {"NAME": f"{BASE_PASSWORD_VALIDATOR}.MinimumLengthValidator"},
    {"NAME": f"{BASE_PASSWORD_VALIDATOR}.CommonPasswordValidator"},
    {"NAME": f"{BASE_PASSWORD_VALIDATOR}.NumericPasswordValidator"},
]

#
# Templates
#

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

#
# WSGI
#

WSGI_APPLICATION = "server.wsgi.application"

#
# Static files (CSS, JavaScript, images)
#

STATIC_URL = "static/"
