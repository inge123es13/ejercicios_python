#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
print('Nombre y Apellido y Esto te muestra tus iniciales')
nombre = input("Dime tu nombre: ")
apellido1 = input("Dime tu primer apellido: ")
apellido2 = input("Dime tu segundo apellido: ")

inicial = nombre[0] + apellido1[0] + apellido2[0]
inicial = inicial.upper()

print("Las iniciales son:", inicial)
