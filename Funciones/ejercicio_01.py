
#Procedimiento centrar: Recibe una cadena y la imprime centrada en la pantalla.
#Suponemos que tenemos una pantalla de 80 caracteres de ancho. 
#Para centrar usamos la formula 40 - (Longitud(cad)/2)
#Par�metros de entrada: cadena a imprimir centrada


def centrar(cad)	:
   
    for i in range(40 - (len(cad) //2)):
        print(" ", end = "")
    print(cad)
    for i in range (40 - (len(cad)//2)):
        print("", end = "")

    for i in range (len(cad)):
        print("", end = "")
    print("")



messaje_1 = "Un mensaje centrado"
centrar(messaje_1);
messaje_2 = "Otro mensaje";
centrar(messaje_2);

print("Fin")
