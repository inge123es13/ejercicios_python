
#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
#el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por 
#las tres ventas que realiza en el mes y el total que recibirá en el mes tomando 
#en cuenta su sueldo base y comisiones.
print ('Calcular Sueldo')
sueldo_base= float(input("Ingresa tu sueldo base :) : "))
venta1= float(input("Ingresa precio de la venta  1 por favor:) : "))
venta2= float(input("Ingresa precio de la venta 2 por favor :) : "))
venta3= float(input("Ingresa precio de la venta 3 por favor :) : "))
comision = (venta1 + venta2 + venta3) * 0.1
print('Comisión por ventas : ',comision)
print('Sueldo total : ', sueldo_base+comision)


