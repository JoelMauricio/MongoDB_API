from fastapi import FastAPI
from uvicorn import run
import queries as q
import logging
import bson.json_util as json_util
import config as C

#setting up the logging
logging.Logger(name="Logs")
logging.basicConfig(filename="log.txt",level=logging.DEBUG, format="%(asctime)s %(message)s")

#starting the API
app = FastAPI()

@app.get("/")
def index():
    logging.info("Se cargó el directorio principal")
    return {"aplicación":"grupo 1"}

@app.get("/consulta1")
def index():
    try:
        logging.info("se intenta retornar los datos de la consulta 1")
        result = json_util.dumps(q.consulta1())
    except:
        logging.error("La consulta 1 falló")
        result = "No se pudo recuperar los datos de la consulta"
    return result

@app.get("/consulta2")
def index():
    try:
        logging.info("se intenta retornar los datos de la consulta 2")
        result = json_util.dumps(q.consulta2())
    except:
        logging.error("La consulta 2 falló")
        result = "No se pudo recuperar los datos de la consulta"
    return result

@app.get("/consulta3")
def index():
    try:
        logging.info("se intenta retornar los datos de la consulta 3")
        result = json_util.dumps(q.consulta3())
    except:
        logging.error("La consulta 3 falló")
        result = "No se pudo recuperar los datos de la consulta"
    return result

@app.get("/consulta4")
def index():
    try:
        logging.info("se intenta retornar los datos de la consulta 4")
        result = json_util.dumps(q.consulta4())
    except:
        logging.error("La consulta 4 falló")
        result = "No se pudo recuperar los datos de la consulta"
    return result

@app.get("/consulta5")
def index():
    try:
        logging.info("se intenta retornar los datos de la consulta 5")
        result = json_util.dumps(q.consulta5())
    except:
        logging.error("La consulta 5 falló")
        result = "No se pudo recuperar los datos de la consulta"
    return result

if __name__ == '__main__':
    logging.info("Se inicializó el API")
    run(app, port=C.PORT)