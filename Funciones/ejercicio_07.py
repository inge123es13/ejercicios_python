
#Función Login: Recibe un nombre de usuario y una contraseña, y devuelve un
#valor lógico: verdadero si se ha introducido el nombre y la contraseña adecuadas.
#Además va incrementa el numero de internos que la recibe como parámetro de 
#entrada/salida
#Parámetros de entrada: nombre y contraseña
#Parámetros de entrada y salida: intentos
#Dato devuelto: Valor lógico indicando si ha hecho login


def login(nombre, password, intentos):
    if nombre == "usuario1" and password == "asdasd":
        eslogin = True
    else:
        eslogin = False
        intentos += 1
    return eslogin, intentos


# Programa principal
cuantasveces = 0
entrar = False

while True:
    usuario = input("Usuario: ")
    clave = input("Password: ")

    entrar, cuantasveces = login(usuario, clave, cuantasveces)

    if not entrar:
        print("Error. Nombre de usuario o contraseña incorrecta.")

    if entrar or cuantasveces == 3:
        break

# Resultado final
if entrar:
    print("Bienvenidos al sistema")
else:
    print("No has entrado en el sistema")

print("Fin")