# -*- coding: UTF-8 -*-

from notes.db import Base
from sqlalchemy import *


class Note(Base):
    __tablename__ = 'notes'

    id = Column('id', Integer, primary_key=True)
    note = Column('note', String(1024), nullable=False)
    publish_date = Column('publish_date', DateTime, nullable=False)
    visits = Column('visits', Integer, nullable=False)
    user_id = Column('user_id', Integer, nullable=False) 


    def __repr__(self):
        return "<Notes(id = %s, note = '%r', publish_date = '%s', visits = '%s', user_id = '%s')>" %  \
               (self.id, self.note, self.publish_date, self.visits, self.user_id)
    
