
# Crear un programa que lea los precios de 5 articulos y las cantidades vendidas 
#por una empresa en sus 4 sucursales. Informar:
# * Las cantidades totales de cada articulo.
# * La cantidad de articulos en la sucursal 2.
# * La cantidad del articulo 3 en la sucursal 1.
# * La recaudación total de cada sucursal.
# * La recaudación total de la empresa.
#* La sucursal de mayor recaudación.

Precio = []
Cantidad = []

for i in range(5):
    p = float(input(f"Ingrese Precio Articulo {i+1}: "))
    Precio.append(p)

for i in range(4):
    fila = []
    for j in range(5):
        c = float(input(f"Ingrese Cant. de Articulo {j+1}, en Sucursal {i+1}: "))
        fila.append(c)
    Cantidad.append(fila)

print("Cantidades por artículos:")
for j in range(5):
    suma = Cantidad[0][j] + Cantidad[1][j] + Cantidad[2][j] + Cantidad[3][j]
    print(f"Total articulo {j+1}: {suma}")

Articulos_Sucursal2 = 0
for j in range(5):
    Articulos_Sucursal2 += Cantidad[1][j]
print("Total Sucursal 2:", Articulos_Sucursal2)

print("Sucursal 1, Articulo 3:", Cantidad[0][2])

MayorRec = 0
NumMayor = 0
TotalEmpresa = 0

for i in range(4):
    TotalSucursal = 0
    for j in range(5):
        TotalSucursal += Cantidad[i][j] * Precio[j]
    print(f"Recaudaciones Sucursal {i+1}: {TotalSucursal}")
    if TotalSucursal > MayorRec:
        MayorRec = TotalSucursal
        NumMayor = i + 1
    TotalEmpresa += TotalSucursal

print("Recaudación total de la empresa:", TotalEmpresa)
print("Sucursal de Mayor Recaudación:", NumMayor)
print("Fin")