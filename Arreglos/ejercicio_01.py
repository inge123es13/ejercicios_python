
#Realizar un programa que defina un vector llamado "vector_numeros" de 10 enteros,
# a continuación lo inicialice con valores aleatorios (del 1 al 10) 
#y posteriormente muestre en pantalla cada elemento del vector junto con 
#su cuadrado y su cubo.

import random 
print(" CuadradoCuboVector")
numeros = []
	
for i in range (10):
    numeros.append(random.randint(1,10))

for n in numeros:
    print('numero:' , n)
    print('cuadrado:' , n**2)
    print('cubo:' , n**3)
print("Fin")
	