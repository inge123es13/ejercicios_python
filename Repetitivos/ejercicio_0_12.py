
#Realizar un algoritmo para determinar cuánto ahorrar una persona en un año, 
#si al final de cada mes deposita cantidades variables de dinero; 
#además, se quiere saber cuánto lleva ahorrado cada mes.

print ('CalcularAhorro')


ahorro_acum = 0  

for mes in range(1, 13):  
    cant_mensual = float(input(f"¿Cuánto has ahorrado en el mes {mes}? : "))
    
    ahorro_acum += cant_mensual  
    print(f"En el mes {mes} llevas ahorrado {ahorro_acum}")

print(f"\nTotal ahorrado en el año: {ahorro_acum}")

print('Fin')