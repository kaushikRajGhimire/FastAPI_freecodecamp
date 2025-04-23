#EACH MODEL DEFINES A TABLE IN THE DATABASE
from sqlalchemy import Column,Integer,String,Boolean    
from .database import Base

class Post(Base):            #make sure that the class name is same as the table name in the database also ALWAYS CAPITALIED
    __tablename__="posts"  #table name in the database
    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    publised=Column(Boolean,default=True)
    #timestamp column halnu cha

    