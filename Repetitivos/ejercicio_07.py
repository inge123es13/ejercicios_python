
#Realizar una algoritmo que muestre la tabla de multiplicar de un número 
#introducido por teclado.

print('Tabla de Un número')
tabla = int(input("¿De qué número quieres mostrar la tabla de multiplicar?: "))

for num in range(1, 11):
    print(f"{tabla} * {num} = {tabla * num}")
print('Fin')
