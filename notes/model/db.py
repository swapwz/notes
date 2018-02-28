# -*- coding: UTF-8 -*-

from sqlite3 import dbapi2 as sqlite3


def init(path):
    db = connect(path)
    with open('notes/model/sql/schema.sql', 'r') as f:
        db.cursor().executescript(f.read()) 
    db.commit()


def connect(path):
    """ Connects to the specific database. """
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    return db
