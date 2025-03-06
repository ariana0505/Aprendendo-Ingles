#MEJORAS:
#Uso de mayusculas de minusculas y aceptos no interfieran en si es correcto o incorrecto
#El usuario oingreara cuantas palabra quiere practicar


from condicion import condicional
from unidecode import unidecode

#Inportaciones: 
import random

#Variables defecto
diccionario = {}
texto = []
score =0

#Abriendo fichero
fichero = open('palabras.txt','r', encoding="utf-8")

#Recorriendo fichero
for linea in fichero:
    texto.append(unidecode(linea.strip()))

#Convirtiendo en diccionario
for i in range(len(texto)):
    valores = texto[i].split(" -> ")
    palabra = valores[0]
    significado = valores[1:] 
    diccionario[palabra] = significado

print(texto)
intentos = int(input("Ingrese el numero de intentos: "))

for i in range(intentos):
    #obteniendo un item random
    clave, valor = random.choice(list(diccionario.items()))
    valor = ", ".join(valor)#me devuelve un str separado por comas
    valores = valor.split(", ")#me devuelveuna lista que esta separado por comas (", ")
    palabraIngresada = input(f"Ingrese el significado de la la palabra {clave}: ").strip()
    score = condicional(unidecode(palabraIngresada), valores, score)
else:
    print(f"Tu puntuacion es: {score}")