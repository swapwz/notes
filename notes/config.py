# -*- coding: UTF-8 -*-

# develop mode
DEBUG = True

# the source py inside
WEB_ROOT = '/var/www/notes'

# store the database file
DB_LOCATION = '/var/run/notes'
DB_NAME = 'notes.db'
DATABASE = 'sqlite:///%s/%s' % (DB_LOCATION, DB_NAME)

# Admin key
SECRET_KEY = 'matrix2018'

UPLOAD_DIR = '/var/www/notes/upload'
