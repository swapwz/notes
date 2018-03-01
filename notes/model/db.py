# -*- coding: UTF-8 -*-

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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


def get_session(url):
    engine = get_engine(url)
    db_session = sessionmaker(bind=engine)
    return db_session()


def put_session():
    if hasattr(g, 'session'):
        g.session.close()
    put_engine()
