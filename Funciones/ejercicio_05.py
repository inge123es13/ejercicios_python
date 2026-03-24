
#Procedimiento CalcularMaxMin: recibe un vector de enteros, su tamaño, y devuelve
# el máximo y el mínimo de los números guardados en el vector.
#Parámetros de entrada: vector de enteros y tamaño
#Parámetros de entrada y salida: valor máximo y mínimo
import random

# Función CalcularMaxMin: recibe un arreglo y devuelve el máximo y el mínimo
def calcularMaxMin(vector):
    maximo = vector[0]
    minimo = vector[0]

    for i in range(len(vector)):
        if maximo < vector[i]:
            maximo = vector[i]
        if minimo > vector[i]:
            minimo = vector[i]

    return maximo, minimo

#Crea una función "calcularMaxMin" que recibe una arreglo con valores númerico y 
#devuelve el valor máximo y el mínimo. Crea un programa que pida números por 
#teclado y muestre el máximo y el mínimo, utilizando la función anterior.

lista = []
size_lista = 10

for i in range(size_lista):
    lista.append(random.randint(1, 100))


vmax, vmin = calcularMaxMin(lista)

print("Lista:", lista)
print("El valor máximo es", vmax)
print("El valor mínimo es", vmin)