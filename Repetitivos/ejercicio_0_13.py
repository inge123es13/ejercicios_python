
#Una empresa tiene el registro de las horas que trabaja diariamente un empleado 
#durante la semana (seis d�as) y requiere determinar el total de �stas, as� como 
#el sueldo que recibir� por las horas trabajadas.

print(' CalcularSueldo ')
	

horas_acum = 0  

sueldo_por_hora = float(input("Introduce el sueldo por hora: "))


for dia in range(1, 7):
    horas = float(input(f"¿Cuántas horas has trabajado el día {dia}? : "))
    horas_acum += horas 

print("\nHoras acumuladas en la semana:", horas_acum)
print("Sueldo semanal:", sueldo_por_hora * horas_acum)

print('FIN')
