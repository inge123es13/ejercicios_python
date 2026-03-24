#Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra 
#palíndroma es aquella que se lee igual adelante que atrás.
def es_palindromo(cadena):
    return cadena == cadena[::-1]

def main():
    palindromo = input("Introduce una cadena: ")

    if es_palindromo(palindromo):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")

if __name__ == "__main__":
    main()
print("FIN")