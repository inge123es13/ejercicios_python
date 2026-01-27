#Condicionales con python
#if, else, elif
"""" 
  if exp_bool:
    instrucciones

    if exp_bool:
    	instrucciones
    else:
    	instrucciones

    if expo_bool:
    	instrucciones
    elif expo_booñ:
    	instrucciones
    else:
    	instrucciones
    	"""

print('Inicio') 
numero = int(input('Ingresa un número: '))

if numero > 0:
    print('Es un número positivo ')
elif numero == 0:
    print('Es Cero')
else:
	print('Es un número negativo (-)')
print('Fin')
