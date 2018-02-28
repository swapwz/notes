# -*- coding: UTF-8 -*-

DEBUG = True
DB_LOCATION = '/var/run/notes'
DB_NAME = 'notes.db'
DATABASE = 'sqlite:///%s/%s' % (DB_LOCATION, DB_NAME)
SECRET_KEY = 'yoursecretkey'
