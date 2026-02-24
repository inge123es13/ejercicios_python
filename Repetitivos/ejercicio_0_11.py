
#Escribe un programa que diga si un n�mero introducido por teclado es o no primo. 
#Un n�mero primo es aquel que s�lo es divisible entre �l mismo y la unidad. 
#Nota: Es suficiente probar hasta la ra�z cuadrada del n�mero para ver si es 
#divisible por alg�n otro n�mero.


print('EsPrimo')
import math

es_primo = True

numero = int(input("Introduce un número para comprobar si es primo: "))

if numero <= 1:
    es_primo = False
else:

    for num in range(2, int(math.sqrt(numero)) + 1):
        if numero % num == 0:
            es_primo = False
            break 

if es_primo:
    print("Es Primo")
else:
    print("No es Primo")
print("Fin")
