
#Crear un vector de 5 elementos de cadenas de caracteres, inicializa el vector 
#con datos leídos por el teclado. Copia los elementos del vector en otro vector 
#pero en orden inverso, y muéstralo por la pantalla.

vector1 = []
vector2 = []

tam = 5


for i in range(tam):
    cadena = input(f"Dame la cadena {i+1}: ")
    vector1.append(cadena)

for i in range(tam - 1, -1, -1):
    vector2.append(vector1[i])


for i in range(tam):
    print(f"La cadena {i+1}: {vector2[i]}")

print("Fin")