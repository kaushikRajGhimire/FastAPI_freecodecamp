from fastapi import APIRouter,Depends, HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas,utils

router=APIRouter(tags=["Authentication"])

@router.post("/login")
async def login(user_credentials:schemas.UserLogin,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==user_credentials.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")   #not real email or password bhanne haina hai GUESS GARNA SAJILO KINA BANAUNE ni??? JUST WRITE "Invalid Credentials"
    #let them figure out if it is the email or password that is wrong THIS IS THE BEST PRACTICE OF BACKEND SECURITY

    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    
    #create a token
    #return a token
    
