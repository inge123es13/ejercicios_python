
#Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. 
#Realice un algoritmo para determinar el sueldo semanal de N trabajadores 
#y, además, calcule cuánto pagá la empresa por los N empleados.


print('CalcularSalario')
horas_acum = 0

trabajadores = int(input("¿Cuántos trabajadores tiene la empresa?: "))
sueldo_por_hora = float(input("Sueldo por hora: "))

for trabajador in range(1, trabajadores + 1):
    horas_por_semana = int(input(f"¿Cuántas horas ha trabajado el trabajador {trabajador}? "))
    
    sueldo = horas_por_semana * sueldo_por_hora
    horas_acum += horas_por_semana
    
    print(f"El trabajador {trabajador} tiene de sueldo {sueldo}")

total_pago = horas_acum * sueldo_por_hora

print(f"El pago a los {trabajadores} trabajadores es: {total_pago}")
print("Fin")