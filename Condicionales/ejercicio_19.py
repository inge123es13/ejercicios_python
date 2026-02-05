
#Escribe un programa que pida un numero entero entre uno y doce e imprima el 
#numero de dias que tiene el mes correspondiente.
# Si introducimos otro numero nos da un error.

print("Dias del mes")

mes = int(input("Introduce el número de mes (1-12): "))

if mes in (1, 3, 5, 7, 8, 10, 12):
    print("31 días")
elif mes == 2:
    print("28 o 29 días")
elif mes in (4, 6, 9, 11):
    print("30 días")
else:
    print("Mes incorrecto")
print('Fin')