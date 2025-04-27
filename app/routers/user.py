from fastapi import FastAPI, Response, status, HTTPException,Depends
from pydantic import BaseModel
from .. import models,schemas,utils
from typing import Optional,List    
from sqlalchemy.orm import Session
from ..database import get_db
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from passlib.context import CryptContext
from fastapi import APIRouter

router=APIRouter(prefix="/users",tags=["Users"])  #prefix le chai sabai endpoint ma /users halne ho ani tags le chai documentation ma k k huncha bhanera bujhna sajilo huncha

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate,db:Session=Depends(get_db)):

    #hash the password - user.password
    #hashed_password=pwd_context.hash(user.password)
    hashed_password=utils.hash(user.password)
    
    user.password=hashed_password
    #user.password liyera hash main.py ma garayera ani feri user.password mai halne then after that table ma halne!!!!!!
    new_user=models.User(**user.dict())      #update and create garda kheri data jun halincha ni tyo ta Dictionary ma convet garera halne 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)   #id refresh garesi ID change huncha ni ta naya user lai ONLY IN POST MA HUNCHA YO CHUTIYAPA
    return new_user

#password back response ma aairako thio so we did the reponse model 

@router.get("/{id}",response_model=schemas.UserResponse)
async def get_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with {id} doesnot exist")
    return user


