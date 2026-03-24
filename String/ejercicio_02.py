#Realizar un programa que comprueba si una cadena leída por teclado comienza por 
#una subcadena introducida por teclado.

cadena=  input(" Escribe una frase:")
subcad = input("Escribe una subcadena")

if cadena.startswith(subcad):
    print(f"{cadena} comienza con {subcad}")
else:
    print(f"{cadena}  no comienza con {subcad}")

print("Fin")