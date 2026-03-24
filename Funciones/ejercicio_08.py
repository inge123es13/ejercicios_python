
#Función CalcularFactorial: Recibe un numero si el número=1 devuelve que el 
#factorial es 1, sino acumula el producto del número con el cálculo del factorial 
#del numero-1. Es una función recursiva.
#Parámetros de entrada: número
#Dato devuelto: Factorial del número

def calcular_factorial(num):
    if num == 1:
        return 1
    else:
        return num * calcular_factorial(num - 1)


def main():
    numero = int(input("Número: "))
    print("El factorial es:", calcular_factorial(numero))


if __name__ == "__main__":
    main()
print("Fin")