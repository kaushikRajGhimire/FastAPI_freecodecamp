#anything related to authentication and jwt tokens make this file ALWAYS

from jose import JWTError,jwt #pip install python-jose[cryptography]
from datetime import datetime, timedelta
from . import schemas,database,models
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")  #tokenUrl le chai kun endpoint bata token lincha bhanera bujhna sakinchha ani yo chai login endpoint ho ani yo chai frontend bata token lincha ani backend ma pathaune ho
#yo chai frontend bata token lincha ani backend ma pathaune ho




#SECRET_KEY
#ALGORITHM LIKE
#ACCESS_TOKEN_EXPIRE_MINUTES   how long the user can be logged in using the token!!!! EXPIRATION TIME HALENA BHANE SECURE KAAM HUNCHA

SECRET_KEY="75953f651715e141ef24acc3c09c27b9f8400a2aa5144cf48b3728c155780752"     #terminal ma "openssl rand -hex 32" le generate garna sakinchha
ALGORITHM="HS256" #HASHING ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES=30 #30 minutes ko lagi token valid huncha

def create_access_token(data:dict):     #token ma payload ni huncha ni ta so DICT LIYEKO PARAMETER, ANI data ma kei pani halna sakincha like user id, email,role etc
    to_encode=data.copy() #temp variable ma store gareko KINA BHANE REAL DATA MA CHANGE NA GAROS K
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) #current time ma 30 minutes add garera expire time banaune
    to_encode.update({"exp":expire}) #token ma expire time halne LIYEKO PAYLOAD DATA MA
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,ALGORITHM)     #VVVVVVVVVVVVIMP    first one is EVERYTHING THAT I WANT TO PUT IN PAYLOAD IN TOKEN, SECRET KEY, ALGORITHM
    return encoded_jwt #token return garne

#verifying the token sent from the frontend request header

def verify_access_token(token:str,credentials_exception):   #token ko type string huncha ni ta
    try:   #kunai pani line ma yesma errors aauna sakcha ni ta so try except hali haleko
        payload=jwt.decode(token,SECRET_KEY,[ALGORITHM])   #token lai decode garne
        id=payload.get("user_id")                        #user_id thio ni ta payload ma token ko create garda kheri
        if id is None:
            raise credentials_exception
        
        token_data=schemas.TokenData(id=id)   #token data lai validity check gareko
    except JWTError:  #yo chai token ko expiry time check garne ho ani yo chai token ko signature check garne ho i.e. token ko data ma kei pani change bhayo bhane yo chai error aaucha
        raise credentials_exception
    
    return token_data  #token data return garne
"""
def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(database.get_db)):
    credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="could not validate credentials",headers={"WWW-Authenticate":"Bearer"})  #yo chai token ko EXPIRY expiry time check garne ho ani yo chai token ko signature check garne ho i.e. token ko data ma kei pani change bhayo bhane yo chai error aaucha

    token=verify_access_token(token,credentials_exception)   #token ko validity check garne ho ani yo chai token ko signature check garne ho i.e. token ko data ma kei pani change bhayo bhane yo chai error aaucha

    user=db.query(models.User).filter(models.User.id==token.id).first()   #token ko id bata user ko data lincha so KAAM easy bhayo ni ta OTHERWISE purano tarika use garepani huncha jasma endpoint mai userid line garicha

    return user   #modularity badhauna lai k euta arko function lekheko josle token extract garera dincha and exception pani kina repeat garirakhnu bhanera pathaucha
"""
# YESARI PANI GARNA SAKINCHA HAI USER_ID PATHAYERA ANI ENDPOINT MA KAAM GARNE PANI SAKINCHA
def get_current_user(token:str=Depends(oauth2_scheme)):
    credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="could not validate credentials",headers={"WWW-Authenticate":"Bearer"})  #yo chai token ko EXPIRY expiry time check garne ho ani yo chai token ko signature check garne ho i.e. token ko data ma kei pani change bhayo bhane yo chai error aaucha
    return verify_access_token(token,credentials_exception)   #token ko validity check garne ho ani yo chai token ko signature check garne ho i.e. token ko data ma kei pani change bhayo bhane yo chai error aaucha
    