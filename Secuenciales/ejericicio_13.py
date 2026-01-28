#Realizar un algoritmos que lea un n�mero y que muestre su ra�z cuadrada 
#y su ra�z c�bica.

import math
print ('Calcular Raiz cuadrada y cubica')
num = float(input("Dime el número: "))

raiz_cuadrada = math.sqrt(num)
raiz_cubica = num ** (1/3)

print("Raíz cuadrada:", raiz_cuadrada)
print("Raíz cúbica:", raiz_cubica)
