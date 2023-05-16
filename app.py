# Importar las librerías necesarias
from fastapi import FastAPI

# Crear una instancia de FastAPI
app = FastAPI()

# Crear una lista vacía para almacenar las publicaciones
posts = []

# Endpoint GET que devuelve un mensaje de bienvenida en la ruta raíz
@app.get('/')
def read_root():
    return {'Welcome': 'Welcome to my Rest API'}

# Endpoint GET que devuelve todas las publicaciones almacenadas
@app.get('/posts')
def get_posts():
    return posts
