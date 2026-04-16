# Código Base
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

tareas = []

#Modelo Pydantic
class Tarea(BaseModel):
    titulo: str
    completada: bool = False

#GET (listar tareas)
@app.get("/tarea")
def obtener_tareas():
    return tareas
# def obtener_tareas(id: int):
#     for t in tareas:
#         if t["id"] == id:
#             return t
#     raise HTTPException(status_code=404, detail= "No encontrada")

#POST (crear tarea)
@app.post("/tareas", status_code=status.HTTP_201_CREATED)
def agregar_tarea(tarea:Tarea):
    nueva = tarea.dict()
    #nueva["id"] = len(tareas) + 1
    nueva["id"] = max([t["id"] for t in tareas], default=0) + 1
    tareas.append(nueva)
    return nueva

#PUT (actualizar tarea)
@app.put("/tareas/{id}")
def actualizar_tarea(id: int, tarea: Tarea):
    for t in tareas:
        if t["id"] == id:
            t["titulo"] = tarea.titulo
            t["completada"] = tarea.completada
            return t
        
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

#DELETE (borrar tarea)
@app.delete("/tareas/{id}")
def eliminar_tarea(id:int):
    for t in tareas:
        if t["id"] == id:
            tareas.remove(t)
            return {"mensaje": "Tarea eliminada"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

