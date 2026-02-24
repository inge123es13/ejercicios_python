
# Crea una aplicación que permita adivinar un número. La aplicación genera un 
# número aleatorio del 1 al 100. A continuación va pidiendo números y va 
# respondiendo si el n�mero a adivinar es mayor o menor que el introducido,
# a dem�s de los intentos que te quedan (tienes 10 intentos para acertarlo). 
# El programa termina cuando se acierta el n�mero (adem�s te dice en cuantos 
#intentos lo has acertado), si se llega al limite de intentos te muestra el 
#n�mero que hab�a generado.

import random

numero_escondido = random.randint(1,100)
intentos = 0


while intentos < 10:
    numero = int(input ('Adivina el número: '))
    intentos = intentos + 1
    if numero_escondido == numero:
        print('Lo Adivinaste')
        print('Fueron', intentos, 'intentos')
        break
    elif numero_escondido > numero:
        print('Mas grande')
    else:
        print('Mas pequeño')

if intentos == 10:
    print("Perdiste: Buu")
print('Fin')