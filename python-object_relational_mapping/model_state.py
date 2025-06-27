#!/usr/bin/python3
"""
File that contains the class definition
of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

engine = create_engine("mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa")

Base.metadata.create_all(engine)




