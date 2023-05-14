from typing import Union
from fastapi import FastAPI,Response,status
from fastapi.exceptions import HTTPException
from fastapi.params import Body
from random import randrange
import models
app = FastAPI()

my_posts = [
    {"id":1, "title":"title 1", "content":"content1"},
    {"id":2, "title":"title 2", "content":"content2"},
    {"id":3, "title":"title 3", "content":"content3"},
]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
        
def find_index_post(id):
    for i, p in  enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get("/")
def read_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: models.PostModel):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000)
    my_posts.append(post_dict)
    return {"dataa": my_posts }

@app.post("/posts/{id}")
def get_posts(id:int, response: Response):
    post = find_post(id)
    if not post :
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f"id {id} doesn't exist")
    return {"post_detail": post }

@app.delete("/posts/{id}")
def delete_posts(id: int):
    index = find_index_post(id)
    my_posts.pop(index)
    if not index :
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f"id {id} doesn't exist")
    return {"message": "delete successfully" }
