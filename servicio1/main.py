from fastapi import FastAPI
import logging
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
logging.basicConfig(level=logging.INFO)

class Libro(BaseModel):    
    titulo: str
    autor: str
    paginas: str
    editorial: Optional[str]


@app.get("/")
def read_root():
    logging.info("Peticion recibida desde el servicio 1")
    return {"message": "Saludos desde el servicio n°1!"}

@app.get("/health")
def health():
    return {"status": "El servicio 1 esta funcionando correctamente"}

@app.get("/libros/{id}")
def obtener_libro(id: int):
    return {"data": id}

@app.post("/libros")
def insertar_libro(libro: Libro):
    return {"message": f"Libro {libro.titulo} insertado correctamente"}

