#Pide una cadena y dos caracteres por teclado (valida que sea un carácter), 
#sustituye la aparición del primer carácter en la cadena por el segundo carácter.


def obtener_caracter(mensaje):
    while True:
        car = input(mensaje)
        if len(car) == 1:
            return car

def sustituir_caracteres(cadena, buscar, sustituir):
    nueva_cadena = ""
    for caracter in cadena:
        if caracter == buscar:
            nueva_cadena += sustituir
        else:
            nueva_cadena += caracter
    return nueva_cadena

def main():
    cad = input("Introduce una cadena: ")

    car_buscar = obtener_caracter("Introduce un caracter a buscar: ")
    car_sustituir = obtener_caracter("Introduce un caracter para sustituir: ")

    newcad = sustituir_caracteres(cad, car_buscar, car_sustituir)

    print(f"La cadena modificada es: {newcad}")

if __name__ == "__main__":
    main()

print("Fin")