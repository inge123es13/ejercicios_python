#Pide una cadena y un carácter por teclado (valida que sea un carácter) 
#y muestra cuantas veces aparece el carácter en la cadena.

frase= input('Ingresa una frase:')
letra= input('Ingresa una letra:')
while len(letra) !=1:
    letra = input('Ingresa una letra:')
count = 0
for i in frase:
    if i == letra:
        count += 1

print(f"La letra'{letra}'esta {count} veces en '{frase}'")

print("Fin")
