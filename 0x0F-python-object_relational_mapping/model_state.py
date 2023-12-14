#!/usr/bin/python3
''' model base for state '''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Column, Integer, String

mymetadata = MetaData()
Base = declarative_base(metadata=mymetada)

Class State(Base):
    ''' class with id and name attributes of each state '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String)

Base.metadata.create_all(engine)
