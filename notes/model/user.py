# -*- coding: UTF-8 -*-

from notes.db import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    name = Column('name', String(32), nullable=False)
    passwd = Column('passwd', String(128), nullable=False)
    nicky = Column('nicky', String(32), nullable=False)
    email = Column('email', String(128), nullable=False)
    sex = Column('sex', String(1), nullable=True)
    description = Column('description', String(256), nullable=True)
