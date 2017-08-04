# -*- coding: utf-8 -*-
from odbx.settings import root, env
import datetime

# Full filesystem path to the project.
PROJECT_ROOT = root('.')

# Name of the project.
PROJECT_NAME = 'odbx'

gettext_noop = lambda s: s

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

SITE_TITLE = gettext_noop(u'报修')

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = root('media')


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = root('../site-static')


# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    root('static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-%f=!ig(bhui8zxf6r7s0s49*6g#p3nkis-qj*k1*xn%r_3r=0'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'odbx.accounts.middleware.UserAccessControl',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'odbx.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'odbx.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    root('templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'crispy_forms',

    'south',

    'rest_framework',
    'odbx.alarms',
    'odbx.api',
    'odbx.accounts',
)


LOGIN_URL = '/auth/login/'
LOGOUT_URL = '/auth/logout'
DEFAULT_REDIRECT_URL = '/'

SOUTH_TESTS_MIGRATE = False

# cache-machine 使用的 cache 前缀, 默认为项目的名称
CACHE_PREFIX = 'odbx'

CRISPY_TEMPLATE_PACK = 'bootstrap'


# email configuration
email_config = env.email_url(default='consolemail://')
vars().update(email_config)
EMAIL_SUBJECT = u'change_me'


# compressor configuration
INSTALLED_APPS += ('compressor',)
STATICFILES_FINDERS += ('compressor.finders.CompressorFinder', )
COMPRESS_CSS_HASHING_METHOD = 'hash'
COMPRESS_ROOT = root('static')
COMPRESS_OUTPUT_DIR = 'assets'
root('static/assets', ensure=True)
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
    ('text/x-scss', 'compressor_compass.PyScssFilter'),
    ('text/stylus', 'stylus < {infile} > {outfile}'),
)

# If you set this to False, Django will disable captcha when register, getpass
USE_CAPTCHA = True
JS_REFRESH = u'<a href="javascript:void(0);" class="js-captcha-refresh">' + gettext_noop(u'换一换') + '</a>'
CAPTCHA_OUTPUT_FORMAT = u'%(hidden_field)s %(text_field)s %(image)s' + JS_REFRESH

INSTALLED_APPS += ('captcha', )

# If you set this to True, will use Celery for async call on some methods.
USE_QUEUE = env.bool('USE_QUEUE', default=False)

if USE_QUEUE:
    #
    # 使用MQ, 必须配置 BROKER_URL
    #
    BROKER_URL = env('BROKER_URL')
    INSTALLED_APPS += ('djcelery', )

    import djcelery
    djcelery.setup_loader()


try:
    import django_extensions
except ImportError:
    django_extensions = None
else:
    INSTALLED_APPS += ('django_extensions', )


INSTALLED_APPS += ('dbbackup', )
DBBACKUP_STORAGE = 'dbbackup.storage.filesystem_storage'
DBBACKUP_FILESYSTEM_DIRECTORY = root('../backups', ensure=True)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),

    # Pagination
    'PAGINATE_BY': 20,
    'PAGINATE_BY_PARAM': 'count',
    'MAX_PAGINATE_BY': 100,

    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=14)
}
