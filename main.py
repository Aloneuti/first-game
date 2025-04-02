from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Aqui é o começo"}

@app.get("/number")
def number():
    return {"Number": True, "Random_number": random.randint(0,154)}

@app.get("/game")
def gamepage():
    return {"Aqui será a pagina do game"}
