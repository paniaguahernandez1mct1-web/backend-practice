# Código Base
from fastapi import FastAPI, status, HTTPException
from models import Tarea
import crud

app = FastAPI()

#GET (listar tareas)
@app.get("/tareas")
def obtener_tareas():
    return crud.obtener_tareas()

#POST (crear tarea)
@app.post("/tareas", status_code=status.HTTP_201_CREATED)
def agregar_tarea(tarea:Tarea):
    nueva = crud.agregar_tarea(tarea.dict())
    return nueva

#PUT (actualizar tarea)
@app.put("/tareas/{id}")
def actualizar_tarea(id: int, tarea: Tarea):
    actualizada = crud.actualizar_tarea(id, tarea.dict())

    if not actualizada:    
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    return actualizada

#DELETE (borrar tarea)
@app.delete("/tareas/{id}")
def eliminar_tarea(id:int):
    eliminado = crud.eliminar_tarea(id)

    if not eliminado:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    return {"mensaje": "Eliminada"}
