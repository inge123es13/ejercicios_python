#Suponiendo que hemos introducido una cadena por teclado que representa una frase 
#(palabras separadas por espacios), realiza un programa que cuente cuantas 
#palabras tiene.

frase = input ('Escribe uan frase:')
words = frase.split (" ")
print(words)
print (f"La frase '{frase}' tiene {len (words) }palabras")

words = []
word = ''

for letra in frase:
    if letra != ' ':
        word += letra
    else:
        words.append(word)
        word = ''

words.append(word)
print("Fin")