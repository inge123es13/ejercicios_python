
#Procedimiento IncializarCola: Recibe un vector (cola) y su tamaño. 
#Recorre el vector e inicializa sus elementos a *. 
#El * representa que el elemento esta vacio.
#Parametros de entrada: Tamaño del vector
#Parametros de entrada y salida: El vector (cola)

def inicializar_cola(cola, size):
    for i in range(size):
        cola[i] = "*"


def longitud_cola(cola, size):
    count = 0
    while count < size and cola[count] != "*":
        count += 1
    return count


def esta_vacia_cola(cola, size):
    return longitud_cola(cola, size) == 0


def esta_llena_cola(cola, size):
    return longitud_cola(cola, size) == size


def add_cola(elem, cola, size):
    if not esta_llena_cola(cola, size):
        cola[longitud_cola(cola, size)] = elem
    else:
        print("No se puede añadir elemento. La cola está llena")


def sacar_de_la_cola(cola, size):
    if not esta_vacia_cola(cola, size):
        elem = cola[0]
        for i in range(size - 1):
            cola[i] = cola[i + 1]
        cola[size - 1] = "*"
        return elem
    else:
        print("No se puede sacar elemento. La cola está vacía")
        return ""


def escribir_cola(cola, size):
    i = 0
    while i < size and cola[i] != "*":
        print(cola[i], end=" ")
        i += 1
    print()


def main():
    tam_cola = 3
    micola = [""] * tam_cola
    inicializar_cola(micola, tam_cola)

    while True:
        print("1.- Añadir elemento a la cola")
        print("2.- Sacar elemento de la cola")
        print("3.- Longitud de la cola")
        print("4.- Mostrar cola")
        print("5.- Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 5:
            break
        elif opcion == 1:
            elem = input("Dame la cadena para añadir a la cola: ")
            add_cola(elem, micola, tam_cola)
        elif opcion == 2:
            print(sacar_de_la_cola(micola, tam_cola))
        elif opcion == 3:
            print("Longitud:", longitud_cola(micola, tam_cola))
        elif opcion == 4:
            escribir_cola(micola, tam_cola)
        else:
            print("Opción incorrecta")


if __name__ == "__main__":
    main()
print("Fin")
