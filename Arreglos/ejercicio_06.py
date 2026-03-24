
#Crea un programa que pida un numero al usuario un número de mes (por ejemplo, 
#el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. 
#Debes usar un vector. Para simplificarlo vamos a suponer que febrero tiene 28 dáas.

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

nombre_mes = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

while True:
    mes = int(input("Introduce un mes (1-12): "))
    if 1 <= mes <= 12:
        break
    else:
        print("Error: mes incorrecto.")

print(f"El mes de {nombre_mes[mes-1]} tiene {dias[mes-1]} días.")

print("FIn")