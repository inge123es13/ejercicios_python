#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

print ('Conversión de Fahrenheit a Celsius')
fahrenheit = float(input("Ingresa los grados Fahrenheit: "))
celsius = (fahrenheit - 32) * (5 / 9)

print('Grados Fahrenheit', fahrenheit)
print('Grados Celsius', celsius)

print(f' { fahrenheit}°F equivalen a { celsius }°C')
