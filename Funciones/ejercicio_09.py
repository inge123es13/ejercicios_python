
#Procedimiento Intercambiar: Recibe dos números como parámetros de entrada y 
#salida e intercambia sus valores si el segundo es mayor que el primero.
#Parámetros de entrada y salida: dos números
# Procedimiento Intercambiar
def intercambiar(mayor, menor):
    if mayor < menor:
        return menor, mayor
    return mayor, menor


def calcular_mcd(num1, num2):
    num1, num2 = intercambiar(num1, num2)
    resto = num1 % num2

    if resto == 0:
        return num2
    else:
        return calcular_mcd(num2, resto)

def main():
    numero1 = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))
    
    print("MCD:", calcular_mcd(numero1, numero2))



main()
print("Fin")