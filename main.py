from fastapi import FastAPI
import random

app = FastAPI()

# 127.0.0.1:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test1")
async def funcaoteste():
    return {"test1": True, "random_number": random.randint(0 , 1000)}

@app.get("/test2")
async def test():
    return {"test2": "number"}
