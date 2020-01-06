# -*- coding: utf-8 -*-

from .settings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Setting of Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    
    # Setting loggers
    'loggers': {
        # For Django
        'django': {
             'handlers': ['console'],
             'level': 'INFO',
        },
        # For App "diary"
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
    
    # Setting handlers
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },
    
    # Setting formatters
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'