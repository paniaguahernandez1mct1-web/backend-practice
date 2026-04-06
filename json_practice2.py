import json

# PARTE 1: Crear diccionario
usuarios = [
    {"nombre": "Emmanuel", "edad": 26},
    {"nombre": "Jaz", "edad": 25}
]

#convertir  a string JSON
json_str = json.dumps(usuarios,indent=4)
print(json_str)

# PARTE 2: Guardar JSON
with open("usuarios.json", "w") as f:
    json.dump(usuarios, f, indent=4)

# PARTE 3: Leer JSON desde archivo
with open("usuarios.json", "r") as f:
    usuarios = json.load(f)

print(usuarios[0]["nombre"])

# # PARTE 4: Parsing desde string
# json_text = '{"nombre": "Ana", "edad": 30}'
# usuario = json.loads(json_text)
# print(usuario["edad"])

# PARTE 5
usuarios[0]["habilidades"] = ["Git"]

#guardar otra vez
with open("usuarios.json", "w") as f:
    json.dump(usuarios, f, indent=4)

print ("JSON actualizado")

