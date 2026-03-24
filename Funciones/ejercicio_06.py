
#Procedimiento CalcularAreaPerimetro: recibe el radio de una circunferencia y
#devuelve el área y el perímetro.
#Parámetros de entrada: radio (real)
#Parámetros de entrada y salida: área y perímetro (real)

import math

def calcularAreaPerimetro(radio):
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area, perimetro




#Diseñar una función que calcule el área y el perímetro de una circunferencia. 
#Utiliza dicha función en un programa principal que lea el radio de una 
#circunferencia y muestre su área y perímetro.

radio = float(input("Introduce el radio: "))

area, perimetro = calcularAreaPerimetro(radio)

print("Área:", area)
print("Perímetro:", perimetro)

print("Fin")