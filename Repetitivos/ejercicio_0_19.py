
#Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta 
#que seleccionamos la opción de "Salir".

print('Menú')

opcion = 0

while opcion != 5:
   

    print("Menú de recomendaciones")
    print("   1. Literatura")
    print("   2. Cine")
    print("   3. Música")
    print("   4. Videojuegos")
    print("   5. Salir")

    opcion = int(input("Elija una opción (1-5): "))

    if opcion == 1:
        print("\nLecturas recomendables:")
        print(" + Esperándolo a Tito - Eduardo Sacheri")
        print(" + El juego de Ender - Orson Scott Card")
        print(" + El sueño de los héroes - Adolfo Bioy Casares")

    elif opcion == 2:
        print("\nPelículas recomendables:")
        print(" + Matrix (1999)")
        print(" + El último samurái (2003)")
        print(" + Cars (2006)")

    elif opcion == 3:
        print("\nDiscos recomendables:")
        print(" + Despedazado por mil partes - La Renga")
        print(" + Búfalo - La Mississippi")
        print(" + Gaia - Mägo de Oz")

    elif opcion == 4:
        print("\nVideojuegos clásicos recomendables:")
        print(" + Día del tentáculo")
        print(" + Terminal Velocity")
        print(" + Death Rally")

    elif opcion == 5:
        print("\nGracias, vuelva pronto")

    else:
        print("\nOpción no válida")

    input("\nPresione Enter para continuar...")
print('Fin')