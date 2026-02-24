#Crea una aplicaci�n que pida un n�mero y calcule su factorial (El factorial de 
#un n�mero es el producto de todos los enteros entre 1 y el propio n�mero y se representa por el n�mero seguido de un signo de exclamaci�n. 
#Por ejemplo 5! = 1x2x3x4x5=120)


print(' Factorial')
	
numero= int(input("Dime un n�mero:"))
	
i = 1
factorial = 1
while i <= numero:
	factorial = factorial * i
	i= i+1
print(' El factorial de ', numero, 'es', factorial)

print(' Fin')