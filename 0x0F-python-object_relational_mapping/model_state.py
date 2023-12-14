#!/usr/bin/python3
''' model base for state '''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Column, Integer, String

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

Class State(Base):
    ''' class with id and name attributes of each state '''
    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
