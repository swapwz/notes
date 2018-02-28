# -*- coding: UTF-8 -*-

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from flask import g

import user
import note

Base = declarative_base()

DB_ENGINE = None


def get_engine(url):
    global DB_ENGINE 

    if DB_ENGINE is None:
        DB_ENGINE = create_engine(url)
    return DB_ENGINE


def create_tables(url):
    engine = get_engine(url)
    Base.metadata.create_all(engine)


def drop_tables(url):
    engine = create_engine(url)
    Base.metadata.drop_all(engine)


def connect(url):
    engine = get_engine(url)
    conn = engine.connect()

    return conn


def disconnect(url):
    if hasattr(g, 'db'):
        g.db.close()
    engine = get_engine(url)
    engine.dispose() 
