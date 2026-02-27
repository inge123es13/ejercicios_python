#Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad 
#de números primos que queremos mostrar.

import math


while True:
    cant_a_mostrar = int(input("Ingrese la cantidad de números primos a mostrar: "))
    if cant_a_mostrar > 0:
        break


print("1: 2")
cant_mostrados = 1
num = 3  


while cant_mostrados < cant_a_mostrar:

    es_primo = True  
    
    for divisor in range(3, int(math.sqrt(num)) + 1, 2):
        if num % divisor == 0:
            es_primo = False
            break  

    if es_primo:
        cant_mostrados += 1
        print(f"{cant_mostrados}: {num}")

    num += 2 
print("Fin")
