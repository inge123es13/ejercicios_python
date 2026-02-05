
#El director de una escuela esta organizando un viaje de estudios, y requiere 
#determinar cuanto debe cobrar a cada alumno y cuanto debe pagar a la compañia de 
#viajes por el servicio. La forma de cobrar es la siguiente: 
#si son 100 alumnos o mas, el costo por cada alumno es de 65 euros; 
#de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
#y si son menos de 30, el costo de la renta del autobus es de 4000 euros, 
#sin importar el numero de alumnos. 
#Realice un algoritmo que permita determinar el pago a la compañia de autobuses 
#y lo que debe pagar cada alumno por el viaje.

print("Autobuses")

num_alumnos = int(input("¿Cuántos alumnos participan en la actividad?: "))

if num_alumnos <= 0:
    print("El número de alumnos debe ser un valor positivo.")
else:
    if num_alumnos >= 100:
        coste_por_alumno = 65
    elif num_alumnos >= 50:
        coste_por_alumno = 70
    elif num_alumnos >= 30:
        coste_por_alumno = 95
    else:
        coste_por_alumno = 4000 / num_alumnos

    coste_autobus = num_alumnos * coste_por_alumno

    print("El coste por alumno es", coste_por_alumno, "euros.")
    print("El coste del autobús es", coste_autobus, "euros.")
print('Fin')