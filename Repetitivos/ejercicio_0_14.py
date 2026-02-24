#Una persona se encuentra en el kil�metro 70 de una carretera, otra se encuentra 
#en el km 150, los coches tienen sentido opuesto y tienen la misma velocidad. 
#Realizar un programa para determinar en qué kilómetro de esa carretera se 
#encontrarán.

print("Calcular Km donde se encuentran")

km1 = 70
km2 = 150

# Mientras no estén en el mismo kilómetro
while km1 != km2:
    km1 += 1
    km2 -= 1

print("Se encuentran en el km:", km1)
print("Fin")

