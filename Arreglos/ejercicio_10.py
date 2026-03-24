
#Dise�ar el algoritmo correspondiente a un programa, que:
# * Crea una tabla bidimensional de longitud 5x5 y nombre 'matriz'.
# * Carga la tabla con valores num�ricos enteros.
# * Suma todos los elementos de cada fila y todos los elementos de cada columna 
#visualizando los resultados en pantalla.

matriz = []
num_filas = 5
num_cols = 5

for fila in range(num_filas):
    fila_actual = []
    for col in range(num_cols):
        num = int(input(f"Introduce el número de la fila {fila+1} y columna {col+1}: "))
        fila_actual.append(num)
    matriz.append(fila_actual)

for fila in range(num_filas):
    suma = 0
    for col in range(num_cols):
        suma += matriz[fila][col]
    print(f"La suma de los elementos de la fila {fila+1} es {suma}")

for col in range(num_cols):
    suma = 0
    for fila in range(num_filas):
        suma += matriz[fila][col]
    print(f"La suma de los elementos de la columna {col+1} es {suma}")

print("FIN")
	
