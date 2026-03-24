"""
strings con python 

"""
name="Francisco"
profession= 'Professon'

gretings= "hello I´m Francisco"
print(gretings)

translate = '"Hello" es "Hola"'
print(translate)

#escapar caracteres con \
#Cambiar el sentido del caracter 
gretings = 'Hello I\´m Francisco'
print(gretings)

menu ='Elige una opcion:\n1,-0p1\n2,-0p2'
print(menu)

#String Formal
message1 = "Hello i´m {} and I´m {} ".format(name,profession)
print(message1)

message2 = ("Hello i´m {name} and I´m {profession}")
print(message2)

# Métodos para string
movie = "Volver al futuro"

print(movie)
print(movie.upper())
print(movie.lower())
print(movie.capitalize())
print(movie.title())
print(movie.split(" "))
print(movie.startswith("V"))
print(movie.endswith("V"))
print('a' in movie)