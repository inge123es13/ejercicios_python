
#Escribir un programa que lea un año indicar si es bisiesto. 
#Nota: un año es bisiesto si es un numero divisible por 4, pero no si es divisible por 100,
# excepto que tambi�n sea divisible por 400.

print('Año')
year = int(input("Introduce el año: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Año bisiesto.")
else:
    print("Año no bisiesto.")
    
print('Fin')