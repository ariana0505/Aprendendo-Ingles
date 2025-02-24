#MEJORAS:
#Uso de mayusculas de minusculas y aceptos no interfieran en si es correcto o incorrecto



#Inportaciones: 
import random

#Variables defecto
score = 0;
diccionario = {}
texto = []

#Abriendo fichero
fichero = open('palabras.txt','r', encoding="utf-8")

#Recorriendo fichero
for linea in fichero:
    texto.append(linea.strip())

#Convirtiendo en diccionario
for i in range(len(texto)):
    valores = texto[i].split(" -> ")
    palabra = valores[0]
    significado = valores[1:]
    diccionario[palabra] = significado



for i in range(10):
    #obteniendo un item random
    clave, valor = random.choice(list(diccionario.items()))
    valor = ", ".join(valor)#me devuelve un str separado por comas
    valores = valor.split(", ")#me devuelveuna lista que esta separado por comas (", ")

    palabraIngresada = input(f"Ingrese el significado de la la palabra {clave}: ")
    if palabraIngresada in valores:
        print("Excelente! +1")
        score =+ 1
    else:
        print(f"Error el significado es {valor}")