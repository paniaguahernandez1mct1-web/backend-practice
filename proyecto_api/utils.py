import json
import yaml

def cargar_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)
    
config = cargar_config()
DATA_FILE = config["data_file"]

def leer_datos():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    #except FileNotFoundError:
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
