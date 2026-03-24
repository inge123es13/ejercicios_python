#Si tenemos una cadena con un nombre y apellidos, realizar un programa que 
#muestre las iniciales en mayúsculas.

fullname= input('Escribe tu nombre completo: ')

words = fullname.split(' ')
iniciales = ''
for word in words:
    iniciales += word[0]
print( iniciales.upper())

print("Fin")