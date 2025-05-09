#4. Solicita el nombre, precio de un producto y un porcentaje de descuento. Muestra el nombre del producto y precio final luego de aplicar el descuento.
nombreproducto = input("Ingrese el nombre del producto: ")
precioproducto = float(input("Ingrese el valor del producto: "))
descuento = int(input("Ingrese el porcentaje de descuento a aplicar: "))
descuentocal = descuento/100
total = precioproducto*descuentocal
totalapagar = precioproducto - total
print(nombreproducto)
print(totalapagar)