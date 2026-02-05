
#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las 
#dimensiones de los lados de un tri�ngulo. 
#El programa debe determinar que tipo de tri�ngulo es, teniendo en cuenta:
#Si se cumple Pit�goras entonces es tri�ngulo rect�ngulo
#Si s�lo dos lados del tri�ngulo son iguales entonces es is�sceles.
#Si los 3 lados son iguales entonces es equil�tero.
#Si no se cumple ninguna de las condiciones anteriores, es escaleno.

print('Triángulos')
# Lectura de datos
ladoA = float(input("Introduce longitud lado A: "))
ladoB = float(input("Introduce longitud lado B: "))
ladoC = float(input("Introduce longitud lado C: "))

# Comprobación de triángulo rectángulo (Pitágoras)
if (ladoA**2 + ladoB**2 == ladoC**2 or
    ladoB**2 + ladoC**2 == ladoA**2 or
    ladoC**2 + ladoA**2 == ladoB**2):
    print("Triángulo Rectángulo")

# Comprobación del tipo según lados
if ((ladoA == ladoB and ladoA != ladoC) or
    (ladoB == ladoC and ladoB != ladoA) or
    (ladoC == ladoA and ladoC != ladoB)):
    print("Triángulo Isósceles")
elif ladoA == ladoB and ladoA == ladoC:
    print("Triángulo Equilátero")
else:
    print("Triángulo Escaleno")

print('Fin')