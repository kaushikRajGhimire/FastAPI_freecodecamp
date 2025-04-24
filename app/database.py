#it handles all the database connections
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#connetion string looks something like this
#  postgresql://<username>:<password>@<ip-address>:<port>or hostname like localhost or server/<database-name>
SQLALCHEMY_DATABASE_URL="postgresql://postgres:yourpassword@localhost/first_fastapi"  #connection string for postgresql

engine=create_engine(SQLALCHEMY_DATABASE_URL)  #creating the engine that connects POSTGRESQL to SQLALCHEMY

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)  #creating the session local object that will be used to create the session for each request
Base=declarative_base()  #creating the base class that will be used to create the models ALWAYS TO MAKE TABLES IN POSTGRES WE WILL BE EXTENDING THIS BASE CLASS

#JUST the postgresql URL will change others all copy paste in all projects


#depencency
def get_db():   #CREATE SESSION WHENEVER WE GET A REQUEST TO ANY API ENDPOINT
    #this function will be used to create a session for each request
    #and close the session after the request is done
    db=SessionLocal()  #creating the session for each request
    try:
        yield db  #yielding the session to be used in the request
    finally:
        db.close()  #closing the session after the request is done
#yo chai database ma connect garne kaam garcha
