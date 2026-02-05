#Algoritmo que pida un número y diga si es positivo, negativo o 0.

print('Inicio') 
numero = int(input('Ingresa un número: '))

if numero > 0:
    print('Es un número positivo (+) ')
elif numero == 0:
    print('Es Cero')
else:
	print('Es un número negativo (-)')
print('Fin')