producto1 = float(input("Ingrese el valor del primer producto: "))
producto2 = float(input("Ingrese el valor del segundo producto: "))
producto3 = float(input("Ingrese el valor del tercer producto: "))
impuesto = (producto1+producto2+producto3)*1.10 #impuesto aplicado
descuento = (impuesto-((producto1+producto2+producto3)*0.05))
print("El valor de los productos con el impuesto aplicado es: ", impuesto)
print("El valor total de los productos con el descuento es: ", descuento)
