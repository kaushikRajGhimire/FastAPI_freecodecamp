from fastapi import APIRouter,Depends, HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas,utils,oauth
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
router=APIRouter(tags=["Authentication"])

# @router.post("/login")
# async def login(user_credentials:schemas.UserLogin,db:Session=Depends(get_db)):
#     user=db.query(models.User).filter(models.User.email==user_credentials.email).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")   #not real email or password bhanne haina hai GUESS GARNA SAJILO KINA BANAUNE ni??? JUST WRITE "Invalid Credentials"
#     #let them figure out if it is the email or password that is wrong THIS IS THE BEST PRACTICE OF BACKEND SECURITY

#     if not utils.verify(user_credentials.password,user.password):
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    
#     #create a token
#     access_token=oauth.create_access_token(data={"user_id":user.id})   #dictionary format ma data pathaune PAYLOAD ho yo, ARU LIKE SCOPE OF ROLE OF DIFFERENT ENDPOINTS HARU PANI HALNA SAKINCHA,EMAIL ETC.

#     #return a token
#     return {"access_token":access_token,"token_type":"bearer"}    #what kind of token is it, like bearer token or something else
# #yo chai frontend ma pathaune ho ani frontend bata token lai use garera aru endpoint haru ma access garna sakinchha



@router.post("/login",response_model=schemas.Token)
async def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):   #creating a token endpoint ho yo chai

    """Oauth2PasswordRequestForm le chai fastapi ko built in class ho jun chai FORM data lincha frontend bata ani POST request ma use garnu parcha ani USERNAME="DFSA" RA PASSWORD="ASLDG" MARTRA STORE GARCHA AFNO DICTIONARY MA"""
    user=db.query(models.User).filter(models.User.email==user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")   #not real email or password bhanne haina hai GUESS GARNA SAJILO KINA BANAUNE ni??? JUST WRITE "Invalid Credentials"
    #let them figure out if it is the email or password that is wrong THIS IS THE BEST PRACTICE OF BACKEND SECURITY

    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    
    #create a token
    access_token=oauth.create_access_token(data={"user_id":user.id})   #dictionary format ma data pathaune PAYLOAD ho yo, ARU LIKE SCOPE OF ROLE OF DIFFERENT ENDPOINTS HARU PANI HALNA SAKINCHA,EMAIL ETC.

    #return a token
    return {"access_token":access_token,"token_type":"bearer"}    #what kind of token is it, like bearer token or something else
#yo chai frontend ma pathaune ho ani frontend bata token lai use garera aru endpoint haru ma access garna sakinchha

