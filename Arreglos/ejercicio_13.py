#De una empresa de transporte se quiere guardar el nombre de los conductores que 
#tiene, y los kilómetros que conducen cada día de la semana.
#Para guardar esta información se van a utilizar dos arreglos:
# * Nombre: Vector para guardar los nombres de los conductores.
# * kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
#Se quiere generar un nuevo vector ("total_kms") con los kilómetros totales que 
#realza cada conductor.
#Al finalizar se muestra la lista con los nombres de conductores y los kilómetros 
#que ha realizado.

nombre = []
kms = []
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

tam_conductores_max = 10

while True:
    num_conductores = int(input("¿Cuántos conductores tiene la empresa?: "))
    if num_conductores <= tam_conductores_max:
        break
    else:
        print(f"Como máximo puedo guardar la información de {tam_conductores_max} conductores")

for i in range(num_conductores):
    n = input(f"Nombre del conductor {i+1}: ")
    nombre.append(n)
    
    fila_kms = []
    for j in range(7):
        km = int(input(f"¿Cuántos km ha realizado el {dias[j]}?: "))
        fila_kms.append(km)
    fila_kms.append(0)
    kms.append(fila_kms)

for i in range(num_conductores):
    for j in range(7):
        kms[i][7] += kms[i][j]

for i in range(num_conductores):
    print(f"{nombre[i]} ha realizado {kms[i][7]} kms.")