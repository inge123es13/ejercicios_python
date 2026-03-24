
#Queremos guardar los nombres y la edades de los alumnos de un curso. 
#Realiza un programa que introduzca el nombre y la edad de cada alumno. 
#El proceso de lectura de datos terminará cuando se introduzca como nombre 
#un asterisco (*) Al finalizar se mostrará los siguientes datos:
# * Todos lo alumnos mayores de edad.
# * Los alumnos mayores (los que tienen más edad)
nombre = []
edad = []
tam_vector = 30

indice = 0

while indice < tam_vector:
    n = input("Dime el nombre de un alumno: ")
    nombre.append(n)
    if n != "*":
        e = int(input("Dime su edad: "))
        edad.append(e)
    else:
        break
    indice += 1

edad_max = edad[0]
indice = 0

while indice < len(nombre) and nombre[indice] != "*":
    if edad[indice] > edad_max:
        edad_max = edad[indice]
    indice += 1

indice = 0
print("Alumnos mayores de edad")
print("=======================")

while indice < len(nombre) and nombre[indice] != "*":
    if edad[indice] >= 18:
        print(nombre[indice])
    indice += 1

indice = 0
print("Alumnos mayores")
print("===============")

while indice < len(nombre) and nombre[indice] != "*":
    if edad[indice] == edad_max:
        print(nombre[indice])
    indice += 1
print("Fin")
