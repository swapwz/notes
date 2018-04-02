# -*- coding: UTF-8 -*-

import os

from notes.model import db
from notes import config


if __name__ == '__main__':
    try:
        if not os.path.exists(config.DB_LOCATION):
            os.mkdir(config.DB_LOCATION)

        print("Create tables for notes")
        db.create_tables(config.DATABASE)

        if not os.path.exists(config.UPLOAD_DIR):
            print("Create upload directory")
            os.mkdir(config.DB_LOCATION)
    except Exception as e:
        print(e)
