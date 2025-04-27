from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime
#pydantic is a data validation and settings management library for python

# class Post(BaseModel):  #extending the BaseModel class (inheritance)
#     title:str
#     #content:str
#     publised:bool=True  #default value is true
#      #default value is true
#     #rating:Optional[int]=None #nahale pani huncha but nahale chai None huncha, tara halepachi int type kai hunuparcha
# #katai pani jasma error aauna sakcha like database connect nahuna sakcha tesma sadai try: bhitra lekhne hai




# #these are normal python classes so we can use them as normal python classes like INHERITANCE AND ALL

# #SO CREATE POST,UPDATE POST ETC MA KK VALIDATION CHAINCHA YEI MAIN BASE CLASS BATA INHERIT GARNA SAKINCHA

# class CreatePost(BaseModel):
#     title:str
#     publised:bool=True

# class UpdatePost(BaseModel):
#     #title:str          YEDI YESTO APPLICATION CHA JASMA USER LE ARU KEI UPDATE GARNA SAKDAINA BAAS published lai MATRA UPDATE GARNA SAKCHA 
#     publised:bool=True

#HAREK REQUEST TYPE LAI EUTA CLASS BANAUNA SAKINCHA ANI BHITRA CHAI KK PERMISSION DINE TYO MATRA LEKHNE CLASS BHITRA

#ARKO TARIKA PANI CHA 
#TESMA CHAI EUTA BASE CLASS BANAUCHAU JASMA SABAII CLASS HARU LAI INHERIT GARNA SAKINCHA ANI TYO BASE CLASS KAI HELP LE ARU MA VALIDATION GARAUNE K

class PostBase(BaseModel):
    title:str
    publised:bool=True

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass
#class PostUpdate(PostBase):
#    title:str  #    publised:bool=True
#    #content:str
#    #rating:Optional[int]=None #nahale pani huncha but nahale chai None huncha, tara halepachi int type kai hunuparcha
#    #rating:Optional[int]=None #nahale pani huncha but nahale chai None huncha, tara halepachi int type kai hunuparcha
#    #yo chai update garna ko lagi ho
#    #yedi update garna ko lagi chai title matra update garna parcha bhane ta yestai garne ho



class PostResponse(BaseModel):
    title:str
    publised:bool
    created_at:datetime
    id:int   #whatever you want to show to the user as response put here
    class Config:
        orm_mode=True #kinaki dictionary ma huncha ani database ma chai object ma huncha ORM ko so pydantic lai yo chai dictinay ho object haina bhanna lai k decorator ma halda
#yo class Config use nagare Error aaucha
    #yesma pani inherit garna sakinthio 
    #class PostResponse(PostBase):
    #   id:int
    #   created_at:datetime   ARU TA MATHI BATAI LII HALCHA TA 


class UserCreate(BaseModel):
    email:EmailStr          #valid email type ko string ho and not just a random string 
    password:str
    class Config:
        orm_mode=True

class UserResponse(BaseModel):
    id:int
    email:EmailStr          # malai yei response chiyo bhanera ho k
    created_at:datetime
    #password:str   #password hunu hudaina ni ta response 

    class Config:                     #yo kina gareko bhanda ORM ma ta object aaucha ni response but teslai pydantic model le bujhne dictionary ma lagna paryo so class Config
        orm_mode=True                 




