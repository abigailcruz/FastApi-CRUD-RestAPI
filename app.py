# Importar las librerías necesarias
from fastapi import FastAPI, HTTPException
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
    return posts[-1]  # Devolver la última publicación añadida

# Endpoint GET que devuelve una publicación específica según su id
@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:  # Recorrer la lista de publicaciones
        if post['id'] == post_id:  # Si se encuentra una publicación con el id especificado
          return post  # Devolver la publicación
    raise HTTPException(status_code=400, detail="POST not found")  # Si no se encuentra la publicación, lanzar una excepción HTTP

# Endpoint DELETE que elimina una publicación específica según su id
@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
    for index, post in enumerate(posts):  # Recorrer la lista de publicaciones
        if post['id'] == post_id:  # Si se encuentra una publicación con el id especificado
            posts.pop(index)  # Eliminar la publicación de la lista
            return {"message": "Post has been deleted succesfully"}  # Devolver un mensaje de confirmación
    raise HTTPException(status_code=400, detail="Post Not Found")  # Si no se encuentra la publicación, lanzar una excepción HTTP

# Endpoint PUT que actualiza una publicación específica según su id
@app.put("/posts/{post_id}")
def update_post(post_id: str, updatedPost: Post):
    for index, post in enumerate(posts):  # Recorrer la lista de publicaciones
        if post['id'] == post_id:  # Si se encuentra una publicación con el id especificado
            # Actualizar los campos de la publicación con los valores proporcionados en la solicitud
            posts[index]["title"] =updatedPost.title
            posts[index]["content"] = updatedPost.content
            posts[index]["author"] = updatedPost.author
            return {"message": "Post has been updated succesfully"}  # Devolver un mensaje de confirmación
    raise HTTPException(status_code=400, detail="Post Not Found")  # Si no se encuentra la publicación, lanzar una excepción HTTP