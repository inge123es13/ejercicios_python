
#Queremos guardar la temperatura minima y máxima de 5 días. realiza un programa 
#que de la siguiente informacion:
# * La temperatura media de cada dia
# * Los días con menos temperatura
# * Se lee una temperatura por teclado y se muestran los días cuya temperatura 
#máxima coincide con ella.Si no existe ningún día se muestra un mensaje de 
#información.

temperatura = []
cant_dias = 5

for i in range(cant_dias):
    temp_min = float(input(f"Día {i+1}. Temperatura mínima: "))
    temp_max = float(input(f"Día {i+1}. Temperatura máxima: "))
    temperatura.append([temp_min, temp_max])

print("Temperaturas medias")
print("===================")

for i in range(cant_dias):
    media = (temperatura[i][0] + temperatura[i][1]) / 2
    print(f"Día {i+1}. Temperatura media: {media}")

temp_min = temperatura[0][0]

for i in range(cant_dias):
    if temperatura[i][0] < temp_min:
        temp_min = temperatura[i][0]

print("Días con menos temperatura")
print("==========================")

for i in range(cant_dias):
    if temperatura[i][0] == temp_min:
        print(f"Día {i+1}")

existe_temperatura = False

print("Días con temperatura máxima")
print("===========================")

temp_max_buscar = float(input("Introduce una temperatura: "))

for i in range(cant_dias):
    if temperatura[i][1] == temp_max_buscar:
        print(f"Día {i+1}")
        existe_temperatura = True

if not existe_temperatura:
    print("No hay ningún día con dicha temperatura.")

print("Fin")
