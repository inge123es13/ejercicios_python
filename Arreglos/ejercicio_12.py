
#DiseÑar el algoritmo correspondiente a un programa, que:
# * Crea una tabla bidimensional de longitud 5x15 y nombre 'marco'.
# * Carga la tabla con dos Unicos valores 0 y 1, donde el valor uno ocuparA las 
#posiciones o elementos que delimitan la tabla, es decir, las mAs externas, 
#mientras que el resto de los elementos contendrAn el valor 0.
matriz = []
num_filas = 5
num_cols = 15

for fila in range(num_filas):
    fila_actual = []
    for col in range(num_cols):
        if fila == 0 or fila == num_filas - 1 or col == 0 or col == num_cols - 1:
            fila_actual.append(1)
        else:
            fila_actual.append(0)
    matriz.append(fila_actual)

for fila in range(num_filas):
    for col in range(num_cols):
        print(matriz[fila][col], end="")
    print()
    
