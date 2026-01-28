#Dos veh�culos viajan a diferentes velocidades (v1 y v2) y est�n distanciados 
#por una distancia d. 
#El que est� detr�s viaja a una velocidad mayor. Se pide hacer un algoritmo 
#para ingresar la distancia entre los dos veh�culos (km) y sus respectivas 
#velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) 
#alcanzar� el veh�culo m�s r�pido al otro.
print('Dos Veiculos ')
velocidad1 = float(input("Dime la velocidad del coche 1 (km/h): "))
velocidad2 = float(input("Dime la velocidad del coche 2 (más pequeña) (km/h): "))
distancia = float(input("Dime la distancia entre los coches (km): "))

if velocidad1 <= velocidad2:
    print("Error: el coche que va detrás debe tener mayor velocidad.")
else:
    tiempo_horas = distancia / (velocidad1 - velocidad2)
    tiempo_minutos = tiempo_horas * 60
    print("Lo alcanza en", tiempo_minutos, "minutos.")


