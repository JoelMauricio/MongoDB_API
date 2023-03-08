from fastapi import FastAPI
from uvicorn import run
import main
import json

app = FastAPI()

with open("./data/restaurants.json", "r") as f:
    data = json.load(f)

@app.get("/all")
def index():
    return data

@app.get("/borough-cuisine")
def index():
    return main.tipos_cocina_sector