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

@app.get("/status")
async def check_status():
    return {"status": "API está funcionando perfeitamente."}

@app.post("/login")
async def login(player: Player):
    return {"message": f"Usuário {player.nickname} logado com sucesso!"}

@app.get("/platforms")
async def list_platforms():
    return {"platforms": ["PC", "Xbox", "PlayStation", "Switch"]}

@app.patch("/player/activate/{nickname}")
async def activate_player(nickname: str):
    return {"nickname": nickname, "activated": True}

@app.get("/random/platform")
async def random_platform():
    platforms = ["PC", "Xbox", "PlayStation", "Switch"]
    return {"platform": random.choice(platforms)}