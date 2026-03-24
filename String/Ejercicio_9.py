#Realizar un programa que compruebe si una cadena contiene una subcadena.
# Las dos cadenas se introducen por teclado.
def contiene_subcadena(cadena, subcadena):
    return subcadena in cadena

def main():
    cad = input("Introduce una cadena: ")
    sub = input("Introduce una subcadena: ")

    if contiene_subcadena(cad, sub):
        print("La cadena contiene la subcadena.")
    else:
        print("La cadena no contiene la subcadena.")

if __name__ == "__main__":
    main()

print("Fin")

