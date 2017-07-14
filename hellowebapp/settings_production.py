# Inherit from standard settings file for defaults
from hellowebapp.settings import *

# Overriding standard settings:

# Parse database configuration for $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto" header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Disable debug mode
DEBUG = False

# Static assert configuration
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
