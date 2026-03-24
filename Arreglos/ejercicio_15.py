
# Crear un programa de ordenador para gestionar los resultados de la quiniela de 
#f�tbol. Para ello vamos a utilizar dos tablas:
# Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre 
#de los equipos de cada partido. En la quiniela se indican 15 partidos.
# Resultados: Es una tabla de enteros donde se indica el resultado. También tiene 
#dos columnas, en la primera se guarda el número de goles del equipo que está
#guardado en la primera columna de la tabla anterior, y en la segunda los goles 
#del otro equipo.
#El programa ira pidiendo los nombres de los equipos de cada partido y el 
#resultado del partido, a continuación se imprimirá la quiniela de esa jornada.
equipos = []
resultados = []
num_equipos = 15

for i in range(num_equipos):
    eq1 = input(f"Introduce el nombre del equipo 1 del partido {i+1}: ")
    eq2 = input(f"Introduce el nombre del equipo 2 del partido {i+1}: ")
    goles1 = int(input(f"Introduce los goles metidos por el equipo {eq1}: "))
    goles2 = int(input(f"Introduce los goles metidos por el equipo {eq2}: "))
    
    equipos.append([eq1, eq2])
    resultados.append([goles1, goles2])

print("QUINIELA")
print("========")

for i in range(num_equipos):
    if resultados[i][0] > resultados[i][1]:
        signo = "1"
    elif resultados[i][0] < resultados[i][1]:
        signo = "2"
    else:
        signo = "X"
    
    print(f"{equipos[i][0]} - {equipos[i][1]} -> {signo}")
print("FIN")
