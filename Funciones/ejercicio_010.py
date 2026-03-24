
#Función Convertir_A_Segundos: Recibe una cantidad de horas, minutos y segundos 
#y calcula a cuantos segundos corresponde.
#Parámetros de entrada: hora, minutos y segundos
#Dato devuelto: Segundos totales

def convertir_a_segundos(h, m, s):
    return h * 3600 + m * 60 + s


def convertir_a_hms(seg):
    h = seg // 3600
    seg = seg - h * 3600

    m = seg // 60
    seg = seg - m * 60

    s = seg
    return h, m, s


def main():
    while True:
        print("1.- Convertir a segundos")
        print("2.- Convertir a horas, minutos y segundos")
        print("3.- Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            hor = int(input("Horas: "))
            min = int(input("Minutos: "))
            seg = int(input("Segundos: "))
            total = convertir_a_segundos(hor, min, seg)
            print("Corresponde a", total, "segundos.")

        elif opcion == 2:
            segund = int(input("Segundos: "))
            h, m, s = convertir_a_hms(segund)
            print(f"Corresponde a {h}:{m}:{s}")

        elif opcion == 3:
            print("Saliendo del programa...")
            break

        else:
            print("Opción incorrecta")


main()
print("Fin")