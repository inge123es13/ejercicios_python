#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos 
#en el plano. Calcula y muestra la distancia entre ellos
import math 
print("Dime las coordenadas del punto 1:")
x1 = int(input("x1: "))
y1 = int(input("y1: "))


print("Dime las coordenadas del punto 2:")
x2 = int(input("x2: "))
y2 = int(input("y2: "))


distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Distancia:", distancia)


