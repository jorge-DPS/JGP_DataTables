# -*- coding: utf-8 -*-

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
from config.settings.components import env

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('POSTGRES_DB', default='jgp_db'),
        'USER': env('POSTGRES_USER', default='jgp_user'),
        'PASSWORD': env('POSTGRES_PASSWORD', default='12345678x'),
        'HOST': env('POSTGRES_HOST', default='db'),
        'PORT': env('POSTGRES_PORT', default='3306'),
        #'CONN_MAX_AGE': env('POSTGRES_CONN_MAX_AGE', default=60),
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES', innodb_strict_mode=1",
            'connect_timeout': 10,
            # Tell MySQLdb to connect with 'utf8mb4' character set
            'charset': 'utf8mb4',
        },
        # Tell Django to build the test database with the 'utf8mb4' character set
        'TEST': {
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci',
        }
    },
}
