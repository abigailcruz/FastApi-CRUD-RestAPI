# Importar las librerías necesarias
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid

# Crear una instancia de FastAPI
app = FastAPI()

# Crear una lista vacía para almacenar las publicaciones
posts = []

# Definir la estructura de un objeto Post utilizando Pydantic
class Post(BaseModel):
    id: Optional[str]  # El id de la publicación es opcional
    title: str  # El título de la publicación es obligatorio
    author: str  # El autor de la publicación es obligatorio
    content: Text  # El contenido de la publicación es obligatorio
    created_at: datetime = datetime.now()  # La fecha de creación se establece automáticamente a la hora actual
    published_at: Optional[datetime]  # La fecha de publicación es opcional
    published: bool= False  # Por defecto, una publicación no está publicada


# Endpoint GET que devuelve un mensaje de bienvenida en la ruta raíz
@app.get('/')
def read_root():
    return {'Welcome': 'Welcome to my Rest API'}

# Endpoint GET que devuelve todas las publicaciones almacenadas
@app.get('/posts')
def get_posts():
    return posts

# Endpoint POST que crea una nueva publicación y la añade a la lista
@app.post('/posts')
def save_post(post: Post):
    post.id = str(uuid())  # Asignar un id único a la publicación
    posts.append(post.dict())  # Convertir la publicación a un diccionario y añadirla a la lista de publicaciones
    return "recibido"
