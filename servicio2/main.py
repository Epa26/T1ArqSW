from fastapi import FastAPI
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    logging.info("Peticion recibida por el servicio 2")
    return {"message": "Saludos desde el servicio n°2!"}

@app.get("/health")
def health():
    return {"status": "El servicio 2 esta funcionando correctamente"}
