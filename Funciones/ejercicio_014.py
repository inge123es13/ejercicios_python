
#Procedimiento IncializarPila: Recibe un vector (pila) y su tamaño. 
#Recorre el vector e inicializa sus elementos a *. 
#El * representa que el elemento esta vacio.
#Parametros de entrada: Tamaño del vector
#Parametros de entrada y salida: El vector (pila)

def inicializar_pila(pila, size):
    for i in range(size):
        pila[i] = "*"


def longitud_pila(pila, size):
    count = 0
    while count < size and pila[count] != "*":
        count += 1
    return count


def esta_vacia_pila(pila, size):
    return longitud_pila(pila, size) == 0


def esta_llena_pila(pila, size):
    return longitud_pila(pila, size) == size


def add_pila(elem, pila, size):
    if not esta_llena_pila(pila, size):
        pila[longitud_pila(pila, size)] = elem
    else:
        print("No se puede añadir elemento. La pila está llena")


def sacar_de_la_pila(pila, size):
    if not esta_vacia_pila(pila, size):
        pos = longitud_pila(pila, size) - 1
        elem = pila[pos]
        pila[pos] = "*"
        return elem
    else:
        print("No se puede sacar elemento. La pila está vacía")
        return ""


def escribir_pila(pila, size):
    i = 0
    while i < size and pila[i] != "*":
        print(pila[i], end=" ")
        i += 1
    print()


def main():
    tam_pila = 10
    mipila = [""] * tam_pila
    inicializar_pila(mipila, tam_pila)

    while True:
        print("1.- Añadir elemento a la pila")
        print("2.- Sacar elemento de la pila")
        print("3.- Longitud de la pila")
        print("4.- Mostrar pila")
        print("5.- Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 5:
            break
        elif opcion == 1:
            elem = input("Dame la cadena para añadir a la pila: ")
            add_pila(elem, mipila, tam_pila)
        elif opcion == 2:
            print(sacar_de_la_pila(mipila, tam_pila))
        elif opcion == 3:
            print("Longitud:", longitud_pila(mipila, tam_pila))
        elif opcion == 4:
            escribir_pila(mipila, tam_pila)
        else:
            print("Opción incorrecta")


if __name__ == "__main__":
    main()
print("Fin")
