# -*- coding: utf-8 -*-


"""Django settings for server project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/
For the full list of settings and their config, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from typing import Dict, List, Tuple, Union
from os.path import join

from config.settings.components import PROJECT_PATH, env

from django.utils.translation import ugettext_lazy as _

#
# ADMIN SETTINGS
# ------------------------------------------------------------------------------
ADMIN_URL = env('DJANGO_ADMIN_URL', default='admin/')
AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = '/admin/'
LOGIN_URL = 'account_login'
USERNAME_BLACKLIST = ['vicobits', 'admin']

DJANGO_APPS: Tuple[str, ...] = (
    # Default Django apps:
    'django.contrib.auth',

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.redirects',
    # 'django.contrib.postgres',
    'django_mysql',

    # Useful template tags:
    'django.contrib.humanize',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.admindocs',
)

THIRD_PARTY_APPS: Tuple[str, ...] = (
    # Security:

    # Health checks:
    # You may want to enable other checks as well,
    # see: https://github.com/KristianOellegaard/django-health-check
    'health_check',
    'health_check.db',
    'health_check.cache',
    'health_check.storage',

    'constance',

    # API Rest
    'corsheaders',
    'rest_framework',
    'rest_framework_api_key',
    'rest_framework_simplejwt.token_blacklist',
    'django_http_referrer_policy',

    # Async Tasks
    'django_celery_beat',
    'django_celery_results',

    # Assets
    'imagekit',
    # 'compressor',
    'import_export',
    'admin_sso',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'location_field.apps.DefaultConfig',

)

LOCAL_APPS: Tuple[str, ...] = (
    'apps.empresa.app.EmpresaConfig',
    'apps.contrib.app.ContribConfig',
    'apps.accounts.app.AccountsConfig',
    'apps.zona.app.ZonaConfig',
    'apps.grupo.app.GrupoConfig',
    'apps.cajas.app.CajasConfig',
    'apps.deposito.app.DepositoConfig',
    #'apps.corte_moneda.app.CorteMonedaConfig',AlbumConfig
    'apps.administracion.app.AdministracionConfig',
    'apps.credito.app.CreditoConfig',
    'apps.albums.app.AlbumConfig',
   
    
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE: Tuple[str, ...] = (
    'corsheaders.middleware.CorsMiddleware',  # CORS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django_feature_policy.FeaturePolicyMiddleware',  # django-feature-policy
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Django HTTP Referrer Policy:
    'django_http_referrer_policy.middleware.ReferrerPolicyMiddleware',
)


# URL CONFIGURATION
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

# MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
SITE_ID = 1
MIGRATION_MODULES = {
    'sites': 'apps.contrib.sites.migrations',
}


# INTERNATIONALIZATION
# ------------------------------------------------------------------------------
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/La_Paz'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('es', _('Spanish')),
    ('en', _('English')),
]
MODELTRANSLATION_DEFAULT_LANGUAGE = 'es'
LOCALE_PATHS = [
    join(PROJECT_PATH, 'locale'),
]

# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
FIXTURE_DIRS = (
    join(PROJECT_PATH, 'fixtures'),
)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST, EMAIL_PORT = '127.0.0.1', 1025  # Work with MailHog
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='Support <info@jesusgranpoder.com.bo>')


# TEMPLATES CONFIGURATION
# ------------------------------------------------------------------------------
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        join(PROJECT_PATH, 'web/templates'),
    ],
    'OPTIONS': {
        'debug': False,
        'loaders': [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ],
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',
            'django.contrib.messages.context_processors.messages',

            # Custom context processor
            'apps.contrib.context_processors.website',
        ],
    },
}]

# See: http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_HTDOCS_PATH = env('DJANGO_HTDOCS_PATH', default=join(PROJECT_PATH, 'assets'))
STATIC_ROOT = join(DJANGO_HTDOCS_PATH, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    join(PROJECT_PATH, 'web/static'),
)
# STATICFILES_FINDERS = (
#    'django.contrib.staticfiles.finders.FileSystemFinder',
#    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

# Compressor
#    'compressor.finders.CompressorFinder',
# )

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
MEDIA_ROOT = join(DJANGO_HTDOCS_PATH, 'media')
MEDIA_URL = '/media/'


# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

#
# AUTHENTICATION CONFIGURATION
# https://docs.djangoproject.com/en/2.2/topics/auth/
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'admin_sso.auth.DjangoSSOAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
    'apps.contrib.auth_backends.SimpleEmailBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# EXTRA CONFIGURATION
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'
DATA_UPLOAD_MAX_NUMBER_FIELDS = 5000
PAGINATION_PAGE_SIZE = 50
TOKEN_EXPIRATION_DAYS = env.int('DJANGO_TOKEN_EXPIRATION_DAYS', default=7)

# Security
# https://docs.djangoproject.com/en/2.2/topics/security/

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

X_FRAME_OPTIONS = 'DENY'

# https://chipcullen.com/django-3-referrer-policy-change/
SECURE_REFERRER_POLICY = "no-referrer-when-downgrade"

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy#Syntax
REFERRER_POLICY = 'no-referrer'

# https://github.com/adamchainz/django-feature-policy#setting
FEATURE_POLICY: Dict[str, Union[str, List[str]]] = {}  # noqa: TAE002


# Timeouts
EMAIL_TIMEOUT = 5

#
# PLATFORM SETTINGS
# ------------------------------------------------------------------------------
PROJECT_SUPPORT_EMAIL = 'info@jesusgranpoder.com.bo'

ADMINS = (
    ('Support', PROJECT_SUPPORT_EMAIL),
)
MANAGERS = ADMINS

PROJECT_NAME = 'Jesús del Gran Poder S.A.'
PROJECT_HOSTNAME = env('DJANGO_HOSTNAME', default='http://localhost:8000')
PROJECT_AUTHOR = 'Support <{0}>'.format(PROJECT_SUPPORT_EMAIL)
PROJECT_OWNER = 'JGP'
PROJECT_OWNER_DOMAIN = PROJECT_HOSTNAME
PROJECT_DESCRIPTION = 'JGP otorga préstamos de dinero fácil y rápido. Hazlo tú mismo o pide la ayuda de un asesor experto. Solicita tu prestamo ya!'
PROJECT_SUPPORT_PHONE = '(+591) 73234523'
PROJECT_TERMS_URL = '{0}/terms'.format(PROJECT_HOSTNAME)


# ALLAUTH CONFIGURATION
# ------------------------------------------------------------------------------
# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # mandatory, optional, none
ACCOUNT_ALLOW_REGISTRATION = env.bool('DJANGO_ACCOUNT_ALLOW_REGISTRATION', True)
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False
ACCOUNT_LOGIN_ON_PASSWORD_RESET = False
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_USERNAME_BLACKLIST = ["vicobits", "admin"]

ACCOUNT_ADAPTER = 'apps.accounts.adapters.AccountAdapter'
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'account_login'
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = False


# DJANGO LOCATION FIELD CONFIGURATIONS
# ------------------------------------------------------------------------------
# STATIC_URL muestra None en producción. mejor usar '/static/location_field'
LOCATION_FIELD_PATH = STATIC_URL + 'location_field'
LOCATION_FIELD = {
    'map.provider': 'google',
    'map.zoom': 13,

    'search.provider': 'google',
    'search.suffix': '',

    # Google
    'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
    'provider.google.api_key': 'AIzaSyAJ13cVM5Dw--zl5NZteWcD0NxgJ7Cbqv8',
    'provider.google.api_libraries': '',
    'provider.google.map.type': 'ROADMAP',

    # Mapbox
    'provider.mapbox.access_token': '',
    'provider.mapbox.max_zoom': 18,
    'provider.mapbox.id': 'mapbox.streets',

    # OpenStreetMap
    'provider.openstreetmap.max_zoom': 18,

    # misc
    'resources.root_path': LOCATION_FIELD_PATH,
    'resources.media': {
        'js': (
            LOCATION_FIELD_PATH + '/js/jquery.livequery.js',
            LOCATION_FIELD_PATH + '/js/form.js',
        ),
    },
}
"""
"""
