#La asociacion de vinicultores tiene como política fijar un precio inicial 
#al kilo de uva, la cual se clasifica en tipos A y B,  y ademes en tamaños 1 y 2. 
#Cuando se realiza la venta del producto, esta es de un solo tipo y tamaño, 
#se requiere determinar cuanto recibira un productor por la uva que entrega en un 
#embarque, considerando lo siguiente: 
# si es de tipo A, se le cargan 20 centimos al precio inicial cuando es 
# de tamaño 1; y 30 centimos si es de tamaño 2. 
# Si es de tipo B, se rebajan 30 centimos cuando es de tama�o 1, y 50 c�ntimos 
# cuando es de tamaño 2. 
#Realice un algoritmo para determinar la ganancia obtenida.

print('ganancia')

precio_inicial = float(input("Introduce el precio inicial por kilo de la uva (céntimos): "))
kilos = int(input("Introduce cuántos kilos has vendido: "))
tipo = input("Introduce el tipo de la uva (A/B): ").upper()

if tipo != "A" and tipo != "B":
    print("Tipo incorrecto")
else:
    tamano = input("Introduce el tamaño de la uva (1/2): ")

    if tamano != "1" and tamano != "2":
        print("Tamaño incorrecto")
    else:
        if tipo == "A":
            if tamano == "1":
                precio_inicial += 20
            else:
                precio_inicial += 30
        else:  # tipo B
            if tamano == "1":
                precio_inicial -= 20
            else:
                precio_inicial -= 30

        precio_final = precio_inicial * kilos
        print("La ganancia es", precio_final / 100, "euros")
print('Fin')
