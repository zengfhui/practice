# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,DateTime

engine = create_engine('mysql://root@localhost/shiyanlougithub')
Base = declarative_base()

class Repository(Base):
	__tablename__ = 'repositories'

	id = Column(Integer,primary_key=True)
	name = Column(String(64),index=True)
	update_time = Column(DateTime)

if __name__ == '__main__':
	Base.metadata.create_all(engine)