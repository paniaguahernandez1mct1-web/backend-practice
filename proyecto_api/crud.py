from utils import leer_datos, guardar_datos

def obtener_tareas():
    return leer_datos()

def agregar_tarea(tarea):
    tareas = leer_datos()

    ids = [t["id"] for t in tareas]
    nuevo_id = max(ids, default=0) + 1

    tarea["id"] = nuevo_id
    tareas.append(tarea)

    guardar_datos(tareas)
    return tarea

def actualizar_tarea(id, nueva_tarea):
    tareas = leer_datos()

    for t in tareas:
        if t["id"] == id:
            t["titulo"] = nueva_tarea["titulo"]
            t["completada"] = nueva_tarea["completada"]
            guardar_datos(tareas)
            return t
        
    return None

def eliminar_tarea(id):
    tareas = leer_datos()

    for t in tareas:
        if t["id"] == id:
            tareas.remove(t)
            guardar_datos(tareas)
            return True
        
    return False

