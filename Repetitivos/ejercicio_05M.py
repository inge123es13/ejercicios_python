#Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
#en caso contrario, el programa termina cuando se introduce un espacio.



car = ""

while car != " ":
    car = input("Introduce un carácter (espacio para salir): ")
    
    # Verificar que solo sea un carácter
    if len(car) != 1:
        print("Por favor, introduce solo un carácter.")
        continue
    
    # Si no es espacio, verificar si es vocal
    if car != " ":
        if car.upper() in ["A", "E", "I", "O", "U"]:
            print("VOCAL")
        else:
            print("NO VOCAL")

print("Programa finalizado.")