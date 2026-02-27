
#Una empresa les paga a sus empleados con base en las horas trabajadas en la semana
#Para esto, se registran los dias que trabaja y las horas de cada dia. 
#Realice un algoritmo para determinar el sueldo semanal de N trabajadores 
#y ademas calcule cuanto paga la empresa por los N empleados.

print('Pago a empleados')

trabajadores = int(input("¿Cuántos trabajadores tiene la empresa?: "))
sueldo_por_hora = float(input("Sueldo por hora: "))

horas_acum = 0

for trabajador in range(1, trabajadores + 1):
    horas_por_trabajador = 0
    
    dias = int(input(f"¿Cuántos días trabajó el trabajador {trabajador}?: "))
    
    for dia in range(1, dias + 1):
        horas = int(input(f"Horas trabajadas el día {dia}: "))
        horas_por_trabajador += horas
    
    sueldo = horas_por_trabajador * sueldo_por_hora
    print(f"El trabajador {trabajador} tiene de sueldo {sueldo}")
    
    horas_acum += horas_por_trabajador

total_pago = horas_acum * sueldo_por_hora
print(f"El pago total a los trabajadores es: {total_pago}")
print("Fin")