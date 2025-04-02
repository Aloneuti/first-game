from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return "minha api está no ar"