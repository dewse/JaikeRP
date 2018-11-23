from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
import pymysql  
pymysql.install_as_MySQLdb()

print("hello!")

# engine = create_engine('mysql://root@localhost')  

# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()

# class User(Base):
    # __tablename__ = 'users'
    
    # id = Column(Integer, primary_key=True)
    # name = Column(String)
    # fullname = Column(String)
    # password = Column(String)
    
    # def __repr__(self):
        # return "<User(name='%s', fullname='%s', password='%s')>" % (
                            # self.name, self.fullname, self.password)
                            
# User.__table__ 
# Table('users', MetaData(bind=None),
            # Column('id', Integer(), primary_key=True, nullable=False),
            # Column('name', String()),   
            # Column('fullname', String()),
            # Column('password', String()), schema=None)