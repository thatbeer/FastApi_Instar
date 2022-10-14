from fastapi import FastAPI
from db import models
from db.database import engine
from router import user , post
from fastapi.staticfiles import StaticFiles
from auth import authentication

app = FastAPI()

@app.get("")
def root():
    return "Hello function"

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(post.router)

models.Base.metadata.create_all(engine)

app.mount('/images',StaticFiles(directory='images'), name='images')