from passlib.context import CryptContext
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")


#NORMAL PASSWORD LAI HASHING GARERA DATABASE MA HALNE WALA FUNCTION BHAYO YO
def hash(password:str):
    return pwd_context.hash(password)

#USER LE HALEKO PASSWORD ANI, TYO EMAIL MA DATABSE MA BHAKO PASSWORD LAI CHECK GARNE WALA FUNCTION
def verify(plain_password:str,hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)  #yo chai password lai hash garera check garne wala function ho


