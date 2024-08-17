from fastapi import FastAPI
import logging
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
logging.basicConfig(level=logging.INFO)

class Review(BaseModel):    
    titulo: str
    autor: str
    resenia: str
    puntaje: int


@app.get("/")
def read_root():
    logging.info("Peticion recibida por el servicio 2")
    return {"message": "Saludos desde el servicio n°2!"}

@app.get("/health")
def health():
    return {"status": "El servicio 2 esta funcionando correctamente"}

@app.get("/review/{id}")
def obtener_review(id: int):
    return {"data": id}

@app.post("/review")
def insertar_review(review: Review):
    return {"message": f"Reseña sobre {review.titulo} insertada "}

