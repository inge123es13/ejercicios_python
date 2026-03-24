
# ###############################################################
# Función EsMultiplo: Recibe dos números e indica si el primero
# es múltiplo del segundo.
# Devuelve True si es múltiplo, False en caso contrario.
# ###############################################################

def es_multiplo(num1, num2):
    if num2 == 0:  
        return False
    return num1 % num2 == 0


# ###############################################################
# Programa principal
# ###############################################################

numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))

if es_multiplo(numero1, numero2):
    print(numero1, "es múltiplo de", numero2)
else:
    print(numero1, "no es múltiplo de", numero2)