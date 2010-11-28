"""
The settings.gdev module contains settings intended for development using
the built-in Django http server and an sqlite3 database.
"""
import os
from common import VIDEOPORTRAIT_ROOT, MIDDLEWARE_CLASSES

DEBUG = True
TEMPLATE_DEBUG = DEBUG

CONFIG_SETTINGS = 'beta'

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(VIDEOPORTRAIT_ROOT,'devel.sqlite')
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

ADMIN_MEDIA_PREFIX = '/media/admin'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_ROOT = '/home/robertlray/beta.videoportrait.net/public/media'
MEDIA_URL = '/media/'

ROOT_URL = "http://beta.videoportrait.net"
