# -*- coding: UTF-8 -*-

from sqlalchemy import *


metadata = MetaData()

notes = Table('notes', metadata,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('note', String(1024), nullable=False),
    Column('publish_date', DateTime, nullable=False),
    Column('visits', Integer, nullable=False),
    Column('user_id', Integer, nullable=False),
)

users = Table('users', metadata,
    Column('id', Integer, autoincrement=True, primary_key=True),
    Column('name', String(32), nullable=False),
    Column('passwd', String(128), nullable=False),
    Column('email', String(128), nullable=False),
    Column('sex', String(1), nullable=True),
    Column('description', String(256), nullable=True)
)


def create_tables(url):
    engine = create_engine(url)
    metadata.create_all(engine)


def drop_tables(url):
    engine = create_engine(url)
    metadata.drop_all(engine)


def connect(url):
    return create_engine(url)
