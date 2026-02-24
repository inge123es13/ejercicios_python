def suma(num1, num2):
    return num1 + num2

result_suma = suma(23, 57)
print(result_suma)

result_suma = suma(12, 5)
print(result_suma)

result_suma = suma(3.25, 4.75)  # corregido
print(result_suma)

def iniciales(name, ape_1, ape_2):
    return name[0] + ape_1[0] + ape_2[0]

curp = iniciales('Francisco', 'Lopez', 'Brioness')
print(curp)

print(iniciales('Ariana', 'Trejo', 'Chivas'))

#fUNCIONES CON PARAMETROS NOMBRADOS
#fUNCIONES CON PARAMETROS POSICIONALES

def super_heroe(name, hero):
    print(name, 'is', hero) 

super_heroe('Tony Stark', 'Ironman')

super_heroe('Peter Parke', 'Spiderman')

super_heroe('Batman', 'Bruce Wayne')

super_heroe(hero='Hulk', name= 'Bruce Banner')

print(iniciales(ape_1='Roggers', name='Steve', ape_2='Chivas'))

#funciones con parametros opcionales
def multiplica(num1,num2 =10):
    return num1 * num2 

print(multiplica(10,24))
print(multiplica(10))
print(multiplica(24))
