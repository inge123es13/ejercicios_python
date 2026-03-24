
#Procedimiento Intercambiar: Recibe dos números como parámetros de entrada y 
#salida e intercambia sus valores si el segundo es mayor que el primero.
#Parámetros de entrada y salida: dos números

def intercambiar(a, b):
    if a < b:
        return b, a
    return a, b


def calcular_mcd(a, b):
    a, b = intercambiar(a, b)
    if b == 0:
        return a
    return calcular_mcd(b, a % b)


def simplificar_fraccion(num, den):
    mcd = calcular_mcd(num, den)
    return num // mcd, den // mcd


def leer_fraccion():
    num = int(input("Numerador: "))
    den = int(input("Denominador: "))
    return simplificar_fraccion(num, den)


def escribir_fraccion(num, den):
    if den != 1:
        print(f"{num}/{den}")
    else:
        print(num)


def sumar_fracciones(n1, d1, n2, d2):
    nr = n1 * d2 + d1 * n2
    dr = d1 * d2
    return simplificar_fraccion(nr, dr)


def restar_fracciones(n1, d1, n2, d2):
    nr = n1 * d2 - d1 * n2
    dr = d1 * d2
    return simplificar_fraccion(nr, dr)


def multiplicar_fracciones(n1, d1, n2, d2):
    nr = n1 * n2
    dr = d1 * d2
    return simplificar_fraccion(nr, dr)


def dividir_fracciones(n1, d1, n2, d2):
    nr = n1 * d2
    dr = d1 * n2
    return simplificar_fraccion(nr, dr)


def main():
    while True:
        print("1.- Sumar dos fracciones")
        print("2.- Restar dos fracciones")
        print("3.- Multiplicar dos fracciones")
        print("4.- Dividir dos fracciones")
        print("5.- Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 5:
            break

        if opcion in [1, 2, 3, 4]:
            print("Fracción 1:")
            num1, den1 = leer_fraccion()

            print("Fracción 2:")
            num2, den2 = leer_fraccion()

            if opcion == 1:
                numr, denr = sumar_fracciones(num1, den1, num2, den2)
            elif opcion == 2:
                numr, denr = restar_fracciones(num1, den1, num2, den2)
            elif opcion == 3:
                numr, denr = multiplicar_fracciones(num1, den1, num2, den2)
            elif opcion == 4:
                numr, denr = dividir_fracciones(num1, den1, num2, den2)

            escribir_fraccion(numr, denr)
        else:
            print("Opción incorrecta")


if __name__ == "__main__":
    main()
print("Fin")
