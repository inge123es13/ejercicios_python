#La politica de cobro de una compañia telefonica es: cuando se realiza una 
#llamada, el cobro es por el tiempo que asta dura, de tal forma que los primeros 
#cinco minutos cuestan 1 euro, los siguientes tres, 80 centimos,
#los siguientes dos minutos, 70 centimos, y a partir del decimo minuto, 50 centimos.
#Ademas, se carga un impuesto de 3 % cuando es domingo, y si es otro d�a, en turno
#de mañana, 15 %, y en turno de tarde, 10 %. 
#Realice un algoritmo para determinar cuanto debe pagar por cada concepto 
#una persona que realiza una llamada.

print('Llamadas')
tiempo = int(input("¿Cuánto tiempo es la llamada (minutos)?: "))
es_domingo = input("¿Es domingo? (S/N): ").upper()

# Cálculo del coste base en céntimos
if tiempo < 5:
    coste = tiempo * 100
elif tiempo < 8:
    coste = (tiempo - 5) * 80 + 500
elif tiempo < 10:
    coste = (tiempo - 8) * 70 + 240 + 500
else:
    coste = (tiempo - 10) * 50 + 140 + 240 + 500

# Impuestos
if es_domingo == "S":
    coste += coste * 0.03
else:
    turno = input("¿Qué turno? Mañana o Tarde (M/T): ").upper()
    if turno == "M":
        coste += coste * 0.15
    else:
        coste += coste * 0.10

print("El coste de la llamada es:", coste / 100, "euros")

print('Fin')