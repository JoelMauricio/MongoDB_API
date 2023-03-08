from fastapi import FastAPI
from uvicorn import run
import queries as q
import json
import bson.json_util as json_util
import config as C

app = FastAPI()

@app.get("/")
def index():
    return {"aplicación":"grupo 1"}

@app.get("/consulta1")
def index():
    result = json_util.dumps(list(q.consulta1))
    return result

@app.get("/consulta2")
def index():
    result = json_util.dumps(list(q.consulta2))
    return result

@app.get("/consulta3")
def index():
    result = json_util.dumps(list(q.consulta3))
    return result

@app.get("/consulta4")
def index():
    result = json_util.dumps(list(q.consulta4))
    return result

@app.get("/consulta5")
def index():
    result = json_util.dumps(list(q.consulta5))
    return result

if __name__ == '__main__':
    run(app, port=C.PORT)