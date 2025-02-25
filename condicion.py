
def condicional(palabraIngresada , valores):
    score = 0
    if palabraIngresada in valores:
        print("Excelente! +1")
        score =+ 1 
    else:
        valor = ", ".join(valores)
        print(f"Error el significado es {valor}")
    