from condicion import condicional
from unidecode import unidecode

import random

diccionario = {}
texto = []
score =0
memoria = []

fichero = open('palabras.txt','r', encoding="utf-8")

for linea in fichero:
    texto.append(unidecode(linea.strip()))

for i in range(len(texto)):
    valores = texto[i].split(" -> ")
    palabra = valores[0]
    significado = valores[1:] 
    diccionario[palabra] = significado

intentos = int(input("Ingrese el numero de intentos: "))

for i in range(intentos):
    clave, valor = random.choice(list(diccionario.items()))

    if clave in memoria:
        continue
    
    memoria.append(clave)
    valor = ", ".join(valor)
    valores = valor.split(", ")
    palabraIngresada = input(f"Ingrese el significado de la la palabra {clave}: ").strip()
    score = condicional(unidecode(palabraIngresada), valores, score)

print(f"Tu puntuacion es: {score}")