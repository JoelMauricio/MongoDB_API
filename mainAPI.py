from fastapi import FastAPI
import json

app = FastAPI()

with open("./data/restaurants-reviews.json", "r") as f:
    data = json.load(f)

@app.get("/")
def index():
    return data
