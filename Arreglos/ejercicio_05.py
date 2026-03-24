
#Hacer un programa que inicialice un vector de números con valores aleatorios, 
#y posterior ordene los elementos de menor a mayor.

import random

vector = []
tam_vector = 10

for i in range(tam_vector):
    vector.append(random.randint(1, 10))

while True:
    cambios = 0
    for i in range(tam_vector - 1):
        if vector[i] > vector[i + 1]:
            aux = vector[i]
            vector[i] = vector[i + 1]
            vector[i + 1] = aux
            cambios += 1
    if cambios == 0:
        break

for num in vector:
    print(num, end=" ")

print("Fin")
