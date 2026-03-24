def convertir_may_min(cad):
    newcad = ""

    for posicion in range(len(cad)):
        caracter = cad[posicion]

        if caracter == caracter.upper():
            newcad += caracter.lower()
        elif caracter == caracter.lower():
            newcad += caracter.upper()

    return newcad


cad = input("Introduce una cadena: ")
newcad = convertir_may_min(cad)

print("La cadena convertida es:", newcad)