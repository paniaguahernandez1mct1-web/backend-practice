import json

# PARTE 1: Crear diccionario
usuario = {
    "nombre": "Emmanuel",
    "edad": 25,
    "habilidades": ["Python", "Linux"]
}

#convertir  a string JSON
json_str = json.dumps(usuario,indent=4)
print(json_str)

# PARTE 2: Guardar JSON
with open("usuario.json", "w") as f:
    json.dump(usuario, f, indent=4)

# PARTE 3: Leer JSON desde archivo
with open("usuario.json", "r") as f:
    usuario = json.load(f)

print(usuario["nombre"])

# # PARTE 4: Parsing desde string
# json_text = '{"nombre": "Ana", "edad": 30}'
# usuario = json.loads(json_text)
# print(usuario["edad"])

# PARTE 5: Modificar datos
usuario["habilidades"].append("Git")

#guardar otra vez
with open("usuario.json", "w") as f:
    json.dump(usuario, f, indent=4)

print ("JSON actualizado")

