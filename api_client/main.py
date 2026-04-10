import requests
import json
import yaml

#URL = "https://jsonplaceholder.typicode.com/posts"

def cargar_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

try:
    config = cargar_config()
    URL = config["api"]["url"]
    ARCHIVO = config["output"]
except Exception as e:
    print("Error cargando configuración:", e)
    exit()

def obtener_posts():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error al consultar API:", e)
        return[]
    
def procesar_posts(posts):
    total = len(posts)
    primeros = posts[:5]

    print(f"\nTotal de posts: {total}\n")

    for post in primeros:
        print(f'{post["id"]} - {post["title"]}')

    return {
        "total": total,
        "muestra": primeros
    }

# def guardar_datos(data):
#     with open("data.json", "w") as f:
#         json.dump(data, f, indent=4)

#     print("\nDatos guardados en data.json")

def guardar_datos(data):
    with open(ARCHIVO, "w") as f:
        json.dump(data, f, indent=4)

    print(f"\nDatos guardados en {ARCHIVO}")
    
def main():
    posts = obtener_posts()

    if not posts:
        print("No se obtuvieron datos")
        return
    
    resumen = procesar_posts(posts)
    guardar_datos(resumen)


if __name__ == "__main__":
    main() 