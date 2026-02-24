"""
[funcion(parametros)] -> valor de retorno

print(param1, param2, param3, ...) -> void
print ("Hola" ,("Mundo", 35))

input(param1, string) -> string
name= input('Escribe tu nombre: ')

int (param1: string) -> float
num2 = float('3.5')

abs(num: int +/-) -> int +
num3 = abs(-10)
"""
"""
Funciones Python 
def my_function(param1, param2, param3, ...):
	return
my_fuction()
"""
#Funcion sin parametros y sin retorno
# Funcion sin parametros y sin retorno
def say_hello():
    print('say_hello')
    print(type('say_hello'))

def say_hello_by_name(name):
    print('hola', name)

say_hello_by_name('Frank')
say_hello_by_name('Humans')
say_hello_by_name('Inges')

def tabla(num):
    for i in range(10):
        print(num, '*', (i+1), '=', (i + 1) * num)

tabla(5)
tabla(13)
tabla(7)
