# -*- coding: UTF-8 -*-

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Note(Base):
    __tablename__ = 'notes'

    id = Column('id', primary_key=True)
    note = Column('note', String(1024), nullable=False)
    publish_date = Column('publish_date', DateTime, nullable=False)
    visits = Column('visits', Integer, nullable=False)
    user_id = Column('user_id', Integer, nullable=False) 


    def __repr__():
        return "<Notes(id = %s, note = '%s', publish_date = '%s', visits = '%s', user_id = '%s')>" %  \
               (self.id, self.note, self.publish_date, self.visits, self.user_id)
    
