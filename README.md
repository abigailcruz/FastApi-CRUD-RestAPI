# fastapi-crud-restapi
Instalación de anaconda 

* Creacion de entorno virtual 
	* **conda create --name fastapi_restapi_crud python=3**
 * Activación de entorno virtual 
	 * **conda activate fastapi-crud-restapi**
* Desactivación de entorno virtual 
	 * **conda deactivate fastapi-crud-restapi**
	 *  conda deactivate fastapi-crud-restapi
* Instalar paquete fastapi 
	* **pip install fastapi**
* Instalar paquete uvicorn es el paquete que ayudara a ejecutar el proyecto de python
	* ** pip install uvicorn**
* Listar todos los paquetes  instalados 
	* **pip freeze > requeriments.txt**

Para no reiniciar el servidor cada que haya un cambio ejecutamos 
* **uvicorn app:app --reload**


**Importaciones Realizadas en el proyecto**
******
1.  `from fastapi import FastAPI, HTTPException`: `FastAPI` es un framework web de alto rendimiento utilizado para crear API RESTful en Python. Proporciona herramientas y utilidades para crear rápidamente servicios web. `HTTPException` es una excepción específica de FastAPI que se utiliza para devolver respuestas HTTP con códigos de estado personalizados.
    
2.  `from pydantic import BaseModel`: `BaseModel` es una clase proporcionada por la biblioteca Pydantic que se utiliza para definir modelos de datos. Los modelos de datos se utilizan para validar y serializar los datos de entrada y salida en una API. Pydantic también proporciona otras funcionalidades como validación de tipos y serialización/deserialización de datos.
    
3.  `from typing import Text, Optional`: `Text` y `Optional` son tipos de datos que se importan del módulo `typing`. `Text` se utiliza para representar cadenas de texto, mientras que `Optional` se utiliza para indicar que un argumento puede ser de un tipo específico o `None`.
    
4.  `from datetime import datetime`: `datetime` es una clase que se importa del módulo `datetime`. Se utiliza para trabajar con fechas y horas en Python. Proporciona métodos para crear, manipular y formatear fechas y horas.
    
5.  `from uuid import uuid4 as uuid`: `uuid4` es una función que se importa del módulo `uuid`. Se utiliza para generar identificadores únicos universales (UUID) versión 4. El alias `uuid` se utiliza para referirse a la función `uuid4` en el código. Los UUID son utilizados comúnmente para asignar identificadores únicos a objetos en aplicaciones distribuidas.
