
# ###############################################################
# Función calcular_temperatura_media:
# Recibe dos temperaturas y devuelve la media.
# ###############################################################

def calcular_temperatura_media(temp1, temp2):
    return (temp1 + temp2) / 2


# ###############################################################
# Programa principal
# ###############################################################

cantidad = int(input("¿Cuántas temperaturas vas a calcular?: "))

for indice in range(1, cantidad + 1):
    print(f"\nDía {indice}")
    
    tmin = float(input("Introduce temperatura mínima: "))
    tmax = float(input("Introduce temperatura máxima: "))
    
    media = calcular_temperatura_media(tmin, tmax)
    
    print("Temperatura media:", media)
print("Fin")