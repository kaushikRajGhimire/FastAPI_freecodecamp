from fastapi import FastAPI, Response, status, HTTPException,Depends
from . import models,schemas,utils
from .database import engine
from .routers import post,user,auth

#pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

#k bujhne aahile lai bhane yo tala ko code nai ho josle table banaucha yedi chaina bhane otherwise yedi tei name ko table pahile nai cha bhane chuda ni chudaina SO CHANGES GSRDA TABLE DELETE GARNE KURO AAYENA DATA LOSS SO WE USE ALEMBIC FOR DATA MIGRATION

#password hashing ko lagi ho KUN ALGORITHM USE GARNE BHANERA MENTION GAREKO

models.Base.metadata.create_all(bind=engine)  #creating the tables in the database using the models defined in the models.py file

app=FastAPI()

app.include_router(post.router) #importing the post router from the post.py file
app.include_router(user.router) #importing the user router from the user.py file
app.include_router(auth.router) #importing the auth router from the auth.py file
#MODULAR BANAKO K CODE LAI MATLAB YEDI USER WALA CHAIYO BHANE USER WALA TAKKA NIKALERA LAGE HUNCHA MODULAR CODE MA SAME LIKE JASARI AJAY KO LOGIN KO CODE UTHAYERA SABAI PROJECTS MA HALKA EDIT MAI GARNA SAKINCHA
#REQUEST TA AAUCHA NORMAL MATHI BATA TALA SAMMA LINE BY LINE BUT ABA ROUTER OBJECT PATTA LAGAUCHA ANI TYO post.router ma JANCHA,yedi user wala request raicha bhane user.router ma jancha tyo FILE ma

#MATLAB SABAI THOK EUTAI MAIN.py FILE MA RAKHERA LONG INFERENCE TIME NI LAGCHA PLUS MODULAR PANI HUDAINA





   

    
