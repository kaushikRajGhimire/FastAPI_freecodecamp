#ROUTER OBJECT le sajilo garera sabai endpoint haru lai ekai thau ma rakhera use garna milcha ani chaiyo bhane import garera use garna milcha

from fastapi import FastAPI, Response, status, HTTPException,Depends
from pydantic import BaseModel
from .. import models,schemas,utils
from typing import Optional,List    
from sqlalchemy.orm import Session
from ..database import get_db
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from passlib.context import CryptContext
from fastapi import APIRouter


router=APIRouter(tags=["SQLAlchemy Test"])  #prefix le chai sabai endpoint ma /users halne ho ani tags le chai documentation ma k k huncha bhanera bujhna sajilo huncha

@router.get("/sqlalchemy_test")
async def test_sqlalchemy(db:Session=Depends(get_db),response_model=List[schemas.PostResponse]):   #sqlalchemy garera TEST GAREKO  SQLALCHEMY KO USE BHAKO CHA BHANE ALWAYS ALWAYS WRITE THAT ARGUMENT FUNCTION MA HAI 
    posts=db.query(models.Post).all() #models.py bhitra bhako Post class ko use le tyo table bhitra CRUD garne ho  
    return posts #returning the data in JSON format automatically by fastapi to the frontend as the answer to some request in some button


@router.get("/sqlalchemy_test/{id}",response_model=schemas.PostResponse)  #response_model le chai k return garne ho bhanera bujhna sakinchha
async def test(id:int,db:Session=Depends(get_db)):     #yesma ta baas euta post chiyeko cha so single lai List chaidaina natra 2 or more or all post linu pareko bhaye we would need List[] in the respomse_model
    post=db.query(models.Post).filter(models.Post.id==id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post not found with {id}")
    return post  #returning the data in JSON format automatically by fastapi to the frontend as the answer to some request in some button

@router.post("/sqlalchemy_test_post",status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponse)
async def test(payload:schemas.PostBase,db:Session=Depends(get_db)):
    new_post=models.Post(**payload.dict())  #creating a new post object using the Post class defined in the models.py file
    db.add(new_post)  #adding the new post object to the session
    db.commit()#  #committing the changes to the database
    db.refresh(new_post)   #refreshing the new post object to get the id and other details from the database
    return new_post

@router.delete("/sqlalchemy_test_delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def test(id:int,db:Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id).first()
    if post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post not found with {id}")
    db.delete(post)
    db.commit()   #yo ta ekdam important so that we can reflect that on the database
    #db.refresh(post)  #yo chai delete garda hunna
    post.delete(synchronize_session=False)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/sqlalchemy_test_update/{id}",response_model=schemas.PostResponse)
async def test(id: int, payload: schemas.PostUpdate, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()   #post is an object got from sqlalchemy query response
    #post_query is a query object so we can use it to update the post
    #post is an object got from sqlalchemy query response
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post not found with id {id}"
        )

    post_query.update(payload.dict(), synchronize_session=False)   #yo wala doubt padhne hai synchronization=False mostly used wala plus the payload wala kina use bhayo post kina bhayena
    db.commit()         #yo k gareko thaha bhayo kinaki data ta json dictionary ma cha ni ta payload ma UpdatePost bata validate gareko but database ma SQLAlchemy use garera update garda ta dictionary ma hunu parcha ni ta thats why post_query.update(payload.dict()ma convert garera haleko)
#natra """post.title=payload.title,
#    post.publised=payload.publised""" garera one by one update garna ni milthio but purai lai update garda or dherai fields lai update garda yestai garne ho 
    return post_query.first()


"""🎯 Here's the Critical Line You Asked About:

post_query.update(payload.dict(), synchronize_session=False)
⚙️ Why payload.dict()?
payload is a Pydantic model, like:


class UpdatePost(BaseModel):
    title: str
    content: str
payload.dict() gives you a Python dictionary like:


{'title': 'New Title', 'content': 'Updated content'}
This is perfect for SQLAlchemy’s update() method, which takes a dictionary of values to update.

✅ You can't pass post here — that's an actual ORM object, not data."""

