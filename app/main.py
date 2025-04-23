from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine, SessionLocal,Base

models.Base.metadata.create_all(bind=engine)  #creating the tables in the database using the models defined in the models.py file

app=FastAPI()

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


#array banako DB ma kaam garnu aagadi bujhna lai k raicha bhanera
my_posts=[{"title":"title of post 1","content":"content of post 1","id":1},
          {"title":"title of post 2","content":"content of post 2","id":2},
          {"title":"title of post 3","content":"content of post 3","id":3}]
#learning the schema validation

#like for making a post you may want the title: str, content: str, boolean: post or save as draft or sth.
#class banaune jasma saab DATA Validation Constraints huncha

# class Post(BaseModel):  #extending the BaseModel class (inheritance)
#     title:str
#     content:str


class Post(BaseModel):  #extending the BaseModel class (inheritance)
    title:str
    content:str
    publised:bool=True  #default value is true
     #default value is true
    #rating:Optional[int]=None #nahale pani huncha but nahale chai None huncha, tara halepachi int type kai hunuparcha
#katai pani jasma error aauna sakcha like database connect nahuna sakcha tesma sadai try: bhitra lekhne hai


while True:      #yedi database connect first mai bhayena or pw haru galat thio bhane jaba samma thik hunna garirakhna paryo ni ta aagadi jana bhayena k program just error message falera !!! 
    try:
        conn=psycopg2.connect(host="localhost",database="first_fastapi",user="postgres",password="yourpassword",cursor_factory=RealDictCursor) #cursor_factory=RealDictCursor le data lai dictionary ma convert garne kaam garcha
        cursor=conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error: ",error)
        time.sleep(2)  #2 seconds wait garne ani feri try garne

#Remember class ma comma hunna JSON jasto ani retrieve garda ni : payload["title"] haina just payload.title
class UpdatePost(BaseModel):
    title:str
    content:str
    publised:bool=True  #default value is true
    #rating:Optional[int]=None
@app.get("/db_posts")
async def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts=cursor.fetchall()
    return {"data":posts}  #returning the data in JSON format automatically by fastapi to the frontend as the answer to some request in some button 

@app.post('/db_posts_post',status_code=status.HTTP_201_CREATED)
async def create_posts(payload:Post):
    cursor.execute("""INSERT INTO posts (title,content,publised) VALUES (%s,%s,%s) RETURNING *""",(payload.title,payload.content,payload.publised))
    new_post=cursor.fetchone()   
    conn.commit()  #commit the changes to the database TO SAVE IN THE DATABASE
    return {"data":new_post}


@app.get('/db_posts/{id}')
async def get_one_post(id:int): #yo int bhaneko tyo url ma k type garcha user le validate gareko
    cursor.execute("""SELECT * FROM posts WHERE id=%s""",(id,)) #comma halnu parcha kina bhane tuple ma convert huncha
    #cursor.execute("""SELECT * FROM posts WHERE id=%s""",(id)) #yo chai tuple ma convert hunna
    #cursor.execute("""SELECT * FROM posts WHERE id=%s""",(id,)) #yo chai tuple ma convert huncha
    post=cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post not found with {id}")
    return {"data":post}

@app.delete('/db_delete_posts/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete(id:int):
    cursor.execute("""delete from posts where id=%s returning *""",(id,))  #returning * bhaneko delete bhayepachi kunai pani data return garne ho Returning * CHAI ALL COLUMNS
    deleted_post=cursor.fetchone()
    conn.commit()   #whnever we make any changes to the database we need to commit the changes
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post not found with {id}")
    return Response(status_code=status.HTTP_204_NO_CONTENT) #204 is no content, kunai pani kura delete bhayo bhane yo status code huncha
#delete garda actual value return garaunu hunna just DELETED bhanne RESPONSE return garne

#GET BAHEK ARU SABAI MA CONN.COMMI HUNAI PARCHA NATRA DATABASE MA DEKHIDAINA

#POST, PUT, DELETE ma sabai ma commit huncha
#GET ma hunna kina bhane GET ma data matra aaucha, data change nahune ho so commit nahune


@app.get("/")  #decorator to tell fastapi that this is a get request
# this is the root endpoint
#if it was @app.get("/login") then I shoud go to this in the URL to use this endponint to use the functions
async def root():

    return {"message": "Hello World!!"} #automatically convert to json by fastapi and sends back to user 


@app.get("/posts")

async def get_login():#name of the function does not matter really but it should be relevant 
    return {"message": "Make Post Page"} #automatically convert to json by fastapi and sends back to user


@app.post("/createposts")
def create_posts(payload:dict=Body(...)):  #frontend bata data liyera ayo FULL BODY ani stored in dict format and saves in the payload variable, frontend bata kasto format ma ako cha?JSON right so yeta pani purai BODY ko data lai DICT ma rakheko
    print(payload)  
    return {"message":f"post is created"}

@app.post("/create")
def create_posts(payload:dict=Body(...)):  #frontend bata data liyera ayo FULL BODY ani stored in dict format and saves in the payload variable, frontend bata kasto format ma ako cha?JSON right so yeta pani purai BODY ko data lai DICT ma rakheko
    print(payload)  
    return {"message":f'tile is {payload["title"]} and content is {payload["content"]}'}
#print is only used for debugging purpose not as backend logic
#actually this data payload from the Body is saved in the DataBase kinaki pachi post herna maan lagyo bahne ni pawos


@app.post("/create_posts",status_code=status.HTTP_201_CREATED)  #201 is created, kunai pani kura create garesi 201 hunuparcha
def creating(new_post:Post):   #title hunai parcha ani str nai huna parcha natra OPTIONAL field halincha class mai
    print(new_post)
    print(new_post.rating)
    new_post_dict=new_post.dict()
    return {"data":f"{new_post.title} and {new_post.content} and:: {new_post.publised} and {new_post_dict}"}
    
@app.get("/get_posts/{id}")
async def get(id:int):
    return {"post_id":id}

def find_a_post(id):
    for post in my_posts:  #because each dictionary in the array of my_post is a POST
        if post["id"]==id:
            return post
    return None

@app.get("/posts/{id}")
async def get_post(id:int,response:Response): #default the fastapi path parameter is string so validation haleko int nai halnu parcha bhanera
    post=find_a_post(id)   #request ma ako id lai afno DB ko array ma bhako POSTS ko array sanga match garako
    if not post:
        #return {"error":"post not found"}
       # response.status_code=status.HTTP_404_NOT_FOUND 
       # return {"error":"post with {id} not found"} #404 is not found

       #we can just use a one liner HTTPException raise
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post not found with {id}")  #baas error message matra haina status code pani return garaunu parcha ni ta natra ERROR but 200 status jancha
    return {"post_detail":post}

#delete garna lai
#find the post with the specific id using enumerate 
#delete the post my my_posts.pop(id)

def find_index(id):
    for i,post in enumerate(my_posts):
        if post["id"]==id:
            return i
    return None

@app.delete("/posts/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index=find_index(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post not found with {id}")
    else:
        my_posts.pop(index)
        return None               #dont sent any detail or content in 204 delete
    
@app.put("/posts/update/{id}")
async def update_post(id:int,post:UpdatePost):   #yesma pani SCHEMA validation huncha SAME POST garda jastai ho so COPY PASTE ARKO class BANAYE ni huncha
    index=find_index(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post not found with {id}")
    
    post_dict=post.dict()  #dict ma convert gareko
    my_posts[index].update(post_dict)  #update the post with the new data
    return {"data":post_dict}

