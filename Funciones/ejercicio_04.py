
#Función ConvetirEspaciado: Recibe una cadena de caracteres, y devuelve otra 
#con los mismos caracteres separados con espacio.
#Parámetros de entrada: Cadena de caracteres
#Dato devuelto: Cadena igual a la anterior pero con espacios entre los 
#caracteres




#Crea un función "ConvertirEspaciado", que reciba como parámetro un texto y 
#devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, 
#"Hola, t" devolver "H o l a , t  ". Crea un programa principal donde se 
#use dicha función.
# Función ConvertirEspaciado: recibe una cadena y devuelve otra
# con un espacio después de cada carácter

def ConvertirEspaciado(cad):
    cad_con_espacios = ""
    
    for i in range(len(cad)):
        cad_con_espacios = cad_con_espacios + cad[i] + " "
    
    return cad_con_espacios



mensaje = input("Introduce una cadena: ")

print("La cadena con espacio:")
print(ConvertirEspaciado(mensaje))

print("Fin")