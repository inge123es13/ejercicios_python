"""
listas
[1,3,5,7,8] 
["a" ,'b','c','d'] 
[True, false , False, True] 
[1,0,'a', True,[1,2]] 
"""
pares = [0,2,4,6,8,10] 
impares =[1,3,5,7,9,11] 
print(type (pares))

print(type (pares[0]))
print(type (pares[2]))
print(type (pares[-1]))

for i in impares:
    print(i)


impares.append(23)#inserta elementos al final
print (impares) 
impares.pop() # esta funcion nos extrae valores 
print (impares) 
impares.reverse() #invierte la lista
print (impares)  
impares.sort() # ordena la lista
print (impares)  
