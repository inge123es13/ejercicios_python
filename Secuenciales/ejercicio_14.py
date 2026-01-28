
#Dado un numero de dos cifras, diseñe un algoritmo que permita obtener el 
#numero invertido. 

print('Numero Invertido')
num = int(input("Dime un número de dos cifras: "))

decenas = num // 10
unidades = num % 10

print("Primera cifra (decenas):", decenas)
print("Segunda cifra (unidades):", unidades)
print("Número invertido:", unidades * 10 + decenas)
