from fastapi import FastAPI
from uvicorn import run
import queries as q
import json
import config as C

app = FastAPI()

with open("./data/restaurants.json", "r") as f:
    data = json.load(f)

@app.get("/")
def index():
    return q.db['restaurants'].estimated_document_count()

@app.get("/consulta1")
def index():
    result = json.dumps(list(q.consulta1))
    return result

if __name__ == '__main__':
    run(app, port=C.PORT)