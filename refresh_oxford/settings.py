# Django settings for refresh_oxford project.
import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
import dj_database_url


DIRNAME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

DEBUG = bool(os.environ.get('DEBUG', False))
DEVELOPMENT_SITE = bool(os.environ.get('DEVELOPMENT_SITE', False))

DATABASES = {'default': dj_database_url.config(default='postgres://localhost/refresh_oxford')}

ADMINS = (('Admin', 'bugs@incuna.com'),)
MANAGERS = ADMINS
ADMIN_EMAILS = zip(*ADMINS)[1]
EMAIL_SUBJECT_PREFIX = '[refresh_oxford] '
SERVER_EMAIL = DEFAULT_FROM_EMAIL = 'info@incuna.com'
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')

TIME_ZONE = 'UTC'
USE_L10N = True  # Locale
USE_TZ = True

LANGUAGE_CODE = 'en-GB'
USE_I18N = False  # Internationalization

# Static
MEDIA_ROOT = os.path.join(DIRNAME, 'client_media')
MEDIA_URL = '/client_media/'
STATIC_ROOT = os.path.join(DIRNAME, 'static_media')
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DEBUG = DEBUG
TEMPLATE_DIRS = (os.path.join(DIRNAME, 'templates'))
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'admin_sso.auth.DjangoSSOAuthBackend',
    'incuna_auth.backends.CustomUserModelBackend',
)

ROOT_URLCONF = 'refresh_oxford.urls'
SECRET_KEY = '$$g6*tl!&amp;u4kd9!cs*re9#-u+xe!)25)m0(&amp;*1%8k*p*&amp;^cc6i'
SITE_ID = 1
WSGI_APPLICATION = 'refresh_oxford.wsgi.application'

INSTALLED_APPS = (
    # Project Apps
    'refresh_oxford',

    # Libraries
    'admin_sso',
    'crispy_forms',
    'south',
    'debug_toolbar',
    'django_extensions',
    'gunicorn',
    'raven.contrib.django',

    # Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

SENTRY_DSN = 'http://6ca204de023846108a3ae330bfe74ef5:c6060bcafb4f4a22989f7d7470dc77d4@sentry.incuna.com/21'
SENTRY_TESTING = DEBUG
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Debug Toolbar
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
INTERNAL_IPS = ('127.0.0.1',)

