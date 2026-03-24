
#Programa que declare un vector de diez elementos enteros y pida números para 
#rellenarlo hasta que se llene el vector o se introduzca un número negativo. 
#Entonces se debe imprimir el vector (s0lo los elementos introducidos).
vector = []
tam_vector = 10
indice = 0

while indice < tam_vector:
    num = int(input(f"Introduce un número en el vector. Número {indice+1}: "))
    vector.append(num)
    indice += 1
    if num < 0:
        break

indice = 0
print("Elementos del vector")

while indice < len(vector) and vector[indice] >= 0:
    print(vector[indice], end=" ")
    indice += 1

print("Fin")
