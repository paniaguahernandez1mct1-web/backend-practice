# # LISTAS
# numeros = [1,2,3,4]

# numeros.append(5)
# numeros.remove(2)

# for n in numeros:
#     print(n)

# # DICIONARIOS
# usuario = {
#     "nombre": "Emmanuel",
#     "edad": 25,
#     "activo": True
# }

# print(usuario["nombre"])

# usuario["ciudad"] = "Guadalajara"

# print(usuario["ciudad"])

# # SETS
# numeros = {1,2,2,3,4}
# print(numeros) #elimina duplicados a través de las llaves

# # STRINGS
# texto = "Backend Developere"

# print(texto.lower())
# print(texto.upper())
# print(texto.split())
# print(len(texto))

# # LEER ARCHIVO EN PYTHON
# with open("datos.txt", "r") as archivo:
#     for linea in archivo:
#         print(linea.strip())

# # PROCESAR DATOS DE ARCHIVO
# with open("datos.txt", "r") as archivo:
#     for linea in archivo:
#         nombre, edad, ciudad = linea.strip().split(",")
#         print(f"{nombre} tiene {edad} años")

# # LEER CSV DE FORMA BÁSICA
# with open("datos.csv", "r") as archivo:
#     for linea in archivo:
#         print(linea.strip().split(","))

# # LEER CSV CON DICCIONARIOS 
# import csv

# with open("datos.csv", newline="") as archivo:
#     reader = csv.DictReader(archivo)

#     for fila in reader:
#         print(fila["nombre"], fila["edad"])

# EJERCICIO FINAL
import csv

NumPersonas = 0
SumaEdades = 0
nombres = set()

conteo_consolas = {}
conteo_genero = {}
conteo_pais = {}

with open("datos_usuarios.csv", newline="") as archivo:
    reader = csv.DictReader(archivo)

    for fila in reader:
        NumPersonas += 1
        SumaEdades += int(fila["Edad"])
        nombres.add(fila["Nombre"])

        # Contar consolas
        consola = fila["Consola"]
        conteo_consolas[consola] = conteo_consolas.get(consola, 0) + 1

        # Contar genero
        genero = fila["Genero"]
        conteo_genero[genero] = conteo_genero.get(genero, 0) + 1

        # Contar pais
        pais = fila["Pais"]
        conteo_pais[pais] = conteo_pais.get(pais, 0) + 1

# Obtener el más frecuente
consola_mas_usada = max(conteo_consolas, key=conteo_consolas.get)
genero_mayor = max(conteo_genero, key=conteo_genero.get)
pais_mayor = max(conteo_pais, key=conteo_pais.get)

print(f"Total de personas: {NumPersonas}")
print(f"Edad promedio: {SumaEdades/NumPersonas}")
print(f"Consola más usada: {consola_mas_usada}")
print(conteo_consolas)
print(f"Género que más usa consolas: {genero_mayor}")
print(f"País que más predomina: {pais_mayor}")
print("Nombres: ", nombres)