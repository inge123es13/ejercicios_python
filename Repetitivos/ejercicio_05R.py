
#Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
#en caso contrario, el programa termina cuando se introduce un espacio.



print(' VocalConsonante')

while True:
    car = input("Introduce un carácter (espacio para salir): ")
    
    if len(car) != 1:
        print("Debes introducir solo un carácter.")
        continue
    
    if car == " ":
        print("Programa finalizado.")
        break
    
    if car.upper() in ["A", "E", "I", "O", "U"]:
        print("VOCAL")
    else:
        print("NO VOCAL")

print("Fin")

 