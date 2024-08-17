from fastapi import FastAPI
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    logging.info("Peticion recibida desde el servicio 1")
    return {"message": "Saludos desde el servicio n°1!"}

@app.get("/health")
def health():
    return {"status": "El servicio 1 esta funcionando correctamente"}
