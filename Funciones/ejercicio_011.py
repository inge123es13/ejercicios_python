
#Función EsBisiesto: Recibe un año y devuelve si es o no bisiesto
#Parámetros de entrada: año
#Dato devuelto: Valor lógico indicando si es bisiesto (Verdadero) o no (Falso)
def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def dias_del_mes(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if es_bisiesto(year):
            return 29
        else:
            return 28


def calcular_dia_juliano(day, month, year):
    diaj = 0
    for mes in range(1, month):
        diaj += dias_del_mes(mes, year)
    diaj += day
    return diaj


def leer_fecha():
    day = int(input("Día: "))
    month = int(input("Mes: "))
    year = int(input("Año: "))
    return day, month, year


def main():
    d, m, a = leer_fecha()
    print("Día Juliano:", calcular_dia_juliano(d, m, a))


if __name__ == "__main__":
    main()

print("Fin")