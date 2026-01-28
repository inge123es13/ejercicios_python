#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a 
#cuantas horas y minutos corresponde.

print ('Cantidad de Minutos, muestra horas y minutos correspondiente')
minutos= int(input("Ingresa la cantidad de minutos: "))
res_horas = (minutos // 60 )
res_min = minutos % 60 
print(f'{res_horas} horas y {res_min} minutos')


