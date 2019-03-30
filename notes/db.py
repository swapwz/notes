# -*- coding: UTF-8 -*-

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import g

# Register tables
Base = declarative_base()
import note
import user
import config as conf


DB_ENGINE = None


def get_engine():
    global DB_ENGINE 
    if DB_ENGINE is None:
        DB_ENGINE = create_engine(conf.DATABASE)

    return DB_ENGINE


def put_engine():
    global DB_ENGINE
    if DB_ENGINE:    
        DB_ENGINE.dispose()
    DB_ENGINE = None


def create_tables():
    engine = get_engine()
    Base.metadata.create_all(engine)
    put_engine()


def drop_tables():
    engine = get_engine()
    Base.metadata.drop_all(engine)
    put_engine()


def get_session():
    engine = get_engine()
    db_session = sessionmaker(bind=engine)
    return db_session()


def put_session():
    if hasattr(g, 'session'):
        g.session.close()
    put_engine()
