
#Crea una aplicaci�n que pida un n�mero y calcule su factorial (El factorial de 
#un n�mero es el producto de todos los enteros entre 1 y el propio n�mero y se 
#representa por el n�mero seguido de un signo de exclamaci�n. Por ejemplo 5! = 1x2x3x4x5=120)

print('Programa que calcula la Factorial de un número')

numero= int(input('Ingresa un número '))

factorial= 1
for i in range(1,numero + 1): #[1,2,3,4,5]
	factorial=factorial * i 

print('factorial de ', numero , 'es' , factorial)
	