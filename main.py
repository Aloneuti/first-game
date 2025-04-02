import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Player(BaseModel):
    nickname: str
    platform: str
    Active: bool

@app.get("/")
async def home():
    return {"message": "Aqui é o começo"}

@app.get("/number")
async def number():
    return {"Number": True, "Random_number": random.randint(0,154)}

@app.get("/game")
async def gamepage():
    return {"Aqui será a pagina do game"}

@app.post("/signup")
async def signuppage(nickname: Player):
    return nickname

@app.put("/signup/update/{id_player}")
async def update_player(id_player: int):
    return id_player > 0

@app.delete("up/delete/{id_player}")
async def delete_player(id_player: int):
    return id_player > 0
