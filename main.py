from characters.utils import get_characters
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"isekai": "Kono Subarashi ni sekai shukufuku wo"}

@app.get("/characters", summary="Get All Characters")
async def get_chars():
    all_chars = get_characters()
    if len(all_chars) < 1:
        return dict(characters=[])
    else:
        return dict(characters=[x['character'] for x in all_chars])