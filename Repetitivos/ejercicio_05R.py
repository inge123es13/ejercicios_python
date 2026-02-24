
# Programa que identifica si un carácter es VOCAL o NO VOCAL
# Termina cuando se introduce un espacio

while True:
    car = input("Introduce un carácter (espacio para salir): ")
    
    # Verificar que solo sea un carácter
    if len(car) != 1:
        print("Por favor, introduce solo un carácter.")
        continue
    
    # Si es espacio, termina el programa
    if car == " ":
        print("Programa finalizado.")
        break
    
    # Verificar si es vocal
    if car.upper() in ["A", "E", "I", "O", "U"]:
        print("VOCAL")
    else:
        print("NO VOCAL")
print("Fin")