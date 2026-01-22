# Un alumno desea saber cual ser� su calificaci�n final en la materia de Algoritmos
# Dicha calificaci�n se compone de los siguientes porcentajes:
# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificaci�n del examen final.
# 15% de la calificaci�n de un trabajo final.

print ('Calificación final')
parcial1= float(input("Ingresa la nota del parcial 1 :) : "))
parcial2= float(input("Ingresa la nota del parcial 2 :) : "))
parcial3= float(input("Ingresa la nota del parcial 3 :) : "))
examen= float(input("Ingresa la nota del examen :) : "))
trabajo= float(input("Ingresa la nota del trabajo :) : "))
nota  = ((parcial1 + parcial2 + parcial3)/3) * 0.55 + 0.3 *examen + 0.15*trabajo
print('Nota final : ',nota)

