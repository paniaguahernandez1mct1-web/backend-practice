from fastapi import FastAPI, status
from pydantic import BaseModel, Field
app = FastAPI()

## DÍA 15
# @app.get("/")

# def inicio():
#     # return {"mensaje": "Hola mundo con FastAPI"}
#     return {"message": "Hi World"}

# @app.get("/saludo")
# def saludo():
#     return {"mensaje": "Hola Gaby"}

# @app.get("/usuario/{nombre}")
# def usuario(nombre: str):
#     return {"usuario": nombre}

## DIA 16
# @app.get("/buscar")
# def buscar(nombre:str):
#     return{"resultado": f"Buscando a {nombre}"}

# @app.get("/usuario/{nombre}")
# def usuario(nombre: str):
#     return {"usuario": nombre}

# @app.post("/crear")
# def crear_usuario(data: dict):
#     return {
#         "mensaje": "Usuario creado",
#         "data": data
#     }

# @app.get("/info")
# def info():
#     return {
#         "app": "Mi API",
#         "version": "1.0",
#         "status": "ok"
#     }

##EJERCICIO
# tareas = []

# @app.get("/")
# def inicio():
#     return {"mensaje": "API de tareas"}

# @app.get("/tareas")
# def obtener_tareas():
#     return tareas

# @app.post("/tareas")
# def agregar_tareas(tarea: dict):
#     if "titulo" not in tarea:
#         return{"error": "Falta título"}
#     tarea["id"] = len(tareas) + 1
#     tareas.append(tarea)
#     return {"mensaje": "Tarea agregada", "tarea": tarea}

## DÍA 17




tareas = []

class Tarea(BaseModel):
    # título: str
    # completada: bool = False
    titulo: str = Field(min_length=3, max_length=50)

@app.get("/tareas")
def obtener_tareas():
    return tareas

@app.post("/tareas", status_code = status.HTTP_201_CREATED)
def agregar_tarea(tarea: Tarea):
    nueva = tarea.model_dump()
    nueva["id"] = len(tareas) + 1
    tareas.append(nueva)

    return {
        "mensaje": "Tarea Creada",
        "tarea": nueva
    }


# @app.post("/tareas")
# def agregar_tarea(tarea: Tarea):
#     return {
#         "mensaje": "Tarea creada",
#         "tarea": tarea
#     }