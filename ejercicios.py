# # VARIABLES
# nombre = "Emmanuel"
# edad = 26
# altura = 1.75

# # CONDICIONALES
# if edad >= 18:
# 	print ("Eres mayor de edad")
# else:
# 	print ("Eres menor de edad")

# #CICLOS
# for i in range(5):
# 	print(i)

# contador = 0

# while contador < 3:
# 	print (contador)
# 	contador += 1

# # FUNCIONES
# def saludar(nombre):
# 	return f"Hola Mr. {nombre}"

# print(saludar("Emmanuel"))

# # EJERCICIO 1 Pide un número e indica si es par o impar
# num = int (input ("Introduce un número: "))

# if num % 2 == 0:
# 	print ("Es un número par")
# else:
# 	print ("Es un número impar")

# # EJERCICIO 2 Dados 3 números, imprime el mayor
# num1 = int (input("Ingresa el primer número: "))
# num2 = int (input("Ingresa el segundo número: "))
# num3 = int (input("Ingresa el tercer número: "))

# if (num1 > num2) and (num1 > num3):
# 	print (f"El número {num1} es el mayor")
# elif (num2 > num1) and (num2 > num3):
# 	print (f"El número {num2} es el mayor")
# else:
# 	print (f"El número {num3} es el mayor")

# # EJERCICIO 3 Suma todos los elementos usando un ciclo
# numeros = [3, 5, 7, 9]
# suma = 0

# for i in range(len(numeros)):
#     suma = suma + numeros[i]

# print (f"El resultado de la suma de numeros es: {suma}")

# # EJERCICIO 4 Cuentas cuántas vocales hay
# def count_vowels(vocals):
#     vowels = set('aeiou')
#     return sum(1 for char in vocals if char in vowels)

# texto = "Backend developer"
# print (f"La cantida de vocales encontradas fue: {count_vowels(texto)}")

# # EJERCICIO 5 Imprime la tabla del 5 del 1 al 10

# for i in range(1,11):
#     resultado = 5 * i
#     print (f"5 x {i}: {resultado}")

# # EJERCICIO 6 FUnción que calcule el área de un rectángulo
# def area (BASE, ALTURA):
#     calculo = BASE * ALTURA
#     return calculo

# print ("Ingrese los datos requeridos para calcular el área de tu rectángulo por favor.")
# base = int (input ("Ingrese el tamaño de la base: "))
# altura = int (input ("Ingrese el tamaño de la altura: "))

# print(f"El área de su rectángulo es: {area(base, altura)}")

# # EJERCICIO 7 Crear lista solo con pares
# def filtrar_pares(num):
#     return num % 2 == 0

# numeros = [1,2,3,4,5,6,7,8,9]
# numeros_pares = list(filter(filtrar_pares, numeros))

# print(numeros_pares)

# # EJERCICIO 8 Contador regresivo del 10 al 0 con while

# contador = 10

# while (contador >= 0):
#     print(contador)
#     contador -= 1

# # EJERCICIO 9 Palabra Invertida de una cadena sin usar [::-1]
# palabra = str(input("Ingresa la palabra que desees invertir: "))
# palabra_invertida = ""
# for letra in palabra:
#     palabra_invertida = letra + palabra_invertida

# print ("Tu palabra ingresada fue:",palabra_invertida)

# # EJERCICIO 10 Función con condición que diga si un número es positivo, negativo o cero
# def revision_numero(num):
#     if num > 0:
#         status = "positivo"
#     elif num < 0:
#         status = "negativo"
#     else:
#         status = "cero"
#     return status

# numero = int (input ("Ingrese el número: "))
# print("El número ingresado es ", revision_numero(numero))

# EJERCICIO EXTRA Convierte 2 ejercicios en funciones reutilizables
def revision_numero(num):
    if num > 0:
        status = "positivo"
    elif num < 0:
        status = "negativo"
    else:
        status = "cero"
    return status

def determinarSiEsPar(num):
    if num % 2 == 0:
        status = "par"
    else:
        status = "impar"
    return status

numero = int (input ("Ingrese el número: "))
print("El número ingresado es ", revision_numero(numero), ", y es ", determinarSiEsPar(numero))

