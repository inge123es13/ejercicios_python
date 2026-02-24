#Algoritmo que pida nÚmeros hasta que se introduzca un cero. Debe imprimir la suma
# y la media de todos los nUmeros introducidos.

print(' Debe imprimir la suma y la media de todos los números introducidos.')

suma = 0
cont = 0

while True:  
    num = int(input("Número (0 para salir): "))
    
    suma += num
    
    
    if num != 0:
        cont += 1
    
    if num == 0:  
        break

if cont != 0:
    media = suma / cont
else:
    media = 0

print("Suma:", suma)
print("Media:", media)

