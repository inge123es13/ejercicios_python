
#Programa que declare tres vectores 'vector1', 'vector2' y 'vector3' de cinco 
#enteros cada uno, pida valores para 'vector1' y 'vector2' y calcule 
#vector3=vector1+vector2.

vector1 = []
vector2 = []
vector3 = []
tam_vector = 5

for i in range(tam_vector):
    num = int(input(f"Introduce el elemento {i+1} del vector1: "))
    vector1.append(num)

for i in range(tam_vector):
    num = int(input(f"Introduce el elemento {i+1} del vector2: "))
    vector2.append(num)

for i in range(tam_vector):
    vector3.append(vector1[i] + vector2[i])

print("La suma de los vectores es:")
for num in vector3:
    print(num, end=" ")
print("Fin")