# -*- coding: UTF-8 -*-

from notes import config
from notes.model import db


if __name__ == '__main__':
    db.init(config.SQLITE_DB_PATH)
