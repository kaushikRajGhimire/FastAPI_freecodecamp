from pydantic import BaseModel
from typing import Optional
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
#class PostUpdate(PostBase):