from lib2to3.pytree import Base
from sqlalchemy import create_engine, Column, Integer, String, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# echo True will print in the console (in SQL) what happens when the file is run
engine = create_engine('sqlite:///users.db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine) # binds user to db
session = Session()

class User(Base): # inherits from Base class
    __tablename__='users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f'<User (name={self.name}, fullname={self.fullname}, nickname={self.nickname})>'

if __name__=='__main__':
    Base.metadata.create_all(engine)
