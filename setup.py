# -*- coding: UTF-8 -*-

import os

from notes.model import db
from notes import config


if __name__ == '__main__':
    try:
        if not os.path.exists(config.DB_LOCATION):
            os.mkdir(config.DB_LOCATION)
    except Exception as e:
        print e
    else:
        print "Create tables for notes"
        db.create_tables(config.DATABASE)
