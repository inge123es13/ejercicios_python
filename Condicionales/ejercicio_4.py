# Crea un programa que pida al usuario dos números y muestre su división 
#si el segundo no es cero, o un mensaje de aviso en caso contrario.

print('CalcularDivision') 
dividendo = int(input('Ingresa el primer número: '))
divisor = int(input('Ingresa el segundo número: '))


if divisor == 0:
    print('No puedes dividir por 0 ')
else:
    print('La división es',dividendo/divisor)

print('Fin')