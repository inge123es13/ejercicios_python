#Algoritmo que muestre la tabla de multiplicar de los n�meros 1,2,3,4 y 5.

print(" TablasDeMultiplicar")

for tabla in range(1, 6):          
    print(f"\nTabla del {tabla}")
    
    for num in range(1, 11):       
        print(f"{tabla} * {num} = {tabla * num}")
    
    input("Presiona Enter para continuar...")
print("Fin")
