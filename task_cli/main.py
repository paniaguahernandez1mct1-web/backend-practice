#CÓDIGO BASE
import json
import os

ARCHIVO = "tareas.json"

def cargar_tareas():
    if not os.path.exists(ARCHIVO):
        return[]
    with open(ARCHIVO, "r") as f:
        return json.load(f)
    
def guardar_tareas(tareas):
    with open(ARCHIVO, "w") as f:
        json.dump(tareas, f, indent=4)

#AGREGAR TAREA
def agregar_tarea():
    tareas = cargar_tareas()
    texto = input("Nueva tarea: ")

    nueva = {
        "id": len(tareas) + 1,
        "tarea": texto,
        "completada": False
    }
    tareas.append(nueva)
    guardar_tareas(tareas)

    print("Tarea agregada ✅")

#LISTAR TAREAS
def listar_tareas():
    tareas = cargar_tareas()

    if not tareas:
        print("No hay tareas")
        return
    
    for t in tareas:
        estado = "✔" if t["completada"] else "✘"
        print(f'{t["id"]}. {t["tarea"]} [{estado}]')

#MARCAR COMO COMPLETADA
def completar_tarea():
    tareas = cargar_tareas()

    listar_tareas()
    #id_tarea = int(input("ID de tarea a completar: "))

    try:
        id_tarea = int(input("ID: "))
        for t in tareas:
            if t["id"] == id_tarea:
                t["completada"] = True

        guardar_tareas(tareas)
        print("Tarea completada 🎉")

    except:
        print("Ingresa número válido")

    

#MENÚ PRINCIPAL (CLI)
def menu():
    while True:
        print("\n--- TO-DO CLI ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Salir")

        opcion = input("Selecciona opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            break
        else:
            print("Opción inválida")        
            
if __name__ == "__main__":
    menu()