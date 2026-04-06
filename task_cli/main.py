import os
import yaml  # pip install pyyaml

ARCHIVO = "tareas.yaml"  # Cambiamos extensión

def cargar_tareas():
    """Carga tareas desde archivo YAML"""
    if not os.path.exists(ARCHIVO):
        return []
    
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        try:
            tareas = yaml.safe_load(f)  # safe_load por seguridad
            return tareas if tareas is not None else []
        except yaml.YAMLError as e:
            print(f"Error al leer YAML: {e}")
            return []

def guardar_tareas(tareas):
    """Guarda tareas en archivo YAML"""
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        # default_flow_style=False para formato legible
        # allow_unicode=True para caracteres especiales
        yaml.dump(tareas, f, 
                 default_flow_style=False,
                 allow_unicode=True,
                 indent=2,
                 sort_keys=False)

def agregar_tarea():
    tareas = cargar_tareas()
    texto = input("Nueva tarea: ")

    # Calcular nuevo ID
    nuevo_id = max([t["id"] for t in tareas], default=0) + 1

    nueva = {
        "id": nuevo_id,
        "tarea": texto,
        "completada": False,
        "fecha_creacion": None,  # Podríamos añadir fecha
        "prioridad": "media"      # Ejemplo de campo nuevo
    }
    tareas.append(nueva)
    guardar_tareas(tareas)
    print(f"Tarea agregada ✅ (ID: {nuevo_id})")

def listar_tareas():
    tareas = cargar_tareas()

    if not tareas:
        print("📭 No hay tareas")
        return
    
    print("\n📋 LISTA DE TAREAS:")
    print("-" * 50)
    for t in tareas:
        estado = "✅" if t["completada"] else "❌"
        prioridad = t.get("prioridad", "media")
        
        # Mostrar con emojis según prioridad
        prioridad_icono = {
            "alta": "🔴",
            "media": "🟡",
            "baja": "🟢"
        }.get(prioridad, "⚪")
        
        print(f"{t['id']}. {estado} {t['tarea']} {prioridad_icono}")
    print("-" * 50)

def completar_tarea():
    tareas = cargar_tareas()
    
    if not tareas:
        print("No hay tareas para completar")
        return
    
    listar_tareas()
    
    try:
        id_tarea = int(input("\nID de tarea a completar: "))
        tarea_encontrada = False
        
        for t in tareas:
            if t["id"] == id_tarea:
                if not t["completada"]:
                    t["completada"] = True
                    print(f"✅ Tarea '{t['tarea']}' completada 🎉")
                else:
                    print(f"⚠️ La tarea ya estaba completada")
                tarea_encontrada = True
                break
        
        if not tarea_encontrada:
            print(f"❌ No existe tarea con ID {id_tarea}")
        else:
            guardar_tareas(tareas)
            
    except ValueError:
        print("❌ Ingresa un número válido")

def eliminar_tarea():
    """Función extra usando YAML"""
    tareas = cargar_tareas()
    
    if not tareas:
        print("No hay tareas para eliminar")
        return
    
    listar_tareas()
    
    try:
        id_tarea = int(input("\nID de tarea a eliminar: "))
        tarea_encontrada = False
        
        for i, t in enumerate(tareas):
            if t["id"] == id_tarea:
                confirmar = input(f"¿Eliminar '{t['tarea']}'? (s/n): ")
                if confirmar.lower() == 's':
                    tareas.pop(i)
                    print(f"🗑️ Tarea eliminada")
                    guardar_tareas(tareas)
                tarea_encontrada = True
                break
        
        if not tarea_encontrada:
            print(f"❌ No existe tarea con ID {id_tarea}")
            
    except ValueError:
        print("❌ Ingresa un número válido")

def menu():
    while True:
        print("\n" + "="*50)
        print("   📝 TO-DO APP con YAML")
        print("="*50)
        print("1. ➕ Agregar tarea")
        print("2. 📋 Listar tareas")
        print("3. ✅ Completar tarea")
        print("4. 🗑️ Eliminar tarea")
        print("5. 💾 Ver archivo YAML generado")
        print("6. 🚪 Salir")
        print("="*50)

        opcion = input("Selecciona opción (1-6): ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            # Mostrar contenido del archivo YAML
            if os.path.exists(ARCHIVO):
                print("\n📄 Contenido de tareas.yaml:")
                print("-" * 50)
                with open(ARCHIVO, "r", encoding="utf-8") as f:
                    print(f.read())
                print("-" * 50)
            else:
                print("Aún no hay archivo YAML")
        elif opcion == "6":
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Elige 1-6")

if __name__ == "__main__":
    print("🚀 Iniciando aplicación con almacenamiento YAML...")
    print(f"📁 Los datos se guardarán en: {ARCHIVO}")
    menu()