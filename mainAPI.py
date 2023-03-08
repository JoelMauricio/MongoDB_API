from fastapi import FastAPI
import json
import configuration as C
from uvicorn import run 

app = FastAPI()

with open("./data/restaurants.json", "r") as f:
    data = json.load(f)

@app.get("/")
def index():
    return data

if __name__ == "__main__":
    run(app, port=C.PORT)