# -*- coding: UTF-8 -*-

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from flask import g

# Register tables
Base = declarative_base()
import note
import user


DB_ENGINE = None


def get_engine(url):
    global DB_ENGINE 
    if DB_ENGINE is None:
        DB_ENGINE = create_engine(url)

    return DB_ENGINE


def put_engine():
    global DB_ENGINE
    if DB_ENGINE:    
        DB_ENGINE.dispose()
    DB_ENGINE = None


def create_tables(url):
    engine = get_engine(url)
    Base.metadata.create_all(engine)
    put_engine()


def drop_tables(url):
    engine = create_engine(url)
    Base.metadata.drop_all(engine)
    put_engine()


def connect(url):
    engine = get_engine(url)
    conn = engine.connect()
    return conn


def disconnect(url):
    if hasattr(g, 'db'):
        g.db.close()
    put_engine()
