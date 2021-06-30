from characters.utils import get_characters
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/characters")
async def get_chars():
    return dict(characters=get_characters())