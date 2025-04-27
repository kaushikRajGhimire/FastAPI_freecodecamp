#EACH MODEL DEFINES A TABLE IN THE DATABASE
from sqlalchemy import Column,Integer,String,Boolean,TIMESTAMP 
from .database import Base
from sqlalchemy.sql.expression import text

class Post(Base):            #make sure that the class name is same as the table name in the database also ALWAYS CAPITALIED
    __tablename__="posts"  #table name in the database
    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    publised=Column(Boolean,server_default='True',nullable=False)  #baas default=true le hudaina hai Default set garnu parcha yesari
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))  #timestamp aahile thakkai jatibela post gare teti bela ko lincha accroding to timezone
    #timestamp column halnu cha
    #server_default=text("now()") le server ma jati bela post garyo teti bela ko time lincha
   #chaina table bhane banaucha but cha bhane kei gardaina pgadmin4 ma so edit garna either delete whole table and run again the code by SAVING or USE ALEMBIC FOR DATA MIGRATION


#user registration handle garna lai
class User(Base):
    __tablename__="users"      #table name in the database
    id=Column(Integer,primary_key=True,nullable=False)         #95% case ma yei line copy paste huncha ID ma                     
    email=Column(String,nullable=False,unique=True)          #eutai email le dui choti register garna sakdaina
    password=Column(String,nullable=False)                   #duita user ko eutai password ta huna sakcha nii 
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()")) #WHENEVER YOU PUT SOMETHING IN THE DATABASE YOU WANT TO KNOW WHEN YOU DID THAT MAXIMUM OF TIMES

    
